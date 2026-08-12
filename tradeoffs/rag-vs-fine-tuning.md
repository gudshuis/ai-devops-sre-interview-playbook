# RAG vs. Fine-Tuning

## What each actually changes

- **RAG**: the model's weights are untouched — you're changing what
  *context* it sees at inference time, retrieved fresh per query.
- **Fine-tuning**: you're changing the model's *weights* themselves,
  training it further on domain-specific data.

## When RAG is the right choice

- The knowledge changes frequently (product docs, policy that updates
  monthly) — RAG's corpus can be updated by re-indexing; fine-tuning
  would need retraining for every update.
- You need **citability/grounding** — RAG can point at which retrieved
  document supported an answer; a fine-tuned model's knowledge is baked
  in with no clean way to attribute a specific claim to a specific source.
- You need to serve genuinely different knowledge to different users
  (per-user document access, per the authorization pattern in
  [`architecture/rag/enterprise-rag.md`](../architecture/rag/enterprise-rag.md))
  — a single fine-tuned model can't easily vary its "knowledge" per
  request the way retrieval can.

## When fine-tuning is the right choice

- The need is about **behavior/style/format**, not knowledge — teaching a
  model to consistently respond in a specific structured format, tone, or
  reasoning pattern is a fine-tuning problem, not a retrieval problem;
  stuffing "always respond in this format" into every prompt via RAG-style
  context is a weaker, more brittle substitute.
- Latency/cost sensitivity is extreme and the domain is stable enough that
  baking knowledge into weights (no retrieval round-trip at inference
  time) is worth the upfront training cost.
- The task requires reasoning patterns specific to a narrow domain that
  general instruction-following combined with retrieved context doesn't
  reliably produce.

## The honest answer for most production systems

**Most systems needing "make the model know about our stuff" want RAG,
not fine-tuning** — the update-frequency and citability requirements
above apply to the large majority of real enterprise use cases. Fine-tuning
gets reached for prematurely fairly often, when the actual requirement
(knowledge injection) is better served by RAG, and the two aren't
mutually exclusive — a fine-tuned model *for behavior/format* combined
with RAG *for knowledge* is a legitimate, increasingly common combination,
not an either/or choice in practice.

## Interview framing

If asked "would you use RAG or fine-tuning for X," the strong answer names
which of the two problems (knowledge vs. behavior) X actually is, rather
than picking a side generically.
