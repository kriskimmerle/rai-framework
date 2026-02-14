# RAI Adoption Maturity Model

**Where is your organization on the responsible AI journey? Use this to self-assess and plan your next steps.**

---

## The Five Levels

```
Level 1        Level 2        Level 3        Level 4        Level 5
REACTIVE  →  AWARENESS  →  STRUCTURED  →  INTEGRATED  →  LEADING
"We'll       "We know      "We have      "It's part    "We drive
deal with    we should     a process"    of how we     the standard"
it later"    do something"               build"
```

---

## Level 1: Reactive

**"We build AI. We don't think much about governance until something goes wrong."**

### Characteristics
- No AI registry - nobody knows how many AI systems exist
- No risk classification process
- AI decisions about documentation, testing, and monitoring are ad-hoc
- Incident response for AI is the same as for any software bug
- Compliance questions are answered retroactively

### Risks at This Level
- Regulatory exposure (especially with EU AI Act enforcement)
- Bias and safety issues discovered in production or by users
- No accountability - when something goes wrong, nobody owns it
- Vendor AI adopted without due diligence

### How to Move to Level 2
- [ ] Acknowledge that AI governance is needed (leadership buy-in)
- [ ] Assign someone to own the effort (even part-time)
- [ ] Read the [QUICKSTART.md](QUICKSTART.md) - 30 minutes

---

## Level 2: Awareness

**"We know responsible AI matters. We're starting to do something about it."**

### Characteristics
- AI registry exists (maybe incomplete)
- Risk classification happens for new projects (sometimes)
- Some documentation - model cards or READMEs for major systems
- Awareness of regulations but no formal compliance mapping
- One or two "champion" individuals push for good practices

### What You Have
- [ ] AI registry (partial)
- [ ] Risk classification for some systems
- [ ] Basic documentation for high-profile systems
- [ ] At least one person who cares about this

### Risks at This Level
- Inconsistency - some teams do it, others don't
- Key-person dependency - if the champion leaves, governance dies
- Partial visibility - unknown systems can't be governed

