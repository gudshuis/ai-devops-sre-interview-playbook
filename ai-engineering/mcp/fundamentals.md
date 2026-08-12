# MCP — Fundamentals

---

### Q1. What problem does MCP actually solve that a normal REST API integration doesn't?

**DIFFICULTY:** 🟢 Beginner
**ROLE:** AI Engineer, AI Platform Engineer, LLM Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand MCP as a
*standardization* layer, not "yet another API format" — a common shallow
misconception.

**ANSWER:** Before a shared protocol, every application that wanted to
give a model access to tools/data built its own bespoke integration layer
— every combination of (model application) × (data source/tool) needed
custom glue code. MCP standardizes that connection: an MCP **server**
exposes tools/resources/prompts in one consistent way; any MCP **client**
(embedded in a model-serving application) can consume any MCP server
without custom per-integration code. It's the same "M×N becomes M+N"
value proposition as protocols like LSP did for editors/language servers.

**SENIOR-LEVEL ANSWER:** The real production value isn't just reduced
integration code — it's that tool/context access becomes **governable at
one layer** instead of scattered across every application's custom
integration. Once tool access goes through MCP servers uniformly, you can
apply authorization, logging, rate-limiting, and auditing consistently at
the protocol boundary, rather than trusting each application team to
implement those controls correctly in their own bespoke integration code.
This matters more than the developer-convenience framing suggests — see
[security.md](security.md) for what happens when that governance layer is
skipped.

**FOLLOW-UP QUESTIONS:**
- What's the difference between an MCP "tool" and an MCP "resource"?
- Why does MCP define "prompts" as a first-class primitive, not just
  tools/resources?
- What transports does MCP support, and when would you choose each?

**RED FLAGS:** Describing MCP as "just a wrapper around REST" without
mentioning the standardization/governance value.

---

### Q2. Explain the difference between MCP's `tools`, `resources`, and `prompts` primitives.

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Engineer, LLM Engineer

**ANSWER:**
- **Tools**: model-invokable functions with defined input schemas — the
  model decides when to call them, with what arguments, based on the
  conversation.
- **Resources**: application-provided context data (files, database rows,
  API responses) that can be attached to a conversation — typically
  surfaced to the *user* or application to select, rather than the model
  autonomously deciding to fetch them the way it does with tools.
- **Prompts**: reusable, parameterized prompt templates the server exposes
  — a way for a server to package "the right way to ask about X" rather
  than every client reinventing prompt wording for a given integration.

**SENIOR-LEVEL ANSWER:** The tools-vs-resources distinction is really
about **who's in control of the fetch**: tools put the model in the
decision loop (autonomous, harder to fully predict), while resources are
typically explicit/user-driven inclusion. This has real security and cost
implications — tools are where prompt-injection-driven unintended actions
actually happen (see [security.md](security.md)), because the model is
the one deciding to invoke them based on text it's read, potentially
including untrusted text. Designing a server's primitives with that
distinction in mind — putting genuinely autonomous, side-effecting actions
behind tools with tight scoping, and keeping read-only/context-only data
behind resources — is a real architectural decision, not just picking
whichever primitive is more convenient to implement.

**FOLLOW-UP QUESTIONS:**
- Would you expose a "delete a record" capability as a tool? What
  safeguards would you want around that specifically?
- How does a client discover what tools/resources/prompts a server
  exposes?
- What's the risk of a tool's input schema being too permissive?

**RED FLAGS:** Treating all three primitives as interchangeable "ways to
give the model data."

---

### Q3. What transports does MCP support, and what determines the choice between them?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Platform Engineer, AI Infrastructure Engineer

**ANSWER:** Local, same-machine integrations typically use **stdio**
(the server is a subprocess the client launches and communicates with over
stdin/stdout) — simple, no network exposure, appropriate for a developer
running a tool locally. Remote/networked integrations use an
**HTTP-based transport** (with streaming for server-initiated messages),
appropriate for enterprise deployments where the MCP server is a shared
service, not a local subprocess.

**SENIOR-LEVEL ANSWER:** The transport choice is really a **trust boundary
decision**. stdio implicitly trusts "whatever's on this machine that I
chose to launch" — fine for a developer's local tool, completely wrong for
"any employee's AI assistant can reach this server." A remote HTTP-based
MCP server crossing that boundary needs everything a normal
network-exposed service needs — authentication (who is this client),
authorization (what can this specific client do), and transport security
— none of which stdio has to think about because the boundary (a local
process launch) provides those guarantees implicitly. The mistake I'd
flag as a red flag in a review: standing up a "remote MCP server" by
just exposing what was originally a stdio-oriented local tool over HTTP
without adding the authn/authz layer that crossing that trust boundary
actually requires.

