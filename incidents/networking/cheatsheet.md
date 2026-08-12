# Networking Cheatsheet

## 1. Quick Mental Model

Networking should help you answer two questions quickly: where the control boundary is, and what evidence proves the runtime state matches the intended state.

```text
Input
  │
  └──► Control Boundary ──► Execution Path ──► Dependency ──► Output
                   │
                   └──► Logs / Metrics / Audit
```

## 2. Most Useful Commands

### Command

```bash
pwd
```

**Purpose:**  
Print current directory

**When to use:**  
Confirm execution context

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
The expected path before running a risky command

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `pwd` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
ls -lah /var/log
```

**Purpose:**  
List files with detail

**When to use:**  
Inspect configs, logs, or artifact layout

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Unexpected ownership, size, or missing files

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `ls -lah` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
cd /etc/systemd/system
```

**Purpose:**  
Change directories

**When to use:**  
Move quickly through incident evidence

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Whether the expected config directory exists

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `cd /path` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
cat /etc/resolv.conf
```

**Purpose:**  
Print a file

**When to use:**  
Check small config or status files

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Broken DNS config or stale search domains

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `cat /path/file` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
less /var/log/syslog
```

**Purpose:**  
Page through a file safely

**When to use:**  
Read long logs or configs

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Error bursts around incident time

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `less /path/file` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
tail -n 100 /var/log/nginx/error.log
```

**Purpose:**  
Read the most recent log lines

**When to use:**  
First five minutes of log triage

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Latest failures without opening the whole file

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `tail -n 100 /var/log/file` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
journalctl -u kubelet -n 100
```

**Purpose:**  
Read systemd service logs

**When to use:**  
Inspect daemon failures

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Restart loops, permission errors, or dependency failures

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `journalctl -u service -n 100` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
systemctl status docker
```

**Purpose:**  
Check service health

**When to use:**  
Verify a daemon state and recent logs

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Failed units and restart reasons

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `systemctl status service` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
ps aux | rg python
```

**Purpose:**  
List running processes

**When to use:**  
Find missing or runaway processes

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Zombie, orphan, or duplicate processes

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `ps aux` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
top
```

**Purpose:**  
Live process and CPU view

**When to use:**  
Quick CPU and memory triage

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Load, idle CPU, and top offenders

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `top` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
htop
```

**Purpose:**  
Interactive process view

**When to use:**  
Faster process triage when available

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Thread-level or per-core skew

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `htop` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
free -m
```

**Purpose:**  
Show memory usage

**When to use:**  
Check memory pressure or cache behavior

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Low available memory or swap usage

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `free -m` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git status
```

**Purpose:**  
Show worktree state

**When to use:**  
First command before any git action

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Unstaged changes, branch, conflicts

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git status` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git branch -vv
```

**Purpose:**  
Show local branches and upstreams

**When to use:**  
Confirm branch context

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Detached HEAD or wrong upstream

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git branch -vv` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git log --oneline --graph --decorate -20
```

**Purpose:**  
Compact history view

**When to use:**  
Understand recent branch movement

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Unexpected merges or rebases

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git log --oneline --graph --decorate -20` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git diff
```

**Purpose:**  
Show unstaged changes

**When to use:**  
Review pending edits

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Accidental edits or risky hunks

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git diff` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git diff --staged
```

**Purpose:**  
Show staged changes

**When to use:**  
Check exactly what will commit

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Mismatched staged content

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git diff --staged` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git add -p
```

**Purpose:**  
Stage hunks interactively

**When to use:**  
Curate a clean commit

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Whether unrelated edits are being separated

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git add -p` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git commit -m 'Fix DNS probe'
```

**Purpose:**  
Create a commit

**When to use:**  
Checkpoint clean logical changes

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
A concise history entry

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git commit -m 'msg'` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git restore README.md
```

**Purpose:**  
Discard local unstaged changes

**When to use:**  
Undo mistakes safely

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Only after confirming the file should revert

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git restore file` to narrow the failing boundary quickly and gather evidence before changing configuration.


## 3. Fast Troubleshooting Commands

First 5 minutes:

- `pwd`
- `ls -lah`
- `cd /path`
- `cat /path/file`
- `less /path/file`

## 4. Files and Locations

```text
/etc/hosts
/etc/resolv.conf
/var/log/
/etc/systemd/system/
~/.kube/config
~/.aws/config
~/.azure/
~/.config/gcloud/
```

Use the topic-relevant configuration first, then confirm environment-specific overrides and generated runtime state.

## 5. Useful Tools

`curl`, `jq`, `yq`, `dig`, `openssl`, `tcpdump`, `ss`, `lsof`, `journalctl`

Add provider or platform-specific tools where the topic naturally supports them.

## 6. Network / Ports / Protocols

| Port | Protocol | Purpose | Security concern |
| --- | --- | --- | --- |
| 53 | UDP/TCP | DNS | Misrouting or spoofed answers |
| 80 | TCP | HTTP | Unexpected plaintext exposure |
| 443 | TCP | HTTPS / APIs | TLS policy and certificate drift |
| 6443 | TCP | Kubernetes API | Cluster-admin exposure |
| 5432 | TCP | PostgreSQL | Unintended east-west access |

## 7. Logs

- Query service logs first.
- Check audit logs for auth or policy changes.
- Compare application logs with infrastructure logs around the same timestamp.

## 8. Metrics

- Error rate
- Latency
- Saturation
- Queue depth or backlog
- Capacity headroom
- Deployment or rollout health

## 9. Traces

Where traces apply, verify whether the request reaches the next dependency and whether retries or fan-out patterns changed latency.

## 10. Health Checks

- Readiness or service health endpoints
- CLI status commands
- Dependency reachability probes
- Certificate and DNS validation

## 11. Security Checks

- Confirm caller identity.
- Check effective permissions.
- Inspect secret sources and age.
- Verify TLS chain and endpoint exposure.
- Ensure temporary mitigations do not become permanent widening of access.

## 12. Performance Checks

- CPU, memory, and IO saturation
- Thread or worker exhaustion
- Network retransmits or DNS latency
- Database or queue backlog
- Autoscaling lag

## 13. Cost Checks

- Egress and NAT-like charges
- Idle compute or oversized nodes
- Log volume and retention
- Duplicate storage copies
- High-cardinality metrics

## 14. Keyboard / CLI Shortcuts

- `Ctrl-r` shell history search
- `!!` rerun last command in shells that support it
- `| jq` for readable JSON
- `--watch` or repeated polling where supported

## 15. Common Failure Patterns

- Auth fails → check caller identity first
- DNS resolves wrong target → inspect resolver, zone, or private DNS drift
- Service healthy but users fail → inspect edge, endpoints, or certificates
- Rollout hangs → check quota, probes, config, and events

## 16. Incident Quick Reference

Symptom  
↓  
Confirm identity and target environment  
↓  
Run the smallest command that proves the failing boundary  
↓  
Gather logs, metrics, and config evidence  
↓  
Apply the smallest safe fix  
↓  
Verify recovery and add prevention

## 17. Interview Quick Recall

- Name the control boundary.
- Explain the first evidence-gathering commands.
- Talk about blast radius, rollback, and observability.
- Mention the production shortcut that is dangerous if used blindly.