### How to Move to Level 3
- [ ] Complete the AI registry (ALL systems, including vendor AI)
- [ ] Classify every system using the [risk decision tree](FRAMEWORK.md#2-risk-classification)
- [ ] Adopt the template set for at least all 🟡 High and 🔴 Critical systems
- [ ] Define the AI Owner role formally

---

## Level 3: Structured

**"We have a process. It's documented, repeatable, and applies to all AI projects."**

### Characteristics
- Complete AI registry maintained actively
- Risk classification is standard practice for all new AI projects
- Lifecycle stages and gate reviews are followed
- Templates are used consistently
- AI Owner role is formally assigned for every system
- Monitoring is in place for production systems
- Incident response plans exist for High+ systems
- Vendor AI is assessed before adoption

### What You Have
- [ ] Complete AI registry with all systems classified
- [ ] Lifecycle gates enforced for 🟡 High and 🔴 Critical
- [ ] Templates in use across teams
- [ ] AI Owners assigned for all production systems
- [ ] Monitoring dashboards for Standard+ systems
- [ ] Incident response plans for High+ systems
- [ ] Vendor AI assessment process
- [ ] Quarterly reviews happening for High systems

### Risks at This Level
- Process without culture - governance feels like bureaucracy
- Checkbox mentality - templates filled in but not taken seriously
- Reactive monitoring - alerts exist but root cause analysis is weak

### How to Move to Level 4
- [ ] Integrate RAI into existing development workflows (not a separate process)
- [ ] Train all engineers (not just ML/AI specialists)
- [ ] Establish metrics for governance health (not just compliance)
- [ ] Create feedback loops - learnings from incidents improve the process
- [ ] Peer review of risk assessments across teams

---

## Level 4: Integrated

**"Responsible AI isn't a separate activity - it's woven into how we build everything."**

### Characteristics
- RAI considerations are part of project planning, sprint work, and code review
- Engineers proactively identify risks (not just when asked)
- Cross-team learning - incident insights shared openly
- Fairness and safety testing is automated in CI/CD where possible
- Governance evolves based on real experience, not just theory
- RAI Sponsor actively engaged, not just on paper
- External stakeholder input (user research, advisory board)
- Vendor AI governance is proactive (re-assessments, exit strategies)

### What You Have (everything from Level 3, plus)
- [ ] RAI integrated into sprint planning and code review
- [ ] Automated fairness/safety checks in CI pipeline
- [ ] Cross-team incident learning (blameless post-mortems shared)
- [ ] Governance process updated based on lessons learned
- [ ] All engineers trained on RAI basics
- [ ] User research includes AI-specific questions
- [ ] Proactive vendor re-assessments

### Risks at This Level
- Complacency - "we're doing great" while the threat landscape evolves
- Process ossification - framework becomes rigid instead of adaptive
- Emerging tech gaps - new AI capabilities (agents, multimodal) outpace governance

### How to Move to Level 5
- [ ] Contribute to industry standards and best practices
- [ ] Publish your learnings (blog posts, talks, open-source contributions)
- [ ] Engage with regulators proactively
- [ ] Benchmark against other organizations
- [ ] Invest in AI governance tooling (beyond templates)

---

## Level 5: Leading

**"We don't just follow responsible AI practices - we help define them."**

### Characteristics
- Published responsible AI commitments and transparency reports
- Contribute to industry standards (NIST, ISO, etc.)
- Share learnings publicly (case studies, tools, frameworks)
- Proactive regulatory engagement
- Third-party audits of AI systems (voluntarily, for Critical systems)
- AI governance metrics reported to the board
- Innovation in RAI tooling and practices
- Mentor other organizations

### What This Looks Like
- [ ] Public transparency report on AI use and governance
- [ ] External audit program for Critical systems
- [ ] Board-level AI governance reporting
- [ ] Published case studies or open-source governance tools
- [ ] Active participation in standards bodies
- [ ] Mentoring or advising other organizations

---

## Self-Assessment Scorecard

Rate your organization honestly for each dimension.

| Dimension | L1 | L2 | L3 | L4 | L5 | Your Level |
|-----------|----|----|----|----|-----|------------|
| **Inventory** - Do you know what AI systems you have? | No registry | Partial list | Complete registry | Actively maintained, includes vendor AI | Published transparency report | |
| **Risk Classification** - Are systems classified by risk? | No classification | Ad-hoc, some systems | All systems classified | Classification reviewed regularly | External validation of classifications | |
| **Documentation** - Are AI systems documented? | No docs | Informal READMEs | Templates used consistently | Living docs updated on change | Published externally where appropriate | |
| **Testing** - Do you test for fairness and safety? | Functional tests only | Some bias testing for major systems | Fairness + safety testing for High+ | Automated in CI/CD | External red teaming, published results | |
| **Monitoring** - Do you watch AI in production? | Basic uptime only | Metrics for major systems | Dashboards + alerts for Standard+ | Automated drift detection, proactive review | Real-time fairness monitoring, public status | |
| **Incident Response** - Can you handle AI incidents? | Same as software bugs | Informal plan for major systems | Documented plans for High+ | Blameless post-mortems, cross-team learning | Public incident reports, industry learning | |
| **Governance** - Who's accountable? | Nobody specific | Informal champions | Formal AI Owner role | RAI Sponsor engaged, org-wide ownership | Board-level oversight, external advisory | |
| **Culture** - Do people care? | Compliance-driven | Champions exist | Teams understand the value | Engineers proactively raise concerns | Industry leadership, public advocacy | |

**Your overall level = your lowest dimension score** (a chain is as strong as its weakest link).

---

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| **Governance theater** | Templates filled in but nobody reads them | Require gate reviews to reference specific sections |
| **Over-engineering for low risk** | ⚪ Low systems get the same process as 🔴 Critical | Trust the risk tiers - lightweight governance is intentional |
| **Key-person dependency** | One champion does all the governance work | Distribute ownership - AI Owner role for every system |
| **Ignoring vendor AI** | "We didn't build it, not our problem" | You deploy it, you own the risk. Use the vendor assessment |
| **Static governance** | Process hasn't changed in a year | Quarterly retrospective on the governance process itself |
| **Compliance-only mindset** | "We need this for the EU AI Act" | Compliance is a floor, not a ceiling. Focus on actual harm prevention |

---

## Planning Template

**Current overall level:** ___

**Target level (6 months):** ___

| Gap to Close | Actions | Owner | Target Date |
|-------------|---------|-------|-------------|
| | | | |
| | | | |
| | | | |

**First step:** _______________

---

*Full framework: [FRAMEWORK.md](FRAMEWORK.md) · Quickstart: [QUICKSTART.md](QUICKSTART.md) · Executive summary: [EXECUTIVE-SUMMARY.md](EXECUTIVE-SUMMARY.md)*
