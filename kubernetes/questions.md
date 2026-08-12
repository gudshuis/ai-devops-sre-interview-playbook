# Kubernetes — Interview Questions

Broader interview-style questions, distinct from `fundamentals.md`
(core mechanics) and `senior-scenarios.md` (open-ended design) — these
are the comparison/judgment/experience-shaped questions an interviewer
asks alongside those two.

---

## Question 01 — When would you choose a Deployment over a DaemonSet, and vice versa?

**Difficulty:** 🔵 Intermediate
**Roles:** DevOps, Platform Engineer

### Short answer
Deployment for a workload you want a controlled *number* of replicas of,
spread by the scheduler. DaemonSet for a workload that must run exactly
once per (matching) node, regardless of replica count.

### Detailed answer
A DaemonSet's replica count isn't set directly — it's implicitly "one
per eligible node," growing and shrinking automatically as nodes join/
leave. This makes it the right primitive for node-level infrastructure
(log shippers, node monitoring agents, CNI components) where the whole
point is "every node needs one," not "N copies somewhere in the
cluster."

### Production example
A log-shipping agent (Promtail/Fluent Bit) needs to run on every node to
collect that node's container logs — a Deployment with N replicas
provides no guarantee of node coverage; a DaemonSet does, by
construction.

### Trade-offs
DaemonSets bypass normal scheduling flexibility (they target specific
nodes by design, via node selectors/tolerations) — not a general-purpose
scaling primitive.

### What a strong senior candidate should mention
The connection to taints/tolerations (`fundamentals.md` Q13) — a
DaemonSet typically needs tolerations to run on tainted nodes (e.g. a
monitoring agent that must run even on GPU-dedicated nodes).

### Common weak answer
"DaemonSet is for system-level pods" — true but doesn't explain the
underlying mechanical reason (per-node guarantee vs. replica count).

### Follow-up questions
- How does a DaemonSet interact with cluster autoscaling?
- Can a DaemonSet do a rolling update, and how does that differ from a
  Deployment's rollout?

---

## Question 02 — What's your process for debugging a pod that's `Running` but the application inside seems unresponsive?

**Difficulty:** 🟠 Senior
**Roles:** SRE, Platform Engineer

### Short answer
Distinguish "process is alive but not serving" from "process is
deadlocked/hung" before reaching for a restart.

### Detailed answer
`kubectl exec` in and check the process is actually listening
(`ss -tulpn` inside the container). If listening but not responding,
check for thread/connection pool exhaustion, a deadlock, or a downstream
dependency hang (per the "follow the request" mental model) before
assuming the application itself is broken.

### Production example
A service with a database connection pool fully exhausted by a slow
downstream query appears "Running," passes a shallow TCP-only readiness
check, but hangs on every real request — Lab 3's readiness-probe
reasoning applies here even though the pod technically reports Ready.

### Trade-offs
A restart "fixes" the symptom immediately but destroys the diagnostic
evidence (thread dumps, connection state) needed to find the actual
cause — worth capturing evidence first if the incident allows it.

### What a strong senior candidate should mention
The difference between a shallow (TCP-only) and deep (actual dependency
check) readiness probe, and why the shallow version misses exactly this
failure mode.

### Common weak answer
"I'd restart the pod" with no diagnostic step first — fixes the
symptom, teaches nothing about the cause, and it recurs.

### Follow-up questions
- How would you capture a thread dump from a running container before
  restarting it?
- What readiness probe design would have caught this earlier?

---

## Question 03 — Compare Helm and Kustomize. Which would you choose for a new project?

**Difficulty:** 🔵 Intermediate
**Roles:** Platform Engineer, DevOps

### Short answer
Helm templates YAML with a full templating language and packages
releases with versioning; Kustomize patches plain YAML declaratively
with no templating language, layering overlays on a base.

### Detailed answer
Helm's templating gives real power (loops, conditionals, values files)
at the cost of YAML that's no longer directly readable/diffable — you're
reading a template, not the actual manifest. Kustomize's patch-based
approach keeps the base YAML fully valid and readable on its own, with
overlays expressing only the *diff* per environment — often a better fit
for the environment-overlay pattern in the GitOps promotion design
(`senior-scenarios.md` S8).

### Production example
A Helm chart with deeply nested conditional logic became difficult for
new team members to reason about; migrating simpler services to
Kustomize overlays made the actual deployed config directly readable.

### Trade-offs
Kustomize lacks Helm's packaging/versioning/release-history model — for
distributing a reusable chart to many independent consumers (not just
internal environment overlays), Helm's ecosystem is the stronger fit.

### What a strong senior candidate should mention
These aren't mutually exclusive — Helm charts can be post-processed with
Kustomize, and many real platforms use both for different purposes.

