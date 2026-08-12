# Linux Cheatsheet

## 1. Quick Mental Model

Linux should help you answer two questions quickly: where the control boundary is, and what evidence proves the runtime state matches the intended state.

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
vmstat 1 5
```

**Purpose:**  
Show run queue, IO wait, and memory behavior

**When to use:**  
Distinguish CPU from IO stalls

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
High wa, blocked procs, swap activity

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `vmstat 1 5` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
iostat -xz 1 5
```

**Purpose:**  
Show disk utilization and latency

**When to use:**  
Debug storage saturation

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
High await or 100% util

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `iostat -xz 1 5` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
pidstat -dur 1 5
```

**Purpose:**  
Per-process CPU, memory, IO stats

**When to use:**  
Pinpoint noisy processes

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Who is driving load

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `pidstat 1 5` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
df -h
```

**Purpose:**  
Show filesystem capacity

**When to use:**  
Detect disk-full incidents

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Nearly full mounts or inode pressure

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `df -h` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
du -sh /var/log/*
```

**Purpose:**  
Summarize disk usage

**When to use:**  
Find large directories

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Runaway logs or artifacts

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `du -sh *` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
ss -tulpn
```

**Purpose:**  
List listening sockets

**When to use:**  
Map processes to ports

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Unexpected listeners or missing ports

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `ss -tulpn` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
lsof -i :443
```

**Purpose:**  
Map open files or sockets to processes

**When to use:**  
Find port conflicts

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Which process owns the port

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `lsof -i` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
curl -vk https://api.internal
```

**Purpose:**  
Probe HTTP/TLS endpoints

**When to use:**  
Check app reachability and certificates

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
TLS handshake errors or 5xx

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `curl -vk https://host` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
dig api.example.com
```

**Purpose:**  
Query DNS directly

**When to use:**  
Debug resolution issues

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Wrong answers, NXDOMAIN, or stale TTL

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `dig example.com` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
nslookup api.example.com
```

**Purpose:**  
Simple DNS lookup

**When to use:**  
Quick DNS validation on minimal systems

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Resolver path and basic answer

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `nslookup example.com` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
ping 10.0.0.10
```

**Purpose:**  
ICMP reachability test

**When to use:**  
Confirm basic network path where allowed

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Loss or unreachable errors

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `ping host` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
traceroute api.example.com
```

**Purpose:**  
Show route hops

**When to use:**  
Debug network path asymmetry

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Where the path changes or stops

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `traceroute host` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
tcpdump -i eth0 port 53
```

**Purpose:**  
Capture packets

**When to use:**  
Prove whether traffic is arriving or leaving

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Dropped queries, resets, retransmits

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `tcpdump -i eth0 port 443` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
strace -p 1234
```

**Purpose:**  
Trace syscalls on a live process

**When to use:**  
Find blocked IO or permission denials

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
EACCES, ENOENT, stuck network calls

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `strace -p PID` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
dmesg | tail -n 50
```

**Purpose:**  
Read kernel messages

**When to use:**  
Check OOM kills or device issues

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Kernel-level failures

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `dmesg | tail` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
env | sort | rg AWS
```

**Purpose:**  
Inspect environment variables

**When to use:**  
Confirm runtime config

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Wrong secrets or region settings

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `env | sort` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
find /etc -name '*.conf'
```

**Purpose:**  
Locate files quickly

**When to use:**  
Find configs, logs, or certificates

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Unexpected duplicates

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `find /path -name file` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
chown app:app /data
```

**Purpose:**  
Change permissions and ownership

**When to use:**  
Fix access problems carefully

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Correct service access without over-broad permissions

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `chmod/chown` to narrow the failing boundary quickly and gather evidence before changing configuration.


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
