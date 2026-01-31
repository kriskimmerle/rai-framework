# RAI Framework — Quickstart

**Get responsible AI governance running in 30 minutes.**

This guide gets you from zero to operational. You don't need to read the full framework first.

---

## Minute 0–5: Understand the Basics

The framework has **5 principles** (memorize these):

1. **Know Your Impact** — What happens when this system fails?
2. **Own It** — One named human is accountable
3. **Show Your Work** — Stakeholders can understand decisions
4. **Stay Vigilant** — Monitor in production, not just at launch
5. **Respect People** — Privacy, fairness, and dignity come first

And **4 risk tiers** (determines how much process to apply):

| Tier | When to Use | Effort |
|------|-------------|--------|
| 🔴 Critical | Affects rights, safety, freedom | Full governance |
| 🟡 High | Major financial/reputational impact | Standard governance |
| 🔵 Standard | Moderate impact, external-facing | Lightweight governance |
| ⚪ Low | Internal, easily reversible | Minimal governance |

---

## Minute 5–10: Create Your AI Registry

Copy [templates/ai-registry.md](templates/ai-registry.md) and list every AI system your team runs.

For each system, fill in:
- **Name** — what you call it
- **Owner** — who's accountable (a specific person, not a team)
- **Risk Tier** — use the decision tree below
- **Status** — Development / Production / Retired

### Quick Risk Classification

Ask these questions in order:

1. **Does it decide about people's rights, safety, health, or legal status?** → 🔴 Critical
2. **Could failure cause >$100K loss, regulatory action, or PR crisis?** → 🟡 High
3. **Does it affect external users?** → 🔵 Standard
4. **Is it internal and easily reversible?** → ⚪ Low

**Bump up one tier** if: uses sensitive data, no human in the loop, affects vulnerable populations, or makes >10K decisions/day.

---

## Minute 10–15: Pick Your First System

Choose **one** system to run through the framework — ideally your highest-risk one. Better to get it right on the important thing than to half-do everything.

Fill in these templates for that system:
1. [templates/use-case-statement.md](templates/use-case-statement.md) — what it does and why
2. [templates/impact-assessment.md](templates/impact-assessment.md) — what could go wrong

These two documents are the foundation. Everything else builds on them.

---

## Minute 15–20: Assign Roles

You need at minimum:

| Role | Who | What They Do |
|------|-----|-------------|
| **AI Owner** | The person closest to the system | Owns it end-to-end, approves deployment |
| **AI Reviewer** | Someone who can review independently | Validates testing and risk assessments |

For 🟡 High and 🔴 Critical systems, these **must be different people**.

For small teams: the AI Owner can self-certify ⚪ Low and 🔵 Standard systems.

---

## Minute 20–25: Set Up Monitoring

Every system in production (🔵 Standard and above) needs monitoring:

### Minimum Viable Monitoring

- [ ] **Performance metric tracked** — accuracy, error rate, or equivalent
- [ ] **Alert on significant degradation** — automated, goes to the AI Owner
- [ ] **User feedback channel** — a way for users to report issues
- [ ] **Monthly check-in** — 15 minutes, AI Owner reviews metrics

For 🟡 High systems, add:
- [ ] Fairness metrics (if applicable)
- [ ] Incident response plan (who to call, how to rollback)

Use [templates/monitoring-plan.md](templates/monitoring-plan.md) to document this.

---

## Minute 25–30: Commit to a Review Cadence

| Risk Tier | Review Frequency | What to Review |
|-----------|-----------------|----------------|
| 🔴 Critical | Monthly | Full metrics, fairness, incidents, risk tier |
| 🟡 High | Quarterly | Metrics, incidents, major changes |
| 🔵 Standard | Annually | Is it still working? Still needed? |
| ⚪ Low | On change | Only review when something changes |

Put the first review on your calendar. Right now.

---

## You're Done (For Now)

You now have:
- ✅ An AI registry
- ✅ Risk classifications for your systems
- ✅ Owners assigned
- ✅ Impact assessment for your highest-risk system
- ✅ Monitoring in place (or a plan to set it up)
- ✅ Review cadence committed

### Next Steps

- **This week:** Complete the use case statement and impact assessment for remaining 🟡 High and 🔴 Critical systems
- **This month:** Run your first formal stage-gate review for one system
- **This quarter:** Fill in model cards and data documentation for all 🔵 Standard+ systems
- **Ongoing:** Review, learn, iterate. This framework should evolve with you.

### Going Deeper

- Read the [full framework](FRAMEWORK.md) for detailed guidance
- Check [examples/](examples/) for worked examples (classical ML and GenAI)
- Use [templates/](templates/) for all the artifacts

---

## Common Questions

**Q: Do I need all these artifacts for every system?**
No. The artifact matrix in the framework shows exactly which artifacts are required for each risk tier. ⚪ Low systems need almost nothing.

**Q: We don't have an ethics team. Can we still use this?**
Yes. The framework is designed for existing roles. The AI Owner is typically a product manager or tech lead. The AI Reviewer is a senior engineer. No new roles required until you have 🔴 Critical systems.

**Q: What about third-party AI (e.g., using OpenAI's API)?**
You're still responsible for how it's used. Classify based on *your use case*, not the model itself. A GPT-4 powered internal FAQ bot might be ⚪ Low. A GPT-4 powered medical advice chatbot is 🔴 Critical.

**Q: How does this relate to the EU AI Act / NIST / ISO 42001?**
The compliance mapping table in the full framework shows how each element maps. This framework is designed to be compatible, not competing.

**Q: This feels like a lot of paperwork.**
For ⚪ Low and 🔵 Standard systems, you're looking at ~1 hour of documentation total. The overhead scales with risk. If a system is 🔴 Critical, the paperwork is the least of your concerns — you *want* rigor there.
