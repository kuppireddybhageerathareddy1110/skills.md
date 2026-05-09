---
name: data-scientist-workflow
description: >
  End-to-end data science project workflow: problem definition, EDA, feature engineering,
  model training, evaluation, hyperparameter tuning, cross-validation, deployment, and monitoring.
  Use this skill whenever user asks to build a machine learning model, run a data science project,
  predict something from data, analyze churn/fraud/demand/risk, create a prediction pipeline,
  evaluate a model, or deploy ML to production. Also triggers for: "how do I approach this ML problem",
  "help me with my data science project", "build me a classifier/regressor", "what features should I engineer",
  "how do I tune my model", "set up model monitoring", or any request that involves training,
  evaluating, or productionizing a predictive model. Covers imbalanced datasets, business impact
  framing, and production API/batch job patterns.
---

# Data Scientist End-to-End Workflow

Complete guide for ML projects from business problem to production. Follow phases in order;
skip phases only when user explicitly has those artifacts already.

---

## Phase 1: Problem Definition

**Before any code**, establish:

1. **Business objective** — What decision changes if model works? Who uses predictions?
2. **Success metrics** — Primary (e.g. reduce churn 20%), secondary (ROI constraint)
3. **ML task type** — Classification / regression / clustering / ranking?
4. **Constraints** — Interpretability, latency, bias requirements, data freshness
5. **Baseline** — Rule-based or naive model to beat (always define before ML)

**Output**: Written problem statement with target metric and baseline. Never skip this.

**Common pitfalls**:
- Accuracy on imbalanced data = misleading. Use AUPRC / recall / F1
- "Maximize recall" and "minimize cost" often conflict → get explicit tradeoff from business
- Define prediction horizon (predict churn in next 30 days, not "eventually")

---

## Phase 2: Data Inventory & EDA

### 2.1 Data Inventory
List all tables/sources. For each: columns, update frequency, join keys, known quality issues.

### 2.2 EDA Checklist

```python
# Always run these checks:
print(df.shape)
print(df.dtypes)
print(df.isnull().sum() / len(df) * 100)  # Missing %
print(df.describe())
print(df['target'].value_counts(normalize=True))  # Class balance
```

**Key EDA outputs**:
- Class distribution → imbalance ratio → choose right metric
- Missing data patterns → imputation strategy
- Outlier presence → cap or remove strategy
- Feature correlations with target → initial signal assessment
- Categorical cardinality → encoding strategy

**Imbalanced data flag**: If minority class < 10%, switch to AUPRC metric, use `class_weight='balanced'` or `scale_pos_weight`.

---

## Phase 3: Data Preprocessing & Feature Engineering

### 3.1 Cleaning Order
1. Fix data types (dates → datetime, categories → category)
2. Handle missing values (KNN imputer for numerical; mode for categorical)
3. Cap outliers (IQR method: `clip(Q1 - 3*IQR, Q3 + 3*IQR)`)
4. Remove invalid rows (negative counts, accounts too new for label)

### 3.2 Feature Engineering Categories

| Category | Examples |
|----------|---------|
| Engagement | activity_ratio, login_frequency, api_intensity |
| Temporal | tenure_days, cohort_month, is_peak_season |
| Segment | is_premium, region dummies |
| Interaction | premium × activity, new × inactive |
| Composite | weighted engagement_score, health_score 0-100 |

**Rules**:
- Engineer features that encode business intuition first
- Create ratio features (X per active day > raw X)
- Interaction features for high-value segments
- Check new feature correlation with target before keeping

### 3.3 Preprocessing Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numerical_features),
    ('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_features)
])

