---
name: ai-architect-workflow
description: >
  End-to-end AI Architect workflow: strategy, system design, MLOps infrastructure, data architecture,
  security/compliance, scaling, org design, and pilot planning. Use this skill whenever the user asks
  about AI strategy, building an AI platform, designing ML infrastructure, MLOps pipelines, scaling AI
  to production, AI governance, responsible AI frameworks, or building an AI Center of Excellence.
  Also triggers for: "how do I architect an AI system", "design my ML platform", "build MLOps pipeline",
  "how to scale ML to 1M users", "AI roadmap", "AI governance framework", "responsible AI", "feature store
  design", "model serving architecture", "how to set up AI organization", "AI use case prioritization",
  "canary deployment for ML", "multi-region AI serving", or any request covering strategy-to-production
  for AI/ML systems at enterprise scale.
---

# AI Architect End-to-End Workflow

Full guide from business vision to production AI at scale. Follow phases in order;
skip only if user explicitly has those artifacts.

---

## Phase 1: Strategic Planning

### 1.1 AI Strategy Document

Before any architecture, establish:

1. **Current state** — % manual processes, existing AI usage, data maturity
2. **Target state** — automation %, AI-driven decisions %, revenue/cost targets
3. **Investment & timeline** — 3-5 year roadmap with annual milestones
4. **Strategic pillars** — typically: Customer Intelligence, Operational Excellence, Product Innovation, Risk/Compliance
5. **Org structure** — CAIO → CDO / ML Engineering Lead / AI Governance Lead

**5-Year Maturity Arc:**

| Year | Focus | Key Milestone |
|------|-------|---------------|
| 1 | Foundation | 5 pilots in production, cloud infra live |
| 2 | Scale | 15 models, MLOps practices, internal ML platform |
| 3–5 | Transform | 50+ models, GenAI features, AI-native culture |

### 1.2 Use Case Prioritization

Score each use case on 4 axes (1–10):

```
Priority Score = (Business Value × 0.35) +
                 (Data Availability × 0.25) +
                 (Competitive Advantage × 0.25) +
                 ((10 - Implementation Difficulty) × 0.15)
```

**Quadrant placement:**
- Score > 7.5 → **Quick Win** (Phase 1, months 1–3)
- Score 6.5–7.5 → **Strategic** (Phase 2, months 4–8)
- Score < 6.5 → **Complex / Data Challenge** (Phase 3, months 9+)

**Typical ranking order:**
1. Churn Prediction (data-rich, fast ROI)
2. Fraud Detection (high business value)
3. Sentiment Analysis (low difficulty)
4. Demand Forecasting / Personalization
5. NLP Chatbot / Computer Vision (high complexity)

---

## Phase 2: Architecture Design

### 2.1 Seven-Layer Architecture

```
DATA SOURCES → INGESTION → STORAGE → DEVELOPMENT → DEPLOYMENT → MONITORING → GOVERNANCE
```

**Layer 1 — Data Sources:**
CRM (Salesforce), Data Warehouse (Snowflake), Event Stream (Kafka), Web Logs (S3)

**Layer 2 — Ingestion:**
- Batch: Apache Airflow (hourly jobs, retry=3, SLA 99.5%)
- Streaming: Kafka + Spark Structured Streaming (<1 sec latency)

**Layer 3 — Storage:**
- Data Warehouse: Snowflake (schemas: raw → staging → analytics → ml)
- Feature Store: Feast (500+ features, online Redis + batch Snowflake)
- Data Lake: Delta Lake on S3 (50TB, 2yr retention, Parquet)

**Layer 4 — ML Development:**
- Experiment tracking: MLflow (params, metrics, artifacts, code version)
- Data versioning: DVC
- Compute: GPU cluster (8× A100) + Ray for distributed training
- Model types: XGBoost/LightGBM (tabular), BERT/RoBERTa (NLP), YOLOv8 (CV), NCF (recommendation)

