"""Statistical utilities for survey analysis and significance testing."""

import numpy as np
import pandas as pd
from scipy import stats
from typing import Optional, Tuple


def calculate_confidence_interval(
    values: np.ndarray,
    confidence: float = 0.95,
) -> Tuple[float, float]:
    """
    Calculate confidence interval for a mean.

    Args:
        values: Array of numeric values
        confidence: Confidence level (default 0.95 for 95% CI)

    Returns:
        Tuple of (lower_bound, upper_bound)
    """
    if len(values) < 2:
        return (values.mean(), values.mean())

    mean = np.mean(values)
    sem = stats.sem(values)  # Standard error of the mean
    ci = sem * stats.t.ppf((1 + confidence) / 2, len(values) - 1)

    return (mean - ci, mean + ci)


def calculate_proportion_ci(
    count: int,
    total: int,
    confidence: float = 0.95,
) -> Tuple[float, float]:
    """
    Calculate confidence interval for a proportion using Wilson score method.

    Args:
        count: Number of successes
        total: Total number of trials
        confidence: Confidence level (default 0.95)

    Returns:
        Tuple of (lower_bound, upper_bound)
    """
    if total == 0:
        return (0.0, 0.0)

    proportion = count / total
    z = stats.norm.ppf((1 + confidence) / 2)

    denominator = 1 + z * z / total
    centre_adjusted_proportion = (proportion + z * z / (2 * total)) / denominator
    adjusted_standard_deviation = np.sqrt(
        (proportion * (1 - proportion) + z * z / (4 * total)) / total
    ) / denominator

    lower = centre_adjusted_proportion - z * adjusted_standard_deviation
    upper = centre_adjusted_proportion + z * adjusted_standard_deviation

    return (max(0, lower), min(1, upper))


def chi_square_test(
    contingency_table: pd.DataFrame,
) -> Tuple[float, float, int]:
    """
    Perform chi-square test of independence.

    Args:
        contingency_table: 2D DataFrame with observed frequencies

    Returns:
        Tuple of (chi2_statistic, p_value, degrees_of_freedom)
    """
    chi2, p_value, dof, _ = stats.chi2_contingency(contingency_table)
    return (chi2, p_value, dof)


def ttest_independent(
    group1: np.ndarray,
    group2: np.ndarray,
) -> Tuple[float, float]:
    """
    Perform independent samples t-test.

    Args:
        group1: First group of values
        group2: Second group of values

    Returns:
        Tuple of (t_statistic, p_value)
    """
    if len(group1) < 2 or len(group2) < 2:
        return (np.nan, np.nan)

    t_stat, p_value = stats.ttest_ind(group1, group2)
    return (t_stat, p_value)


def cohens_d(
    group1: np.ndarray,
    group2: np.ndarray,
) -> float:
    """
    Calculate Cohen's d effect size for two groups.

    Args:
        group1: First group of values
        group2: Second group of values

    Returns:
        Cohen's d effect size
    """
    if len(group1) < 2 or len(group2) < 2:
        return np.nan

    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)

    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))

    if pooled_std == 0:
        return np.nan

    return (np.mean(group1) - np.mean(group2)) / pooled_std


def cramers_v(
    contingency_table: pd.DataFrame,
) -> float:
    """
    Calculate Cramér's V effect size for chi-square test.

    Args:
        contingency_table: 2D DataFrame with observed frequencies

    Returns:
        Cramér's V effect size (0 to 1)
    """
    chi2, _, _ = chi_square_test(contingency_table)
    n = contingency_table.sum().sum()
    min_dim = min(contingency_table.shape) - 1

    if min_dim == 0 or n == 0:
        return 0.0

    return np.sqrt(chi2 / (n * min_dim))


def is_statistically_significant(
    p_value: float,
    alpha: float = 0.05,
) -> bool:
    """
    Check if a p-value indicates statistical significance.

    Args:
        p_value: P-value from statistical test
        alpha: Significance level (default 0.05)

    Returns:
        True if statistically significant
    """
    return p_value < alpha


class SurveyWeights:
    """Utility for handling survey weights (if applicable to responses)."""

    @staticmethod
    def calculate_weighted_mean(
        values: np.ndarray,
        weights: Optional[np.ndarray] = None,
    ) -> float:
        """
        Calculate weighted mean of values.

        Args:
            values: Array of values
            weights: Array of weights (default: equal weights)

        Returns:
            Weighted mean
        """
        if weights is None:
            return np.mean(values)

        return np.average(values, weights=weights)

    @staticmethod
    def calculate_weighted_variance(
        values: np.ndarray,
        weights: Optional[np.ndarray] = None,
    ) -> float:
        """
        Calculate weighted variance of values.

        Args:
            values: Array of values
            weights: Array of weights (default: equal weights)

        Returns:
            Weighted variance
        """
        if weights is None:
            return np.var(values)

        mean = np.average(values, weights=weights)
        variance = np.average((values - mean) ** 2, weights=weights)
        return variance

    @staticmethod
    def calculate_weighted_proportion(
        successes: np.ndarray,
        weights: Optional[np.ndarray] = None,
    ) -> float:
        """
        Calculate weighted proportion.

        Args:
            successes: Boolean array indicating successes
            weights: Array of weights (default: equal weights)

        Returns:
            Weighted proportion
        """
        if weights is None:
            return np.mean(successes)

        return np.average(successes, weights=weights)
