"""High-level analysis planner tool."""

from pathlib import Path
from typing import Any

from dd_agent.contracts.specs import HighLevelPlan
from dd_agent.contracts.tool_output import ToolOutput, ToolMessage, err
from dd_agent.llm.structured import build_messages, chat_structured_pydantic
from dd_agent.tools.base import Tool, ToolContext


class HighLevelPlanner(Tool):
    """Tool for generating high-level analysis plans.

    Given a question catalog and optional scope document, this tool
    proposes a comprehensive set of analysis intents that would
    provide valuable insights from the survey data.
    """

    @property
    def name(self) -> str:
        return "high_level_planner"

    @property
    def description(self) -> str:
        return "Generates a high-level analysis plan with intents and suggested segments"

    def run(self, ctx: ToolContext) -> ToolOutput[HighLevelPlan]:
        """Execute the high-level planning tool.

        Args:
            ctx: Tool context with questions and optional scope

        Returns:
            ToolOutput containing a HighLevelPlan or errors
        """
        # Load the high-level planning prompt
        prompt_path = Path(__file__).parent.parent / "llm" / "prompts" / "high_level_plan.md"
        system_prompt = prompt_path.read_text()

        # Build user message with questions and scope context
        user_content = self._build_user_content(ctx)

        # Call LLM with structured output
        messages = build_messages(system_prompt=system_prompt, user_content=user_content)
        plan, trace = chat_structured_pydantic(
            messages=messages,
            model=HighLevelPlan,
        )

        # Validate the plan
        errors = self._validate_plan(plan, ctx)

        # Check if LLM returned errors (when errors exist in the response)
        if hasattr(plan, "__pydantic_extra__") and plan.__pydantic_extra__:
            llm_errors = plan.__pydantic_extra__.get("errors", [])
            if llm_errors:
                # Convert dict errors to ToolMessage objects
                for err_dict in llm_errors:
                    code = err_dict.get("code", "llm_error")
                    message = err_dict.get("message", "Unknown error")
                    context = err_dict.get("context")
                    errors.append(err(code, message, context))

        if errors:
            return ToolOutput.failure(errors=errors, trace=trace)

        return ToolOutput.success(data=plan, trace=trace)

    def _build_user_content(self, ctx: ToolContext) -> str:
        """Build the user message content with questions and scope."""
        lines = ["# Analysis Planning Request\n"]

        # Add scope if provided
        if ctx.scope:
            lines.append(f"## Project Scope\n{ctx.scope}\n")

        lines.append("## Available Questions\n")
        lines.append(ctx.get_questions_summary())

        return "\n".join(lines)

    def _validate_plan(
        self, plan: HighLevelPlan, ctx: ToolContext
    ) -> list[ToolMessage]:
        """Validate the generated plan against available questions."""
        errors = []

        # Validate that intents have unique IDs
        intent_ids = [intent.intent_id for intent in plan.intents]
        if len(intent_ids) != len(set(intent_ids)):
            errors.append(err("duplicate_intent_ids", "Intent IDs must be unique"))

        # Validate priority values
        for intent in plan.intents:
            if intent.priority not in [1, 2, 3]:
                errors.append(
                    err(
                        "invalid_priority",
                        f"Intent {intent.intent_id} has invalid priority {intent.priority}. Must be 1, 2, or 3.",
                    )
                )

        # Validate suggested segments if any
        for segment in plan.suggested_segments:
            # Import here to avoid circular dependency
            from dd_agent.contracts.validate import validate_segment_spec
            segment_errors = validate_segment_spec(segment, ctx.questions_by_id)
            errors.extend(segment_errors)

        return errors
