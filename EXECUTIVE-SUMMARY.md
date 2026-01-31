# RAI Framework — Executive Summary

**One page. Everything leadership needs to know.**

---

## What Is This?

A practical governance framework for AI systems. It tells your teams exactly what to do — not just what to care about.

## Why Do We Need It?

| Without governance | With this framework |
|---|---|
| Teams build AI with no consistency | Standard process, scaled by risk |
| Incidents happen, nobody knows the plan | Clear ownership, incident response ready |
| Regulators ask questions, you scramble | Compliance mapping to NIST, EU AI Act, ISO 42001 built in |
| Bias and safety issues found in production | Caught during testing, before launch |
| Nobody knows what AI systems we have | Centralized AI registry |

## How Does It Work?

**Three core ideas:**

### 1. Risk Tiers — Not Everything Needs the Same Scrutiny

| Tier | What Goes Here | Overhead |
|------|---------------|----------|
| 🔴 Critical | Medical diagnosis, credit scoring, hiring | Full governance, external review |
| 🟡 High | Fraud detection, customer chatbots | Standard governance, internal review |
| 🔵 Standard | Recommendations, forecasting | Lightweight governance |
| ⚪ Low | Internal tools, test automation | Registration only |

Most of your AI systems are 🔵 Standard or ⚪ Low. The heavy process only applies where it matters.

### 2. Lifecycle Gates — Check Before You Ship

Every AI system goes through: **Scope → Build → Test → Deploy → Retire**

Between each stage, there's a gate — a checklist and an approval. Higher risk = more rigorous gates. Lower risk = lightweight self-certification.

### 3. Templates — Fill In, Don't Write From Scratch

10 ready-to-use templates: AI registry, use case statement, impact assessment, model card, data documentation, test report, monitoring plan, incident response, retirement plan, vendor AI assessment.

Teams fill in the blanks. No guesswork.

## What Does It Cost?

**Time, not money.** No software to buy, no consultants needed.

| System Risk | Time to Adopt (first system) | Ongoing Overhead |
|-------------|------------------------------|------------------|
| ⚪ Low | ~30 minutes | Minimal |
| 🔵 Standard | ~2 hours | Annual review |
| 🟡 High | ~1 day | Quarterly review |
| 🔴 Critical | ~1 week | Monthly review |

## What Does It Give Us?

- **Regulatory readiness** — Mapped to NIST AI RMF, EU AI Act, ISO 42001
- **Reduced risk** — Catches bias, safety, and privacy issues before production
- **Accountability** — Every AI system has a named owner
- **Audit trail** — Documentation at every lifecycle stage
- **Incident preparedness** — Response plans in place before something goes wrong
- **Consistency** — Same process for classical ML, GenAI, and AI agents

## How Do We Start?

1. **Week 1:** Read the [30-minute quickstart](QUICKSTART.md). Create the AI registry. Classify existing systems.
2. **Month 1:** Run your highest-risk system through the full framework.
3. **Quarter 1:** All 🟡 High and 🔴 Critical systems documented. Review cadence established.
4. **Ongoing:** New AI systems go through the lifecycle from day one.

## Who Owns This?

| Role | Responsibility |
|------|---------------|
| **AI Owner** (per system) | Product manager or tech lead — owns the system end-to-end |
| **AI Reviewer** (per system) | Senior engineer — validates testing and risk assessments |
| **RAI Sponsor** (org-level) | VP/Director — resolves escalations, sets risk appetite |

No new hires needed. Works with existing roles.

---

*Full framework: [FRAMEWORK.md](FRAMEWORK.md) · Quickstart: [QUICKSTART.md](QUICKSTART.md)*
