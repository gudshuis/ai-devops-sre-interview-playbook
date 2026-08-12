# MCP — Interview Questions

Broader interview-style questions, distinct from `fundamentals.md` (core
protocol mechanics) and `senior-scenarios.md` (open-ended platform
design).

---

## Question 01 — How would you explain MCP to a backend engineer who's never worked with LLMs, using an analogy they'd already understand?

**Difficulty:** 🟢 Beginner
**Roles:** AI Engineer, Backend Engineer

### Short answer
It's a standardized API contract between AI applications and tool/data
providers — the same value proposition as REST or gRPC standardizing
service-to-service communication, applied to "model talks to tools."

### Detailed answer
A backend engineer already understands why a shared API contract (REST,
gRPC, GraphQL) beats every service inventing its own bespoke integration
format — MCP is that same idea for the "AI application needs to call
tools/fetch context" problem specifically, with schema validation,
discovery, and authorization built into the standard.

### Production example
Comparing MCP's tool discovery to a service registry (like Consul) —
both let a consumer find available capabilities dynamically rather than
hardcoding endpoints.

### Trade-offs
The analogy isn't perfect — MCP's tool invocation is triggered by model
*reasoning*, not deterministic application code, which is the genuinely
new part a backend-engineering analogy alone doesn't fully capture.

### What a strong senior candidate should mention
Where the analogy breaks down (model-driven invocation) is itself a
good signal of understanding, not just reciting the comparison.

### Common weak answer
An analogy with no acknowledgment of where it stops applying.

### Follow-up questions
- What's genuinely new about MCP versus prior "AI function calling"
  patterns?
- How would you explain the authorization difference to that same
  engineer?

---

## Question 02 — What's your experience level with MCP, and what's a specific technical detail you had to learn the hard way?

**Difficulty:** 🔵 Intermediate
**Roles:** AI Engineer, AI Platform Engineer

### Short answer
Behavioral question — tests genuine hands-on experience versus
surface-level familiarity.

### Detailed answer
A strong answer names something specific and non-obvious (the tool-name
collision problem across multiple servers, the session-start-only
discovery timing, the stdio-vs-remote trust boundary distinction) rather
than a generic "I've used MCP."

### Production example
N/A — personal experience question.

### Trade-offs
N/A.

### What a strong senior candidate should mention
The specific debugging process that led to the discovery, not just the
fact learned.

### Common weak answer
A vague or textbook-sounding answer with no specific incident.

### Follow-up questions
- How did that change how you design MCP integrations now?
- What would you tell someone building their first MCP integration to
  watch out for?

---

## Question 03 — Compare MCP to LangChain's tool-calling abstraction. When would you use one over the other?

**Difficulty:** 🔵 Intermediate
**Roles:** AI Engineer, LLM Engineer

### Short answer
LangChain's tool abstraction is framework-internal and Python-specific;
MCP is a language-agnostic, cross-application protocol. Not mutually
exclusive — LangChain can consume MCP servers as one of its tool
sources.

### Detailed answer
The real distinction is portability and governance scope (per
`fundamentals.md` Q1) — a LangChain tool definition only works within
that specific application's process; an MCP server can be reached by
any compliant client, LangChain-based or not, and governed centrally at
the protocol boundary.

### Production example
A team building multiple AI applications (a Python backend, a separate
IDE plugin) standardized on MCP servers so both consumed the same tool
implementations, rather than reimplementing tool logic per framework.

### Trade-offs
For a single, simple, single-language application with no cross-app
reuse need, framework-native tool calling is lower overhead than
standing up a full MCP server.

### What a strong senior candidate should mention
That these operate at different layers (Q22 in fundamentals) — not
strictly competing options.

### Common weak answer
Declaring one strictly better without naming the actual use-case
difference.

### Follow-up questions
- Would you ever wrap an existing LangChain tool as an MCP server —
  what would that involve?
- How does this choice affect long-term maintainability as an
  organization's AI tooling grows?

---

## Question 04 — Tell me about a security concern you'd raise before connecting a new third-party MCP server to a production system.

**Difficulty:** 🟠 Senior
**Roles:** AI Security Engineer, AI Platform Engineer