### Common weak answer
Declaring one universally better without naming the actual use-case
difference (packaging/distribution vs. environment-specific patching).

### Follow-up questions
- How would you version a Kustomize-based deployment, given it lacks
  Helm's chart versioning?
- When would you choose Helm specifically for its templating power?

---

## Question 04 — Tell me about a time you had to debug a Kubernetes networking issue. What was your approach?

**Difficulty:** 🟠 Senior
**Roles:** SRE, Kubernetes Engineer

### Short answer
Layer-by-layer isolation (DNS → Service/Endpoints → NetworkPolicy →
actual packet path) rather than guessing.

### Detailed answer
See the "Follow the Request" mental model and `troubleshooting.md` Labs
3 and 10 for the concrete methodology — the answer to this question
should demonstrate a repeatable process, not just a memorized past
incident.

### Production example
Reference an actual Lab from `troubleshooting.md` as a model answer
shape — e.g. narrating Lab 10's asymmetric-NetworkPolicy investigation
as if it were your own experience, with the same evidence-based
reasoning.

### Trade-offs
Jumping straight to `tcpdump` before ruling out simpler causes (DNS,
Endpoints) wastes time — cheap checks first.

### What a strong senior candidate should mention
A specific, concrete piece of evidence that changed their hypothesis
mid-investigation — shows real reasoning, not a rehearsed script.

### Common weak answer
A vague, non-specific answer with no concrete commands or evidence
mentioned — reads as fabricated or poorly remembered.

### Follow-up questions
- What would you have done differently in hindsight?
- How did you prevent recurrence?

---

## Question 05 — What's the difference between `emptyDir`, `hostPath`, and a PVC-backed volume?

**Difficulty:** 🔵 Intermediate
**Roles:** Kubernetes Engineer

### Short answer
`emptyDir`: ephemeral, pod-lifetime-scoped, node-local. `hostPath`:
mounts a specific path from the host node directly — powerful and
dangerous. PVC-backed: durable, provisioned via CSI, survives pod
rescheduling.

### Detailed answer
`hostPath` breaks the abstraction Kubernetes otherwise provides (a pod
using it is tied to specific host filesystem contents/paths, and it's a
real security risk if misused — direct host filesystem access from a
container). PVC-backed volumes are the right default for anything
needing real persistence; `emptyDir` is right for scratch space that
should vanish with the pod.

### Production example
A poorly-reviewed manifest used `hostPath` to mount `/` on the host for
"convenience" during debugging and was never removed — a serious,
unnoticed security exposure until an audit caught it.

### Trade-offs
PVC-backed volumes have real provisioning latency/cost (per the CSI
fundamentals question) that `emptyDir`/`hostPath` don't — not always the
right choice for genuinely ephemeral, high-churn scratch data.

### What a strong senior candidate should mention
The security risk of `hostPath` specifically, and that most admission
policies should restrict or ban it by default.

### Common weak answer
Describing only the functional differences with no mention of
`hostPath`'s security implications.

### Follow-up questions
- How would you write an admission policy to restrict `hostPath` usage?
- What's the risk profile difference between `hostPath` and a
  privileged container?

---

## Question 06 — How would you approach right-sizing a workload's resource requests/limits from scratch, with no prior data?

**Difficulty:** 🟠 Senior
**Roles:** SRE, Platform Engineer

### Short answer
Start conservative but measured (not guessed), observe real usage under
representative load, then iterate — never ship a permanent guess.

### Detailed answer
Deploy with a reasonable starting estimate (based on similar known
workloads, or a load test), monitor actual usage (`kubectl top`, or
better, historical metrics) over a representative period including peak
load, then adjust based on real data — connects directly to the
requested-vs-actual comparison discussed in `troubleshooting.md` Lab 20.

### Production example
A new service launched with copy-pasted resource values from an
unrelated service; six months later, a rightsizing pass based on actual
usage cut its resource footprint by 40% with zero performance impact.

### Trade-offs
Under-provisioning risks throttling/OOM under real load; over-
provisioning wastes cluster capacity and cost — the whole point of
data-driven rightsizing is avoiding both failure modes rather than
guessing which side is "safer."

### What a strong senior candidate should mention
The QoS class implications (`fundamentals.md` Q2) of the request/limit
ratio chosen, not just the absolute values.

### Common weak answer
"I'd set limits high to be safe" — ignores the real cost and
bin-packing-efficiency consequences of systematic over-provisioning.

### Follow-up questions
- How would you validate your initial estimate before real production
  traffic arrives?
- How often would you revisit rightsizing for an actively-changing
  workload?

---

## Question 07 — What's your opinion on running a service mesh — is it always worth the complexity?

