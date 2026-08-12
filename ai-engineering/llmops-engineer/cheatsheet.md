# LLMOps Engineer — Cheatsheet

## Role-specific focus

- shadow traffic
- prompt versioning
- fallback rollout
- regression detection
- release approvals
- post-release metrics

## High-value metrics and alerts

- deployment
- versioning
- canaries
- A/B testing
- drift
- rollbacks

## Core incident commands

```bash
kubectl get pods -A
kubectl describe pod <pod> -n <ns>
kubectl logs <pod> -n <ns> --tail=100
helm list -A
curl -vk https://service.internal/health
dig api.internal
openssl s_client -connect host:443
nvidia-smi
journalctl -u service -n 100
```

## Prometheus / observability shortcuts

```promql
rate(http_requests_total[5m])
histogram_quantile(0.95, sum(rate(request_latency_bucket[5m])) by (le))
sum(rate(token_output_total[5m])) by (model)
```

## Common checks

- Confirm the intended tenant, region, cluster, and release version first.
- Confirm identity and policy assumptions before assuming an infrastructure fault.
- Confirm whether the problem is correctness, latency, cost, saturation, or rollout drift.
- Compare the current state to the last known good release or configuration.

## Useful configuration snippets

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: llmops-engineer
spec:
  replicas: 2
```

```json
{
  "role": "llmops-engineer",
  "environment": "production",
  "telemetry": true
}
```

```python
def health_signal(latency_ms: float, success_rate: float) -> str:
    if success_rate < 0.99:
        return "degraded"
    if latency_ms > 1500:
        return "slow"
    return "healthy"
```

## Failure signatures

- A change improves one local metric but worsens the overall request path.
- Alerts identify a symptom but not the first failed control boundary.
- A fallback path exists in architecture diagrams but not in runtime reality.
- Cost and reliability drift silently because telemetry is incomplete.

## Runbook reminders

- Start with evidence collection, not immediate configuration churn.
- Prefer reversible mitigations before deep surgery.
- Record the exact release, policy, or traffic change that preceded the incident.
- Add prevention controls after the incident so the same failure is easier to detect next time.
