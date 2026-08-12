# System Design

**Status: deep first-pass content** (priority section for V1).

## What belongs here

Open-ended architecture exercises, split by focus area. Domain-specific
deep dives (Kubernetes internals, MCP architecture) live in their own
top-level folders — this section is about **composing** systems from
those building blocks under real constraints (scale, cost, failure modes),
not re-teaching any single technology.

## Contents

- [case-studies/](case-studies/README.md) — fully worked designs
  (requirements → architecture → trade-offs → failure modes → follow-ups)
- [backend/](backend/README.md) — backend-focused design principles and
  exercises
- [frontend/](frontend/README.md) — frontend-specific system design
  (rendering strategy, edge/CDN, real-time UI, frontend performance)

## How every case study is structured

Per the root README's format, each case study covers: Requirements, Scale
estimates, High-level architecture (with a Mermaid diagram), Data model,
APIs, Networking, Security, Reliability, Observability, Scaling, Cost,
Failure modes, Trade-offs, and Follow-up questions. Use these as practice
material by attempting your own design **before** reading the worked
answer — see `docs/interview-strategy/` for how to get the most out of
that practice.