**FOLLOW-UP QUESTIONS:**
- How would you authenticate a remote MCP client — what's the equivalent
  of an API key/OAuth flow in an MCP context?
- What's the blast radius difference between a compromised stdio server
  and a compromised remote MCP server?
- How would you rate-limit or sandbox a remote MCP server serving many
  concurrent enterprise users?

**RED FLAGS:** Not recognizing that stdio's security model relies entirely
on "this is running as a local subprocess I launched," which doesn't
transfer to a remote deployment at all.

---

### Q4. What's the difference between an MCP "tool" and simply exposing a REST endpoint the model happens to know about via prompt instructions?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Engineer, LLM Engineer

**ANSWER:** Functionally, both let a model trigger external actions. The
difference is **structure and discoverability**: an MCP tool has a
formally defined, machine-readable input schema that the client validates
against before invocation, and is dynamically discoverable by any
compliant client without prior hardcoded knowledge — a REST endpoint
described only in a prompt has no schema enforcement (the model can send
malformed arguments that only fail at the API layer, not before) and
isn't discoverable by anything other than that specific prompt's authors.

**SENIOR-LEVEL ANSWER:** The schema-validation distinction has a real
reliability consequence: with a defined MCP tool schema, a malformed
tool-call attempt can be caught and rejected by the *client* before ever
reaching the actual backend service, often triggering a clear, structured
error the model can self-correct from. A prompt-described REST call has
no such gate — malformed calls reach the real backend, potentially
causing partial side effects before failing, or failing with an
unstructured error the model can't reliably parse and recover from. At
scale (many tools, many models, many client applications), the
discoverability property matters more than it seems: it's what makes the
governed-gateway pattern in `senior-scenarios.md` possible at all —
tools can be added/removed centrally without every client needing
prompt-level updates.

**FOLLOW-UP QUESTIONS:**
- How does schema validation change what a client can safely retry
  automatically versus what needs to surface back to the user?
- What's lost, if anything, by using MCP's structured tool definition
  instead of a more flexible, less-structured prompt-based approach?
- How would you migrate an existing prompt-described-endpoint integration
  to a proper MCP tool?

**RED FLAGS:** Treating "the model can call an API" and "this is
implemented as an MCP tool" as equivalent — the schema/discoverability
properties are the entire point, not an implementation detail.

---

### Q5. What are MCP "resources," concretely, and how does a client decide when to include one in a conversation?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Engineer

**ANSWER:** A resource is a unit of context a server exposes (a file, a
database row, an API response) that can be attached to a conversation,
identified by a URI the server defines. Unlike tools (model-invoked,
autonomous), resources are typically **explicitly selected** — by the
user, or by the client application's own logic — rather than
autonomously fetched by the model mid-conversation.

**SENIOR-LEVEL ANSWER:** The explicit-selection property is a genuine
design choice, not an arbitrary spec limitation — it keeps a category of
context inclusion under deterministic, auditable control (a user
explicitly attached this specific file) separate from the
harder-to-fully-predict category of autonomous tool-driven context
gathering. This matters for both cost control (resources aren't fetched
speculatively the way an over-eager tool-calling model might) and for
the security reasoning in `security.md` — resource inclusion has a
clearer provenance trail than a model's own decision to call a
data-fetching tool mid-conversation.

**FOLLOW-UP QUESTIONS:**
- Could a client application choose to auto-attach certain resources
  without explicit per-instance user selection — would that undermine
  the provenance benefit described above?
- How would resource URIs be structured for a server exposing a large,
  hierarchical document set?
- What's the practical context-window cost consideration when a resource
  is large (e.g. an entire codebase file)?

**RED FLAGS:** Conflating resources and tools as interchangeable — the
explicit-vs-autonomous distinction has real security and cost
implications covered elsewhere in this domain.

---

### Q6. What's an MCP "prompt" (the primitive), and why would a server want to define one rather than letting the client/application author its own prompts?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Engineer

**ANSWER:** An MCP prompt is a reusable, parameterized prompt template a
server exposes — packaging "the right way to ask about this server's
domain" as a first-class, versioned artifact the server owns, rather than
leaving every client application to independently reverse-engineer
effective prompting for that server's tools/resources.

**SENIOR-LEVEL ANSWER:** This matters most for servers with genuinely
non-obvious best practices for using their own tools effectively — e.g. a
server exposing a complex query tool where prompt wording significantly
affects query quality. Without server-defined prompts, that domain
expertise lives scattered across every client application's own prompt
engineering, inconsistently, and improvements to prompting strategy don't
propagate — a client stuck on an old prompt approach doesn't benefit when
the server owner discovers a better one. With server-defined prompts,
that expertise is centralized and versioned exactly like tool
definitions, so an improvement to the prompt template benefits every
client using it, consistent with the "consistency across many
integrations" value proposition from Q1.

