# RAG Engineer

**Ground models with trustworthy retrieval, not optimistic assumptions.**

## What this role is

Build retrieval systems that feed models relevant, fresh, authorized context instead of forcing them to hallucinate.

## Why this role exists

This role exists because retrieval quality often determines whether an AI system is trustworthy, yet retrieval design is an engineering discipline of its own.

## Where it sits in modern engineering organisations

Usually supports AI product, agent, and platform teams with ingestion, indexing, retrieval quality, and freshness architecture.

## Role responsibilities

- Design ingestion, chunking, metadata, embedding, and retrieval flows.
- Choose vector, hybrid, or reranking approaches based on workload trade-offs.
- Protect document security and freshness across the retrieval pipeline.
- Measure retrieval quality and debug bad grounding behavior.
- Scale indexing and search pipelines reliably in production.

## Required skill stack

- retrieval design
- chunking
- metadata modeling
- vector search
- hybrid search
- evaluation
- pipeline operations

## Technologies commonly involved

vector databases, embeddings, rerankers, object storage, PostgreSQL/pgvector, Python

## Role boundaries

- Not just 'put docs in a vector DB'.
- Owns the data and retrieval path more than the model path itself.
- Must think about permissions and freshness as first-class requirements.

## Relationship to DevOps / SRE / Platform / Cloud engineering

- Works closely with context engineers, evals, and AI security.
- Provides grounded context to agents and LLM applications.

## Typical production architecture

```text
source docs
  │
  ▼
ingestion
  │
  ▼
chunking
  │
  ▼
embedding
  │
  ▼
index
  │
  ▼
retrieval
  │
  ▼
rerank
  │
  ▼
citations
```

## Learning roadmap

```text
RAG basics
      ↓
ingestion and chunking
      ↓
search and reranking
      ↓
evaluation
      ↓
security and freshness
      ↓
enterprise architecture
```

## Beginner → Senior → Staff progression

- **Beginner:** learns the core workflow, tools, and failure vocabulary.
- **Senior:** designs safer systems, debugs incidents systematically, and explains trade-offs clearly.
- **Staff / Principal:** defines platform patterns, governance boundaries, reliability targets, and cross-team operating models.

## Interview focus areas

- ingestion
- chunking
- embeddings
- vector search
- reranking

## Practical learning path

1. Learn the mechanisms in `fundamentals.md`.
2. Pressure-test your understanding with `questions.md`.
3. Practice incident thinking in `troubleshooting.md`.
4. Move into trade-off reasoning in `senior-scenarios.md`.
5. Use `challenges.md` and `cheatsheet.md` as hands-on companions.

## Directory navigation

- [fundamentals.md](fundamentals.md)
- [questions.md](questions.md)
- [troubleshooting.md](troubleshooting.md)
- [senior-scenarios.md](senior-scenarios.md)
- [challenges.md](challenges.md)
- [cheatsheet.md](cheatsheet.md)
- [architecture/01-basic-flow.md](architecture/01-basic-flow.md)
- [architecture/02-production-flow.md](architecture/02-production-flow.md)
- [architecture/03-enterprise-flow.md](architecture/03-enterprise-flow.md)

## Cross-links

- See also: [Context Engineer](../context-engineer/README.md)
- See also: [AI Evals Engineer](../ai-evals-engineer/README.md)
- See also: [AI Security Engineer](../ai-security-engineer/README.md)

## Q&A

        ### Q1. Why would a company invest in this role instead of asking a general software or DevOps engineer to absorb the work?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether the candidate understands the distinct production complexity behind the role.

**ANSWER:** Because the role exists at a failure boundary where generic engineering knowledge stops being enough.

**SENIOR-LEVEL ANSWER:** The senior framing is that specialization here is not about prestige, it is about ownership of new operational risk. For this role, that usually shows up around **ingestion** and **hybrid search**.

**FOLLOW-UP QUESTIONS:**
- How does this role intersect with DevOps and SRE? for RAG Engineer specifically?
- What anti-pattern appears when nobody explicitly owns this concern? for RAG Engineer specifically?

**RED FLAGS:** Answering with marketing language instead of concrete engineering boundaries.

---
### Q2. What are the most important responsibilities of this role in a production organization?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can distinguish core ownership from adjacent responsibilities.

**ANSWER:** The role is responsible for design ingestion, chunking, metadata, embedding, and retrieval flows. and related operating concerns.

