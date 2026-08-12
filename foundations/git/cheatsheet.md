# Git Cheatsheet

## 1. Quick Mental Model

Git should help you answer two questions quickly: where the control boundary is, and what evidence proves the runtime state matches the intended state.

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

### Command

```bash
git restore --staged app.py
```

**Purpose:**  
Unstage a file

**When to use:**  
Fix staging mistakes

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Clean index without losing working changes

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git restore --staged file` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git stash push -m 'wip kube debug'
```

**Purpose:**  
Temporarily shelve work

**When to use:**  
Switch contexts during incidents

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Whether the worktree is clean enough to continue

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git stash push -m 'msg'` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git stash list
```

**Purpose:**  
List stashes

**When to use:**  
Recover or inspect shelved work

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Find the right stash before applying

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git stash list` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git stash pop
```

**Purpose:**  
Reapply the latest stash

**When to use:**  
Resume paused work

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Conflicts or overlapping edits

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git stash pop` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git fetch --all --prune
```

**Purpose:**  
Refresh remotes

**When to use:**  
Check latest upstream state

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Deleted branches or incoming changes

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git fetch --all --prune` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git rebase origin/main
```

**Purpose:**  
Replay commits on latest main

**When to use:**  
Keep a branch up to date

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Conflicts introduced by drift

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git rebase origin/main` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git merge release/1.2
```

**Purpose:**  
Merge another branch

**When to use:**  
Combine histories without rebasing

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Conflict surface and merge commit

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git merge branch` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git cherry-pick abc1234
```

**Purpose:**  
Apply one commit elsewhere

**When to use:**  
Backport or hotfix

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Conflict risk or missing dependency

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git cherry-pick SHA` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git reset --soft HEAD~1
```

**Purpose:**  
Move HEAD but keep changes staged

**When to use:**  
Rewrite the last local commit safely

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Useful before recommitting better history

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git reset --soft HEAD~1` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git revert abc1234
```

**Purpose:**  
Create an inverse commit

**When to use:**  
Undo bad changes on shared history

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Safe rollback path

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git revert SHA` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git bisect start
```

**Purpose:**  
Begin binary search for a bad commit

**When to use:**  
Find regressions efficiently

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Structured regression isolation

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git bisect start` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git blame server.py
```

**Purpose:**  
Show line authorship

**When to use:**  
Trace context on a specific line

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Who changed the risky code and when

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git blame file` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git show abc1234
```

**Purpose:**  
Inspect one commit

**When to use:**  
Review exact patch details

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Hidden migrations, config, or generated files

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git show SHA` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git remote -v
```

**Purpose:**  
List remotes

**When to use:**  
Check push/fetch destinations

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Wrong origin or fork confusion

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git remote -v` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git tag
```

**Purpose:**  
List tags

**When to use:**  
Inspect releases and cut points

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Release mapping

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git tag` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git clean -nd
```

**Purpose:**  
Preview untracked file cleanup

**When to use:**  
See generated junk before deletion

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
What would be removed

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git clean -nd` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
git worktree list
```

**Purpose:**  
Show linked worktrees

**When to use:**  
Manage parallel contexts safely

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Unexpected extra checkout state

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `git worktree list` to narrow the failing boundary quickly and gather evidence before changing configuration.


## 3. Fast Troubleshooting Commands

First 5 minutes:

- `git status`
- `git branch -vv`
- `git log --oneline --graph --decorate -20`
- `git diff`
- `git diff --staged`

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
| 22 | TCP | SSH Git remote | Key exposure or weak host verification |
| 443 | TCP | HTTPS Git remote | Token leakage or proxy interception |

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