**FOLLOW-UP QUESTIONS:**
- How would prompt versioning work if a server improves its prompt
  template — do existing client sessions need to migrate?
- When would a client legitimately want to override a server-provided
  prompt rather than use it as-is?
- How does this interact with context engineering more broadly (per
  `ai-engineering/context-engineering/README.md`)?

**RED FLAGS:** Not recognizing prompts as a distinct, deliberate MCP
primitive — conflating them with tools or treating them as an optional
afterthought rather than genuine, centralized prompt-engineering
ownership.

---

### Q7. How does an MCP client actually discover what capabilities (tools/resources/prompts) a server offers, and when does that discovery happen?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Engineer, AI Platform Engineer

**ANSWER:** On connection, an MCP client and server perform an
initialization handshake where the server advertises its capabilities —
which primitive types it supports and (for tools specifically) their
schemas. This happens at **session start**, not per-message — a client
doesn't re-discover the full capability set on every single interaction.

**SENIOR-LEVEL ANSWER:** The session-start-only discovery timing has a
real operational consequence directly relevant to the gateway design in
`senior-scenarios.md` S2: if a tool's availability changes *during* an
active session (a permission is revoked, or a new tool is added), a
client that already completed discovery won't automatically see that
change until its next fresh session/reconnection, unless the
implementation specifically supports a re-discovery or push-notification
mechanism. This is exactly the staleness gap named as a real production
risk in the gateway authorization discussion — session-start-only
discovery and authorization-cache staleness are two instances of the
same underlying problem (a security/capability boundary that only
refreshes at defined checkpoints, not continuously).

**FOLLOW-UP QUESTIONS:**
- How would you design a system to push capability changes to already-
  connected clients rather than waiting for reconnection?
- What's the trade-off of re-running discovery on every single
  interaction instead of once per session?
- How does this affect a long-running agent session versus a short,
  human-driven interactive session?

**RED FLAGS:** Assuming capability changes take effect instantly for
already-connected clients — misses the session-start discovery timing
and its staleness implications.

---

### Q8. What's the risk of an MCP tool's input schema being "too permissive" (e.g. accepting a free-text string where a constrained enum would be more appropriate)?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Engineer, AI Security Engineer

**SENIOR-LEVEL ANSWER:** A permissive schema pushes validation
responsibility from the **protocol/client layer** (where a schema
mismatch is caught cheaply, before any backend call) to the **backend
service itself** (where an invalid or unexpected value is only caught
after the call is made, potentially after side effects have already
started) — the same "catch it as early and cheaply as possible" principle
that applies broadly in software engineering, applied specifically to
tool-call validation. Beyond correctness, this has a real security
dimension: a free-text field where a constrained set of valid values
would suffice is a larger surface for injection-style attacks (per
`security.md`) — a tightly-scoped enum simply has no room for an injected
instruction to hide in, while a free-text field does. Schema design is
therefore a genuine security control, not just an API-design nicety.

**FOLLOW-UP QUESTIONS:**
- Give a concrete example of a tool where a permissive schema created a
  real security or reliability gap that a tighter schema would have
  closed.
- How would you retrofit a tighter schema onto an existing tool without
  breaking clients that depend on the looser one?
- What's the trade-off of an overly restrictive schema — can tightening
  go too far?

**RED FLAGS:** Treating schema strictness as purely a data-quality
concern with no security dimension.

---

### Q9. Two different MCP servers both expose a tool named `search`. How does a client/model distinguish between them, and what confusion can arise if it doesn't?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Engineer, AI Platform Engineer

**SENIOR-LEVEL ANSWER:** Tool identity in a multi-server client
connection needs to be **namespaced by server**, not just by tool name
alone — most real implementations qualify a tool's effective identity by
its originating server (e.g. `serverA.search` vs. `serverB.search`)
specifically to avoid this collision. If a client/gateway implementation
gets this wrong (flattening tool names without server-scoped
namespacing), the practical failure mode is a model correctly deciding
"I should call `search`" but the *wrong* underlying server's `search`
tool actually being invoked — a class of bug that's especially dangerous
if one server's `search` is read-only and another's has side effects, or
if one is scoped to public data and another to sensitive internal data.
This connects directly to the gateway tool-discovery design in
`senior-scenarios.md` — per-identity scoped discovery needs to preserve
server-origin disambiguation, not just present a flattened tool list.

**FOLLOW-UP QUESTIONS:**
- How would you design tool naming/namespacing for a gateway aggregating
  dozens of MCP servers, to keep names both disambiguated and usable by
  the model?