**SENIOR-LEVEL ANSWER:** A senior engineer would emphasize not just building systems, but making them governable, observable, and supportable under production pressure in rag engineer domains. For this role, that usually shows up around **chunking** and **document ACLs**.

**FOLLOW-UP QUESTIONS:**
- Which responsibilities should stay with platform or security teams? for RAG Engineer specifically?
- Where does this role most often get pulled into incident response? for RAG Engineer specifically?

**RED FLAGS:** Listing technologies without explaining operational ownership.

---
### Q3. How does this role relate to DevOps, SRE, platform engineering, and cloud engineering?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can place the role inside a broader engineering organization.

**ANSWER:** It overlaps with works closely with context engineers, evals, and ai security.

**SENIOR-LEVEL ANSWER:** The senior answer is to describe the control boundaries clearly: what this role inherits from existing disciplines and what new AI-specific complexity it adds. For this role, that usually shows up around **embeddings** and **query rewriting**.

**FOLLOW-UP QUESTIONS:**
- Where does this role create new interfaces with security or FinOps? for RAG Engineer specifically?
- What should remain centralized versus team-local? for RAG Engineer specifically?

**RED FLAGS:** Pretending the role is completely separate from existing engineering disciplines.

---
### Q4. What skill stack should a senior engineer in this role have?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand that seniority here is about systems thinking plus execution, not just tool familiarity.

**ANSWER:** A senior engineer should combine retrieval design, chunking, metadata modeling, vector search, then layer on the rest through production repetition.

**SENIOR-LEVEL ANSWER:** The best answer ties each skill to a failure mode: identity and networking failures, rollout failures, retrieval failures, GPU contention, or cost explosions depending on the role. For this role, that usually shows up around **vector search** and **index rebuilds**.

**FOLLOW-UP QUESTIONS:**
- Which skills are foundational versus role-specific? for RAG Engineer specifically?
- How would you onboard an engineer transitioning into this role? for RAG Engineer specifically?

**RED FLAGS:** Giving a shopping list of buzzwords with no prioritization.

---
### Q5. Where does this role sit in a modern engineering organization?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can explain the role in organizational terms, not only technical terms.

**ANSWER:** Usually supports AI product, agent, and platform teams with ingestion, indexing, retrieval quality, and freshness architecture.

**SENIOR-LEVEL ANSWER:** The senior framing is to explain why the role must collaborate across product, platform, security, and operations rather than acting as an isolated specialty. For this role, that usually shows up around **reranking** and **metadata schema**.

**FOLLOW-UP QUESTIONS:**
- Which teams are the closest day-to-day partners? for RAG Engineer specifically?
- What tension usually appears around ownership? for RAG Engineer specifically?

**RED FLAGS:** Treating the role as if it only works alone.

---
### Q6. Why would a company invest in this role instead of asking a general software or DevOps engineer to absorb the work?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether the candidate understands the distinct production complexity behind the role.

**ANSWER:** Because the role exists at a failure boundary where generic engineering knowledge stops being enough.

**SENIOR-LEVEL ANSWER:** The senior framing is that specialization here is not about prestige, it is about ownership of new operational risk. For this role, that usually shows up around **freshness** and **retrieval quality metrics**.

**FOLLOW-UP QUESTIONS:**
- How does this role intersect with DevOps and SRE? for RAG Engineer specifically?
- What anti-pattern appears when nobody explicitly owns this concern? for RAG Engineer specifically?

**RED FLAGS:** Answering with marketing language instead of concrete engineering boundaries.

---
### Q7. What are the most important responsibilities of this role in a production organization?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can distinguish core ownership from adjacent responsibilities.

**ANSWER:** The role is responsible for design ingestion, chunking, metadata, embedding, and retrieval flows. and related operating concerns.

**SENIOR-LEVEL ANSWER:** A senior engineer would emphasize not just building systems, but making them governable, observable, and supportable under production pressure in rag engineer domains. For this role, that usually shows up around **ingestion** and **hybrid search**.

**FOLLOW-UP QUESTIONS:**
- Which responsibilities should stay with platform or security teams? for RAG Engineer specifically?
- Where does this role most often get pulled into incident response? for RAG Engineer specifically?

**RED FLAGS:** Listing technologies without explaining operational ownership.

---
### Q8. How does this role relate to DevOps, SRE, platform engineering, and cloud engineering?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can place the role inside a broader engineering organization.

**ANSWER:** It overlaps with works closely with context engineers, evals, and ai security.

