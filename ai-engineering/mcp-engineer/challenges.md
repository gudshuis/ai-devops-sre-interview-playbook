# MCP Engineer — Challenges

---

## Challenge 1: Improve resource exposure safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **OAuth** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **prompt delivery** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **prompt delivery** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 2: Improve prompt delivery safely

**Level:** Level 2 — Implementation

**Objective**  
Build confidence operating **HTTP** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **tenant isolation** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **tenant isolation** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 3: Improve tenant isolation safely

**Level:** Level 3 — Production

**Objective**  
Build confidence operating **stdio** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **tool approval** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **tool approval** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 4: Improve tool approval safely

**Level:** Level 4 — Troubleshooting

**Objective**  
Build confidence operating **API gateways** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **blast radius** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **blast radius** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 5: Improve blast radius safely

**Level:** Level 5 — Senior Engineering

**Objective**  
Build confidence operating **Kubernetes** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **protocol debugging** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **protocol debugging** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 6: Improve protocol debugging safely

**Level:** Level 6 — Staff / Principal Architecture

**Objective**  
Build confidence operating **Redis** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **resource exposure** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **resource exposure** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 7: Improve resource exposure safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **MCP** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **prompt delivery** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **prompt delivery** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 8: Improve prompt delivery safely

**Level:** Level 2 — Implementation

**Objective**  
Build confidence operating **OAuth** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **tenant isolation** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **tenant isolation** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 9: Improve tenant isolation safely

**Level:** Level 3 — Production

**Objective**  
Build confidence operating **HTTP** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **tool approval** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **tool approval** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 10: Improve tool approval safely

**Level:** Level 4 — Troubleshooting

**Objective**  
Build confidence operating **stdio** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **blast radius** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **blast radius** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 11: Improve blast radius safely

**Level:** Level 5 — Senior Engineering

**Objective**  
Build confidence operating **API gateways** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **protocol debugging** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **protocol debugging** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 12: Improve protocol debugging safely

**Level:** Level 6 — Staff / Principal Architecture

**Objective**  
Build confidence operating **Kubernetes** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **resource exposure** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **resource exposure** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 13: Improve resource exposure safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **Redis** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **prompt delivery** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **prompt delivery** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 14: Improve prompt delivery safely

**Level:** Level 2 — Implementation

**Objective**  
Build confidence operating **MCP** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **tenant isolation** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **tenant isolation** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 15: Improve tenant isolation safely

**Level:** Level 3 — Production

**Objective**  
Build confidence operating **OAuth** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **tool approval** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **tool approval** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 16: Improve tool approval safely

**Level:** Level 4 — Troubleshooting

**Objective**  
Build confidence operating **HTTP** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **blast radius** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **blast radius** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 17: Improve blast radius safely

**Level:** Level 5 — Senior Engineering

**Objective**  
Build confidence operating **stdio** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **protocol debugging** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **protocol debugging** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 18: Improve protocol debugging safely

**Level:** Level 6 — Staff / Principal Architecture

**Objective**  
Build confidence operating **API gateways** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **resource exposure** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **resource exposure** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 19: Improve resource exposure safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **Kubernetes** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **prompt delivery** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **prompt delivery** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 20: Improve prompt delivery safely

**Level:** Level 2 — Implementation

**Objective**  
Build confidence operating **Redis** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **tenant isolation** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **tenant isolation** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 21: Improve tenant isolation safely

**Level:** Level 3 — Production

**Objective**  
Build confidence operating **MCP** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **tool approval** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **tool approval** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 22: Improve tool approval safely

**Level:** Level 4 — Troubleshooting

**Objective**  
Build confidence operating **OAuth** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **blast radius** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **blast radius** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 23: Improve blast radius safely

**Level:** Level 5 — Senior Engineering

**Objective**  
Build confidence operating **HTTP** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **protocol debugging** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **protocol debugging** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 24: Improve protocol debugging safely

**Level:** Level 6 — Staff / Principal Architecture

**Objective**  
Build confidence operating **stdio** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **resource exposure** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **resource exposure** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
## Challenge 25: Improve resource exposure safely

**Level:** Level 1 — Fundamentals

**Objective**  
Build confidence operating **API gateways** in a way that reflects the responsibilities of a **MCP Engineer**.

**Scenario**  
You inherit a workflow where **prompt delivery** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

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
Start by clarifying the current failure boundary, then apply the smallest change that improves **prompt delivery** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

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
