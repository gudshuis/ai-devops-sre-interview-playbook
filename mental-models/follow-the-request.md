# Mental Model: Follow the Request

The single most broadly useful debugging/design framework in this
repository — used implicitly throughout, made explicit here.

## The model

```text
Client
  ↓
DNS
  ↓
Network
  ↓
Load Balancer
  ↓
Proxy / Ingress
  ↓
Application
  ↓
Dependency
  ↓
Database
```

At **every** boundary between two boxes, ask the same fixed set of
questions:

```text
Did the request arrive?
Did the request leave?
How long did it take?
Was identity/auth preserved across this boundary?
Was the data modified here?
Was an error generated here?
```

## Why this works

Most debugging confusion comes from **skipping straight to a guess**
about which layer is broken, based on the symptom's surface appearance —
per the [Kubernetes 503 troubleshooting lab](../kubernetes/troubleshooting.md#lab-3-kubectl-reports-ingress-is-healthy-but-requests-return-503),
a generic error at the client tells you almost nothing about which
boundary actually failed. Walking the request boundary-by-boundary,
asking the same fixed questions at each one, converts "vague symptom" into
"specific boundary where a specific question's answer was 'no.'"

## Where it's used throughout this repository

- [`request-journeys/prompt-to-rag-response.md`](../request-journeys/prompt-to-rag-response.md)
  is this exact model applied to an AI system.
- [`foundations/networking/README.md`](../foundations/networking/README.md)
  Q1 is this model applied specifically to the TCP/TLS/application-layer
  boundary.
- Every troubleshooting lab in [`kubernetes/troubleshooting.md`](../kubernetes/troubleshooting.md)
  implicitly follows this shape even where not stated explicitly.

## Applying it live

When you're stuck on a system-design or troubleshooting question and
don't know where to start: **draw the boxes first**, even roughly, before
trying to answer anything. The act of drawing forces you to commit to
what the actual request path is, which is usually most of the battle in
an ambiguous prompt.