# Fit ONLY on train. Transform val/test with fitted preprocessor.
X_train_scaled = preprocessor.fit_transform(X_train)
X_val_scaled = preprocessor.transform(X_val)   # Never refit!
```

---

## Phase 4: Train/Val/Test Split

**Always stratified**. For imbalanced: manually split each class, then combine.

```python
from sklearn.model_selection import train_test_split

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.4, stratify=y, random_state=42
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=42
)
# Result: 60/20/20 split
```

**Rules**:
- Temporal data → time-based split (no random shuffle)
- Verify churn % matches across all splits
- Save splits to disk; never regenerate mid-project

---

## Phase 5: Model Training

### 5.1 Model Selection Strategy

Start with 5 models in order of complexity:

```python
models = {
    'Logistic Regression': LogisticRegression(class_weight='balanced', max_iter=1000),
    'Random Forest': RandomForestClassifier(class_weight='balanced', n_estimators=100),
    'Gradient Boosting': GradientBoostingClassifier(n_estimators=100),
    'XGBoost': XGBClassifier(scale_pos_weight=neg/pos, n_estimators=100),
    'AdaBoost': AdaBoostClassifier(n_estimators=100)
}
```

**Ranking metric**: AUPRC for imbalanced, RMSE for regression, ROC-AUC for balanced classification.

### 5.2 Evaluation Per Model

```python
from sklearn.metrics import precision_recall_curve, auc, roc_auc_score

y_proba = model.predict_proba(X_val)[:, 1]
prec, rec, _ = precision_recall_curve(y_val, y_proba)
auprc = auc(rec, prec)
roc_auc = roc_auc_score(y_val, y_proba)
```

---

## Phase 6: Comprehensive Evaluation

Run on **test set only** after model selected. Never tune on test set.

### 6.1 Metrics to Report

| Metric | When to use | Interpretation |
|--------|-------------|----------------|
| AUPRC | Imbalanced classification | Higher = better at finding rare events |
| ROC-AUC | Any classification | >0.85 good, >0.90 excellent |
| Precision | When FP is costly | Of flagged customers, % actually churn |
| Recall | When FN is costly | Of actual churners, % we catch |
| Confusion Matrix | Always | Shows TP/FP/TN/FN counts |

### 6.2 Threshold Analysis

Default 0.5 threshold rarely optimal. Run sweep:

```python
for threshold in [0.3, 0.4, 0.5, 0.6, 0.7]:
    y_pred = (y_proba >= threshold).astype(int)
    # Report precision, recall, F1, num_flagged
```

Choose threshold based on business cost tradeoff (recall vs. retention budget).

### 6.3 Business Impact

Always translate model metrics to dollars:
```
customers_saved = TP × retention_success_rate
revenue_saved = customers_saved × customer_LTV
ROI = (revenue_saved - campaign_cost) / campaign_cost
```

### 6.4 Feature Importance

```python
importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)
```

Top features → validate with domain experts → sanity check (no data leakage signals).

---

## Phase 7: Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'max_depth': [3, 5, 7],
    'learning_rate': [0.05, 0.1],
    'n_estimators': [100, 200],
    'subsample': [0.8, 1.0],
}

grid_search = GridSearchCV(
    model, param_grid,
    cv=5, scoring='roc_auc',
    n_jobs=-1
)
grid_search.fit(X_train_scaled, y_train)
```

**Tips**:
- Start with wide grid, then narrow around best
- Use RandomizedSearchCV for large grids (>500 combos)
- Tune on train+val, evaluate final on test

---

## Phase 8: Cross-Validation

```python
from sklearn.model_selection import StratifiedKFold, cross_validate

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_results = cross_validate(model, X_train_scaled, y_train,
                             cv=skf, scoring=['roc_auc', 'precision', 'recall', 'f1'],
                             return_train_score=True)

# Check for overfitting
for metric in ['roc_auc', 'precision']:
    train = cv_results[f'train_{metric}'].mean()
    test = cv_results[f'test_{metric}'].mean()
    gap = train - test
    print(f"{metric}: train={train:.3f} test={test:.3f} gap={gap:.3f}")
    # Gap > 0.05 = overfitting warning
```

---

## Phase 9: Deployment

### 9.1 Production Pipeline Class

