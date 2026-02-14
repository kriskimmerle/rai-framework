# Third-Party / Vendor AI Assessment

> Use this template when adopting AI systems you didn't build - SaaS AI features, API-based models, vendor platforms, open-source models. You are still responsible for how third-party AI is used in your context.

## System Information

| Field | Value |
|-------|-------|
| **System Name (internal)** | |
| **Vendor / Provider** | |
| **Product / Service** | |
| **Owner (your org)** | |
| **Date** | |
| **Risk Tier (your use case)** | |

## Use Case Context

**What are you using this vendor AI for?**
*(Your specific application - not what the vendor markets it as)*



**Why a third-party solution instead of building?**
*(Cost, time-to-market, expertise gap, etc.)*



**Risk tier rationale:**
*(Classify based on YOUR use case, not the vendor's general risk level. A general-purpose LLM is neither low nor high risk by itself - how you deploy it determines the tier.)*



## Vendor Due Diligence

### Company & Stability

| Question | Answer | Notes |
|----------|--------|-------|
| Company name and jurisdiction | | |
| Years in operation | | |
| Funding / financial stability | | |
| Notable customers (social proof) | | |
| SOC 2 / ISO 27001 certified? | Yes / No / Unknown | |
| GDPR compliant? | Yes / No / N/A | |
| AI-specific certifications (ISO 42001, etc.)? | Yes / No | |
| Published responsible AI policy? | Yes / No → Link: | |

### Model & Technology

| Question | Answer | Notes |
|----------|--------|-------|
| What model(s) power the service? | | |
| Is the model proprietary, open-source, or third-party? | | |
| Model version / last update | | |
| Can you choose or pin model versions? | Yes / No | |
| Training data transparency (do they disclose sources?) | Full / Partial / None | |
| Fine-tuning or customization available? | Yes / No | |
| On-premises / private deployment option? | Yes / No | |

### Data Handling

| Question | Answer | Red Flag? |
|----------|--------|-----------|
| Does the vendor use your data to train their models? | Yes / No / Opt-out available | 🔴 if Yes with no opt-out |
| Data retention policy (how long do they keep inputs/outputs?) | | 🟡 if >30 days |
| Where is data processed (geographic region)? | | 🔴 if incompatible with your compliance |
| Is data encrypted in transit? | Yes / No | 🔴 if No |
| Is data encrypted at rest? | Yes / No | 🟡 if No |
| Can you request data deletion? | Yes / No | 🔴 if No for sensitive data |
| Do they share data with sub-processors? | Yes / No → Who? | |
| Data Processing Agreement (DPA) available? | Yes / No | 🔴 if No for regulated data |

### Performance & Reliability

| Question | Answer | Notes |
|----------|--------|-------|
| Published SLA (uptime guarantee)? | | |
| Historical uptime / status page? | | |
| Rate limits | | |
| Latency guarantees (p50 / p95 / p99) | | |
| What happens when the service is down? (your fallback) | | |

### Security

| Question | Answer | Notes |
|----------|--------|-------|
| API authentication method | | |
| Audit logging available? | Yes / No | |
| Vulnerability disclosure / bug bounty program? | Yes / No | |
| Penetration testing reports available? | Yes / No | |
| Incident notification process and SLA | | |
| Content safety / output filtering built in? | Yes / No | |

## Risk Assessment (Your Context)

### What Could Go Wrong

| Risk | Likelihood (L/M/H) | Severity (L/M/H) | Your Mitigation |
|------|--------------------|--------------------|-----------------|
| Vendor model hallucinates / gives wrong answers | | | |
| Vendor suffers data breach exposing your data | | | |
| Vendor changes model behavior (silent update) | | | |
| Vendor discontinues product or goes bankrupt | | | |
| Vendor AI produces biased / unfair outputs in your context | | | |
| Vendor is acquired - policies change | | | |
| Regulatory change makes vendor non-compliant | | | |
| Vendor AI used for unintended purpose by your users | | | |

### Vendor Lock-In Assessment

| Question | Answer |
|----------|--------|
| Can you export your data / customizations? | |
| Is there an open-standard API (easy to swap)? | |
| Estimated switching cost (time + money) | |
| Alternative vendors identified? | |
| Do you have a fallback if vendor disappears tomorrow? | |

## Contractual Protections

*(Check that these exist in your agreement)*

| Protection | In Contract? | Notes |
|------------|-------------|-------|
| Data ownership clause (your data stays yours) | ☐ | |
| Opt-out of training on your data | ☐ | |
| Data deletion on termination | ☐ | |
| Breach notification SLA | ☐ | |
| Liability / indemnification for AI outputs | ☐ | |
| Right to audit | ☐ | |
| Model change notification | ☐ | |
| Service level agreement with penalties | ☐ | |
| Termination rights (exit clause) | ☐ | |

## Your Controls

*(What guardrails are YOU putting around the vendor AI?)*

| Control | Implemented? | Details |
|---------|-------------|---------|
| Input validation / sanitization | ☐ | |
| Output filtering / safety checks | ☐ | |
| PII stripping before sending to vendor | ☐ | |
| Rate limiting | ☐ | |
| Logging and audit trail (your side) | ☐ | |
| Human review for high-stakes outputs | ☐ | |
| Fallback / degraded mode if vendor is down | ☐ | |
| Regular output quality sampling | ☐ | |
| Version pinning (if available) | ☐ | |

## Monitoring

| What to Monitor | Method | Frequency |
|----------------|--------|-----------|
| Output quality (sample review) | | Weekly |
| Vendor uptime / status | | Real-time |
| Cost / usage | | Weekly |
| User complaints about AI-generated content | | Continuous |
| Vendor changelog / model updates | | On release |
| Contract renewal / terms changes | | On notification |

## Decision

| Criterion | Assessment |
|-----------|------------|
| Does the vendor meet your data handling requirements? | Yes / No / Partial |
| Are contractual protections adequate? | Yes / No / Partial |
| Is the risk acceptable given your use case tier? | Yes / No |
| Do you have adequate controls on your side? | Yes / No / Partial |
| Is there a viable exit strategy? | Yes / No |

**Decision:**

- [ ] **Approve** - vendor meets requirements, controls in place
- [ ] **Approve with conditions** - must implement before go-live: _______________
- [ ] **Reject** - unacceptable risk: _______________
- [ ] **Defer** - need more information from vendor: _______________

## Re-Assessment Schedule

| Trigger | Action |
|---------|--------|
| Vendor updates terms of service | Review data handling & contractual sections |
| Vendor changes model | Re-evaluate output quality, re-run safety tests |
| Your use case scope changes | Re-classify risk tier, update controls |
| Annual review (minimum) | Full re-assessment |
| Security incident at vendor | Immediate re-assessment |

## Approval

| Role | Name | Decision | Date |
|------|------|----------|------|
| AI Owner | | | |
| AI Reviewer | | | |
| RAI Sponsor (High+) | | | |
| Security / Legal (if required) | | | |
