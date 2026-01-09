#!/usr/bin/env python3
"""Demo script showing improved grounding with diagnostics."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from dd_agent.contracts.questions import Question
from dd_agent.util.grounding import find_matching_questions
from dd_agent.util.grounding_diagnostics import GroundingDiagnostics

# Load questions
demo_dir = Path(__file__).parent / "data/demo"
questions = [Question(**q) for q in json.load(open(demo_dir / "questions.json"))]

print("\n" + "=" * 70)
print("IMPROVED GROUNDING DEMONSTRATION")
print("=" * 70)

# Test case 1: Exact match
print("\n[Test 1] Exact match: 'Income'")
result = find_matching_questions("Income", questions, interactive=False)
print(f"  Result: {result.question_id if result else 'No match'} - {result.label if result else 'N/A'}")

# Test case 2: Fuzzy match
print("\n[Test 2] Fuzzy match: 'Support' (partial)")
result = find_matching_questions("Support", questions, interactive=False)
print(f"  Result: {result.question_id if result else 'No match'} - {result.label if result else 'N/A'}")

# Test case 3: Partial match
print("\n[Test 3] Partial match: 'Feat' (prefix)")
result = find_matching_questions("Feat", questions, interactive=False)
print(f"  Result: {result.question_id if result else 'No match'} - {result.label if result else 'N/A'}")

# Test case 4: Ambiguous match (should fail gracefully)
print("\n[Test 4] Ambiguous: 'Plan' (matches multiple)")
try:
    result = find_matching_questions("Plan", questions, interactive=False)
    print(f"  Result: {result.question_id if result else 'No match'}")
except Exception as e:
    print(f"  Correctly handled ambiguity: {type(e).__name__}")
    print(f"    Message: {str(e)}")

# Test case 5: No match
print("\n[Test 5] No match: 'xyzabc123'")
result = find_matching_questions("xyzabc123", questions, interactive=False)
print(f"  Result: {result.question_id if result else 'No match'}")

# Diagnostic analysis
print("\n" + "=" * 70)
print("GROUNDING DIAGNOSTICS ANALYSIS")
print("=" * 70)

test_terms = [
    "Income",
    "Support",  # Should match "Support Satisfaction"
    "Features",
    "Region",
    "Gender",  # Should match exactly
    "Tenure",  # Should match exactly or via fuzzy
]

analysis = GroundingDiagnostics.analyze_question_grounding(test_terms, questions)
report = GroundingDiagnostics.print_grounding_report(
    analysis, "Test Term Grounding Analysis"
)
print(report)

print("=" * 70)
print("✓ Improved grounding supports:")
print("  - Exact ID and label matches")
print("  - Prefix and substring matching")
print("  - Fuzzy matching with configurable threshold")
print("  - Clear error messages and suggestions for failures")
print("=" * 70 + "\n")
