"""Segment builder tool for converting NL definitions to SegmentSpecs."""

from pathlib import Path

from dd_agent.contracts.specs import SegmentSpec
from dd_agent.contracts.tool_output import ToolOutput, ToolMessage, err
from dd_agent.contracts.validate import validate_segment_spec
from dd_agent.llm.structured import build_messages, chat_structured_pydantic
from dd_agent.tools.base import Tool, ToolContext


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
        segment_spec, trace = chat_structured_pydantic(
            messages=messages,
            response_model=SegmentSpec,
        )

        # Validate the segment spec against questions catalog
        errors = validate_segment_spec(segment_spec, ctx.questions_by_id)

        # Check if LLM returned errors (when errors exist in the response)
        if hasattr(segment_spec, "__pydantic_extra__") and segment_spec.__pydantic_extra__:
            llm_errors = segment_spec.__pydantic_extra__.get("errors", [])
            if llm_errors:
                # Convert dict errors to ToolMessage objects
                for err_dict in llm_errors:
                    code = err_dict.get("code", "llm_error")
                    message = err_dict.get("message", "Unknown error")
                    context = err_dict.get("context")
                    errors.append(err(code, message, context))

        if errors:
            return ToolOutput.failure(errors=errors, trace=trace)

        return ToolOutput.success(data=segment_spec, trace=trace)

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
