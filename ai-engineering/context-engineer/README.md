# Context Engineer

**Engineer what the model sees, not just what it says.**

## What this role is

Engineer the information environment around a model so it sees the right context, in the right form, at the right cost.

## Why this role exists

This role exists because prompt quality depends less on wording alone than on retrieval, memory, ranking, token budgeting, and state assembly across a system.

## Where it sits in modern engineering organisations

Often overlaps with RAG, agent, and LLM engineering. This role becomes distinct in teams where context quality directly affects correctness, latency, or cost.

## Role responsibilities

- Design context assembly pipelines for prompts, retrieval, memory, and tool outputs.
- Control token budgets and compression strategies deliberately.
- Prevent stale, irrelevant, or poisoned context from reaching models.
- Measure the effect of context changes on quality and latency.
- Debug context-window failures and long-running conversational drift.

## Required skill stack

- prompt architecture
- retrieval design
- ranking
- summarization
- token budgeting
- state design
- evaluation

## Technologies commonly involved

LLMs, RAG pipelines, vector databases, Redis, Python, OpenTelemetry

## Role boundaries

- Not just prompt writing.
- Owns context quality and structure, not only the final prompt text.
- Must balance relevance against latency and cost.

## Relationship to DevOps / SRE / Platform / Cloud engineering

- Strongly overlaps with RAG and agentic AI engineering.
- Acts as the context-system counterpart to model and runtime engineering.

## Typical production architecture

```text
inputs
  │
  ▼
ranking
  │
  ▼
memory
  │
  ▼
compression
  │
  ▼
prompt assembly
  │
  ▼
token budget
  │
  ▼
telemetry
```

## Learning roadmap

```text
prompt basics
      ↓
retrieval and ranking
      ↓
memory and summarization
      ↓
token economics
      ↓
quality measurement
      ↓
advanced context architectures
```

## Beginner → Senior → Staff progression

- **Beginner:** learns the core workflow, tools, and failure vocabulary.
- **Senior:** designs safer systems, debugs incidents systematically, and explains trade-offs clearly.
- **Staff / Principal:** defines platform patterns, governance boundaries, reliability targets, and cross-team operating models.

## Interview focus areas

- context windows
- compression
- memory
- ranking
- token budgets

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

- See also: [RAG Engineer](../rag-engineer/README.md)
- See also: [Agentic AI Engineer](../agentic-ai-engineer/README.md)
- See also: [LLMOps Engineer](../llmops-engineer/README.md)

## Q&A

        ### Q1. Why would a company invest in this role instead of asking a general software or DevOps engineer to absorb the work?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether the candidate understands the distinct production complexity behind the role.

**ANSWER:** Because the role exists at a failure boundary where generic engineering knowledge stops being enough.

**SENIOR-LEVEL ANSWER:** The senior framing is that specialization here is not about prestige, it is about ownership of new operational risk. For this role, that usually shows up around **context windows** and **state summarization**.

**FOLLOW-UP QUESTIONS:**
- How does this role intersect with DevOps and SRE? for Context Engineer specifically?
- What anti-pattern appears when nobody explicitly owns this concern? for Context Engineer specifically?

**RED FLAGS:** Answering with marketing language instead of concrete engineering boundaries.

---
### Q2. What are the most important responsibilities of this role in a production organization?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can distinguish core ownership from adjacent responsibilities.

**ANSWER:** The role is responsible for design context assembly pipelines for prompts, retrieval, memory, and tool outputs. and related operating concerns.

**SENIOR-LEVEL ANSWER:** A senior engineer would emphasize not just building systems, but making them governable, observable, and supportable under production pressure in context engineer domains. For this role, that usually shows up around **compression** and **tool-output compaction**.

**FOLLOW-UP QUESTIONS:**
- Which responsibilities should stay with platform or security teams? for Context Engineer specifically?
- Where does this role most often get pulled into incident response? for Context Engineer specifically?

**RED FLAGS:** Listing technologies without explaining operational ownership.

---
### Q3. How does this role relate to DevOps, SRE, platform engineering, and cloud engineering?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can place the role inside a broader engineering organization.

**ANSWER:** It overlaps with strongly overlaps with rag and agentic ai engineering.

