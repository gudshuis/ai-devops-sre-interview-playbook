# AI Infrastructure Engineer — Fundamentals

---

### Q1. What are the core production primitives behind this role?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know the building blocks well enough to reason about higher-order failures.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **MIG partitioning** is never only a feature choice. It changes how the system behaves around **GPU clusters**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **NVIDIA stack**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **MIG partitioning** is only a win if it does not silently worsen **GPU clusters** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if MIG partitioning scaled 10x?
- How would you instrument GPU clusters so you could prove the answer in production?
- When would NVIDIA stack be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q2. Why does this role require systems thinking instead of only model or application knowledge?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can connect local mechanisms to end-to-end production outcomes.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **GPU memory fragmentation** is never only a feature choice. It changes how the system behaves around **CUDA**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **CUDA**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **GPU memory fragmentation** is only a win if it does not silently worsen **CUDA** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if GPU memory fragmentation scaled 10x?
- How would you instrument CUDA so you could prove the answer in production?
- When would CUDA be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q3. Which failure modes become common when teams scale this capability too quickly?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand operational maturity problems, not just happy-path mechanics.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **driver compatibility** is never only a feature choice. It changes how the system behaves around **storage**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **nvidia-smi**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **driver compatibility** is only a win if it does not silently worsen **storage** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if driver compatibility scaled 10x?
- How would you instrument storage so you could prove the answer in production?
- When would nvidia-smi be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q4. How should a senior engineer reason about trade-offs in this role?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can balance speed, safety, latency, cost, and ownership.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **node health** is never only a feature choice. It changes how the system behaves around **RDMA**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Kubernetes**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **node health** is only a win if it does not silently worsen **RDMA** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if node health scaled 10x?
- How would you instrument RDMA so you could prove the answer in production?
- When would Kubernetes be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q5. What production telemetry matters most here?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know how to prove a system is healthy instead of assuming it.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **capacity forecasting** is never only a feature choice. It changes how the system behaves around **hardware utilization**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **containerd**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **capacity forecasting** is only a win if it does not silently worsen **hardware utilization** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if capacity forecasting scaled 10x?
- How would you instrument hardware utilization so you could prove the answer in production?
- When would containerd be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q6. What are the core production primitives behind this role?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know the building blocks well enough to reason about higher-order failures.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **cluster scaling** is never only a feature choice. It changes how the system behaves around **capacity**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **RDMA**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **cluster scaling** is only a win if it does not silently worsen **capacity** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if cluster scaling scaled 10x?
- How would you instrument capacity so you could prove the answer in production?
- When would RDMA be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q7. Why does this role require systems thinking instead of only model or application knowledge?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can connect local mechanisms to end-to-end production outcomes.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **MIG partitioning** is never only a feature choice. It changes how the system behaves around **GPU clusters**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **object storage**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **MIG partitioning** is only a win if it does not silently worsen **GPU clusters** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if MIG partitioning scaled 10x?
- How would you instrument GPU clusters so you could prove the answer in production?
- When would object storage be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q8. Which failure modes become common when teams scale this capability too quickly?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand operational maturity problems, not just happy-path mechanics.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **GPU memory fragmentation** is never only a feature choice. It changes how the system behaves around **CUDA**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **NVIDIA stack**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **GPU memory fragmentation** is only a win if it does not silently worsen **CUDA** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if GPU memory fragmentation scaled 10x?
- How would you instrument CUDA so you could prove the answer in production?
- When would NVIDIA stack be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q9. How should a senior engineer reason about trade-offs in this role?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can balance speed, safety, latency, cost, and ownership.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **driver compatibility** is never only a feature choice. It changes how the system behaves around **storage**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **CUDA**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **driver compatibility** is only a win if it does not silently worsen **storage** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if driver compatibility scaled 10x?
- How would you instrument storage so you could prove the answer in production?
- When would CUDA be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q10. What production telemetry matters most here?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know how to prove a system is healthy instead of assuming it.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **node health** is never only a feature choice. It changes how the system behaves around **RDMA**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **nvidia-smi**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **node health** is only a win if it does not silently worsen **RDMA** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if node health scaled 10x?
- How would you instrument RDMA so you could prove the answer in production?
- When would nvidia-smi be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q11. What are the core production primitives behind this role?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know the building blocks well enough to reason about higher-order failures.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **capacity forecasting** is never only a feature choice. It changes how the system behaves around **hardware utilization**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Kubernetes**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **capacity forecasting** is only a win if it does not silently worsen **hardware utilization** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if capacity forecasting scaled 10x?
- How would you instrument hardware utilization so you could prove the answer in production?
- When would Kubernetes be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q12. Why does this role require systems thinking instead of only model or application knowledge?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can connect local mechanisms to end-to-end production outcomes.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **cluster scaling** is never only a feature choice. It changes how the system behaves around **capacity**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **containerd**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **cluster scaling** is only a win if it does not silently worsen **capacity** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if cluster scaling scaled 10x?
- How would you instrument capacity so you could prove the answer in production?
- When would containerd be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q13. Which failure modes become common when teams scale this capability too quickly?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand operational maturity problems, not just happy-path mechanics.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **MIG partitioning** is never only a feature choice. It changes how the system behaves around **GPU clusters**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **RDMA**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **MIG partitioning** is only a win if it does not silently worsen **GPU clusters** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if MIG partitioning scaled 10x?
- How would you instrument GPU clusters so you could prove the answer in production?
- When would RDMA be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q14. How should a senior engineer reason about trade-offs in this role?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can balance speed, safety, latency, cost, and ownership.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **GPU memory fragmentation** is never only a feature choice. It changes how the system behaves around **CUDA**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **object storage**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **GPU memory fragmentation** is only a win if it does not silently worsen **CUDA** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if GPU memory fragmentation scaled 10x?
- How would you instrument CUDA so you could prove the answer in production?
- When would object storage be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q15. What production telemetry matters most here?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know how to prove a system is healthy instead of assuming it.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **driver compatibility** is never only a feature choice. It changes how the system behaves around **storage**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **NVIDIA stack**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **driver compatibility** is only a win if it does not silently worsen **storage** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if driver compatibility scaled 10x?
- How would you instrument storage so you could prove the answer in production?
- When would NVIDIA stack be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q16. What are the core production primitives behind this role?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know the building blocks well enough to reason about higher-order failures.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **node health** is never only a feature choice. It changes how the system behaves around **RDMA**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **CUDA**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **node health** is only a win if it does not silently worsen **RDMA** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if node health scaled 10x?
- How would you instrument RDMA so you could prove the answer in production?
- When would CUDA be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q17. Why does this role require systems thinking instead of only model or application knowledge?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can connect local mechanisms to end-to-end production outcomes.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **capacity forecasting** is never only a feature choice. It changes how the system behaves around **hardware utilization**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **nvidia-smi**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **capacity forecasting** is only a win if it does not silently worsen **hardware utilization** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if capacity forecasting scaled 10x?
- How would you instrument hardware utilization so you could prove the answer in production?
- When would nvidia-smi be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q18. Which failure modes become common when teams scale this capability too quickly?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand operational maturity problems, not just happy-path mechanics.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **cluster scaling** is never only a feature choice. It changes how the system behaves around **capacity**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Kubernetes**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **cluster scaling** is only a win if it does not silently worsen **capacity** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if cluster scaling scaled 10x?
- How would you instrument capacity so you could prove the answer in production?
- When would Kubernetes be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q19. How should a senior engineer reason about trade-offs in this role?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can balance speed, safety, latency, cost, and ownership.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **MIG partitioning** is never only a feature choice. It changes how the system behaves around **GPU clusters**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **containerd**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **MIG partitioning** is only a win if it does not silently worsen **GPU clusters** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if MIG partitioning scaled 10x?
- How would you instrument GPU clusters so you could prove the answer in production?
- When would containerd be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q20. What production telemetry matters most here?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know how to prove a system is healthy instead of assuming it.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **GPU memory fragmentation** is never only a feature choice. It changes how the system behaves around **CUDA**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **RDMA**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **GPU memory fragmentation** is only a win if it does not silently worsen **CUDA** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if GPU memory fragmentation scaled 10x?
- How would you instrument CUDA so you could prove the answer in production?
- When would RDMA be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q21. What are the core production primitives behind this role?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know the building blocks well enough to reason about higher-order failures.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **driver compatibility** is never only a feature choice. It changes how the system behaves around **storage**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **object storage**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **driver compatibility** is only a win if it does not silently worsen **storage** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if driver compatibility scaled 10x?
- How would you instrument storage so you could prove the answer in production?
- When would object storage be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q22. Why does this role require systems thinking instead of only model or application knowledge?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can connect local mechanisms to end-to-end production outcomes.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **node health** is never only a feature choice. It changes how the system behaves around **RDMA**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **NVIDIA stack**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **node health** is only a win if it does not silently worsen **RDMA** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if node health scaled 10x?
- How would you instrument RDMA so you could prove the answer in production?
- When would NVIDIA stack be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q23. Which failure modes become common when teams scale this capability too quickly?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand operational maturity problems, not just happy-path mechanics.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **capacity forecasting** is never only a feature choice. It changes how the system behaves around **hardware utilization**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **CUDA**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **capacity forecasting** is only a win if it does not silently worsen **hardware utilization** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if capacity forecasting scaled 10x?
- How would you instrument hardware utilization so you could prove the answer in production?
- When would CUDA be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q24. How should a senior engineer reason about trade-offs in this role?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you can balance speed, safety, latency, cost, and ownership.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **cluster scaling** is never only a feature choice. It changes how the system behaves around **capacity**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **nvidia-smi**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **cluster scaling** is only a win if it does not silently worsen **capacity** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if cluster scaling scaled 10x?
- How would you instrument capacity so you could prove the answer in production?
- When would nvidia-smi be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
### Q25. What production telemetry matters most here?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Infrastructure Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you know how to prove a system is healthy instead of assuming it.

**ANSWER:** In ai infrastructure engineer, one of the core ideas is that **MIG partitioning** is never only a feature choice. It changes how the system behaves around **GPU clusters**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. For example, when a team introduces or changes **Kubernetes**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'.

**SENIOR-LEVEL ANSWER:** The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. They will also separate local optimizations from system optimizations: improving **MIG partitioning** is only a win if it does not silently worsen **GPU clusters** elsewhere.

**FOLLOW-UP QUESTIONS:**
- What would break first if MIG partitioning scaled 10x?
- How would you instrument GPU clusters so you could prove the answer in production?
- When would Kubernetes be the wrong choice for this role?

**RED FLAGS:** Staying at dictionary-definition depth and never reaching production trade-offs.

---
