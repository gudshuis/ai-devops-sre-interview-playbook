# Hints

Only open this if you're stuck — try your own design first.

- What's the actual difference between "self-service ingestion" and
  "self-service *and* correctly authorized ingestion"? Where does
  authorization metadata need to be captured, and by whom?
- Look at [`architecture/rag/enterprise-rag.md`](../../../architecture/rag/enterprise-rag.md)
  for the retrieval-time-authorization pattern — this problem is that
  same pattern, scaled to many independent document owners instead of one.
- Look at [`system-design/case-studies/design-an-internal-developer-platform.md`](../../../system-design/case-studies/design-an-internal-developer-platform.md)
  for the "golden path" pattern applied to a different kind of
  self-service platform — the same "standardized template + escape hatch"
  tension applies here.
- Consider: does every team need their own vector index, or can they
  share one with metadata-based filtering? What are the trade-offs of
  each?
