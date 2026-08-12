# Learning Path: Platform Engineer

## Assumed baseline

Strong Kubernetes and CI/CD fundamentals from an operational role (DevOps,
SRE, or similar). This path is about the shift from *operating* systems to
*building the platform other engineers use to operate theirs*.

## Recommended order

1. [`kubernetes/`](../../kubernetes/README.md) — especially multi-cluster
   fleet management and policy enforcement (Kyverno/OPA)
2. [`platform-engineering/internal-developer-platforms/`](../../platform-engineering/internal-developer-platforms/README.md) —
   the core of this path: golden paths, developer portals, self-service
3. [`platform-engineering/gitops-and-cicd/`](../../platform-engineering/gitops-and-cicd/README.md) —
   GitOps as a platform primitive, not just a deployment mechanism
4. [`platform-engineering/devsecops-and-cloud-security/`](../../platform-engineering/devsecops-and-cloud-security/README.md) —
   policy-as-code, admission control, secrets as platform features
5. [`platform-engineering/sre/`](../../platform-engineering/sre/README.md) —
   platform SLOs (yes, the platform itself needs SLOs)
6. [`platform-engineering/finops/`](../../platform-engineering/finops/README.md) —
   cost as a platform concern, not an afterthought

## What interviewers at this level actually probe for

- **"When does Platform Engineering become another ticket-based Ops
  team?"** — this is asked more often than you'd expect; have a real
  answer about self-service vs. gatekeeping.
- Can you **measure whether your platform is actually succeeding** —
  adoption, golden-path usage, time-to-first-deploy — not just "it's
  running"?
- Do you design for **multi-tenancy** from the start, or bolt it on later?
- Can you explain a **control plane** design choice (what's centralized vs.
  delegated) and defend the trade-off?

## Priority exercises

- `senior-scenarios/` — cluster lifecycle management across 100+ clusters
- `troubleshooting-labs/` — Argo CD says Synced but the application is
  broken; shared build-agent cluster resource contention
- `system-design/case-studies/` — "design an internal developer platform"
