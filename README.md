![CI](https://github.com/kriskimmerle/rai-framework/actions/workflows/test.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

# Responsible AI Framework

**Governance that works on Monday morning.**

Every organization deploying AI needs governance. The problem is that existing frameworks - NIST AI RMF, EU AI Act guidance, ISO 42001 - tell you what to care about but not what to do. Teams read them, agree in principle, and then build the same ungoverned systems they were building before.

This framework is different. It gives you decision trees, templates, and checklists. Risk tiers that scale effort to actual impact. A 30-minute quickstart that gets you from nothing to operational. Worked examples for classical ML, GenAI, and autonomous agents.

If you have been looking at your AI systems thinking "we should probably govern these" but not sure where to start, start here.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## What is in the box

| Document | Purpose |
|----------|---------|
| [QUICKSTART.md](QUICKSTART.md) | Get operational in 30 minutes |
| [FRAMEWORK.md](FRAMEWORK.md) | The full framework - principles, risk tiers, lifecycle, gates |
| [EXECUTIVE-SUMMARY.md](EXECUTIVE-SUMMARY.md) | One-page overview for leadership |
| [MATURITY-MODEL.md](MATURITY-MODEL.md) | Self-assess your organization and plan next steps |
| [GLOSSARY.md](GLOSSARY.md) | Shared vocabulary (35+ terms) |
| [templates/](templates/) | 11 fill-in-the-blank templates for every lifecycle stage |
| [examples/](examples/) | 3 worked examples: fraud detection, customer chatbot, DevOps agent |

## Core ideas

**Risk tiers.** Not every AI system needs the same scrutiny. A content recommendation widget is not a credit scoring model. Four tiers (Critical, High, Standard, Low) determine how much process to apply. Most of your systems are probably Standard or Low.

**Lifecycle gates.** Every AI system goes through Scope, Build, Test, Deploy, Retire. Between each stage there is a checkpoint. Higher risk means more rigorous checks. Lower risk means lightweight self-certification.

**Templates, not essays.** 11 ready-to-use templates. Fill in the blanks. Use case statements, impact assessments, model cards, monitoring plans, incident response, vendor AI assessments. Teams fill them in rather than staring at a blank page.

**Existing roles.** No ethics team required. The AI Owner is your product manager or tech lead. The AI Reviewer is a senior engineer. New roles only appear at the Critical tier.

## How this maps to existing standards

| This Framework | NIST AI RMF | EU AI Act | ISO 42001 |
|---------------|-------------|-----------|-----------|
| Risk Tiers | GOVERN (Risk Appetite) | Risk Categories (Art. 6) | Context of Organization |
| Lifecycle Gates | MANAGE | Conformity Assessment (Art. 43) | Planning & Operation |
| AI Registry | MAP | EU Database (Art. 71) | Statement of Applicability |
| Monitoring | MEASURE, MANAGE | Post-Market Monitoring (Art. 72) | Monitoring & Review |
| Incident Response | MANAGE | Serious Incident Reporting (Art. 73) | Incident Management |

This framework is designed to satisfy requirements from these standards, not compete with them. The compliance mapping in [FRAMEWORK.md](FRAMEWORK.md#8-compliance-mapping) is explicit.

## Who this is for

- Engineering teams building ML/AI who need governance without bureaucracy
- Product managers responsible for AI-powered features
- Startups that want to do the right thing without hiring a compliance team
- Enterprises looking for a practical starting point they can customize
- Anyone who has read NIST or EU AI Act guidance and thought "okay, but what do I actually do?"

## Getting started

```bash
git clone https://github.com/kriskimmerle/rai-framework.git
cd rai-framework
```

Read [QUICKSTART.md](QUICKSTART.md). You will have an AI registry, risk classifications, and monitoring plan within 30 minutes.

## Contributing

Found a gap? Open an issue or PR. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. Use freely. Attribution appreciated but not required.
