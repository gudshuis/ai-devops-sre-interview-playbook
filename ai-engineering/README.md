# AI Engineering

**Status: deep first-pass content, priority section for V1** (see root
[README.md](../README.md)).

Everything at the intersection of AI systems and production engineering —
deliberately **not** an ML-academic treatment (no derivations of attention
math). Each subfolder asks: *can you build, operate, secure, and pay for
this in production?*

## Subfolders

- [`foundations/`](foundations/README.md) — just enough model/inference
  vocabulary to reason about the rest (tokens, context windows, inference
  vs. training, quantization, KV cache)
- [`llm/`](llm/README.md) — prompt/context engineering, LLM gateways,
  routing, caching, cost, reliability
- [`rag/`](rag/README.md) — ingestion, chunking, retrieval, reranking,
  advanced RAG patterns, production debugging
- [`vector-databases/`](vector-databases/README.md) — pgvector, Pinecone,
  Qdrant, Weaviate, Milvus; ANN indexing, recall/precision trade-offs
- [`mcp/`](mcp/README.md) — Model Context Protocol architecture and
  security (deep content — priority for V1)
- [`agents-and-agentic-ai/`](agents-and-agentic-ai/README.md) — agent
  loops, memory, multi-agent orchestration, production agentic design
  (deep content — priority for V1)
- [`ai-infrastructure/`](ai-infrastructure/README.md) — GPU scheduling,
  inference clusters, model serving (vLLM, Triton, KServe)
- [`ai-platform-engineering/`](ai-platform-engineering/README.md) —
  designing an internal AI platform end-to-end
- [`ai-security/`](ai-security/README.md) — prompt injection, RAG/vector
  poisoning, MCP-specific threats, agent authorization (first-class
  section, not an afterthought)
- [`llmops-and-mlops/`](llmops-and-mlops/README.md) — model lifecycle,
  registries, canary/shadow deployment, drift
- [`evals/`](evals/README.md) — offline/online evals, LLM-as-judge,
  regression testing for AI systems
- [`context-engineering/`](context-engineering/README.md) — engineering a
  model's entire information environment, not just prompt wording

## Why "AI Engineering" is one parent folder

See [`docs/architecture/README.md`](../docs/architecture/README.md) for the
reasoning — these topics are too interdependent (MCP security touches
agent authorization; RAG evaluation touches evals; context engineering
touches almost everything) to scatter across a flat top-level namespace.

## AI Engineering Career Universe

```text
AI ENGINEERING
│
├── Customer / Solutions
│   ├── Forward-Deployed AI Engineer
│   └── AI Solutions Architect
│
├── Agents
│   ├── Agentic AI Engineer
│   ├── MCP Engineer
│   ├── Agent Platform Engineer
│   └── Context Engineer
│
├── Platform & Infrastructure
│   ├── AI Platform Engineer
│   ├── AI Infrastructure Engineer
│   ├── AI Systems Engineer
│   └── AI Developer Experience Engineer
│
├── Models & Runtime
│   ├── LLMOps Engineer
│   └── Inference Engineer
│
├── Data & Retrieval
│   └── RAG Engineer
│
├── Reliability & Operations
│   ├── AI Reliability Engineer
│   ├── AI Observability Engineer
│   └── AI FinOps Engineer
│
└── Trust
    ├── AI Security Engineer
    ├── AI Evals Engineer
    └── AI Governance Engineer
```

### Role landing pages

- [Forward-Deployed AI Engineer](forward-deployed-ai-engineer/README.md)
- [Agentic AI Engineer](agentic-ai-engineer/README.md)
- [AI Platform Engineer](ai-platform-engineer/README.md)
- [AI Infrastructure Engineer](ai-infrastructure-engineer/README.md)
- [AI Reliability Engineer](ai-reliability-engineer/README.md)
- [MCP Engineer](mcp-engineer/README.md)
- [Agent Platform Engineer](agent-platform-engineer/README.md)
- [LLMOps Engineer](llmops-engineer/README.md)
- [Inference Engineer](inference-engineer/README.md)
- [AI Observability Engineer](ai-observability-engineer/README.md)
- [AI Security Engineer](ai-security-engineer/README.md)
- [AI Evals Engineer](ai-evals-engineer/README.md)
- [AI FinOps Engineer](ai-finops-engineer/README.md)
- [AI Governance Engineer](ai-governance-engineer/README.md)
- [Context Engineer](context-engineer/README.md)
- [RAG Engineer](rag-engineer/README.md)
- [AI Solutions Architect](ai-solutions-architect/README.md)
- [AI Systems Engineer](ai-systems-engineer/README.md)
- [AI Developer Experience Engineer](ai-developer-experience-engineer/README.md)