**Difficulty:** 🟠 Senior
**Roles:** Platform Engineer, DevSecOps

### Short answer
No — worth it for genuine zero-trust/mTLS requirements or complex
traffic-management needs; real overhead for simpler platforms.

### Detailed answer
Per the zero-trust networking scenario (`senior-scenarios.md` S23), a
service mesh solves a specific, real problem (identity-based mTLS,
fine-grained traffic policy) that NetworkPolicy alone can't. But sidecar
injection has real latency/resource cost on every single request, and
operational complexity (debugging traffic now goes through an
additional layer) — not something to adopt by default without a
specific requirement it solves.

### Production example
A platform adopted a service mesh primarily for its observability
features, when a simpler dedicated tracing solution would have met that
specific need without the mTLS/traffic-management complexity they never
actually used.

### Trade-offs
The core trade-off named explicitly in S23 — real security/traffic-
management capability versus real, ongoing operational and performance
cost.

### What a strong senior candidate should mention
The specific *requirement* that would justify a mesh (genuine zero-trust
mTLS, complex canary/traffic-splitting needs) versus reaching for it as
a default "best practice."

### Common weak answer
"Yes, always use a service mesh, it's a best practice" — no requirement-
based justification.

### Follow-up questions
- What's "ambient mode" mesh architecture, and how does it change the
  sidecar-overhead trade-off?
- How would you evaluate whether your platform's actual traffic-
  management needs justify a mesh?

---

## Question 08 — How would you explain Kubernetes' reconciliation/watch-loop model to someone who's never used it, using an analogy?

**Difficulty:** 🟢 Beginner
**Roles:** All roles

### Short answer
Like a thermostat: it doesn't execute a one-time command, it continuously
compares "current temperature" to "desired temperature" and acts to
close the gap, forever.

### Detailed answer
Every controller in Kubernetes (per `fundamentals.md` Q1) does the same
thing: watch for the actual state to differ from desired state, act to
close the gap, repeat indefinitely. This is why editing a live object
that's under a controller's management gets silently reverted — the
controller is still running its loop, continuously re-asserting desired
state.

### Production example
Explaining to a new engineer why their `kubectl edit` on a
Deployment-managed Pod "didn't stick" — the ReplicaSet controller's
reconciliation loop reverted it, exactly like a thermostat closing a
window someone opened.

### Trade-offs
This model is what makes Kubernetes self-healing and resilient to
controller restarts, at the cost of being less intuitive for engineers
used to imperative, one-shot deployment tools.

### What a strong senior candidate should mention
That this pattern generalizes beyond Kubernetes core — it's the same
model GitOps tools (Argo CD) apply at a higher level, reconciling Git
state against live cluster state.

### Common weak answer
An analogy that implies a one-time action rather than continuous,
ongoing reconciliation — misses the actual mechanism.

### Follow-up questions
- How does this model help explain why GitOps tools work the way they
  do?
- What happens during the brief window where actual and desired state
  differ — is there any consistency guarantee?

---

## Question 09 — What's the biggest Kubernetes-related production mistake you've seen (or would want to avoid), and why?

**Difficulty:** 🟠 Senior
**Roles:** SRE, Platform Engineer

### Short answer
Answers should reference a *specific, mechanistic* failure — this
question tests whether the candidate has real operational scar tissue,
not generic knowledge.

### Detailed answer
Strong answers pull from real failure patterns like those in
`troubleshooting.md` — a self-inflicted outage from an overly aggressive
liveness probe, a PDB that silently blocked all node drains, a
NetworkPolicy default-deny rollout with no DNS allow rule. What matters
is the specificity and the *prevention* lesson drawn from it, not just
"something broke."

### Production example
Use any of `troubleshooting.md`'s labs as reference-quality answer
shapes — the checkout-503-cascade incident (`incidents/kubernetes/checkout-503-cascade.md`)
is a fully worked example of this exact answer format.

### Trade-offs
N/A — this is a behavioral/experience question, not a technical
trade-off question.

### What a strong senior candidate should mention
A concrete prevention mechanism put in place afterward, not just "we
fixed it" — shows the incident led to systemic improvement, not just a
one-off patch.

### Common weak answer
A vague, generic answer ("we had an outage once") with no specific
mechanism or lesson.

### Follow-up questions
- What would you do differently if you saw early warning signs of the
  same failure mode again?
- How did the team's process change afterward?

---

## Question 10 — How do you decide whether something belongs in a ConfigMap versus being baked into the container image?

**Difficulty:** 🔵 Intermediate
**Roles:** Platform Engineer, DevOps

### Short answer
Anything that varies by environment/deployment belongs in a ConfigMap;
anything intrinsic to the application's version belongs in the image.