**Layer 5 — Deployment (three modes):**

| Mode | Platform | Latency SLA | Scale |
|------|----------|-------------|-------|
| Batch | Spark on K8s | 1 hour | 1M preds/day |
| Online | KServe + FastAPI | <100ms p95 | 10K req/sec |
| Streaming | Spark Streaming + Kafka | <500ms | 100K events/sec |

**Layer 6 — Monitoring:**
- Infrastructure: Prometheus + Grafana
- ML-specific: Evidently (data drift) + Arize (model drift)
- Alert triggers: latency >200ms, AUC drop >5%, missing data >5%

**Layer 7 — Governance:**
- Model approval workflow: development → staging → production (board sign-off)
- Bias audits: quarterly (Fairness-360)
- Documentation: model cards, data lineage, decision trees

### 2.2 Technology Stack

```yaml
data_ingestion: [Airflow, Kafka, Fivetran]
data_storage:   [Snowflake, S3 + Delta Lake, Feast]
ml_dev:         [MLflow, DVC, Ray, Jupyter]
model_serving:  [FastAPI, KServe, Seldon, gRPC]
monitoring:     [Prometheus, Grafana, Evidently, Arize]
governance:     [Collibra, Great Expectations, OpenMetadata]
infra:          [Kubernetes, Docker, Terraform, GitLab CI]
```

---

## Phase 3: MLOps Pipeline Design

### 3.1 Continuous Training Pipeline

**Triggers:** data drift detected | monthly schedule | manual

**Steps:**
1. `data_preparation` — fetch from feature store, validate, split, handle imbalance (15 min)
2. `feature_selection` — importance ranking, multicollinearity check (10 min)
3. `model_training` — Optuna hyperparameter tuning, cross-validation, early stopping (2 hr, GPU)
4. `model_evaluation` — metrics, per-segment analysis, fairness check (30 min)
5. `compare_with_baseline` — statistical significance test; approve if improvement >1% (5 min)
6. `register_model` — MLflow registry, model card, version code+data (2 min)

### 3.2 Progressive Deployment (Canary)

```
Staging (100% staging traffic)
  ↓ smoke + integration + fairness tests pass
Canary 1% (1–2 hrs)
  ↓ error rate < baseline, latency p95 < baseline + 10%
Canary 10% (4–8 hrs)
  ↓ same checks + business metrics
Canary 50% (8–24 hrs)
  ↓ business metrics stable
Production 100%
```

**Auto-rollback triggers:** error rate >1% | latency increase >20% | any fairness violation

### 3.3 Feature Store Design

```python
# Online vs batch serving decision:
if latency_required < 50ms:
    source = "Redis cache"          # <10ms, real-time freshness
else:
    source = "Snowflake"            # <1hr, batch freshness

# Feature repositories:
# customer_features  (300 features: tenure, spend, engagement, LTV)
# transaction_features (150 features: amount, MCC, fraud_risk)
# behavioral_features  (50 features: login_frequency, session_duration)
```

**Point-in-time correctness is mandatory** — prevents data leakage in training.

---

## Phase 4: Data Architecture

### 4.1 Data Lake Structure

```
s3://datalake/
├── raw/          Parquet, 2yr retention, engineers only
├── staging/      Cleaned + deduped, 90d retention
├── analytics/    Dimensional model, all employees
└── ml/           Training datasets, features, ML team only
```

### 4.2 Data Warehouse (Snowflake)

Schemas: `raw_data → staging → analytics → ml`

Dimensional model: `dim_customer`, `dim_date`, `fact_transactions`, `fact_interactions`

### 4.3 Data Governance

| Domain | Tool | What It Covers |
|--------|------|----------------|
| Metadata | Collibra / OpenMetadata | Lineage, ownership, usage |
| Quality | Great Expectations | Missing, range, schema, freshness |
| Security | AWS KMS + RBAC | Encryption, access control |
| PII | Masking + anonymization | Non-prod data protection |