**SENIOR-LEVEL ANSWER:** The senior answer is to describe the control boundaries clearly: what this role inherits from existing disciplines and what new AI-specific complexity it adds. For this role, that usually shows up around **chunking** and **document ACLs**.

**FOLLOW-UP QUESTIONS:**
- Where does this role create new interfaces with security or FinOps? for RAG Engineer specifically?
- What should remain centralized versus team-local? for RAG Engineer specifically?

**RED FLAGS:** Pretending the role is completely separate from existing engineering disciplines.

---
### Q9. What skill stack should a senior engineer in this role have?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand that seniority here is about systems thinking plus execution, not just tool familiarity.

**ANSWER:** A senior engineer should combine retrieval design, chunking, metadata modeling, vector search, then layer on the rest through production repetition.

**SENIOR-LEVEL ANSWER:** The best answer ties each skill to a failure mode: identity and networking failures, rollout failures, retrieval failures, GPU contention, or cost explosions depending on the role. For this role, that usually shows up around **embeddings** and **query rewriting**.

**FOLLOW-UP QUESTIONS:**
- Which skills are foundational versus role-specific? for RAG Engineer specifically?
- How would you onboard an engineer transitioning into this role? for RAG Engineer specifically?

**RED FLAGS:** Giving a shopping list of buzzwords with no prioritization.

---
### Q10. Where does this role sit in a modern engineering organization?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can explain the role in organizational terms, not only technical terms.

**ANSWER:** Usually supports AI product, agent, and platform teams with ingestion, indexing, retrieval quality, and freshness architecture.

**SENIOR-LEVEL ANSWER:** The senior framing is to explain why the role must collaborate across product, platform, security, and operations rather than acting as an isolated specialty. For this role, that usually shows up around **vector search** and **index rebuilds**.

**FOLLOW-UP QUESTIONS:**
- Which teams are the closest day-to-day partners? for RAG Engineer specifically?
- What tension usually appears around ownership? for RAG Engineer specifically?

**RED FLAGS:** Treating the role as if it only works alone.

---
### Q11. Why would a company invest in this role instead of asking a general software or DevOps engineer to absorb the work?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether the candidate understands the distinct production complexity behind the role.

**ANSWER:** Because the role exists at a failure boundary where generic engineering knowledge stops being enough.

**SENIOR-LEVEL ANSWER:** The senior framing is that specialization here is not about prestige, it is about ownership of new operational risk. For this role, that usually shows up around **reranking** and **metadata schema**.

**FOLLOW-UP QUESTIONS:**
- How does this role intersect with DevOps and SRE? for RAG Engineer specifically?
- What anti-pattern appears when nobody explicitly owns this concern? for RAG Engineer specifically?

**RED FLAGS:** Answering with marketing language instead of concrete engineering boundaries.

---
### Q12. What are the most important responsibilities of this role in a production organization?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can distinguish core ownership from adjacent responsibilities.

**ANSWER:** The role is responsible for design ingestion, chunking, metadata, embedding, and retrieval flows. and related operating concerns.

**SENIOR-LEVEL ANSWER:** A senior engineer would emphasize not just building systems, but making them governable, observable, and supportable under production pressure in rag engineer domains. For this role, that usually shows up around **freshness** and **retrieval quality metrics**.

**FOLLOW-UP QUESTIONS:**
- Which responsibilities should stay with platform or security teams? for RAG Engineer specifically?
- Where does this role most often get pulled into incident response? for RAG Engineer specifically?

**RED FLAGS:** Listing technologies without explaining operational ownership.

---
### Q13. How does this role relate to DevOps, SRE, platform engineering, and cloud engineering?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can place the role inside a broader engineering organization.

**ANSWER:** It overlaps with works closely with context engineers, evals, and ai security.

**SENIOR-LEVEL ANSWER:** The senior answer is to describe the control boundaries clearly: what this role inherits from existing disciplines and what new AI-specific complexity it adds. For this role, that usually shows up around **ingestion** and **hybrid search**.

**FOLLOW-UP QUESTIONS:**
- Where does this role create new interfaces with security or FinOps? for RAG Engineer specifically?
- What should remain centralized versus team-local? for RAG Engineer specifically?

**RED FLAGS:** Pretending the role is completely separate from existing engineering disciplines.

---
### Q14. What skill stack should a senior engineer in this role have?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand that seniority here is about systems thinking plus execution, not just tool familiarity.

**ANSWER:** A senior engineer should combine retrieval design, chunking, metadata modeling, vector search, then layer on the rest through production repetition.

