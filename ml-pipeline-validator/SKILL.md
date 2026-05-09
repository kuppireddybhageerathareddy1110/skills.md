---
name: ml-pipeline-validator
description: |-
  Validates machine learning pipelines for data leakage, training-serving skew, reproducibility issues, and model governance gaps. Use this skill whenever the user shares ML training code, preprocessing scripts, or inference code and asks for a review, audit, or "is this production-ready?" — even casual asks like "does this look right?" or "why is my model performing worse in prod?". Triggers for: "check for data leakage", "review my training pipeline", "validate my ML code", "why does my model degrade in production", or any upload of train.py / preprocessing.py / inference.py files.
---

# Skill: ml-pipeline-validator

## Purpose
Audits ML pipelines across four dimensions: Data Leakage, Train-Serve Skew, Reproducibility, and Model Governance. Returns prioritized findings with concrete fixes.

## Supported Frameworks
scikit-learn, PyTorch, TensorFlow, JAX, Hugging Face, XGBoost, LightGBM, pandas/numpy pipelines.

## Input Forms
- Training script(s)
- Preprocessing + inference scripts (compare both)
- Notebook cells
- Config files (YAML/JSON with hyperparameters)

---

## Review Process

### Step 1: Orient
Identify: framework, task type (classification/regression/NLP/CV), pipeline stages present, data flow.

### Step 2: Run All Four Checks

#### 1. DATA LEAKAGE (highest priority)
Flag when:
- **Scaler/encoder fit on full dataset**: `scaler.fit_transform(X)` before train/test split → CRITICAL
- **Test labels used in feature engineering**: target-encoding, mean-encoding using test rows
- **Temporal leakage**: future timestamps in features for historical prediction
- **ID/timestamp columns**: leaking row identity into features
- **Statistical properties of test set** used in normalization

```python
# BAD
scaler.fit_transform(X)  # fits on train+test combined

# GOOD
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
```

#### 2. TRAIN-SERVE SKEW
Compare training vs inference code for mismatches in:
- **Normalization parameters**: hardcoded values in serving vs learned from training
- **Feature order**: column order differs between train DataFrame and inference payload
- **Missing value handling**: `fillna(0)` in training but `dropna()` in serving
- **Encoding**: one-hot in training, label encoding in serving
- **Data types**: float32 in training, float64 in inference

Flag: any preprocessing step present in one file but absent or different in the other.

#### 3. REPRODUCIBILITY
Check for:
- **Missing random seeds**: `np.random.seed()`, `torch.manual_seed()`, `tf.random.set_seed()`, `random.seed()`
- **Non-deterministic ops**: `torch.use_deterministic_algorithms(True)` missing
- **Undocumented data splits**: no record of how train/val/test was divided
- **Hyperparameters hardcoded in script**: should be in versioned config file
- **No model checkpointing**: training can't be resumed after interruption
- **Missing dependency versions**: no requirements.txt / pyproject.toml / environment.yml

#### 4. MODEL GOVERNANCE
Check for:
- **Wrong metrics for task**:
  - Imbalanced classification → accuracy alone is misleading; need F1/AUC-ROC
  - Regression → need RMSE *and* MAE (one hides outlier impact)
  - NLP generation → perplexity or BLEU, not just loss
- **No baseline comparison**: model vs. trivial predictor (majority class, mean, last value)
- **Missing documentation**: dataset source, feature definitions, known failure modes
- **No validation set**: training directly against test set
- **Class imbalance unaddressed**: imbalanced dataset with no SMOTE / class weights / oversampling

---

### Step 3: Assign Severity

| Level | Meaning |
|-------|---------|
| CRITICAL | Data leakage — results are invalid and overstated |
| HIGH | Skew or reproducibility issue causing silent prod degradation |
| MEDIUM | Governance gap, wrong metrics, missing documentation |
| LOW | Minor style, logging, or config organization |

### Step 4: Output the Review

---

## 🧪 ML Pipeline Review: `[filename(s)]`
**Framework**: X | **Task**: X | **Health Score**: X/10

### Summary
N critical · N high · N medium · N low

### Findings

**[SEVERITY] [CATEGORY] — `file.py` line N**
> _Issue_: One-sentence description.
> _Impact_: Quantified effect (e.g., "model performance overstated by ~10-20%").
> _Fix_:
```python
# corrected code
```

_(repeat per finding)_

### Metrics Checklist
| Metric | Present | Appropriate for Task |
|--------|---------|----------------------|
| Accuracy | ✓/✗ | ✓/✗ |
| F1 / AUC-ROC | ✓/✗ | ✓/✗ |
| ... | | |

### Governance Checklist
- [ ] Random seeds set
- [ ] Preprocessing versioned/exported
- [ ] Hyperparameters in config file
- [ ] Baseline model compared
- [ ] Dataset schema documented
- [ ] Known limitations noted

### Top 3 Actions
1. [Most urgent] — ~X min
2. [Second] — ~X min
3. [Third] — ~X min

---

## Scoring
Start at 10. Deduct: CRITICAL −2, HIGH −1, MEDIUM −0.5, LOW −0.1. Min: 1.
