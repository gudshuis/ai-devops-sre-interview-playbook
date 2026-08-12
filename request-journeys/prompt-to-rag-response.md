# What Happens When You Ask an Enterprise RAG Assistant a Question?

The full path, from keystroke to answer, through the enterprise RAG
architecture in [`architecture/rag/enterprise-rag.md`](../architecture/rag/enterprise-rag.md).

```text
User types a question
  ↓
Frontend (streaming UI, per system-design/frontend/rendering-strategy.md)
  ↓
API Gateway — authentication
  ↓
RAG Orchestrator
  ↓
Query Rewriter (may expand/reformulate the question)
  ↓
Embedding service (question → vector)
  ↓
Retriever queries Vector DB
  ↓
Policy Engine filters results to only what THIS user is authorized to see
  ↓
Reranker reorders authorized candidates by relevance
  ↓
Context Builder assembles final prompt (question + top reranked chunks)
  ↓
LLM Gateway routes to an appropriate model
  ↓
Model streams tokens back
  ↓
API Gateway streams tokens to Frontend
  ↓
User sees the answer appear incrementally
```

## At each boundary, ask

- **Did the request arrive?** (network/auth failure would show here)
- **Did it leave with the right shape?** (malformed query, empty
  embedding, etc.)
- **How long did this step take?** (TTFT and total latency both matter
  differently here — see `ai-engineering/llm/questions.md`)
- **Was authorization actually enforced, or just assumed?** (the single
  most important check in this entire journey — see
  `architecture/rag/enterprise-rag.md`'s security section)
- **What would a user actually observe if this step failed?**

## Where it can go wrong, mapped to existing content

- Wrong chunk retrieved, or retrieved chunk poorly positioned in context →
  [`ai-engineering/rag/questions.md`](../ai-engineering/rag/questions.md)
- Unauthorized content retrieved before the policy filter (never let this
  reach the LLM) → [`architecture/rag/enterprise-rag.md`](../architecture/rag/enterprise-rag.md)
- Slow perceived response despite fast total generation → TTFT discussion
  in [`ai-engineering/llm/questions.md`](../ai-engineering/llm/questions.md)
- Model manipulated by injected instructions in retrieved content →
  [`ai-engineering/ai-security/fundamentals.md`](../ai-engineering/ai-security/fundamentals.md)

## Interview framing

A strong senior/staff answer to "walk me through what happens when a user
asks your RAG system a question" is exactly this — a boundary-by-boundary
trace, with a named failure mode and its owning subsystem at each step,
not just "it retrieves stuff and the LLM answers."
