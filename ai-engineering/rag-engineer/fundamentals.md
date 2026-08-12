# RAG Engineer — Fundamentals

---

### Q1. What are the core production primitives behind this role?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know the building blocks well enough to reason about higher-order failures.

**ANSWER:** In rag engineer, one of the core ideas is that **hybrid search** is never only a feature choice. It changes how the system behaves around **ingestion**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **vector databases**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **hybrid search** is only a win if it does not silently worsen **ingestion** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if hybrid search scaled 10x?
- How would you instrument ingestion so you could prove the answer in production?
- When would vector databases be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q2. Why does this role require systems thinking instead of only model or application knowledge?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can connect local mechanisms to end-to-end production outcomes.

**ANSWER:** In rag engineer, one of the core ideas is that **document ACLs** is never only a feature choice. It changes how the system behaves around **chunking**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **embeddings**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **document ACLs** is only a win if it does not silently worsen **chunking** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if document ACLs scaled 10x?
- How would you instrument chunking so you could prove the answer in production?
- When would embeddings be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q3. Which failure modes become common when teams scale this capability too quickly?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand operational maturity problems, not just happy-path mechanics.

**ANSWER:** In rag engineer, one of the core ideas is that **query rewriting** is never only a feature choice. It changes how the system behaves around **embeddings**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **rerankers**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **query rewriting** is only a win if it does not silently worsen **embeddings** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if query rewriting scaled 10x?
- How would you instrument embeddings so you could prove the answer in production?
- When would rerankers be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q4. How should a senior engineer reason about trade-offs in this role?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can balance speed, safety, latency, cost, and ownership.

**ANSWER:** In rag engineer, one of the core ideas is that **index rebuilds** is never only a feature choice. It changes how the system behaves around **vector search**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **object storage**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **index rebuilds** is only a win if it does not silently worsen **vector search** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if index rebuilds scaled 10x?
- How would you instrument vector search so you could prove the answer in production?
- When would object storage be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q5. What production telemetry matters most here?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know how to prove a system is healthy instead of assuming it.

**ANSWER:** In rag engineer, one of the core ideas is that **metadata schema** is never only a feature choice. It changes how the system behaves around **reranking**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **PostgreSQL/pgvector**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **metadata schema** is only a win if it does not silently worsen **reranking** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if metadata schema scaled 10x?
- How would you instrument reranking so you could prove the answer in production?
- When would PostgreSQL/pgvector be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q6. What are the core production primitives behind this role?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know the building blocks well enough to reason about higher-order failures.

**ANSWER:** In rag engineer, one of the core ideas is that **retrieval quality metrics** is never only a feature choice. It changes how the system behaves around **freshness**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Python**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **retrieval quality metrics** is only a win if it does not silently worsen **freshness** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if retrieval quality metrics scaled 10x?
- How would you instrument freshness so you could prove the answer in production?
- When would Python be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q7. Why does this role require systems thinking instead of only model or application knowledge?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can connect local mechanisms to end-to-end production outcomes.

**ANSWER:** In rag engineer, one of the core ideas is that **hybrid search** is never only a feature choice. It changes how the system behaves around **ingestion**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **vector databases**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **hybrid search** is only a win if it does not silently worsen **ingestion** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if hybrid search scaled 10x?
- How would you instrument ingestion so you could prove the answer in production?
- When would vector databases be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q8. Which failure modes become common when teams scale this capability too quickly?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand operational maturity problems, not just happy-path mechanics.

**ANSWER:** In rag engineer, one of the core ideas is that **document ACLs** is never only a feature choice. It changes how the system behaves around **chunking**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **embeddings**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **document ACLs** is only a win if it does not silently worsen **chunking** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if document ACLs scaled 10x?
- How would you instrument chunking so you could prove the answer in production?
- When would embeddings be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q9. How should a senior engineer reason about trade-offs in this role?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can balance speed, safety, latency, cost, and ownership.

**ANSWER:** In rag engineer, one of the core ideas is that **query rewriting** is never only a feature choice. It changes how the system behaves around **embeddings**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **rerankers**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **query rewriting** is only a win if it does not silently worsen **embeddings** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if query rewriting scaled 10x?
- How would you instrument embeddings so you could prove the answer in production?
- When would rerankers be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q10. What production telemetry matters most here?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know how to prove a system is healthy instead of assuming it.

**ANSWER:** In rag engineer, one of the core ideas is that **index rebuilds** is never only a feature choice. It changes how the system behaves around **vector search**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **object storage**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **index rebuilds** is only a win if it does not silently worsen **vector search** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if index rebuilds scaled 10x?
- How would you instrument vector search so you could prove the answer in production?
- When would object storage be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q11. What are the core production primitives behind this role?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know the building blocks well enough to reason about higher-order failures.

**ANSWER:** In rag engineer, one of the core ideas is that **metadata schema** is never only a feature choice. It changes how the system behaves around **reranking**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **PostgreSQL/pgvector**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **metadata schema** is only a win if it does not silently worsen **reranking** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if metadata schema scaled 10x?
- How would you instrument reranking so you could prove the answer in production?
- When would PostgreSQL/pgvector be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q12. Why does this role require systems thinking instead of only model or application knowledge?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can connect local mechanisms to end-to-end production outcomes.

**ANSWER:** In rag engineer, one of the core ideas is that **retrieval quality metrics** is never only a feature choice. It changes how the system behaves around **freshness**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Python**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **retrieval quality metrics** is only a win if it does not silently worsen **freshness** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if retrieval quality metrics scaled 10x?
- How would you instrument freshness so you could prove the answer in production?
- When would Python be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q13. Which failure modes become common when teams scale this capability too quickly?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand operational maturity problems, not just happy-path mechanics.

