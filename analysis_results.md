# Analysis Results Summary

Total Cuts Executed: 125
Errors Encountered: 0

## Q_AGE -> mean by Question: Q_INCOME
- **Cut ID**: `USER_REQ_AGE_BY_INCOME`
- **Base N**: 100
- **Golden Comparison**: ✅ PASS (Prompt: 'Show the average age broken down by income')
- **Warnings**:
  - [HIGH] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.
  - [LOW] Base size (31) is below recommended threshold (100). Interpret results with caution.
  - [MED] Base size (24) is below minimum threshold (30). Results may not be statistically reliable.
  - [VHIGH] Base size (22) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension  value   metric  base_n
0  Q_INCOME   HIGH  61.3043      23
1  Q_INCOME    LOW  54.2581      31
2  Q_INCOME    MED  53.8750      24
3  Q_INCOME  VHIGH  48.8182      22
```

---

## Q_RESP_ID -> mean
- **Cut ID**: `CUT_1_Q_RESP_ID_mean`
- **Base N**: 100

```text
   mean      std  min    max  count
0  50.5  29.0115  1.0  100.0    100
```

---

## Q_RESP_ID -> mean by Question: Q_REGION
- **Cut ID**: `CUT_1_Q_RESP_ID_mean_BY_Q_REGION`
- **Base N**: 100
- **Warnings**:
  - [CENTRAL] Base size (21) is below minimum threshold (30). Results may not be statistically reliable.
  - [EAST] Base size (24) is below minimum threshold (30). Results may not be statistically reliable.
  - [NORTH] Base size (16) is below minimum threshold (30). Results may not be statistically reliable.
  - [SOUTH] Base size (16) is below minimum threshold (30). Results may not be statistically reliable.
  - [WEST] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension    value   metric  base_n
0  Q_REGION  CENTRAL  44.8095      21
1  Q_REGION     EAST  50.0417      24
2  Q_REGION    NORTH  53.3750      16
3  Q_REGION    SOUTH  41.3750      16
4  Q_REGION     WEST  60.5217      23
```

---

## Q_RESP_ID -> mean by Segment: SEG_HIGH_INCOME
- **Cut ID**: `CUT_1_Q_RESP_ID_mean_BY_SEG_HIGH_INCOME`
- **Base N**: 100
- **Warnings**:
  - [SEG_HIGH_INCOME] Base size (45) is below recommended threshold (100). Interpret results with caution.
  - [Not_SEG_HIGH_INCOME] Base size (55) is below recommended threshold (100). Interpret results with caution.

```text
         dimension                value   metric  base_n
0  SEG_HIGH_INCOME      SEG_HIGH_INCOME  51.4000      45
1  SEG_HIGH_INCOME  Not_SEG_HIGH_INCOME  49.7636      55
```

---

## Q_RESP_ID -> mean (Filtered)
- **Cut ID**: `CUT_1_Q_RESP_ID_mean_FILTERED_SEG_MALE_NORTH`
- **Base N**: 2
- **Warnings**:
  - Base size (2) is below minimum threshold (30). Results may not be statistically reliable.

```text
   mean      std   min   max  count
0  47.5  45.9619  15.0  80.0      2
```

---

## Q_AGE -> mean
- **Cut ID**: `CUT_2_Q_AGE_mean`
- **Base N**: 100
- **Golden Comparison**: ✅ PASS (Prompt: 'Average age')

```text
    mean      std   min   max  count
0  54.59  22.0019  18.0  89.0    100
```

---

## Q_AGE -> mean by Question: Q_INCOME
- **Cut ID**: `CUT_2_Q_AGE_mean_BY_Q_INCOME`
- **Base N**: 100
- **Golden Comparison**: ✅ PASS (Prompt: 'Show the average age broken down by income')
- **Warnings**:
  - [HIGH] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.
  - [LOW] Base size (31) is below recommended threshold (100). Interpret results with caution.
  - [MED] Base size (24) is below minimum threshold (30). Results may not be statistically reliable.
  - [VHIGH] Base size (22) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension  value   metric  base_n
0  Q_INCOME   HIGH  61.3043      23
1  Q_INCOME    LOW  54.2581      31
2  Q_INCOME    MED  53.8750      24
3  Q_INCOME  VHIGH  48.8182      22
```

---

## Q_AGE -> mean by Segment: SEG_MALE_NORTH
- **Cut ID**: `CUT_2_Q_AGE_mean_BY_SEG_MALE_NORTH`
- **Base N**: 100
- **Warnings**:
  - [SEG_MALE_NORTH] Base size (2) is below minimum threshold (30). Results may not be statistically reliable.
  - [Not_SEG_MALE_NORTH] Base size (98) is below recommended threshold (100). Interpret results with caution.

```text
        dimension               value   metric  base_n
0  SEG_MALE_NORTH      SEG_MALE_NORTH  76.5000       2
1  SEG_MALE_NORTH  Not_SEG_MALE_NORTH  54.1429      98
```

---

## Q_AGE -> mean (Filtered)
- **Cut ID**: `CUT_2_Q_AGE_mean_FILTERED_SEG_TECH_ACTIVE`
- **Base N**: 51
- **Warnings**:
  - Base size (51) is below recommended threshold (100). Interpret results with caution.

```text
      mean      std   min   max  count
0  49.7647  20.7119  19.0  89.0     51
```

---

## Q_GENDER -> frequency
- **Cut ID**: `CUT_3_Q_GENDER_frequency`
- **Base N**: 100
- **Golden Comparison**: ✅ PASS (Prompt: 'Frequency of gender')

```text
  value              label  count  percentage
0     F             Female     31        31.0
1   PNS  Prefer not to say     25        25.0
2     M               Male     22        22.0
3    NB         Non-binary     22        22.0
```

---

## Q_GENDER -> frequency by Question: Q_USAGE_FREQ
- **Cut ID**: `CUT_3_Q_GENDER_frequency_BY_Q_USAGE_FREQ`
- **Base N**: 100
- **Warnings**:
  - [DAILY] Base size (26) is below minimum threshold (30). Results may not be statistically reliable.
  - [MONTHLY] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.
  - [RARELY] Base size (28) is below minimum threshold (30). Results may not be statistically reliable.
  - [WEEKLY] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.

```text
      dimension    value                                                                                                                                                                                                                                                                                             metric  base_n
0  Q_USAGE_FREQ    DAILY   [{'value': 'F', 'label': 'Female', 'count': 8, 'percentage': 30.77}, {'value': 'NB', 'label': 'Non-binary', 'count': 7, 'percentage': 26.92}, {'value': 'PNS', 'label': 'Prefer not to say', 'count': 7, 'percentage': 26.92}, {'value': 'M', 'label': 'Male', 'count': 4, 'percentage': 15.38}]      26
1  Q_USAGE_FREQ  MONTHLY   [{'value': 'F', 'label': 'Female', 'count': 7, 'percentage': 30.43}, {'value': 'NB', 'label': 'Non-binary', 'count': 6, 'percentage': 26.09}, {'value': 'M', 'label': 'Male', 'count': 5, 'percentage': 21.74}, {'value': 'PNS', 'label': 'Prefer not to say', 'count': 5, 'percentage': 21.74}]      23
2  Q_USAGE_FREQ   RARELY  [{'value': 'F', 'label': 'Female', 'count': 11, 'percentage': 39.29}, {'value': 'PNS', 'label': 'Prefer not to say', 'count': 9, 'percentage': 32.14}, {'value': 'NB', 'label': 'Non-binary', 'count': 4, 'percentage': 14.29}, {'value': 'M', 'label': 'Male', 'count': 4, 'percentage': 14.29}]      28
3  Q_USAGE_FREQ   WEEKLY   [{'value': 'M', 'label': 'Male', 'count': 9, 'percentage': 39.13}, {'value': 'F', 'label': 'Female', 'count': 5, 'percentage': 21.74}, {'value': 'NB', 'label': 'Non-binary', 'count': 5, 'percentage': 21.74}, {'value': 'PNS', 'label': 'Prefer not to say', 'count': 4, 'percentage': 17.39}]      23
```

---

## Q_GENDER -> frequency by Segment: SEG_TECH_ACTIVE
- **Cut ID**: `CUT_3_Q_GENDER_frequency_BY_SEG_TECH_ACTIVE`
- **Base N**: 100
- **Warnings**:
  - [SEG_TECH_ACTIVE] Base size (51) is below recommended threshold (100). Interpret results with caution.
  - [Not_SEG_TECH_ACTIVE] Base size (49) is below recommended threshold (100). Interpret results with caution.

```text
         dimension                value                                                                                                                                                                                                                                                                                                metric  base_n
0  SEG_TECH_ACTIVE      SEG_TECH_ACTIVE  [{'value': 'PNS', 'label': 'Prefer not to say', 'count': 15, 'percentage': 29.41}, {'value': 'F', 'label': 'Female', 'count': 15, 'percentage': 29.41}, {'value': 'NB', 'label': 'Non-binary', 'count': 11, 'percentage': 21.57}, {'value': 'M', 'label': 'Male', 'count': 10, 'percentage': 19.61}]      51
1  SEG_TECH_ACTIVE  Not_SEG_TECH_ACTIVE  [{'value': 'F', 'label': 'Female', 'count': 16, 'percentage': 32.65}, {'value': 'M', 'label': 'Male', 'count': 12, 'percentage': 24.49}, {'value': 'NB', 'label': 'Non-binary', 'count': 11, 'percentage': 22.45}, {'value': 'PNS', 'label': 'Prefer not to say', 'count': 10, 'percentage': 20.41}]      49
```

---

## Q_GENDER -> frequency (Filtered)
- **Cut ID**: `CUT_3_Q_GENDER_frequency_FILTERED_SEG_NOT_LOW_INCOME`
- **Base N**: 69
- **Warnings**:
  - Base size (69) is below recommended threshold (100). Interpret results with caution.

```text
  value              label  count  percentage
0     F             Female     21       30.43
1   PNS  Prefer not to say     19       27.54
2    NB         Non-binary     15       21.74
3     M               Male     14       20.29
```

---

## Q_REGION -> frequency
- **Cut ID**: `CUT_4_Q_REGION_frequency`
- **Base N**: 100

```text
     value    label  count  percentage
0     EAST     East     24        24.0
1     WEST     West     23        23.0
2  CENTRAL  Central     21        21.0
3    NORTH    North     16        16.0
4    SOUTH    South     16        16.0
```

---

## Q_REGION -> frequency by Question: Q_TENURE
- **Cut ID**: `CUT_4_Q_REGION_frequency_BY_Q_TENURE`
- **Base N**: 100
- **Warnings**:
  - [LONG] Base size (33) is below recommended threshold (100). Interpret results with caution.
  - [MED] Base size (33) is below recommended threshold (100). Interpret results with caution.
  - [NEW] Base size (34) is below recommended threshold (100). Interpret results with caution.

```text
  dimension value                                                                                                                                                                                                                                                                                                                                                                 metric  base_n
0  Q_TENURE  LONG     [{'value': 'WEST', 'label': 'West', 'count': 9, 'percentage': 27.27}, {'value': 'EAST', 'label': 'East', 'count': 8, 'percentage': 24.24}, {'value': 'SOUTH', 'label': 'South', 'count': 7, 'percentage': 21.21}, {'value': 'CENTRAL', 'label': 'Central', 'count': 7, 'percentage': 21.21}, {'value': 'NORTH', 'label': 'North', 'count': 2, 'percentage': 6.06}]      33
1  Q_TENURE   MED    [{'value': 'CENTRAL', 'label': 'Central', 'count': 10, 'percentage': 30.3}, {'value': 'NORTH', 'label': 'North', 'count': 9, 'percentage': 27.27}, {'value': 'EAST', 'label': 'East', 'count': 5, 'percentage': 15.15}, {'value': 'SOUTH', 'label': 'South', 'count': 5, 'percentage': 15.15}, {'value': 'WEST', 'label': 'West', 'count': 4, 'percentage': 12.12}]      33
2  Q_TENURE   NEW  [{'value': 'EAST', 'label': 'East', 'count': 11, 'percentage': 32.35}, {'value': 'WEST', 'label': 'West', 'count': 10, 'percentage': 29.41}, {'value': 'NORTH', 'label': 'North', 'count': 5, 'percentage': 14.71}, {'value': 'SOUTH', 'label': 'South', 'count': 4, 'percentage': 11.76}, {'value': 'CENTRAL', 'label': 'Central', 'count': 4, 'percentage': 11.76}]      34
```

---

## Q_REGION -> frequency by Segment: SEG_NOT_LOW_INCOME
- **Cut ID**: `CUT_4_Q_REGION_frequency_BY_SEG_NOT_LOW_INCOME`
- **Base N**: 100
- **Warnings**:
  - [SEG_NOT_LOW_INCOME] Base size (69) is below recommended threshold (100). Interpret results with caution.
  - [Not_SEG_NOT_LOW_INCOME] Base size (31) is below recommended threshold (100). Interpret results with caution.

```text
            dimension                   value                                                                                                                                                                                                                                                                                                                                                                   metric  base_n