- What's the risk if two servers' tools have the same name AND similar
  (but subtly different) semantics, not just a naming collision?
- How would you test for this class of bug before it causes a real
  production incident?

**RED FLAGS:** Assuming tool names are inherently unique across an
entire multi-server integration without describing an actual
namespacing/disambiguation mechanism.

---

### Q10. What's the operational difference between an MCP server crashing versus an MCP server hanging (never responding) from the calling client's perspective?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Platform Engineer, SRE

**ANSWER:** A crashed server produces an immediate, detectable connection
failure the client can react to (retry, fail fast, surface an error). A
hanging server produces **no signal at all** — the client is left waiting
indefinitely unless it has its own timeout configured, since nothing
about the connection itself indicates failure.

**SENIOR-LEVEL ANSWER:** This is the same fail-open-vs-fail-closed,
timeout-discipline reasoning that shows up throughout distributed systems
generally (and specifically in the admission-webhook hang scenario in
`kubernetes/troubleshooting.md` Lab 13) — a hanging dependency without an
enforced timeout doesn't just delay one request, it can exhaust a
client's own limited concurrency/connection pool waiting on a server that
will never respond, degrading unrelated requests that have nothing to do
with the hung server. Every MCP client integration needs an explicit,
deliberately-chosen timeout on tool invocations — treating "the server
will eventually respond" as a safe assumption is the exact failure mode
this question tests for.

**FOLLOW-UP QUESTIONS:**
- How would you choose an appropriate timeout value for a tool call,
  given some legitimate operations may genuinely take a while?
- What should the client/gateway do when a timeout is hit — retry, fail
  the request, something else?
- How does this interact with circuit-breaking for a consistently slow/
  unreliable MCP server?

**RED FLAGS:** No mention of timeouts at all when discussing tool-
invocation reliability — an unbounded wait on an external dependency is a
classic, well-known failure mode this question is specifically probing
for.

---

### Q11. Why does the MCP spec separate "tools" from "sampling" (a server requesting the client's LLM to generate something on the server's behalf)?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Engineer, AI Platform Engineer

**ANSWER:** Tools flow **model → server** (the model decides to invoke
server-side functionality). Sampling flows the opposite direction —
**server → model** — letting a server request that the client's LLM
generate content on the server's behalf, without the server needing its
own separate model access/credentials.

**SENIOR-LEVEL ANSWER:** This inversion exists to solve a real practical
problem: without sampling, any MCP server wanting LLM-generation
capability as part of its own logic would need to independently
integrate with (and pay for, and manage credentials for) an LLM provider
itself — duplicating what the client already has. Sampling lets a server
borrow the client's existing model access instead. The security
implication worth naming: a sampling request is the server asking the
*client* to run inference — the client should apply the same scrutiny to
a sampling request's content as to any other externally-supplied input
influencing a model call, since a malicious server could use sampling
requests to attempt various forms of manipulation via the generation it's
requesting, not just via tool results.

**FOLLOW-UP QUESTIONS:**
- What controls would you want a client to apply before honoring a
  server's sampling request?
- Why might a client choose to reject or heavily restrict sampling
  requests from certain servers?
- How is this different from the server just calling its own separate
  LLM API directly?

**RED FLAGS:** Not recognizing sampling as a genuinely different data-
flow direction from tools — treating it as "just another kind of tool
call."

---

### Q12. How would you version an MCP tool's schema over time without breaking clients that cached an older version?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Platform Engineer

**SENIOR-LEVEL ANSWER:** The safe pattern mirrors general API versioning
discipline: **additive, backward-compatible changes** (a new optional
parameter with a sensible default) can ship without breaking existing
clients at all. **Breaking changes** (removing a parameter, changing a
type, changing required-vs-optional) need either a new tool name/version
(`search_v2` alongside `search`, with `search` eventually deprecated on
its own timeline) or a coordinated migration — never an in-place breaking
change to an existing tool name that active clients may have cached
schemas for. This directly parallels the CRD versioning/conversion
concern in `kubernetes/fundamentals.md` Q20 — the same "existing consumers
may be relying on the old shape" problem, in a different protocol.

**FOLLOW-UP QUESTIONS:**
- How would you detect which clients are still using an old tool version,
  to know when it's safe to fully deprecate it?
- What's the cost of maintaining two versions of the same tool
  simultaneously during a migration window?
- How does the session-start-only discovery timing (Q7) affect how
  quickly a schema change actually reaches active clients?

**RED FLAGS:** Proposing an in-place breaking change to an existing
tool's schema without any versioning/migration strategy — directly
breaks any client that cached the old schema at session start.

---

### Q13. What does "remote MCP" mean, and how does authentication for a remote MCP server typically differ from a local stdio server?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Platform Engineer