**ANSWER:** In rag engineer, one of the core ideas is that **hybrid search** is never only a feature choice. It changes how the system behaves around **ingestion**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **vector databases**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **hybrid search** is only a win if it does not silently worsen **ingestion** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if hybrid search scaled 10x?
- How would you instrument ingestion so you could prove the answer in production?
- When would vector databases be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q14. How should a senior engineer reason about trade-offs in this role?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can balance speed, safety, latency, cost, and ownership.

**ANSWER:** In rag engineer, one of the core ideas is that **document ACLs** is never only a feature choice. It changes how the system behaves around **chunking**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **embeddings**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **document ACLs** is only a win if it does not silently worsen **chunking** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if document ACLs scaled 10x?
- How would you instrument chunking so you could prove the answer in production?
- When would embeddings be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q15. What production telemetry matters most here?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know how to prove a system is healthy instead of assuming it.

**ANSWER:** In rag engineer, one of the core ideas is that **query rewriting** is never only a feature choice. It changes how the system behaves around **embeddings**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **rerankers**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **query rewriting** is only a win if it does not silently worsen **embeddings** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if query rewriting scaled 10x?
- How would you instrument embeddings so you could prove the answer in production?
- When would rerankers be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q16. What are the core production primitives behind this role?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know the building blocks well enough to reason about higher-order failures.

**ANSWER:** In rag engineer, one of the core ideas is that **index rebuilds** is never only a feature choice. It changes how the system behaves around **vector search**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **object storage**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **index rebuilds** is only a win if it does not silently worsen **vector search** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if index rebuilds scaled 10x?
- How would you instrument vector search so you could prove the answer in production?
- When would object storage be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q17. Why does this role require systems thinking instead of only model or application knowledge?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can connect local mechanisms to end-to-end production outcomes.

**ANSWER:** In rag engineer, one of the core ideas is that **metadata schema** is never only a feature choice. It changes how the system behaves around **reranking**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **PostgreSQL/pgvector**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **metadata schema** is only a win if it does not silently worsen **reranking** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if metadata schema scaled 10x?
- How would you instrument reranking so you could prove the answer in production?
- When would PostgreSQL/pgvector be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q18. Which failure modes become common when teams scale this capability too quickly?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand operational maturity problems, not just happy-path mechanics.

**ANSWER:** In rag engineer, one of the core ideas is that **retrieval quality metrics** is never only a feature choice. It changes how the system behaves around **freshness**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Python**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **retrieval quality metrics** is only a win if it does not silently worsen **freshness** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if retrieval quality metrics scaled 10x?
- How would you instrument freshness so you could prove the answer in production?
- When would Python be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q19. How should a senior engineer reason about trade-offs in this role?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can balance speed, safety, latency, cost, and ownership.

**ANSWER:** In rag engineer, one of the core ideas is that **hybrid search** is never only a feature choice. It changes how the system behaves around **ingestion**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **vector databases**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **hybrid search** is only a win if it does not silently worsen **ingestion** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if hybrid search scaled 10x?
- How would you instrument ingestion so you could prove the answer in production?
- When would vector databases be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q20. What production telemetry matters most here?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know how to prove a system is healthy instead of assuming it.

**ANSWER:** In rag engineer, one of the core ideas is that **document ACLs** is never only a feature choice. It changes how the system behaves around **chunking**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **embeddings**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **document ACLs** is only a win if it does not silently worsen **chunking** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if document ACLs scaled 10x?
- How would you instrument chunking so you could prove the answer in production?
- When would embeddings be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q21. What are the core production primitives behind this role?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know the building blocks well enough to reason about higher-order failures.

**ANSWER:** In rag engineer, one of the core ideas is that **query rewriting** is never only a feature choice. It changes how the system behaves around **embeddings**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **rerankers**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **query rewriting** is only a win if it does not silently worsen **embeddings** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if query rewriting scaled 10x?
- How would you instrument embeddings so you could prove the answer in production?
- When would rerankers be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q22. Why does this role require systems thinking instead of only model or application knowledge?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can connect local mechanisms to end-to-end production outcomes.

**ANSWER:** In rag engineer, one of the core ideas is that **index rebuilds** is never only a feature choice. It changes how the system behaves around **vector search**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **object storage**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **index rebuilds** is only a win if it does not silently worsen **vector search** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if index rebuilds scaled 10x?
- How would you instrument vector search so you could prove the answer in production?
- When would object storage be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q23. Which failure modes become common when teams scale this capability too quickly?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand operational maturity problems, not just happy-path mechanics.

**ANSWER:** In rag engineer, one of the core ideas is that **metadata schema** is never only a feature choice. It changes how the system behaves around **reranking**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **PostgreSQL/pgvector**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **metadata schema** is only a win if it does not silently worsen **reranking** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if metadata schema scaled 10x?
- How would you instrument reranking so you could prove the answer in production?
- When would PostgreSQL/pgvector be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q24. How should a senior engineer reason about trade-offs in this role?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can balance speed, safety, latency, cost, and ownership.

**ANSWER:** In rag engineer, one of the core ideas is that **retrieval quality metrics** is never only a feature choice. It changes how the system behaves around **freshness**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Python**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **retrieval quality metrics** is only a win if it does not silently worsen **freshness** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if retrieval quality metrics scaled 10x?
- How would you instrument freshness so you could prove the answer in production?
- When would Python be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q25. What production telemetry matters most here?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know how to prove a system is healthy instead of assuming it.

**ANSWER:** In rag engineer, one of the core ideas is that **hybrid search** is never only a feature choice. It changes how the system behaves around **ingestion**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **vector databases**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **hybrid search** is only a win if it does not silently worsen **ingestion** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if hybrid search scaled 10x?
- How would you instrument ingestion so you could prove the answer in production?
- When would vector databases be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
