# Roadmap

This repository is built in phases. Each phase adds real, complete
content rather than padding toward a target count — see the root
[README.md](README.md) and `scripts/validate-content.py` for why depth is
tracked honestly rather than advertised.

## V1 — Foundation (current)

- Full repository architecture, governance docs, CI, premium README
- `templates/` — the fixed format every content type follows
- Starter content across every domain folder (real, not filler)
- Deep initial content in: Kubernetes, AI engineering (LLM/RAG/MCP/Agentic
  AI, AI Security), and System Design case studies
- First worked examples of the newer content types: `architecture/rag/`
  (3 flows), one `challenges/debug-this/` and one `challenges/design-this/`,
  one `request-journeys/`, two `cheatsheets/`, two `mental-models/`, two
  `tradeoffs/`, one `incidents/` entry
- `scripts/validate-content.py` — real, working content-completeness
  validator, wired into CI
- `docs/repository-governance.md`, `docs/licensing-options.md`

## V2 — Filename standardization + fundamentals depth pass

Cleanup item flagged honestly in the README: several V1 domains have real
content under non-canonical filenames (`questions.md`, `principles.md`,
`rendering-strategy.md` instead of `fundamentals.md`) that
`validate-content.py` doesn't count yet. V2 standardizes every domain onto
the canonical filenames from `templates/`, then begins the push toward the
25+-question target per `fundamentals.md`, starting with Kubernetes and
AI engineering (already the deepest domains, so closest to the target).

## V3 — Troubleshooting + senior-scenarios depth pass

Bring every domain's `troubleshooting.md` and `senior-scenarios.md`
toward the 25+ target, starting with the domains most requested for
interview prep (Kubernetes, AI Security, Platform Engineering).

## V4 — Architecture flows for every major domain

Extend the `architecture/` pattern demonstrated in `architecture/rag/`
(3 flows minimum) to: `kubernetes/`, `platform-engineering/`, `cloud/`,
`sre/`, `ai-platform/`, `mcp/`, `agents/`, `cicd/`, `security/`.

## V5 — Learning-experience layer

- `visuals/` — "how it works" visual explainers (Kubernetes request flow,
  DNS resolution, TLS handshake, container startup, RAG request flow, MCP
  tool call, AI agent loop, LLM inference, incident response)
- `why/` — deep-explanation questions testing understanding over
  memorization (why a Pod can be Running but unavailable, why retries can
  make an outage worse, etc.)
- `toolbox/` — "which debugging tool, when, why" reference material
- More `request-journeys/`, `tradeoffs/`, `mental-models/`, `incidents/`
  entries beyond the V1 starter set

## V6 — Interview-format layer

- `interview-modes/` — 15-minute, 30-minute, 60-minute senior, Staff, and
  Principal interview simulations assembled from existing content
- `question-of-the-day/` — a static, no-backend random-question index
  (GitHub Pages compatible, no server required)
- `INDEX.md`, `QUESTION_INDEX.md`, `ARCHITECTURE_INDEX.md`,
  `TROUBLESHOOTING_INDEX.md` — full searchable indexes, generated from
  repository contents rather than hand-maintained

## V7 — Optional static site

A lightweight, static (no backend) GitHub Pages version of the knowledge
base — searchable, responsive, dark/light theme — **only if** it adds
real value beyond browsing the repository directly on GitHub. The
repository itself must remain fully usable without it.

## V8 — Community question submissions

Revisit the current "not accepting external contributions" policy (see
[CONTRIBUTING.md](CONTRIBUTING.md)) once the repository's own voice,
structure, and quality bar are well-established — not before.

## Out of scope (for now)

- Video content / a companion course
- A hosted/interactive quiz application with a real backend — this
  repository is markdown-first and static-site-first by design
- Certification-style question banks (AWS/Azure/GCP certification prep is
  a different goal from this repository's production-engineering focus)