**ANSWER:** Remote MCP refers to servers reached over a network transport
(HTTP-based) rather than launched as a local subprocess. Since there's no
implicit "I launched this process, so I trust it" boundary (per Q3),
remote servers need explicit authentication — typically OAuth-style
token-based auth, matching how any other network-exposed API would
authenticate a caller.

**SENIOR-LEVEL ANSWER:** The practical design question this raises: is
the client authenticating as **itself** (a single, shared client
identity for every user of that client application) or **on behalf of
the actual end user** (per-user identity flowing through to the server)?
The latter is almost always the correct model for anything beyond a
single-user tool — it's what makes the gateway's per-identity
authorization design in `senior-scenarios.md` possible at all. A remote
MCP integration authenticating only as a shared client identity loses
the ability to apply per-user authorization at the server/gateway level
entirely, collapsing back to "anyone with client access can do anything
the client's shared identity can do."

**FOLLOW-UP QUESTIONS:**
- How would per-user identity actually propagate from the end user
  through the client to the remote MCP server?
- What's the risk of a client application caching a user's token longer
  than appropriate?
- How does token refresh/expiry interact with a long-running agent
  session?

**RED FLAGS:** Designing remote MCP authentication around a single
shared client credential when the actual use case needs per-user
authorization — undermines the entire governance value proposition.

---

### Q14. Why might an MCP client want to sandbox a locally-run stdio MCP server, even though it already trusts "I chose to launch this"?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Security Engineer

**SENIOR-LEVEL ANSWER:** "I chose to launch this" establishes trust in
the *decision* to run the server, not in the server's *implementation*
being bug-free or fully benign in every respect — a legitimate,
intentionally-installed server can still have a vulnerability, an
unintended side effect, or (per `security.md`'s third-party server
discussion) turn out to be less trustworthy than initially assessed.
Sandboxing (restricted filesystem access, no unnecessary network access,
resource limits) is defense in depth against exactly that gap between
"I trust the decision to run this" and "I'm certain this specific process
will only ever do what it's supposed to." This mirrors the container-
runtime-vulnerability reasoning in `kubernetes/senior-scenarios.md` S5 —
a trust boundary you've deliberately drawn (launching a process; running
a container) is still worth defending in depth, not treated as
sufficient on its own.

**FOLLOW-UP QUESTIONS:**
- What's a concrete sandboxing mechanism you'd apply to a local MCP
  server process, practically?
- How would you balance sandboxing strictness against a server
  genuinely needing broad filesystem access for its stated purpose (e.g.
  a code-editing tool)?
- Does sandboxing reduce the priority of also vetting the server's
  publisher/provenance, or are these complementary?

**RED FLAGS:** "I launched it myself, so it's fully trusted" as a
complete security posture — ignores the gap between trusting a launch
decision and trusting an implementation's correctness.

---

### Q15. What's "tool discovery scoped per-identity" (mentioned in the enterprise gateway design), and why is it stronger than just enforcing authorization at invocation time?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Security Engineer, AI Platform Engineer

**SENIOR-LEVEL ANSWER:** Invocation-time authorization (checking "is this
identity allowed to call this tool" only when the call is actually
attempted) is necessary but not sufficient on its own — it still lets an
unauthorized identity (or a model acting on its behalf) **see** that a
sensitive tool exists in the first place, which is itself information
disclosure, and gives a manipulated model something concrete to attempt
even if it's ultimately rejected. Per-identity scoped discovery removes
unauthorized tools from what's even presented to the client/model at
session start — a defense-in-depth layer *before* invocation-time
authorization, not a replacement for it. Both layers matter: discovery
scoping reduces the attack surface a compromised/manipulated session can
even attempt against; invocation-time authorization is the actual hard
enforcement boundary that must hold even if discovery scoping somehow
failed or was bypassed.

**FOLLOW-UP QUESTIONS:**
- Why isn't invocation-time authorization alone considered sufficient,
  given it would still correctly block an unauthorized call?
- What's the performance/complexity cost of computing per-identity
  discovery results versus a single shared discovery response for
  everyone?
- How would you test that discovery scoping is actually working
  correctly, not just assumed to be?

**RED FLAGS:** Treating discovery-time scoping as redundant with
invocation-time authorization — they're complementary defense-in-depth
layers, not the same control twice.

---

### Q16. How would you design health-checking for an MCP server so a gateway can proactively route around an unhealthy one, rather than waiting for a request to time out?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Platform Engineer, SRE

