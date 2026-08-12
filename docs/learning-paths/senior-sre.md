# Learning Path: Senior SRE

## Assumed baseline

Comfortable with Linux fundamentals, basic networking, and has operated at
least one production service. This path does not re-teach what a process
or a TCP handshake is.

## Recommended order

1. [`foundations/linux/`](../../foundations/linux/README.md) — cgroups,
   OOM behavior, systemd (skim if already strong here)
2. [`foundations/networking/`](../../foundations/networking/README.md) —
   DNS/TCP/TLS troubleshooting fundamentals
3. [`kubernetes/`](../../kubernetes/README.md) — full read-through,
   especially scheduling, resource management, and multi-cluster scenarios
4. [`platform-engineering/sre/`](../../platform-engineering/sre/README.md) —
   SLI/SLO design, error budgets, burn-rate alerting (core of this path)
5. [`platform-engineering/observability/`](../../platform-engineering/observability/README.md) —
   golden signals, cardinality, distributed tracing
6. [`troubleshooting-labs/`](../../troubleshooting-labs/README.md) — work
   every Kubernetes and networking scenario before checking the answer
7. [`system-design/case-studies/`](../../system-design/case-studies/README.md) —
   focus on "design an observability platform" / reliability-heavy case
   studies

## What interviewers at this level actually probe for

- Can you **design an SLI that measures what users actually experience**,
  not just what's easy to instrument?
- Do you reach for an error budget / burn-rate framing, or just "watch the
  dashboards and page on everything"?
- Can you reason about **blast radius** before proposing a fix, not just
  after an outage?
- Do you distinguish symptom from root cause under time pressure?

## Priority exercises

- `senior-scenarios/` — the multi-cluster, multi-cloud reliability
  scenarios are the closest simulation of a senior SRE panel round
- `troubleshooting-labs/` — Kubernetes OOMKilled, DNS-works-in-one-namespace,
  Prometheus cardinality explosion, Kafka consumer lag
