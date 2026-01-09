"""Debug cut planner with a simple test."""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent / "src"))

from dd_agent.tools.cut_planner import CutPlanner
from dd_agent.tools.base import ToolContext
from dd_agent.contracts.questions import Question, QuestionType, Option

# Create sample questions
questions = [
    Question(
        question_id="Q_GENDER",
        label="What is your gender?",
        type=QuestionType.single_choice,
        options=[
            Option(code="M", label="Male"),
            Option(code="F", label="Female"),
            Option(code="O", label="Other"),
        ]
    ),
    Question(
        question_id="Q_AGE",
        label="What is your age?",
        type=QuestionType.numeric,
    ),
]

# Test the planner
planner = CutPlanner()
ctx = ToolContext(
    questions=questions,
    prompt="Frequency of gender",
)

result = planner.run(ctx)

print("\n=== CUT PLANNER RESULT ===")
print(f"OK: {result.ok}")
if result.ok:
    print(f"Cut ID: {result.data.cut_id}")
    print(f"Metric: {result.data.metric}")
    print(f"Trace: {result.trace}")
else:
    print(f"Errors: {result.errors}")
    print(f"Trace: {result.trace}")
