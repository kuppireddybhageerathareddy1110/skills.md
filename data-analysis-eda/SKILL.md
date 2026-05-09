---
name: data-analysis-eda
description: |-
  Performs automated exploratory data analysis (EDA) with statistical validation, anomaly detection, correlation analysis, and business insights. Use this skill whenever the user uploads a dataset (CSV, Excel, JSON) or shares data and asks to "analyze", "explore", "profile", "find patterns", "check data quality", "visualize", or "what's interesting in this data?". Also triggers for: "find outliers", "check for missing values", "what correlates with X", "is this data clean?", or any request to understand a dataset before modeling.
---

# Skill: data-analysis-eda

## Purpose
Comprehensive dataset profiling: structure, quality, distributions, correlations, anomalies, and actionable business insights — all in one structured report.

## Input Forms
- CSV / Excel / JSON file uploaded
- Pandas DataFrame description or `.head()` output pasted
- Column names + sample rows described in text
- SQL query result pasted as table

---

## Analysis Process

### Step 1: Dataset Overview
Report immediately:
- Shape: rows × columns
- Memory usage estimate
- Data types per column (numeric, categorical, datetime, text, boolean)
- % missing per column
- Exact duplicate row count

### Step 2: Per-Column Analysis

#### Numeric Columns — always compute:
| Stat | Why |
|------|-----|
| Mean / Median / Mode | Central tendency + skew signal |
| Std dev / IQR | Spread |
| Min / Max / Percentiles (1, 5, 25, 75, 95, 99) | Full distribution |
| Skewness / Kurtosis | Shape |
| Outlier count (IQR method: < Q1−1.5×IQR or > Q3+1.5×IQR) | Anomalies |
| Normality (Shapiro-Wilk if n<5000, else KS test) | Model assumption check |

Flag:
- **High skew** (|skewness| > 2): recommend log transform
- **Outliers > 1%**: investigate, may need capping
- **Zero-inflated**: many exact zeros, separate model may be needed

#### Categorical Columns — always compute:
| Stat | Why |
|------|-----|
| Cardinality (unique count) | High card = encoding risk |
| Value frequencies (top 10) | Dominant categories |
| % of rows in top category | Imbalance signal |
| Rare categories (< 1% prevalence) | May need grouping |

Flag:
- **Cardinality > 50**: high-cardinality, warn before one-hot encoding
- **Single dominant value > 95%**: near-constant, low predictive value
- **Free text detected**: recommend NLP treatment

#### Datetime Columns:
- Date range and duration
- Gaps or irregular intervals
- Seasonality signals (hourly/daily/weekly/monthly patterns)
- Timezone consistency

### Step 3: Missing Data Analysis
For each column with missing values:
- Count + percentage
- Pattern: **MCAR** (random), **MAR** (depends on other cols), **MNAR** (depends on value itself)
- Recommended action: drop row / impute mean-median-mode / model-based imputation / flag as separate feature

### Step 4: Correlation Analysis
- Pearson correlation matrix for numeric columns
- Flag pairs with |r| > 0.8 (multicollinearity risk)
- Flag pairs with |r| > 0.5 with target variable (if target identified)
- Cramér's V for categorical pairs (if asked or if target is categorical)
- Mutual information for non-linear relationships (mention if relevant)

### Step 5: Anomaly Detection
Run at least two methods:
1. **IQR method**: univariate, per numeric column
2. **Z-score**: flag rows with |z| > 3 in any numeric column
3. **Contextual**: flag combinations that are unusual (e.g., age=5 + job=CEO)

Report: count of anomalous rows, which columns triggered, sample examples.

### Step 6: Business Insights
Extract 3–5 plain-language findings that matter:
- Strongest predictors of any target column
- Surprising distributions or concentrations
- Data quality issues that would break a model
- Actionable segments visible in the data
- Temporal trends if datetime present

---

## Output Format

### 📊 EDA Report: `{dataset name}`
**Shape**: N rows × M columns | **Quality Score**: X/10 | **Missing**: X%

---

#### Dataset Overview
_(table of columns, types, missing %, unique count)_

---

#### Key Findings (plain language, top 5)
1. ...
2. ...

---

#### Numeric Column Profiles
_(one section per numeric column with stats table + flags)_

#### Categorical Column Profiles
_(one section per categorical column with frequency table + flags)_

---

#### Missing Data Summary
| Column | Missing % | Pattern | Recommendation |
|--------|-----------|---------|---------------|

---

#### Correlation Highlights
- Top positive correlations: ...
- Top negative correlations: ...
- Multicollinearity risks: ...

---

#### Anomalies Detected
N rows flagged. Examples: ...

---

#### Data Preparation Checklist
- [ ] Remove N exact duplicates
- [ ] Impute / drop missing in: [columns]
- [ ] Cap outliers in: [columns]
- [ ] Log-transform: [columns]
- [ ] Encode categoricals: [columns]
- [ ] Drop near-constant: [columns]

---

## Quality Scoring
Start at 10. Deduct:
- Missing > 20% in any column: −1
- Duplicate rows > 1%: −0.5
- Outlier rate > 2%: −0.5
- High cardinality categoricals unaddressed: −0.5
- Zero variance columns: −0.5

## Tone
Lead with the most important finding. Be specific with numbers. Every flag gets a recommended action.
