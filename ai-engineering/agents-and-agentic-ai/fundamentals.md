# Agents & Agentic AI — Fundamentals

---

### Q1. What actually distinguishes an "agent" from a deterministic pipeline that happens to call an LLM?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Engineer, Applied AI Engineer, Agentic AI Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you have a real definition,
since "agent" gets used loosely enough in industry marketing that many
candidates can't actually distinguish it from a normal LLM call in a
pipeline.

**ANSWER:** A deterministic pipeline calls an LLM at a fixed point with a
fixed, predetermined next step regardless of the output content (e.g.
"call the model, take its output, pass to step 2"). An **agent**
involves the model **deciding its own next action** — which tool to call,
whether to continue or stop, whether to re-plan — based on the results of
previous steps, in a loop, until some termination condition.

**SENIOR-LEVEL ANSWER:** The practically important distinction isn't
philosophical, it's **predictability and testability**. A deterministic
pipeline's execution path is enumerable — you can write conventional
tests against it. An agent's execution path is only knowable at runtime,
which changes your entire engineering approach: you can't exhaustively
test every path, so reliability engineering shifts toward **bounding the
blast radius of any single step** (least-privilege tool access, spend/step
caps, human-in-the-loop gates on high-risk actions) rather than trying to
prove correctness of the whole trajectory in advance. The senior framing
I'd want in an interview: "agent vs. workflow" is a spectrum, and the
right engineering question for a given task isn't "should this be an
agent" as a binary — it's "how much of this task's control flow can
safely be deterministic, and where does genuine judgment-under-uncertainty
actually earn the reliability cost of making that part agentic." Most
production systems that need "agentic" behavior only need it for a narrow
slice of the overall task, with everything else kept deterministic.

**FOLLOW-UP QUESTIONS:**
- Give an example of a task that looks like it needs an agent but is
  actually better served by a deterministic pipeline with one LLM
  classification step.
- How would you test an agent's behavior given its path isn't enumerable?
- What's "ReAct" (reason + act) and how does it relate to the basic agent
  loop?

**RED FLAGS:** Calling any system with an LLM call in it an "agent" —
loses the actual engineering distinction that matters for reliability
design.

---

### Q2. Explain the difference between an agent's short-term and long-term memory, and why conflating them causes real production bugs.

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Engineer, Agentic AI Engineer

**ANSWER:**
- **Short-term memory**: the current conversation/task context — what's
  in the model's context window right now, scoped to this session/task.
- **Long-term memory**: information persisted **across** sessions —
  learned facts, user preferences, past task outcomes — typically stored
  externally (a database, a vector store) and selectively retrieved back
  into context when relevant.

**SENIOR-LEVEL ANSWER:** The production bug pattern I'd want a candidate
to name: **writing everything to long-term memory indiscriminately**,
which causes two distinct failure modes over time. First, **retrieval
noise** — as long-term memory grows, retrieving "relevant" past context
becomes progressively harder to do precisely, and irrelevant retrieved
memories can actively degrade the current task's output quality (this is
the same retrieval-precision problem RAG has, applied to an agent's own
history). Second, and more subtle: **stale memory presented as current
fact** — if a user's preference or a fact about the world changes, and the
old version is still retrievable from long-term memory without any
staleness/recency signal, the agent can confidently act on outdated
information. The engineering discipline this requires: treating long-term
memory writes as a deliberate design decision (what's actually worth
persisting, with what metadata for later relevance/recency scoring), not
"log everything, sort it out at retrieval time."

**FOLLOW-UP QUESTIONS:**
- How would you decide what's worth writing to long-term memory versus
  discarding at the end of a session?
- How would you handle contradictory information in long-term memory
  (a preference that changed)?
- What's the relationship between an agent's long-term memory and a RAG
  system — are they the same thing?

**RED FLAGS:** Treating "give the agent long-term memory" as a strictly
positive feature addition with no downside/design cost.

---

### Q3. What's a "reflection" step in an agent loop, and when does adding one actually improve reliability versus just adding latency and cost?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Engineer, Agentic AI Engineer

**ANSWER:** A reflection step has the agent evaluate its own prior output
or plan before proceeding — e.g. "review the code you just wrote for
bugs before running it" as an explicit additional step, rather than
proceeding directly from generation to execution.

**SENIOR-LEVEL ANSWER:** Reflection genuinely helps when the failure
modes it's meant to catch are things the model **can plausibly detect
given the same information it already had** — a logic error in
self-written code it can re-read, an obviously malformed tool-call
argument. It does **not** reliably help against failure modes the model
lacks the information to detect in the first place — hallucinated facts
it has no way to self-verify without external grounding, for instance.
Adding a reflection step there just adds latency/cost for a confident
re-statement of the same error, not genuine error correction. The senior
engineering call: reflection is worth its cost specifically for
self-checkable failure modes (syntax, logical consistency within a task's
own stated constraints), and should be replaced with **external
verification** (running the code, checking against a ground-truth source,
a human review gate) for failure modes that require information the model
doesn't already have.