**SENIOR-LEVEL ANSWER:** The senior answer is to describe the control boundaries clearly: what this role inherits from existing disciplines and what new AI-specific complexity it adds. For this role, that usually shows up around **memory** and **freshness scoring**.

**FOLLOW-UP QUESTIONS:**
- Where does this role create new interfaces with security or FinOps? for Context Engineer specifically?
- What should remain centralized versus team-local? for Context Engineer specifically?

**RED FLAGS:** Pretending the role is completely separate from existing engineering disciplines.

---
### Q4. What skill stack should a senior engineer in this role have?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand that seniority here is about systems thinking plus execution, not just tool familiarity.

**ANSWER:** A senior engineer should combine prompt architecture, retrieval design, ranking, summarization, then layer on the rest through production repetition.

**SENIOR-LEVEL ANSWER:** The best answer ties each skill to a failure mode: identity and networking failures, rollout failures, retrieval failures, GPU contention, or cost explosions depending on the role. For this role, that usually shows up around **ranking** and **context cache design**.

**FOLLOW-UP QUESTIONS:**
- Which skills are foundational versus role-specific? for Context Engineer specifically?
- How would you onboard an engineer transitioning into this role? for Context Engineer specifically?

**RED FLAGS:** Giving a shopping list of buzzwords with no prioritization.

---
### Q5. Where does this role sit in a modern engineering organization?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can explain the role in organizational terms, not only technical terms.

**ANSWER:** Often overlaps with RAG, agent, and LLM engineering. This role becomes distinct in teams where context quality directly affects correctness, latency, or cost.

**SENIOR-LEVEL ANSWER:** The senior framing is to explain why the role must collaborate across product, platform, security, and operations rather than acting as an isolated specialty. For this role, that usually shows up around **token budgets** and **context truncation**.

**FOLLOW-UP QUESTIONS:**
- Which teams are the closest day-to-day partners? for Context Engineer specifically?
- What tension usually appears around ownership? for Context Engineer specifically?

**RED FLAGS:** Treating the role as if it only works alone.

---
### Q6. Why would a company invest in this role instead of asking a general software or DevOps engineer to absorb the work?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether the candidate understands the distinct production complexity behind the role.

**ANSWER:** Because the role exists at a failure boundary where generic engineering knowledge stops being enough.

**SENIOR-LEVEL ANSWER:** The senior framing is that specialization here is not about prestige, it is about ownership of new operational risk. For this role, that usually shows up around **context poisoning** and **conversation drift**.

**FOLLOW-UP QUESTIONS:**
- How does this role intersect with DevOps and SRE? for Context Engineer specifically?
- What anti-pattern appears when nobody explicitly owns this concern? for Context Engineer specifically?

**RED FLAGS:** Answering with marketing language instead of concrete engineering boundaries.

---
### Q7. What are the most important responsibilities of this role in a production organization?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can distinguish core ownership from adjacent responsibilities.

**ANSWER:** The role is responsible for design context assembly pipelines for prompts, retrieval, memory, and tool outputs. and related operating concerns.

**SENIOR-LEVEL ANSWER:** A senior engineer would emphasize not just building systems, but making them governable, observable, and supportable under production pressure in context engineer domains. For this role, that usually shows up around **context windows** and **state summarization**.

**FOLLOW-UP QUESTIONS:**
- Which responsibilities should stay with platform or security teams? for Context Engineer specifically?
- Where does this role most often get pulled into incident response? for Context Engineer specifically?

**RED FLAGS:** Listing technologies without explaining operational ownership.

---
### Q8. How does this role relate to DevOps, SRE, platform engineering, and cloud engineering?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can place the role inside a broader engineering organization.

**ANSWER:** It overlaps with strongly overlaps with rag and agentic ai engineering.

**SENIOR-LEVEL ANSWER:** The senior answer is to describe the control boundaries clearly: what this role inherits from existing disciplines and what new AI-specific complexity it adds. For this role, that usually shows up around **compression** and **tool-output compaction**.

**FOLLOW-UP QUESTIONS:**
- Where does this role create new interfaces with security or FinOps? for Context Engineer specifically?
- What should remain centralized versus team-local? for Context Engineer specifically?

**RED FLAGS:** Pretending the role is completely separate from existing engineering disciplines.

