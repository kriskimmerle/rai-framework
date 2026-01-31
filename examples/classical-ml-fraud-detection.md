# Worked Example: Fraud Detection System (Classical ML)

> This example walks through applying the RAI Framework to a classical ML fraud detection system at a mid-size fintech company.

---

## Context

**Company:** FinPay — a payment processing company with 2M users
**System:** Real-time fraud detection model that flags suspicious transactions
**Team:** 15 engineers, no dedicated ethics team
**Model:** Gradient boosted decision tree (XGBoost) trained on 3 years of transaction data

---

## Step 1: Risk Classification

Walking through the decision tree:

1. *Does the system make or directly influence decisions about people's rights, freedom, safety, health, or legal status?*
   - **Yes.** Flagged transactions are automatically declined. This directly affects people's ability to use their money. False positives can lock people out of their accounts.
   - → **🔴 Critical**

**But wait** — let's say instead the system only *flags* for human review and doesn't auto-decline. Then:

1. *Does it directly affect rights/safety?* — Not directly, human reviews first → NO
2. *Could failure cause >$100K loss, regulatory action, or reputational damage?* — **Yes** — fraud losses, PCI/regulatory requirements → **🟡 High**

**Escalation factors check:**
- Uses financial data (sensitive) ✅ — but already classified 🟡 High
- High volume (50K+ transactions/day) ✅ — confirm 🟡 High

**Final classification: 🟡 High** (with human-in-the-loop) or **🔴 Critical** (auto-decline)

*For this example, we'll use the 🟡 High version (human reviews flagged transactions).*

---

## Step 2: Use Case Statement (Filled)

| Field | Value |
|-------|-------|
| **System Name** | FraudGuard v2 |
| **Owner** | Sarah Chen (Senior ML Engineer) |
| **Date** | 2026-01-15 |
| **Risk Tier** | 🟡 High |

**What does this system do?**
Scores each transaction 0-100 for fraud likelihood based on transaction amount, merchant category, user history, device info, and geolocation. Transactions scoring >75 are queued for manual review by the fraud team.

**What problem does it solve?**
Manual review of all transactions is impossible at 50K+/day volume. Without the model, we'd either miss fraud or have unacceptable review delays. Previous rule-based system had 40% false positive rate.

**Who is affected?**
All 2M users. Legitimate users with flagged transactions experience delayed processing (2-4 hours average). Merchants may see delayed settlement.

**Human's role:** Human-on-the-loop. Model flags, human fraud analyst reviews and decides.

**What could go wrong?**
Model could systematically flag transactions from certain demographic groups, ZIP codes, or merchant types — causing disproportionate delays for those users. Alternatively, model could miss a new fraud pattern and allow significant losses.

**Fallback:** Revert to rule-based system (higher false positive rate but understood behavior).

---

## Step 3: Impact Assessment (Key Points)

### Harms to Individuals

| Risk | Likelihood | Severity | Mitigation |
|------|-----------|----------|------------|
| Disproportionate flagging by geography/demographics | Medium | High | Fairness testing across ZIP code clusters, regular bias audits |
| Legitimate transactions delayed (false positives) | High | Medium | SLA: flagged transactions reviewed within 4 hours. Target <5% false positive rate |
| Fraud not caught (false negatives) | Medium | High | Secondary rule-based checks for high-value transactions. Daily loss monitoring |

### Data Risks

- Uses financial transaction data (sensitive) ✅
- No health/biometric data
- PII present (name, address, device IDs)
- Consent: covered by Terms of Service
- Retention: transaction data retained per regulatory requirements (7 years)

**Decision: Proceed** with fairness testing and monitoring conditions.

---

## Step 4: Key Artifacts

### Model Card (Summary)

- **Architecture:** XGBoost, 150 estimators, max depth 8
- **Training data:** 18M transactions (2023-2025), 0.3% fraud rate (heavily imbalanced)
- **Features:** 47 features including transaction amount, merchant category, hour of day, device fingerprint, velocity features, geolocation distance
- **Primary metric:** AUPRC = 0.82 (precision-recall, not ROC, because of class imbalance)
- **Threshold:** Score >75 → flag for review (tuned for 95% recall on known fraud, <5% false positive rate)

### Fairness Testing Results

| Subgroup (by ZIP cluster) | False Positive Rate | Within Threshold? |
|--------------------------|--------------------|--------------------|
| High-income urban | 3.2% | ✅ |
| Suburban | 4.1% | ✅ |
| Rural | 6.8% | ⚠️ Elevated |
| Low-income urban | 7.1% | ⚠️ Elevated |

**Action:** Investigated rural/low-income elevated rates. Root cause: fewer transaction history data points for new users in these areas. Mitigation: added feature for "account maturity" and retrained. Post-fix rural FPR: 4.9%.

---

## Step 5: Monitoring (Key Elements)

| Metric | Baseline | Alert Threshold | Frequency |
|--------|----------|-----------------|-----------|
| Overall false positive rate | 4.2% | >6% | Daily |
| FPR by ZIP cluster | See above | >2x baseline for any cluster | Weekly |
| Fraud catch rate (recall) | 95.1% | <90% | Daily |
| Average review time | 2.1 hours | >4 hours | Daily |
| Input feature drift (PSI) | <0.1 | >0.25 | Weekly |

**Review cadence:** Quarterly (🟡 High tier)

---

## Lessons

1. **Class imbalance matters.** Using AUPRC instead of accuracy/ROC avoided a model that looks great on paper but misses fraud.
2. **Fairness testing found a real problem.** Without testing across subgroups, the rural/low-income disparity would have gone unnoticed.
3. **Human-in-the-loop changed the risk tier.** Auto-decline = 🔴 Critical. Flag for review = 🟡 High. The human review step is a meaningful control.
4. **Monitoring drift is essential.** Fraud patterns shift constantly. A model trained on 2023-2025 data will degrade — the weekly drift check catches this early.
