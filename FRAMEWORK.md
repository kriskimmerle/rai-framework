# Responsible AI Framework (RAI)

**A practical, actionable framework for building and deploying AI responsibly.**

> Most RAI frameworks tell you *what* to care about. This one tells you *what to do*.

---

## Who This Is For

Any team building or deploying AI systems — whether you're training a fraud detection model, fine-tuning an LLM, building a recommendation engine, or deploying an AI agent. This framework scales from a 3-person startup to a Fortune 500 company.

**Works for:**
- Classical ML (classification, regression, clustering, forecasting)
- Generative AI (LLMs, image generation, code generation)
- AI agents and autonomous systems
- ML-powered features in larger products

---

## How This Framework Is Different

| Existing Frameworks | This Framework |
|---|---|
| Lists principles | Provides **decision trees and checklists** |
| One-size-fits-all | **Risk-tiered** — effort scales with impact |
| Focuses on development | Covers **full lifecycle including production monitoring and retirement** |
| Requires weeks to understand | **Quickstart in 30 minutes** |
| Assumes dedicated ethics team | Works with **existing roles** |
| Either classical ML or GenAI | **Covers both** with conditional guidance |

---

## Table of Contents

1. [Core Principles](#1-core-principles)
2. [Risk Classification](#2-risk-classification)
3. [Governance Structure](#3-governance-structure)
4. [Development Lifecycle](#4-development-lifecycle)
5. [Stage Gates](#5-stage-gates)
6. [GenAI-Specific Guidance](#6-genai-specific-guidance)
7. [Monitoring & Incident Response](#7-monitoring--incident-response)
8. [Compliance Mapping](#8-compliance-mapping)

---

## 1. Core Principles

Five principles. Memorizable. Each one has a concrete test.

### 1.1 Know Your Impact

Before building anything, understand what happens when it goes wrong.

**Test:** *Can you describe the worst realistic outcome of a failure or misuse of this system in one sentence? Have you told your stakeholders?*

### 1.2 Own It

Every AI system has a named human owner who is accountable for its behavior in production — not just at launch.

**Test:** *If this system causes harm at 2 AM on a Saturday, does one specific person get the call? Do they have the authority to shut it down?*

### 1.3 Show Your Work

Stakeholders affected by the system can understand what it does, how decisions are made, and what data was used — at a level appropriate to their role.

**Test:** *Can you explain to a non-technical executive why the system made a specific decision? Can the person affected by that decision get an explanation?*

### 1.4 Stay Vigilant

AI systems degrade. Data drifts. The world changes. Monitor continuously and have a plan for when things go wrong.

**Test:** *Do you have automated alerts for performance degradation? When was the last time you checked if the model still works for all subgroups?*

### 1.5 Respect People

The humans affected by your system — their privacy, dignity, autonomy, and rights — take precedence over model performance metrics.

**Test:** *If the people whose data you're using, or whose lives your system affects, could see everything you're doing — would they be okay with it?*

---

## 2. Risk Classification

Not all AI systems need the same level of oversight. A content recommendation widget doesn't need the same scrutiny as a loan approval model. Risk classification determines how much governance to apply.

### Risk Tiers

| Tier | Impact | Examples | Governance Level |
|------|--------|----------|-----------------|
| **🔴 Critical** | Affects fundamental rights, safety, freedom, or legal status | Credit scoring, medical diagnosis, criminal risk assessment, autonomous vehicles, hiring/firing decisions, child welfare screening | Full governance: all artifacts, external review, continuous monitoring |
| **🟡 High** | Significant financial, operational, or reputational impact | Fraud detection, content moderation, insurance pricing, customer churn prediction, GenAI customer-facing chatbot | Standard governance: all artifacts, internal review, monitoring |
| **🔵 Standard** | Moderate business impact, limited individual harm potential | Product recommendations, demand forecasting, internal search ranking, code completion tools | Lightweight governance: core artifacts, self-assessment, basic monitoring |
| **⚪ Low** | Minimal impact, easily reversible, internal only | Internal productivity tools, data visualization, spell-check, test data generation | Minimal governance: registration + basic documentation |

### How to Classify: Decision Tree

```
START
  │
  ├─ Does the system make or directly influence decisions about
  │  people's rights, freedom, safety, health, or legal status?
  │  ├─ YES → 🔴 CRITICAL
  │  └─ NO ↓
  │
  ├─ Could a failure cause significant financial loss (>$100K),
  │  regulatory action, or public reputational damage?
  │  ├─ YES → 🟡 HIGH
  │  └─ NO ↓
  │
  ├─ Does the system affect external users or customers directly?
  │  ├─ YES → 🔵 STANDARD (minimum)
  │  └─ NO ↓
  │
  ├─ Is the system's output easily reversible with no lasting impact?
  │  ├─ YES → ⚪ LOW
  │  └─ NO → 🔵 STANDARD
  │
  ESCALATION FACTORS (bump up one tier if any apply):
  ├─ Uses sensitive personal data (health, financial, biometric, children's data)
  ├─ Operates autonomously without human-in-the-loop
  ├─ Affects vulnerable populations
  ├─ High volume of decisions (>10K/day)
  └─ Difficult or impossible to reverse decisions
```

### GenAI Escalation

Generative AI systems get an automatic tier bump when:
- They are **public-facing** (customer chatbots, content generation)
- They can **take actions** (agents, tool-calling LLMs)
- They handle **regulated domains** (medical, legal, financial advice)
- They generate content that could be mistaken for **authoritative human output**

---

## 3. Governance Structure

Governance doesn't require a new department. It requires clear roles and accountability.

### Roles

| Role | Responsibility | Who | Required At |
|------|---------------|-----|-------------|
| **AI Owner** | Accountable for the system end-to-end. Approves deployment, owns incidents. | Product manager, tech lead, or designated senior IC | All tiers |
| **AI Reviewer** | Reviews risk assessments, validates testing, approves gate transitions | Engineering manager, senior engineer, or designated reviewer | 🔵 Standard and above |
| **RAI Sponsor** | Org-level accountability. Resolves escalations, sets risk appetite, ensures resources | VP/Director of Engineering or Product | 🟡 High and above |
| **External Reviewer** | Independent review of high-impact systems (can be internal-but-independent team) | Ethics board, external auditor, or cross-functional review panel | 🔴 Critical only |

### Scaling Guidance

**Small team (1-10):** AI Owner + AI Reviewer can be the same person for ⚪ Low and 🔵 Standard. For 🟡 High and above, they must be different people.

**Medium team (10-100):** Designate AI Reviewers per product area. RAI Sponsor is typically the engineering or product lead.

**Large org (100+):** Consider a lightweight RAI working group (not a committee — a working group that ships). Cross-functional: engineering, product, legal, security.

### The AI Registry

Maintain a registry of all AI systems. At minimum:

| Field | Description |
|-------|-------------|
| System name | Human-readable identifier |
| Owner | Named individual |
| Risk tier | 🔴/🟡/🔵/⚪ |
| Status | Development / Staging / Production / Retired |
| Purpose | One-paragraph description of what it does and why |
| Data sources | What data does it use? Any PII? |
| Affected users | Who is impacted by the system's outputs? |
| Last review date | When was the risk assessment last updated? |
| Monitoring status | What's being monitored? Any active alerts? |

Template: [templates/ai-registry.md](templates/ai-registry.md)

### Third-Party / Vendor AI

Most organizations don't only build AI — they also buy it. SaaS platforms with AI features, API-based models (OpenAI, Anthropic, Google), vendor tools with embedded ML — these all belong in your AI Registry.

**Key principle: You deploy it, you own the risk.** Classify vendor AI based on *your use case*, not the vendor's marketing.

Before adopting vendor AI:
1. Register it in the AI Registry like any other system
2. Classify it using the risk decision tree (based on your context)
3. Complete a vendor AI assessment covering: data handling, contractual protections, your-side controls, exit strategy

Template: [templates/vendor-ai-assessment.md](templates/vendor-ai-assessment.md)

---

## 4. Development Lifecycle

Five stages. Each has required artifacts that scale with risk tier.

### Stage Overview

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  SCOPE   │───▶│  BUILD   │───▶│  TEST    │───▶│  DEPLOY  │───▶│  RETIRE  │
│          │    │          │    │          │    │& MONITOR │    │          │
└──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
   Gate 1          Gate 2          Gate 3          Gate 4          Gate 5
```

### Stage 1: Scope

**Purpose:** Define what you're building, why, and what could go wrong.

| Artifact | ⚪ Low | 🔵 Standard | 🟡 High | 🔴 Critical |
|----------|--------|------------|---------|------------|
| Use Case Statement | ✅ | ✅ | ✅ | ✅ |
| Risk Classification | ✅ | ✅ | ✅ | ✅ |
| Impact Assessment | — | ✅ | ✅ | ✅ |
| Stakeholder Analysis | — | — | ✅ | ✅ |
| Legal/Regulatory Review | — | — | ✅ | ✅ |

Templates: [templates/use-case-statement.md](templates/use-case-statement.md), [templates/impact-assessment.md](templates/impact-assessment.md), [templates/stakeholder-analysis.md](templates/stakeholder-analysis.md)

### Stage 2: Build

**Purpose:** Develop the model/system with responsible practices baked in.

| Artifact | ⚪ Low | 🔵 Standard | 🟡 High | 🔴 Critical |
|----------|--------|------------|---------|------------|
| Data Documentation | — | ✅ | ✅ | ✅ |
| Model/System Card | — | ✅ | ✅ | ✅ |
| Bias & Fairness Plan | — | — | ✅ | ✅ |
| Privacy Review | — | — | ✅ | ✅ |
| Security Review | — | ✅ | ✅ | ✅ |

Templates: [templates/data-documentation.md](templates/data-documentation.md), [templates/model-card.md](templates/model-card.md)

### Stage 3: Test

**Purpose:** Validate that the system works correctly, fairly, and safely.

| Artifact | ⚪ Low | 🔵 Standard | 🟡 High | 🔴 Critical |
|----------|--------|------------|---------|------------|
| Functional Testing | ✅ | ✅ | ✅ | ✅ |
| Fairness Testing | — | — | ✅ | ✅ |
| Adversarial/Red Team Testing | — | — | ✅ | ✅ |
| Performance Benchmarks | — | ✅ | ✅ | ✅ |
| Edge Case Documentation | — | — | ✅ | ✅ |
| Human Review of Outputs | — | — | ✅ | ✅ |

Template: [templates/test-report.md](templates/test-report.md)

### Stage 4: Deploy & Monitor

**Purpose:** Ship safely and watch continuously.

| Artifact | ⚪ Low | 🔵 Standard | 🟡 High | 🔴 Critical |
|----------|--------|------------|---------|------------|
| Deployment Plan | — | ✅ | ✅ | ✅ |
| Rollback Plan | — | ✅ | ✅ | ✅ |
| Monitoring Dashboard | — | ✅ | ✅ | ✅ |
| Incident Response Plan | — | — | ✅ | ✅ |
| Periodic Review Schedule | — | ✅ (annual) | ✅ (quarterly) | ✅ (monthly) |
| User Recourse Documentation | — | — | ✅ | ✅ |

Template: [templates/monitoring-plan.md](templates/monitoring-plan.md), [templates/incident-response.md](templates/incident-response.md)

### Stage 5: Retire

**Purpose:** End-of-life the system responsibly.

| Artifact | ⚪ Low | 🔵 Standard | 🟡 High | 🔴 Critical |
|----------|--------|------------|---------|------------|
| Retirement Notice | — | ✅ | ✅ | ✅ |
| Data Disposition Plan | — | — | ✅ | ✅ |
| Migration Plan (if applicable) | — | ✅ | ✅ | ✅ |
| Post-Mortem | — | — | — | ✅ |

Template: [templates/retirement-plan.md](templates/retirement-plan.md)

---

## 5. Stage Gates

Stage gates are approval checkpoints between lifecycle stages. Their rigor scales with risk tier.

### Gate Approval Matrix

| Gate | ⚪ Low | 🔵 Standard | 🟡 High | 🔴 Critical |
|------|--------|------------|---------|------------|
| **G1: Scope → Build** | AI Owner self-certifies | AI Owner + Reviewer | AI Owner + Reviewer + RAI Sponsor | AI Owner + Reviewer + RAI Sponsor + Legal |
| **G2: Build → Test** | No gate | AI Owner reviews | AI Reviewer approval | AI Reviewer + Security review |
| **G3: Test → Deploy** | No gate | AI Owner + Reviewer | RAI Sponsor approval | External review + RAI Sponsor |
| **G4: Monitor → Continue/Retire** | Annual self-check | Annual review | Quarterly review | Monthly review |

### What to Check at Each Gate

**G1 (Scope → Build):**
- [ ] Risk tier is correctly assigned
- [ ] Use case statement is complete
- [ ] Impact assessment identifies realistic harms
- [ ] No regulatory blockers identified

**G2 (Build → Test):**
- [ ] Data documentation is complete
- [ ] Model/system card drafted
- [ ] Known limitations documented
- [ ] Security review passed (Standard+)

**G3 (Test → Deploy):**
- [ ] All required tests pass
- [ ] Fairness metrics within acceptable bounds (High+)
- [ ] Red team testing complete with no critical findings (High+)
- [ ] Monitoring plan in place
- [ ] Rollback plan tested
- [ ] Incident response plan documented (High+)

**G4 (Periodic Review):**
- [ ] Performance metrics still within bounds
- [ ] No significant data drift detected
- [ ] Fairness metrics still acceptable
- [ ] Incident log reviewed
- [ ] Risk tier still appropriate (world may have changed)

---

## 6. GenAI-Specific Guidance

Generative AI introduces risks that classical ML frameworks don't address. This section provides supplementary guidance.

### 6.1 Hallucination & Factuality

| Risk | Mitigation |
|------|-----------|
| Model generates false information | Implement retrieval-augmented generation (RAG) with source attribution |
| Model presents speculation as fact | Add confidence indicators; require citations for factual claims |
| Model generates plausible but wrong technical content | Human review for high-stakes domains; automated fact-checking where possible |

**Required for 🟡 High+:** Document hallucination rate from testing. Define acceptable threshold.

### 6.2 Prompt Injection & Adversarial Use

| Risk | Mitigation |
|------|-----------|
| Users manipulate system via crafted prompts | Input validation, system prompt hardening, output filtering |
| Indirect injection via external data | Sanitize external content before inclusion in prompts |
| Jailbreaking attempts | Rate limiting, pattern detection, abuse monitoring |

**Required for 🟡 High+:** Red team testing specifically for prompt injection. Document findings and mitigations.

### 6.3 Content Safety

| Risk | Mitigation |
|------|-----------|
| Generates harmful, illegal, or offensive content | Output filters, content classifiers, safety system prompts |
| Generates content that violates copyright or IP | Training data documentation, output monitoring |
| Generates misleading content at scale | Watermarking, provenance tracking, rate limits |

**Required for 🔵 Standard+:** Content safety testing with adversarial inputs. Output filtering in production.

### 6.4 Agent & Tool-Use Systems

Autonomous AI agents (systems that can take actions, call APIs, execute code) require additional controls:

- **Scope boundaries:** Define exactly what actions the agent can and cannot take
- **Human-in-the-loop:** Require human approval for high-impact actions (financial transactions, external communications, data deletion)
- **Audit trail:** Log all actions taken, including reasoning
- **Kill switch:** Ability to immediately halt the agent
- **Sandboxing:** Limit access to only necessary systems and data

**All agent systems are minimum 🔵 Standard tier.** Agent systems with external impact are minimum 🟡 High.

### 6.5 Data & Privacy for GenAI

- Document what data was used for training/fine-tuning and its provenance
- Implement guardrails against PII leakage in outputs
- If using user data for improvement: explicit consent, opt-out mechanism, data deletion capability
- For third-party models (API-based): understand the provider's data retention and usage policies

---

## 7. Monitoring & Incident Response

### What to Monitor

| Signal | Classical ML | GenAI | Frequency |
|--------|-------------|-------|-----------|
| Performance metrics (accuracy, precision, recall, etc.) | ✅ | ✅ | Daily/weekly |
| Data drift (input distribution changes) | ✅ | — | Weekly |
| Output distribution changes | ✅ | ✅ | Daily |
| Fairness metrics across subgroups | ✅ (High+) | ✅ (High+) | Weekly/monthly |
| Latency and availability | ✅ | ✅ | Real-time |
| User feedback / complaints | ✅ | ✅ | Continuous |
| Safety violations (harmful outputs) | — | ✅ | Real-time |
| Abuse patterns | — | ✅ | Daily |
| Cost and usage | ✅ | ✅ | Daily |

### Incident Severity Levels

| Level | Definition | Response Time | Example |
|-------|-----------|---------------|---------|
| **P0 — Critical** | Active harm to users, safety incident, data breach | Immediate (minutes) | Model leaking PII, biased decisions causing real harm |
| **P1 — High** | Significant degradation, regulatory risk | Within hours | Major accuracy drop, fairness metric violation |
| **P2 — Medium** | Noticeable issues, no immediate harm | Within 1 business day | Moderate drift, increased error rate |
| **P3 — Low** | Minor issues, cosmetic | Within 1 week | Slight performance dip, non-critical bug |

### Incident Response Process

```
DETECT → ASSESS → CONTAIN → INVESTIGATE → REMEDIATE → REVIEW
  │         │         │           │             │          │
  │         │         │           │             │          └─ Update docs,
  │         │         │           │             │            adjust monitoring
  │         │         │           │             └─ Fix root cause,
  │         │         │           │               validate fix
  │         │         │           └─ Determine root cause,
  │         │         │             scope of impact
  │         │         └─ Disable/rollback if needed,
  │         │           limit blast radius
  │         └─ Assign severity level,
  │           notify stakeholders
  └─ Automated alert or
    human report
```

Template: [templates/incident-response.md](templates/incident-response.md)

---

## 8. Compliance Mapping

This framework aligns with major regulations and standards. Use this mapping to demonstrate compliance.

| This Framework | NIST AI RMF | EU AI Act | ISO 42001 | Microsoft RAI |
|---------------|-------------|-----------|-----------|---------------|
| Know Your Impact | MAP | Risk Classification (Art. 6) | Risk Assessment | Impact Assessment |
| Own It | GOVERN | Provider Obligations (Art. 16) | Leadership & Governance | Accountability |
| Show Your Work | MAP, MEASURE | Transparency (Art. 13) | Documentation | Transparency |
| Stay Vigilant | MEASURE, MANAGE | Post-Market Monitoring (Art. 72) | Monitoring & Review | Reliability & Safety |
| Respect People | GOVERN, MANAGE | Fundamental Rights (Art. 27) | Interested Parties | Fairness, Privacy |
| Risk Tiers | GOVERN (Risk Appetite) | Risk Categories (Art. 6, Annex III) | Context of Organization | — |
| Stage Gates | MANAGE | Conformity Assessment (Art. 43) | Planning & Operation | — |
| AI Registry | MAP | EU Database (Art. 71) | Statement of Applicability | — |
| Incident Response | MANAGE | Serious Incident Reporting (Art. 73) | Incident Management | — |

---

## Getting Started

1. **Read** [QUICKSTART.md](QUICKSTART.md) — get operational in 30 minutes
2. **Classify** your existing AI systems using the decision tree
3. **Register** them in the AI Registry template
4. **Pick one** High or Critical system and run through the full lifecycle
5. **Iterate** — this framework is a living document, adapt it to your context

**Additional resources:**
- [Executive Summary](EXECUTIVE-SUMMARY.md) — one-page overview for leadership
- [Maturity Model](MATURITY-MODEL.md) — assess where your organization is and plan next steps
- [Glossary](GLOSSARY.md) — shared vocabulary for the framework

---

## References & Inspiration

- [NIST AI Risk Management Framework (AI RMF 1.0)](https://doi.org/10.6028/NIST.AI.100-1)
- [NIST AI 600-1: Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
- [EU AI Act](https://artificialintelligenceact.eu/)
- [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html)
- [Singapore Model AI Governance Framework](https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2024/public-consult-model-ai-governance-framework-genai)
- [Microsoft Responsible AI Principles](https://www.microsoft.com/en-us/ai/principles-and-approach)
- [OECD AI Principles](https://oecd.ai/en/ai-principles)
- [WEF Advancing Responsible AI Innovation Playbook (2025)](https://www.weforum.org/publications/advancing-responsible-ai-innovation-a-playbook/)

---

## License

MIT — Use this framework freely. Attribution appreciated but not required.
