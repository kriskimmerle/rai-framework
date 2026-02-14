# AI System Retirement Plan

> Use this template when decommissioning an AI system. Required for 🔵 Standard and above.

## System Information

| Field | Value |
|-------|-------|
| **System Name** | |
| **Owner** | |
| **Date** | |
| **Risk Tier** | |
| **Production Since** | |
| **Target Retirement Date** | |

## Reason for Retirement

- [ ] Replaced by a new system → Replacement: _______________
- [ ] No longer needed (business change)
- [ ] Performance degraded beyond acceptable thresholds
- [ ] Risk profile changed - no longer acceptable to operate
- [ ] Regulatory or compliance requirement
- [ ] Cost no longer justified
- [ ] Other: _______________

**Detailed rationale:**



## Impact Analysis

### Who is affected by the shutdown?

| Stakeholder Group | How Affected | Notification Plan |
|-------------------|-------------|-------------------|
| *Example: Customer support team* | *Loses automated ticket triage* | *Email 30 days prior, training on replacement* |
| | | |
| | | |

### Downstream Dependencies

| System / Process | Dependency Type | Migration Plan |
|-----------------|----------------|----------------|
| *Example: Dashboard reporting* | *Consumes model predictions* | *Switch to new model endpoint by [date]* |
| | | |
| | | |

## Migration Plan

*(Required if a replacement system exists)*

| Step | Owner | Target Date | Status |
|------|-------|-------------|--------|
| New system validated and deployed | | | ☐ |
| Parallel operation period (both systems running) | | | ☐ |
| Traffic fully migrated to new system | | | ☐ |
| Old system serving zero traffic confirmed | | | ☐ |
| Old system disabled | | | ☐ |

**Parallel operation period:** _____ days/weeks

**Rollback plan during migration:**



## Data Disposition

*(Required for 🟡 High and 🔴 Critical)*

### Training Data

| Dataset | Action | Justification | Deadline |
|---------|--------|---------------|----------|
| | Retain / Archive / Delete | | |
| | Retain / Archive / Delete | | |

### Model Artifacts

| Artifact | Action | Justification | Deadline |
|----------|--------|---------------|----------|
| Model weights / binaries | Retain / Archive / Delete | | |
| Configuration files | Retain / Archive / Delete | | |
| Feature pipelines | Retain / Archive / Delete | | |

### Production Data (Logs, Predictions, Feedback)

| Data Type | Retention Required? | Basis (regulatory, audit, etc.) | Delete After |
|-----------|--------------------|---------------------------------|-------------|
| Prediction logs | | | |
| User feedback | | | |
| Monitoring data | | | |
| Incident reports | | | |

### Data Deletion Verification

- [ ] All data marked for deletion has been deleted
- [ ] Deletion verified (not just in primary storage - check backups, caches, replicas)
- [ ] Deletion documented with timestamps
- [ ] Data Processing Agreements updated or terminated

## Infrastructure Decommission

| Resource | Action | Owner | Deadline |
|----------|--------|-------|----------|
| Compute (servers, GPU, endpoints) | | | |
| Storage (S3, databases, vector stores) | | | |
| Monitoring / alerting rules | | | |
| API endpoints / DNS records | | | |
| CI/CD pipelines | | | |
| Access credentials / API keys | Rotate or revoke | | |

## Communication

| Audience | Message | Channel | When |
|----------|---------|---------|------|
| Internal teams | Retirement timeline, migration instructions | | 30 days prior |
| External users (if applicable) | Service change notice, alternatives | | Per contractual obligations |
| Regulators (if applicable) | System removed from registry | | Per regulatory timeline |

## Knowledge Preservation

*(What did we learn from operating this system?)*

**What worked well:**



**What didn't work:**



**Recommendations for successor system:**



**Documentation to preserve:** *(link to model card, incident reports, performance history)*



## Post-Mortem

*(Required for 🔴 Critical systems)*

**System lifetime:** _____ months/years

**Total incidents during operation:**

| Severity | Count |
|----------|-------|
| P0 - Critical | |
| P1 - High | |
| P2 - Medium | |
| P3 - Low | |

**Key learnings for the organization:**



## Retirement Checklist

| Step | Owner | Done |
|------|-------|------|
| Stakeholders notified | | ☐ |
| Migration complete (if applicable) | | ☐ |
| System disabled / endpoints removed | | ☐ |
| Data disposition complete | | ☐ |
| Infrastructure decommissioned | | ☐ |
| Access credentials revoked | | ☐ |
| AI Registry updated (status → Retired) | | ☐ |
| Monitoring and alerts removed | | ☐ |
| Knowledge documented | | ☐ |
| Post-mortem complete (Critical only) | | ☐ |
| Final sign-off | | ☐ |

## Approval

| Role | Name | Approved | Date |
|------|------|----------|------|
| AI Owner | | ☐ | |
| AI Reviewer | | ☐ | |
| RAI Sponsor (High+) | | ☐ | |