0  SEG_NOT_LOW_INCOME      SEG_NOT_LOW_INCOME  [{'value': 'WEST', 'label': 'West', 'count': 18, 'percentage': 26.09}, {'value': 'CENTRAL', 'label': 'Central', 'count': 17, 'percentage': 24.64}, {'value': 'EAST', 'label': 'East', 'count': 14, 'percentage': 20.29}, {'value': 'NORTH', 'label': 'North', 'count': 11, 'percentage': 15.94}, {'value': 'SOUTH', 'label': 'South', 'count': 9, 'percentage': 13.04}]      69
1  SEG_NOT_LOW_INCOME  Not_SEG_NOT_LOW_INCOME      [{'value': 'EAST', 'label': 'East', 'count': 10, 'percentage': 32.26}, {'value': 'SOUTH', 'label': 'South', 'count': 7, 'percentage': 22.58}, {'value': 'NORTH', 'label': 'North', 'count': 5, 'percentage': 16.13}, {'value': 'WEST', 'label': 'West', 'count': 5, 'percentage': 16.13}, {'value': 'CENTRAL', 'label': 'Central', 'count': 4, 'percentage': 12.9}]      31
```

---

## Q_REGION -> frequency (Filtered)
- **Cut ID**: `CUT_4_Q_REGION_frequency_FILTERED_SEG_OR_CONDITION`
- **Base N**: 29
- **Warnings**:
  - Base size (29) is below minimum threshold (30). Results may not be statistically reliable.

```text
     value    label  count  percentage
0     WEST     West     11       37.93
1  CENTRAL  Central      6       20.69
2     EAST     East      6       20.69
3    NORTH    North      4       13.79
4    SOUTH    South      2        6.90
```

---

## Q_INCOME -> frequency
- **Cut ID**: `CUT_5_Q_INCOME_frequency`
- **Base N**: 100

```text
   value               label  count  percentage
0    LOW       Under $30,000     31        31.0
1    MED   $30,000 - $75,000     24        24.0
2   HIGH  $75,000 - $150,000     23        23.0
3  VHIGH       Over $150,000     22        22.0
```

---

## Q_INCOME -> frequency by Question: Q_PLAN
- **Cut ID**: `CUT_5_Q_INCOME_frequency_BY_Q_PLAN`
- **Base N**: 100
- **Warnings**:
  - [BASIC] Base size (26) is below minimum threshold (30). Results may not be statistically reliable.
  - [ENT] Base size (28) is below minimum threshold (30). Results may not be statistically reliable.
  - [FREE] Base size (20) is below minimum threshold (30). Results may not be statistically reliable.
  - [PRO] Base size (26) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension  value                                                                                                                                                                                                                                                                                                                             metric  base_n
0    Q_PLAN  BASIC   [{'value': 'HIGH', 'label': '$75,000 - $150,000', 'count': 8, 'percentage': 30.77}, {'value': 'VHIGH', 'label': 'Over $150,000', 'count': 6, 'percentage': 23.08}, {'value': 'LOW', 'label': 'Under $30,000', 'count': 6, 'percentage': 23.08}, {'value': 'MED', 'label': '$30,000 - $75,000', 'count': 6, 'percentage': 23.08}]      26
1    Q_PLAN    ENT     [{'value': 'VHIGH', 'label': 'Over $150,000', 'count': 8, 'percentage': 28.57}, {'value': 'HIGH', 'label': '$75,000 - $150,000', 'count': 7, 'percentage': 25.0}, {'value': 'LOW', 'label': 'Under $30,000', 'count': 7, 'percentage': 25.0}, {'value': 'MED', 'label': '$30,000 - $75,000', 'count': 6, 'percentage': 21.43}]      28
2    Q_PLAN   FREE       [{'value': 'MED', 'label': '$30,000 - $75,000', 'count': 7, 'percentage': 35.0}, {'value': 'LOW', 'label': 'Under $30,000', 'count': 6, 'percentage': 30.0}, {'value': 'VHIGH', 'label': 'Over $150,000', 'count': 5, 'percentage': 25.0}, {'value': 'HIGH', 'label': '$75,000 - $150,000', 'count': 2, 'percentage': 10.0}]      20
3    Q_PLAN    PRO  [{'value': 'LOW', 'label': 'Under $30,000', 'count': 12, 'percentage': 46.15}, {'value': 'HIGH', 'label': '$75,000 - $150,000', 'count': 6, 'percentage': 23.08}, {'value': 'MED', 'label': '$30,000 - $75,000', 'count': 5, 'percentage': 19.23}, {'value': 'VHIGH', 'label': 'Over $150,000', 'count': 3, 'percentage': 11.54}]      26
```

---

## Q_INCOME -> frequency by Segment: SEG_OR_CONDITION
- **Cut ID**: `CUT_5_Q_INCOME_frequency_BY_SEG_OR_CONDITION`
- **Base N**: 100
- **Warnings**:
  - [SEG_OR_CONDITION] Base size (29) is below minimum threshold (30). Results may not be statistically reliable.
  - [Not_SEG_OR_CONDITION] Base size (71) is below recommended threshold (100). Interpret results with caution.

```text
          dimension                 value                                                                                                                                                                                                                                                                                                                          metric  base_n
0  SEG_OR_CONDITION      SEG_OR_CONDITION  [{'value': 'VHIGH', 'label': 'Over $150,000', 'count': 22, 'percentage': 75.86}, {'value': 'LOW', 'label': 'Under $30,000', 'count': 4, 'percentage': 13.79}, {'value': 'MED', 'label': '$30,000 - $75,000', 'count': 2, 'percentage': 6.9}, {'value': 'HIGH', 'label': '$75,000 - $150,000', 'count': 1, 'percentage': 3.45}]      29
1  SEG_OR_CONDITION  Not_SEG_OR_CONDITION                                                                            [{'value': 'LOW', 'label': 'Under $30,000', 'count': 27, 'percentage': 38.03}, {'value': 'MED', 'label': '$30,000 - $75,000', 'count': 22, 'percentage': 30.99}, {'value': 'HIGH', 'label': '$75,000 - $150,000', 'count': 22, 'percentage': 30.99}]      71
```

---

## Q_INCOME -> frequency (Filtered)
- **Cut ID**: `CUT_5_Q_INCOME_frequency_FILTERED_SEG_YOUNG`
- **Base N**: 29
- **Warnings**:
  - Base size (29) is below minimum threshold (30). Results may not be statistically reliable.

```text
   value               label  count  percentage
0  VHIGH       Over $150,000      9       31.03
1    LOW       Under $30,000      9       31.03
2    MED   $30,000 - $75,000      7       24.14
3   HIGH  $75,000 - $150,000      4       13.79
```

---

## Q_NPS -> mean
- **Cut ID**: `CUT_6_Q_NPS_mean`
- **Base N**: 100

```text
   mean     std  min   max  count
0  5.08  3.0902  0.0  10.0    100
```

---

## Q_NPS -> mean by Question: Q_GENDER
- **Cut ID**: `CUT_6_Q_NPS_mean_BY_Q_GENDER`
- **Base N**: 100
- **Warnings**:
  - [F] Base size (31) is below recommended threshold (100). Interpret results with caution.
  - [M] Base size (22) is below minimum threshold (30). Results may not be statistically reliable.
  - [NB] Base size (22) is below minimum threshold (30). Results may not be statistically reliable.
  - [PNS] Base size (25) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension value  metric  base_n
0  Q_GENDER     F  4.6774      31
1  Q_GENDER     M  4.9545      22
2  Q_GENDER    NB  6.1818      22
3  Q_GENDER   PNS  4.7200      25
```

---

## Q_NPS -> mean by Segment: SEG_YOUNG
- **Cut ID**: `CUT_6_Q_NPS_mean_BY_SEG_YOUNG`
- **Base N**: 100
- **Warnings**:
  - [SEG_YOUNG] Base size (29) is below minimum threshold (30). Results may not be statistically reliable.
  - [Not_SEG_YOUNG] Base size (71) is below recommended threshold (100). Interpret results with caution.

```text
   dimension          value  metric  base_n
0  SEG_YOUNG      SEG_YOUNG  5.1724      29
1  SEG_YOUNG  Not_SEG_YOUNG  5.0423      71
```

---

## Q_NPS -> mean (Filtered)
- **Cut ID**: `CUT_6_Q_NPS_mean_FILTERED_SEG_HIGH_INCOME`
- **Base N**: 45
- **Warnings**:
  - Base size (45) is below recommended threshold (100). Interpret results with caution.

```text
     mean     std  min   max  count
0  5.7778  3.1253  0.0  10.0     45
```

---

## Q_NPS -> nps
- **Cut ID**: `CUT_7_Q_NPS_nps`
- **Base N**: 100
- **Golden Comparison**: ✅ PASS (Prompt: 'NPS score for the product')

```text
    nps  promoters_count  promoters_pct  passives_count  passives_pct  detractors_count  detractors_pct  total
0 -47.0               19           19.0              15          15.0                66            66.0    100
```

---

## Q_NPS -> nps by Question: Q_REGION
- **Cut ID**: `CUT_7_Q_NPS_nps_BY_Q_REGION`
- **Base N**: 100
- **Golden Comparison**: ✅ PASS (Prompt: 'Performance of NPS by region')
- **Warnings**:
  - [CENTRAL] Base size (21) is below minimum threshold (30). Results may not be statistically reliable.
  - [EAST] Base size (24) is below minimum threshold (30). Results may not be statistically reliable.
  - [NORTH] Base size (16) is below minimum threshold (30). Results may not be statistically reliable.
  - [SOUTH] Base size (16) is below minimum threshold (30). Results may not be statistically reliable.
  - [WEST] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension    value  metric  base_n
0  Q_REGION  CENTRAL  -66.67      21
1  Q_REGION     EAST  -45.83      24
2  Q_REGION    NORTH  -62.50      16
3  Q_REGION    SOUTH  -43.75      16
4  Q_REGION     WEST  -21.74      23
```

---

## Q_NPS -> nps by Segment: SEG_HIGH_INCOME
- **Cut ID**: `CUT_7_Q_NPS_nps_BY_SEG_HIGH_INCOME`
- **Base N**: 100
- **Warnings**:
  - [SEG_HIGH_INCOME] Base size (45) is below recommended threshold (100). Interpret results with caution.
  - [Not_SEG_HIGH_INCOME] Base size (55) is below recommended threshold (100). Interpret results with caution.

```text
         dimension                value  metric  base_n
0  SEG_HIGH_INCOME      SEG_HIGH_INCOME  -26.67      45
1  SEG_HIGH_INCOME  Not_SEG_HIGH_INCOME  -63.64      55
```

---

## Q_NPS -> nps (Filtered)
- **Cut ID**: `CUT_7_Q_NPS_nps_FILTERED_SEG_MALE_NORTH`
- **Base N**: 2
- **Warnings**:
  - Base size (2) is below minimum threshold (30). Results may not be statistically reliable.

```text
     nps  promoters_count  promoters_pct  passives_count  passives_pct  detractors_count  detractors_pct  total
0 -100.0                0            0.0               0           0.0                 2           100.0      2
```

---

## Q_OVERALL_SAT -> frequency
- **Cut ID**: `CUT_8_Q_OVERALL_SAT_frequency`
- **Base N**: 100

```text
   value              label  count  percentage
0      1  Very Dissatisfied     13        13.0
1      2       Dissatisfied     18        18.0
2      3            Neutral     21        21.0
3      4          Satisfied     28        28.0
4      5     Very Satisfied     20        20.0
```

---

## Q_OVERALL_SAT -> frequency by Question: Q_INCOME
- **Cut ID**: `CUT_8_Q_OVERALL_SAT_frequency_BY_Q_INCOME`
- **Base N**: 100
- **Warnings**:
  - [HIGH] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.
  - [LOW] Base size (31) is below recommended threshold (100). Interpret results with caution.
  - [MED] Base size (24) is below minimum threshold (30). Results may not be statistically reliable.
  - [VHIGH] Base size (22) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension  value                                                                                                                                                                                                                                                                                                                                                                   metric  base_n
