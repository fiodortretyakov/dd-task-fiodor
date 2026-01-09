"""Statistical comparison tool for analyzing differences between groups."""

import numpy as np
import pandas as pd
from typing import Optional, Dict, Any, Tuple
from dataclasses import dataclass

from dd_agent.engine.statistics import (
    ttest_independent,
    cohens_d,
    calculate_confidence_interval,
    is_statistically_significant,
)


@dataclass
class ComparisonResult:
    """Result of statistical comparison between two groups."""

    group1_name: str
    group2_name: str
    group1_mean: float
    group2_mean: float
    group1_n: int
    group2_n: int
    difference: float
    t_statistic: float
    p_value: float
    effect_size: float
    significant: bool
    group1_ci: Tuple[float, float]
    group2_ci: Tuple[float, float]

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "group1_name": self.group1_name,
            "group2_name": self.group2_name,
            "group1_mean": self.group1_mean,
            "group2_mean": self.group2_mean,
            "group1_n": self.group1_n,
            "group2_n": self.group2_n,
            "difference": self.difference,
            "t_statistic": self.t_statistic,
            "p_value": self.p_value,
            "effect_size": self.effect_size,
            "significant": self.significant,
            "group1_ci": self.group1_ci,
            "group2_ci": self.group2_ci,
        }

    def to_report(self) -> str:
        """Generate human-readable report."""
        sig_mark = "***" if self.significant else ""
        lines = [
            f"Comparison: {self.group1_name} vs {self.group2_name}",
            f"",
            f"{self.group1_name}:",
            f"  Mean: {self.group1_mean:.3f}",
            f"  95% CI: [{self.group1_ci[0]:.3f}, {self.group1_ci[1]:.3f}]",
            f"  N: {self.group1_n}",
            f"",
            f"{self.group2_name}:",
            f"  Mean: {self.group2_mean:.3f}",
            f"  95% CI: [{self.group2_ci[0]:.3f}, {self.group2_ci[1]:.3f}]",
            f"  N: {self.group2_n}",
            f"",
            f"Difference: {self.difference:.3f}",
            f"t-statistic: {self.t_statistic:.3f}",
            f"p-value: {self.p_value:.4f} {sig_mark}",
            f"Cohen's d: {self.effect_size:.3f}",
            f"Significant (α=0.05): {self.significant}",
        ]
        return "\n".join(lines)


class StatisticalComparison:
    """Tool for comparing values between groups."""

    @staticmethod
    def compare_groups(
        group1_values: np.ndarray,
        group2_values: np.ndarray,
        group1_name: str = "Group 1",
        group2_name: str = "Group 2",
    ) -> ComparisonResult:
        """
        Compare two groups of numeric values.

        Args:
            group1_values: Array of values for group 1
            group2_values: Array of values for group 2
            group1_name: Name for group 1
            group2_name: Name for group 2

        Returns:
            ComparisonResult with statistical analysis
        """
        group1_mean = np.mean(group1_values)
        group2_mean = np.mean(group2_values)
        difference = group1_mean - group2_mean

        t_stat, p_value = ttest_independent(group1_values, group2_values)
        effect_size = cohens_d(group1_values, group2_values)

        group1_ci = calculate_confidence_interval(group1_values)
        group2_ci = calculate_confidence_interval(group2_values)

        significant = is_statistically_significant(p_value)

        return ComparisonResult(
            group1_name=group1_name,
            group2_name=group2_name,
            group1_mean=group1_mean,
            group2_mean=group2_mean,
            group1_n=len(group1_values),
            group2_n=len(group2_values),
            difference=difference,
            t_statistic=t_stat,
            p_value=p_value,
            effect_size=effect_size,
            significant=bool(significant),
            group1_ci=group1_ci,
            group2_ci=group2_ci,
        )

    @staticmethod
    def compare_by_dimension(
        df: pd.DataFrame,
        value_column: str,
        dimension_column: str,
    ) -> Dict[Tuple[str, str], ComparisonResult]:
        """
        Compare all pairs of groups in a dimension.

        Args:
            df: DataFrame with data
            value_column: Name of column with numeric values
            dimension_column: Name of column with group labels

        Returns:
            Dictionary mapping (group1, group2) tuples to ComparisonResult
        """
        results = {}
        groups = df[dimension_column].unique()

        for i, group1 in enumerate(groups):
            for group2 in groups[i + 1 :]:
                values1 = df[df[dimension_column] == group1][value_column].dropna().values
                values2 = df[df[dimension_column] == group2][value_column].dropna().values

                if len(values1) > 0 and len(values2) > 0:
                    result = StatisticalComparison.compare_groups(
                        values1,
                        values2,
                        group1_name=str(group1),
                        group2_name=str(group2),
                    )
                    results[(str(group1), str(group2))] = result

        return results

    @staticmethod
    def bonferroni_correction(
        p_values: list[float],
        num_comparisons: Optional[int] = None,
    ) -> list[float]:
        """
        Apply Bonferroni correction to p-values.

        Args:
            p_values: List of p-values
            num_comparisons: Number of comparisons (defaults to len(p_values))

        Returns:
            Corrected p-values (capped at 1.0)
        """
        if num_comparisons is None:
            num_comparisons = len(p_values)

        return [min(p * num_comparisons, 1.0) for p in p_values]
