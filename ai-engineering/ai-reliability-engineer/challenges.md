# AI Reliability Engineer — Challenges

---

## Challenge 1: Improve token throughput safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **Grafana** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **agent success rate** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **agent success rate** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 2: Improve agent success rate safely

**Level:** Level 2 — Implementation

**Objective**  
Build confidence operating **OpenTelemetry** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **retrieval success** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **retrieval success** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 3: Improve retrieval success safely

**Level:** Level 3 — Production

**Objective**  
Build confidence operating **Kubernetes** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **tool dependency health** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **tool dependency health** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 4: Improve tool dependency health safely

**Level:** Level 4 — Troubleshooting

**Objective**  
Build confidence operating **LLM gateways** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **quality rollback** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **quality rollback** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 5: Improve quality rollback safely

**Level:** Level 5 — Senior Engineering

**Objective**  
Build confidence operating **Redis** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **error budget policy** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **error budget policy** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 6: Improve error budget policy safely

**Level:** Level 6 — Staff / Principal Architecture

**Objective**  
Build confidence operating **queues** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **token throughput** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **token throughput** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 7: Improve token throughput safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **Prometheus** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **agent success rate** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **agent success rate** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 8: Improve agent success rate safely

**Level:** Level 2 — Implementation

**Objective**  
Build confidence operating **Grafana** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **retrieval success** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **retrieval success** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 9: Improve retrieval success safely

**Level:** Level 3 — Production

**Objective**  
Build confidence operating **OpenTelemetry** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **tool dependency health** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **tool dependency health** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 10: Improve tool dependency health safely

**Level:** Level 4 — Troubleshooting

**Objective**  
Build confidence operating **Kubernetes** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **quality rollback** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **quality rollback** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 11: Improve quality rollback safely

**Level:** Level 5 — Senior Engineering

**Objective**  
Build confidence operating **LLM gateways** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **error budget policy** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **error budget policy** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 12: Improve error budget policy safely

**Level:** Level 6 — Staff / Principal Architecture

**Objective**  
Build confidence operating **Redis** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **token throughput** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **token throughput** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 13: Improve token throughput safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **queues** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **agent success rate** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **agent success rate** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 14: Improve agent success rate safely

**Level:** Level 2 — Implementation

**Objective**  
Build confidence operating **Prometheus** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **retrieval success** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **retrieval success** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 15: Improve retrieval success safely

**Level:** Level 3 — Production

**Objective**  
Build confidence operating **Grafana** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **tool dependency health** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **tool dependency health** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 16: Improve tool dependency health safely

**Level:** Level 4 — Troubleshooting

**Objective**  
Build confidence operating **OpenTelemetry** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **quality rollback** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **quality rollback** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 17: Improve quality rollback safely

**Level:** Level 5 — Senior Engineering

**Objective**  
Build confidence operating **Kubernetes** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **error budget policy** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **error budget policy** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 18: Improve error budget policy safely

**Level:** Level 6 — Staff / Principal Architecture

**Objective**  
Build confidence operating **LLM gateways** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **token throughput** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **token throughput** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 19: Improve token throughput safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **Redis** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **agent success rate** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **agent success rate** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 20: Improve agent success rate safely

**Level:** Level 2 — Implementation

**Objective**  
Build confidence operating **queues** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **retrieval success** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **retrieval success** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 21: Improve retrieval success safely

**Level:** Level 3 — Production

**Objective**  
Build confidence operating **Prometheus** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **tool dependency health** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **tool dependency health** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 22: Improve tool dependency health safely

**Level:** Level 4 — Troubleshooting

**Objective**  
Build confidence operating **Grafana** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **quality rollback** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **quality rollback** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 23: Improve quality rollback safely

**Level:** Level 5 — Senior Engineering

**Objective**  
Build confidence operating **OpenTelemetry** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **error budget policy** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **error budget policy** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 24: Improve error budget policy safely

**Level:** Level 6 — Staff / Principal Architecture

**Objective**  
Build confidence operating **Kubernetes** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **token throughput** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **token throughput** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 25: Improve token throughput safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **LLM gateways** in a way that reflects the responsibilities of a **AI Reliability Engineer**.

**Scenario**  
You inherit a workflow where **agent success rate** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **agent success rate** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
