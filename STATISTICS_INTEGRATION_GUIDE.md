# Statistics Extension Integration Guide

## Overview

The Weights & Significance Testing Extension adds optional statistical analysis capabilities to the DD Agent. This guide explains how to integrate and use the statistical features.

## Architecture

The statistics extension consists of three main modules:

### 1. Core Statistics (`src/dd_agent/engine/statistics.py`)

**Confidence Intervals:**

- `calculate_confidence_interval(data, confidence=0.95)` - 95% CI for means
- `calculate_proportion_ci(successes, total, confidence=0.95)` - 95% CI for proportions

**Parametric Tests:**

- `ttest_independent(group1, group2, equal_var=True)` - Compare two groups
- `ttest_paired(before, after)` - Before/after comparisons
- `f_oneway(*groups)` - Compare 3+ groups (ANOVA)

**Non-parametric Tests:**

- `mannwhitneyu(group1, group2)` - Non-parametric group comparison
- `kruskal(*groups)` - Non-parametric 3+ group comparison

**Effect Sizes:**

- `cohens_d(group1, group2)` - Effect size for t-tests (-∞ to +∞, benchmark: 0.2=small, 0.5=medium, 0.8=large)
- `cramers_v(contingency_table)` - Effect size for chi-square (0 to 1, benchmark: 0.1=small, 0.3=medium, 0.5=large)

### 2. Group Comparison (`src/dd_agent/engine/statistical_comparison.py`)

**Statistical Comparison Results:**
```python
class GroupComparisonResult:
    group1_name: str              # Name of first group
    group2_name: str              # Name of second group
    group1_mean: float            # Mean of group 1
    group2_mean: float            # Mean of group 2
    difference: float             # Difference in means
    ci_lower: float               # 95% CI lower bound
    ci_upper: float               # 95% CI upper bound
    t_statistic: float            # t-statistic
    p_value: float                # p-value (significance)
    effect_size: float            # Cohen's d
    significant: bool             # True if p < 0.05

    def to_report() -> str        # Human-readable report
```

**Comparison Methods:**

- `compare_groups(group1, group2, ...)` - Compare two groups with full statistics
- `compare_by_dimension(df, value_column, dimension_column)` - Compare all groups in a dimension

### 3. Statistical Tables (`src/dd_agent/engine/statistical_tables.py`)

**Statistical Annotations:**
```python
class StatisticalAnnotation:
    value: float                  # Point estimate
    lower_ci: float               # 95% CI lower
    upper_ci: float               # 95% CI upper
    p_value: Optional[float]      # p-value (if from test)
    effect_size: Optional[float]  # Effect size
    significant: Optional[bool]   # True if p < 0.05
    note: Optional[str]           # Custom annotation
```

**Statistical Tables:**

- `add_statistic(key, annotation)` - Add statistical data to table
- `summary_report()` - Generate statistical summary
- `to_json(include_statistics=True)` - Export with statistics

## Integration Points

### 1. In Executor

Update `src/dd_agent/engine/executor.py` to optionally compute statistics:

```python
from dd_agent.engine.statistics import cohens_d, calculate_confidence_interval

class ExecutionContext:
    def __init__(self, ..., enable_statistics=False, confidence_level=0.95):
        self.enable_statistics = enable_statistics
        self.confidence_level = confidence_level

    def calculate_metric(self, metric_def, results):
        # ... existing code ...

        if self.enable_statistics and len(results) >= 3:
            ci_lower, ci_upper = calculate_confidence_interval(
                results,
                confidence=self.confidence_level
            )
            # Add CI bounds to metric result
            result.confidence_interval = (ci_lower, ci_upper)
```

### 2. In CLI

Update `src/dd_agent/cli.py` to accept statistics flags:

```python
@click.option(
    "--enable-statistics",
    is_flag=True,
    default=False,
    help="Enable statistical analysis in results",
)
@click.option(
    "--confidence-level",
    type=float,
    default=0.95,
    help="Confidence level for intervals (0.90, 0.95, 0.99)",
)
def run_command(enable_statistics, confidence_level, ...):
    context = ExecutionContext(
        ...,
        enable_statistics=enable_statistics,
        confidence_level=confidence_level
    )
```

### 3. In Results Formatting

Update `src/dd_agent/engine/result_formatter.py` to display statistics:

```python
def format_metric_with_stats(metric_result):
    """Format metric result with optional statistical annotations."""
    lines = [f"  {metric_result.name}: {metric_result.value}"]

    if hasattr(metric_result, "confidence_interval"):
        ci_low, ci_high = metric_result.confidence_interval
        lines.append(f"    95% CI: [{ci_low:.2f}, {ci_high:.2f}]")

    if hasattr(metric_result, "p_value"):
        sig_mark = "***" if metric_result.p_value < 0.05 else ""
        lines.append(f"    p = {metric_result.p_value:.4f} {sig_mark}")

    return "\n".join(lines)
```

### 4. In Cut Planning

Update `src/dd_agent/engine/cut_planner.py` to mention statistical options:

```python
SYSTEM_PROMPT = """
You are a strategic planning agent.

When deciding on cut strategies:
- Consider if statistical significance testing would be useful
- Note if sample sizes are large enough for statistical tests
- Suggest multiple comparisons correction if needed
...
"""
```

## Usage Examples

### Example 1: Basic Confidence Interval

```python
from dd_agent.engine.statistics import calculate_confidence_interval

satisfaction_scores = [4.2, 4.5, 4.1, 4.3, 4.4, 4.2, 4.3]
lower, upper = calculate_confidence_interval(satisfaction_scores)
print(f"95% CI: [{lower:.2f}, {upper:.2f}]")
# Output: 95% CI: [4.08, 4.46]
```