**Data classification:** Public → Internal → Confidential → Restricted (PII/financial/health)

---

## Phase 5: Security & Compliance

### 5.1 Security Layers

**Data security:**
- At rest: AES-256 | In transit: TLS 1.3 | Keys: AWS KMS / HashiCorp Vault
- RBAC roles: data_viewer → data_editor → model_developer → model_deployer → admin
- MFA required for all production access

**API security:**
- Auth: JWT (1hr expiry) or API key (rotated monthly)
- Rate limiting: 1K req/hr per user, 10K req/hr per IP
- DDoS: Cloudflare + AWS Shield

**Model security:**
- Adversarial robustness testing before each deployment
- Model signing to verify authenticity
- Input validation + sanitization (prompt injection defense for LLMs)

### 5.2 Compliance Frameworks

| Framework | Scope | Key Requirements |
|-----------|-------|-----------------|
| GDPR | EU residents | Consent, right-to-delete, DPIA, data minimization |
| CCPA | California | Opt-out, right-to-know, non-discrimination |
| HIPAA | Healthcare US | PHI encryption, audit logs, BAA |
| PCI-DSS | Payment data | Tokenization, network segmentation, no raw card storage |

### 5.3 Responsible AI Framework

**Transparency:** SHAP/LIME explainability for all high-stakes decisions; mandatory model cards

**Fairness checks (quarterly):**
- Demographic parity (equal prediction rates across groups)
- Equalized odds (equal TPR/FPR across groups)
- Calibration (confidence accuracy)

**Privacy:** Differential privacy for analytics; federated learning for sensitive domains; data minimization

### 5.4 Pre-Deployment Checklist

```
□ Bias & Fairness Audit (Ethics team → fairness_report.pdf)
□ Security Scan (Security team → vulnerability_scan.pdf)
□ DPIA completed (Legal/Privacy → dpia_signed.pdf)
□ Model Governance Board approval
□ Explainability report (SHAP values + model card)
□ Documentation complete (model_card.md + data_docs)
```

---

## Phase 6: Scaling to 1M+ Users

### 6.1 Capacity Planning

```python
users = 10_000_000
dau = users * 0.30              # 3M daily active
peak_concurrent = dau * 0.01    # 30K concurrent
predictions_per_day = 1_000_000
requests_per_second = 10_000    # peak

# Infrastructure needed:
api_servers = ceil(requests_per_second / 500)  # 20 servers → deploy 30 (HA)
cache_size = "100 GB Redis"
cache_hit_target = 0.85  # drive 85% traffic to cache, not DB
```

### 6.2 Multi-Region Deployment

```
us-east-1   → 5M users, <50ms SLA
eu-west-1   → 3M users, <50ms SLA
ap-southeast-1 → 2M users, <50ms SLA
```

Strategy: **active-active multi-region**, latency-based routing (Route53 / Cloudflare),
replication lag <1 sec, CRDT conflict resolution.

### 6.3 Database Scaling Strategy

1. **Vertical** — upgrade instance (limited ceiling)
2. **Read replicas** — 5–10 replicas for reads (<100ms lag)
3. **Sharding** — hash by `customer_id`, 10–100 shards, consistent hashing
4. **Caching** — L1 (app in-memory) → L2 (Redis) → L3 (DB query cache), LRU eviction

### 6.4 Cost Optimization

| Resource | Cost | Optimization |
|----------|------|-------------|
| Compute | $50K/month (10M users) | Spot instances (−70%), reserved (−50%), auto-scale |
| Data transfer | $15K/month (1TB/day) | CDN, compression (gzip/brotli) |
| ML inference | $1K/month (1M preds/day) | Batch where possible, model quantization |

---

## Phase 7: Organization Design

### 7.1 AI Center of Excellence (CoE) Structure

