# Agent vs. Deterministic Workflow

See [`ai-engineering/agents-and-agentic-ai/fundamentals.md`](../ai-engineering/agents-and-agentic-ai/fundamentals.md)
Q1 for the underlying definition this card assumes.

## When a deterministic workflow is the right choice

- The task's steps and their order are genuinely knowable in advance —
  "extract field X, validate it, write to database" doesn't need an LLM
  deciding what to do next; it needs an LLM (if at all) doing one bounded
  extraction step inside an otherwise fixed pipeline.
- You need **testability** — a deterministic pipeline's paths are
  enumerable, so conventional test coverage is possible; an agent's
  execution path is only knowable at runtime.
- Reliability requirements are strict and the task doesn't genuinely
  require judgment under uncertainty.

## When an agent is the right choice

- The task requires **deciding what to do next based on results you can't
  fully predict in advance** — genuinely open-ended investigation, or a
  task where the right sequence of tool calls depends on what earlier
  calls returned.
- The cost of enumerating every possible path deterministically would
  itself be prohibitive, and some judgment-under-uncertainty is an
  acceptable trade for handling that flexibility.

## The trap

Treating "agent vs. workflow" as an architecture-wide, all-or-nothing
choice for an entire product feature. In practice, most production
systems that need agentic behavior only need it for a **narrow slice** of
the overall task — the rest should stay deterministic. Building an entire
feature as one large agent loop when only one step genuinely needs
judgment-under-uncertainty trades away testability and reliability for no
real benefit on the deterministic parts of the task.

## Interview framing

A strong answer to "should this be an agent" names the *specific step(s)*
that need genuine judgment, rather than answering for the whole feature at
once.
