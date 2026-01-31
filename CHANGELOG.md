# Changelog

All notable changes to the RAI Framework are documented here.

---

## [1.1.0] — 2026-02-01

### Added
- **Stakeholder Analysis template** — Structured identification of direct, indirect, and oversight stakeholders plus vulnerable populations. Referenced in Stage 1 artifacts. (`templates/stakeholder-analysis.md`)
- **Retirement Plan template** — Full decommission checklist: migration, data disposition, infrastructure teardown, knowledge preservation, and post-mortem for Critical systems. (`templates/retirement-plan.md`)
- **Vendor AI Assessment template** — Due diligence for third-party AI: vendor stability, data handling, contractual protections, lock-in assessment, and your-side controls. (`templates/vendor-ai-assessment.md`)
- **AI Agent worked example** — DevOps autonomous agent with action classification tiers, dead man's switch, shadow mode rollout, and agent-specific red teaming. (`examples/genai-autonomous-agent.md`)
- **Executive Summary** — One-page overview for leadership: what the framework is, what it costs, what it gives you, and how to start. (`EXECUTIVE-SUMMARY.md`)
- **Adoption Maturity Model** — Five-level self-assessment (Reactive → Leading) with scorecards, pitfall guide, and planning template. (`MATURITY-MODEL.md`)
- **Glossary** — 35+ terms defined with cross-references to framework sections and templates. (`GLOSSARY.md`)
- **Contributing guide** — How to contribute improvements, report issues, and maintain quality. (`CONTRIBUTING.md`)

### Changed
- **FRAMEWORK.md** — Updated Stage 1 and Stage 5 artifact references to link to new templates. Added vendor AI guidance to governance section.
- **README.md** — Updated file tree, feature count, and descriptions to reflect all v1.1 additions.

---

## [1.0.0] — 2026-01-31

### Initial Release
- 5 core principles with concrete tests
- 4 risk tiers with decision tree and escalation factors
- 5 lifecycle stages with risk-scaled artifact matrix
- Stage gates with approval matrix
- GenAI-specific guidance (hallucination, prompt injection, content safety, agents, data/privacy)
- Monitoring signals and incident severity levels
- Compliance mapping to NIST AI RMF, EU AI Act, ISO 42001, Microsoft RAI
- 7 templates: AI registry, use case statement, impact assessment, model card, data documentation, test report, monitoring plan, incident response
- 2 worked examples: classical ML fraud detection (XGBoost), GenAI customer chatbot (RAG + GPT-4)
- 30-minute quickstart guide