```
Chief AI Officer
├── Chief Data Officer
│   ├── Data Engineering (15): pipelines, DW, quality
│   └── Data Science (30): models, analytics, insights
│
├── ML Engineering Lead (25)
│   ├── MLOps (4): deployment, monitoring, retraining
│   ├── ML Platform (4): tools, feature store, infra
│   └── ML Engineers (8): model development
│
└── AI Governance (8)
    ├── Ethics & Responsible AI (2)
    ├── Security & Compliance (2)
    └── Privacy & Model Governance (3)

Total: ~78 people, $15–20M/year (salary + infra)
```

### 7.2 Hiring Timeline

```
Months 1–3:   CAIO, VP ML Engineering, Director Data Eng
Months 3–6:   5 Senior Data Scientists, 4 MLOps, 6 Data Engineers
Months 6–12:  15 Data Scientists, 8 ML Engineers, Governance team
Year 2+:      2–3× team size based on model portfolio
```

### 7.3 Team Development

- Internal certification paths: Data Science (12 wk), ML Engineering (16 wk), Data Eng (8 wk)
- External: Fast.ai, DeepLearning.AI specializations, cloud certs (AWS/GCP)
- Budget: $5K/person/year
- Vendor partnerships: Databricks (platform), Scale AI (labeling), HuggingFace (NLP)

---

## Phase 8: Pilot Projects (Quick Wins)

### 8.1 Three Starter Pilots

**Pilot 1: Churn Prediction (8 weeks, $100K)**
- Model: XGBoost, predict 30-day churn
- ROI: $10M/year if churn drops 1%
- Team: 2 data scientists + 1 ML engineer

**Pilot 2: Personalized Recommendations (10 weeks, $400K)**
- Model: Collaborative filtering + content hybrid
- ROI: +15–20% revenue on targeted customers
- A/B test required

**Pilot 3: Fraud Detection (12 weeks, $150K)**
- Model: Isolation Forest + Neural Network ensemble
- ROI: Block 80% fraud → prevent $16M/year loss
- Real-time scoring on every transaction

### 8.2 Pilot Timeline

```
Weeks 1–2:   Project setup, data ingestion
Weeks 3–5:   EDA, feature engineering
Weeks 6–8:   Model training, evaluation
Weeks 9–10:  Deployment, CRM/API integration
Weeks 11–12: Monitoring, threshold tuning
Week 13+:    Ongoing management + iteration
```

---

## Infrastructure as Code Reference

### Kubernetes Deployment Pattern

```yaml
# Key K8s resources for model serving:
Deployment:
  replicas: 3
  strategy: RollingUpdate (maxSurge=1, maxUnavailable=0)
  resources: {cpu: "4", memory: "16Gi", gpu: "1"}
  probes:
    liveness: GET /health (period 10s)
    readiness: GET /ready (period 5s)

HorizontalPodAutoscaler:
  min: 3, max: 20
  target_cpu: 70%, target_memory: 80%

PodDisruptionBudget:
  minAvailable: 2  # always 2 pods up during updates

Service: LoadBalancer → port 80 → containerPort 8000
Ingress: api.ml.company.com/model-name → service
```

---

## Deliverables Checklist

An AI Architect produces:

```
□ Strategic AI Roadmap (5-year, phased)
□ Technical Architecture Blueprints (data, ML, infra)
□ MLOps Framework (CI/CD, monitoring, governance)
□ Security & Compliance Framework (GDPR/CCPA/HIPAA + responsible AI)
□ Organization Structure & Hiring Plan
□ Cost Projections (capex, opex, ROI per use case)
□ Risk Assessment & Mitigation Matrix
□ Vendor & Platform Recommendations
□ Use Case Prioritization Matrix
□ Pilot Project Plans (3 quick wins)
```

**Key skills required:** Strategic thinking · System design · Deep ML knowledge ·
Infrastructure/DevOps · Governance/compliance · Organizational leadership · Communication

**Total timeline:** 3–4 months from kickoff to strategy complete + first pilots deployed
