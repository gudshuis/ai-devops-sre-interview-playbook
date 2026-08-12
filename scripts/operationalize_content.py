#!/usr/bin/env python3
"""Upgrade cheatsheets, challenges, troubleshooting, and senior scenarios repo-wide."""
from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

TOPIC_DIRS = []
for filename in ("cheatsheet.md", "challenges.md", "troubleshooting.md", "senior-scenarios.md"):
    for path in REPO_ROOT.rglob(filename):
        TOPIC_DIRS.append(path.parent)
TOPIC_DIRS = sorted(set(TOPIC_DIRS))


def pretty_name(path: Path) -> str:
    text = path.relative_to(REPO_ROOT).as_posix().split("/")[-1].replace("-", " ").title()
    return text.replace("Ai", "AI").replace("Mcp", "MCP").replace("Llm", "LLM").replace("Rag", "RAG").replace("Sre", "SRE").replace("Cicd", "CI/CD")


def topic_type(path: Path) -> str:
    parts = path.relative_to(REPO_ROOT).parts
    joined = "/".join(parts)
    if "aws" in parts:
        return "aws"
    if "azure" in parts:
        return "azure"
    if "gcp" in parts:
        return "gcp"
    if "kubernetes" in parts:
        return "kubernetes"
    if "linux" in parts:
        return "linux"
    if "git" in parts:
        return "git"
    if "containers" in parts:
        return "docker"
    if "networking" in parts:
        return "networking"
    if "mcp" in parts:
        return "mcp"
    if "rag" in parts:
        return "rag"
    if "llm" in parts and "llmops" not in joined:
        return "llm"
    if "ai-infrastructure" in joined:
        return "ai-infra"
    if "observability" in parts:
        return "observability"
    if "database" in joined or "databases" in parts or "vector-databases" in parts:
        return "databases"
    if "gitops" in joined or "cicd" in joined:
        return "cicd"
    return "generic"


