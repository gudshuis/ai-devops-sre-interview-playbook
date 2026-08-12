# Learning Path: AI Platform Engineer

## Assumed baseline

Solid Kubernetes and platform-engineering fundamentals already. This path
is about layering AI-specific infrastructure and platform concerns on top
of that, not teaching Kubernetes from scratch.

## Recommended order

1. [`platform-engineering/internal-developer-platforms/`](../../platform-engineering/internal-developer-platforms/README.md) —
   golden paths, self-service infra, platform-as-product framing
2. [`ai-engineering/foundations/`](../../ai-engineering/foundations/README.md) —
   just enough model/inference vocabulary to reason about infra decisions
3. [`ai-engineering/ai-infrastructure/`](../../ai-engineering/ai-infrastructure/README.md) —
   GPU scheduling, inference clusters, model serving
4. [`ai-engineering/mcp/`](../../ai-engineering/mcp/README.md) — MCP
   architecture and enterprise gateway design (core of this path)
5. [`ai-engineering/ai-platform-engineering/`](../../ai-engineering/ai-platform-engineering/README.md) —
   the "design an internal AI platform" scenarios
6. [`ai-engineering/ai-security/`](../../ai-engineering/ai-security/README.md) —
   you will be asked about this even in a pure-infra interview
7. [`platform-engineering/finops/`](../../platform-engineering/finops/README.md) —
   GPU/token FinOps specifically

## What interviewers at this level actually probe for

- Can you design a **model/MCP gateway** with real authn/authz, not just
  "put it behind an API gateway"?
- Do you understand the **cost shape** of AI infrastructure (GPU
  utilization, token cost per request) well enough to defend a design
  against a FinOps objection?
- Can you reason about **agent/tool blast radius** — what happens when a
  tool call goes wrong, not just when the model is wrong?
- Do you default to security as a bolt-on, or as part of the platform
  design from the start (identity, least privilege, sandboxing)?

## Priority exercises

- `ai-engineering/mcp/senior-scenarios.md` — enterprise MCP gateway design
- `system-design/case-studies/` — "design an AI platform for 5,000
  engineers" style prompts
- `troubleshooting-labs/` — GPU nodes showing low utilization despite
  queued inference requests; MCP server exposing credentials
