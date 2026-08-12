# Glossary

Short, precise definitions for terms used across the repository without
being re-explained every time. This is a reference, not a learning
resource — if you need the *why*, follow the link to the domain folder
where the concept is treated in depth.

## Platform / SRE

- **SLI (Service Level Indicator)** — a quantitative measure of some
  aspect of service behavior (e.g. request latency at p99). See
  `platform-engineering/sre/`.
- **SLO (Service Level Objective)** — a target value/range for an SLI over
  a time window (e.g. "p99 latency < 300ms for 99.9% of the trailing
  28 days"). Not a promise to a customer — that's an SLA.
- **Error budget** — the allowed amount of SLO violation before it's
  "spent"; a formalized way of trading reliability work against feature
  velocity.
- **Toil** — manual, repetitive, automatable operational work that scales
  linearly with service growth. Google's original SRE framing; reducing it
  is a core SRE mandate, not just "nice to have."
- **Blast radius** — the scope of impact if a given component/change
  fails. Central to almost every senior design answer in this repository.

## Kubernetes / Platform

- **Control plane** — the set of components (API server, etcd, scheduler,
  controller manager) that make and record cluster-wide decisions, as
  opposed to the data plane (kubelet, running workloads) that executes
  them.
- **Golden path** — a supported, paved, well-documented way to accomplish
  a common task on a platform, as opposed to every team building their own
  bespoke solution.
- **GitOps** — declarative infrastructure/application state stored in Git,
  reconciled into the live environment by an automated controller (e.g.
  Argo CD, Flux), rather than applied by imperative pipeline steps.

## AI Engineering

- **Context window** — the maximum amount of text (measured in tokens) a
  model can attend to in a single inference call.
- **RAG (Retrieval-Augmented Generation)** — augmenting a model's response
  with content retrieved from an external knowledge source at inference
  time, rather than relying solely on what was learned during training.
- **MCP (Model Context Protocol)** — an open protocol standardizing how
  applications provide context, tools, and resources to LLMs. See
  `ai-engineering/mcp/`.
- **Agent** — a system where a model plans and executes a sequence of
  actions (often via tool calls) toward a goal, rather than producing a
  single response to a single prompt.
- **Hallucination** — a model producing output that is fluent and
  confident but factually incorrect or unsupported by its given context.

## Distributed Systems

- **CAP theorem** — a distributed data store can provide at most two of
  Consistency, Availability, and Partition tolerance simultaneously during
  an actual network partition.
- **Idempotency** — a property where performing an operation multiple
  times has the same effect as performing it once; essential for safe
  retries.
- **Backpressure** — a mechanism for a system under load to signal
  upstream producers to slow down, rather than silently dropping work or
  degrading unbounded.

---

This glossary grows alongside the content that needs it — if a domain
folder introduces a term worth a one-line reference definition here, add
it via the process in [CONTRIBUTING.md](../../CONTRIBUTING.md).
