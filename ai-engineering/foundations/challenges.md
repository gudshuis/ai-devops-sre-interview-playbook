# Foundations Challenges

## Challenge 01 — Foundations practical investigation 1

**Difficulty:** Beginner

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 02 — Foundations practical investigation 2

**Difficulty:** Beginner

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 03 — Foundations practical investigation 3

**Difficulty:** Beginner

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 04 — Foundations practical investigation 4

**Difficulty:** Beginner

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 05 — Foundations practical investigation 5

**Difficulty:** Beginner

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 06 — Foundations practical investigation 6

**Difficulty:** Intermediate

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 07 — Foundations practical investigation 7

**Difficulty:** Intermediate

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 08 — Foundations practical investigation 8

**Difficulty:** Intermediate

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 09 — Foundations practical investigation 9

**Difficulty:** Intermediate

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 10 — Foundations practical investigation 10

**Difficulty:** Intermediate

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 11 — Foundations practical investigation 11

**Difficulty:** Senior

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 12 — Foundations practical investigation 12

**Difficulty:** Senior

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 13 — Foundations practical investigation 13

**Difficulty:** Senior

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 14 — Foundations practical investigation 14

**Difficulty:** Senior

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 15 — Foundations practical investigation 15

**Difficulty:** Senior

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 16 — Foundations practical investigation 16

**Difficulty:** Senior

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 17 — Foundations practical investigation 17

**Difficulty:** Senior

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 18 — Foundations practical investigation 18

**Difficulty:** Senior

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 19 — Foundations practical investigation 19

**Difficulty:** Senior

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 20 — Foundations practical investigation 20

**Difficulty:** Senior

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 21 — Foundations practical investigation 21

**Difficulty:** Staff

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 22 — Foundations practical investigation 22

**Difficulty:** Staff

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 23 — Foundations practical investigation 23

**Difficulty:** Staff

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 24 — Foundations practical investigation 24

**Difficulty:** Principal

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.

## Challenge 25 — Foundations practical investigation 25

**Difficulty:** Principal

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live foundations problem with incomplete context, recent changes, and pressure to restore service without guessing.

### Starting evidence

```text
Service owner reports user impact.
Dashboard shows a regression.
Recent infrastructure or config changes are suspected.
```

### Your task

Identify the failing boundary, gather evidence, and implement the smallest safe fix. Explain how you would prove recovery and prevent recurrence.

### Terminal tasks

1. Confirm the active environment and identity.
2. Run the fastest command that proves the first failing boundary.
3. Inspect logs, metrics, config, or runtime state.
4. Modify the smallest relevant file, YAML, policy, or command path if needed.
5. Validate the fix and document follow-up automation.

### Useful tools

`pwd`, `ls`, `cd`, `cat`, `less`, `tail`, `journalctl`, `systemctl`

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
pwd
ls -lah /var/log
cd /etc/systemd/system
cat /etc/resolv.conf
```

### Explanation

These commands work because they move from context validation into concrete evidence collection. The point is to prove the failure path step by step rather than assuming the first suspicious component is the root cause.

### What a senior engineer would also check

- Blast radius beyond the first failing service
- Monitoring gaps that slowed diagnosis
- Security impact of the proposed fix
- Rollback safety
- Prevention and automation opportunities

### Hard mode

Repeat the challenge assuming one of your main observability signals is missing and the incident spans more than one team or region.