COMMANDS = {
    "linux": [
        ("pwd", "Print current directory", "Confirm execution context", "", "pwd", "The expected path before running a risky command"),
        ("ls -lah", "List files with detail", "Inspect configs, logs, or artifact layout", "", "ls -lah /var/log", "Unexpected ownership, size, or missing files"),
        ("cd /path", "Change directories", "Move quickly through incident evidence", "", "cd /etc/systemd/system", "Whether the expected config directory exists"),
        ("cat /path/file", "Print a file", "Check small config or status files", "", "cat /etc/resolv.conf", "Broken DNS config or stale search domains"),
        ("less /path/file", "Page through a file safely", "Read long logs or configs", "", "less /var/log/syslog", "Error bursts around incident time"),
        ("tail -n 100 /var/log/file", "Read the most recent log lines", "First five minutes of log triage", "", "tail -n 100 /var/log/nginx/error.log", "Latest failures without opening the whole file"),
        ("journalctl -u service -n 100", "Read systemd service logs", "Inspect daemon failures", "", "journalctl -u kubelet -n 100", "Restart loops, permission errors, or dependency failures"),
        ("systemctl status service", "Check service health", "Verify a daemon state and recent logs", "", "systemctl status docker", "Failed units and restart reasons"),
        ("ps aux", "List running processes", "Find missing or runaway processes", "", "ps aux | rg python", "Zombie, orphan, or duplicate processes"),
        ("top", "Live process and CPU view", "Quick CPU and memory triage", "", "top", "Load, idle CPU, and top offenders"),
        ("htop", "Interactive process view", "Faster process triage when available", "", "htop", "Thread-level or per-core skew"),
        ("free -m", "Show memory usage", "Check memory pressure or cache behavior", "", "free -m", "Low available memory or swap usage"),
        ("vmstat 1 5", "Show run queue, IO wait, and memory behavior", "Distinguish CPU from IO stalls", "", "vmstat 1 5", "High wa, blocked procs, swap activity"),
        ("iostat -xz 1 5", "Show disk utilization and latency", "Debug storage saturation", "", "iostat -xz 1 5", "High await or 100% util"),
        ("pidstat 1 5", "Per-process CPU, memory, IO stats", "Pinpoint noisy processes", "", "pidstat -dur 1 5", "Who is driving load"),
        ("df -h", "Show filesystem capacity", "Detect disk-full incidents", "", "df -h", "Nearly full mounts or inode pressure"),
        ("du -sh *", "Summarize disk usage", "Find large directories", "", "du -sh /var/log/*", "Runaway logs or artifacts"),
        ("ss -tulpn", "List listening sockets", "Map processes to ports", "", "ss -tulpn", "Unexpected listeners or missing ports"),
        ("lsof -i", "Map open files or sockets to processes", "Find port conflicts", "", "lsof -i :443", "Which process owns the port"),
        ("curl -vk https://host", "Probe HTTP/TLS endpoints", "Check app reachability and certificates", "", "curl -vk https://api.internal", "TLS handshake errors or 5xx"),
        ("dig example.com", "Query DNS directly", "Debug resolution issues", "", "dig api.example.com", "Wrong answers, NXDOMAIN, or stale TTL"),
        ("nslookup example.com", "Simple DNS lookup", "Quick DNS validation on minimal systems", "", "nslookup api.example.com", "Resolver path and basic answer"),
        ("ping host", "ICMP reachability test", "Confirm basic network path where allowed", "", "ping 10.0.0.10", "Loss or unreachable errors"),
        ("traceroute host", "Show route hops", "Debug network path asymmetry", "", "traceroute api.example.com", "Where the path changes or stops"),
        ("tcpdump -i eth0 port 443", "Capture packets", "Prove whether traffic is arriving or leaving", "", "tcpdump -i eth0 port 53", "Dropped queries, resets, retransmits"),
        ("strace -p PID", "Trace syscalls on a live process", "Find blocked IO or permission denials", "", "strace -p 1234", "EACCES, ENOENT, stuck network calls"),
        ("dmesg | tail", "Read kernel messages", "Check OOM kills or device issues", "", "dmesg | tail -n 50", "Kernel-level failures"),
        ("env | sort", "Inspect environment variables", "Confirm runtime config", "", "env | sort | rg AWS", "Wrong secrets or region settings"),
        ("find /path -name file", "Locate files quickly", "Find configs, logs, or certificates", "", "find /etc -name '*.conf'", "Unexpected duplicates"),
        ("chmod/chown", "Change permissions and ownership", "Fix access problems carefully", "", "chown app:app /data", "Correct service access without over-broad permissions"),
    ],
    "git": [
        ("git status", "Show worktree state", "First command before any git action", "", "git status", "Unstaged changes, branch, conflicts"),
        ("git branch -vv", "Show local branches and upstreams", "Confirm branch context", "", "git branch -vv", "Detached HEAD or wrong upstream"),
        ("git log --oneline --graph --decorate -20", "Compact history view", "Understand recent branch movement", "", "git log --oneline --graph --decorate -20", "Unexpected merges or rebases"),
        ("git diff", "Show unstaged changes", "Review pending edits", "", "git diff", "Accidental edits or risky hunks"),
        ("git diff --staged", "Show staged changes", "Check exactly what will commit", "", "git diff --staged", "Mismatched staged content"),
        ("git add -p", "Stage hunks interactively", "Curate a clean commit", "", "git add -p", "Whether unrelated edits are being separated"),
        ("git commit -m 'msg'", "Create a commit", "Checkpoint clean logical changes", "", "git commit -m 'Fix DNS probe'" , "A concise history entry"),
        ("git restore file", "Discard local unstaged changes", "Undo mistakes safely", "", "git restore README.md", "Only after confirming the file should revert"),
        ("git restore --staged file", "Unstage a file", "Fix staging mistakes", "", "git restore --staged app.py", "Clean index without losing working changes"),
        ("git stash push -m 'msg'", "Temporarily shelve work", "Switch contexts during incidents", "", "git stash push -m 'wip kube debug'", "Whether the worktree is clean enough to continue"),
        ("git stash list", "List stashes", "Recover or inspect shelved work", "", "git stash list", "Find the right stash before applying"),
        ("git stash pop", "Reapply the latest stash", "Resume paused work", "", "git stash pop", "Conflicts or overlapping edits"),
        ("git fetch --all --prune", "Refresh remotes", "Check latest upstream state", "", "git fetch --all --prune", "Deleted branches or incoming changes"),
        ("git rebase origin/main", "Replay commits on latest main", "Keep a branch up to date", "", "git rebase origin/main", "Conflicts introduced by drift"),
        ("git merge branch", "Merge another branch", "Combine histories without rebasing", "", "git merge release/1.2", "Conflict surface and merge commit"),
        ("git cherry-pick SHA", "Apply one commit elsewhere", "Backport or hotfix", "", "git cherry-pick abc1234", "Conflict risk or missing dependency"),
        ("git reset --soft HEAD~1", "Move HEAD but keep changes staged", "Rewrite the last local commit safely", "", "git reset --soft HEAD~1", "Useful before recommitting better history"),
        ("git revert SHA", "Create an inverse commit", "Undo bad changes on shared history", "", "git revert abc1234", "Safe rollback path"),
        ("git bisect start", "Begin binary search for a bad commit", "Find regressions efficiently", "", "git bisect start", "Structured regression isolation"),
        ("git blame file", "Show line authorship", "Trace context on a specific line", "", "git blame server.py", "Who changed the risky code and when"),
        ("git show SHA", "Inspect one commit", "Review exact patch details", "", "git show abc1234", "Hidden migrations, config, or generated files"),
        ("git remote -v", "List remotes", "Check push/fetch destinations", "", "git remote -v", "Wrong origin or fork confusion"),
        ("git tag", "List tags", "Inspect releases and cut points", "", "git tag", "Release mapping"),
        ("git clean -nd", "Preview untracked file cleanup", "See generated junk before deletion", "", "git clean -nd", "What would be removed"),
        ("git worktree list", "Show linked worktrees", "Manage parallel contexts safely", "", "git worktree list", "Unexpected extra checkout state"),
    ],
    "kubernetes": [
        ("kubectl config get-contexts", "List kube contexts", "Verify the cluster before acting", "", "kubectl config get-contexts", "Wrong cluster is the first incident risk"),
        ("kubectl config use-context prod", "Switch kube context", "Move to the intended cluster", "", "kubectl config use-context prod", "Confirm after switch"),
        ("kubectl get ns", "List namespaces", "Understand tenant layout", "", "kubectl get ns", "Missing or terminating namespaces"),
        ("kubectl get pods -A -o wide", "List pods with node placement", "Check workload spread and failures", "", "kubectl get pods -A -o wide", "CrashLoop, Pending, skew"),
        ("kubectl describe pod POD", "Detailed pod state", "Explain scheduling or runtime failures", "", "kubectl describe pod api-123 -n prod", "Events, probes, image pull errors"),
        ("kubectl logs POD --previous", "Read previous container logs", "Catch crash loops", "", "kubectl logs api-123 -n prod --previous", "Startup exceptions"),
        ("kubectl exec -it POD -- sh", "Enter a running container", "Debug live container state", "", "kubectl exec -it api-123 -n prod -- sh", "DNS, env vars, mounted files"),
        ("kubectl top pod -A", "Pod resource usage", "Check CPU/memory pressure", "", "kubectl top pod -A", "Hot pods or memory leaks"),
        ("kubectl top node", "Node resource usage", "Detect node saturation", "", "kubectl top node", "High pressure or imbalance"),
        ("kubectl get deploy,sts,ds -A", "Workload summary", "See rollout and controller health", "", "kubectl get deploy,sts,ds -A", "Unavailable replicas"),
        ("kubectl rollout status deploy/name", "Watch rollout progress", "Validate deployments safely", "", "kubectl rollout status deploy/api -n prod", "Stuck or degraded rollout"),
        ("kubectl rollout undo deploy/name", "Rollback a deployment", "Restore last known good state", "", "kubectl rollout undo deploy/api -n prod", "Fast mitigation"),
        ("kubectl get svc -A", "List services", "Inspect exposure model", "", "kubectl get svc -A", "Wrong ports or ClusterIP state"),
        ("kubectl get endpoints,endpointslices -A", "Backend endpoint mapping", "Debug service to pod wiring", "", "kubectl get endpoints,endpointslices -A", "Empty endpoints cause 503s"),
        ("kubectl get ingress -A", "List ingresses", "Check external routing", "", "kubectl get ingress -A", "Address assignment and host rules"),
        ("kubectl describe ingress NAME", "Ingress detail", "Investigate 4xx/5xx at the edge", "", "kubectl describe ingress app -n prod", "Annotation mismatches, backend refs"),
        ("kubectl get events -A --sort-by=.lastTimestamp", "Recent cluster events", "Timeline investigation", "", "kubectl get events -A --sort-by=.lastTimestamp", "Scheduling, pull, or volume failures"),
        ("kubectl get nodes -o wide", "Node inventory", "Check node readiness and versions", "", "kubectl get nodes -o wide", "NotReady nodes, version skew"),
        ("kubectl describe node NODE", "Detailed node state", "Debug taints, pressure, kubelet issues", "", "kubectl describe node ip-10-0-0-1", "Conditions and allocatable resources"),
        ("kubectl cordon NODE", "Mark node unschedulable", "Contain failures", "", "kubectl cordon node-1", "Protect cluster during remediation"),
        ("kubectl drain NODE --ignore-daemonsets", "Evict workloads safely", "Maintenance or bad node handling", "", "kubectl drain node-1 --ignore-daemonsets", "Pod disruption blockers"),
        ("kubectl uncordon NODE", "Return node to service", "Post-maintenance recovery", "", "kubectl uncordon node-1", "Capacity restored"),
        ("kubectl get pvc,pv -A", "Storage attachment view", "Debug pending or stuck volumes", "", "kubectl get pvc,pv -A", "Unbound claims"),
        ("kubectl describe pvc NAME", "Detailed claim state", "Explain storage provisioning failures", "", "kubectl describe pvc data -n prod", "StorageClass, events"),
        ("kubectl get netpol -A", "List network policies", "Check traffic restrictions", "", "kubectl get netpol -A", "Unexpected deny boundaries"),
        ("kubectl auth can-i ACTION RESOURCE", "Check RBAC authorization", "Debug access issues", "", "kubectl auth can-i get secrets -n prod", "Whether RBAC is the blocker"),
        ("helm list -A", "List Helm releases", "Map workloads to release ownership", "", "helm list -A", "Failed or pending upgrades"),
        ("helm get values RELEASE -n NS", "Inspect deployed values", "Debug chart config drift", "", "helm get values ingress-nginx -n ingress", "Wrong configuration inputs"),
        ("kubectl diff -f file.yaml", "Preview manifest changes", "Safer deploy review", "", "kubectl diff -f deploy.yaml", "Risk before apply"),
        ("kubectl apply -f file.yaml", "Apply manifests", "Deploy or patch resources", "", "kubectl apply -f deploy.yaml", "Created vs configured output"),
        ("kubectl delete pod POD", "Force pod recreation", "Recover from stuck state when safe", "", "kubectl delete pod api-123 -n prod", "Controller should recreate it"),
        ("crictl ps", "Container runtime inventory", "Node-level runtime debugging", "", "crictl ps", "Container exists even if kube state is stale"),
        ("ctr -n k8s.io containers ls", "Containerd inventory", "Deep runtime inspection", "", "ctr -n k8s.io containers ls", "Lower-level runtime truth"),
        ("nsenter -t PID -n ss -tulpn", "Enter namespaces for node-level checks", "Debug host network from container context", "", "nsenter -t 1 -n ss -tulpn", "Host-level listeners and ports"),
        ("dig service.ns.svc.cluster.local", "Query cluster DNS", "Debug service resolution", "", "dig kube-dns.kube-system.svc.cluster.local", "DNS response or timeout"),
        ("openssl s_client -connect host:443", "Inspect TLS handshake", "Debug ingress or mTLS", "", "openssl s_client -connect app.example.com:443", "Cert chain, SNI issues"),
        ("tcpdump -i any port 53", "Packet capture on nodes", "Prove DNS path", "", "tcpdump -i any port 53", "Dropped queries or wrong destination"),
        ("kubectl api-resources", "List API kinds", "Check CRDs and resource availability", "", "kubectl api-resources", "Missing CRDs during deploys"),
        ("kubectl get apiservices", "Extension API health", "Debug aggregated API issues", "", "kubectl get apiservices", "Unavailable extension services"),
        ("kubectl get componentstatuses", "Legacy control-plane quick check", "Very rough control-plane glance on older clusters", "", "kubectl get componentstatuses", "Not authoritative, but hints"),
    ],
}


