"""Enhanced table results with statistical annotations."""

import pandas as pd
from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from dd_agent.engine.statistics import (
    calculate_confidence_interval,
    calculate_proportion_ci,
    is_statistically_significant,
)


@dataclass
class StatisticalAnnotation:
    """Statistical annotation for a value."""

    value: float
    lower_ci: Optional[float] = None
    upper_ci: Optional[float] = None
    p_value: Optional[float] = None
    effect_size: Optional[float] = None
    significant: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "value": self.value,
            "lower_ci": self.lower_ci,
            "upper_ci": self.upper_ci,
            "p_value": self.p_value,
            "effect_size": self.effect_size,
            "significant": self.significant,
        }

    def to_string(self, include_ci: bool = True, include_p: bool = True) -> str:
        """
        Format annotation as human-readable string.

        Args:
            include_ci: Include confidence interval
            include_p: Include p-value

        Returns:
            Formatted string representation
        """
        parts = [f"{self.value:.2f}"]

        if include_ci and self.lower_ci is not None and self.upper_ci is not None:
            parts.append(f"[{self.lower_ci:.2f}, {self.upper_ci:.2f}]")

        if include_p and self.p_value is not None:
            sig_mark = "*" if self.significant else ""
            parts.append(f"p={self.p_value:.4f}{sig_mark}")

        if self.effect_size is not None:
            parts.append(f"d={self.effect_size:.2f}")

        return " ".join(parts)


class StatisticalTable:
    """Enhanced table with statistical annotations."""

    def __init__(
        self,
        data: pd.DataFrame,
        base_n: int,
        metric: str,
        dimensions: Optional[list[str]] = None,
        statistics: Optional[Dict[str, StatisticalAnnotation]] = None,
    ):
        """
        Initialize statistical table.

        Args:
            data: Main data table
            base_n: Base number of respondents
            metric: Metric name
            dimensions: List of dimension column names
            statistics: Dict mapping column names to StatisticalAnnotation objects
        """
        self.data = data
        self.base_n = base_n
        self.metric = metric
        self.dimensions = dimensions or []
        self.statistics = statistics or {}

    def add_statistic(
        self,
        column: str,
        annotation: StatisticalAnnotation,
    ) -> None:
        """Add or update a statistical annotation for a column."""
        self.statistics[column] = annotation

    def to_dataframe_with_annotations(
        self,
        include_ci: bool = True,
        include_p: bool = True,
    ) -> pd.DataFrame:
        """
        Export table as DataFrame with statistical annotations in column names or separate columns.

        Args:
            include_ci: Include confidence intervals
            include_p: Include p-values

        Returns:
            DataFrame with annotations
        """
        result = self.data.copy()

        for col, annotation in self.statistics.items():
            if col in result.columns:
                # Create annotated version as separate column
                result[f"{col}_annotated"] = annotation.to_string(
                    include_ci=include_ci,
                    include_p=include_p,
                )

        return result

    def to_json(self, include_statistics: bool = True) -> Dict[str, Any]:
        """
        Export table as JSON.

        Args:
            include_statistics: Include statistical annotations

        Returns:
            Dictionary suitable for JSON serialization
        """
        result = {
            "metric": self.metric,
            "base_n": self.base_n,
            "dimensions": self.dimensions,
            "data": self.data.to_dict(orient="records"),
        }

        if include_statistics and self.statistics:
            result["statistics"] = {
                col: ann.to_dict() for col, ann in self.statistics.items()
            }

        return result

    def summary_report(self) -> str:
        """Generate human-readable summary report with statistics."""
        lines = [
            f"Metric: {self.metric}",
            f"Base N: {self.base_n}",
        ]

        if self.dimensions:
            lines.append(f"Dimensions: {', '.join(self.dimensions)}")

        if self.statistics:
            lines.append("\nStatistical Summary:")
            for col, annotation in self.statistics.items():
                formatted = annotation.to_string()
                lines.append(f"  {col}: {formatted}")

        return "\n".join(lines)