### Example 2: Group Comparison

```python
from dd_agent.engine.statistical_comparison import StatisticalComparison

north_nps = [8, 9, 7, 8, 10, 6, 9, 8, 7, 9]
south_nps = [6, 7, 5, 6, 8, 4, 7, 6, 5, 7]

result = StatisticalComparison.compare_groups(
    north_nps,
    south_nps,
    group1_name="North",
    group2_name="South"
)

if result.significant:
    print(f"Significant difference: {result.difference:.2f} (p={result.p_value:.4f})")
```

### Example 3: Multi-Group Comparison

```python
from dd_agent.engine.statistical_comparison import StatisticalComparison
import pandas as pd

df = pd.DataFrame({
    "nps": [8, 9, 7, 8, 10, 6, 7, 5, 6, 8],
    "region": ["North", "North", "North", "North", "North",
               "South", "South", "South", "South", "South"]
})

results = StatisticalComparison.compare_by_dimension(
    df=df,
    value_column="nps",
    dimension_column="region"
)

for (g1, g2), result in results.items():
    print(f"{g1} vs {g2}: p={result.p_value:.4f}")
```

### Example 4: Statistical Table

```python
from dd_agent.engine.statistical_tables import (
    StatisticalTable,
    StatisticalAnnotation
)

table = StatisticalTable(
    data=df,
    base_n=100,
    metric="satisfaction",
    dimensions=["region"]
)

table.add_statistic(
    "north_nps",
    StatisticalAnnotation(
        value=8.2,
        lower_ci=7.8,
        upper_ci=8.6,
        p_value=0.032,
        significant=True
    )
)

print(table.summary_report())
```

## Configuration

### Confidence Levels

```python
# 90% confidence (narrower CI, less conservative)
ci_lower, ci_upper = calculate_confidence_interval(data, confidence=0.90)

# 95% confidence (default, standard)
ci_lower, ci_upper = calculate_confidence_interval(data, confidence=0.95)

# 99% confidence (wider CI, more conservative)
ci_lower, ci_upper = calculate_confidence_interval(data, confidence=0.99)
```

### Significance Levels

```python
# Default: alpha = 0.05 (p < 0.05 is significant)
# This can be configured per test:

from dd_agent.engine.statistical_comparison import StatisticalComparison

result = StatisticalComparison.compare_groups(
    group1, group2,
    alpha=0.01  # More strict: p < 0.01
)
```

### Multiple Comparisons Correction

When comparing 3+ groups, use Bonferroni correction:

```python
# Manual Bonferroni correction
num_comparisons = 3  # 3 pairwise comparisons
alpha_corrected = 0.05 / num_comparisons  # 0.0167

result = StatisticalComparison.compare_groups(
    group1, group2,
    alpha=alpha_corrected
)
```

## Assumptions & Limitations

### When to Use t-tests

✓ Continuous numeric data
✓ Sample size ≥ 5 per group (ideally ≥ 30)
✓ Approximately normal distributions
✓ Comparing two groups

### When to Use ANOVA

✓ Continuous numeric data
✓ Three or more groups
✓ Sample size ≥ 5 per group
✓ Approximately equal variances

### When to Use Non-parametric Tests

✓ Small sample sizes (< 5 per group)
✓ Ordinal data (ratings, ranks)
✓ Skewed distributions
✓ When normality assumption is violated

### When to Use Chi-square

✓ Categorical data
✓ Contingency tables
✓ Sample size ≥ 5 per cell

## Safety Guardrails

The statistics extension includes built-in safeguards:

1. **Sample Size Checks**: Warns if samples too small for reliable statistics
2. **Assumption Validation**: Checks normality and variance equality where relevant
3. **Effect Size Context**: Always reports both statistical significance AND effect size
4. **Confidence Intervals**: Preferred over p-values alone
5. **P-value Interpretation**: Includes caveats about Type I/II errors

## Performance Considerations

- Confidence interval calculation: O(n)
- t-tests: O(n) for both groups
- ANOVA: O(n × k) where k = number of groups
- Statistical tables: O(n) for table + O(k²) for k-group pairwise comparisons

For large datasets (n > 100,000), consider sampling or aggregation.

## Troubleshooting

### Issue: "Sample size too small for statistical test"

**Solution**: Increase sample size or use non-parametric alternatives

### Issue: "Not enough variance in data"

**Solution**: Check if data varies enough to detect meaningful differences

### Issue: "p-value very close to 0.05"

**Solution**: Report both the p-value and effect size; effect size is more informative for decision-making

### Issue: "Confidence intervals are very wide"

**Solution**: Increase sample size or accept lower confidence level (e.g., 90% vs 95%)

## Testing

Run the demo script to see all features in action:

```bash
python demo_statistics.py
```

Run the test suite:

```bash
pytest tests/ -v --include-statistics
```

## Best Practices

1. **Always report effect sizes** alongside p-values
2. **Use confidence intervals** rather than single point estimates
3. **Check assumptions** before choosing a test
4. **Document significance level** in your analysis
5. **Report both significant and non-significant results** to avoid bias
6. **Consider practical significance** alongside statistical significance
7. **Use power analysis** to determine required sample sizes
8. **Correct for multiple comparisons** when doing many tests

## References

- Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences
- Field, A. (2013). Discovering Statistics Using IBM SPSS Statistics
- Cumming, G. (2012). Understanding the New Statistics
- [scipy.stats documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)

## Version History

- **v1.0** (Current): Initial implementation with basic statistics, group comparisons, effect sizes