---
### Q9. What skill stack should a senior engineer in this role have?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand that seniority here is about systems thinking plus execution, not just tool familiarity.

**ANSWER:** A senior engineer should combine prompt architecture, retrieval design, ranking, summarization, then layer on the rest through production repetition.

**SENIOR-LEVEL ANSWER:** The best answer ties each skill to a failure mode: identity and networking failures, rollout failures, retrieval failures, GPU contention, or cost explosions depending on the role. For this role, that usually shows up around **memory** and **freshness scoring**.

**FOLLOW-UP QUESTIONS:**
- Which skills are foundational versus role-specific? for Context Engineer specifically?
- How would you onboard an engineer transitioning into this role? for Context Engineer specifically?

**RED FLAGS:** Giving a shopping list of buzzwords with no prioritization.

---
### Q10. Where does this role sit in a modern engineering organization?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can explain the role in organizational terms, not only technical terms.

**ANSWER:** Often overlaps with RAG, agent, and LLM engineering. This role becomes distinct in teams where context quality directly affects correctness, latency, or cost.

**SENIOR-LEVEL ANSWER:** The senior framing is to explain why the role must collaborate across product, platform, security, and operations rather than acting as an isolated specialty. For this role, that usually shows up around **ranking** and **context cache design**.

**FOLLOW-UP QUESTIONS:**
- Which teams are the closest day-to-day partners? for Context Engineer specifically?
- What tension usually appears around ownership? for Context Engineer specifically?

**RED FLAGS:** Treating the role as if it only works alone.

---
### Q11. Why would a company invest in this role instead of asking a general software or DevOps engineer to absorb the work?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether the candidate understands the distinct production complexity behind the role.

**ANSWER:** Because the role exists at a failure boundary where generic engineering knowledge stops being enough.

**SENIOR-LEVEL ANSWER:** The senior framing is that specialization here is not about prestige, it is about ownership of new operational risk. For this role, that usually shows up around **token budgets** and **context truncation**.

**FOLLOW-UP QUESTIONS:**
- How does this role intersect with DevOps and SRE? for Context Engineer specifically?
- What anti-pattern appears when nobody explicitly owns this concern? for Context Engineer specifically?

**RED FLAGS:** Answering with marketing language instead of concrete engineering boundaries.

---
### Q12. What are the most important responsibilities of this role in a production organization?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can distinguish core ownership from adjacent responsibilities.

**ANSWER:** The role is responsible for design context assembly pipelines for prompts, retrieval, memory, and tool outputs. and related operating concerns.

**SENIOR-LEVEL ANSWER:** A senior engineer would emphasize not just building systems, but making them governable, observable, and supportable under production pressure in context engineer domains. For this role, that usually shows up around **context poisoning** and **conversation drift**.

**FOLLOW-UP QUESTIONS:**
- Which responsibilities should stay with platform or security teams? for Context Engineer specifically?
- Where does this role most often get pulled into incident response? for Context Engineer specifically?

**RED FLAGS:** Listing technologies without explaining operational ownership.

---
### Q13. How does this role relate to DevOps, SRE, platform engineering, and cloud engineering?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can place the role inside a broader engineering organization.

**ANSWER:** It overlaps with strongly overlaps with rag and agentic ai engineering.

**SENIOR-LEVEL ANSWER:** The senior answer is to describe the control boundaries clearly: what this role inherits from existing disciplines and what new AI-specific complexity it adds. For this role, that usually shows up around **context windows** and **state summarization**.

**FOLLOW-UP QUESTIONS:**
- Where does this role create new interfaces with security or FinOps? for Context Engineer specifically?
- What should remain centralized versus team-local? for Context Engineer specifically?

**RED FLAGS:** Pretending the role is completely separate from existing engineering disciplines.

---
### Q14. What skill stack should a senior engineer in this role have?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand that seniority here is about systems thinking plus execution, not just tool familiarity.

**ANSWER:** A senior engineer should combine prompt architecture, retrieval design, ranking, summarization, then layer on the rest through production repetition.

**SENIOR-LEVEL ANSWER:** The best answer ties each skill to a failure mode: identity and networking failures, rollout failures, retrieval failures, GPU contention, or cost explosions depending on the role. For this role, that usually shows up around **compression** and **tool-output compaction**.