### Short answer
Tool-description poisoning risk and data exposure via context/resources
— per `security.md`, connecting a third-party server is equivalent to
running untrusted third-party code.

### Detailed answer
Beyond "does the tool implementation do what it claims," the less
obvious risks are: what context/resources does this server's connection
expose to it (potential exfiltration even without any tool call), and
have the tool *descriptions* been reviewed for manipulative phrasing,
not just the code reviewed for malicious behavior.

### Production example
See `troubleshooting.md` Lab 6 — a real-shaped incident of exactly this
concern materializing via unreviewed auto-generated tool descriptions.

### Trade-offs
Full vetting takes real time/effort — balancing catalog breadth against
review rigor is a genuine platform trade-off (per `senior-scenarios.md`
S13's trust-tiering approach).

### What a strong senior candidate should mention
That code review alone doesn't catch tool-description manipulation risk
— a distinct review lens is needed.

### Common weak answer
Only mentioning standard supply-chain concerns (dependency
vulnerabilities) without the MCP-specific description-poisoning risk.

### Follow-up questions
- How would you design an automated first-pass screen before manual
  review?
- What would make you comfortable connecting a specific third-party
  server despite the general risk category?

---

## Question 05 — What's your opinion on MCP's decision to support both stdio and HTTP-based transports rather than a single unified one?

**Difficulty:** 🔵 Intermediate
**Roles:** AI Platform Engineer

### Short answer
The right call — the two transports serve genuinely different trust
models (local implicit trust vs. remote explicit auth), forcing one
would burden one use case or weaken the other.

### Detailed answer
See `fundamentals.md` Q20 for the full reasoning — a single-transport
spec would either force local tool integrations to carry unnecessary
network/auth overhead, or make remote enterprise services awkward to
secure properly.

### Production example
A local developer tool (stdio) versus an enterprise gateway (HTTP-based)
within the same organization — both are legitimate MCP use cases with
genuinely different requirements.

### Trade-offs
Supporting two transports does mean more implementation surface for
client libraries to cover — a real but justified cost.

### What a strong senior candidate should mention
A concrete example of when they'd choose each transport, not just
abstract agreement with the design choice.

### Common weak answer
No opinion or a purely theoretical answer with no grounding in a real
use case difference.

### Follow-up questions
- Could a single server support both transports — would that ever make
  sense?
- What would you want to see in a future MCP spec revision regarding
  transports?

---

## Question 06 — How would you convince a skeptical engineering leader that investing in an MCP gateway is worth the upfront cost versus letting teams build ad-hoc integrations?

**Difficulty:** 🟠 Senior
**Roles:** AI Platform Engineer, Staff Engineer

### Short answer
Frame it around governance/security debt avoided and integration-cost
reduction at scale — per `senior-scenarios.md` S7's migration reasoning,
in business terms.

### Detailed answer
Ad-hoc integrations feel cheaper per-team in the short term but
accumulate inconsistent security postures (no centralized authorization,
no consistent audit trail) and duplicated integration effort across
teams — the gateway's value compounds with team count, while ad-hoc
cost compounds too (just less visibly, until an incident or an audit
surfaces it).

### Production example
Reference the enterprise gateway case study's specific value points:
consistent authorization, centralized audit logging, and reduced
per-team integration effort.

### Trade-offs
The gateway has real upfront build cost and becomes a critical-path
dependency (per S14's scaling discussion) — a legitimate concern worth
acknowledging honestly, not dismissing.

### What a strong senior candidate should mention
Quantifying the trade-off in terms the leader cares about (risk,
velocity at scale) rather than purely technical elegance arguments.

### Common weak answer
A purely technical pitch with no business framing — unlikely to
persuade a skeptical non-technical or business-focused leader.

### Follow-up questions
- How would you propose piloting this to build the business case
  incrementally rather than asking for the full investment upfront?
- What metrics would you track to prove the investment paid off?

---

## Question 07 — What's a design decision in MCP's spec that you initially disagreed with but came to understand the reasoning for?

**Difficulty:** 🟠 Senior
**Roles:** AI Engineer, AI Platform Engineer

### Short answer
Behavioral/intellectual-honesty question — tests genuine engagement with
the spec's design trade-offs, not just surface familiarity.

### Detailed answer
A strong answer names something specific (e.g. session-start-only
discovery per Q7 in fundamentals, or the separation of tools from
sampling per Q11) with the actual reasoning that changed their mind, not
just agreement for its own sake.

### Production example
N/A — personal reflection question.

### Trade-offs
N/A.

### What a strong senior candidate should mention
What specifically changed their understanding — a concrete realization,
not vague agreement.

### Common weak answer
Claiming to have agreed with everything from the start, or genuine
disengagement with the spec's actual design trade-offs.

### Follow-up questions
- Is there anything in the spec you still have reservations about?
- How would you propose an improvement if you found a genuine gap?

---

## Question 08 — How would you test an MCP server's implementation before shipping it, beyond basic functional testing?

**Difficulty:** 🟠 Senior
**Roles:** AI Engineer, AI Platform Engineer

### Short answer
Schema-contract testing, adversarial/malformed-input testing, and
description-manipulation review — beyond happy-path functional tests.

### Detailed answer
Functional correctness alone misses the failure modes this whole domain
cares about: does the server correctly reject malformed arguments per
its own schema (not just accept anything), how does it behave under
concurrent/racing calls (per `troubleshooting.md` Lab 18), and have its
tool descriptions been reviewed for unintended model-influencing
phrasing (Q19 in fundamentals).

### Production example
A test suite that deliberately sends malformed/adversarial tool-call
arguments and confirms the server rejects them cleanly, rather than only
testing well-formed happy-path calls.

### Trade-offs
This level of testing is real additional effort versus basic functional
coverage — justified for anything beyond a purely internal,
low-stakes tool.

### What a strong senior candidate should mention
Testing for race conditions specifically (Lab 18) — an easy category to
overlook in typical test suites.

### Common weak answer
Only mentioning standard unit/integration testing with no MCP-specific
failure modes addressed.

### Follow-up questions
- How would you set up automated schema-contract testing in CI?
- How would you red-team a tool description for manipulation risk before
  shipping?

---

## Question 09 — What metrics would you want visible on an MCP gateway's operational dashboard?

**Difficulty:** 🔵 Intermediate
**Roles:** AI Platform Engineer, SRE

### Short answer
Per-server health/latency, per-identity authorization rejection rate,
tool-call volume/cost per team, and audit-log completeness — not just
generic uptime.

### Detailed answer
Beyond standard service health metrics, this domain specifically needs:
authorization-rejection rate (a spike signals either misconfiguration or
a security concern, per `troubleshooting.md` Lab 13), per-backend-server
health independent of gateway health (per the circuit-breaker isolation
scenario), and cost/usage attribution per team (per S8's budget-control
design).

### Production example
A dashboard that surfaced a single backend server's degraded latency
before it caused user-visible failures, because per-server (not just
aggregate) latency was tracked separately.

### Trade-offs
More granular metrics cost more to collect/store — worth it given the
gateway's critical-path role, per the general observability investment
reasoning applied throughout this repository.

### What a strong senior candidate should mention
The distinction between metrics for operational health versus metrics
for security/audit purposes — both matter, for different reasons.

### Common weak answer
Only generic infrastructure metrics (CPU, memory, request rate) with no
MCP-specific signals.

### Follow-up questions
- How would you set alerting thresholds for authorization-rejection
  rate specifically?
- What would you want visible during an active incident that isn't
  needed day-to-day?

---

## Question 10 — Describe how you'd approach code review for a pull request adding a new MCP tool.

**Difficulty:** 🔵 Intermediate
**Roles:** AI Engineer, AI Platform Engineer

### Short answer
Standard code review plus MCP-specific checks: schema strictness (Q8 in
fundamentals), description manipulation-risk review (Q19), risk
classification/tiering, and idempotency/retry-safety signaling (Q21).

### Detailed answer
A thorough review checks: is the input schema appropriately constrained
(not overly permissive), is the tool description free of directive-
sounding phrasing that could be interpreted as broader instructions, is
the tool correctly classified for its actual risk tier (read-only vs.
side-effecting), and does its response clearly signal retry-safety for
agentic callers.

### Production example
A review catching an under-constrained free-text parameter before merge,
avoiding both a reliability issue and a potential injection-adjacent
security gap.

### Trade-offs
This is a meaningfully more thorough review than typical code review —
justified by the specific risks this domain has (model-facing
descriptions, autonomous invocation).

### What a strong senior candidate should mention
Naming the specific additional review dimensions beyond standard code
correctness.

### Common weak answer
Describing only standard code review practices with no MCP-specific
considerations.

### Follow-up questions
- Who should be required reviewers for a new tool touching sensitive
  data?
- How would you build a review checklist that's actually followed
  consistently, not just aspirational?

---

## Question 11 — What's the hardest part of operating an MCP gateway in production, in your view?

**Difficulty:** 🟠 Senior
**Roles:** AI Platform Engineer, SRE

### Short answer
Balancing the authorization-cache-freshness/latency trade-off — real,
ongoing operational tension, not a one-time design decision.

### Detailed answer
Per the trade-off explicitly named in `senior-scenarios.md`'s original
design, this isn't solved once — it's an ongoing tuning exercise as
usage patterns and security requirements evolve, making it a genuinely
hard *operational* problem, not just a design decision made once at
launch.

### Production example
An incident where a stale authorization cache allowed access briefly
after revocation (`troubleshooting.md` Lab 11) illustrates the real
stakes of getting this tuning wrong.

### Trade-offs
N/A — the trade-off itself is the answer to this question.

### What a strong senior candidate should mention
That this requires ongoing attention, not a "solved and done" mindset.

### Common weak answer
A generic answer about "scaling is hard" with no specific operational
insight.

### Follow-up questions
- How would you monitor for authorization staleness proactively?
- What would you do differently if you were designing this from
  scratch, knowing what you know now?

---

## Question 12 — How would you handle a disagreement with another engineer about whether a tool should require human-in-the-loop approval?

**Difficulty:** 🟠 Senior
**Roles:** Agentic AI Engineer, AI Platform Engineer

### Short answer
Ground it in the risk-tiering framework (S9) — irreversibility and data
sensitivity should drive the decision, not opinion.

### Detailed answer
Per S9's risk-scored approval routing design, this shouldn't be a
binary per-tool-class opinion debate — the right resolution is applying
a consistent risk framework (transaction amount, reversibility, data
sensitivity) to the *specific* tool in question, letting the framework's
output settle the disagreement rather than either party's general
preference.

### Production example
A disagreement resolved by explicitly scoring the tool against agreed
risk criteria — the framework's output (not either engineer's initial
opinion) became the actual decision.

### Trade-offs
N/A — behavioral/process question.

### What a strong senior candidate should mention
The value of a documented, consistent framework for resolving this kind
of disagreement repeatably, not case-by-case debate every time.

### Common weak answer
A purely interpersonal answer with no technical framework grounding the
resolution.

### Follow-up questions
- What would you do if the framework itself is ambiguous for this
  specific case?
- How would you build organizational buy-in for the framework itself?

---

## Question 13 — What's a common misconception engineers have when they first start building MCP integrations?

**Difficulty:** 🔵 Intermediate
**Roles:** AI Engineer

### Short answer
That authorization can live in the prompt/model instructions — per
Q25 in fundamentals, this is the single most important misconception to
correct early.

### Detailed answer
New MCP builders frequently reach for "just tell the model not to call
that tool" as their security mechanism, not realizing (until a
prompt-injection incident, per `security.md`) that this isn't a real
control — enforcement must live in code the model can't reason around.