0  Q_INCOME   HIGH    [{'value': 1, 'label': 'Very Dissatisfied', 'count': 2, 'percentage': 8.7}, {'value': 2, 'label': 'Dissatisfied', 'count': 7, 'percentage': 30.43}, {'value': 3, 'label': 'Neutral', 'count': 5, 'percentage': 21.74}, {'value': 4, 'label': 'Satisfied', 'count': 5, 'percentage': 21.74}, {'value': 5, 'label': 'Very Satisfied', 'count': 4, 'percentage': 17.39}]      23
1  Q_INCOME    LOW   [{'value': 1, 'label': 'Very Dissatisfied', 'count': 4, 'percentage': 12.9}, {'value': 2, 'label': 'Dissatisfied', 'count': 5, 'percentage': 16.13}, {'value': 3, 'label': 'Neutral', 'count': 8, 'percentage': 25.81}, {'value': 4, 'label': 'Satisfied', 'count': 8, 'percentage': 25.81}, {'value': 5, 'label': 'Very Satisfied', 'count': 6, 'percentage': 19.35}]      31
2  Q_INCOME    MED    [{'value': 1, 'label': 'Very Dissatisfied', 'count': 4, 'percentage': 16.67}, {'value': 2, 'label': 'Dissatisfied', 'count': 3, 'percentage': 12.5}, {'value': 3, 'label': 'Neutral', 'count': 3, 'percentage': 12.5}, {'value': 4, 'label': 'Satisfied', 'count': 7, 'percentage': 29.17}, {'value': 5, 'label': 'Very Satisfied', 'count': 7, 'percentage': 29.17}]      24
3  Q_INCOME  VHIGH  [{'value': 1, 'label': 'Very Dissatisfied', 'count': 3, 'percentage': 13.64}, {'value': 2, 'label': 'Dissatisfied', 'count': 3, 'percentage': 13.64}, {'value': 3, 'label': 'Neutral', 'count': 5, 'percentage': 22.73}, {'value': 4, 'label': 'Satisfied', 'count': 8, 'percentage': 36.36}, {'value': 5, 'label': 'Very Satisfied', 'count': 3, 'percentage': 13.64}]      22
```

---

## Q_OVERALL_SAT -> frequency by Segment: SEG_MALE_NORTH
- **Cut ID**: `CUT_8_Q_OVERALL_SAT_frequency_BY_SEG_MALE_NORTH`
- **Base N**: 100
- **Warnings**:
  - [SEG_MALE_NORTH] Base size (2) is below minimum threshold (30). Results may not be statistically reliable.
  - [Not_SEG_MALE_NORTH] Base size (98) is below recommended threshold (100). Interpret results with caution.

```text
        dimension               value                                                                                                                                                                                                                                                                                                                                                                        metric  base_n
0  SEG_MALE_NORTH      SEG_MALE_NORTH                                                                                                                                                                                                                                        [{'value': 3, 'label': 'Neutral', 'count': 1, 'percentage': 50.0}, {'value': 4, 'label': 'Satisfied', 'count': 1, 'percentage': 50.0}]       2
1  SEG_MALE_NORTH  Not_SEG_MALE_NORTH  [{'value': 1, 'label': 'Very Dissatisfied', 'count': 13, 'percentage': 13.27}, {'value': 2, 'label': 'Dissatisfied', 'count': 18, 'percentage': 18.37}, {'value': 3, 'label': 'Neutral', 'count': 20, 'percentage': 20.41}, {'value': 4, 'label': 'Satisfied', 'count': 27, 'percentage': 27.55}, {'value': 5, 'label': 'Very Satisfied', 'count': 20, 'percentage': 20.41}]      98
```

---

## Q_OVERALL_SAT -> frequency (Filtered)
- **Cut ID**: `CUT_8_Q_OVERALL_SAT_frequency_FILTERED_SEG_TECH_ACTIVE`
- **Base N**: 51
- **Warnings**:
  - Base size (51) is below recommended threshold (100). Interpret results with caution.

```text
   value              label  count  percentage
0      1  Very Dissatisfied      7       13.73
1      2       Dissatisfied     12       23.53
2      3            Neutral     10       19.61
3      4          Satisfied     13       25.49
4      5     Very Satisfied      9       17.65
```

---

## Q_OVERALL_SAT -> mean
- **Cut ID**: `CUT_9_Q_OVERALL_SAT_mean`
- **Base N**: 100

```text
   mean    std  min  max  count
0  3.24  1.319  1.0  5.0    100
```

---

## Q_OVERALL_SAT -> mean by Question: Q_USAGE_FREQ
- **Cut ID**: `CUT_9_Q_OVERALL_SAT_mean_BY_Q_USAGE_FREQ`
- **Base N**: 100
- **Warnings**:
  - [DAILY] Base size (26) is below minimum threshold (30). Results may not be statistically reliable.
  - [MONTHLY] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.
  - [RARELY] Base size (28) is below minimum threshold (30). Results may not be statistically reliable.
  - [WEEKLY] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.

```text
      dimension    value  metric  base_n
0  Q_USAGE_FREQ    DAILY  2.9615      26
1  Q_USAGE_FREQ  MONTHLY  3.5217      23
2  Q_USAGE_FREQ   RARELY  3.5000      28
3  Q_USAGE_FREQ   WEEKLY  2.9565      23
```

---

## Q_OVERALL_SAT -> mean by Segment: SEG_TECH_ACTIVE
- **Cut ID**: `CUT_9_Q_OVERALL_SAT_mean_BY_SEG_TECH_ACTIVE`
- **Base N**: 100
- **Warnings**:
  - [SEG_TECH_ACTIVE] Base size (51) is below recommended threshold (100). Interpret results with caution.
  - [Not_SEG_TECH_ACTIVE] Base size (49) is below recommended threshold (100). Interpret results with caution.

```text
         dimension                value  metric  base_n
0  SEG_TECH_ACTIVE      SEG_TECH_ACTIVE  3.0980      51
1  SEG_TECH_ACTIVE  Not_SEG_TECH_ACTIVE  3.3878      49
```

---

## Q_OVERALL_SAT -> mean (Filtered)
- **Cut ID**: `CUT_9_Q_OVERALL_SAT_mean_FILTERED_SEG_NOT_LOW_INCOME`
- **Base N**: 69
- **Warnings**:
  - Base size (69) is below recommended threshold (100). Interpret results with caution.

```text
     mean     std  min  max  count
0  3.2464  1.3329  1.0  5.0     69
```

---

## Q_OVERALL_SAT -> top2box
- **Cut ID**: `CUT_10_Q_OVERALL_SAT_top2box`
- **Base N**: 100
- **Golden Comparison**: ✅ PASS (Prompt: 'Top 2 box for overall satisfaction')

```text
   top2box_pct  top2box_count  total top_values
0         48.0             48    100     [4, 5]
```

---

## Q_OVERALL_SAT -> top2box by Question: Q_TENURE
- **Cut ID**: `CUT_10_Q_OVERALL_SAT_top2box_BY_Q_TENURE`
- **Base N**: 100
- **Warnings**:
  - [LONG] Base size (33) is below recommended threshold (100). Interpret results with caution.
  - [MED] Base size (33) is below recommended threshold (100). Interpret results with caution.
  - [NEW] Base size (34) is below recommended threshold (100). Interpret results with caution.

```text
  dimension value  metric  base_n
0  Q_TENURE  LONG   42.42      33
1  Q_TENURE   MED   51.52      33
2  Q_TENURE   NEW   50.00      34
```

---

## Q_OVERALL_SAT -> top2box by Segment: SEG_NOT_LOW_INCOME
- **Cut ID**: `CUT_10_Q_OVERALL_SAT_top2box_BY_SEG_NOT_LOW_INCOME`
- **Base N**: 100
- **Warnings**:
  - [SEG_NOT_LOW_INCOME] Base size (69) is below recommended threshold (100). Interpret results with caution.
  - [Not_SEG_NOT_LOW_INCOME] Base size (31) is below recommended threshold (100). Interpret results with caution.

```text
            dimension                   value  metric  base_n
0  SEG_NOT_LOW_INCOME      SEG_NOT_LOW_INCOME   49.28      69
1  SEG_NOT_LOW_INCOME  Not_SEG_NOT_LOW_INCOME   45.16      31
```

---

## Q_OVERALL_SAT -> top2box (Filtered)
- **Cut ID**: `CUT_10_Q_OVERALL_SAT_top2box_FILTERED_SEG_OR_CONDITION`
- **Base N**: 29
- **Warnings**:
  - Base size (29) is below minimum threshold (30). Results may not be statistically reliable.

```text
   top2box_pct  top2box_count  total top_values
0        55.17             16     29     [4, 5]
```

---

## Q_OVERALL_SAT -> bottom2box
- **Cut ID**: `CUT_11_Q_OVERALL_SAT_bottom2box`
- **Base N**: 100

```text
   bottom2box_pct  bottom2box_count  total bottom_values
0            31.0                31    100        [1, 2]
```

---

## Q_OVERALL_SAT -> bottom2box by Question: Q_PLAN
- **Cut ID**: `CUT_11_Q_OVERALL_SAT_bottom2box_BY_Q_PLAN`
- **Base N**: 100
- **Warnings**:
  - [BASIC] Base size (26) is below minimum threshold (30). Results may not be statistically reliable.
  - [ENT] Base size (28) is below minimum threshold (30). Results may not be statistically reliable.
  - [FREE] Base size (20) is below minimum threshold (30). Results may not be statistically reliable.
  - [PRO] Base size (26) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension  value  metric  base_n
0    Q_PLAN  BASIC   30.77      26
1    Q_PLAN    ENT   25.00      28
2    Q_PLAN   FREE   30.00      20
3    Q_PLAN    PRO   38.46      26
```

---

## Q_OVERALL_SAT -> bottom2box by Segment: SEG_OR_CONDITION
- **Cut ID**: `CUT_11_Q_OVERALL_SAT_bottom2box_BY_SEG_OR_CONDITION`
- **Base N**: 100
- **Warnings**:
  - [SEG_OR_CONDITION] Base size (29) is below minimum threshold (30). Results may not be statistically reliable.
  - [Not_SEG_OR_CONDITION] Base size (71) is below recommended threshold (100). Interpret results with caution.

```text
          dimension                 value  metric  base_n
0  SEG_OR_CONDITION      SEG_OR_CONDITION   24.14      29
1  SEG_OR_CONDITION  Not_SEG_OR_CONDITION   33.80      71
```

---

## Q_OVERALL_SAT -> bottom2box (Filtered)
- **Cut ID**: `CUT_11_Q_OVERALL_SAT_bottom2box_FILTERED_SEG_YOUNG`
- **Base N**: 29
- **Warnings**:
  - Base size (29) is below minimum threshold (30). Results may not be statistically reliable.

```text
   bottom2box_pct  bottom2box_count  total bottom_values
0           31.03                 9     29        [1, 2]
```

---

## Q_EASE_OF_USE -> frequency
- **Cut ID**: `CUT_12_Q_EASE_OF_USE_frequency`
- **Base N**: 100

```text
   value           label  count  percentage
0      1  Very Difficult     19        19.0
1      2       Difficult     20        20.0
2      3         Neutral     18        18.0
3      4            Easy     24        24.0
4      5       Very Easy     19        19.0
```

---

## Q_EASE_OF_USE -> frequency by Question: Q_GENDER
- **Cut ID**: `CUT_12_Q_EASE_OF_USE_frequency_BY_Q_GENDER`
- **Base N**: 100
- **Warnings**:
  - [F] Base size (31) is below recommended threshold (100). Interpret results with caution.
  - [M] Base size (22) is below minimum threshold (30). Results may not be statistically reliable.
  - [NB] Base size (22) is below minimum threshold (30). Results may not be statistically reliable.
  - [PNS] Base size (25) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension value                                                                                                                                                                                                                                                                                                                                                   metric  base_n
0  Q_GENDER     F   [{'value': 1, 'label': 'Very Difficult', 'count': 6, 'percentage': 19.35}, {'value': 2, 'label': 'Difficult', 'count': 6, 'percentage': 19.35}, {'value': 3, 'label': 'Neutral', 'count': 2, 'percentage': 6.45}, {'value': 4, 'label': 'Easy', 'count': 8, 'percentage': 25.81}, {'value': 5, 'label': 'Very Easy', 'count': 9, 'percentage': 29.03}]      31
1  Q_GENDER     M  [{'value': 1, 'label': 'Very Difficult', 'count': 7, 'percentage': 31.82}, {'value': 2, 'label': 'Difficult', 'count': 3, 'percentage': 13.64}, {'value': 3, 'label': 'Neutral', 'count': 4, 'percentage': 18.18}, {'value': 4, 'label': 'Easy', 'count': 4, 'percentage': 18.18}, {'value': 5, 'label': 'Very Easy', 'count': 4, 'percentage': 18.18}]      22
2  Q_GENDER    NB  [{'value': 1, 'label': 'Very Difficult', 'count': 4, 'percentage': 18.18}, {'value': 2, 'label': 'Difficult', 'count': 4, 'percentage': 18.18}, {'value': 3, 'label': 'Neutral', 'count': 7, 'percentage': 31.82}, {'value': 4, 'label': 'Easy', 'count': 4, 'percentage': 18.18}, {'value': 5, 'label': 'Very Easy', 'count': 3, 'percentage': 13.64}]      22
3  Q_GENDER   PNS        [{'value': 1, 'label': 'Very Difficult', 'count': 2, 'percentage': 8.0}, {'value': 2, 'label': 'Difficult', 'count': 7, 'percentage': 28.0}, {'value': 3, 'label': 'Neutral', 'count': 5, 'percentage': 20.0}, {'value': 4, 'label': 'Easy', 'count': 8, 'percentage': 32.0}, {'value': 5, 'label': 'Very Easy', 'count': 3, 'percentage': 12.0}]      25
```

---

## Q_EASE_OF_USE -> frequency by Segment: SEG_YOUNG
- **Cut ID**: `CUT_12_Q_EASE_OF_USE_frequency_BY_SEG_YOUNG`
- **Base N**: 100
- **Warnings**:
  - [SEG_YOUNG] Base size (29) is below minimum threshold (30). Results may not be statistically reliable.
  - [Not_SEG_YOUNG] Base size (71) is below recommended threshold (100). Interpret results with caution.

```text
   dimension          value                                                                                                                                                                                                                                                                                                                                                       metric  base_n