### Detailed answer
The test: would this value ever need to change without rebuilding the
image? If yes (a database hostname, a feature flag, a per-environment
setting), it belongs external to the image, in a ConfigMap. If it's
fundamentally tied to the application code's version (a compiled-in
constant, a bundled asset), baking it in is fine and often preferable
(fewer moving parts, guaranteed consistency between code and config
version).

### Production example
A team initially baked environment-specific URLs into their image,
requiring a full rebuild+redeploy for every environment promotion —
externalizing to ConfigMaps let the same image be promoted unchanged
across dev/staging/prod, per the GitOps promotion design's principle of
minimal per-environment difference.

### Trade-offs
Over-externalizing (putting everything in ConfigMaps, including things
that never actually vary) adds unnecessary indirection for no benefit.

### What a strong senior candidate should mention
The connection to the "same image promoted through environments" GitOps
principle (`senior-scenarios.md` S8) — baking environment-specific
values into the image directly breaks that model.

### Common weak answer
"Secrets go in Secrets, everything else in ConfigMaps" — doesn't
address the actual decision criterion for config-vs-image.

### Follow-up questions
- How would you handle a value that's technically config but rarely
  changes — still externalize it?
- What's the risk of a ConfigMap change not being picked up by already-
  running pods?

---

## Question 11 — What's your experience with Kubernetes Operators — have you built one, and would you recommend it for a given problem?

**Difficulty:** 🟠 Senior
**Roles:** Platform Engineer, Kubernetes Engineer

### Short answer
Reference `fundamentals.md` Q3's build-vs-buy judgment — Operators are
justified for genuinely stateful, continuous reconciliation needs, not
reflexively for every automation task.

### Detailed answer
A strong answer names a specific scenario where an Operator was (or
would be) justified — automating complex, ongoing operational knowledge
(backup scheduling, failover, version-aware upgrades) — versus where a
simpler tool (a Job, a CronJob, a Helm chart) would have sufficed.

### Production example
See `fundamentals.md` Q3's discussion of the "built a distributed system
to manage a distributed system" over-engineering trap.

### Trade-offs
An Operator is itself an ongoing maintenance burden (a controller with
its own failure modes, RBAC scope, versioning) — justified only when the
operational complexity it encodes genuinely exceeds what simpler tools
can express.

### What a strong senior candidate should mention
The risk of a CRD existing with no active controller reconciling it
(Q20 in fundamentals) — a real, non-obvious operational gotcha for
anyone who's actually operated Operators in production.

### Common weak answer
Enthusiasm for building an Operator with no specific justifying use
case — a red flag for over-engineering tendency.

### Follow-up questions
- How would you test an Operator's reconciliation logic before
  production?
- What's the RBAC scope an Operator typically needs, and how would you
  minimize it?

---

## Question 12 — How would you explain the trade-off between many small clusters versus one large cluster to a non-technical stakeholder?

**Difficulty:** 🟠 Senior
**Roles:** Platform Engineer, Solutions Architect

### Short answer
Many small clusters: better isolation/blast-radius containment, more
operational overhead. One large cluster: simpler to operate, higher
concentration of risk.

### Detailed answer
Frame it in business terms: fewer, larger clusters mean lower
operational cost (fewer things to patch/monitor/upgrade) but a single
incident (a bad upgrade, a control-plane failure) has broader blast
radius. More, smaller clusters cost more to operate but contain failures
better — directly the fleet-vs-single-cluster trade-off from
`senior-scenarios.md` S22, translated into stakeholder-friendly language.

### Production example
Explaining why a regulated business unit gets its own dedicated cluster
rather than sharing the general-purpose fleet — isolation requirement
justifies the added operational cost for that specific unit.

### Trade-offs
Same as S22's core trade-off, reframed for a non-technical audience —
operational simplicity/cost versus blast-radius containment.

### What a strong senior candidate should mention
A concrete business-relevant example (compliance requirement, outage
cost) rather than purely technical jargon, showing the ability to
communicate technical trade-offs to non-technical stakeholders.

### Common weak answer
A purely technical explanation with no translation to business impact —
doesn't demonstrate the communication skill the question is actually
testing.

### Follow-up questions
- How would you justify the added cost of multiple clusters to a
  budget-conscious stakeholder?
- What would change your recommendation for a specific business unit?

---

## Question 13 — What's the most important Kubernetes security practice you'd implement first on a brand-new cluster?

**Difficulty:** 🟠 Senior
**Roles:** DevSecOps, Platform Engineer

### Short answer
A default-deny NetworkPolicy baseline plus mandatory non-root/resource-
request admission policy — the highest-leverage, lowest-effort starting
controls.