### Production example
A team's first MCP integration relied entirely on system-prompt
instructions to restrict tool access; a red-team exercise trivially
bypassed it, prompting a redesign around gateway-enforced authorization.

### Trade-offs
N/A.

### What a strong senior candidate should mention
Why this misconception is so common — prompt-based restriction feels
like it should work because it usually does in casual testing, until
someone actually tries to break it.

### Common weak answer
Naming a less consequential misconception (like a minor API detail)
instead of this foundational security misunderstanding.

### Follow-up questions
- How would you catch this misconception early in a code review?
- What other AI-specific security misconceptions have you seen?

---

## Question 14 — Describe a scenario where you'd deliberately choose NOT to use MCP for a given AI tool integration.

**Difficulty:** 🟠 Senior
**Roles:** AI Engineer, AI Platform Engineer

### Short answer
A single-use, throwaway prototype with no reuse/governance need — MCP's
overhead isn't justified for genuinely one-off, low-stakes experiments.

### Detailed answer
Per the general "don't adopt infrastructure without a genuine
requirement" principle applied throughout this repository — a quick
prototype exploring whether an AI feature is even worth building
doesn't need the discovery/schema/governance overhead MCP provides; a
direct, ad-hoc function call is faster to iterate on, with MCP adoption
deferred until the prototype proves out and genuinely needs the
portability/governance MCP offers.