0  SEG_YOUNG      SEG_YOUNG        [{'value': 1, 'label': 'Very Difficult', 'count': 2, 'percentage': 6.9}, {'value': 2, 'label': 'Difficult', 'count': 6, 'percentage': 20.69}, {'value': 3, 'label': 'Neutral', 'count': 5, 'percentage': 17.24}, {'value': 4, 'label': 'Easy', 'count': 9, 'percentage': 31.03}, {'value': 5, 'label': 'Very Easy', 'count': 7, 'percentage': 24.14}]      29
1  SEG_YOUNG  Not_SEG_YOUNG  [{'value': 1, 'label': 'Very Difficult', 'count': 17, 'percentage': 23.94}, {'value': 2, 'label': 'Difficult', 'count': 14, 'percentage': 19.72}, {'value': 3, 'label': 'Neutral', 'count': 13, 'percentage': 18.31}, {'value': 4, 'label': 'Easy', 'count': 15, 'percentage': 21.13}, {'value': 5, 'label': 'Very Easy', 'count': 12, 'percentage': 16.9}]      71
```

---

## Q_EASE_OF_USE -> frequency (Filtered)
- **Cut ID**: `CUT_12_Q_EASE_OF_USE_frequency_FILTERED_SEG_HIGH_INCOME`
- **Base N**: 45
- **Warnings**:
  - Base size (45) is below recommended threshold (100). Interpret results with caution.

```text
   value           label  count  percentage
0      1  Very Difficult      6       13.33
1      2       Difficult      7       15.56
2      3         Neutral      7       15.56
3      4            Easy     15       33.33
4      5       Very Easy     10       22.22
```

---

## Q_EASE_OF_USE -> mean
- **Cut ID**: `CUT_13_Q_EASE_OF_USE_mean`
- **Base N**: 100

```text
   mean     std  min  max  count
0  3.04  1.4065  1.0  5.0    100
```

---

## Q_EASE_OF_USE -> mean by Question: Q_REGION
- **Cut ID**: `CUT_13_Q_EASE_OF_USE_mean_BY_Q_REGION`
- **Base N**: 100
- **Warnings**:
  - [CENTRAL] Base size (21) is below minimum threshold (30). Results may not be statistically reliable.
  - [EAST] Base size (24) is below minimum threshold (30). Results may not be statistically reliable.
  - [NORTH] Base size (16) is below minimum threshold (30). Results may not be statistically reliable.
  - [SOUTH] Base size (16) is below minimum threshold (30). Results may not be statistically reliable.
  - [WEST] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension    value  metric  base_n
0  Q_REGION  CENTRAL  2.5238      21
1  Q_REGION     EAST  3.0417      24
2  Q_REGION    NORTH  3.1875      16
3  Q_REGION    SOUTH  2.7500      16
4  Q_REGION     WEST  3.6087      23
```

---

## Q_EASE_OF_USE -> mean by Segment: SEG_HIGH_INCOME
- **Cut ID**: `CUT_13_Q_EASE_OF_USE_mean_BY_SEG_HIGH_INCOME`
- **Base N**: 100
- **Warnings**:
  - [SEG_HIGH_INCOME] Base size (45) is below recommended threshold (100). Interpret results with caution.
  - [Not_SEG_HIGH_INCOME] Base size (55) is below recommended threshold (100). Interpret results with caution.

```text
         dimension                value  metric  base_n
0  SEG_HIGH_INCOME      SEG_HIGH_INCOME  3.3556      45
1  SEG_HIGH_INCOME  Not_SEG_HIGH_INCOME  2.7818      55
```

---

## Q_EASE_OF_USE -> mean (Filtered)
- **Cut ID**: `CUT_13_Q_EASE_OF_USE_mean_FILTERED_SEG_MALE_NORTH`
- **Base N**: 2
- **Warnings**:
  - Base size (2) is below minimum threshold (30). Results may not be statistically reliable.

```text
   mean  std  min  max  count
0   1.0  0.0  1.0  1.0      2
```

---

## Q_EASE_OF_USE -> top2box
- **Cut ID**: `CUT_14_Q_EASE_OF_USE_top2box`
- **Base N**: 100

```text
   top2box_pct  top2box_count  total top_values
0         43.0             43    100     [4, 5]
```

---

## Q_EASE_OF_USE -> top2box by Question: Q_INCOME
- **Cut ID**: `CUT_14_Q_EASE_OF_USE_top2box_BY_Q_INCOME`
- **Base N**: 100
- **Warnings**:
  - [HIGH] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.
  - [LOW] Base size (31) is below recommended threshold (100). Interpret results with caution.
  - [MED] Base size (24) is below minimum threshold (30). Results may not be statistically reliable.
  - [VHIGH] Base size (22) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension  value  metric  base_n
0  Q_INCOME   HIGH   39.13      23
1  Q_INCOME    LOW   29.03      31
2  Q_INCOME    MED   37.50      24
3  Q_INCOME  VHIGH   72.73      22
```

---

## Q_EASE_OF_USE -> top2box by Segment: SEG_MALE_NORTH
- **Cut ID**: `CUT_14_Q_EASE_OF_USE_top2box_BY_SEG_MALE_NORTH`
- **Base N**: 100
- **Warnings**:
  - [SEG_MALE_NORTH] Base size (2) is below minimum threshold (30). Results may not be statistically reliable.
  - [Not_SEG_MALE_NORTH] Base size (98) is below recommended threshold (100). Interpret results with caution.

```text
        dimension               value  metric  base_n
0  SEG_MALE_NORTH      SEG_MALE_NORTH    0.00       2
1  SEG_MALE_NORTH  Not_SEG_MALE_NORTH   43.88      98
```

---

## Q_EASE_OF_USE -> top2box (Filtered)
- **Cut ID**: `CUT_14_Q_EASE_OF_USE_top2box_FILTERED_SEG_TECH_ACTIVE`
- **Base N**: 51
- **Warnings**:
  - Base size (51) is below recommended threshold (100). Interpret results with caution.

```text
   top2box_pct  top2box_count  total top_values
0        49.02             25     51     [4, 5]
```

---

## Q_EASE_OF_USE -> bottom2box
- **Cut ID**: `CUT_15_Q_EASE_OF_USE_bottom2box`
- **Base N**: 100
- **Golden Comparison**: ✅ PASS (Prompt: 'Bottom 2 box for ease of use')

```text
   bottom2box_pct  bottom2box_count  total bottom_values
0            39.0                39    100        [1, 2]
```

---

## Q_EASE_OF_USE -> bottom2box by Question: Q_USAGE_FREQ
- **Cut ID**: `CUT_15_Q_EASE_OF_USE_bottom2box_BY_Q_USAGE_FREQ`
- **Base N**: 100
- **Warnings**:
  - [DAILY] Base size (26) is below minimum threshold (30). Results may not be statistically reliable.
  - [MONTHLY] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.
  - [RARELY] Base size (28) is below minimum threshold (30). Results may not be statistically reliable.
  - [WEEKLY] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.

```text
      dimension    value  metric  base_n
0  Q_USAGE_FREQ    DAILY   38.46      26
1  Q_USAGE_FREQ  MONTHLY   17.39      23
2  Q_USAGE_FREQ   RARELY   42.86      28
3  Q_USAGE_FREQ   WEEKLY   56.52      23
```

---

## Q_EASE_OF_USE -> bottom2box by Segment: SEG_TECH_ACTIVE
- **Cut ID**: `CUT_15_Q_EASE_OF_USE_bottom2box_BY_SEG_TECH_ACTIVE`
- **Base N**: 100
- **Warnings**:
  - [SEG_TECH_ACTIVE] Base size (51) is below recommended threshold (100). Interpret results with caution.
  - [Not_SEG_TECH_ACTIVE] Base size (49) is below recommended threshold (100). Interpret results with caution.

```text
         dimension                value  metric  base_n
0  SEG_TECH_ACTIVE      SEG_TECH_ACTIVE   35.29      51
1  SEG_TECH_ACTIVE  Not_SEG_TECH_ACTIVE   42.86      49
```

---

## Q_EASE_OF_USE -> bottom2box (Filtered)
- **Cut ID**: `CUT_15_Q_EASE_OF_USE_bottom2box_FILTERED_SEG_NOT_LOW_INCOME`
- **Base N**: 69
- **Warnings**:
  - Base size (69) is below recommended threshold (100). Interpret results with caution.

```text
   bottom2box_pct  bottom2box_count  total bottom_values
0           33.33                23     69        [1, 2]
```

---

## Q_VALUE -> frequency
- **Cut ID**: `CUT_16_Q_VALUE_frequency`
- **Base N**: 100
- **Golden Comparison**: ✅ PASS (Prompt: 'Value for money frequency')

```text
   value      label  count  percentage
0      1  Very Poor     16        16.0
1      2       Poor     17        17.0
2      3       Fair     25        25.0
3      4       Good     16        16.0
4      5  Excellent     26        26.0
```

---

## Q_VALUE -> frequency by Question: Q_TENURE
- **Cut ID**: `CUT_16_Q_VALUE_frequency_BY_Q_TENURE`
- **Base N**: 100
- **Warnings**:
  - [LONG] Base size (33) is below recommended threshold (100). Interpret results with caution.
  - [MED] Base size (33) is below recommended threshold (100). Interpret results with caution.
  - [NEW] Base size (34) is below recommended threshold (100). Interpret results with caution.

```text
  dimension value                                                                                                                                                                                                                                                                                                                                      metric  base_n
0  Q_TENURE  LONG  [{'value': 1, 'label': 'Very Poor', 'count': 6, 'percentage': 18.18}, {'value': 2, 'label': 'Poor', 'count': 6, 'percentage': 18.18}, {'value': 3, 'label': 'Fair', 'count': 9, 'percentage': 27.27}, {'value': 4, 'label': 'Good', 'count': 7, 'percentage': 21.21}, {'value': 5, 'label': 'Excellent', 'count': 5, 'percentage': 15.15}]      33
1  Q_TENURE   MED  [{'value': 1, 'label': 'Very Poor', 'count': 5, 'percentage': 15.15}, {'value': 2, 'label': 'Poor', 'count': 8, 'percentage': 24.24}, {'value': 3, 'label': 'Fair', 'count': 7, 'percentage': 21.21}, {'value': 4, 'label': 'Good', 'count': 2, 'percentage': 6.06}, {'value': 5, 'label': 'Excellent', 'count': 11, 'percentage': 33.33}]      33
2  Q_TENURE   NEW  [{'value': 1, 'label': 'Very Poor', 'count': 5, 'percentage': 14.71}, {'value': 2, 'label': 'Poor', 'count': 3, 'percentage': 8.82}, {'value': 3, 'label': 'Fair', 'count': 9, 'percentage': 26.47}, {'value': 4, 'label': 'Good', 'count': 7, 'percentage': 20.59}, {'value': 5, 'label': 'Excellent', 'count': 10, 'percentage': 29.41}]      34
```

---

## Q_VALUE -> frequency by Segment: SEG_NOT_LOW_INCOME
- **Cut ID**: `CUT_16_Q_VALUE_frequency_BY_SEG_NOT_LOW_INCOME`
- **Base N**: 100
- **Warnings**:
  - [SEG_NOT_LOW_INCOME] Base size (69) is below recommended threshold (100). Interpret results with caution.
  - [Not_SEG_NOT_LOW_INCOME] Base size (31) is below recommended threshold (100). Interpret results with caution.

```text
            dimension                   value                                                                                                                                                                                                                                                                                                                                          metric  base_n
0  SEG_NOT_LOW_INCOME      SEG_NOT_LOW_INCOME  [{'value': 1, 'label': 'Very Poor', 'count': 7, 'percentage': 10.14}, {'value': 2, 'label': 'Poor', 'count': 13, 'percentage': 18.84}, {'value': 3, 'label': 'Fair', 'count': 18, 'percentage': 26.09}, {'value': 4, 'label': 'Good', 'count': 11, 'percentage': 15.94}, {'value': 5, 'label': 'Excellent', 'count': 20, 'percentage': 28.99}]      69
1  SEG_NOT_LOW_INCOME  Not_SEG_NOT_LOW_INCOME       [{'value': 1, 'label': 'Very Poor', 'count': 9, 'percentage': 29.03}, {'value': 2, 'label': 'Poor', 'count': 4, 'percentage': 12.9}, {'value': 3, 'label': 'Fair', 'count': 7, 'percentage': 22.58}, {'value': 4, 'label': 'Good', 'count': 5, 'percentage': 16.13}, {'value': 5, 'label': 'Excellent', 'count': 6, 'percentage': 19.35}]      31
```

---

## Q_VALUE -> frequency (Filtered)
- **Cut ID**: `CUT_16_Q_VALUE_frequency_FILTERED_SEG_OR_CONDITION`
- **Base N**: 29
- **Warnings**:
  - Base size (29) is below minimum threshold (30). Results may not be statistically reliable.

```text
   value      label  count  percentage