**FOLLOW-UP QUESTIONS:**
- How would you measure whether a reflection step is actually improving
  output quality versus just adding cost?
- What's the difference between reflection and a separate "critic" model
  reviewing the primary model's output?
- At what point does iterative reflection stop helping and start looping
  unproductively — how would you bound it?

**RED FLAGS:** Treating reflection as a general-purpose reliability fix
applicable to every failure mode, without distinguishing self-checkable
errors from genuinely unverifiable ones.

---

### Q4. What's "planning" in an agent context, and how does it differ from the agent just picking the next tool call reactively at each step?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** AI Engineer, Agentic AI Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand planning as
a distinct architectural choice with real trade-offs, not just a
synonym for "the agent thinks before acting."

**ANSWER:** A purely reactive agent decides only its immediate next
action based on current state, with no explicit representation of the
overall task's remaining steps. A planning agent first produces an
explicit (if revisable) multi-step plan, then executes against it,
potentially re-planning if execution reveals the plan was wrong.

**SENIOR-LEVEL ANSWER:** The trade-off: upfront planning gives better
global coherence for tasks with real interdependencies between steps
(step 3 depends on knowing step 5 is coming) and lets a human/reviewer
see the intended approach before execution — genuinely useful for
higher-stakes tasks. Purely reactive agents are cheaper (no separate
planning call) and adapt more fluidly to genuinely unpredictable
environments where a fixed plan would go stale quickly. Most production
systems land on a hybrid: a coarse initial plan, re-evaluated
reactively as execution reveals new information — rarely purely one or
the other.

**FOLLOW-UP QUESTIONS:**
- When would a fixed upfront plan actively hurt an agent's performance?
- How would you decide when a plan needs to be revised mid-execution?
- What's the cost of re-planning too frequently?

**RED FLAGS:** Treating "planning" and "reasoning" as identical — every
agent reasons at each step; not every agent produces an explicit,
reusable plan.

---

### Q5. What's the difference between short-term "working memory" within a single agent turn and the cross-session long-term memory discussed in Q2?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Engineer

**ANSWER:** Working memory is whatever's in the current context window
for this specific task/turn — it vanishes when the session ends unless
explicitly persisted. Long-term memory (Q2) is deliberately persisted
across sessions in external storage, retrieved back selectively when
relevant.

**SENIOR-LEVEL ANSWER:** The engineering-relevant distinction is what
each is *for*: working memory should hold everything genuinely needed
for the current task's coherence (no artificial gaps mid-task), while
long-term memory should hold only what's worth the retrieval-noise cost
of surfacing in a *future*, different task. Conflating them — treating
every long-term memory write as equally available "just like" working
memory — reintroduces the retrieval-precision problem discussed in Q2
unnecessarily for information that only ever needed to live within one
turn's working memory.

**FOLLOW-UP QUESTIONS:**
- How would you decide, at the end of a session, what (if anything)
  graduates from working memory to long-term memory?
- What's the context-window cost trade-off of a very large working
  memory versus aggressive summarization?
- How does this distinction map onto human cognitive-science memory
  models, if at all — is the analogy useful or misleading?

**RED FLAGS:** Using "memory" as an undifferentiated single concept
without distinguishing session-scoped from cross-session persistence.

---

### Q6. What does "state" mean for an agent, and why does managing it well matter for reliability?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Engineer, Agentic AI Engineer

**ANSWER:** State is everything the agent needs to track about where it
is in a task — completed steps, gathered information, current plan,
outstanding sub-goals — distinct from the raw conversation transcript,
which is unstructured and harder to reason over programmatically.

**SENIOR-LEVEL ANSWER:** Well-structured, explicit state (a defined
schema for "what step am I on, what have I gathered") makes an agent's
progress inspectable and resumable — you can pause, persist, and resume
an agent's execution cleanly. An agent that only tracks state implicitly
via the conversation transcript is much harder to debug (you have to
re-parse the whole transcript to know "where" it is) and much harder to
resume reliably after an interruption. This connects directly to the
externalized-session-state scaling discussion in
`ai-engineering/mcp/senior-scenarios.md` S22 — the same principle,
applied at the single-agent-execution level rather than
gateway-session-scale.

**FOLLOW-UP QUESTIONS:**
- How would you design an explicit state schema for a multi-step
  research agent?
- What's the risk of state drifting out of sync with the actual
  conversation transcript?
- How would you resume an agent's execution cleanly after a crash
  mid-task?