### Production example
A hackathon prototype used direct function calling for speed; once it
was greenlit for production investment, the team migrated to a proper
MCP server as part of formalizing it.

### Trade-offs
Deferring MCP adoption means eventual migration cost if the prototype
succeeds — an acceptable trade for faster initial iteration speed.

### What a strong senior candidate should mention
That this is a deliberate, temporary choice with a clear migration
trigger, not a permanent decision to skip MCP.

### Common weak answer
"Always use MCP" with no situational judgment about when its overhead
isn't yet justified.

### Follow-up questions
- What would trigger you to migrate the prototype to a proper MCP
  server?
- How would you avoid the prototype accidentally becoming permanent,
  ungoverned infrastructure?

---

## Question 15 — How would you explain the tool-poisoning risk to a non-technical stakeholder who's skeptical it's a real concern?

**Difficulty:** 🟠 Senior
**Roles:** AI Security Engineer

### Short answer
Frame it as "the instructions could be malicious even if the code
isn't" — a concept most people intuitively grasp once stated plainly.

### Detailed answer
Use a concrete, relatable framing: imagine hiring a contractor whose
work is fine, but whose instruction manual for using their tool
secretly tells your employees to also do something harmful — the tool
itself passed inspection, but the *instructions for using it* didn't.
That's tool-description poisoning, translated out of technical jargon.

