# Monitoring Plan

> Required for 🔵 Standard and above. Complete before deployment.

## System Information

| Field | Value |
|-------|-------|
| **System Name** | |
| **Owner** | |
| **Date** | |
| **Risk Tier** | |

## Metrics to Monitor

### Performance Metrics

| Metric | Baseline | Alert Threshold | Check Frequency | Dashboard/Tool |
|--------|----------|-----------------|-----------------|----------------|
| | | | | |
| | | | | |
| | | | | |

### Fairness Metrics (🟡 High and 🔴 Critical)

| Metric | Subgroups | Baseline | Alert Threshold | Check Frequency |
|--------|-----------|----------|-----------------|-----------------|
| | | | | |
| | | | | |

### Operational Metrics

| Metric | Alert Threshold | Check Frequency |
|--------|-----------------|-----------------|
| Latency (p95) | | |
| Error rate | | |
| Throughput | | |
| Availability | | |
| Cost per request/prediction | | |

### Data Drift (Classical ML)

| Feature/Signal | Method | Alert Threshold | Check Frequency |
|---------------|--------|-----------------|-----------------|
| | | | |
| | | | |

### Safety Signals (GenAI)

| Signal | Detection Method | Alert Threshold | Check Frequency |
|--------|-----------------|-----------------|-----------------|
| Harmful output rate | | | |
| Hallucination rate | | | |
| PII leakage incidents | | | |
| Abuse/misuse patterns | | | |

## Alerting

| Alert Level | Notification Method | Recipient | Response Time |
|-------------|-------------------|-----------|---------------|
| Critical (P0) | | | Immediate |
| High (P1) | | | Hours |
| Medium (P2) | | | 1 business day |
| Low (P3) | | | 1 week |

## Review Schedule

| Frequency | What to Review | Reviewer |
|-----------|---------------|----------|
| Daily | Automated alerts, error rates | On-call engineer |
| Weekly | Performance trends, drift signals | AI Owner |
| Monthly (Critical) / Quarterly (High) / Annually (Standard) | Full review: metrics, incidents, risk tier | AI Owner + Reviewer |

## Rollback Criteria

**Automatic rollback triggers:**
*(What conditions should trigger an automatic rollback?)*



**Manual rollback process:**
*(Steps to roll back to previous version)*

1.
2.
3.

**Rollback tested?** Yes / No

**Last rollback test date:**

## User Feedback

| Channel | How Monitored | Response Process |
|---------|--------------|-----------------|
| | | |

## Change Log

| Date | Change | Changed By |
|------|--------|------------|
| | | |
