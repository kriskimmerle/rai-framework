# Glossary

**Shared vocabulary for the RAI Framework. When we say these words, this is what we mean.**

---

### A

**Adversarial testing** — Deliberately trying to make an AI system fail, produce harmful outputs, or behave unexpectedly. Includes red teaming, prompt injection testing, and edge case probing. See also: *Red teaming*.

**AI agent** — An AI system that can take actions autonomously — calling APIs, executing code, modifying data, or interacting with external systems. Agents require additional controls (scope boundaries, kill switches, audit trails) compared to passive AI systems. See [Section 6.4](FRAMEWORK.md#64-agent--tool-use-systems).

**AI Owner** — The named individual accountable for an AI system end-to-end. Responsible for risk classification, lifecycle gates, deployment decisions, and incident response. Not a team — a specific person. See [Governance Structure](FRAMEWORK.md#3-governance-structure).

**AI Reviewer** — A person who independently validates testing, risk assessments, and gate transitions for an AI system. Must be different from the AI Owner for 🟡 High and 🔴 Critical systems.

**AI Registry** — A centralized inventory of all AI systems in an organization, including their owners, risk tiers, status, and review dates. Template: [templates/ai-registry.md](templates/ai-registry.md).

**AUPRC** — Area Under the Precision-Recall Curve. A performance metric preferred over AUROC for imbalanced datasets (where one class is much rarer than others). Common in fraud detection, anomaly detection.

### B

**Bias** — Systematic and unfair discrimination in an AI system's outputs. Can originate from training data (historical bias, selection bias), model design, or deployment context. Not all statistical skew is harmful bias — the question is whether the disparity causes unjust outcomes.

### C

**Calibration** — A model is well-calibrated when its confidence scores match reality. If the model says "80% confidence," the prediction should be correct about 80% of the time.

**Content safety** — Controls to prevent AI systems from generating harmful, illegal, offensive, or inappropriate content. Includes output filters, content classifiers, and safety system prompts.

**Compliance mapping** — A table showing how elements of this framework correspond to requirements in external regulations and standards (NIST AI RMF, EU AI Act, ISO 42001, etc.). See [Section 8](FRAMEWORK.md#8-compliance-mapping).

### D

**Data drift** — When the statistical properties of input data in production change compared to the data the model was trained on. A leading indicator that model performance may degrade. Measured with metrics like Population Stability Index (PSI).

**Demographic parity** — A fairness criterion where the positive prediction rate is equal across protected groups. One of several fairness definitions — no single metric works for all contexts.

### E

**Equal opportunity** — A fairness criterion where the true positive rate (recall) is equal across protected groups. Focuses on ensuring the model is equally accurate for all groups among people who should receive a positive outcome.

**Escalation factor** — A condition that bumps a system's risk tier up by one level. Includes: sensitive personal data, no human-in-the-loop, vulnerable populations, high decision volume (>10K/day), irreversible decisions.

### F

**Fairness testing** — Evaluating an AI system's performance across demographic subgroups, geographic regions, or other population segments to detect disproportionate impact. Required for 🟡 High and 🔴 Critical systems.

**False positive** — The system incorrectly flags/predicts a positive outcome (e.g., marking a legitimate transaction as fraud). The cost of false positives varies by context — in some systems it's minor inconvenience, in others it's life-altering.

**Feature drift** — See *Data drift*.

### G

**Gate / Stage gate** — An approval checkpoint between lifecycle stages (Scope → Build → Test → Deploy → Retire). The rigor of gates scales with risk tier. See [Section 5](FRAMEWORK.md#5-stage-gates).

### H

**Hallucination** — When a generative AI model produces content that sounds plausible but is factually incorrect, fabricated, or not supported by its source data. A core risk for GenAI systems. See [Section 6.1](FRAMEWORK.md#61-hallucination--factuality).

**Human-in-the-loop (HITL)** — A human reviews and approves every AI decision before it takes effect. The strongest level of human oversight.

**Human-on-the-loop (HOTL)** — A human monitors AI decisions and can intervene, but the system operates autonomously by default. The human can override or halt the system.

**Human-out-of-the-loop** — The AI system operates fully autonomously with no human review. Appropriate only for low-risk, easily reversible decisions.

### I

**Impact assessment** — A structured analysis of what could go wrong with an AI system, who could be harmed, and how. Required for 🔵 Standard and above. Template: [templates/impact-assessment.md](templates/impact-assessment.md).

### K

**Kill switch** — The ability to immediately halt an AI system's operation. Required for all AI agent systems. Should be accessible to the AI Owner and on-call engineers.

### M

**Model card** — A document describing an AI model/system: what it does, how it was trained, its performance characteristics, limitations, and intended use. Based on [Mitchell et al. (2019)](https://arxiv.org/abs/1810.03993). Template: [templates/model-card.md](templates/model-card.md).

**MTTR** — Mean Time to Resolution. Average time from incident detection to resolution. Used in monitoring and incident response.

### P

**PII** — Personally Identifiable Information. Data that can identify a specific individual: name, email, phone, address, SSN, biometrics, IP addresses, etc. Requires special handling in AI systems.

**Prompt injection** — An attack where a user manipulates a GenAI system by crafting inputs that override or alter the system's instructions. Includes direct injection (user input) and indirect injection (via external data the system processes). See [Section 6.2](FRAMEWORK.md#62-prompt-injection--adversarial-use).

**PSI** — Population Stability Index. A metric measuring how much the distribution of a variable has shifted between two datasets (typically training vs. production). PSI > 0.25 generally indicates significant drift.

### R

**RAG** — Retrieval-Augmented Generation. An architecture where a GenAI model retrieves relevant documents from a knowledge base before generating a response. Reduces hallucination by grounding responses in source material, but does not eliminate it.

**RAI Sponsor** — Organization-level role responsible for AI governance. Resolves escalations, sets risk appetite, ensures resources. Typically a VP/Director. Required for 🟡 High and above.

**Red teaming** — Structured adversarial testing where a team attempts to find failures, biases, vulnerabilities, and harmful outputs in an AI system. Required for 🟡 High and 🔴 Critical systems. For GenAI, this includes prompt injection and jailbreaking attempts.

**Risk tier** — Classification of an AI system based on its potential impact. Four levels: 🔴 Critical, 🟡 High, 🔵 Standard, ⚪ Low. Determines the required level of governance. See [Section 2](FRAMEWORK.md#2-risk-classification).

### S

**Shadow mode** — Running a new AI system in parallel with the existing process, where the AI's outputs are logged and reviewed but not acted upon. A safe way to validate performance before enabling autonomous operation.

**Stage gate** — See *Gate*.

**Stakeholder analysis** — Identifying all parties affected by an AI system — direct users, indirect stakeholders, oversight bodies, and vulnerable populations. Required for 🟡 High and 🔴 Critical. Template: [templates/stakeholder-analysis.md](templates/stakeholder-analysis.md).

### T

**Tool-calling** — A capability where an AI model can invoke external functions or APIs during its reasoning process. Enables AI agents. Requires scope boundaries and audit logging.

**Transparency** — The principle that stakeholders affected by an AI system can understand what it does, how decisions are made, and what data was used. The depth of explanation should match the audience (executive vs. engineer vs. affected individual).

### V

**Vendor AI** — AI systems you use but didn't build — SaaS AI features, API-based models, third-party platforms. You're still responsible for how they're used in your context. Template: [templates/vendor-ai-assessment.md](templates/vendor-ai-assessment.md).

---

*Terms not covered here? Open an issue — we'll add them.*