**RED FLAGS:** Relying purely on the raw transcript as the agent's
"state," with no structured representation — makes debugging and
resumption much harder than necessary.

---

### Q7. What's the difference between a supervisor-worker multi-agent pattern and simply chaining several single-purpose agents sequentially?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Agentic AI Engineer

**ANSWER:** A sequential chain has a fixed, predetermined order — agent A
always runs, then B, then C. A supervisor-worker pattern has a
supervisor *dynamically deciding* which worker(s) to invoke, in what
order, potentially in parallel, based on the task — the routing itself
is a decision, not a fixed pipeline.

**SENIOR-LEVEL ANSWER:** This maps directly onto the agent-vs-workflow
distinction from Q1 — a fixed sequential chain is really a deterministic
workflow with LLM calls at each stage (testable, predictable path); a
supervisor-worker pattern is genuinely agentic at the routing layer
(the supervisor's decision of *which* worker to invoke isn't
enumerable in advance). The senior judgment call: use a fixed chain
when the task decomposition is genuinely always the same order; use a
supervisor only when the actual routing decision varies meaningfully
by task content — reaching for supervisor-worker by default adds
unpredictability and cost for tasks that never actually needed dynamic
routing.

**FOLLOW-UP QUESTIONS:**
- How would you decide whether a given multi-step task needs dynamic
  supervisor routing versus a fixed sequential chain?
- What's the failure-propagation difference between the two patterns?
- How does this connect to the multi-agent orchestration scenario in
  `senior-scenarios.md` S1?

**RED FLAGS:** Using "multi-agent" as a blanket term without
distinguishing fixed chains (deterministic) from genuine dynamic
supervisor routing (agentic).

---

### Q8. What's a "runaway agent," and what specifically causes an agent loop to fail to terminate?

**DIFFICULTY:** 🟢 Beginner / 🔵 Intermediate
**ROLE:** AI Engineer, SRE

**ANSWER:** A runaway agent is one that keeps taking actions (tool
calls, reasoning steps) without converging toward task completion —
looping indefinitely, or until some external limit (cost, time, max
iterations) forcibly stops it.

**SENIOR-LEVEL ANSWER:** The common root causes: an evaluator/stopping
condition that's never satisfied (too strict, or checking for the wrong
signal), a tool returning ambiguous results the agent keeps
re-attempting (per the partial-failure-signaling discussion in
`ai-engineering/mcp/fundamentals.md` Q21), or a genuinely unanswerable
task with no graceful "give up and report uncertainty" path built in.
The non-negotiable engineering control: every agent loop needs a hard
max-iteration or max-cost bound with a defined fallback behavior
(report partial progress/uncertainty) when hit — treating "the agent
will naturally converge" as a safe assumption is exactly the failure
mode this question tests for.

**FOLLOW-UP QUESTIONS:**
- How would you choose an appropriate max-iteration bound for a given
  task type?
- What should the fallback behavior be when the bound is hit — silent
  failure, or something better?
- How would you detect a runaway agent in production before it consumes
  excessive cost?

**RED FLAGS:** No mention of a hard iteration/cost bound as a
non-negotiable safety control — this is the single most basic
reliability requirement for any agent loop.

---

### Q9. What's the difference between a tool call failing and a tool call succeeding but returning a result the agent misinterprets?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Engineer, Agentic AI Engineer

**ANSWER:** A failed call is detectable at the protocol/execution level
(an error response, a timeout). A "successful but misinterpreted" call
returns valid data that the agent's *reasoning* about it goes wrong on —
no error anywhere in the technical stack, but the agent's next action is
still wrong.

**SENIOR-LEVEL ANSWER:** The second category is much harder to catch
programmatically — there's no exception to log, no failed health check;
the only way to detect it is evaluating the agent's actual *decisions*
against expected behavior (per the evals discipline in
`ai-engineering/evals/README.md`), not just monitoring for technical
errors. This is why agent-specific evaluation needs to check full
trajectories (which tools were called, with what reasoning) rather than
just final-output correctness or error-rate metrics — a technically
error-free session can still represent a complete reasoning failure.

**FOLLOW-UP QUESTIONS:**
- How would you build monitoring that catches "successful but
  misinterpreted" tool results, given there's no technical error to
  alert on?
- Give a concrete example of a tool result that's easy for an agent to
  misinterpret.
- How does this connect to the LLM-as-judge evaluation approach?

**RED FLAGS:** Equating "no errors in the logs" with "the agent behaved
correctly" — misses this entire failure category.

---

### Q10. What's idempotency's role specifically in agent tool design, beyond the general software-engineering definition?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Agentic AI Engineer, AI Engineer

