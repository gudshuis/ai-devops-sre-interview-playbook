# Requirements

**Functional:**
- Any team can onboard a new document source (ingest, chunk, embed,
  index) without building their own retrieval infrastructure.
- Per-document, per-user authorization — a user querying the platform
  should only ever retrieve content they're actually authorized to see,
  regardless of which team's documents happen to be relevant.
- Support both a shared/general-purpose query interface and
  team-specific applications built on top of the platform.

**Non-functional:**
- 40 teams onboarding independently shouldn't require central-team
  bottlenecking on every single ingestion.
- Query latency acceptable for an interactive chat-style interface.
- Cost attribution per team (who's actually driving platform cost).

**Explicitly out of scope for this exercise:** the LLM generation step
itself (assume an existing LLM gateway is available) — focus on the
retrieval/RAG-specific architecture.
