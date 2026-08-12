# LLMOps Engineer — Challenges

---

## Challenge 1: Improve shadow traffic safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **Argo CD** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **prompt versioning** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **prompt versioning** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 2: Improve prompt versioning safely

**Level:** Level 2 — Implementation

**Objective**  
Build confidence operating **LLM gateways** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **fallback rollout** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **fallback rollout** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 3: Improve fallback rollout safely

**Level:** Level 3 — Production

**Objective**  
Build confidence operating **Prometheus** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **regression detection** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **regression detection** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 4: Improve regression detection safely

**Level:** Level 4 — Troubleshooting

**Objective**  
Build confidence operating **OpenTelemetry** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **release approvals** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **release approvals** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 5: Improve release approvals safely

**Level:** Level 5 — Senior Engineering

**Objective**  
Build confidence operating **Python** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **post-release metrics** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **post-release metrics** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 6: Improve post release metrics safely

**Level:** Level 6 — Staff / Principal Architecture

**Objective**  
Build confidence operating **GitHub Actions** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **shadow traffic** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **shadow traffic** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 7: Improve shadow traffic safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **Argo CD** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **prompt versioning** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **prompt versioning** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 8: Improve prompt versioning safely

**Level:** Level 2 — Implementation

**Objective**  
Build confidence operating **LLM gateways** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **fallback rollout** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **fallback rollout** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 9: Improve fallback rollout safely

**Level:** Level 3 — Production

**Objective**  
Build confidence operating **Prometheus** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **regression detection** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **regression detection** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 10: Improve regression detection safely

**Level:** Level 4 — Troubleshooting

**Objective**  
Build confidence operating **OpenTelemetry** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **release approvals** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **release approvals** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 11: Improve release approvals safely

**Level:** Level 5 — Senior Engineering

**Objective**  
Build confidence operating **Python** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **post-release metrics** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **post-release metrics** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 12: Improve post release metrics safely

**Level:** Level 6 — Staff / Principal Architecture

**Objective**  
Build confidence operating **GitHub Actions** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **shadow traffic** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **shadow traffic** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 13: Improve shadow traffic safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **Argo CD** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **prompt versioning** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **prompt versioning** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 14: Improve prompt versioning safely

**Level:** Level 2 — Implementation

**Objective**  
Build confidence operating **LLM gateways** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **fallback rollout** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **fallback rollout** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 15: Improve fallback rollout safely

**Level:** Level 3 — Production

**Objective**  
Build confidence operating **Prometheus** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **regression detection** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **regression detection** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 16: Improve regression detection safely

**Level:** Level 4 — Troubleshooting

**Objective**  
Build confidence operating **OpenTelemetry** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **release approvals** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **release approvals** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 17: Improve release approvals safely

**Level:** Level 5 — Senior Engineering

**Objective**  
Build confidence operating **Python** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **post-release metrics** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **post-release metrics** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 18: Improve post release metrics safely

**Level:** Level 6 — Staff / Principal Architecture

**Objective**  
Build confidence operating **GitHub Actions** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **shadow traffic** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **shadow traffic** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 19: Improve shadow traffic safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **Argo CD** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **prompt versioning** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **prompt versioning** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 20: Improve prompt versioning safely

**Level:** Level 2 — Implementation

**Objective**  
Build confidence operating **LLM gateways** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **fallback rollout** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **fallback rollout** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 21: Improve fallback rollout safely

**Level:** Level 3 — Production

**Objective**  
Build confidence operating **Prometheus** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **regression detection** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **regression detection** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 22: Improve regression detection safely

**Level:** Level 4 — Troubleshooting

**Objective**  
Build confidence operating **OpenTelemetry** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **release approvals** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **release approvals** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 23: Improve release approvals safely

**Level:** Level 5 — Senior Engineering

**Objective**  
Build confidence operating **Python** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **post-release metrics** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **post-release metrics** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 24: Improve post release metrics safely

**Level:** Level 6 — Staff / Principal Architecture

**Objective**  
Build confidence operating **GitHub Actions** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **shadow traffic** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **shadow traffic** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 25: Improve shadow traffic safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **Argo CD** in a way that reflects the responsibilities of a **LLMOps Engineer**.

**Scenario**  
You inherit a workflow where **prompt versioning** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **prompt versioning** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