### Production example
Reference the real incident shape from `troubleshooting.md` Lab 6 as a
concrete "this actually happens" example, translated to non-technical
terms.

### Trade-offs
N/A — communication question.

### What a strong senior candidate should mention
A relatable analogy plus a concrete, non-hypothetical example — abstract
explanation alone often doesn't land with skeptical stakeholders.

### Common weak answer
Pure technical jargon with no translation for a non-technical audience —
fails the actual communication goal of the question.

### Follow-up questions
- How would you propose a mitigation to that same stakeholder in
  similarly accessible terms?
- What would convince them to fund the review process this risk
  requires?

---

## Question 16 — What's your process for staying current on MCP spec changes as the protocol evolves?

**Difficulty:** 🟢 Beginner / 🔵 Intermediate
**Roles:** All AI engineering roles

### Short answer
Official spec changelog as primary source, plus hands-on testing of
changes against real integrations before broad adoption.

### Detailed answer
Given MCP is a relatively young, actively-evolving protocol, tracking
the official spec repository's changes directly (not just secondhand
summaries) and testing new capabilities in a sandboxed environment
before depending on them in production is the disciplined approach —
mirrors the general "verify against authoritative sources" principle
this repository emphasizes throughout.

### Production example
N/A — process question.

### Trade-offs
N/A.

### What a strong senior candidate should mention
Distinguishing spec-level changes from client-library-level changes —
both matter but require different tracking.

### Common weak answer
"I read blog posts about it" — secondhand summaries can lag or
misrepresent actual spec changes.

### Follow-up questions
- How would you evaluate whether a new spec capability is stable enough
  to adopt in production?
- How do you communicate spec changes to a broader team that isn't
  tracking them as closely?

---

## Question 17 — What would you do if you discovered, after shipping, that a tool you built has a schema design flaw that's causing real reliability issues?

**Difficulty:** 🟠 Senior
**Roles:** AI Engineer, AI Platform Engineer