**SENIOR-LEVEL ANSWER:** The best answer ties each skill to a failure mode: identity and networking failures, rollout failures, retrieval failures, GPU contention, or cost explosions depending on the role. For this role, that usually shows up around **chunking** and **document ACLs**.

**FOLLOW-UP QUESTIONS:**
- Which skills are foundational versus role-specific? for RAG Engineer specifically?
- How would you onboard an engineer transitioning into this role? for RAG Engineer specifically?

**RED FLAGS:** Giving a shopping list of buzzwords with no prioritization.

---
### Q15. Where does this role sit in a modern engineering organization?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can explain the role in organizational terms, not only technical terms.

**ANSWER:** Usually supports AI product, agent, and platform teams with ingestion, indexing, retrieval quality, and freshness architecture.

**SENIOR-LEVEL ANSWER:** The senior framing is to explain why the role must collaborate across product, platform, security, and operations rather than acting as an isolated specialty. For this role, that usually shows up around **embeddings** and **query rewriting**.

**FOLLOW-UP QUESTIONS:**
- Which teams are the closest day-to-day partners? for RAG Engineer specifically?
- What tension usually appears around ownership? for RAG Engineer specifically?

**RED FLAGS:** Treating the role as if it only works alone.

---
### Q16. Why would a company invest in this role instead of asking a general software or DevOps engineer to absorb the work?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether the candidate understands the distinct production complexity behind the role.

**ANSWER:** Because the role exists at a failure boundary where generic engineering knowledge stops being enough.

**SENIOR-LEVEL ANSWER:** The senior framing is that specialization here is not about prestige, it is about ownership of new operational risk. For this role, that usually shows up around **vector search** and **index rebuilds**.

**FOLLOW-UP QUESTIONS:**
- How does this role intersect with DevOps and SRE? for RAG Engineer specifically?
- What anti-pattern appears when nobody explicitly owns this concern? for RAG Engineer specifically?

**RED FLAGS:** Answering with marketing language instead of concrete engineering boundaries.

---
### Q17. What are the most important responsibilities of this role in a production organization?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can distinguish core ownership from adjacent responsibilities.

**ANSWER:** The role is responsible for design ingestion, chunking, metadata, embedding, and retrieval flows. and related operating concerns.

**SENIOR-LEVEL ANSWER:** A senior engineer would emphasize not just building systems, but making them governable, observable, and supportable under production pressure in rag engineer domains. For this role, that usually shows up around **reranking** and **metadata schema**.

**FOLLOW-UP QUESTIONS:**
- Which responsibilities should stay with platform or security teams? for RAG Engineer specifically?
- Where does this role most often get pulled into incident response? for RAG Engineer specifically?

**RED FLAGS:** Listing technologies without explaining operational ownership.

---
### Q18. How does this role relate to DevOps, SRE, platform engineering, and cloud engineering?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can place the role inside a broader engineering organization.

**ANSWER:** It overlaps with works closely with context engineers, evals, and ai security.

**SENIOR-LEVEL ANSWER:** The senior answer is to describe the control boundaries clearly: what this role inherits from existing disciplines and what new AI-specific complexity it adds. For this role, that usually shows up around **freshness** and **retrieval quality metrics**.

**FOLLOW-UP QUESTIONS:**
- Where does this role create new interfaces with security or FinOps? for RAG Engineer specifically?
- What should remain centralized versus team-local? for RAG Engineer specifically?

**RED FLAGS:** Pretending the role is completely separate from existing engineering disciplines.

---
### Q19. What skill stack should a senior engineer in this role have?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand that seniority here is about systems thinking plus execution, not just tool familiarity.

**ANSWER:** A senior engineer should combine retrieval design, chunking, metadata modeling, vector search, then layer on the rest through production repetition.

**SENIOR-LEVEL ANSWER:** The best answer ties each skill to a failure mode: identity and networking failures, rollout failures, retrieval failures, GPU contention, or cost explosions depending on the role. For this role, that usually shows up around **ingestion** and **hybrid search**.

**FOLLOW-UP QUESTIONS:**
- Which skills are foundational versus role-specific? for RAG Engineer specifically?
- How would you onboard an engineer transitioning into this role? for RAG Engineer specifically?

**RED FLAGS:** Giving a shopping list of buzzwords with no prioritization.

---
### Q20. Where does this role sit in a modern engineering organization?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can explain the role in organizational terms, not only technical terms.