**SENIOR-LEVEL ANSWER:** A gateway relying purely on request-level
timeouts (Q10) to detect an unhealthy server means **every user
request** to that server pays the full timeout cost before failing —
poor UX at scale. A proactive health-check (a lightweight, periodic
liveness probe against each backend MCP server, independent of real user
traffic) lets the gateway mark a server unhealthy and route around it
(or fail fast with a clear error) *before* real user requests hit the
slow/dead path — the same principle as a Kubernetes readiness probe
removing an unhealthy pod from Service Endpoints (per
`kubernetes/fundamentals.md` Q5) applied to MCP server backends in a
gateway.

**FOLLOW-UP QUESTIONS:**
- How would you avoid the same over-aggressive-probe failure mode
  discussed in the Kubernetes readiness-probe question, applied here?
- What should the gateway do with in-flight requests to a server that
  just became unhealthy?
- How would you alert operators when a specific backend server has been
  unhealthy for an extended period?

**RED FLAGS:** Relying solely on request-level timeouts for health
detection — every single user request pays the discovery cost instead of
proactive health-checking catching it once.

---

### Q17. What's the difference between an MCP server being "stateless" versus maintaining session state across multiple tool calls within a conversation?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Engineer, AI Platform Engineer

**ANSWER:** A stateless server treats every tool call independently, with
no memory of prior calls in the same session. A stateful server
maintains context across calls within a session (e.g. a multi-step
transaction, or an incrementally-built query) — requiring the server to
track session identity and associated state.

**SENIOR-LEVEL ANSWER:** Statelessness is the simpler, more scalable
default (any server instance can handle any request, trivial horizontal
scaling, no session-affinity requirement) and should be preferred unless
the tool's actual semantics genuinely require cross-call state. When
state is genuinely required, the design question becomes *where* that
state lives — in the server's own memory (creates a session-affinity
requirement, complicating horizontal scaling and failover, per the
StatefulSet identity discussion in `kubernetes/fundamentals.md` Q10) or
externalized to a shared store the server reads/writes per call
(preserves horizontal scalability, at the cost of added
latency/complexity per call). This is the same stateless-vs-stateful
architecture trade-off that recurs throughout distributed systems,
applied specifically to MCP server design.

**FOLLOW-UP QUESTIONS:**
- Give an example of an MCP tool that genuinely needs cross-call state,
  and one that looks like it might but doesn't.
- How would you handle a stateful server instance crashing mid-session —
  what happens to the in-progress state?
- How does statelessness affect how a gateway can load-balance across
  multiple instances of the same server?

**RED FLAGS:** Defaulting to stateful server design without justifying
why the specific tool semantics require it — adds real scaling/failover
complexity that should be a deliberate trade-off, not a default.

---

### Q18. How would you design rate limiting for MCP tool calls — per client, per identity, per tool, or some combination?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Platform Engineer

**SENIOR-LEVEL ANSWER:** A single global rate limit is almost never the
right granularity — it fails to distinguish "one identity is
misbehaving/looping" from "the platform is genuinely at capacity," and
punishes every user equally for one bad actor's behavior. The right
design layers rate limits at **multiple granularities simultaneously**:
per-identity (bounds what any single user/agent session can do,
catching runaway loops per the agent-reliability reasoning in
`ai-engineering/agents-and-agentic-ai/senior-scenarios.md`), per-tool
(some tools are inherently more expensive/sensitive and warrant tighter
limits regardless of caller), and a platform-wide aggregate limit
(protects overall capacity regardless of how well-distributed individual
limits are). Whichever limit is hit first for a given request determines
the specific rejection reason surfaced back — important for
debuggability, since "you're rate limited" without specifying which
layer is unhelpful for a caller trying to understand and fix their usage
pattern.

**FOLLOW-UP QUESTIONS:**
- How would you choose appropriate limits for a brand-new tool with no
  historical usage data to base them on?
- What's the risk of setting per-identity limits too tight for a
  legitimate, high-volume automated agent use case?
- How would rate-limit rejections be communicated back to the calling
  model in a way it could reasonably act on (e.g. back off and retry)?

**RED FLAGS:** Proposing a single, flat rate limit with no distinction
by identity or tool sensitivity — fails to isolate a single bad actor
from affecting everyone else.

---

### Q19. What's the risk of an MCP tool's description being auto-generated from code (e.g. from function docstrings) without human review?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Engineer, AI Security Engineer

**SENIOR-LEVEL ANSWER:** Auto-generation from docstrings is convenient
and keeps documentation in sync with code, but it inherits whatever the
docstring author wrote **without independent review for
model-manipulation risk** (per the tool-poisoning discussion in
`security.md`) — a docstring written purely for human-developer
clarity was never evaluated against "could this text be interpreted by a
model as an implicit instruction beyond describing the tool." This isn't
a hypothetical: docstrings sometimes contain phrasing like "always do X
before calling this" intended as developer guidance that a model could
interpret as a directive to follow universally, not just when genuinely
relevant. The practical mitigation: auto-generation is fine as a
starting draft, but tool descriptions that will actually be exposed to a
model should get a distinct review pass specifically for
manipulation-risk framing, not just accuracy — a different review
lens than normal code review applies.