**ANSWER:** An agent — unlike a typical deterministic client — may retry
a tool call because it *misjudged* whether the first attempt succeeded
(per Q9), not just because of a network failure. This makes idempotency
even more important for agent-invoked tools than for typical
client-server retries, since the retry trigger itself is less reliable
(model judgment, not just a technical failure signal).

**SENIOR-LEVEL ANSWER:** Per the retry-safety discussion in
`ai-engineering/mcp/fundamentals.md` Q21, a non-idempotent tool without
clear retry-safety signaling combined with an agent's own tendency to
retry on ambiguous results is a specific, real production risk (a
duplicate charge, a duplicate message sent) — not a hypothetical edge
case. The engineering response is layered: design tools to be
idempotent where at all possible (a repeated call with the same
idempotency key has no additional effect), and where genuinely not
possible, make the non-idempotency and retry-unsafety explicit in the
tool's response schema so the agent's own retry logic can respect it.

**FOLLOW-UP QUESTIONS:**
- How would you retrofit idempotency onto an existing, already-deployed
  tool that doesn't have it?
- What's the risk of an idempotency key implementation that isn't
  itself atomic (per the distributed-systems race-condition reasoning)?
- How would you test that an agent actually respects a retry-unsafety
  signal, rather than retrying regardless?

**RED FLAGS:** Treating idempotency as a nice-to-have rather than a
near-mandatory property for any side-effecting tool an agent can invoke.

---

### Q11. How would you version an agent's own prompt/reasoning logic over time, given it's not a traditional API with a formal schema?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Engineer, LLMOps Engineer

**ANSWER:** Treat prompt/reasoning-logic changes with the same rigor as
code changes — version-controlled, with a defined rollback path, and
evaluated against a golden dataset (per
`ai-engineering/llmops-and-mlops/README.md`) before promotion, rather
than edited in place with no tracking.

**SENIOR-LEVEL ANSWER:** The specific risk of *not* doing this: an
in-place prompt edit with no versioning makes it impossible to cleanly
answer "did behavior change because of this prompt edit, or because of
a model upgrade, or both simultaneously" when something regresses —
exactly the diagnostic problem the model-upgrade regression question in
LLMOps addresses, applied to prompt changes specifically. Treating
prompts as versioned artifacts (with the same golden-dataset regression
gate applied to model upgrades) closes this diagnostic gap.

**FOLLOW-UP QUESTIONS:**
- How would you A/B test a prompt change safely in production before
  full rollout?
- What's the relationship between prompt versioning and the underlying
  model version — do they need to be tracked together?
- How would you roll back a prompt change that's already been fully
  deployed?

**RED FLAGS:** Editing agent prompts in place with no version control or
evaluation gate — the same anti-pattern as deploying code changes
without review or testing.

---

### Q12. What does "blast radius" mean specifically for an autonomous agent, and how would you bound it for a newly-deployed agent you don't yet fully trust?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Agentic AI Engineer, AI Security Engineer

**ANSWER:** Blast radius is the scope of damage a single bad decision
(a hallucinated plan, a misjudged tool call) can cause before it's
caught — determined by what tools/data/systems the agent can actually
reach and act on, not by how "smart" the underlying model is.

**SENIOR-LEVEL ANSWER:** Bounding blast radius for a new, not-yet-
trusted agent means applying least-privilege tool access (only the
specific tools the task genuinely requires, not a broad general
toolkit "just in case"), tiered permissions for irreversible actions
(per the human-in-the-loop design in `ai-engineering/mcp/senior-scenarios.md`
S9), and staged trust expansion — starting with read-only/recommend-
only capability and graduating to autonomous action only after
demonstrated reliability, mirroring the staged-trust design in the
production-infrastructure-access scenario (S2). The blast radius should
shrink as trust is *earned* through evidence, not granted upfront based
on capability alone.

**FOLLOW-UP QUESTIONS:**
- How would you measure "demonstrated reliability" concretely enough to
  justify expanding an agent's blast radius?
- What's the risk of bounding blast radius too conservatively — does it
  have a real cost?
- How does this connect to the least-privilege principle discussed
  throughout `ai-engineering/mcp/security.md`?

**RED FLAGS:** Granting a new agent broad tool access based on the
model's general capability rather than staged, evidence-based trust
expansion.

---

### Q13. What's the difference between "human-in-the-loop" and "human-on-the-loop" for agent oversight?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Agentic AI Engineer

**ANSWER:** Human-in-the-loop means a human must actively approve before
a specific action executes (synchronous gate). Human-on-the-loop means
the agent acts autonomously but a human monitors and can intervene/stop
it, without pre-approving each action (asynchronous oversight).