**ANSWER:** Usually supports AI product, agent, and platform teams with ingestion, indexing, retrieval quality, and freshness architecture.

**SENIOR-LEVEL ANSWER:** The senior framing is to explain why the role must collaborate across product, platform, security, and operations rather than acting as an isolated specialty. For this role, that usually shows up around **chunking** and **document ACLs**.

**FOLLOW-UP QUESTIONS:**
- Which teams are the closest day-to-day partners? for RAG Engineer specifically?
- What tension usually appears around ownership? for RAG Engineer specifically?

**RED FLAGS:** Treating the role as if it only works alone.

---
### Q21. Why would a company invest in this role instead of asking a general software or DevOps engineer to absorb the work?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether the candidate understands the distinct production complexity behind the role.

**ANSWER:** Because the role exists at a failure boundary where generic engineering knowledge stops being enough.

**SENIOR-LEVEL ANSWER:** The senior framing is that specialization here is not about prestige, it is about ownership of new operational risk. For this role, that usually shows up around **embeddings** and **query rewriting**.

**FOLLOW-UP QUESTIONS:**
- How does this role intersect with DevOps and SRE? for RAG Engineer specifically?
- What anti-pattern appears when nobody explicitly owns this concern? for RAG Engineer specifically?

**RED FLAGS:** Answering with marketing language instead of concrete engineering boundaries.

---
### Q22. What are the most important responsibilities of this role in a production organization?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can distinguish core ownership from adjacent responsibilities.

**ANSWER:** The role is responsible for design ingestion, chunking, metadata, embedding, and retrieval flows. and related operating concerns.

**SENIOR-LEVEL ANSWER:** A senior engineer would emphasize not just building systems, but making them governable, observable, and supportable under production pressure in rag engineer domains. For this role, that usually shows up around **vector search** and **index rebuilds**.

**FOLLOW-UP QUESTIONS:**
- Which responsibilities should stay with platform or security teams? for RAG Engineer specifically?
- Where does this role most often get pulled into incident response? for RAG Engineer specifically?

**RED FLAGS:** Listing technologies without explaining operational ownership.

---
### Q23. How does this role relate to DevOps, SRE, platform engineering, and cloud engineering?

**DIFFICULTY:** 🟠 Senior
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can place the role inside a broader engineering organization.

**ANSWER:** It overlaps with works closely with context engineers, evals, and ai security.

**SENIOR-LEVEL ANSWER:** The senior answer is to describe the control boundaries clearly: what this role inherits from existing disciplines and what new AI-specific complexity it adds. For this role, that usually shows up around **reranking** and **metadata schema**.

**FOLLOW-UP QUESTIONS:**
- Where does this role create new interfaces with security or FinOps? for RAG Engineer specifically?
- What should remain centralized versus team-local? for RAG Engineer specifically?

**RED FLAGS:** Pretending the role is completely separate from existing engineering disciplines.

---
### Q24. What skill stack should a senior engineer in this role have?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand that seniority here is about systems thinking plus execution, not just tool familiarity.

**ANSWER:** A senior engineer should combine retrieval design, chunking, metadata modeling, vector search, then layer on the rest through production repetition.

**SENIOR-LEVEL ANSWER:** The best answer ties each skill to a failure mode: identity and networking failures, rollout failures, retrieval failures, GPU contention, or cost explosions depending on the role. For this role, that usually shows up around **freshness** and **retrieval quality metrics**.

**FOLLOW-UP QUESTIONS:**
- Which skills are foundational versus role-specific? for RAG Engineer specifically?
- How would you onboard an engineer transitioning into this role? for RAG Engineer specifically?

**RED FLAGS:** Giving a shopping list of buzzwords with no prioritization.

---
### Q25. Where does this role sit in a modern engineering organization?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** RAG Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can explain the role in organizational terms, not only technical terms.

**ANSWER:** Usually supports AI product, agent, and platform teams with ingestion, indexing, retrieval quality, and freshness architecture.

**SENIOR-LEVEL ANSWER:** The senior framing is to explain why the role must collaborate across product, platform, security, and operations rather than acting as an isolated specialty. For this role, that usually shows up around **ingestion** and **hybrid search**.

**FOLLOW-UP QUESTIONS:**
- Which teams are the closest day-to-day partners? for RAG Engineer specifically?
- What tension usually appears around ownership? for RAG Engineer specifically?

**RED FLAGS:** Treating the role as if it only works alone.

---
