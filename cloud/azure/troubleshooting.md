# Azure Troubleshooting

## Scenario 01 — Azure outage pattern 1

**Difficulty:** Intermediate
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 02 — Azure outage pattern 2

**Difficulty:** Intermediate
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 03 — Azure outage pattern 3

**Difficulty:** Intermediate
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 04 — Azure outage pattern 4

**Difficulty:** Intermediate
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 05 — Azure outage pattern 5

**Difficulty:** Intermediate
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 06 — Azure outage pattern 6

**Difficulty:** Intermediate
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 07 — Azure outage pattern 7

**Difficulty:** Intermediate
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 08 — Azure outage pattern 8

**Difficulty:** Intermediate
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 09 — Azure outage pattern 9

**Difficulty:** Advanced
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 10 — Azure outage pattern 10

**Difficulty:** Advanced
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 11 — Azure outage pattern 11

**Difficulty:** Advanced
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 12 — Azure outage pattern 12

**Difficulty:** Advanced
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 13 — Azure outage pattern 13

**Difficulty:** Advanced
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 14 — Azure outage pattern 14

**Difficulty:** Advanced
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 15 — Azure outage pattern 15

**Difficulty:** Advanced
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 16 — Azure outage pattern 16

**Difficulty:** Advanced
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 17 — Azure outage pattern 17

**Difficulty:** Advanced
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 18 — Azure outage pattern 18

**Difficulty:** Advanced
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 19 — Azure outage pattern 19

**Difficulty:** Senior
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 20 — Azure outage pattern 20

**Difficulty:** Senior
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 21 — Azure outage pattern 21

**Difficulty:** Senior
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 22 — Azure outage pattern 22

**Difficulty:** Senior
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 23 — Azure outage pattern 23

**Difficulty:** Senior
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 24 — Azure outage pattern 24

**Difficulty:** Senior
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?

## Scenario 25 — Azure outage pattern 25

**Difficulty:** Senior
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```

### Situation

A production path involving azure is failing and the on-call engineer must narrow the issue quickly with real evidence.

### Symptoms

- Users report errors or timeouts
- Dashboards show one or more regressions
- Recent rollout, policy, or dependency change may be involved

### Evidence

```text
Error rate increased
Latency worsened
At least one recent configuration or deployment change exists
```

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Investigation flow

```text
Symptom
  ↓
Confirm target environment and identity
  ↓
Check edge or entry-point behavior
  ↓
Check routing / policy / service mapping
  ↓
Check workload or dependency health
  ↓
Validate fix and prevention
```

### What would you investigate first?

Start with the narrowest boundary that can explain the user-visible symptom and the recent change together.

### What evidence are we looking for?

Evidence that shows whether the failure is caused by identity, naming, routing, endpoint health, rollout drift, quota, or a downstream dependency.

### Possible root causes

- Mis-scoped permissions
- DNS or route drift
- Stale TLS or broken secrets
- Saturated compute or dependency
- Bad rollout or policy change
- Missing telemetry hiding the true failure

### Most likely diagnosis

The most likely diagnosis is the one that matches both the symptom timing and the authoritative control-plane evidence, not the loudest dashboard.

### Resolution

Apply the smallest safe rollback or correction first, then verify end-to-end recovery with the same signals that first proved the failure.

### Prevention

Add automation, safer rollout checks, better quota visibility, stronger policies, or clearer dashboards so the next incident is cheaper.

### Observability

Call out the metric, log, and audit signal that should have shortened time-to-diagnosis.

### Security considerations

Avoid permanent permission expansion or temporary public exposure as a shortcut fix.

### Senior engineer discussion

A senior engineer explains why certain hypotheses were ruled out, protects adjacent services from blast radius, and captures what the platform should standardize next.

### Follow-up questions

- What would you instrument next?
- What is the rollback path?
- How do you prove the issue is fully resolved?
