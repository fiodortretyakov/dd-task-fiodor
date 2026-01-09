#!/usr/bin/env python3
"""Demonstration of statistical analysis capabilities."""

import numpy as np
import pandas as pd
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from dd_agent.engine.statistics import (
    calculate_confidence_interval,
    calculate_proportion_ci,
    cohens_d,
)
from dd_agent.engine.statistical_comparison import StatisticalComparison
from dd_agent.engine.statistical_tables import StatisticalTable, StatisticalAnnotation


def print_section(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'=' * 70}")
    print(f"{title:^70}")
    print(f"{'=' * 70}\n")


def demo_confidence_intervals() -> None:
    """Demonstrate confidence interval calculations."""
    print_section("1. Confidence Intervals")

    # Mean confidence interval
    nps_scores = np.array([8, 9, 7, 8, 10, 6, 9, 8, 7, 9, 10, 8])
    lower, upper = calculate_confidence_interval(nps_scores)
    mean = np.mean(nps_scores)

    print(f"NPS Scores: {nps_scores}")
    print(f"Mean: {mean:.2f}")
    print(f"95% Confidence Interval: [{lower:.2f}, {upper:.2f}]")
    print(f"Interpretation: We are 95% confident the true mean is between {lower:.2f} and {upper:.2f}")

    # Proportion confidence interval
    print(f"\n---")
    satisfied_count = 45
    total_count = 60
    lower_prop, upper_prop = calculate_proportion_ci(satisfied_count, total_count)
    proportion = satisfied_count / total_count

    print(f"Satisfaction (Top-2-Box): {satisfied_count}/{total_count} = {proportion:.1%}")
    print(f"95% Confidence Interval: [{lower_prop:.1%}, {upper_prop:.1%}]")
    print(f"Interpretation: We are 95% confident the true proportion is between {lower_prop:.1%} and {upper_prop:.1%}")


def demo_group_comparison() -> None:
    """Demonstrate statistical group comparison."""
    print_section("2. Group Comparison (t-test)")

    # Sample data: NPS by region
    np.random.seed(42)
    north_nps = np.array([8, 9, 7, 8, 10, 6, 9, 8, 7, 9])
    south_nps = np.array([6, 7, 5, 6, 8, 4, 7, 6, 5, 7])

    print(f"North Region NPS: {list(north_nps)}")
    print(f"Mean: {np.mean(north_nps):.2f}, SD: {np.std(north_nps, ddof=1):.2f}")

    print(f"\nSouth Region NPS: {list(south_nps)}")
    print(f"Mean: {np.mean(south_nps):.2f}, SD: {np.std(south_nps, ddof=1):.2f}")

    # Perform comparison
    result = StatisticalComparison.compare_groups(
        north_nps,
        south_nps,
        group1_name="North",
        group2_name="South",
    )

    print(f"\n{'-' * 70}")
    print(result.to_report())
    print(f"{'-' * 70}")

    if result.significant:
        print(f"\n✓ The difference is statistically significant (p < 0.05)")
        print(f"  The North region has significantly higher NPS than the South region")
        if abs(result.effect_size) < 0.2:
            effect_desc = "negligible"
        elif abs(result.effect_size) < 0.5:
            effect_desc = "small"
        elif abs(result.effect_size) < 0.8:
            effect_desc = "medium"
        else:
            effect_desc = "large"
        print(f"  Effect size (Cohen's d): {result.effect_size:.3f} ({effect_desc})")
    else:
        print(f"\n✗ The difference is NOT statistically significant (p ≥ 0.05)")
        print(f"  We cannot conclude that North and South regions differ in NPS")


def demo_dimension_comparison() -> None:
    """Demonstrate comparisons across multiple groups."""
    print_section("3. Multi-Group Comparison (Plan Tiers)")

    # Create sample data
    np.random.seed(42)
    df = pd.DataFrame({
        "satisfaction": np.concatenate([
            np.random.normal(4.0, 0.8, 30),  # Free plan
            np.random.normal(4.5, 0.8, 30),  # Basic plan
            np.random.normal(5.0, 0.8, 30),  # Pro plan
        ]),
        "plan_tier": ["Free"] * 30 + ["Basic"] * 30 + ["Pro"] * 30,
    })

    print(f"Data Summary:")
    print(df.groupby("plan_tier")["satisfaction"].agg(["count", "mean", "std"]))

    # Compare all pairs
    results = StatisticalComparison.compare_by_dimension(
        df=df,
        value_column="satisfaction",
        dimension_column="plan_tier",
    )

    print(f"\nPairwise Comparisons:")
    print(f"{'-' * 70}")

    for (group1, group2), result in results.items():
        sig_mark = "***" if result.significant else ""
        print(
            f"{group1:10} vs {group2:10}: "
            f"Δ = {result.difference:6.3f}, p = {result.p_value:.4f} {sig_mark}"
        )

    print(f"\n* p < 0.05 (statistically significant)")


def demo_statistical_table() -> None:
    """Demonstrate statistical table with annotations."""
    print_section("4. Statistical Tables with Annotations")

    # Create sample data
    df = pd.DataFrame({
        "region": ["North", "South", "East", "West"],
        "nps": [8.5, 6.2, 7.8, 7.1],
        "base_n": [50, 45, 55, 48],
    })

    # Create statistical table
    table = StatisticalTable(
        data=df,
        base_n=198,
        metric="nps",
        dimensions=["region"],
    )

    # Add statistical annotations
    table.add_statistic(
        "nps_north",
        StatisticalAnnotation(
            value=8.5,
            lower_ci=8.1,
            upper_ci=8.9,
            p_value=0.032,
            effect_size=0.45,
            significant=True,
        ),
    )

    table.add_statistic(
        "nps_south",
        StatisticalAnnotation(
            value=6.2,
            lower_ci=5.7,
            upper_ci=6.7,
            p_value=0.082,
            effect_size=-0.12,
            significant=False,
        ),
    )

    # Display table
    print(df.to_string(index=False))
    print(f"\n{table.summary_report()}")

    # Export to JSON
    json_data = table.to_json(include_statistics=True)
    print(f"\nJSON Export (statistics only):")
    import json

    print(json.dumps(json_data["statistics"], indent=2))


def main() -> None:
    """Run all demonstrations."""
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 68 + "║")
    print("║" + "WEIGHTS & SIGNIFICANCE TESTING EXTENSION DEMO".center(68) + "║")
    print("║" + " " * 68 + "║")
    print("╚" + "═" * 68 + "╝")

    demo_confidence_intervals()
    demo_group_comparison()
    demo_dimension_comparison()
    demo_statistical_table()

    print_section("Summary")
    print("✓ Confidence intervals quantify uncertainty in estimates")
    print("✓ t-tests determine if differences are statistically significant")
    print("✓ Effect sizes show the practical magnitude of differences")
    print("✓ Multi-group comparisons identify which groups differ")
    print("✓ Statistical tables provide comprehensive analysis output")

    print("\nAll statistical tests support:")
    print("  • Optional use (disabled by default)")
    print("  • Configurable significance levels")
    print("  • Multiple comparison corrections")
    print("  • Both frequentist and Bayesian interpretations")
    print()


if __name__ == "__main__":
    main()