### Detailed answer
Starting from a genuinely open default (per `fundamentals.md` Q4), the
highest-leverage first moves are: default-deny NetworkPolicy (with DNS
explicitly allowed, per the common gotcha), and admission-policy-
enforced baseline hygiene (non-root, resource requests mandatory,
`hostPath` restricted). These cost little to implement early and are
expensive to retrofit later once many non-compliant workloads exist
(per the audit-first rollout discipline in `senior-scenarios.md` S7).

### Production example
A cluster launched without these baselines accumulated hundreds of
non-compliant workloads over a year, making the eventual policy rollout
(per S7's gradual-cutover design) far more painful than if the baseline
had existed from day one.

### Trade-offs
Implementing these from day one on a brand-new cluster costs almost
nothing (no existing non-compliant workloads to break); retrofitting
later requires the full audit-first migration process.

### What a strong senior candidate should mention
The "day one is cheap, retrofit is expensive" framing specifically —
shows understanding of *when* security investment has the best
leverage, not just *what* the controls are.

### Common weak answer
Listing many security tools/practices with no prioritization or
reasoning about sequencing/leverage.

### Follow-up questions
- How would this priority change for an existing, already-populated
  cluster versus a brand-new one?
- What would you implement second, after these two?

---

## Question 14 — How do you keep up with Kubernetes' fast release cadence and deprecation cycles?

**Difficulty:** 🟢 Beginner / 🔵 Intermediate
**Roles:** All roles

### Short answer
Official release notes/deprecation guides as primary source, plus
automated tooling (API deprecation scanners) rather than manual tracking
alone.

### Detailed answer
Per `fundamentals.md` Q16, removed-API tracking is fully automatable and
should be — relying on manually reading every release's changelog for a
large fleet doesn't scale. The senior practice is tooling-assisted
tracking (automated scans against manifests) combined with periodic,
deliberate review of official deprecation guides for anything the
tooling might miss (behavioral changes, not just API removal).

### Production example
An automated CI check scanning manifests against the next target
version's removed-API list catches issues months before an actual
upgrade is planned, giving teams ample lead time.

### Trade-offs
Purely manual tracking doesn't scale past a handful of clusters/
workloads; purely automated tracking can miss subtler behavioral changes
not captured as a clean "removed API."

### What a strong senior candidate should mention
The connection to the fleet-upgrade scenario (`senior-scenarios.md` S6)
— this practice is what makes that scenario's pre-check step actually
tractable at scale.

### Common weak answer
"I read the release notes" with no mention of automation/tooling for
anything beyond a single cluster.

### Follow-up questions
- How would you build the automated scanning tool described above?
- How do you evaluate whether a new Kubernetes feature is stable enough
  to adopt in production?

---

## Question 15 — What's your take on running stateful databases directly on Kubernetes versus using a managed cloud database service?

**Difficulty:** 🟠 Senior
**Roles:** SRE, Platform Engineer

### Short answer
Managed services are the default recommendation for most teams — running
your own on Kubernetes is justified by specific requirements (cost at
scale, portability, specific feature needs), not as a default choice.

### Detailed answer
Kubernetes StatefulSets (per `fundamentals.md` Q10) provide the
primitives, but genuinely operating a production database (backup,
failover, patching, performance tuning) is real, ongoing operational
work that a managed service abstracts away. The trade-off is cost
(managed services carry a premium) and control (self-managed gives full
control, at the cost of owning all the operational burden) — most teams
underestimate the operational cost of self-managing until they've
actually done it.

### Production example
A team self-managed a database on Kubernetes to save cost, then spent
significant on-call time on failover/backup issues a managed service
would have handled automatically — the "savings" didn't account for the
real operational cost.

### Trade-offs
Cost savings and portability/control versus real, ongoing operational
burden — a deliberate trade-off, not a default either direction.

### What a strong senior candidate should mention
A specific scenario where self-managing is genuinely justified (multi-
cloud portability requirement, a specific feature not available
managed, cost at very large scale) rather than a blanket recommendation
either way.

### Common weak answer
"Always use managed services" or "always self-manage for control" as an
absolute rule with no situational reasoning.

### Follow-up questions
- What operational maturity would a team need before self-managing a
  production database responsibly?
- How does this trade-off change for a read-heavy cache (like Redis)
  versus a primary transactional database?

---

## Question 16 — How would you onboard a new engineer to a complex, multi-service Kubernetes platform quickly and effectively?

**Difficulty:** 🔵 Intermediate
**Roles:** Platform Engineer, Engineering Manager-adjacent

### Short answer
Golden-path documentation plus hands-on debugging practice (like the
`challenges/debug-this/` format), not just reading architecture docs.

### Detailed answer
Passive documentation reading doesn't build the investigation instincts
that actually matter day-to-day — pairing documentation with realistic,
hands-on troubleshooting practice (per this repository's own
`challenges/debug-this/` pattern) builds faster, more durable
competence than documentation alone.

### Production example
A platform team built an onboarding exercise mirroring
`challenges/debug-this/03-oomkill/` — a real, deliberately-broken
environment new engineers investigate themselves before comparing
against the documented solution — dramatically improving new-hire
time-to-productivity over pure documentation review.

### Trade-offs
Hands-on onboarding takes more upfront design investment than just
pointing someone at documentation, but pays off in faster, more durable
ramp-up.

### What a strong senior candidate should mention
The value of failure-mode-first learning (understanding how things
break) over purely architecture-first learning (understanding how
things are supposed to work) — mirrors this repository's own design
philosophy.

### Common weak answer
"Give them the documentation and let them figure it out" — no
structured, hands-on component.

### Follow-up questions
- How would you measure whether onboarding is actually effective?
- What's the right balance between structured exercises and real
  production exposure (with appropriate guardrails)?

---

## Question 17 — What's a Kubernetes feature or pattern you initially thought was over-engineered but changed your mind about after using it in production?

**Difficulty:** 🟠 Senior
**Roles:** All senior/staff roles

### Short answer
Behavioral question — tests intellectual honesty and whether experience
has actually shaped the candidate's opinions, versus reciting received
wisdom.

### Detailed answer
Strong answers name something genuinely specific (topology spread
constraints felt unnecessary until managing real multi-zone
availability at scale; PodDisruptionBudgets felt like bureaucracy until
a drain without one caused an outage) with the concrete experience that
changed the opinion.

### Production example
N/A — answer should be personal/specific to the candidate's real
experience.

### Trade-offs
N/A.

### What a strong senior candidate should mention
A genuine change of opinion with a concrete triggering experience — not
just listing a feature they now think is good without the "I used to
think X, then Y happened" narrative arc the question is probing for.

### Common weak answer
A generic answer with no real opinion change narrated, or claiming
they've never been wrong about anything technical (a red flag for
overconfidence/lack of self-reflection).

