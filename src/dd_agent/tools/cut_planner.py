"""Cut planner tool for converting NL requests to CutSpecs."""

from typing import Any, Optional

from pydantic import BaseModel, Field

from dd_agent.contracts.specs import CutSpec
from dd_agent.contracts.tool_output import ToolOutput, err
from dd_agent.contracts.validate import validate_cut_spec
from dd_agent.llm.structured import build_messages, chat_structured_pydantic
from dd_agent.tools.base import Tool, ToolContext


class CutPlanResult(BaseModel):
    """Result of the cut planner tool."""

    ok: bool = Field(..., description="Whether planning succeeded")
    cut: Optional[CutSpec] = Field(default=None, description="The planned cut specification")
    resolution_map: dict[str, str] = Field(
        default_factory=dict,
        description="Mapping of NL terms to question/segment IDs",
    )
    ambiguity_options: list[str] = Field(
        default_factory=list,
        description="Possible interpretations if ambiguous",
    )
    errors: list[dict[str, Any]] = Field(
        default_factory=list, description="Any errors from the LLM"
    )


class CutPlanner(Tool):
    """Tool for converting natural language requests to CutSpecs.

    Takes a natural language analysis request (e.g., "Show NPS by region")
    and produces a validated CutSpec that can be executed deterministically.
    """

    @property
    def name(self) -> str:
        return "cut_planner"

    @property
    def description(self) -> str:
        return "Converts natural language analysis requests to executable CutSpecs"

    def run(self, ctx: ToolContext) -> ToolOutput[CutSpec]:
        """Execute the cut planner tool.

        Args:
            ctx: Tool context with questions, segments, and the prompt

        Returns:
            ToolOutput containing a validated CutSpec or errors
        """
        if not ctx.prompt:
            return ToolOutput.failure(
                errors=[err("missing_prompt", "No analysis request provided")]
            )

        # Build the prompt with context
        user_content = self._build_user_content(ctx)

        # Load the system prompt
        from pathlib import Path

        prompt_path = Path(__file__).parent.parent / "llm" / "prompts" / "cut_plan.md"
        system_prompt = prompt_path.read_text()

        # Build messages
        messages = build_messages(system_prompt=system_prompt, user_content=user_content)

        # Call LLM with structured output
        try:
            result, llm_trace = chat_structured_pydantic(messages=messages, model=CutPlanResult)
        except Exception as e:
            return ToolOutput.failure(errors=[err("llm_error", f"LLM call failed: {str(e)}")])

        # If the LLM indicated ambiguity or failure
        if not result.ok:
            # Convert LLM errors (dicts) to ToolMessage objects
            llm_errors = []
            if result.errors:
                for error in result.errors:
                    if isinstance(error, dict):
                        llm_errors.append(
                            err(
                                error.get("code", "llm_error"),
                                error.get("message", "Unknown error"),
                                **error.get("context", {}),
                            )
                        )
                    else:
                        llm_errors.append(error)

            return ToolOutput.failure(
                errors=llm_errors or [err("ambiguous", "Request is ambiguous")],
                trace={
                    "llm": llm_trace,
                    "ambiguity_options": result.ambiguity_options,
                    "resolution_map": result.resolution_map,
                },
            )

        # Validate the cut spec
        if not result.cut:
            return ToolOutput.failure(
                errors=[err("missing_cut", "LLM did not provide a cut specification")]
            )

        # Validate against the question catalog and segments
        validation_errors = validate_cut_spec(
            cut=result.cut, questions_by_id=ctx.questions_by_id, segments_by_id=ctx.segments_by_id
        )

        if validation_errors:
            return ToolOutput.failure(
                errors=validation_errors,
                trace={
                    "llm": llm_trace,
                    "resolution_map": result.resolution_map,
                },
            )

        # Success!
        return ToolOutput.success(
            data=result.cut,
            trace={
                "llm": llm_trace,
                "resolution_map": result.resolution_map,
            },
        )

    def _build_user_content(self, ctx: ToolContext) -> str:
        """Build the user message content."""
        parts = [
            f"## Analysis Request\n{ctx.prompt}\n",
            f"## Available Questions\n{ctx.get_questions_summary()}\n",
        ]

        if ctx.segments:
            parts.append(f"## Available Segments\n{ctx.get_segments_summary()}\n")

        return "\n".join(parts)
