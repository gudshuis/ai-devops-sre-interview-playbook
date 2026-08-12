# Kubernetes

**Status: deep first-pass content** (priority section for V1 — see root
[README.md](../README.md)).

## What belongs here

Anything where Kubernetes itself is the subject under test — architecture,
scheduling, resource management, networking, RBAC, GitOps-on-Kubernetes,
multi-cluster/fleet operations, and Kubernetes-specific troubleshooting.
Broader platform-engineering concerns that happen to run *on* Kubernetes
(internal developer platforms, CI/CD runner isolation) live in
[`platform-engineering/`](../platform-engineering/README.md) instead —
check there if a Kubernetes-adjacent topic isn't found here.

## Contents

- [fundamentals.md](fundamentals.md) — 🟢🔵 architecture, core objects,
  scheduling, resource management basics
- [senior-scenarios.md](senior-scenarios.md) — 🟠🔴 multi-cluster fleet
  management, cgroups/OOM deep dives, policy enforcement at scale
- [troubleshooting.md](troubleshooting.md) — real outage investigations
  with `kubectl`/`crictl`/`nsenter`-level debugging

## Debugging toolkit referenced throughout

`kubectl`, `crictl`, `ctr`, `nsenter`, `ip`, `ss`, `tcpdump`, `dig`, `curl`,
`openssl`, `etcdctl` — used in context in the troubleshooting scenarios
rather than listed as an abstract reference; see
[troubleshooting.md](troubleshooting.md) for real usage.