**SENIOR-LEVEL ANSWER:** These aren't just different UX patterns — they
have fundamentally different latency and risk profiles. In-the-loop adds
real latency to every gated action (justified for genuinely high-risk,
low-frequency actions per the risk-scored approval routing in
`ai-engineering/mcp/senior-scenarios.md` S9) but guarantees nothing bad
executes without review. On-the-loop preserves autonomous speed but
means a bad action can execute *before* a human notices — appropriate
only when the action's blast radius is bounded enough that "caught
after the fact, quickly" is an acceptable risk posture, not when
actions are irreversible.

**FOLLOW-UP QUESTIONS:**
- What class of action would you never put under on-the-loop oversight,
  regardless of monitoring quality?
- How fast does human intervention need to be for on-the-loop oversight
  to be meaningful for a given action's risk profile?
- Could an agent's action class move from in-the-loop to on-the-loop
  over time — what would justify that?

**RED FLAGS:** Treating on-the-loop monitoring as equivalent risk
protection to in-the-loop approval — it's a materially weaker
guarantee, appropriate only for lower-blast-radius actions.

---

### Q14. How would you design observability specifically for an agent's *reasoning*, not just its tool calls?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Engineer, SRE

**ANSWER:** Log the agent's intermediate reasoning/planning output (not
just the final tool calls and results) — the "why" behind each
decision, not just the "what" — so a reviewer can reconstruct not only
what the agent did but what it believed at each step.

