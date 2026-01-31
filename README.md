# Responsible AI Framework (RAI)

**A practical, actionable framework for building and deploying AI responsibly.**

Most RAI frameworks tell you *what* to care about. This one tells you *what to do*.

## The Problem

Existing responsible AI frameworks are either too abstract (NIST AI RMF), too regulatory (EU AI Act), too vendor-specific (Microsoft RAI), or too academic. Teams read them, nod in agreement, and then don't know what to actually implement on Monday morning.

## The Solution

A complete, template-driven framework with:

- **5 core principles** — memorizable and testable
- **4 risk tiers** — effort scales with impact (not every system needs the same governance)
- **5 lifecycle stages** with clear gate criteria
- **7 reusable templates** — fill-in-the-blank, not write-from-scratch
- **2 worked examples** — classical ML (fraud detection) and GenAI (customer chatbot)
- **Compliance mapping** to NIST AI RMF, EU AI Act, ISO 42001, and Microsoft RAI

## Quick Start

**Get operational in 30 minutes:** Read [QUICKSTART.md](QUICKSTART.md)

**Deep dive:** Read [FRAMEWORK.md](FRAMEWORK.md)

## What's Included

```
rai-framework/
├── FRAMEWORK.md          # The full framework
├── QUICKSTART.md          # Get started in 30 minutes
├── templates/
│   ├── ai-registry.md            # Track all your AI systems
│   ├── use-case-statement.md     # Define what you're building and why
│   ├── impact-assessment.md      # Identify and assess risks
│   ├── model-card.md             # Document your model/system
│   ├── data-documentation.md     # Document your datasets
│   ├── test-report.md            # Validate before deployment
│   ├── monitoring-plan.md        # Watch it in production
│   └── incident-response.md      # Plan for when things go wrong
└── examples/
    ├── classical-ml-fraud-detection.md  # Worked example: fraud detection (XGBoost)
    └── genai-customer-chatbot.md        # Worked example: RAG chatbot (GPT-4)
```

## Who Is This For?

- **Engineering teams** building ML/AI systems who need governance without bureaucracy
- **Product managers** responsible for AI-powered features
- **Startups** that want to do the right thing without hiring a compliance team
- **Enterprises** looking for a practical starting point they can customize
- **Anyone** deploying AI who's read NIST/EU AI Act and thought "okay, but what do I *do*?"

## What Makes This Different

| Existing Frameworks | This Framework |
|---|---|
| Lists principles | Provides **decision trees and checklists** |
| One-size-fits-all | **Risk-tiered** — effort matches impact |
| Development-focused | **Full lifecycle** including monitoring and retirement |
| Requires weeks to understand | **30-minute quickstart** |
| Assumes dedicated ethics team | Works with **existing roles** |
| Either classical ML or GenAI | **Covers both** with conditional guidance |

## Works With (Not Against)

This framework is designed to complement, not compete with:

- [NIST AI Risk Management Framework](https://doi.org/10.6028/NIST.AI.100-1) — our Govern/Map/Measure/Manage mapping is explicit
- [EU AI Act](https://artificialintelligenceact.eu/) — our risk tiers align with EU risk categories
- [ISO/IEC 42001](https://www.iso.org/standard/81230.html) — our governance structure maps to ISO requirements
- [Microsoft Responsible AI](https://www.microsoft.com/en-us/ai/principles-and-approach) — our principles overlap with theirs

See the compliance mapping table in [FRAMEWORK.md](FRAMEWORK.md#8-compliance-mapping).

## Installation

There's nothing to install. This is a documentation framework. Clone or download and start using the templates:

```bash
git clone https://github.com/kriskimmerle/rai-framework.git
cd rai-framework
```

Copy templates into your project, customize for your context, and start filling them in.

## Contributing

Found a gap? Have a suggestion? Open an issue or PR. This framework is a living document.

## License

MIT — Use freely. Attribution appreciated but not required.