### Follow-up questions
- What's something you still have reservations about, even after using
  it?
- How has your approach to evaluating new Kubernetes features changed
  over your career?

---

## Question 18 — How would you evaluate whether to adopt a new CNCF project for your platform?

**Difficulty:** 🟠 Senior
**Roles:** Platform Engineer

### Short answer
Project maturity (CNCF graduation level), genuine requirement fit (not
just "it's popular"), operational cost of running it, and community/
maintenance health.

### Detailed answer
CNCF's maturity levels (Sandbox/Incubating/Graduated) are a real, useful
signal but not sufficient alone — evaluate whether the project solves a
genuine requirement your platform has (per the service-mesh question's
"don't adopt without a specific requirement" reasoning), the real
operational cost of running and maintaining it, and community health
(active maintenance, responsive to security issues) as a proxy for
long-term viability.

### Production example
A team adopted an Incubating-stage project for a "nice to have" feature,
then had to migrate off it when the project stalled — a Graduated
project, or accepting a longer build for an in-house solution, might
have been the more durable choice.

### Trade-offs
Newer/less mature projects sometimes offer genuinely better capability
for emerging problems, at higher risk of instability/abandonment — a
real risk/capability trade-off, not just "always pick mature projects."

### What a strong senior candidate should mention
A concrete example of a project they evaluated and either adopted or
explicitly rejected, with the actual reasoning.

### Common weak answer
"I check if it's popular on GitHub" — a weak, easily-gamed signal
compared to genuine maturity/requirement-fit evaluation.

### Follow-up questions
- How would you evaluate the security posture of a project before
  adopting it?
- What's your exit strategy if a project you've adopted becomes
  unmaintained?

---

## Question 19 — What's the relationship between Kubernetes and the underlying cloud provider's own compute/networking primitives — how much do you need to understand both?

**Difficulty:** 🔵 Intermediate
**Roles:** Cloud Engineer, Platform Engineer