def commands_for(kind: str) -> list[tuple[str, str, str, str, str, str]]:
    base = COMMANDS.get(kind)
    if base:
        return base
    return COMMANDS["linux"][:12] + COMMANDS["git"][:8]


def flow_for(kind: str, title: str) -> str:
    if kind == "kubernetes":
        return """```text
┌──────────────────┐
│      Client      │
└────────┬─────────┘
         ↓
┌──────────────────┐
│   DNS / Edge     │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Ingress / LB     │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Service / Policy │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Pod / Container  │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Dependency Layer │
└──────────────────┘
```"""
    if kind in {"aws", "azure", "gcp"}:
        return """```text
Client
  │
  └──► Identity ──► Network Path ──► Edge / Load Balancer ──► Compute ──► Data
                                                │
                                                └──► Logs / Metrics / Audit
```"""
    if kind in {"rag", "llm", "mcp", "ai-infra"}:
        return """```text
User
  │
  └──► Prompt / Request ──► Orchestrator ──► Retrieval / Tool / Model ──► Response
                                 │
                                 └──► Logs / Metrics / Traces / Cost
```"""
    return f"""```text
Input
  │
  └──► Control Boundary ──► Execution Path ──► Dependency ──► Output
                   │
                   └──► Logs / Metrics / Audit
```"""