**SENIOR-LEVEL ANSWER:** Tool-call-only logging tells you *what*
happened but not *why* — insufficient for diagnosing a reasoning
failure (Q9's "successful but misinterpreted" category specifically).
Full reasoning-trace observability is what makes it possible to
distinguish "the tool gave bad data" from "the tool gave good data and
the agent reasoned about it incorrectly" — a genuinely different root
cause requiring a genuinely different fix (fix the tool vs. fix the
prompt/reasoning). This directly extends the full-trace observability
principle from `ai-engineering/mcp/senior-scenarios.md` S12/`troubleshooting.md`
Lab 25 to include the reasoning layer, not just the protocol-call layer.

**FOLLOW-UP QUESTIONS:**
- What's the cost (token usage, storage) of logging full reasoning
  traces at scale, and how would you manage it?
- How would you build tooling to actually make sense of a large volume
  of reasoning traces, rather than just accumulating unreviewed logs?
- How does this observability data feed back into prompt/model
  evaluation?

**RED FLAGS:** Logging only tool calls and final outputs, with no
visibility into the agent's actual intermediate reasoning — makes
diagnosing reasoning-layer failures nearly impossible.

---

### Q15. What's the cost structure of a multi-step agentic task, and how does it differ from a single LLM call's cost?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Agentic AI Engineer, FinOps Engineer

**ANSWER:** A single call's cost is roughly proportional to input/output
tokens for that one call. An agentic task's cost compounds across every
step (each reasoning step, each tool call's context assembly) — total
cost scales with the *number of steps*, not just the complexity of any
single step, and is much harder to predict upfront since the step count
itself is often not known in advance.

**SENIOR-LEVEL ANSWER:** This unpredictability is a real production
FinOps concern distinct from single-call cost management — a task that
should take 3 steps but loops to 30 (per the runaway-agent failure mode
in Q8) has a cost blow-up that a per-call cost estimate never predicted.
The engineering response: per-task cost caps (not just per-call), cost
monitoring granular enough to catch anomalous task-level cost before it
compounds further, and cost-awareness built into the agent's own
stopping/evaluation logic (a task that's consuming disproportionate
cost relative to its apparent value should itself be a signal to stop
and escalate, not just a cost the platform absorbs silently).

**FOLLOW-UP QUESTIONS:**
- How would you set a reasonable per-task cost cap without knowing the
  task's genuine complexity in advance?
- How does this connect to the runaway-agent bound discussed in Q8 — are
  they the same control or complementary ones?
- How would you attribute agentic-task cost per team/user for chargeback
  purposes?

**RED FLAGS:** Estimating agentic feature cost the same way as a
single-call feature's cost — misses the compounding, unpredictable
nature of multi-step task cost entirely.

---

### Q16. What's "excessive agency" as an AI security concern, and how is it distinct from a tool simply having a security vulnerability?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Security Engineer, Agentic AI Engineer

**ANSWER:** Excessive agency means an agent has been granted more
autonomous capability (tool access, action scope) than its actual task
requires — a security risk even if every individual tool is itself
perfectly secure and bug-free, because a manipulated or
misjudging agent can misuse *legitimate* capability it never needed for
its stated purpose.

**SENIOR-LEVEL ANSWER:** This is the agent-specific instance of the
general least-privilege principle (per
`ai-engineering/mcp/security.md`), but worth naming distinctly because
it's easy to conflate with "is the tool secure" — a tool can be
flawlessly implemented and still represent excessive agency risk if
granted to an agent whose task never actually required it. The fix
isn't securing the tool further (there's nothing to fix in the tool
itself); it's narrowing what the *agent* is granted access to, per the
blast-radius bounding discussed in Q12.

**FOLLOW-UP QUESTIONS:**
- Give an example of a perfectly secure tool that still represents
  excessive agency risk when granted to a specific agent.
- How would you audit an existing agent's tool grants for excessive
  agency?
- How does this connect to the discovery-scoping defense-in-depth
  principle from the MCP domain?

**RED FLAGS:** Conflating "excessive agency" with "insecure tool" — they
require completely different fixes (narrow agent permissions vs. fix
the tool implementation).

---

### Q17. How would you design a rollback mechanism for an agent that's taken a sequence of actions and one turns out to be wrong?

**DIFFICULTY:** 🟠 Staff
**ROLE:** Agentic AI Engineer

**ANSWER:** True "undo" is only possible for actions with a defined
inverse operation — not every action is reversible (an email sent
can't be unsent). Design requires: distinguishing reversible from
irreversible actions upfront (informing the tiered-permission/approval
design from Q13), maintaining an explicit action log the rollback logic
can walk backward through, and defining an inverse operation for every
reversible action type at tool-design time, not improvised after the
fact.

**SENIOR-LEVEL ANSWER:** The harder case is a sequence where later
actions *depended on* an earlier action that now needs undoing — undoing
step 2 might invalidate steps 3-5's assumptions, not just step 2's
direct effect. This is genuinely the same cascading-dependency problem
distributed systems deal with in compensating transactions (the Saga
pattern) — an agent's action sequence with real rollback requirements
needs the same compensating-action design discipline, not an ad-hoc
per-incident undo attempt. For irreversible actions, the honest answer
is rollback isn't possible — which is exactly why irreversibility should
be a first-class input to the approval-tier decision in Q13, not
discovered only when something needs undoing.

**FOLLOW-UP QUESTIONS:**
- How would you design compensating actions for a specific multi-step
  agent task, concretely?
- What's the risk of an agent attempting to "fix" its own mistake
  autonomously rather than escalating?
- How does this connect to the general Saga pattern in distributed
  systems, and where does the analogy break down?

**RED FLAGS:** Assuming all agent actions are cleanly undoable — a
dangerously incomplete assumption that will eventually meet an
irreversible action with no plan.

---

### Q18. What's the relationship between an agent's temperature/sampling settings and its reliability for production use?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Engineer, Agentic AI Engineer

**ANSWER:** Higher temperature increases output randomness/creativity;
lower temperature (often near-zero) increases determinism/consistency.
For agentic tool-calling specifically, lower temperature is generally
preferred — you want consistent, predictable tool-call formatting and
argument generation, not creative variation in how the agent structures
a function call.

**SENIOR-LEVEL ANSWER:** The nuance: near-zero temperature isn't a
strictly "safer" choice in every dimension — it can make an agent more
prone to getting stuck in a repetitive, unproductive pattern (low
diversity in retry attempts after a failure, since it'll tend to
generate a very similar "fix" each time) compared to a small amount of
temperature giving retry attempts genuine variation. The practical
approach many production agents use: low temperature for the
tool-invocation/argument-generation step specifically (where format
consistency matters most), with slightly higher temperature reserved
for open-ended reasoning/planning steps where some exploration is
genuinely valuable.

**FOLLOW-UP QUESTIONS:**
- How would you diagnose whether a stuck/looping agent's problem is
  temperature-related versus a genuine logic/tooling issue?
- Would you use different temperature settings for different steps
  within the same agent's task, and how would you implement that?
- What's the reproducibility cost of using temperature above zero for
  evaluation/testing purposes specifically?

**RED FLAGS:** "Always use temperature zero for agents" as an absolute
rule without acknowledging the repetitive-stuck-loop trade-off.

---

### Q19. How would you design an agent's context window management for a task that genuinely requires more history than fits in one window?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Engineer, Context Engineering

**ANSWER:** Summarization/compression of older context (per
`ai-engineering/context-engineering/README.md`) is the standard
approach — periodically compress the older portion of the working
history into a denser summary, preserving recent detail at full
fidelity while older context degrades gracefully rather than being
abruptly truncated or silently dropped.

**SENIOR-LEVEL ANSWER:** Naive truncation (just dropping the oldest
messages when the window fills) risks silently losing task-critical
information established early in a long session — a much worse failure
mode than degraded-but-present summarized context, because truncation
gives no signal anything was lost. The engineering discipline: decide
deliberately what's compressible (routine intermediate steps) versus
what must be preserved at full fidelity regardless of age (the original
task specification, key constraints established early) — this is
exactly the context-contamination/compression concern named generally
in the context-engineering fundamentals question, applied specifically
to long-running agent sessions.

**FOLLOW-UP QUESTIONS:**
- How would you decide what's safe to summarize versus what must be
  preserved verbatim regardless of context pressure?
- What's the risk of summarization itself introducing subtle errors
  that compound over a long session?
- How would you test that your compression strategy doesn't lose
  task-critical information in practice?

**RED FLAGS:** Naive truncation (silently dropping oldest context) as
the context-management strategy, with no deliberate compression/
preservation design.

---

### Q20. What's the difference between evaluating an agent's final output and evaluating its full trajectory — why does this repository's evals guidance emphasize the latter?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Engineer, MLOps Engineer

**ANSWER:** Final-output evaluation only checks whether the end result
was correct. Trajectory evaluation checks the full sequence of
decisions/tool calls that produced that result — which tools were
called, in what order, with what reasoning.

**SENIOR-LEVEL ANSWER:** Per the model-upgrade regression question in
`ai-engineering/llmops-and-mlops/README.md`, a model upgrade can produce
a superficially similar correct final answer while taking a
meaningfully worse or riskier path to get there — output-only
evaluation completely misses this, since it only ever sees the
destination, not the route. This matters especially for the excessive-
agency and blast-radius concerns discussed in Q12/Q16 — an agent that
achieves the right answer via an unnecessarily broad, risky tool-call
pattern is a real regression even though output-only eval would score
it identically to a version that achieved the same answer more safely.

**FOLLOW-UP QUESTIONS:**
- How would you build automated trajectory evaluation, given
  "reasonable path" is harder to define than "correct answer"?
- What's the cost of trajectory evaluation versus output-only
  evaluation, and how would you justify the investment?
- How does this connect to the observability discussion in Q14 — is
  trajectory eval just replaying logged reasoning traces?

**RED FLAGS:** Relying solely on output-correctness metrics for agent
evaluation, missing the path-quality dimension entirely.

---

### Q21. How would you design a deployment/release process for an agent that safely handles a bad release without a full manual rollback?

**DIFFICULTY:** 🟠 Staff
**ROLE:** Agentic AI Engineer, MLOps Engineer

**ANSWER:** Canary/shadow deployment (per
`ai-engineering/llmops-and-mlops/README.md`), applied to agent releases
specifically — a new agent version runs on a small fraction of traffic
(or in shadow mode alongside the existing version, not affecting real
outcomes) with trajectory-level evaluation (Q20) comparing against the
existing version before full rollout.

**SENIOR-LEVEL ANSWER:** The agent-specific wrinkle beyond standard
canary deployment: because agent behavior is non-deterministic across
identical inputs (unlike a traditional deterministic service), a
canary comparison needs enough sample volume to distinguish a genuine
regression from normal run-to-run variation — a single bad-looking
trajectory in canary traffic isn't automatically a real regression
signal the way a single failed health check would be for a traditional
service. This requires statistically-aware canary analysis (similar in
spirit to the AnalysisRun pattern in
`kubernetes/troubleshooting.md` Lab 22), not a naive pass/fail on
individual canary samples.

**FOLLOW-UP QUESTIONS:**
- How would you determine sufficient canary sample size given agent
  non-determinism?
- What automated rollback trigger would you set, and how would you
  avoid both over- and under-sensitivity?
- How does this interact with the prompt-versioning discipline from Q11?

**RED FLAGS:** Treating agent canary analysis identically to
deterministic-service canary analysis, ignoring the non-determinism
that requires statistically-aware comparison instead of single-sample
pass/fail.

---

### Q22. What's the difference between an agent framework (LangGraph, CrewAI, etc.) and the underlying agentic principles this domain covers — how much does framework choice actually matter?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Engineer, Agentic AI Engineer

**ANSWER:** Frameworks provide implementation scaffolding (state
management primitives, graph/orchestration abstractions) for patterns
that exist independent of any specific framework — the underlying
principles (blast radius bounding, idempotency, observability,
evaluation) apply regardless of which framework implements them.

**SENIOR-LEVEL ANSWER:** Framework choice matters for development
velocity and ecosystem fit, but a team that picks a sophisticated
framework while skipping the underlying reliability/security principles
(Q8's iteration bounds, Q12's blast-radius design, Q17's rollback
planning) hasn't actually solved the hard problems this domain is about
— the framework handles orchestration mechanics, not judgment about
tool permissions, cost bounds, or evaluation rigor. Interviewers
generally care much more about whether a candidate understands these
underlying principles than which specific framework they've used,
precisely because frameworks change faster than the principles do.

**FOLLOW-UP QUESTIONS:**
- What would make you choose one agent framework over another for a
  specific project?
- How portable is your understanding of agent design if you had to
  switch frameworks tomorrow?
- What's a framework-specific footgun you've encountered that's really
  a violation of one of these underlying principles?

**RED FLAGS:** Deep framework-specific trivia knowledge with no
demonstrated understanding of the underlying reliability/security
principles that apply regardless of framework.

---

### Q23. How would you explain to a non-technical stakeholder why an "autonomous" agent still needs guardrails — doesn't autonomy mean it handles things itself?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Engineer, Agentic AI Engineer

**ANSWER:** Autonomy means the agent decides its own next actions
without a human choosing each step — it does *not* mean the agent is
infallible or should be trusted with unlimited capability. Guardrails
(per Q8, Q12) bound what can go wrong when the agent's autonomous
judgment is wrong, which happens with some non-zero, non-negligible
frequency for any current AI system.

**SENIOR-LEVEL ANSWER:** A useful analogy for a non-technical audience:
autonomous cruise control in a car handles routine driving decisions
without a human choosing every input, but the car still has guardrails
(lane-departure warnings, automatic braking, the driver's ability to
take back control) — autonomy in a bounded, guardrailed system, not
autonomy meaning "no oversight needed at all." The same framing applies
directly to AI agents.

**FOLLOW-UP QUESTIONS:**
- How would you extend this analogy to explain human-in-the-loop versus
  human-on-the-loop (Q13) to the same audience?
- What would you say if the stakeholder pushed back that guardrails
  defeat the purpose of "autonomous" AI?
- How would you measure and report on guardrail effectiveness to build
  stakeholder confidence over time?

**RED FLAGS:** A purely technical explanation with no accessible
analogy — fails the actual communication goal of translating the
concept for a non-technical audience.

---

### Q24. What's a concrete example of an agent design that looked reasonable in isolation but created a systemic risk once deployed alongside other agents in the same environment?

**DIFFICULTY:** 🟠 Staff
**ROLE:** Agentic AI Engineer, Staff Engineer

**ANSWER:** Multiple independently-designed agents, each individually
respecting reasonable per-agent rate limits/cost bounds, can
collectively overwhelm a shared downstream resource (a database, a
third-party API) that none of them individually appeared to threaten —
a systemic effect invisible from any single agent's own design review.

**SENIOR-LEVEL ANSWER:** This is the multi-agent-system equivalent of
the "noisy neighbor" resource-contention problem discussed for
Kubernetes CI runners (`kubernetes/senior-scenarios.md` S3), but harder
to catch because there's no shared infrastructure layer (like
Kubernetes ResourceQuota) automatically enforcing it — it requires
deliberate cross-agent capacity planning and shared rate-limiting
infrastructure (the per-tool rate limiting discussed in
`ai-engineering/mcp/fundamentals.md` Q18, applied at aggregate-across-
all-agents scope, not just per-identity) that individual agent
designers won't naturally think to build without organizational
awareness of the systemic risk.

**FOLLOW-UP QUESTIONS:**
- How would you design shared capacity governance across many
  independently-built agents in the same organization?
- How would you detect this systemic risk before it causes a real
  incident, given no single agent's design review would surface it?
- What organizational process (not just technical control) would help
  catch this earlier?

**RED FLAGS:** Reviewing agent designs purely in isolation, with no
consideration of aggregate/systemic effects across multiple
independently-deployed agents sharing infrastructure.

---

### Q25. If you had to name the single most important discipline for building production-reliable agentic systems, what would it be and why?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Agentic AI Engineer, Staff Engineer

**SENIOR-LEVEL ANSWER:** Treating non-determinism as the central design
constraint, not an inconvenience to work around — every principle
covered in this domain (bounded iteration, trajectory-level evaluation,
statistically-aware canary analysis, idempotent tools, staged trust
expansion) is ultimately a response to the same underlying fact: an
agent's behavior on the same input isn't guaranteed to be the same
twice, unlike traditional deterministic software. Teams that design
agentic systems using deterministic-software mental models (single-
sample testing, exact-output assertions, "it worked once so it's
correct") consistently under-invest in the actual controls this domain
needs. The teams that get this right start from "this system will
sometimes be wrong, in ways I can't fully predict — design accordingly"
rather than trying to eliminate non-determinism entirely, which isn't
achievable with current techniques.

**FOLLOW-UP QUESTIONS:**
- How would you convince a team used to deterministic software testing
  practices to adopt statistically-aware evaluation instead?
- What's a concrete example of a deterministic-software mental model
  causing a real problem when applied to an agentic system?
- How do you think this discipline will need to evolve as underlying
  models become more capable?

**RED FLAGS:** Naming a purely technical/framework answer instead of
the underlying epistemic shift (from deterministic to statistical
thinking) that actually differentiates reliable agentic system design.