### Short answer
Follow the versioning discipline from Q12 in fundamentals — never patch
in-place if clients may have cached the old schema; ship a new version.

### Detailed answer
Even under pressure to fix quickly, an in-place breaking schema change
risks breaking every client that cached the flawed schema at session
start — the disciplined fix is a new tool version (or additive-only
patch if the fix can be expressed that way) with a proper migration
path, not a rushed in-place change.

### Production example
Reference `troubleshooting.md` Lab 4's exact failure mode as what
happens when this discipline isn't followed.

### Trade-offs
The disciplined fix takes longer to fully roll out than an in-place
change — worth it to avoid breaking existing clients unpredictably.

### What a strong senior candidate should mention
Resisting the pressure to "just patch it fast" when a fast patch would
itself cause a different class of incident.

### Common weak answer
Proposing an immediate in-place fix without acknowledging the
breaking-change risk to existing clients.

### Follow-up questions
- How would you communicate the issue and the fix timeline to affected
  teams?
- How would you prevent this class of flaw from reaching production
  again?

---

## Question 18 — How do you approach estimating the effort to build a new MCP server integration for an unfamiliar backend system?

**Difficulty:** 🔵 Intermediate
**Roles:** AI Engineer, AI Platform Engineer

### Short answer
Understand the backend's actual API/auth model first, then map to MCP
primitives — most estimation risk is in the backend integration, not the
MCP layer itself.

### Detailed answer
The MCP-specific work (defining tools/resources, schema design) is
usually the smaller, more predictable part; the larger unknown is
understanding the backend system's own quirks (rate limits, auth
complexity, data model) — accurate estimation requires investigating
the backend first, not assuming MCP-layer work dominates the timeline.

### Production example
An estimate that assumed MCP-layer work would dominate turned out
wrong once the backend's undocumented rate-limiting behavior was
discovered mid-implementation — the actual bottleneck was backend
integration complexity, not MCP tooling.

### Trade-offs
N/A.

### What a strong senior candidate should mention
Explicitly separating "MCP-layer effort" from "backend-integration
effort" in the estimate, rather than treating it as one undifferentiated
task.

### Common weak answer
A single, undifferentiated time estimate with no accounting for backend-
specific unknowns.

### Follow-up questions
- How would you de-risk the estimate before committing to a timeline?
- What would you do if the backend turns out to have no good API at
  all, only a legacy interface?

---

## Question 19 — What's your view on whether every internal API should eventually be exposed via MCP, or whether that's over-application of the pattern?

**Difficulty:** 🟠 Senior
**Roles:** AI Platform Engineer, Staff Engineer

### Short answer
No — only APIs a model genuinely needs to reason about invoking
autonomously; not every internal API is a good MCP tool candidate.

### Detailed answer
MCP's value is specifically for *model-driven* invocation — an API a
human-driven application calls deterministically doesn't benefit from
being wrapped as an MCP tool just because MCP exists; the actual test is
whether an AI agent genuinely needs to decide, autonomously, when and
how to call it.

### Production example
A team considered wrapping every internal microservice as an MCP tool
"for consistency," then recognized most had no genuine AI-driven use
case and scoped back to only the APIs actual AI features needed.

### Trade-offs
Under-exposing APIs limits future AI feature flexibility; over-exposing
adds unnecessary catalog bloat, review overhead (per Q19 in
fundamentals), and unused attack surface.

### What a strong senior candidate should mention
The specific test (does a model need to autonomously decide to invoke
this) rather than a blanket "expose everything" or "expose nothing"
stance.

### Common weak answer
"Yes, expose everything for future flexibility" — ignores the real
review/security overhead of a bloated tool catalog.

### Follow-up questions
- How would you decide when a previously-not-exposed API should become
  an MCP tool?
- What's the maintenance cost of an unused, over-broadly-exposed tool
  catalog?

---

## Question 20 — Walk me through how you'd explain MCP's value proposition to a CFO evaluating whether to fund a platform investment in it.

**Difficulty:** 🟠 Senior
**Roles:** AI Platform Engineer, Staff Engineer

### Short answer
Frame around risk reduction (governance, security) and velocity at
scale (avoided duplicated integration effort across teams) in financial
terms, not technical elegance.