**FOLLOW-UP QUESTIONS:**
- What would a review checklist specifically for model-facing tool
  descriptions look like, distinct from normal documentation review?
- How would you detect, after the fact, that a tool description is
  actually influencing model behavior in an unintended way?
- Should tool descriptions be versioned/audited the same way tool
  schemas are (per Q12)?

**RED FLAGS:** Treating tool-description generation as purely a
documentation-accuracy concern with no distinct security review needed.

---

### Q20. Why does the MCP spec support multiple simultaneous transports (stdio and HTTP-based) rather than standardizing on just one?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Platform Engineer

**SENIOR-LEVEL ANSWER:** Per Q3, the two transports serve genuinely
different deployment shapes with different trust models — stdio for
local, single-machine, implicitly-trusted tool integration; HTTP-based
for shared, remote, explicitly-authenticated services. Forcing a single
transport would either burden every local, single-developer tool
integration with unnecessary network/auth infrastructure (if HTTP-only),
or make legitimate shared enterprise services awkward to expose safely
(if stdio-only, since stdio has no natural network-auth story). Supporting
both, with the trust model appropriate to each, is a deliberate
acknowledgment that MCP serves both use cases and they have genuinely
different requirements — not an accidental spec complexity.

**FOLLOW-UP QUESTIONS:**
- Could a single server support both transports simultaneously, and
  would that ever make sense?
- How would you decide which transport is appropriate for a new
  integration you're building?
- What would be lost if MCP had standardized on HTTP-only from the
  start?

**RED FLAGS:** Viewing transport flexibility as unnecessary complexity
rather than a deliberate response to genuinely different deployment/trust
requirements.

---

### Q21. How would a client know whether a tool call actually succeeded, partially succeeded, or failed — and why does that distinction matter for agentic use specifically?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Engineer, Agentic AI Engineer

**SENIOR-LEVEL ANSWER:** A well-designed tool response distinguishes
these outcomes explicitly rather than collapsing everything into a
binary success/failure — this matters far more for **agentic** use
(per `ai-engineering/agents-and-agentic-ai/`) than for a single
human-driven interaction, because an agent making autonomous follow-up
decisions based on a tool result needs to know whether a partial failure
means "safe to retry the whole operation" (idempotent, nothing
persisted) or "do not retry blindly" (a side effect already occurred,
and retrying could duplicate it) — collapsing this distinction into a
generic error risks an agent retrying a non-idempotent operation and
causing a real duplicate side effect, directly connecting to the
idempotency-key reasoning in `system-design/backend/principles.md` Q2,
applied to agent-tool interaction instead of client-server API retries.

**FOLLOW-UP QUESTIONS:**
- How would you design a tool's response schema to clearly communicate
  partial-failure/retry-safety to a calling agent?
- What's the risk if a tool is inherently non-idempotent and doesn't
  communicate that clearly?
- How would you test an agent's actual behavior when it receives an
  ambiguous partial-failure response?

**RED FLAGS:** Designing tool responses as a flat success/failure boolean
with no partial-failure or retry-safety signal — a real gap for
autonomous agentic callers specifically.

---

### Q22. What's the relationship between MCP and function/tool calling as implemented natively by various LLM providers — is MCP a replacement for provider-native tool calling?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Engineer, LLM Engineer

**ANSWER:** No — they operate at different layers. Provider-native tool
calling is the **model-level mechanism** by which a model expresses "I
want to call this function with these arguments" as part of its output
format. MCP is a **protocol standardizing how applications supply tool
definitions and execute those calls**, independent of which model/
provider is being used. An MCP client typically translates MCP tool
definitions into whatever tool-calling format the specific model
provider expects.

**SENIOR-LEVEL ANSWER:** This layering is exactly what gives MCP its
portability value (per Q1) — an MCP server's tool definitions don't need
to know or care which model provider's native tool-calling format will
ultimately consume them; that translation is the client's
responsibility. This means switching model providers (per the
model-routing discussion in `ai-engineering/llm/questions.md`) doesn't
require re-authoring tool integrations — the MCP layer is provider-
agnostic by design, while native tool-calling is inherently
provider-specific.

**FOLLOW-UP QUESTIONS:**
- What happens if a model provider's native tool-calling format can't
  represent something an MCP tool schema expresses (a format mismatch)?
- Would you ever bypass MCP and use a provider's native tool-calling
  directly — when might that be the right call?
- How does this layering affect testing — can you test MCP tool
  definitions independent of any specific model?

