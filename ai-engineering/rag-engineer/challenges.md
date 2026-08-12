# RAG Engineer — Challenges

---

## Challenge 1: Improve hybrid search safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **embeddings** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **document ACLs** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **document ACLs** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 2: Improve document ACLs safely

**Level:** Level 2 — Implementation

**Objective**  
Build confidence operating **rerankers** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **query rewriting** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **query rewriting** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 3: Improve query rewriting safely

**Level:** Level 3 — Production

**Objective**  
Build confidence operating **object storage** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **index rebuilds** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **index rebuilds** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 4: Improve index rebuilds safely

**Level:** Level 4 — Troubleshooting

**Objective**  
Build confidence operating **PostgreSQL/pgvector** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **metadata schema** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **metadata schema** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 5: Improve metadata schema safely

**Level:** Level 5 — Senior Engineering

**Objective**  
Build confidence operating **Python** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **retrieval quality metrics** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **retrieval quality metrics** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 6: Improve retrieval quality metrics safely

**Level:** Level 6 — Staff / Principal Architecture

**Objective**  
Build confidence operating **vector databases** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **hybrid search** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **hybrid search** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 7: Improve hybrid search safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **embeddings** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **document ACLs** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **document ACLs** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 8: Improve document ACLs safely

**Level:** Level 2 — Implementation

**Objective**  
Build confidence operating **rerankers** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **query rewriting** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **query rewriting** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 9: Improve query rewriting safely

**Level:** Level 3 — Production

**Objective**  
Build confidence operating **object storage** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **index rebuilds** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **index rebuilds** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 10: Improve index rebuilds safely

**Level:** Level 4 — Troubleshooting

**Objective**  
Build confidence operating **PostgreSQL/pgvector** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **metadata schema** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **metadata schema** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 11: Improve metadata schema safely

**Level:** Level 5 — Senior Engineering

**Objective**  
Build confidence operating **Python** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **retrieval quality metrics** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **retrieval quality metrics** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 12: Improve retrieval quality metrics safely

**Level:** Level 6 — Staff / Principal Architecture

**Objective**  
Build confidence operating **vector databases** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **hybrid search** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **hybrid search** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 13: Improve hybrid search safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **embeddings** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **document ACLs** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **document ACLs** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 14: Improve document ACLs safely

**Level:** Level 2 — Implementation

**Objective**  
Build confidence operating **rerankers** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **query rewriting** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **query rewriting** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 15: Improve query rewriting safely

**Level:** Level 3 — Production

**Objective**  
Build confidence operating **object storage** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **index rebuilds** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **index rebuilds** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 16: Improve index rebuilds safely

**Level:** Level 4 — Troubleshooting

**Objective**  
Build confidence operating **PostgreSQL/pgvector** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **metadata schema** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **metadata schema** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 17: Improve metadata schema safely

**Level:** Level 5 — Senior Engineering

**Objective**  
Build confidence operating **Python** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **retrieval quality metrics** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **retrieval quality metrics** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 18: Improve retrieval quality metrics safely

**Level:** Level 6 — Staff / Principal Architecture

**Objective**  
Build confidence operating **vector databases** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **hybrid search** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **hybrid search** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 19: Improve hybrid search safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **embeddings** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **document ACLs** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **document ACLs** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 20: Improve document ACLs safely

**Level:** Level 2 — Implementation

**Objective**  
Build confidence operating **rerankers** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **query rewriting** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **query rewriting** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 21: Improve query rewriting safely

**Level:** Level 3 — Production

**Objective**  
Build confidence operating **object storage** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **index rebuilds** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **index rebuilds** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 22: Improve index rebuilds safely

**Level:** Level 4 — Troubleshooting

**Objective**  
Build confidence operating **PostgreSQL/pgvector** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **metadata schema** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **metadata schema** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 23: Improve metadata schema safely

**Level:** Level 5 — Senior Engineering

**Objective**  
Build confidence operating **Python** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **retrieval quality metrics** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **retrieval quality metrics** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 24: Improve retrieval quality metrics safely

**Level:** Level 6 — Staff / Principal Architecture

**Objective**  
Build confidence operating **vector databases** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **hybrid search** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **hybrid search** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
## Challenge 25: Improve hybrid search safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **embeddings** in a way that reflects the responsibilities of a **RAG Engineer**.

**Scenario**  
You inherit a workflow where **document ACLs** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

**Requirements**  
- Preserve security and auditability.
- Keep the system observable enough for future debugging.
- Document one explicit trade-off you are making.

**Constraints**  
- Assume no perfect greenfield rewrite.
- Prefer an incremental change that can be validated quickly.

**Tasks**  
1. Inspect the current state.
2. Propose a safer or more scalable configuration.
3. Show how you would validate the result.
4. Explain a rollback path.

**Commands / configuration**  
```bash
kubectl get deploy -A
helm get values platform -n ai
curl -s https://service.internal/readyz
python3 scripts/check.py
```

```yaml
kind: Deployment
metadata:
  name: role-lab
spec:
  replicas: 2
```

**Expected result**  
The workflow becomes safer, easier to observe, and easier to operate during failure.

**Solution**  
Start by clarifying the current failure boundary, then apply the smallest change that improves **document ACLs** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

**Explanation**  
This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

**Verification**  
- Confirm successful rollout or config application.
- Confirm key metrics and traces improved.
- Confirm rollback instructions still work.

**Possible failure modes**  
- Validation only checks happy-path behavior.
- Hidden dependencies still violate the assumptions behind the fix.
- The new control improves one metric but worsens cost or latency.

**Stretch challenge**  
Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

---