### Detailed answer
A CFO cares about risk exposure and cost efficiency — translate "MCP
gateway" into "avoids N teams each independently building and securing
their own AI-tool integrations, with inconsistent security posture that
creates real breach/compliance risk exposure," and "reduces the
marginal cost of each new AI feature needing tool access."

### Production example
A cost/risk comparison showing the aggregate cost of N teams' duplicated
ad-hoc integration efforts versus one centrally-maintained gateway,
alongside the risk cost of inconsistent security posture across N
independent implementations.

### Trade-offs
Acknowledge honestly that this is an upfront investment with returns
that compound over time and team count — not an immediate cost
reduction in year one.

### What a strong senior candidate should mention
Concrete, quantifiable framing (even rough estimates) rather than
purely qualitative arguments — CFOs respond to numbers.

### Common weak answer
A purely technical pitch with no financial/risk translation — unlikely
to land with a CFO audience.

### Follow-up questions
- How would you measure and report back on the investment's actual
  return?
- What would make you recommend against this investment for a smaller
  organization?

---

## Question 21 — What's the difference in how you'd design an MCP integration for an internal tool versus one that will eventually be customer-facing?

**Difficulty:** 🟠 Senior
**Roles:** AI Platform Engineer, AI Security Engineer

### Short answer
Trust model inversion — per `senior-scenarios.md` S20, customer-facing
means treating every caller as untrusted-by-default from day one, not
retrofitting that assumption later.

### Detailed answer
Designing "internal-first, harden for external later" tends to miss
assumptions baked in early (a shared internal-trust default that's hard
to fully unwind) — if customer-facing use is even a plausible future
direction, designing with per-customer isolation and strict catalog
scoping from the start avoids a much harder retrofit later.

### Production example
A tool built assuming internal-employee trust required a significant
redesign (not just a config change) when a customer-facing use case
emerged later — isolation assumptions were baked into the original
design in ways that were hard to unwind.

### Trade-offs
Designing for the stricter customer-facing trust model from the start
costs more upfront even if the immediate use case is internal-only —
worth it only if external use is a genuine, non-speculative future
possibility.

### What a strong senior candidate should mention
Not over-engineering for a purely hypothetical future external use case
either — this is a judgment call informed by actual product roadmap, not
a default to always design for the strictest case.

### Common weak answer
Treating internal and customer-facing designs as interchangeable with
"add auth later" as a sufficient plan.

### Follow-up questions
- How would you decide whether a given internal tool is a plausible
  future customer-facing candidate?
- What's the cost of over-designing for external use that never
  materializes?

---

## Question 22 — How would you handle a situation where a business stakeholder wants to bypass your MCP gateway's authorization for "just this one urgent request"?

**Difficulty:** 🟠 Senior
**Roles:** AI Platform Engineer, AI Security Engineer

### Short answer
Push back on bypassing the control itself; find the fast, legitimate
path within the system (an expedited approval, a scoped emergency
grant) instead.

### Detailed answer
"Just this once" bypass requests are exactly how authorization controls
erode over time — the right response isn't a flat "no" that ignores the
genuine urgency, but redirecting to a legitimate fast-path (an
expedited, still-logged, still-scoped emergency access grant) that
preserves the control's integrity while addressing the real time
pressure.

### Production example
A genuine incident-response need was served through a pre-defined
emergency-access procedure (logged, time-bound, narrowly scoped) rather
than disabling authorization checks outright — the urgency was real, the
bypass request itself wasn't the right mechanism to address it.

### Trade-offs
Building a legitimate fast-path requires upfront design investment
before the urgent moment arrives — worth having ready rather than
improvising a bypass under pressure.

### What a strong senior candidate should mention
The distinction between "the request is genuinely urgent" (often true)
and "bypassing the control is the right response to that urgency"
(usually not) — and having a pre-built alternative ready.

### Common weak answer
Either an inflexible "policy says no" with no path forward, or actually
disabling the control under pressure — both are real failure modes this
question probes for.

### Follow-up questions
- How would you design that emergency-access fast-path in advance?
- How would you handle it if this becomes a recurring pattern from the
  same stakeholder?