**RED FLAGS:** Treating MCP and native tool-calling as competing/
redundant mechanisms rather than recognizing they operate at different,
complementary layers.

---

### Q23. Why might a platform want a "dry-run" or "preview" mode for certain MCP tools, distinct from actually executing them?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Platform Engineer, AI Security Engineer

**SENIOR-LEVEL ANSWER:** For side-effecting, hard-to-reverse tools (per
the tiered-permission reasoning in
`ai-engineering/agents-and-agentic-ai/senior-scenarios.md` S2), a dry-run
mode lets a human reviewer (or an automated safety check) see **exactly
what the tool would do** with the model's chosen arguments before
committing to the real action — closing the gap between "the model
decided to call this tool with these arguments" and "these arguments
are actually correct and safe to execute for real," without needing full
human-in-the-loop confirmation on every single invocation of that tool
class. This is a genuinely useful middle ground between full autonomy and
full manual confirmation: cheaper than blocking every call for human
review, safer than blind autonomous execution for the specific tool
classes where a preview is meaningful and cheap to generate.

**FOLLOW-UP QUESTIONS:**
- For what class of tool would a dry-run mode be meaningless or
  impossible to implement usefully?
- How would you decide which tools warrant a dry-run option versus
  direct execution versus full human confirmation?
- What would the review UX look like for a human evaluating a dry-run
  result under time pressure?

**RED FLAGS:** Not distinguishing dry-run/preview from either full
autonomy or full human-gate-every-call — missing a genuinely useful
middle option in the tiered-permission design space.

---

### Q24. How would you approach deprecating and eventually removing an MCP tool that's still receiving low but non-zero usage?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** AI Platform Engineer

**SENIOR-LEVEL ANSWER:** Mirrors the removed-API-deprecation discipline
in `kubernetes/fundamentals.md` Q16 and Q12's schema-versioning
discussion, applied to whole-tool retirement: (1) mark the tool
deprecated in its own description/metadata (visible to both humans and,
importantly, to the model itself if the description is surfaced as
context, which can reduce organic usage as models "see" the
deprecation notice); (2) instrument actual usage to know who/what is
still calling it, not guess; (3) directly reach out to identified
remaining callers with a migration path to the replacement, if one
exists; (4) only remove once usage is confirmed at zero or the remaining
callers have an acceptable migration deadline — never remove a tool with
active non-zero traffic without notice, mirroring the same removed-API
fleet-upgrade risk discussed for Kubernetes.

**FOLLOW-UP QUESTIONS:**
- How would you instrument tool usage attribution well enough to know
  exactly which client/identity is still calling a deprecated tool?
- What's the risk of a deprecation notice in a tool description actually
  confusing the model into unexpected behavior, rather than just
  informing human developers?
- How long would you keep a deprecated tool available before hard
  removal, and what would inform that timeline?

**RED FLAGS:** Removing a tool based on aggregate usage looking "low"
without actually confirming zero remaining callers — low isn't zero, and
someone's integration may still depend on it.

---

### Q25. What's the single most important property an MCP gateway needs to get right before anything else, if you had to prioritize?

**DIFFICULTY:** 🟠 Senior
**ROLE:** AI Platform Engineer, AI Security Engineer

**SENIOR-LEVEL ANSWER:** **Authorization enforced independently of model
behavior** — every other property discussed across this domain
(discovery scoping, rate limiting, health-checking, tool versioning,
dry-run modes) is a refinement or defense-in-depth layer on top of this
one foundational property, and none of them substitute for it. A gateway
with excellent observability, rate limiting, and health-checking, but
that ultimately trusts the model's own restraint for what it's allowed
to invoke, has not actually solved the core problem this whole domain
exists to address — this is the single thread running through the
security scenarios in `security.md`, the gateway design in
`senior-scenarios.md`, and the tiered-permission agent scenarios in
`ai-engineering/agents-and-agentic-ai/senior-scenarios.md`: the boundary
must be enforced in code the model cannot reason its way around, not in
instructions it's asked to follow. Everything else is genuinely valuable,
but is worth building *after* this foundation is solid, not instead of
it.

**FOLLOW-UP QUESTIONS:**
- If you had to launch an MCP gateway with only one of
  {authorization enforcement, rate limiting, observability} fully built,
  which would you pick and why?
- How would you convince a team under launch-deadline pressure not to
  cut the authorization-enforcement work to ship faster?
- What's a real-world example (from any domain, not necessarily MCP) of
  a system that shipped without this kind of foundational control and
  paid for it later?

**RED FLAGS:** Naming observability, rate limiting, or discoverability as
the top priority instead of enforced authorization — these are valuable
but secondary to the one property nothing else can substitute for.