**FOLLOW-UP QUESTIONS:**
- Which skills are foundational versus role-specific? for Context Engineer specifically?
- How would you onboard an engineer transitioning into this role? for Context Engineer specifically?

**RED FLAGS:** Giving a shopping list of buzzwords with no prioritization.

---
### Q15. Where does this role sit in a modern engineering organization?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can explain the role in organizational terms, not only technical terms.

**ANSWER:** Often overlaps with RAG, agent, and LLM engineering. This role becomes distinct in teams where context quality directly affects correctness, latency, or cost.

**SENIOR-LEVEL ANSWER:** The senior framing is to explain why the role must collaborate across product, platform, security, and operations rather than acting as an isolated specialty. For this role, that usually shows up around **memory** and **freshness scoring**.

**FOLLOW-UP QUESTIONS:**
- Which teams are the closest day-to-day partners? for Context Engineer specifically?
- What tension usually appears around ownership? for Context Engineer specifically?

**RED FLAGS:** Treating the role as if it only works alone.

---
### Q16. Why would a company invest in this role instead of asking a general software or DevOps engineer to absorb the work?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether the candidate understands the distinct production complexity behind the role.

**ANSWER:** Because the role exists at a failure boundary where generic engineering knowledge stops being enough.

**SENIOR-LEVEL ANSWER:** The senior framing is that specialization here is not about prestige, it is about ownership of new operational risk. For this role, that usually shows up around **ranking** and **context cache design**.

**FOLLOW-UP QUESTIONS:**
- How does this role intersect with DevOps and SRE? for Context Engineer specifically?
- What anti-pattern appears when nobody explicitly owns this concern? for Context Engineer specifically?

**RED FLAGS:** Answering with marketing language instead of concrete engineering boundaries.

---
### Q17. What are the most important responsibilities of this role in a production organization?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can distinguish core ownership from adjacent responsibilities.

**ANSWER:** The role is responsible for design context assembly pipelines for prompts, retrieval, memory, and tool outputs. and related operating concerns.

**SENIOR-LEVEL ANSWER:** A senior engineer would emphasize not just building systems, but making them governable, observable, and supportable under production pressure in context engineer domains. For this role, that usually shows up around **token budgets** and **context truncation**.

**FOLLOW-UP QUESTIONS:**
- Which responsibilities should stay with platform or security teams? for Context Engineer specifically?
- Where does this role most often get pulled into incident response? for Context Engineer specifically?

**RED FLAGS:** Listing technologies without explaining operational ownership.

---
### Q18. How does this role relate to DevOps, SRE, platform engineering, and cloud engineering?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can place the role inside a broader engineering organization.

**ANSWER:** It overlaps with strongly overlaps with rag and agentic ai engineering.

**SENIOR-LEVEL ANSWER:** The senior answer is to describe the control boundaries clearly: what this role inherits from existing disciplines and what new AI-specific complexity it adds. For this role, that usually shows up around **context poisoning** and **conversation drift**.

**FOLLOW-UP QUESTIONS:**
- Where does this role create new interfaces with security or FinOps? for Context Engineer specifically?
- What should remain centralized versus team-local? for Context Engineer specifically?

**RED FLAGS:** Pretending the role is completely separate from existing engineering disciplines.

---
### Q19. What skill stack should a senior engineer in this role have?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand that seniority here is about systems thinking plus execution, not just tool familiarity.

**ANSWER:** A senior engineer should combine prompt architecture, retrieval design, ranking, summarization, then layer on the rest through production repetition.

**SENIOR-LEVEL ANSWER:** The best answer ties each skill to a failure mode: identity and networking failures, rollout failures, retrieval failures, GPU contention, or cost explosions depending on the role. For this role, that usually shows up around **context windows** and **state summarization**.

**FOLLOW-UP QUESTIONS:**
- Which skills are foundational versus role-specific? for Context Engineer specifically?
- How would you onboard an engineer transitioning into this role? for Context Engineer specifically?

**RED FLAGS:** Giving a shopping list of buzzwords with no prioritization.

---
### Q20. Where does this role sit in a modern engineering organization?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can explain the role in organizational terms, not only technical terms.

**ANSWER:** Often overlaps with RAG, agent, and LLM engineering. This role becomes distinct in teams where context quality directly affects correctness, latency, or cost.

