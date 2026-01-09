"""Diagnostics and debugging utilities for grounding."""

import json
from typing import Any

from dd_agent.contracts.questions import Question
from dd_agent.util.grounding import (
    ground_option_with_diagnostics,
    ground_questions_with_diagnostics,
)


class GroundingDiagnostics:
    """Utility for diagnosing and debugging grounding issues."""

    @staticmethod
    def analyze_question_grounding(
        search_terms: list[str],
        questions: list[Question],
    ) -> dict[str, Any]:
        """
        Analyze how well search terms ground to questions.

        Args:
            search_terms: List of search terms to analyze
            questions: Available questions

        Returns:
            Dictionary with grounding analysis results
        """
        results = ground_questions_with_diagnostics(search_terms, questions)

        found_count = sum(1 for r in results.values() if r["found"])
        total_count = len(results)

        return {
            "summary": {
                "total_terms": total_count,
                "successfully_grounded": found_count,
                "failed": total_count - found_count,
                "success_rate": round((found_count / total_count * 100) if total_count > 0 else 0, 1),
            },
            "details": results,
        }

    @staticmethod
    def analyze_option_grounding(
        search_terms: list[str],
        question: Question,
    ) -> dict[str, Any]:
        """
        Analyze how well search terms ground to options in a question.

        Args:
            search_terms: List of search terms to analyze
            question: The question to search within

        Returns:
            Dictionary with grounding analysis results
        """
        results = {}

        for term in search_terms:
            results[term] = ground_option_with_diagnostics(term, question)

        found_count = sum(1 for r in results.values() if r["found"])
        total_count = len(results)

        return {
            "summary": {
                "question_id": question.question_id,
                "question_label": question.label,
                "total_terms": total_count,
                "successfully_grounded": found_count,
                "failed": total_count - found_count,
                "success_rate": round((found_count / total_count * 100) if total_count > 0 else 0, 1),
            },
            "details": results,
        }

    @staticmethod
    def print_grounding_report(
        analysis: dict[str, Any],
        title: str = "Grounding Analysis Report",
    ) -> str:
        """
        Generate a human-readable report from grounding analysis.

        Args:
            analysis: Results from analyze_question_grounding or analyze_option_grounding
            title: Title for the report

        Returns:
            Formatted report string
        """
        report_lines = [
            f"\n{'=' * 60}",
            f"{title:^60}",
            f"{'=' * 60}\n",
        ]

        summary = analysis.get("summary", {})
        report_lines.append("SUMMARY")
        report_lines.append("-" * 40)

        for key, value in summary.items():
            if key != "question_id":  # Skip some internal keys
                formatted_key = key.replace("_", " ").title()
                report_lines.append(f"  {formatted_key}: {value}")

        report_lines.append("\n")

        details = analysis.get("details", {})
        if details:
            report_lines.append("DETAILED RESULTS")
            report_lines.append("-" * 40)

            for term, result in details.items():
                status = "✓ FOUND" if result.get("found") else "✗ NOT FOUND"
                report_lines.append(f"\n  Term: '{term}' [{status}]")

                if result.get("found"):
                    question_id = result.get("question_id") or result.get("option_code")
                    label = result.get("label") or result.get("option_label")
                    report_lines.append(f"    ID: {question_id}")
                    if label:
                        report_lines.append(f"    Label: {label}")
                else:
                    if "error" in result:
                        report_lines.append(f"    Error: {result['error']}")

                    similar = result.get("similar_questions") or result.get("similar_options", [])
                    if similar:
                        report_lines.append(f"    Similar candidates:")
                        for candidate in similar:
                            similarity = candidate.get("similarity", "?")
                            cand_id = candidate.get("id") or candidate.get("code")
                            cand_label = candidate.get("label")
                            report_lines.append(
                                f"      - [{similarity}] {cand_id}: {cand_label}"
                            )

        report_lines.append(f"\n{'=' * 60}\n")

        return "\n".join(report_lines)

    @staticmethod
    def export_grounding_analysis(
        analysis: dict[str, Any],
        output_path: str,
    ) -> None:
        """
        Export grounding analysis to JSON file.

        Args:
            analysis: Results from analyze_question_grounding or analyze_option_grounding
            output_path: Path to save the JSON file
        """
        with open(output_path, "w") as f:
            json.dump(analysis, f, indent=2)