def write(path: Path, content: str) -> None:
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def render_cheatsheet(path: Path) -> str:
    kind = topic_type(path)
    title = pretty_name(path)
    commands = commands_for(kind)
    first_five = commands[:5]
    cmd_sections = []
    for cmd, purpose, when, flags, example, look in commands:
        cmd_sections.append(
            f"""### Command

```bash
{example}
```

**Purpose:**  
{purpose}

**When to use:**  
{when}

**Important flags:**  
{flags or "Use default flags first; add filters or output flags to narrow evidence."}

**What to look for:**  
{look}

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `{cmd}` to narrow the failing boundary quickly and gather evidence before changing configuration.

"""
        )
    files = """```text
/etc/hosts
/etc/resolv.conf
/var/log/
/etc/systemd/system/
~/.kube/config
~/.aws/config
~/.azure/
~/.config/gcloud/
```"""
    quick = "\n".join([f"- `{c[0]}`" for c in first_five])
    tools = "`curl`, `jq`, `yq`, `dig`, `openssl`, `tcpdump`, `ss`, `lsof`, `journalctl`"
    ports = """| Port | Protocol | Purpose | Security concern |
| --- | --- | --- | --- |
| 53 | UDP/TCP | DNS | Misrouting or spoofed answers |
| 80 | TCP | HTTP | Unexpected plaintext exposure |
| 443 | TCP | HTTPS / APIs | TLS policy and certificate drift |
| 6443 | TCP | Kubernetes API | Cluster-admin exposure |
| 5432 | TCP | PostgreSQL | Unintended east-west access |"""
    if kind == "git":
        ports = "| Port | Protocol | Purpose | Security concern |\n| --- | --- | --- | --- |\n| 22 | TCP | SSH Git remote | Key exposure or weak host verification |\n| 443 | TCP | HTTPS Git remote | Token leakage or proxy interception |"
    return f"""# {title} Cheatsheet

## 1. Quick Mental Model

{title} should help you answer two questions quickly: where the control boundary is, and what evidence proves the runtime state matches the intended state.

{flow_for(kind, title)}

## 2. Most Useful Commands

{''.join(cmd_sections)}
## 3. Fast Troubleshooting Commands

First 5 minutes:

{quick}

## 4. Files and Locations

{files}

Use the topic-relevant configuration first, then confirm environment-specific overrides and generated runtime state.

## 5. Useful Tools

{tools}

Add provider or platform-specific tools where the topic naturally supports them.

## 6. Network / Ports / Protocols

{ports}

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
"""