---

## Question 23 — What's a question you'd ask a candidate to distinguish someone who's actually built production MCP integrations from someone who's only read about MCP?

**Difficulty:** 🟠 Senior
**Roles:** AI Platform Engineer, Hiring Manager-adjacent

### Short answer
Ask about a specific failure mode they debugged (a race condition, a
schema-versioning incident, an authorization-staleness issue) — genuine
experience produces specific, mechanistic answers; reading-only
knowledge produces generic ones.

### Detailed answer
The Labs in `troubleshooting.md` are exactly the shape of question that
distinguishes real operational experience — someone who's actually run
an MCP integration in production can describe a *specific* incident with
*specific* evidence and a *specific* fix; someone who's only read the
spec can describe the theory but not a lived debugging experience.

### Production example
N/A — meta/interviewing question.

### Trade-offs
N/A.

### What a strong senior candidate should mention
That genuine specificity (not just correctness) is the signal to listen
for.

### Common weak answer
A question that only tests spec knowledge (definitions) rather than
operational experience.

### Follow-up questions
- What other domains would you apply this same "ask for a specific
  incident" interviewing technique to?
- How would you calibrate for a candidate who's genuinely skilled but
  worked at a company where they simply haven't hit certain failure
  modes yet?

---

## Question 24 — How would you design an internal training/enablement program to get 200 engineers proficient in building MCP tools safely?

**Difficulty:** 🟠 Senior
**Roles:** AI Platform Engineer, Developer Experience

### Short answer
Hands-on, failure-mode-first training (mirroring this repository's own
`challenges.md` philosophy) paired with a golden-path template — not
purely documentation-based onboarding.

### Detailed answer
Per the general onboarding-effectiveness reasoning in
`kubernetes/questions.md` Q16, purely passive documentation doesn't
build the safety instincts this domain specifically needs (schema
design discipline, description-review awareness, authorization
principles) — a hands-on exercise walking through a deliberately-flawed
tool (an under-constrained schema, a description with manipulation-risk
phrasing) and having engineers find and fix the issues themselves builds
much more durable competence.

### Production example
A training exercise modeled on `challenges/debug-this/` — engineers
investigate a pre-built, intentionally-flawed MCP tool before comparing
against the documented fix.

### Trade-offs
Building genuinely hands-on training material is a real upfront
investment versus writing documentation alone — justified at 200-
engineer scale where the leverage is high.

### What a strong senior candidate should mention
Connecting the training design to this repository's own pedagogical
approach (learn by debugging, not just reading) as a validated pattern.

### Common weak answer
"Write comprehensive documentation" with no hands-on component.

### Follow-up questions
- How would you measure whether the training actually improved tool
  quality in practice?
- How would you keep training material current as the platform evolves?

---

## Question 25 — Looking forward, what do you think is the biggest unsolved problem in the MCP ecosystem right now?

**Difficulty:** 🟠 Senior
**Roles:** AI Platform Engineer, AI Security Engineer

### Short answer
Reliable, automated detection of tool-description manipulation/
poisoning — currently relies heavily on human review, which doesn't
scale to a large, growing tool catalog.

### Detailed answer
Per Q1 in `security.md`, tool poisoning is a natural-language problem
wearing a supply-chain costume — traditional automated security scanning
(signature/vulnerability-based) doesn't address it, and human review
doesn't scale to hundreds or thousands of tools across a growing
ecosystem. This is a genuinely open problem, not a solved one, and a
candidate who names it (rather than claiming everything's solved) is
showing real, current engagement with the domain's actual frontier.

### Production example
N/A — forward-looking/opinion question.

### Trade-offs
N/A.

### What a strong senior candidate should mention
Honest acknowledgment of an unsolved problem, ideally with a plausible
direction for progress (e.g. LLM-based description scanning as an
imperfect but scalable first pass) rather than overclaiming a solved
state.

### Common weak answer
Claiming everything about MCP security is already solved — signals
either inexperience with the domain's real edges or overconfidence.

### Follow-up questions
- What approach would you take to build automated detection for this,
  even an imperfect first version?
- What other genuinely unsolved problems do you see in the broader AI
  security space?