**SENIOR-LEVEL ANSWER:** The senior framing is to explain why the role must collaborate across product, platform, security, and operations rather than acting as an isolated specialty. For this role, that usually shows up around **compression** and **tool-output compaction**.

**FOLLOW-UP QUESTIONS:**
- Which teams are the closest day-to-day partners? for Context Engineer specifically?
- What tension usually appears around ownership? for Context Engineer specifically?

**RED FLAGS:** Treating the role as if it only works alone.

---
### Q21. Why would a company invest in this role instead of asking a general software or DevOps engineer to absorb the work?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether the candidate understands the distinct production complexity behind the role.

**ANSWER:** Because the role exists at a failure boundary where generic engineering knowledge stops being enough.

**SENIOR-LEVEL ANSWER:** The senior framing is that specialization here is not about prestige, it is about ownership of new operational risk. For this role, that usually shows up around **memory** and **freshness scoring**.

**FOLLOW-UP QUESTIONS:**
- How does this role intersect with DevOps and SRE? for Context Engineer specifically?
- What anti-pattern appears when nobody explicitly owns this concern? for Context Engineer specifically?

**RED FLAGS:** Answering with marketing language instead of concrete engineering boundaries.

---
### Q22. What are the most important responsibilities of this role in a production organization?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can distinguish core ownership from adjacent responsibilities.

**ANSWER:** The role is responsible for design context assembly pipelines for prompts, retrieval, memory, and tool outputs. and related operating concerns.

**SENIOR-LEVEL ANSWER:** A senior engineer would emphasize not just building systems, but making them governable, observable, and supportable under production pressure in context engineer domains. For this role, that usually shows up around **ranking** and **context cache design**.

**FOLLOW-UP QUESTIONS:**
- Which responsibilities should stay with platform or security teams? for Context Engineer specifically?
- Where does this role most often get pulled into incident response? for Context Engineer specifically?

**RED FLAGS:** Listing technologies without explaining operational ownership.

---
### Q23. How does this role relate to DevOps, SRE, platform engineering, and cloud engineering?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can place the role inside a broader engineering organization.

**ANSWER:** It overlaps with strongly overlaps with rag and agentic ai engineering.

**SENIOR-LEVEL ANSWER:** The senior answer is to describe the control boundaries clearly: what this role inherits from existing disciplines and what new AI-specific complexity it adds. For this role, that usually shows up around **token budgets** and **context truncation**.

**FOLLOW-UP QUESTIONS:**
- Where does this role create new interfaces with security or FinOps? for Context Engineer specifically?
- What should remain centralized versus team-local? for Context Engineer specifically?

**RED FLAGS:** Pretending the role is completely separate from existing engineering disciplines.

---
### Q24. What skill stack should a senior engineer in this role have?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand that seniority here is about systems thinking plus execution, not just tool familiarity.

**ANSWER:** A senior engineer should combine prompt architecture, retrieval design, ranking, summarization, then layer on the rest through production repetition.

**SENIOR-LEVEL ANSWER:** The best answer ties each skill to a failure mode: identity and networking failures, rollout failures, retrieval failures, GPU contention, or cost explosions depending on the role. For this role, that usually shows up around **context poisoning** and **conversation drift**.

**FOLLOW-UP QUESTIONS:**
- Which skills are foundational versus role-specific? for Context Engineer specifically?
- How would you onboard an engineer transitioning into this role? for Context Engineer specifically?

**RED FLAGS:** Giving a shopping list of buzzwords with no prioritization.

---
### Q25. Where does this role sit in a modern engineering organization?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** Context Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can explain the role in organizational terms, not only technical terms.

**ANSWER:** Often overlaps with RAG, agent, and LLM engineering. This role becomes distinct in teams where context quality directly affects correctness, latency, or cost.

**SENIOR-LEVEL ANSWER:** The senior framing is to explain why the role must collaborate across product, platform, security, and operations rather than acting as an isolated specialty. For this role, that usually shows up around **context windows** and **state summarization**.

**FOLLOW-UP QUESTIONS:**
- Which teams are the closest day-to-day partners? for Context Engineer specifically?
- What tension usually appears around ownership? for Context Engineer specifically?

**RED FLAGS:** Treating the role as if it only works alone.

---
