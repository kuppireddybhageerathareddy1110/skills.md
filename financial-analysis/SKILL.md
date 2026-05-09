---
name: financial-analysis
description: |-
  Performs comprehensive financial analysis including ratio analysis, DCF valuation, cash flow quality assessment, risk scoring, and investment thesis generation. Use this skill whenever the user shares financial statements, earnings data, or company financials and asks to "analyze", "value", "assess", "is this a good investment?", "review the financials", or "what do the numbers say?". Triggers for: P&L analysis, balance sheet review, cash flow analysis, ratio calculation, DCF model, comparable company analysis, credit risk, or any request involving financial data from a company or portfolio.
---

# Skill: financial-analysis

## Purpose
Structured financial analysis across five dimensions: Profitability, Liquidity, Leverage, Cash Flow Quality, and Valuation. Returns a scored assessment with investment thesis and key risks.

## Input Forms
- Income statement + balance sheet + cash flow statement (any format)
- 10-K / annual report excerpt
- Earnings call numbers pasted as text
- Single metric set described in text (e.g., "revenue $500M, EBITDA $80M, debt $200M")

---

## Analysis Framework

### Step 1: Extract Key Numbers
Always identify:
- Revenue (and YoY growth)
- Gross profit + gross margin
- EBITDA / operating income + margin
- Net income + net margin
- Total assets, total debt, total equity
- Current assets, current liabilities
- Operating cash flow, capex, free cash flow
- Shares outstanding + stock price (if valuation requested)

### Step 2: Calculate All Ratios

#### Profitability
| Ratio | Formula | Healthy Range |
|-------|---------|---------------|
| Gross Margin | Gross Profit / Revenue | Industry-dependent |
| Operating Margin | EBIT / Revenue | >10% solid |
| Net Margin | Net Income / Revenue | >5% solid |
| ROE | Net Income / Equity | >15% good |
| ROA | Net Income / Assets | >5% good |
| ROIC | NOPAT / Invested Capital | > WACC = value-creating |

#### Liquidity
| Ratio | Formula | Healthy Range |
|-------|---------|---------------|
| Current Ratio | Current Assets / Current Liabilities | 1.5–3.0 |
| Quick Ratio | (CA − Inventory) / CL | > 1.0 |
| Cash Ratio | Cash / CL | > 0.2 |

#### Leverage
| Ratio | Formula | Watch Level |
|-------|---------|------------|
| Debt/Equity | Total Debt / Equity | < 2.0 |
| Debt/EBITDA | Net Debt / EBITDA | < 3.0× |
| Interest Coverage | EBIT / Interest Expense | > 3.0× |

#### Cash Flow Quality
- **FCF = Operating CF − CapEx**
- **FCF Margin** = FCF / Revenue
- **FCF vs Net Income ratio**: > 1.0 = high earnings quality; < 0.7 = earnings may be accrual-inflated
- **Cash Conversion Cycle** = DSO + DIO − DPO (lower = better)
- **CapEx intensity** = CapEx / Revenue (high = capital-heavy business)

#### Valuation (if price or market cap available)
| Multiple | Formula | Use |
|----------|---------|-----|
| P/E | Price / EPS | Earnings-based |
| EV/EBITDA | (Market Cap + Debt − Cash) / EBITDA | Most universal |
| EV/Revenue | EV / Revenue | Pre-profit companies |
| P/FCF | Price / FCF per share | Cash flow quality |
| P/B | Market Cap / Book Value | Asset-heavy cos |

### Step 3: DCF Valuation (if requested or if enough data)
```
Inputs needed: FCF, growth rate assumption, WACC, terminal growth rate

Year 1–5: FCF × (1 + growth_rate)^year
Terminal Value: FCF_year5 × (1 + terminal_growth) / (WACC − terminal_growth)
Enterprise Value = PV of FCFs + PV of Terminal Value
Equity Value = EV − Net Debt
Per Share = Equity Value / Shares Outstanding

Always show: bear / base / bull cases
```

### Step 4: Risk Assessment

#### Altman Z-Score (public companies)
Z = 1.2×(WC/Assets) + 1.4×(RE/Assets) + 3.3×(EBIT/Assets) + 0.6×(MktCap/Liabilities) + 1.0×(Revenue/Assets)
- Z > 2.99: Safe zone
- 1.81–2.99: Gray zone
- Z < 1.81: Distress zone

#### Credit Risk Flags
- Debt/EBITDA > 5×: high leverage
- Interest Coverage < 2×: stress risk
- Negative FCF for 2+ years: cash burn
- Current ratio < 1.0: near-term liquidity risk
- Revenue declining YoY: top-line pressure

### Step 5: Investment Thesis
Summarize: Bull case, Bear case, Key catalysts, Key risks, Verdict.

---

## Output Format

### 💰 Financial Analysis: `{Company Name}`
**Period**: FY{year} | **Health Score**: X/10 | **Verdict**: BUY / HOLD / AVOID / INSUFFICIENT DATA

---

#### Snapshot
| Metric | Value | vs Industry | Trend |
|--------|-------|-------------|-------|
| Revenue | $Xm | Above/Below avg | ↑/↓/→ |
| Net Margin | X% | ... | ... |
| FCF | $Xm | ... | ... |
| Debt/EBITDA | X× | ... | ... |

---

#### Profitability Analysis
_(ratio table + assessment per ratio)_

#### Liquidity Analysis
_(ratio table + assessment)_

#### Leverage & Credit Risk
_(ratio table + Altman Z-Score + credit flags)_

#### Cash Flow Quality
_(FCF calculation + quality assessment + earnings quality ratio)_

#### Valuation
_(multiples table + DCF summary if data available + implied upside/downside)_

---

#### Investment Thesis
**Bull case**: ...
**Bear case**: ...
**Key catalysts**: ...
**Key risks**: ...

---

#### Red Flags 🚩
_(any critical concerns in bullet form)_

#### Top 3 Questions to Investigate
1. ...
2. ...
3. ...

---

## Rules
- NEVER make a definitive investment recommendation — present the analysis, note this is not financial advice
- Always flag when data is insufficient to calculate a ratio
- Show formulas when numbers might be contested
- Be specific: "$X declining from $Y to $Z" not just "revenue fell"
- Assume USD unless stated otherwise; flag currency if uncertain