def render_challenges(path: Path) -> str:
    title = pretty_name(path)
    kind = topic_type(path)
    cmds = [c[4] for c in commands_for(kind)[:8]]
    blocks = []
    for idx in range(1, 26):
        diff = "Beginner" if idx <= 5 else "Intermediate" if idx <= 10 else "Senior" if idx <= 20 else "Staff" if idx <= 23 else "Principal"
        blocks.append(
            f"""## Challenge {idx:02d} — {title} practical investigation {idx}

**Difficulty:** {diff}

**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Platform Engineer

### Environment

```text
Ubuntu 24.04
Standard engineering shell access
Topic-specific tooling configured
Operational telemetry available
```

### Scenario

You have been handed a live {title.lower()} problem with incomplete context, recent changes, and pressure to restore service without guessing.

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

{", ".join([f"`{cmd.split()[0]}`" for cmd in cmds])}

### Hints

- Start from the symptom, not the architecture diagram.
- Separate auth, network, control-plane, and application problems.
- Prefer commands that reduce uncertainty fastest.

### Solution

The complete solution should verify context first, inspect the authoritative control plane, confirm the runtime state, and then apply the smallest safe corrective action instead of a broad permission or network bypass.

### Commands

```bash
{cmds[0]}
{cmds[1]}
{cmds[2]}
{cmds[3]}
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

"""
        )
    return f"# {title} Challenges\n\n{''.join(blocks)}"


