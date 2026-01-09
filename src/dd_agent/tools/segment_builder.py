"""Segment builder tool for converting NL definitions to SegmentSpecs."""

from pathlib import Path
from typing import Any, Optional

from pydantic import BaseModel, Field

from dd_agent.contracts.specs import SegmentSpec
from dd_agent.contracts.tool_output import ToolOutput, err
from dd_agent.contracts.validate import validate_segment_spec
from dd_agent.llm.structured import build_messages, chat_structured_pydantic
from dd_agent.tools.base import Tool, ToolContext


class SegmentBuilderResult(BaseModel):
    """Result of the segment builder tool."""

    ok: bool = Field(..., description="Whether building succeeded")
    segment: Optional[SegmentSpec] = Field(
        default=None, description="The built segment specification"
    )
    errors: list[dict[str, Any]] = Field(
        default_factory=list, description="Any errors from the LLM"
    )


class SegmentBuilder(Tool):
    """Tool for converting natural language segment definitions to SegmentSpecs.

    Takes a natural language segment description (e.g., "Young professionals
    aged 25-34 in urban areas") and produces a validated SegmentSpec with
    a filter expression.
    """

    @property
    def name(self) -> str:
        return "segment_builder"

    @property
    def description(self) -> str:
        return "Converts natural language segment definitions to executable SegmentSpecs"

    def run(self, ctx: ToolContext) -> ToolOutput[SegmentSpec]:
        """Execute the segment builder tool.

        Args:
            ctx: Tool context with questions and the segment definition prompt

        Returns:
            ToolOutput containing a validated SegmentSpec or errors
        """
        if not ctx.prompt:
            return ToolOutput.failure(
                errors=[err("missing_prompt", "No segment definition provided")]
            )

        # Load the segment planning prompt
        prompt_path = Path(__file__).parent.parent / "llm" / "prompts" / "segment_plan.md"
        system_prompt = prompt_path.read_text()

        # Build user message with questions context
        user_content = self._build_user_content(ctx)

        # Call LLM with structured output
        messages = build_messages(system_prompt=system_prompt, user_content=user_content)

        try:
            result, trace = chat_structured_pydantic(
                messages=messages,
                model=SegmentBuilderResult,
            )
        except Exception as e:
            return ToolOutput.failure(
                errors=[err("llm_error", f"LLM call failed: {str(e)}")]
            )

        # If the LLM indicated failure
        if not result.ok:
            llm_errors = []
            if result.errors:
                for error in result.errors:
                    if isinstance(error, dict):
                        llm_errors.append(err(
                            error.get("code", "llm_error"),
                            error.get("message", "Unknown error"),
                            **error.get("context", {})
                        ))
                    else:
                        llm_errors.append(error)

            return ToolOutput.failure(
                errors=llm_errors or [err("unmappable", "Request could not be mapped to available questions")],
                trace=trace
            )

        # Validate the segment spec
        if not result.segment:
            return ToolOutput.failure(
                errors=[err("missing_segment", "LLM did not provide a segment specification")]
            )

        # Validate against questions catalog
        errors = validate_segment_spec(result.segment, ctx.questions_by_id)

        if errors:
            return ToolOutput.failure(errors=errors, trace=trace)

        return ToolOutput.success(data=result.segment, trace=trace)

    def _build_user_content(self, ctx: ToolContext) -> str:
        """Build the user message content with questions and segment description."""
        lines = ["# Segment Definition Request\n"]
        lines.append(f"**Segment Description:** {ctx.prompt}\n")
        lines.append("## Available Questions\n")

        for q in ctx.questions:
            lines.append(f"- **{q.question_id}** ({q.type.value}): {q.label}")
            if q.options:
                options_str = ", ".join([f"{opt.code}: {opt.label}" for opt in q.options])
                lines.append(f"  - Options: {options_str}")

        return "\n".join(lines)