0      1  Very Poor      1        3.45
1      2       Poor      5       17.24
2      3       Fair      8       27.59
3      4       Good      7       24.14
4      5  Excellent      8       27.59
```

---

## Q_VALUE -> mean
- **Cut ID**: `CUT_17_Q_VALUE_mean`
- **Base N**: 100

```text
   mean    std  min  max  count
0  3.19  1.412  1.0  5.0    100
```

---

## Q_VALUE -> mean by Question: Q_PLAN
- **Cut ID**: `CUT_17_Q_VALUE_mean_BY_Q_PLAN`
- **Base N**: 100
- **Golden Comparison**: ✅ PASS (Prompt: 'Value for money by plan type')
- **Warnings**:
  - [BASIC] Base size (26) is below minimum threshold (30). Results may not be statistically reliable.
  - [ENT] Base size (28) is below minimum threshold (30). Results may not be statistically reliable.
  - [FREE] Base size (20) is below minimum threshold (30). Results may not be statistically reliable.
  - [PRO] Base size (26) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension  value  metric  base_n
0    Q_PLAN  BASIC  3.4615      26
1    Q_PLAN    ENT  3.2857      28
2    Q_PLAN   FREE  3.3500      20
3    Q_PLAN    PRO  2.6923      26
```

---

## Q_VALUE -> mean by Segment: SEG_OR_CONDITION
- **Cut ID**: `CUT_17_Q_VALUE_mean_BY_SEG_OR_CONDITION`
- **Base N**: 100
- **Warnings**:
  - [SEG_OR_CONDITION] Base size (29) is below minimum threshold (30). Results may not be statistically reliable.
  - [Not_SEG_OR_CONDITION] Base size (71) is below recommended threshold (100). Interpret results with caution.

```text
          dimension                 value  metric  base_n
0  SEG_OR_CONDITION      SEG_OR_CONDITION  3.5517      29
1  SEG_OR_CONDITION  Not_SEG_OR_CONDITION  3.0423      71
```

---

## Q_VALUE -> mean (Filtered)
- **Cut ID**: `CUT_17_Q_VALUE_mean_FILTERED_SEG_YOUNG`
- **Base N**: 29
- **Warnings**:
  - Base size (29) is below minimum threshold (30). Results may not be statistically reliable.

```text
     mean     std  min  max  count
0  3.5172  1.3528  1.0  5.0     29
```

---

## Q_VALUE -> top2box
- **Cut ID**: `CUT_18_Q_VALUE_top2box`
- **Base N**: 100

```text
   top2box_pct  top2box_count  total top_values
0         42.0             42    100     [4, 5]
```

---

## Q_VALUE -> top2box by Question: Q_GENDER
- **Cut ID**: `CUT_18_Q_VALUE_top2box_BY_Q_GENDER`
- **Base N**: 100
- **Warnings**:
  - [F] Base size (31) is below recommended threshold (100). Interpret results with caution.
  - [M] Base size (22) is below minimum threshold (30). Results may not be statistically reliable.
  - [NB] Base size (22) is below minimum threshold (30). Results may not be statistically reliable.
  - [PNS] Base size (25) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension value  metric  base_n
0  Q_GENDER     F   51.61      31
1  Q_GENDER     M   40.91      22
2  Q_GENDER    NB   40.91      22
3  Q_GENDER   PNS   32.00      25
```

---

## Q_VALUE -> top2box by Segment: SEG_YOUNG
- **Cut ID**: `CUT_18_Q_VALUE_top2box_BY_SEG_YOUNG`
- **Base N**: 100
- **Warnings**:
  - [SEG_YOUNG] Base size (29) is below minimum threshold (30). Results may not be statistically reliable.
  - [Not_SEG_YOUNG] Base size (71) is below recommended threshold (100). Interpret results with caution.

```text
   dimension          value  metric  base_n
0  SEG_YOUNG      SEG_YOUNG   51.72      29
1  SEG_YOUNG  Not_SEG_YOUNG   38.03      71
```

---

## Q_VALUE -> top2box (Filtered)
- **Cut ID**: `CUT_18_Q_VALUE_top2box_FILTERED_SEG_HIGH_INCOME`
- **Base N**: 45
- **Warnings**:
  - Base size (45) is below recommended threshold (100). Interpret results with caution.

```text
   top2box_pct  top2box_count  total top_values
0        46.67             21     45     [4, 5]
```

---

## Q_VALUE -> bottom2box
- **Cut ID**: `CUT_19_Q_VALUE_bottom2box`
- **Base N**: 100

```text
   bottom2box_pct  bottom2box_count  total bottom_values
0            33.0                33    100        [1, 2]
```

---

## Q_VALUE -> bottom2box by Question: Q_REGION
- **Cut ID**: `CUT_19_Q_VALUE_bottom2box_BY_Q_REGION`
- **Base N**: 100
- **Warnings**:
  - [CENTRAL] Base size (21) is below minimum threshold (30). Results may not be statistically reliable.
  - [EAST] Base size (24) is below minimum threshold (30). Results may not be statistically reliable.
  - [NORTH] Base size (16) is below minimum threshold (30). Results may not be statistically reliable.
  - [SOUTH] Base size (16) is below minimum threshold (30). Results may not be statistically reliable.
  - [WEST] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension    value  metric  base_n
0  Q_REGION  CENTRAL   47.62      21
1  Q_REGION     EAST   20.83      24
2  Q_REGION    NORTH   25.00      16
3  Q_REGION    SOUTH   62.50      16
4  Q_REGION     WEST   17.39      23
```

---

## Q_VALUE -> bottom2box by Segment: SEG_HIGH_INCOME
- **Cut ID**: `CUT_19_Q_VALUE_bottom2box_BY_SEG_HIGH_INCOME`
- **Base N**: 100
- **Warnings**:
  - [SEG_HIGH_INCOME] Base size (45) is below recommended threshold (100). Interpret results with caution.
  - [Not_SEG_HIGH_INCOME] Base size (55) is below recommended threshold (100). Interpret results with caution.

```text
         dimension                value  metric  base_n
0  SEG_HIGH_INCOME      SEG_HIGH_INCOME   24.44      45
1  SEG_HIGH_INCOME  Not_SEG_HIGH_INCOME   40.00      55
```

---

## Q_VALUE -> bottom2box (Filtered)
- **Cut ID**: `CUT_19_Q_VALUE_bottom2box_FILTERED_SEG_MALE_NORTH`
- **Base N**: 2
- **Warnings**:
  - Base size (2) is below minimum threshold (30). Results may not be statistically reliable.

```text
   bottom2box_pct  bottom2box_count  total bottom_values
0            50.0                 1      2        [1, 2]
```

---

## Q_SUPPORT_SAT -> frequency
- **Cut ID**: `CUT_20_Q_SUPPORT_SAT_frequency`
- **Base N**: 100

```text
   value              label  count  percentage
0      1  Very Dissatisfied     23        23.0
1      2       Dissatisfied     16        16.0
2      3            Neutral     16        16.0
3      4          Satisfied     20        20.0
4      5     Very Satisfied     25        25.0
```

---

## Q_SUPPORT_SAT -> frequency by Question: Q_INCOME
- **Cut ID**: `CUT_20_Q_SUPPORT_SAT_frequency_BY_Q_INCOME`
- **Base N**: 100
- **Warnings**:
  - [HIGH] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.
  - [LOW] Base size (31) is below recommended threshold (100). Interpret results with caution.
  - [MED] Base size (24) is below minimum threshold (30). Results may not be statistically reliable.
  - [VHIGH] Base size (22) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension  value                                                                                                                                                                                                                                                                                                                                                                   metric  base_n
0  Q_INCOME   HIGH  [{'value': 1, 'label': 'Very Dissatisfied', 'count': 4, 'percentage': 17.39}, {'value': 2, 'label': 'Dissatisfied', 'count': 6, 'percentage': 26.09}, {'value': 3, 'label': 'Neutral', 'count': 5, 'percentage': 21.74}, {'value': 4, 'label': 'Satisfied', 'count': 3, 'percentage': 13.04}, {'value': 5, 'label': 'Very Satisfied', 'count': 5, 'percentage': 21.74}]      23
1  Q_INCOME    LOW  [{'value': 1, 'label': 'Very Dissatisfied', 'count': 6, 'percentage': 19.35}, {'value': 2, 'label': 'Dissatisfied', 'count': 5, 'percentage': 16.13}, {'value': 3, 'label': 'Neutral', 'count': 6, 'percentage': 19.35}, {'value': 4, 'label': 'Satisfied', 'count': 7, 'percentage': 22.58}, {'value': 5, 'label': 'Very Satisfied', 'count': 7, 'percentage': 22.58}]      31
2  Q_INCOME    MED    [{'value': 1, 'label': 'Very Dissatisfied', 'count': 8, 'percentage': 33.33}, {'value': 2, 'label': 'Dissatisfied', 'count': 2, 'percentage': 8.33}, {'value': 3, 'label': 'Neutral', 'count': 2, 'percentage': 8.33}, {'value': 4, 'label': 'Satisfied', 'count': 4, 'percentage': 16.67}, {'value': 5, 'label': 'Very Satisfied', 'count': 8, 'percentage': 33.33}]      24
3  Q_INCOME  VHIGH  [{'value': 1, 'label': 'Very Dissatisfied', 'count': 5, 'percentage': 22.73}, {'value': 2, 'label': 'Dissatisfied', 'count': 3, 'percentage': 13.64}, {'value': 3, 'label': 'Neutral', 'count': 3, 'percentage': 13.64}, {'value': 4, 'label': 'Satisfied', 'count': 6, 'percentage': 27.27}, {'value': 5, 'label': 'Very Satisfied', 'count': 5, 'percentage': 22.73}]      22
```

---

## Q_SUPPORT_SAT -> frequency by Segment: SEG_MALE_NORTH
- **Cut ID**: `CUT_20_Q_SUPPORT_SAT_frequency_BY_SEG_MALE_NORTH`
- **Base N**: 100
- **Warnings**:
  - [SEG_MALE_NORTH] Base size (2) is below minimum threshold (30). Results may not be statistically reliable.
  - [Not_SEG_MALE_NORTH] Base size (98) is below recommended threshold (100). Interpret results with caution.

```text
        dimension               value                                                                                                                                                                                                                                                                                                                                                                        metric  base_n
0  SEG_MALE_NORTH      SEG_MALE_NORTH                                                                                                                                                                                                                                   [{'value': 2, 'label': 'Dissatisfied', 'count': 1, 'percentage': 50.0}, {'value': 4, 'label': 'Satisfied', 'count': 1, 'percentage': 50.0}]       2
1  SEG_MALE_NORTH  Not_SEG_MALE_NORTH  [{'value': 1, 'label': 'Very Dissatisfied', 'count': 23, 'percentage': 23.47}, {'value': 2, 'label': 'Dissatisfied', 'count': 15, 'percentage': 15.31}, {'value': 3, 'label': 'Neutral', 'count': 16, 'percentage': 16.33}, {'value': 4, 'label': 'Satisfied', 'count': 19, 'percentage': 19.39}, {'value': 5, 'label': 'Very Satisfied', 'count': 25, 'percentage': 25.51}]      98
```

---

## Q_SUPPORT_SAT -> frequency (Filtered)
- **Cut ID**: `CUT_20_Q_SUPPORT_SAT_frequency_FILTERED_SEG_TECH_ACTIVE`
- **Base N**: 51
- **Warnings**:
  - Base size (51) is below recommended threshold (100). Interpret results with caution.

```text
   value              label  count  percentage
0      1  Very Dissatisfied      8       15.69
1      2       Dissatisfied      8       15.69
2      3            Neutral     11       21.57
3      4          Satisfied     10       19.61
4      5     Very Satisfied     14       27.45
```

---

## Q_SUPPORT_SAT -> mean
- **Cut ID**: `CUT_21_Q_SUPPORT_SAT_mean`
- **Base N**: 100
- **Golden Comparison**: ✅ PASS (Prompt: 'Support satisfaction mean score')

```text
   mean     std  min  max  count
0  3.08  1.5154  1.0  5.0    100
```

---

## Q_SUPPORT_SAT -> mean by Question: Q_USAGE_FREQ
- **Cut ID**: `CUT_21_Q_SUPPORT_SAT_mean_BY_Q_USAGE_FREQ`
- **Base N**: 100
- **Warnings**:
  - [DAILY] Base size (26) is below minimum threshold (30). Results may not be statistically reliable.
  - [MONTHLY] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.
  - [RARELY] Base size (28) is below minimum threshold (30). Results may not be statistically reliable.
  - [WEEKLY] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.

```text
      dimension    value  metric  base_n
