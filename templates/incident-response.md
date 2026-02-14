# Incident Response Plan

> Required for 🟡 High and 🔴 Critical systems. Complete before deployment.

## System Information

| Field | Value |
|-------|-------|
| **System Name** | |
| **Owner** | |
| **Date** | |
| **Risk Tier** | |

## Contacts

| Role | Name | Contact | Backup |
|------|------|---------|--------|
| AI Owner | | | |
| On-Call Engineer | | | |
| RAI Sponsor | | | |
| Legal (if needed) | | | |
| Communications (if needed) | | | |

## Severity Definitions

| Level | Definition | Response Time | Examples |
|-------|-----------|---------------|---------|
| **P0 - Critical** | Active harm, safety incident, data breach, regulatory violation | **Immediate** (within minutes) | PII leak, discriminatory decisions causing harm, system compromise |
| **P1 - High** | Significant degradation, potential harm, regulatory risk | **Within 2 hours** | Major accuracy drop, fairness metric violation, sustained errors |
| **P2 - Medium** | Noticeable issues, no immediate harm | **Within 1 business day** | Moderate performance drift, increased error rate, user complaints |
| **P3 - Low** | Minor issues, cosmetic, no user impact | **Within 1 week** | Slight metric dip, non-critical logging issue |

## Response Process

### Step 1: Detect

**How incidents are detected:**
- [ ] Automated monitoring alerts
- [ ] User reports / complaints
- [ ] Internal review / audit
- [ ] External report (researcher, regulator, media)

### Step 2: Assess

- [ ] Confirm the incident is real (not a false alert)
- [ ] Assign severity level (P0/P1/P2/P3)
- [ ] Identify scope: how many users/decisions affected?
- [ ] Notify appropriate contacts per severity level

### Step 3: Contain

**P0/P1 containment options:**
- [ ] Disable the system entirely
- [ ] Rollback to previous version
- [ ] Enable human-in-the-loop for all decisions
- [ ] Reduce system scope (e.g., limit to certain user segments)
- [ ] Block specific input patterns

**Containment decision maker:** *(who has authority to disable the system?)*


### Step 4: Investigate

- [ ] Identify root cause
- [ ] Determine full scope of impact
- [ ] Collect evidence (logs, model outputs, data samples)
- [ ] Document timeline

### Step 5: Remediate

- [ ] Implement fix
- [ ] Validate fix (test with the scenario that caused the incident)
- [ ] Deploy fix through normal gate process (or expedited for P0/P1)
- [ ] Verify monitoring catches this type of issue going forward

### Step 6: Review

- [ ] Write post-incident report (template below)
- [ ] Update monitoring/alerting to prevent recurrence
- [ ] Update this incident response plan if needed
- [ ] Share learnings with team
- [ ] Notify affected users if appropriate

## Communication

### Internal Communication

| Severity | Who to Notify | When | How |
|----------|--------------|------|-----|
| P0 | AI Owner, RAI Sponsor, Legal, Exec team | Immediately | Phone/page |
| P1 | AI Owner, RAI Sponsor | Within 2 hours | Message/email |
| P2 | AI Owner | Within 1 day | Email |
| P3 | AI Owner | Next review cycle | Ticket |

### External Communication (if needed)

| Trigger | Action |
|---------|--------|
| User data affected | Notify legal → determine disclosure obligations |
| Regulatory reporting required | Notify legal → file within required timeframe |
| Public awareness likely | Notify communications → prepare statement |
| User harm confirmed | Direct notification to affected users |

## Post-Incident Report Template

```markdown
# Incident Report: [System Name] - [Date]

## Summary
One paragraph: what happened, impact, resolution.

## Timeline
- HH:MM - Incident detected by [method]
- HH:MM - Severity assessed as [P0/P1/P2/P3]
- HH:MM - [Containment action taken]
- HH:MM - Root cause identified
- HH:MM - Fix deployed
- HH:MM - Confirmed resolved

## Impact
- Users affected: [number]
- Decisions affected: [number]
- Duration: [time]
- Severity: [P0/P1/P2/P3]

## Root Cause
What went wrong and why.

## Resolution
What was done to fix it.

## Prevention
What changes are being made to prevent recurrence.

## Lessons Learned
What did we learn?
```

## Incident Log

| Date | Severity | Summary | Resolution | Report Link |
|------|----------|---------|-----------|-------------|
| | | | | |
