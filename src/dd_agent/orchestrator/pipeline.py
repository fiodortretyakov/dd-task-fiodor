"""Pipeline for running analysis flows."""

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

import pandas as pd

from dd_agent.contracts.questions import Question
from dd_agent.contracts.specs import CutSpec, HighLevelPlan, SegmentSpec
from dd_agent.contracts.tool_output import ToolOutput
from dd_agent.engine.executor import ExecutionResult
from dd_agent.orchestrator.agent import Agent
from dd_agent.run_store import RunStore
from dd_agent.tools.base import ToolContext
from dd_agent.util.logging import get_logger

logger = get_logger("pipeline")


@dataclass
class PipelineResult:
    """Result of a pipeline execution."""

    success: bool
    run_id: str
    run_dir: Path
    plan: Optional[HighLevelPlan] = None
    cuts_planned: list[CutSpec] = field(default_factory=list)
    cuts_failed: list[dict[str, Any]] = field(default_factory=list)
    execution_result: Optional[ExecutionResult] = None
    errors: list[str] = field(default_factory=list)


class Pipeline:
    """Pipeline for running analysis flows.

    Provides two main flows:
    1. run_single: Execute a single analysis request
    2. run_autoplan: Generate and execute a full analysis plan
    """

    def __init__(
        self,
        data_dir: Path,
        runs_dir: Optional[Path] = None,
        interactive: bool = True,
    ):
        """Initialize the pipeline.

        Args:
            data_dir: Directory containing questions.json, responses.csv, scope.md
            runs_dir: Directory for saving run artifacts (defaults to data_dir/runs)
            interactive: Enable interactive ambiguity resolution (default: True)
        """
        self.data_dir = Path(data_dir)
        self.runs_dir = runs_dir or self.data_dir / "runs"
        self.interactive = interactive

        # Load data
        self.questions = self._load_questions()
        self.responses_df = self._load_responses()
        self.scope = self._load_scope()

        # Create agent
        self.agent = Agent(
            questions=self.questions,
            responses_df=self.responses_df,
            scope=self.scope,
            data_dir=self.data_dir,
            interactive=self.interactive,
        )

    def _load_questions(self) -> list[Question]:
        """Load questions from questions.json."""
        questions_path = self.data_dir / "questions.json"
        if not questions_path.exists():
            raise FileNotFoundError(f"Questions file not found: {questions_path}")

        with open(questions_path) as f:
            data = json.load(f)

        # Handle both list and dict formats
        if isinstance(data, list):
            return [Question.model_validate(q) for q in data]
        elif isinstance(data, dict) and "questions" in data:
            return [Question.model_validate(q) for q in data["questions"]]
        else:
            raise ValueError("Invalid questions.json format")

    def _load_responses(self) -> pd.DataFrame:
        """Load responses from responses.csv."""
        responses_path = self.data_dir / "responses.csv"
        if not responses_path.exists():
            raise FileNotFoundError(f"Responses file not found: {responses_path}")

        return pd.read_csv(responses_path)

    def _load_scope(self) -> Optional[str]:
        """Load scope from scope.md if it exists."""
        scope_path = self.data_dir / "scope.md"
        if scope_path.exists():
            return scope_path.read_text()
        return None

    def run_single(
        self,
        prompt: str,
        save_run: bool = True,
    ) -> PipelineResult:
        """Execute a single analysis request.

        Args:
            prompt: Natural language analysis request
            save_run: Whether to save run artifacts

        Returns:
            PipelineResult with execution details
        """
        run_store = RunStore(self.runs_dir)
        run_store.new_run(prompt=prompt)
        run_store.compute_dataset_hash(
            self.data_dir / "questions.json",
            self.data_dir / "responses.csv",
            self.data_dir / "scope.md" if (self.data_dir / "scope.md").exists() else None,
        )

        result = PipelineResult(
            success=False,
            run_id=run_store.run_id or "unknown",
            run_dir=run_store.run_dir or Path(),
        )

        try:
            # Save inputs
            run_store.save_input("questions.json", self.data_dir / "questions.json")
            run_store.save_input("responses.csv", self.data_dir / "responses.csv")
            if self.scope:
                run_store.save_input_text("scope.md", self.scope)
            run_store.save_input_text("user_prompt.txt", prompt)

            # Plan the cut
            cut_output = self.agent.plan_cut(prompt)
            if not cut_output.ok or cut_output.data is None:
                result.errors = [str(e) for e in (cut_output.errors or [])]
                return result

            cut_spec = cut_output.data
            result.cuts_planned.append(cut_spec)

            # Save plan and trace
            run_store.save_artifact(
                "cut_spec.json",
                cut_spec.model_dump(exclude_none=True)
            )
            if cut_output.trace:
                run_store.save_artifact("trace.json", cut_output.trace)

            # Execute the cut
            exec_result = self.agent.execute_cuts([cut_spec])
            result.execution_result = exec_result

            # Save results
            if exec_result.tables:
                for table in exec_result.tables:
                    # Save each table as CSV
                    df = table.get_dataframe()
                    if df is not None and run_store.artifacts_dir is not None:
                        csv_path = run_store.artifacts_dir / f"{table.cut_id}.csv"
                        df.to_csv(csv_path, index=False)

                # Save results JSON
                results_data = {
                    "tables": [
                        {
                            "cut_id": t.cut_id,
                            "metric_type": t.metric_type,
                            "question_id": t.question_id,
                            "base_n": t.base_n,
                            "warnings": t.warnings or [],
                        }
                        for t in exec_result.tables
                    ],
                    "errors": exec_result.errors,
                }
                run_store.save_artifact("results.json", results_data)

            result.success = len(exec_result.errors) == 0
            run_store.save_report(result)

        except Exception as e:
            result.errors.append(str(e))
            logger.error(f"Pipeline error: {e}", exc_info=True)

        return result

    def run_autoplan(
        self,
        save_run: bool = True,
        max_cuts: int = 20,
    ) -> PipelineResult:
        """Generate and execute a full analysis plan.

        Args:
            save_run: Whether to save run artifacts
            max_cuts: Maximum number of cuts to execute

        Returns:
            PipelineResult with execution details
        """
        run_store = RunStore(self.runs_dir)
        run_store.new_run(prompt="autoplan")
        run_store.compute_dataset_hash(
            self.data_dir / "questions.json",
            self.data_dir / "responses.csv",
            self.data_dir / "scope.md" if (self.data_dir / "scope.md").exists() else None,
        )

        result = PipelineResult(
            success=False,
            run_id=run_store.run_id or "unknown",
            run_dir=run_store.run_dir or Path(),
        )

        try:
            # Save inputs
            run_store.save_input("questions.json", self.data_dir / "questions.json")
            run_store.save_input("responses.csv", self.data_dir / "responses.csv")
            if self.scope:
                run_store.save_input_text("scope.md", self.scope)

            # Generate high-level plan
            plan_output = self.agent.high_level_planner.run(
                ToolContext(
                    questions=self.agent.questions,
                    questions_by_id=self.agent.questions_by_id,
                    scope=self.agent.scope,
                    responses_df=self.agent.responses_df,
                    data_dir=self.agent.data_dir,
                )
            )

            if not plan_output.ok or plan_output.data is None:
                result.errors = [str(e) for e in (plan_output.errors or [])]
                return result

            plan = plan_output.data
            result.plan = plan

            # Save plan
            run_store.save_artifact("high_level_plan.json", plan.model_dump(exclude_none=True))
            if plan_output.trace:
                run_store.save_artifact("plan_trace.json", plan_output.trace)

            # Add suggested segments
            for segment in plan.suggested_segments:
                self.agent.add_segment(segment)

            if plan.suggested_segments:
                run_store.save_artifact(
                    "segments.json",
                    [s.model_dump(exclude_none=True) for s in plan.suggested_segments]
                )

            # Plan and execute cuts for each intent
            all_cuts = []
            for i, intent in enumerate(plan.intents[:max_cuts]):
                # Create a cut request based on intent
                cut_output = self.agent.plan_cut(intent.description)

                if not cut_output.ok or cut_output.data is None:
                    result.cuts_failed.append({
                        "intent_id": intent.intent_id,
                        "description": intent.description,
                        "error": str(cut_output.errors[0]) if cut_output.errors else "Unknown error"
                    })
                    continue

                cut_spec = cut_output.data
                all_cuts.append(cut_spec)
                result.cuts_planned.append(cut_spec)

            # Save cuts
            if all_cuts:
                run_store.save_artifact(
                    "cuts.json",
                    [c.model_dump(exclude_none=True) for c in all_cuts]
                )

            # Execute all cuts
            if all_cuts:
                exec_result = self.agent.execute_cuts(all_cuts)
                result.execution_result = exec_result

                # Save results
                if exec_result.tables:
                    results_data = {
                        "tables": [
                            {
                                "cut_id": t.cut_id,
                                "metric_type": t.metric_type,
                                "question_id": t.question_id,
                                "base_n": t.base_n,
                                "dimensions": t.dimensions or [],
                                "warnings": t.warnings or [],
                            }
                            for t in exec_result.tables
                        ],
                        "errors": exec_result.errors,
                    }
                    run_store.save_artifact("results.json", results_data)

                    # Save each table as CSV
                    for table in exec_result.tables:
                        df = table.get_dataframe()
                        if df is not None and run_store.artifacts_dir is not None:
                            csv_path = run_store.artifacts_dir / f"{table.cut_id}.csv"
                            df.to_csv(csv_path, index=False)

            result.success = len(result.cuts_failed) == 0 and (
                result.execution_result is None or len(result.execution_result.errors) == 0
            )
            run_store.save_report(result)

        except Exception as e:
            result.errors.append(str(e))
            logger.error(f"Pipeline error: {e}", exc_info=True)

        return result