0  Q_USAGE_FREQ    DAILY  3.0769      26
1  Q_USAGE_FREQ  MONTHLY  3.2609      23
2  Q_USAGE_FREQ   RARELY  3.0714      28
3  Q_USAGE_FREQ   WEEKLY  2.9130      23
```

---

## Q_SUPPORT_SAT -> mean by Segment: SEG_TECH_ACTIVE
- **Cut ID**: `CUT_21_Q_SUPPORT_SAT_mean_BY_SEG_TECH_ACTIVE`
- **Base N**: 100
- **Warnings**:
  - [SEG_TECH_ACTIVE] Base size (51) is below recommended threshold (100). Interpret results with caution.
  - [Not_SEG_TECH_ACTIVE] Base size (49) is below recommended threshold (100). Interpret results with caution.

```text
         dimension                value  metric  base_n
0  SEG_TECH_ACTIVE      SEG_TECH_ACTIVE  3.2745      51
1  SEG_TECH_ACTIVE  Not_SEG_TECH_ACTIVE  2.8776      49
```

---

## Q_SUPPORT_SAT -> mean (Filtered)
- **Cut ID**: `CUT_21_Q_SUPPORT_SAT_mean_FILTERED_SEG_NOT_LOW_INCOME`
- **Base N**: 69
- **Warnings**:
  - Base size (69) is below recommended threshold (100). Interpret results with caution.

```text
    mean     std  min  max  count
0  3.058  1.5519  1.0  5.0     69
```

---

## Q_SUPPORT_SAT -> top2box
- **Cut ID**: `CUT_22_Q_SUPPORT_SAT_top2box`
- **Base N**: 100

```text
   top2box_pct  top2box_count  total top_values
0         45.0             45    100     [4, 5]
```

---

## Q_SUPPORT_SAT -> top2box by Question: Q_TENURE
- **Cut ID**: `CUT_22_Q_SUPPORT_SAT_top2box_BY_Q_TENURE`
- **Base N**: 100
- **Warnings**:
  - [LONG] Base size (33) is below recommended threshold (100). Interpret results with caution.
  - [MED] Base size (33) is below recommended threshold (100). Interpret results with caution.
  - [NEW] Base size (34) is below recommended threshold (100). Interpret results with caution.

```text
  dimension value  metric  base_n
0  Q_TENURE  LONG   42.42      33
1  Q_TENURE   MED   57.58      33
2  Q_TENURE   NEW   35.29      34
```

---

## Q_SUPPORT_SAT -> top2box by Segment: SEG_NOT_LOW_INCOME
- **Cut ID**: `CUT_22_Q_SUPPORT_SAT_top2box_BY_SEG_NOT_LOW_INCOME`
- **Base N**: 100
- **Warnings**:
  - [SEG_NOT_LOW_INCOME] Base size (69) is below recommended threshold (100). Interpret results with caution.
  - [Not_SEG_NOT_LOW_INCOME] Base size (31) is below recommended threshold (100). Interpret results with caution.

```text
            dimension                   value  metric  base_n
0  SEG_NOT_LOW_INCOME      SEG_NOT_LOW_INCOME   44.93      69
1  SEG_NOT_LOW_INCOME  Not_SEG_NOT_LOW_INCOME   45.16      31
```

---

## Q_SUPPORT_SAT -> top2box (Filtered)
- **Cut ID**: `CUT_22_Q_SUPPORT_SAT_top2box_FILTERED_SEG_OR_CONDITION`
- **Base N**: 29
- **Warnings**:
  - Base size (29) is below minimum threshold (30). Results may not be statistically reliable.

```text
   top2box_pct  top2box_count  total top_values
0        51.72             15     29     [4, 5]
```

---

## Q_SUPPORT_SAT -> bottom2box
- **Cut ID**: `CUT_23_Q_SUPPORT_SAT_bottom2box`
- **Base N**: 100

```text
   bottom2box_pct  bottom2box_count  total bottom_values
0            39.0                39    100        [1, 2]
```

---

## Q_SUPPORT_SAT -> bottom2box by Question: Q_PLAN
- **Cut ID**: `CUT_23_Q_SUPPORT_SAT_bottom2box_BY_Q_PLAN`
- **Base N**: 100
- **Warnings**:
  - [BASIC] Base size (26) is below minimum threshold (30). Results may not be statistically reliable.
  - [ENT] Base size (28) is below minimum threshold (30). Results may not be statistically reliable.
  - [FREE] Base size (20) is below minimum threshold (30). Results may not be statistically reliable.
  - [PRO] Base size (26) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension  value  metric  base_n
0    Q_PLAN  BASIC   34.62      26
1    Q_PLAN    ENT   46.43      28
2    Q_PLAN   FREE   20.00      20
3    Q_PLAN    PRO   50.00      26
```

---

## Q_SUPPORT_SAT -> bottom2box by Segment: SEG_OR_CONDITION
- **Cut ID**: `CUT_23_Q_SUPPORT_SAT_bottom2box_BY_SEG_OR_CONDITION`
- **Base N**: 100
- **Warnings**:
  - [SEG_OR_CONDITION] Base size (29) is below minimum threshold (30). Results may not be statistically reliable.
  - [Not_SEG_OR_CONDITION] Base size (71) is below recommended threshold (100). Interpret results with caution.

```text
          dimension                 value  metric  base_n
0  SEG_OR_CONDITION      SEG_OR_CONDITION   37.93      29
1  SEG_OR_CONDITION  Not_SEG_OR_CONDITION   39.44      71
```

---

## Q_SUPPORT_SAT -> bottom2box (Filtered)
- **Cut ID**: `CUT_23_Q_SUPPORT_SAT_bottom2box_FILTERED_SEG_YOUNG`
- **Base N**: 29
- **Warnings**:
  - Base size (29) is below minimum threshold (30). Results may not be statistically reliable.

```text
   bottom2box_pct  bottom2box_count  total bottom_values
0           37.93                11     29        [1, 2]
```

---

## Q_FEATURES_USED -> frequency
- **Cut ID**: `CUT_24_Q_FEATURES_USED_frequency`
- **Base N**: 100
- **Golden Comparison**: ✅ PASS (Prompt: 'How many people use each feature?')

```text
    value                label  count  percentage
0    DASH            Dashboard     40        40.0
1  EXPORT          Data Export     36        36.0
2  COLLAB  Collaboration Tools     33        33.0
3     API      API Integration     32        32.0
4  REPORT            Reporting     29        29.0
5  MOBILE           Mobile App     24        24.0
```

---

## Q_FEATURES_USED -> frequency by Question: Q_GENDER
- **Cut ID**: `CUT_24_Q_FEATURES_USED_frequency_BY_Q_GENDER`
- **Base N**: 100
- **Golden Comparison**: ✅ PASS (Prompt: 'Frequency of features used by gender')
- **Warnings**:
  - [F] Base size (31) is below recommended threshold (100). Interpret results with caution.
  - [M] Base size (22) is below minimum threshold (30). Results may not be statistically reliable.
  - [NB] Base size (22) is below minimum threshold (30). Results may not be statistically reliable.
  - [PNS] Base size (25) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     metric  base_n
0  Q_GENDER     F  [{'value': 'EXPORT', 'label': 'Data Export', 'count': 14, 'percentage': 45.16}, {'value': 'API', 'label': 'API Integration', 'count': 10, 'percentage': 32.26}, {'value': 'DASH', 'label': 'Dashboard', 'count': 10, 'percentage': 32.26}, {'value': 'COLLAB', 'label': 'Collaboration Tools', 'count': 9, 'percentage': 29.03}, {'value': 'REPORT', 'label': 'Reporting', 'count': 7, 'percentage': 22.58}, {'value': 'MOBILE', 'label': 'Mobile App', 'count': 6, 'percentage': 19.35}]      31
1  Q_GENDER     M     [{'value': 'DASH', 'label': 'Dashboard', 'count': 8, 'percentage': 36.36}, {'value': 'COLLAB', 'label': 'Collaboration Tools', 'count': 7, 'percentage': 31.82}, {'value': 'API', 'label': 'API Integration', 'count': 6, 'percentage': 27.27}, {'value': 'MOBILE', 'label': 'Mobile App', 'count': 6, 'percentage': 27.27}, {'value': 'REPORT', 'label': 'Reporting', 'count': 6, 'percentage': 27.27}, {'value': 'EXPORT', 'label': 'Data Export', 'count': 4, 'percentage': 18.18}]      22
2  Q_GENDER    NB    [{'value': 'DASH', 'label': 'Dashboard', 'count': 12, 'percentage': 54.55}, {'value': 'REPORT', 'label': 'Reporting', 'count': 9, 'percentage': 40.91}, {'value': 'COLLAB', 'label': 'Collaboration Tools', 'count': 9, 'percentage': 40.91}, {'value': 'EXPORT', 'label': 'Data Export', 'count': 7, 'percentage': 31.82}, {'value': 'MOBILE', 'label': 'Mobile App', 'count': 6, 'percentage': 27.27}, {'value': 'API', 'label': 'API Integration', 'count': 5, 'percentage': 22.73}]      22
3  Q_GENDER   PNS        [{'value': 'API', 'label': 'API Integration', 'count': 11, 'percentage': 44.0}, {'value': 'EXPORT', 'label': 'Data Export', 'count': 11, 'percentage': 44.0}, {'value': 'DASH', 'label': 'Dashboard', 'count': 10, 'percentage': 40.0}, {'value': 'COLLAB', 'label': 'Collaboration Tools', 'count': 8, 'percentage': 32.0}, {'value': 'REPORT', 'label': 'Reporting', 'count': 7, 'percentage': 28.0}, {'value': 'MOBILE', 'label': 'Mobile App', 'count': 6, 'percentage': 24.0}]      25
```

---

## Q_FEATURES_USED -> frequency by Segment: SEG_YOUNG
- **Cut ID**: `CUT_24_Q_FEATURES_USED_frequency_BY_SEG_YOUNG`
- **Base N**: 100
- **Warnings**:
  - [SEG_YOUNG] Base size (29) is below minimum threshold (30). Results may not be statistically reliable.
  - [Not_SEG_YOUNG] Base size (71) is below recommended threshold (100). Interpret results with caution.

```text
   dimension          value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        metric  base_n
0  SEG_YOUNG      SEG_YOUNG    [{'value': 'API', 'label': 'API Integration', 'count': 14, 'percentage': 48.28}, {'value': 'EXPORT', 'label': 'Data Export', 'count': 13, 'percentage': 44.83}, {'value': 'COLLAB', 'label': 'Collaboration Tools', 'count': 11, 'percentage': 37.93}, {'value': 'DASH', 'label': 'Dashboard', 'count': 10, 'percentage': 34.48}, {'value': 'MOBILE', 'label': 'Mobile App', 'count': 6, 'percentage': 20.69}, {'value': 'REPORT', 'label': 'Reporting', 'count': 4, 'percentage': 13.79}]      29
1  SEG_YOUNG  Not_SEG_YOUNG  [{'value': 'DASH', 'label': 'Dashboard', 'count': 30, 'percentage': 42.25}, {'value': 'REPORT', 'label': 'Reporting', 'count': 25, 'percentage': 35.21}, {'value': 'EXPORT', 'label': 'Data Export', 'count': 23, 'percentage': 32.39}, {'value': 'COLLAB', 'label': 'Collaboration Tools', 'count': 22, 'percentage': 30.99}, {'value': 'API', 'label': 'API Integration', 'count': 18, 'percentage': 25.35}, {'value': 'MOBILE', 'label': 'Mobile App', 'count': 18, 'percentage': 25.35}]      71
```

---

## Q_FEATURES_USED -> frequency (Filtered)
- **Cut ID**: `CUT_24_Q_FEATURES_USED_frequency_FILTERED_SEG_HIGH_INCOME`
- **Base N**: 45
- **Warnings**:
  - Base size (45) is below recommended threshold (100). Interpret results with caution.

```text
    value                label  count  percentage
0    DASH            Dashboard     17       37.78
1     API      API Integration     15       33.33
2  COLLAB  Collaboration Tools     14       31.11
3  REPORT            Reporting     14       31.11
4  EXPORT          Data Export     14       31.11
5  MOBILE           Mobile App      9       20.00
```

---

## Q_PURCHASE_INTENT -> frequency
- **Cut ID**: `CUT_25_Q_PURCHASE_INTENT_frequency`
- **Base N**: 100
- **Golden Comparison**: ✅ PASS (Prompt: 'Purchase intent distribution')

```text
   value          label  count  percentage