```python
class PredictionPipeline:
    def __init__(self, model_path, preprocessor_path):
        self.model = pickle.load(open(model_path, 'rb'))
        self.preprocessor = pickle.load(open(preprocessor_path, 'rb'))
    
    def predict(self, customer_data, threshold=0.4):
        X_scaled = self.preprocessor.transform(customer_data)
        proba = self.model.predict_proba(X_scaled)[0, 1]
        return {
            'churn_probability': float(proba),
            'will_churn': bool(proba >= threshold),
            'risk_tier': self._risk_tier(proba),
            'recommendation': self._recommend(proba, threshold)
        }
    
    def batch_predict(self, df, threshold=0.4):
        X_scaled = self.preprocessor.transform(df)
        probas = self.model.predict_proba(X_scaled)[:, 1]
        return pd.DataFrame({
            'customer_id': df['customer_id'],
            'churn_probability': probas,
            'will_churn': probas >= threshold,
            'risk_tier': pd.cut(probas, bins=[0,.3,.5,.7,1], labels=['Low','Medium','High','Critical'])
        })
```

### 9.2 FastAPI Service (minimal)

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
pipeline = PredictionPipeline('models/model.pkl', 'models/preprocessor.pkl')

@app.post("/predict")
async def predict(customer: CustomerData):
    return pipeline.predict(pd.DataFrame([customer.dict()]))

@app.get("/health")
async def health():
    return {"status": "healthy", "model_version": "1.0"}
```

### 9.3 Scheduled Batch Job

```python
from apscheduler.schedulers.background import BackgroundScheduler

def daily_job():
    customers = fetch_active_customers()
    predictions = pipeline.batch_predict(customers)
    save_to_db(predictions)
    high_risk = predictions[predictions['risk_tier'].isin(['High','Critical'])]
    send_alerts(high_risk)

scheduler = BackgroundScheduler()
scheduler.add_job(daily_job, 'cron', hour=2)
scheduler.start()
```

---

## Phase 10: Monitoring & Retraining

### 10.1 Monitor Three Things

| What | How | Alert threshold |
|------|-----|-----------------|
| **Data drift** | Compare feature distributions weekly | >20% mean shift |
| **Prediction drift** | Track mean churn probability daily | >15% from baseline |
| **Performance decay** | Compare AUC on labeled actuals | >5% AUC drop |

### 10.2 Retraining Triggers

- AUC drops >5% from launch baseline
- Data drift detected in key features
- Business context changes (pricing, product)
- Scheduled: monthly for fast-changing domains

### 10.3 Retraining Strategy

```python
# Include new data, keep historical
new_data = fetch_data(start=last_train_date, end=today)
full_data = pd.concat([historical_data, new_data])

# Retrain with same pipeline
# Compare new model vs old on held-out set
# Deploy only if new model beats old by >1% AUC
```

---

## Phase 11: Business Action Plan

Translate predictions to actions:

```python
def get_action(churn_prob):
    if churn_prob > 0.8: return "Urgent: executive call + $200 offer"
    if churn_prob > 0.6: return "High: personalized email + $100 discount"
    if churn_prob > 0.4: return "Medium: loyalty program outreach"
    return "Low: standard engagement"
```

Deliver to business team as:
- Prioritized customer list with actions
- Expected cost and ROI per segment
- Weekly tracking dashboard

---

## Quick Reference

| Phase | Key Output | Common Mistake |
|-------|-----------|----------------|
| 1. Problem | Baseline + success metric | Skipping baseline |
| 2. EDA | Class balance, missing %, correlations | Using accuracy on imbalanced data |
| 3. Features | 20+ engineered features | Leaking future data into features |
| 4. Split | Stratified 60/20/20 | Random split on temporal data |
| 5. Training | 5 models compared | Tuning on test set |
| 6. Evaluation | AUPRC + business ROI | Single threshold, no sweep |
| 7. Tuning | GridSearchCV | Overfitting to val set |
| 8. CV | 5-fold stratified | Not checking train/test gap |
| 9. Deploy | Pipeline class + API | Forgetting to save preprocessor |
| 10. Monitor | Drift + decay alerts | No monitoring = silent failure |
| 11. Actions | Prioritized list with costs | Model without business integration |

**Total timeline**: 6–8 weeks for full project. Phases 1–4 = ~40% of time. Never rush EDA.
