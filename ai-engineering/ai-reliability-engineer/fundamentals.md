# AI Reliability Engineer — Fundamentals

---

### Q1. What are the core production primitives behind this role?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know the building blocks well enough to reason about higher-order failures.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **token throughput** is never only a feature choice. It changes how the system behaves around **SLIs**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Prometheus**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **token throughput** is only a win if it does not silently worsen **SLIs** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if token throughput scaled 10x?
- How would you instrument SLIs so you could prove the answer in production?
- When would Prometheus be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q2. Why does this role require systems thinking instead of only model or application knowledge?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can connect local mechanisms to end-to-end production outcomes.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **agent success rate** is never only a feature choice. It changes how the system behaves around **SLOs**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Grafana**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **agent success rate** is only a win if it does not silently worsen **SLOs** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if agent success rate scaled 10x?
- How would you instrument SLOs so you could prove the answer in production?
- When would Grafana be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q3. Which failure modes become common when teams scale this capability too quickly?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand operational maturity problems, not just happy-path mechanics.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **retrieval success** is never only a feature choice. It changes how the system behaves around **error budgets**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **OpenTelemetry**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **retrieval success** is only a win if it does not silently worsen **error budgets** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if retrieval success scaled 10x?
- How would you instrument error budgets so you could prove the answer in production?
- When would OpenTelemetry be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q4. How should a senior engineer reason about trade-offs in this role?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can balance speed, safety, latency, cost, and ownership.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **tool dependency health** is never only a feature choice. It changes how the system behaves around **latency**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Kubernetes**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **tool dependency health** is only a win if it does not silently worsen **latency** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if tool dependency health scaled 10x?
- How would you instrument latency so you could prove the answer in production?
- When would Kubernetes be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q5. What production telemetry matters most here?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know how to prove a system is healthy instead of assuming it.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **quality rollback** is never only a feature choice. It changes how the system behaves around **TTFT**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **LLM gateways**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **quality rollback** is only a win if it does not silently worsen **TTFT** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if quality rollback scaled 10x?
- How would you instrument TTFT so you could prove the answer in production?
- When would LLM gateways be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q6. What are the core production primitives behind this role?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know the building blocks well enough to reason about higher-order failures.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **error budget policy** is never only a feature choice. It changes how the system behaves around **incident response**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Redis**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **error budget policy** is only a win if it does not silently worsen **incident response** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if error budget policy scaled 10x?
- How would you instrument incident response so you could prove the answer in production?
- When would Redis be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q7. Why does this role require systems thinking instead of only model or application knowledge?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can connect local mechanisms to end-to-end production outcomes.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **token throughput** is never only a feature choice. It changes how the system behaves around **SLIs**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **queues**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **token throughput** is only a win if it does not silently worsen **SLIs** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if token throughput scaled 10x?
- How would you instrument SLIs so you could prove the answer in production?
- When would queues be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q8. Which failure modes become common when teams scale this capability too quickly?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand operational maturity problems, not just happy-path mechanics.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **agent success rate** is never only a feature choice. It changes how the system behaves around **SLOs**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Prometheus**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **agent success rate** is only a win if it does not silently worsen **SLOs** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if agent success rate scaled 10x?
- How would you instrument SLOs so you could prove the answer in production?
- When would Prometheus be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q9. How should a senior engineer reason about trade-offs in this role?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can balance speed, safety, latency, cost, and ownership.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **retrieval success** is never only a feature choice. It changes how the system behaves around **error budgets**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Grafana**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **retrieval success** is only a win if it does not silently worsen **error budgets** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if retrieval success scaled 10x?
- How would you instrument error budgets so you could prove the answer in production?
- When would Grafana be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q10. What production telemetry matters most here?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know how to prove a system is healthy instead of assuming it.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **tool dependency health** is never only a feature choice. It changes how the system behaves around **latency**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **OpenTelemetry**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **tool dependency health** is only a win if it does not silently worsen **latency** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if tool dependency health scaled 10x?
- How would you instrument latency so you could prove the answer in production?
- When would OpenTelemetry be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q11. What are the core production primitives behind this role?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know the building blocks well enough to reason about higher-order failures.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **quality rollback** is never only a feature choice. It changes how the system behaves around **TTFT**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Kubernetes**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **quality rollback** is only a win if it does not silently worsen **TTFT** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if quality rollback scaled 10x?
- How would you instrument TTFT so you could prove the answer in production?
- When would Kubernetes be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q12. Why does this role require systems thinking instead of only model or application knowledge?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can connect local mechanisms to end-to-end production outcomes.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **error budget policy** is never only a feature choice. It changes how the system behaves around **incident response**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **LLM gateways**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **error budget policy** is only a win if it does not silently worsen **incident response** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if error budget policy scaled 10x?
- How would you instrument incident response so you could prove the answer in production?
- When would LLM gateways be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q13. Which failure modes become common when teams scale this capability too quickly?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand operational maturity problems, not just happy-path mechanics.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **token throughput** is never only a feature choice. It changes how the system behaves around **SLIs**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Redis**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **token throughput** is only a win if it does not silently worsen **SLIs** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if token throughput scaled 10x?
- How would you instrument SLIs so you could prove the answer in production?
- When would Redis be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q14. How should a senior engineer reason about trade-offs in this role?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can balance speed, safety, latency, cost, and ownership.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **agent success rate** is never only a feature choice. It changes how the system behaves around **SLOs**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **queues**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **agent success rate** is only a win if it does not silently worsen **SLOs** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if agent success rate scaled 10x?
- How would you instrument SLOs so you could prove the answer in production?
- When would queues be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q15. What production telemetry matters most here?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know how to prove a system is healthy instead of assuming it.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **retrieval success** is never only a feature choice. It changes how the system behaves around **error budgets**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Prometheus**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **retrieval success** is only a win if it does not silently worsen **error budgets** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if retrieval success scaled 10x?
- How would you instrument error budgets so you could prove the answer in production?
- When would Prometheus be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q16. What are the core production primitives behind this role?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know the building blocks well enough to reason about higher-order failures.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **tool dependency health** is never only a feature choice. It changes how the system behaves around **latency**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Grafana**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **tool dependency health** is only a win if it does not silently worsen **latency** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if tool dependency health scaled 10x?
- How would you instrument latency so you could prove the answer in production?
- When would Grafana be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q17. Why does this role require systems thinking instead of only model or application knowledge?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can connect local mechanisms to end-to-end production outcomes.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **quality rollback** is never only a feature choice. It changes how the system behaves around **TTFT**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **OpenTelemetry**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **quality rollback** is only a win if it does not silently worsen **TTFT** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if quality rollback scaled 10x?
- How would you instrument TTFT so you could prove the answer in production?
- When would OpenTelemetry be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q18. Which failure modes become common when teams scale this capability too quickly?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand operational maturity problems, not just happy-path mechanics.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **error budget policy** is never only a feature choice. It changes how the system behaves around **incident response**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Kubernetes**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **error budget policy** is only a win if it does not silently worsen **incident response** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if error budget policy scaled 10x?
- How would you instrument incident response so you could prove the answer in production?
- When would Kubernetes be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q19. How should a senior engineer reason about trade-offs in this role?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can balance speed, safety, latency, cost, and ownership.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **token throughput** is never only a feature choice. It changes how the system behaves around **SLIs**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **LLM gateways**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **token throughput** is only a win if it does not silently worsen **SLIs** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if token throughput scaled 10x?
- How would you instrument SLIs so you could prove the answer in production?
- When would LLM gateways be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q20. What production telemetry matters most here?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know how to prove a system is healthy instead of assuming it.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **agent success rate** is never only a feature choice. It changes how the system behaves around **SLOs**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Redis**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **agent success rate** is only a win if it does not silently worsen **SLOs** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if agent success rate scaled 10x?
- How would you instrument SLOs so you could prove the answer in production?
- When would Redis be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q21. What are the core production primitives behind this role?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know the building blocks well enough to reason about higher-order failures.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **retrieval success** is never only a feature choice. It changes how the system behaves around **error budgets**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **queues**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **retrieval success** is only a win if it does not silently worsen **error budgets** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if retrieval success scaled 10x?
- How would you instrument error budgets so you could prove the answer in production?
- When would queues be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q22. Why does this role require systems thinking instead of only model or application knowledge?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can connect local mechanisms to end-to-end production outcomes.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **tool dependency health** is never only a feature choice. It changes how the system behaves around **latency**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Prometheus**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **tool dependency health** is only a win if it does not silently worsen **latency** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if tool dependency health scaled 10x?
- How would you instrument latency so you could prove the answer in production?
- When would Prometheus be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q23. Which failure modes become common when teams scale this capability too quickly?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand operational maturity problems, not just happy-path mechanics.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **quality rollback** is never only a feature choice. It changes how the system behaves around **TTFT**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Grafana**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **quality rollback** is only a win if it does not silently worsen **TTFT** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if quality rollback scaled 10x?
- How would you instrument TTFT so you could prove the answer in production?
- When would Grafana be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q24. How should a senior engineer reason about trade-offs in this role?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can balance speed, safety, latency, cost, and ownership.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **error budget policy** is never only a feature choice. It changes how the system behaves around **incident response**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **OpenTelemetry**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **error budget policy** is only a win if it does not silently worsen **incident response** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if error budget policy scaled 10x?
- How would you instrument incident response so you could prove the answer in production?
- When would OpenTelemetry be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q25. What production telemetry matters most here?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Reliability Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know how to prove a system is healthy instead of assuming it.

**ANSWER:** In ai reliability engineer, one of the core ideas is that **token throughput** is never only a feature choice. It changes how the system behaves around **SLIs**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Kubernetes**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **token throughput** is only a win if it does not silently worsen **SLIs** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if token throughput scaled 10x?
- How would you instrument SLIs so you could prove the answer in production?
- When would Kubernetes be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