0      1  Very Unlikely     17        17.0
1      2       Unlikely     23        23.0
2      3        Neutral     20        20.0
3      4         Likely     17        17.0
4      5    Very Likely     23        23.0
```

---

## Q_PURCHASE_INTENT -> frequency by Question: Q_REGION
- **Cut ID**: `CUT_25_Q_PURCHASE_INTENT_frequency_BY_Q_REGION`
- **Base N**: 100
- **Warnings**:
  - [CENTRAL] Base size (21) is below minimum threshold (30). Results may not be statistically reliable.
  - [EAST] Base size (24) is below minimum threshold (30). Results may not be statistically reliable.
  - [NORTH] Base size (16) is below minimum threshold (30). Results may not be statistically reliable.
  - [SOUTH] Base size (16) is below minimum threshold (30). Results may not be statistically reliable.
  - [WEST] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension    value                                                                                                                                                                                                                                                                                                                                                     metric  base_n
0  Q_REGION  CENTRAL  [{'value': 1, 'label': 'Very Unlikely', 'count': 5, 'percentage': 23.81}, {'value': 2, 'label': 'Unlikely', 'count': 5, 'percentage': 23.81}, {'value': 3, 'label': 'Neutral', 'count': 4, 'percentage': 19.05}, {'value': 4, 'label': 'Likely', 'count': 4, 'percentage': 19.05}, {'value': 5, 'label': 'Very Likely', 'count': 3, 'percentage': 14.29}]      21
1  Q_REGION     EAST     [{'value': 1, 'label': 'Very Unlikely', 'count': 3, 'percentage': 12.5}, {'value': 2, 'label': 'Unlikely', 'count': 6, 'percentage': 25.0}, {'value': 3, 'label': 'Neutral', 'count': 6, 'percentage': 25.0}, {'value': 4, 'label': 'Likely', 'count': 4, 'percentage': 16.67}, {'value': 5, 'label': 'Very Likely', 'count': 5, 'percentage': 20.83}]      24
2  Q_REGION    NORTH                                                                              [{'value': 2, 'label': 'Unlikely', 'count': 4, 'percentage': 25.0}, {'value': 3, 'label': 'Neutral', 'count': 5, 'percentage': 31.25}, {'value': 4, 'label': 'Likely', 'count': 1, 'percentage': 6.25}, {'value': 5, 'label': 'Very Likely', 'count': 6, 'percentage': 37.5}]      16
3  Q_REGION    SOUTH     [{'value': 1, 'label': 'Very Unlikely', 'count': 4, 'percentage': 25.0}, {'value': 2, 'label': 'Unlikely', 'count': 4, 'percentage': 25.0}, {'value': 3, 'label': 'Neutral', 'count': 2, 'percentage': 12.5}, {'value': 4, 'label': 'Likely', 'count': 3, 'percentage': 18.75}, {'value': 5, 'label': 'Very Likely', 'count': 3, 'percentage': 18.75}]      16
4  Q_REGION     WEST  [{'value': 1, 'label': 'Very Unlikely', 'count': 5, 'percentage': 21.74}, {'value': 2, 'label': 'Unlikely', 'count': 4, 'percentage': 17.39}, {'value': 3, 'label': 'Neutral', 'count': 3, 'percentage': 13.04}, {'value': 4, 'label': 'Likely', 'count': 5, 'percentage': 21.74}, {'value': 5, 'label': 'Very Likely', 'count': 6, 'percentage': 26.09}]      23
```

---

## Q_PURCHASE_INTENT -> frequency by Segment: SEG_HIGH_INCOME
- **Cut ID**: `CUT_25_Q_PURCHASE_INTENT_frequency_BY_SEG_HIGH_INCOME`
- **Base N**: 100
- **Golden Comparison**: ✅ PASS (Prompt: 'Break down purchase intent by the 'High Income' segment')
- **Warnings**:
  - [SEG_HIGH_INCOME] Base size (45) is below recommended threshold (100). Interpret results with caution.
  - [Not_SEG_HIGH_INCOME] Base size (55) is below recommended threshold (100). Interpret results with caution.

```text
         dimension                value                                                                                                                                                                                                                                                                                                                                                       metric  base_n
0  SEG_HIGH_INCOME      SEG_HIGH_INCOME   [{'value': 1, 'label': 'Very Unlikely', 'count': 8, 'percentage': 17.78}, {'value': 2, 'label': 'Unlikely', 'count': 11, 'percentage': 24.44}, {'value': 3, 'label': 'Neutral', 'count': 5, 'percentage': 11.11}, {'value': 4, 'label': 'Likely', 'count': 9, 'percentage': 20.0}, {'value': 5, 'label': 'Very Likely', 'count': 12, 'percentage': 26.67}]      45
1  SEG_HIGH_INCOME  Not_SEG_HIGH_INCOME  [{'value': 1, 'label': 'Very Unlikely', 'count': 9, 'percentage': 16.36}, {'value': 2, 'label': 'Unlikely', 'count': 12, 'percentage': 21.82}, {'value': 3, 'label': 'Neutral', 'count': 15, 'percentage': 27.27}, {'value': 4, 'label': 'Likely', 'count': 8, 'percentage': 14.55}, {'value': 5, 'label': 'Very Likely', 'count': 11, 'percentage': 20.0}]      55
```

---

## Q_PURCHASE_INTENT -> frequency (Filtered)
- **Cut ID**: `CUT_25_Q_PURCHASE_INTENT_frequency_FILTERED_SEG_MALE_NORTH`
- **Base N**: 2
- **Warnings**:
  - Base size (2) is below minimum threshold (30). Results may not be statistically reliable.

```text
   value    label  count  percentage
0      3  Neutral      1        50.0
1      4   Likely      1        50.0
```

---

## Q_PURCHASE_INTENT -> mean
- **Cut ID**: `CUT_26_Q_PURCHASE_INTENT_mean`
- **Base N**: 100

```text
   mean     std  min  max  count
0  3.06  1.4201  1.0  5.0    100
```

---

## Q_PURCHASE_INTENT -> mean by Question: Q_INCOME
- **Cut ID**: `CUT_26_Q_PURCHASE_INTENT_mean_BY_Q_INCOME`
- **Base N**: 100
- **Warnings**:
  - [HIGH] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.
  - [LOW] Base size (31) is below recommended threshold (100). Interpret results with caution.
  - [MED] Base size (24) is below minimum threshold (30). Results may not be statistically reliable.
  - [VHIGH] Base size (22) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension  value  metric  base_n
0  Q_INCOME   HIGH  3.0435      23
1  Q_INCOME    LOW  3.0968      31
2  Q_INCOME    MED  2.8750      24
3  Q_INCOME  VHIGH  3.2273      22
```

---

## Q_PURCHASE_INTENT -> mean by Segment: SEG_MALE_NORTH
- **Cut ID**: `CUT_26_Q_PURCHASE_INTENT_mean_BY_SEG_MALE_NORTH`
- **Base N**: 100
- **Warnings**:
  - [SEG_MALE_NORTH] Base size (2) is below minimum threshold (30). Results may not be statistically reliable.
  - [Not_SEG_MALE_NORTH] Base size (98) is below recommended threshold (100). Interpret results with caution.

```text
        dimension               value  metric  base_n
0  SEG_MALE_NORTH      SEG_MALE_NORTH   3.500       2
1  SEG_MALE_NORTH  Not_SEG_MALE_NORTH   3.051      98
```

---

## Q_PURCHASE_INTENT -> mean (Filtered)
- **Cut ID**: `CUT_26_Q_PURCHASE_INTENT_mean_FILTERED_SEG_TECH_ACTIVE`
- **Base N**: 51
- **Warnings**:
  - Base size (51) is below recommended threshold (100). Interpret results with caution.

```text
     mean     std  min  max  count
0  3.1373  1.5365  1.0  5.0     51
```

---

## Q_PURCHASE_INTENT -> top2box
- **Cut ID**: `CUT_27_Q_PURCHASE_INTENT_top2box`
- **Base N**: 100

```text
   top2box_pct  top2box_count  total top_values
0         40.0             40    100     [4, 5]
```

---

## Q_PURCHASE_INTENT -> top2box by Question: Q_USAGE_FREQ
- **Cut ID**: `CUT_27_Q_PURCHASE_INTENT_top2box_BY_Q_USAGE_FREQ`
- **Base N**: 100
- **Warnings**:
  - [DAILY] Base size (26) is below minimum threshold (30). Results may not be statistically reliable.
  - [MONTHLY] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.
  - [RARELY] Base size (28) is below minimum threshold (30). Results may not be statistically reliable.
  - [WEEKLY] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.

```text
      dimension    value  metric  base_n
0  Q_USAGE_FREQ    DAILY   61.54      26
1  Q_USAGE_FREQ  MONTHLY   34.78      23
2  Q_USAGE_FREQ   RARELY   32.14      28
3  Q_USAGE_FREQ   WEEKLY   30.43      23
```

---

## Q_PURCHASE_INTENT -> top2box by Segment: SEG_TECH_ACTIVE
- **Cut ID**: `CUT_27_Q_PURCHASE_INTENT_top2box_BY_SEG_TECH_ACTIVE`
- **Base N**: 100
- **Warnings**:
  - [SEG_TECH_ACTIVE] Base size (51) is below recommended threshold (100). Interpret results with caution.
  - [Not_SEG_TECH_ACTIVE] Base size (49) is below recommended threshold (100). Interpret results with caution.

```text
         dimension                value  metric  base_n
0  SEG_TECH_ACTIVE      SEG_TECH_ACTIVE   43.14      51
1  SEG_TECH_ACTIVE  Not_SEG_TECH_ACTIVE   36.73      49
```

---

## Q_PURCHASE_INTENT -> top2box (Filtered)
- **Cut ID**: `CUT_27_Q_PURCHASE_INTENT_top2box_FILTERED_SEG_NOT_LOW_INCOME`
- **Base N**: 69
- **Warnings**:
  - Base size (69) is below recommended threshold (100). Interpret results with caution.

```text
   top2box_pct  top2box_count  total top_values
0        40.58             28     69     [4, 5]
```

---

## Q_PURCHASE_INTENT -> bottom2box
- **Cut ID**: `CUT_28_Q_PURCHASE_INTENT_bottom2box`
- **Base N**: 100

```text
   bottom2box_pct  bottom2box_count  total bottom_values
0            40.0                40    100        [1, 2]
```

---

## Q_PURCHASE_INTENT -> bottom2box by Question: Q_TENURE
- **Cut ID**: `CUT_28_Q_PURCHASE_INTENT_bottom2box_BY_Q_TENURE`
- **Base N**: 100
- **Warnings**:
  - [LONG] Base size (33) is below recommended threshold (100). Interpret results with caution.
  - [MED] Base size (33) is below recommended threshold (100). Interpret results with caution.
  - [NEW] Base size (34) is below recommended threshold (100). Interpret results with caution.

```text
  dimension value  metric  base_n
0  Q_TENURE  LONG   39.39      33
1  Q_TENURE   MED   39.39      33
2  Q_TENURE   NEW   41.18      34
```

---

## Q_PURCHASE_INTENT -> bottom2box by Segment: SEG_NOT_LOW_INCOME
- **Cut ID**: `CUT_28_Q_PURCHASE_INTENT_bottom2box_BY_SEG_NOT_LOW_INCOME`
- **Base N**: 100
- **Warnings**:
  - [SEG_NOT_LOW_INCOME] Base size (69) is below recommended threshold (100). Interpret results with caution.
  - [Not_SEG_NOT_LOW_INCOME] Base size (31) is below recommended threshold (100). Interpret results with caution.

```text
            dimension                   value  metric  base_n
0  SEG_NOT_LOW_INCOME      SEG_NOT_LOW_INCOME   42.03      69
1  SEG_NOT_LOW_INCOME  Not_SEG_NOT_LOW_INCOME   35.48      31
```

---

## Q_PURCHASE_INTENT -> bottom2box (Filtered)
- **Cut ID**: `CUT_28_Q_PURCHASE_INTENT_bottom2box_FILTERED_SEG_OR_CONDITION`
- **Base N**: 29
- **Warnings**:
  - Base size (29) is below minimum threshold (30). Results may not be statistically reliable.

```text
   bottom2box_pct  bottom2box_count  total bottom_values
0           27.59                 8     29        [1, 2]
```

---

## Q_USAGE_FREQ -> frequency
- **Cut ID**: `CUT_29_Q_USAGE_FREQ_frequency`
- **Base N**: 100

```text
     value    label  count  percentage
