# Incident: Checkout Service 503 Cascade

**Fictional company:** Northwind Retail (constructed for this repository
— not a real incident at a real company).

## Incident

Northwind Retail's checkout service returned `503` for approximately 40%
of requests over an 18-minute window during a promotional traffic spike.

## Timeline

- **T+0:00** — Marketing promotion goes live; traffic to `checkout-svc`
  climbs roughly 6x baseline within 3 minutes.
- **T+0:04** — `checkout-svc` pods begin failing readiness probes
  intermittently.
- **T+0:06** — Error-rate alert fires (`checkout-svc` 5xx rate > 5%).
- **T+0:09** — On-call engineer confirms pods are `Running` but a growing
  fraction are `NotReady`.
- **T+0:14** — Root cause identified (see below).
- **T+0:18** — Mitigation applied; error rate returns to baseline within 2
  minutes.

## Symptoms

`kubectl get pods` showed pods cycling between `Ready` and `NotReady`
under load, without restarting (`RESTARTS` stayed at 0 — this ruled out a
crash-and-restart pattern early).

## Impact

~40% of checkout attempts during the window received a `503`; estimated
significant abandoned-cart impact during a promotional traffic spike
specifically — the worst possible timing.

## Evidence

- Readiness probe configuration: `httpGet /healthz`, `periodSeconds: 5`,
  `failureThreshold: 1` — a single failed check immediately marked the
  pod `NotReady`.
- `/healthz` implementation: checked connectivity to the checkout
  database connection pool.
- Database connection pool metrics: pool utilization spiked to 100%
  during the traffic surge, with brief queueing for available
  connections under peak load.

## Investigation

Per the [Follow the Request](../../mental-models/follow-the-request.md)
model, the pattern (Running, not crashing, but cycling `Ready`/`NotReady`
under load) pointed directly at the readiness probe rather than the
application crashing — matching the general
[liveness-vs-readiness](../../kubernetes/fundamentals.md#q5-whats-the-difference-between-a-liveness-probe-and-a-readiness-probe-and-whats-the-risk-of-misconfiguring-each)
reasoning. The specific trigger: under peak load, brief, sub-second
connection-pool queueing (a normal, recoverable condition, not an actual
outage) was enough to fail `/healthz`'s DB-connectivity check, and with
`failureThreshold: 1`, a single slow check was enough to pull the pod out
of the load-balancing rotation immediately.

## Root cause

The readiness probe was checking a dependency (DB pool availability) with
**zero tolerance for transient conditions** (`failureThreshold: 1`,
5-second period) — appropriate for detecting genuine, sustained
unhealthiness, but far too sensitive for a metric (connection pool
saturation) that fluctuates normally under real load. The result: normal
load-induced queueing was misinterpreted as pod-level unhealthiness,
pulling healthy capacity out of rotation at exactly the moment it was
most needed, which then increased load on the remaining pods, worsening
the same condition — a self-reinforcing cascade.

## Resolution

- Raised `failureThreshold` to `3` and `periodSeconds` to `10` (tolerating
  brief transient conditions before marking a pod unready).
- Separated the readiness check's DB-connectivity check from a stricter
  timeout/threshold than the overall probe, so a genuinely slow/dead DB
  still fails fast, while brief pool queueing under load doesn't.

## Prevention

- Load-tested the readiness probe configuration specifically under
  realistic peak-traffic connection-pool behavior before the next
  promotional event — the original configuration had only been validated
  under steady-state load, where pool saturation never occurred.
- Added an explicit alert on **readiness-probe-driven pod removal rate**
  (pods leaving rotation due to failed readiness checks, not
  crashes) — this incident's actual mechanism wasn't visible in the
  standard crash/restart-focused alerting that existed beforehand.

## SLO impact

Consumed a meaningful fraction of `checkout-svc`'s monthly availability
error budget in an 18-minute window — flagged in the postmortem as the
kind of event that should trigger tightened pre-promotion load-testing
requirements going forward, not just this specific probe fix.

## Lessons learned

Readiness probes checking a **fluctuating-under-load** dependency need
threshold tuning that accounts for normal load variance, not just
steady-state behavior — the same probe configuration that looks perfectly
reasonable in steady-state testing can actively cause an outage under the
exact traffic spike it should be helping the system survive.

## Interview questions

1. Why did `RESTARTS` staying at 0 rule out certain hypotheses early in
   this investigation?
2. How would you design a readiness check for a dependency that's
   *expected* to show brief degradation under real load, without making
   the check meaningless?
3. What's the mechanism by which this became a self-reinforcing cascade,
   specifically?
4. How would you have caught this before the promotion went live?