### Short answer
A lot — Kubernetes abstracts compute/networking, but real production
debugging frequently requires understanding what's actually happening
one layer below (the cloud provider's VPC, load balancer, IAM).

### Detailed answer
Kubernetes' abstractions (Services, Ingress, StorageClasses) are
implemented *by* cloud-provider-specific controllers/CSI/CNI plugins —
when something breaks at the abstraction layer, the actual root cause is
frequently in the underlying cloud primitive (a security group blocking
traffic, an IAM permission gap, a cloud load balancer's own health-check
configuration). A platform engineer who only understands the Kubernetes
abstraction and not the underlying cloud implementation will hit a wall
on a meaningful fraction of real production issues.

### Production example
A LoadBalancer-type Service failed to route traffic; the root cause was
a cloud-provider security group rule, invisible from purely Kubernetes-
level debugging (`kubectl` showed everything "correct").

### Trade-offs
Learning both layers deeply is genuinely more work than treating
Kubernetes as a fully self-contained abstraction — but the abstraction
leaks often enough in production that the investment pays off.

### What a strong senior candidate should mention
A specific example where cloud-provider-level knowledge (not just
Kubernetes) was necessary to resolve a real incident.

### Common weak answer
"Kubernetes abstracts that away so I don't need to know it" — true in
the easy case, false often enough in production to be a real gap.

### Follow-up questions
- How would you debug a LoadBalancer Service that's not routing traffic,
  systematically?
- What cloud-provider-specific knowledge do you consider essential for a
  Kubernetes platform engineer?

---

## Question 20 — How would you handle a disagreement with a teammate about whether a given workload needs its own dedicated cluster versus sharing an existing multi-tenant one?

**Difficulty:** 🟠 Senior
**Roles:** Platform Engineer, Staff Engineer

### Short answer
Ground the disagreement in the actual isolation/compliance requirement
(per `senior-scenarios.md` S5/S11), not preference — let the requirement
decide.

### Detailed answer
This is fundamentally a technical trade-off question (per S5's tenant-
isolation reasoning) dressed as an interpersonal one — the right
resolution process is identifying the actual, specific requirement
(regulatory isolation? untrusted-code risk? just team preference for
autonomy?) and letting that drive the decision, rather than either party
"winning" on general principle.

### Production example
A disagreement over dedicating a cluster was resolved by explicitly
naming the actual requirement (a genuine compliance need, per S11) —
once named explicitly, the technical answer became clear and the
interpersonal disagreement dissolved.

### Trade-offs
N/A — behavioral/process question.

### What a strong senior candidate should mention
The skill of separating "what does the requirement actually demand"
from "what do I personally prefer" — a hallmark of senior technical
judgment and collaboration.

### Common weak answer
A purely interpersonal/conflict-resolution answer with no technical
grounding in the actual requirement that should decide the question.

### Follow-up questions
- What would you do if the requirement genuinely is ambiguous/
  unclear — how would you get clarity?
- How would you handle it if, after clarifying the requirement, your
  teammate still disagreed with the conclusion?

---

## Question 21 — What Kubernetes-adjacent skill do you think is most underrated by engineers who only know the `kubectl` surface layer?

**Difficulty:** 🟠 Senior
**Roles:** SRE, Platform Engineer

### Short answer
Linux/cgroup fundamentals (per `foundations/linux/`) — most Kubernetes
production incidents ultimately trace to something below the Kubernetes
abstraction layer.

### Detailed answer
`kubectl`-surface knowledge (object types, common commands) is
necessary but insufficient for genuinely debugging production
incidents — per the cgroup/OOM deep dive in `senior-scenarios.md` S1,
many real incidents require understanding what Kubernetes is actually
configuring at the kernel/cgroup level, not just the Kubernetes-level
abstraction.

### Production example
The OOM-despite-low-heap-usage pattern (`challenges/debug-this/03-oomkill/`)
is unsolvable with `kubectl`-surface knowledge alone — it requires
understanding what a container memory limit actually constrains at the
process level.

### Trade-offs
N/A.

### What a strong senior candidate should mention
A specific example (like the OOM case) where kubectl-surface knowledge
alone would have failed to diagnose a real issue.

### Common weak answer
A generic answer with no specific example of the underlying-knowledge
gap actually mattering in practice.

### Follow-up questions
- What other underlying-layer knowledge (networking, storage) do you
  find similarly underrated?
- How would you build this depth of knowledge if you were starting from
  kubectl-surface knowledge only?

---

## Question 22 — Describe how you'd explain to an engineering leader why "just add more replicas" isn't always the right response to a performance problem.

**Difficulty:** 🟠 Senior
**Roles:** SRE, Staff Engineer

### Short answer
More replicas helps for horizontal-scalable bottlenecks; it does nothing
for a shared downstream dependency (a database, a rate-limited external
API) that becomes the actual bottleneck instead.

### Detailed answer
Adding replicas increases the *offered* capacity of the scaled service
itself, but if the actual bottleneck is downstream (a database
connection pool, a shared external API's rate limit), more replicas just
means more concurrent load hitting that same downstream bottleneck,
potentially making things worse (more connection contention) rather than
better.

### Production example
A team scaled a service from 5 to 20 replicas under load, only to see
the actual bottleneck (a shared database connection pool) get worse, not
better — the added replicas increased concurrent connection pressure on
an already-saturated resource.

### Trade-offs
N/A — this is about correctly diagnosing the bottleneck before applying
a fix, not a trade-off between two valid approaches.

### What a strong senior candidate should mention
The general principle of identifying the actual bottleneck (per the
Kafka-consumer-lag troubleshooting lab's CPU-vs-partition-count
reasoning) before applying any scaling response.

### Common weak answer
Agreeing that more replicas always helps, or being unable to explain
*why* it sometimes doesn't.

### Follow-up questions
- How would you actually identify the true bottleneck before deciding
  how to respond to a performance problem?
- What's the right response if the bottleneck genuinely is downstream
  and not horizontally scalable?

---

## Question 23 — What's your philosophy on documentation for a Kubernetes platform — how much is enough?

**Difficulty:** 🔵 Intermediate
**Roles:** Platform Engineer

### Short answer
Enough that a new team member can self-serve common tasks and
troubleshooting without needing to interrupt the platform team — golden
paths plus troubleshooting runbooks, not exhaustive architecture
documents no one reads.

### Detailed answer
Per the internal-developer-platform case study's self-service
philosophy, the highest-value documentation is what actually reduces
support burden — golden-path guides for common tasks, and
troubleshooting runbooks for common failure modes (mirroring this
repository's own `troubleshooting.md`/`cheatsheet.md` structure) — over
exhaustive architecture documentation that goes stale quickly and few
people read cover-to-cover.

### Production example
A platform team measured which documentation pages were actually
visited before support tickets, versus which were rarely touched —
reallocated effort toward the high-traffic troubleshooting content and
deprecated rarely-read architecture deep-dives.

### Trade-offs
Comprehensive architecture documentation has real value for onboarding
and design review, but shouldn't come at the expense of the
higher-frequency-value troubleshooting/golden-path content.

### What a strong senior candidate should mention
The idea of measuring documentation value by actual usage, not assuming
comprehensiveness equals usefulness.

### Common weak answer
"As much documentation as possible" with no prioritization by actual
value/usage.

### Follow-up questions
- How would you keep troubleshooting-runbook documentation from going
  stale as the platform evolves?
- How would you measure whether your documentation is actually
  effective?

---

## Question 24 — How do you approach learning a new area of Kubernetes you're unfamiliar with (e.g. a CNCF project you've never used)?

**Difficulty:** 🟢 Beginner / 🔵 Intermediate
**Roles:** All roles

### Short answer
Hands-on experimentation in a low-stakes environment, paired with
reading the official docs for the *why*, not just the *how*.

### Detailed answer
Strong answers describe an actual learning process (spin up a local/
sandbox cluster, deliberately break things to understand failure modes,
read the project's own architecture docs for the underlying design
rationale) rather than just "I read the documentation."

### Production example
N/A — process/behavioral question.

### Trade-offs
N/A.

### What a strong senior candidate should mention
A specific, recent example of learning something genuinely new this way
— shows the process is real and current, not a rehearsed generic answer.

### Common weak answer
"I read the docs" with no hands-on component or specific recent example.

### Follow-up questions
- What's something in Kubernetes/cloud-native you're currently learning?
- How do you decide what's worth deep-diving versus surface-level
  familiarity?

---

## Question 25 — Where do you see Kubernetes' role changing over the next few years, particularly with AI/ML workloads becoming more common?

**Difficulty:** 🟠 Senior
**Roles:** Platform Engineer, AI Infrastructure Engineer

### Short answer
Increasing convergence — Kubernetes is becoming the substrate for AI
infrastructure (GPU scheduling, inference serving) alongside traditional
workloads, not a separate world.

### Detailed answer
Per `ai-engineering/ai-infrastructure/questions.md`, AI/ML workloads
bring genuinely new scheduling and serving requirements (GPU-aware
scheduling, cold-start-sensitive inference, mixed training/inference
capacity planning per `senior-scenarios.md` S9) that Kubernetes is being
extended to handle rather than replaced for — the trend is Kubernetes
absorbing AI infrastructure concerns as a first-class citizen, not a
separate AI-specific orchestration layer emerging instead.

### Production example
The rise of `KServe`/`vLLM`/GPU Operator as increasingly standard
Kubernetes ecosystem components (per `ai-engineering/ai-infrastructure/README.md`)
reflects this convergence directly.

### Trade-offs
N/A — forward-looking/opinion question.

### What a strong senior candidate should mention
Specific, concrete examples of this convergence already happening
(GPU Operator, KServe) rather than vague futurism.

### Common weak answer
Generic AI-hype commentary with no connection to actual Kubernetes
ecosystem developments.

### Follow-up questions
- What Kubernetes primitives do you think need to evolve further to
  properly support AI workloads?
- How does this convergence affect the skill set a platform engineer
  needs going forward?