0   RARELY   Rarely     28        28.0
1    DAILY    Daily     26        26.0
2  MONTHLY  Monthly     23        23.0
3   WEEKLY   Weekly     23        23.0
```

---

## Q_USAGE_FREQ -> frequency by Question: Q_PLAN
- **Cut ID**: `CUT_29_Q_USAGE_FREQ_frequency_BY_Q_PLAN`
- **Base N**: 100
- **Warnings**:
  - [BASIC] Base size (26) is below minimum threshold (30). Results may not be statistically reliable.
  - [ENT] Base size (28) is below minimum threshold (30). Results may not be statistically reliable.
  - [FREE] Base size (20) is below minimum threshold (30). Results may not be statistically reliable.
  - [PRO] Base size (26) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension  value                                                                                                                                                                                                                                                                                                  metric  base_n
0    Q_PLAN  BASIC    [{'value': 'WEEKLY', 'label': 'Weekly', 'count': 9, 'percentage': 34.62}, {'value': 'MONTHLY', 'label': 'Monthly', 'count': 6, 'percentage': 23.08}, {'value': 'RARELY', 'label': 'Rarely', 'count': 6, 'percentage': 23.08}, {'value': 'DAILY', 'label': 'Daily', 'count': 5, 'percentage': 19.23}]      26
1    Q_PLAN    ENT  [{'value': 'RARELY', 'label': 'Rarely', 'count': 10, 'percentage': 35.71}, {'value': 'MONTHLY', 'label': 'Monthly', 'count': 10, 'percentage': 35.71}, {'value': 'WEEKLY', 'label': 'Weekly', 'count': 4, 'percentage': 14.29}, {'value': 'DAILY', 'label': 'Daily', 'count': 4, 'percentage': 14.29}]      28
2    Q_PLAN   FREE        [{'value': 'DAILY', 'label': 'Daily', 'count': 9, 'percentage': 45.0}, {'value': 'RARELY', 'label': 'Rarely', 'count': 5, 'percentage': 25.0}, {'value': 'WEEKLY', 'label': 'Weekly', 'count': 3, 'percentage': 15.0}, {'value': 'MONTHLY', 'label': 'Monthly', 'count': 3, 'percentage': 15.0}]      20
3    Q_PLAN    PRO    [{'value': 'DAILY', 'label': 'Daily', 'count': 8, 'percentage': 30.77}, {'value': 'WEEKLY', 'label': 'Weekly', 'count': 7, 'percentage': 26.92}, {'value': 'RARELY', 'label': 'Rarely', 'count': 7, 'percentage': 26.92}, {'value': 'MONTHLY', 'label': 'Monthly', 'count': 4, 'percentage': 15.38}]      26
```

---

## Q_USAGE_FREQ -> frequency by Segment: SEG_OR_CONDITION
- **Cut ID**: `CUT_29_Q_USAGE_FREQ_frequency_BY_SEG_OR_CONDITION`
- **Base N**: 100
- **Warnings**:
  - [SEG_OR_CONDITION] Base size (29) is below minimum threshold (30). Results may not be statistically reliable.
  - [Not_SEG_OR_CONDITION] Base size (71) is below recommended threshold (100). Interpret results with caution.

```text
          dimension                 value                                                                                                                                                                                                                                                                                                    metric  base_n
0  SEG_OR_CONDITION      SEG_OR_CONDITION      [{'value': 'DAILY', 'label': 'Daily', 'count': 9, 'percentage': 31.03}, {'value': 'MONTHLY', 'label': 'Monthly', 'count': 7, 'percentage': 24.14}, {'value': 'WEEKLY', 'label': 'Weekly', 'count': 7, 'percentage': 24.14}, {'value': 'RARELY', 'label': 'Rarely', 'count': 6, 'percentage': 20.69}]      29
1  SEG_OR_CONDITION  Not_SEG_OR_CONDITION  [{'value': 'RARELY', 'label': 'Rarely', 'count': 22, 'percentage': 30.99}, {'value': 'DAILY', 'label': 'Daily', 'count': 17, 'percentage': 23.94}, {'value': 'WEEKLY', 'label': 'Weekly', 'count': 16, 'percentage': 22.54}, {'value': 'MONTHLY', 'label': 'Monthly', 'count': 16, 'percentage': 22.54}]      71
```

---

## Q_USAGE_FREQ -> frequency (Filtered)
- **Cut ID**: `CUT_29_Q_USAGE_FREQ_frequency_FILTERED_SEG_YOUNG`
- **Base N**: 29
- **Warnings**:
  - Base size (29) is below minimum threshold (30). Results may not be statistically reliable.

```text
     value    label  count  percentage
0    DAILY    Daily      9       31.03
1   RARELY   Rarely      8       27.59
2   WEEKLY   Weekly      7       24.14
3  MONTHLY  Monthly      5       17.24
```

---

## Q_TENURE -> frequency
- **Cut ID**: `CUT_30_Q_TENURE_frequency`
- **Base N**: 100
- **Golden Comparison**: ✅ PASS (Prompt: 'Tenure distribution among customers')

```text
  value               label  count  percentage
0   NEW  Less than 6 months     34        34.0
1   MED  6 months - 2 years     33        33.0
2  LONG            2+ years     33        33.0
```

---

## Q_TENURE -> frequency by Question: Q_GENDER
- **Cut ID**: `CUT_30_Q_TENURE_frequency_BY_Q_GENDER`
- **Base N**: 100
- **Warnings**:
  - [F] Base size (31) is below recommended threshold (100). Interpret results with caution.
  - [M] Base size (22) is below minimum threshold (30). Results may not be statistically reliable.
  - [NB] Base size (22) is below minimum threshold (30). Results may not be statistically reliable.
  - [PNS] Base size (25) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension value                                                                                                                                                                                                                                          metric  base_n
0  Q_GENDER     F  [{'value': 'MED', 'label': '6 months - 2 years', 'count': 18, 'percentage': 58.06}, {'value': 'NEW', 'label': 'Less than 6 months', 'count': 7, 'percentage': 22.58}, {'value': 'LONG', 'label': '2+ years', 'count': 6, 'percentage': 19.35}]      31
1  Q_GENDER     M   [{'value': 'LONG', 'label': '2+ years', 'count': 11, 'percentage': 50.0}, {'value': 'NEW', 'label': 'Less than 6 months', 'count': 7, 'percentage': 31.82}, {'value': 'MED', 'label': '6 months - 2 years', 'count': 4, 'percentage': 18.18}]      22
2  Q_GENDER    NB   [{'value': 'NEW', 'label': 'Less than 6 months', 'count': 11, 'percentage': 50.0}, {'value': 'LONG', 'label': '2+ years', 'count': 8, 'percentage': 36.36}, {'value': 'MED', 'label': '6 months - 2 years', 'count': 3, 'percentage': 13.64}]      22
3  Q_GENDER   PNS      [{'value': 'NEW', 'label': 'Less than 6 months', 'count': 9, 'percentage': 36.0}, {'value': 'MED', 'label': '6 months - 2 years', 'count': 8, 'percentage': 32.0}, {'value': 'LONG', 'label': '2+ years', 'count': 8, 'percentage': 32.0}]      25
```

---

## Q_TENURE -> frequency by Segment: SEG_YOUNG
- **Cut ID**: `CUT_30_Q_TENURE_frequency_BY_SEG_YOUNG`
- **Base N**: 100
- **Warnings**:
  - [SEG_YOUNG] Base size (29) is below minimum threshold (30). Results may not be statistically reliable.
  - [Not_SEG_YOUNG] Base size (71) is below recommended threshold (100). Interpret results with caution.

```text
   dimension          value                                                                                                                                                                                                                                           metric  base_n
0  SEG_YOUNG      SEG_YOUNG  [{'value': 'MED', 'label': '6 months - 2 years', 'count': 13, 'percentage': 44.83}, {'value': 'NEW', 'label': 'Less than 6 months', 'count': 10, 'percentage': 34.48}, {'value': 'LONG', 'label': '2+ years', 'count': 6, 'percentage': 20.69}]      29
1  SEG_YOUNG  Not_SEG_YOUNG  [{'value': 'LONG', 'label': '2+ years', 'count': 27, 'percentage': 38.03}, {'value': 'NEW', 'label': 'Less than 6 months', 'count': 24, 'percentage': 33.8}, {'value': 'MED', 'label': '6 months - 2 years', 'count': 20, 'percentage': 28.17}]      71
```

---

## Q_TENURE -> frequency (Filtered)
- **Cut ID**: `CUT_30_Q_TENURE_frequency_FILTERED_SEG_HIGH_INCOME`
- **Base N**: 45
- **Warnings**:
  - Base size (45) is below recommended threshold (100). Interpret results with caution.

```text
  value               label  count  percentage
0  LONG            2+ years     16       35.56
1   NEW  Less than 6 months     16       35.56
2   MED  6 months - 2 years     13       28.89
```

---

## Q_PLAN -> frequency
- **Cut ID**: `CUT_31_Q_PLAN_frequency`
- **Base N**: 100

```text
   value         label  count  percentage
0    ENT    Enterprise     28        28.0
1  BASIC         Basic     26        26.0
2    PRO  Professional     26        26.0
3   FREE          Free     20        20.0
```

---

## Q_PLAN -> frequency by Question: Q_REGION
- **Cut ID**: `CUT_31_Q_PLAN_frequency_BY_Q_REGION`
- **Base N**: 100
- **Warnings**:
  - [CENTRAL] Base size (21) is below minimum threshold (30). Results may not be statistically reliable.
  - [EAST] Base size (24) is below minimum threshold (30). Results may not be statistically reliable.
  - [NORTH] Base size (16) is below minimum threshold (30). Results may not be statistically reliable.
  - [SOUTH] Base size (16) is below minimum threshold (30). Results may not be statistically reliable.
  - [WEST] Base size (23) is below minimum threshold (30). Results may not be statistically reliable.

```text
  dimension    value                                                                                                                                                                                                                                                                                              metric  base_n
0  Q_REGION  CENTRAL   [{'value': 'BASIC', 'label': 'Basic', 'count': 8, 'percentage': 38.1}, {'value': 'ENT', 'label': 'Enterprise', 'count': 5, 'percentage': 23.81}, {'value': 'PRO', 'label': 'Professional', 'count': 5, 'percentage': 23.81}, {'value': 'FREE', 'label': 'Free', 'count': 3, 'percentage': 14.29}]      21
1  Q_REGION     EAST    [{'value': 'ENT', 'label': 'Enterprise', 'count': 8, 'percentage': 33.33}, {'value': 'FREE', 'label': 'Free', 'count': 6, 'percentage': 25.0}, {'value': 'PRO', 'label': 'Professional', 'count': 6, 'percentage': 25.0}, {'value': 'BASIC', 'label': 'Basic', 'count': 4, 'percentage': 16.67}]      24
2  Q_REGION    NORTH     [{'value': 'BASIC', 'label': 'Basic', 'count': 6, 'percentage': 37.5}, {'value': 'FREE', 'label': 'Free', 'count': 5, 'percentage': 31.25}, {'value': 'ENT', 'label': 'Enterprise', 'count': 4, 'percentage': 25.0}, {'value': 'PRO', 'label': 'Professional', 'count': 1, 'percentage': 6.25}]      16
3  Q_REGION    SOUTH    [{'value': 'PRO', 'label': 'Professional', 'count': 6, 'percentage': 37.5}, {'value': 'ENT', 'label': 'Enterprise', 'count': 4, 'percentage': 25.0}, {'value': 'FREE', 'label': 'Free', 'count': 3, 'percentage': 18.75}, {'value': 'BASIC', 'label': 'Basic', 'count': 3, 'percentage': 18.75}]      16
4  Q_REGION     WEST  [{'value': 'PRO', 'label': 'Professional', 'count': 8, 'percentage': 34.78}, {'value': 'ENT', 'label': 'Enterprise', 'count': 7, 'percentage': 30.43}, {'value': 'BASIC', 'label': 'Basic', 'count': 5, 'percentage': 21.74}, {'value': 'FREE', 'label': 'Free', 'count': 3, 'percentage': 13.04}]      23
```

---

## Q_PLAN -> frequency by Segment: SEG_HIGH_INCOME
- **Cut ID**: `CUT_31_Q_PLAN_frequency_BY_SEG_HIGH_INCOME`
- **Base N**: 100
- **Warnings**:
  - [SEG_HIGH_INCOME] Base size (45) is below recommended threshold (100). Interpret results with caution.
  - [Not_SEG_HIGH_INCOME] Base size (55) is below recommended threshold (100). Interpret results with caution.

```text
         dimension                value                                                                                                                                                                                                                                                                                                  metric  base_n
0  SEG_HIGH_INCOME      SEG_HIGH_INCOME     [{'value': 'ENT', 'label': 'Enterprise', 'count': 15, 'percentage': 33.33}, {'value': 'BASIC', 'label': 'Basic', 'count': 14, 'percentage': 31.11}, {'value': 'PRO', 'label': 'Professional', 'count': 9, 'percentage': 20.0}, {'value': 'FREE', 'label': 'Free', 'count': 7, 'percentage': 15.56}]      45
1  SEG_HIGH_INCOME  Not_SEG_HIGH_INCOME  [{'value': 'PRO', 'label': 'Professional', 'count': 17, 'percentage': 30.91}, {'value': 'FREE', 'label': 'Free', 'count': 13, 'percentage': 23.64}, {'value': 'ENT', 'label': 'Enterprise', 'count': 13, 'percentage': 23.64}, {'value': 'BASIC', 'label': 'Basic', 'count': 12, 'percentage': 21.82}]      55
```

---

## Q_PLAN -> frequency (Filtered)
- **Cut ID**: `CUT_31_Q_PLAN_frequency_FILTERED_SEG_MALE_NORTH`
- **Base N**: 2
- **Warnings**:
  - Base size (2) is below minimum threshold (30). Results may not be statistically reliable.

```text
   value  label  count  percentage
0  BASIC  Basic      2       100.0
```

---