def render_troubleshooting(path: Path) -> str:
    title = pretty_name(path)
    kind = topic_type(path)
    blocks = []
    for idx in range(1, 26):
        diff = "Intermediate" if idx <= 8 else "Advanced" if idx <= 18 else "Senior"
        blocks.append(
            f"""## Scenario {idx:02d} — {title} outage pattern {idx}

**Difficulty:** {diff}
**Roles:** DevOps Engineer / SRE / Platform Engineer / Cloud Engineer / AI Infrastructure Engineer

### Architecture / request flow

{flow_for(kind, title)}

### Situation

A production path involving {title.lower()} is failing and the on-call engineer must narrow the issue quickly with real evidence.

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
{commands_for(kind)[0][4]}
{commands_for(kind)[1][4]}
{commands_for(kind)[2][4]}
{commands_for(kind)[3][4]}
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

"""
        )
    return f"# {title} Troubleshooting\n\n{''.join(blocks)}"


def render_senior(path: Path) -> str:
    title = pretty_name(path)
    kind = topic_type(path)
    blocks = []
    for idx in range(1, 26):
        diff = "Senior" if idx <= 10 else "Staff" if idx <= 20 else "Principal"
        blocks.append(
            f"""## Scenario {idx:02d} — {title} platform-scale scenario {idx}

**Difficulty:** {diff}

### Architecture / engineering flow

{flow_for(kind, title)}

### Situation

The organization is outgrowing its current {title.lower()} operating model and needs a design that works across teams, incidents, compliance, and scale.

### Candidate should clarify

- Which teams and workloads are in scope?
- Is the driver reliability, security, cost, migration, or growth?
- What recovery, residency, and compliance constraints already exist?

### Functional requirements

Support current delivery needs, self-service workflows, and a migration path that avoids a rewrite-first strategy.

### Non-functional requirements

Reliability, auditability, security, observability, platform usability, and controlled cost growth.

### Architecture

Define the control-plane boundaries, execution path, dependency model, and the shared services that should become platform defaults.

### Request/data flow

Explain how a request or deployment path moves through identity, policy, network, execution, and data boundaries and where operators observe or intervene.

### Components

- Identity and policy layer
- Network or routing layer
- Execution platform
- Data dependencies
- Observability and audit
- Automation and delivery workflow

### Scaling strategy

Explain how the design survives more teams, more tenants, more regions, or more traffic without forcing a rebuild.

### Reliability

Describe HA, failover assumptions, dependency isolation, and recovery validation.

### Security boundaries

Call out the hard isolation layers and the places where teams are most tempted to weaken them.

### Observability

Identify the default dashboards, alerts, traces, and audit events needed to operate this safely.

### Failure scenarios

- Dependency outage
- Identity drift
- Route or DNS drift
- Quota or capacity exhaustion
- Broken deployment automation

### Cost

Discuss steady-state cost, disaster-recovery cost, observability cost, and the platform tax of standardization.

### Trade-offs

The right answer balances safety, team velocity, and migration risk. Over-centralization can be as harmful as no standards.

### Senior-level answer

A strong senior answer sequences the work: reduce blast radius, standardize interfaces, add automation, then optimize cost and developer experience.

### Staff / Principal extension

A staff or principal answer adds organization design, platform-product strategy, adoption mechanics, and explicit governance for multi-team scale.

### Follow-up questions

- What would you centralize first?
- What should remain team-owned?
- How would you prove the new model is better before full rollout?

"""
        )
    return f"# {title} Senior Scenarios\n\n{''.join(blocks)}"


def main() -> None:
    for topic_dir in TOPIC_DIRS:
        for name, renderer in {
            "cheatsheet.md": render_cheatsheet,
            "challenges.md": render_challenges,
            "troubleshooting.md": render_troubleshooting,
            "senior-scenarios.md": render_senior,
        }.items():
            path = topic_dir / name
            if path.exists():
                write(path, renderer(topic_dir))


if __name__ == "__main__":
    main()
