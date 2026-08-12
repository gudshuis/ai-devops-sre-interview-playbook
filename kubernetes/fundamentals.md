# Kubernetes — Fundamentals

---

### Q1. Walk through what happens between `kubectl apply -f deployment.yaml` and a running pod.

**DIFFICULTY:** 🟢 Beginner
**ROLE:** All platform/infra roles

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand the control
plane as a set of cooperating, loosely-coupled controllers rather than one
monolithic "Kubernetes" black box — this distinction matters for almost
every debugging question later.

**ANSWER:**
1. `kubectl` sends the Deployment manifest to the **API server**, which
   authenticates/authorizes the request and persists the desired state to
   **etcd**.
2. The **Deployment controller** (part of `kube-controller-manager`)
   notices the new/changed Deployment and creates a matching **ReplicaSet**.
3. The **ReplicaSet controller** creates Pod objects to match the desired
   replica count — these Pods exist in etcd but are `Unscheduled`.
4. The **scheduler** watches for unscheduled pods, evaluates node
   constraints (resources, affinity, taints/tolerations), and binds each
   Pod to a node.
5. The **kubelet** on that node sees a Pod bound to it, and instructs the
   **CRI** (e.g. containerd) to pull the image and start the container(s),
   configuring networking via the **CNI** plugin and storage via **CSI**
   if volumes are involved.
6. The kubelet reports Pod status back to the API server, which updates
   etcd — this is what `kubectl get pods` is reading.

**SENIOR-LEVEL ANSWER:** The important pattern underneath all of this is
**reconciliation via watch loops**, not a single request/response
pipeline. Every controller (Deployment, ReplicaSet, scheduler, kubelet) is
independently watching the API server for objects it cares about and
converging actual state toward desired state. This is *why* Kubernetes is
resilient to a controller restarting mid-operation — on restart it just
re-lists and re-watches, and picks up wherever reconciliation left off. It
also explains a common failure mode: if you edit a Pod's owning ReplicaSet
directly instead of the Deployment, the Deployment controller will
eventually revert it — you're fighting a reconciliation loop, not editing
a static config.

**FOLLOW-UP QUESTIONS:**
- What's actually stored in etcd, and why does etcd's own consensus
  (Raft) matter for cluster availability?
- What happens if the scheduler is down when you apply a new Deployment?
- How does a StatefulSet's pod creation differ from a Deployment's?
- What's the difference between a Pod's `Pending` and `ContainerCreating`
  states, diagnostically?

**RED FLAGS:** Describing this as "kubectl talks to the nodes" — it never
does; kubectl only ever talks to the API server. Not knowing that etcd is
where state actually lives.

---

### Q2. What's the difference between a resource *request* and a resource *limit*, and what determines a pod's QoS class?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** SRE, Platform Engineer, Kubernetes Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand resource
management well enough to reason about scheduling and eviction behavior,
not just the YAML syntax.

**ANSWER:**
- **Request**: what the scheduler guarantees is available on the chosen
  node before binding the pod there. Also used for CPU shares (proportional
  CPU time under contention).
- **Limit**: a hard ceiling. For CPU, the container is throttled past the
  limit. For memory, the container is OOM-killed past the limit — there's
  no "throttling" equivalent for memory.
- **QoS class** is derived automatically from requests/limits, not set
  directly:
  - **Guaranteed**: every container has requests == limits for both CPU
    and memory.
  - **Burstable**: at least one container has a request set, but not equal
    to its limit (or limits aren't set on every resource).
  - **BestEffort**: no requests or limits set at all.

**SENIOR-LEVEL ANSWER:** QoS class directly determines **eviction order**
under node memory pressure: BestEffort pods are evicted first, then
Burstable pods (ordered by how far usage exceeds requests), and Guaranteed
pods last (and only if they're actually exceeding their own limits, or if
system daemons need the memory). This means QoS class is a real production
lever, not a cosmetic label — if you want a pod to be the last thing
killed when a node is under memory pressure, you set requests == limits,
full stop. The trade-off: Guaranteed pods can't burst, so you're trading
flexibility for eviction priority, and over-provisioning Guaranteed pods
wastes cluster capacity you can't reclaim for bursty workloads.

**FOLLOW-UP QUESTIONS:**
- Why is there no memory throttling equivalent to CPU throttling?
- How does the kubelet decide *which* Burstable pod to evict first when
  several are over their requests?
- What's the operational risk of setting no limits at all cluster-wide?
- How do LimitRanges and ResourceQuotas interact with per-pod
  requests/limits?

**RED FLAGS:** Saying QoS class is "set in the YAML" — it's derived, not
declared. Not connecting resource config to eviction behavior at all.

---

### Q3. What is a Kubernetes Operator, and when is building one actually justified?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Platform Engineer, Kubernetes Engineer

**WHAT THE INTERVIEWER IS TESTING:** Engineering judgment about
build-vs-buy/build-vs-script, not just knowledge of the Operator pattern.

**ANSWER:** An Operator is a custom controller that watches a Custom
Resource Definition (CRD) and reconciles real-world state (often outside
Kubernetes entirely — a database, a cloud resource) to match it, encoding
operational knowledge that would otherwise live in a human runbook.

**SENIOR-LEVEL ANSWER:** An Operator is justified when the operational
task is (a) genuinely stateful and non-trivial to reconcile — backup
scheduling, failover, version-aware upgrades — and (b) needs to happen
*continuously and automatically* in response to drift, not just at
deploy time. A Helm chart that just templates YAML at install time is
enough for most stateless services; building a full Operator for
something a Job or a CronJob could handle is over-engineering that adds a
controller you now have to maintain, version, and RBAC-scope forever. The
failure mode I've seen most often is teams building an Operator because
it's the "cloud-native" thing to do, then discovering they've built a
distributed system (the Operator itself, with its own failure modes) to
manage another distributed system.

**FOLLOW-UP QUESTIONS:**
- What's the blast radius if your Operator's reconcile loop has a bug and
  starts flapping a resource?
- How would you test an Operator's reconciliation logic without a full
  cluster?
- What's the difference between a CRD and an aggregated API server, and
  when would you need the latter?

**RED FLAGS:** "Operators are always better than Helm" — shows no
awareness of the added operational cost of running a custom controller.

---

### Q4. Explain `NetworkPolicy` default behavior: what's allowed if no NetworkPolicy exists, versus after you create one?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** SRE, DevSecOps, Platform Engineer

**WHAT THE INTERVIEWER IS TESTING:** A specific, commonly-misunderstood
default-behavior detail that has real security implications.

**ANSWER:**
- With **zero** NetworkPolicies in a namespace, **all traffic is allowed**
  — Kubernetes networking is flat and open by default.
- The moment **any** NetworkPolicy selects a given pod, that pod's traffic
  (in the direction(s) the policy specifies — `Ingress`, `Egress`, or both)
  becomes **default-deny**, and only what's explicitly allowed by
  matching policies is permitted. Policies are additive — multiple
  policies selecting the same pod are OR'd together, not AND'd.

**SENIOR-LEVEL ANSWER:** The "selecting a pod flips it to default-deny in
that direction only" behavior is the single most common source of
NetworkPolicy production incidents: a team writes an `Ingress`-only policy
intending to restrict inbound traffic, doesn't realize `Egress` is
unaffected (still fully open) — or the reverse, someone writes an
`Egress` policy for DLP purposes and doesn't realize `Ingress` is now
untouched. The other frequent gotcha: NetworkPolicy enforcement is
delegated to the CNI plugin — if your cluster's CNI doesn't implement
NetworkPolicy (some do only ingress, or don't support them at all), the
policy objects apply successfully to etcd and do **nothing** on the wire,
silently. Verifying your CNI actually enforces what you think it does is
a real, easy-to-skip step.

**FOLLOW-UP QUESTIONS:**
- How would you implement a namespace-wide default-deny baseline, and what
  do you need to explicitly allow afterward (DNS egress is the classic
  one people forget)?
- What's the difference between NetworkPolicy and a service mesh's
  authorization policy (e.g. Istio AuthorizationPolicy)?
- How do you test that a NetworkPolicy is actually being enforced?

**RED FLAGS:** Assuming NetworkPolicies are enforced by the API server
itself, or that Kubernetes networking is deny-by-default out of the box.

---

### Q5. What's the difference between a liveness probe and a readiness probe, and what's the risk of misconfiguring each?

**DIFFICULTY:** 🟢 Beginner (definition) / 🔵 Intermediate (risk analysis)
**ROLE:** All infra/platform roles

**ANSWER:**
- **Readiness probe**: controls whether the pod receives traffic from
  Services (removed from endpoints if failing). Does not restart the
  container.
- **Liveness probe**: controls whether the kubelet restarts the container.
  Failing liveness = the container is killed and restarted.

**SENIOR-LEVEL ANSWER:** A liveness probe that's too aggressive relative
to a slow cold-start (e.g. a JVM app with a 90-second warmup, probed every
10 seconds starting immediately) is a classic **self-inflicted
restart-loop outage**: the app never finishes starting because it keeps
getting killed mid-startup. The fix is `initialDelaySeconds`/
`startupProbe` tuned to genuine cold-start time, not "genuinely unhealthy"
detection tuned too tight. The opposite failure — a readiness probe that's
too lenient (e.g. just checking the process is listening, not that
dependencies like a DB connection pool are actually healthy) — causes
traffic to be routed to pods that will error on every request, which is
worse for users than a slightly-slower rollout. The senior framing: these
two probes answer different questions ("should this get traffic" vs.
"should this be killed"), and conflating them (using one probe/endpoint
for both with identical logic) is a common root cause of both failure
modes above.

**FOLLOW-UP QUESTIONS:**
- What's a `startupProbe` for, and why was it added separately from
  liveness?
- How would you design a readiness check for a service with a downstream
  dependency that's sometimes slow but not actually down?
- What happens to in-flight requests when a pod fails its readiness probe
  mid-request?

**RED FLAGS:** Using the exact same endpoint/logic for both probes without
being able to explain why that's sometimes fine and sometimes dangerous.

---

### Q6. What is a PodDisruptionBudget, and what's it actually protecting against?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** SRE, Platform Engineer

**ANSWER:** A PDB (`minAvailable` or `maxUnavailable`) limits how many
pods of a given set can be **voluntarily** disrupted at once — node
drains, cluster upgrades, cluster-autoscaler scale-downs. It does **not**
protect against involuntary disruption (a node crashing, an OOM kill).

**SENIOR-LEVEL ANSWER:** The "voluntary only" distinction is the whole
point and the most commonly missed detail. A PDB gives you no protection
at all against the failure modes people usually worry about (crashes,
OOM) — its actual job is making **planned maintenance safe**: it's the
mechanism that lets a cluster upgrade or node drain proceed pod-by-pod
without ever taking your service below its minimum available replica
count, by having the eviction API respect the budget and simply wait/retry
rather than evicting past it. The real production risk: setting
`minAvailable` equal to your replica count (or `maxUnavailable: 0`) makes
the PDB **impossible to satisfy** during a drain — the drain will hang
indefinitely rather than violate the budget, which can block a node
upgrade cluster-wide until someone notices and intervenes.

**FOLLOW-UP QUESTIONS:**
- How does a PDB interact with the cluster autoscaler trying to drain a
  node for scale-down?
- What happens during a drain if a PDB literally cannot be satisfied?
- How would you set a PDB for a 2-replica Deployment where you genuinely
  can't tolerate going to 1?

**RED FLAGS:** Believing a PDB protects against pod crashes or node
failure — it explicitly does not.

---

### Q7. What does the API server actually do, and why is it the only component that talks to etcd directly?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Platform Engineer, Kubernetes Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you understand the API
server as a gatekeeper/validation layer, not just a proxy — this is what
makes the rest of the control plane's "everyone watches the API server"
pattern (Q1) actually safe.

**ANSWER:** The API server is the single entry point for every read/write
to cluster state: it authenticates the caller, authorizes the request
(RBAC), validates and mutates the object (admission control), and only
then persists to etcd. No other component — not the scheduler, not
kubelet, not `kubectl` — ever talks to etcd directly.

**SENIOR-LEVEL ANSWER:** Centralizing all writes through one component
with a fixed validation pipeline is what makes admission control,
audit logging, and RBAC enforcement *consistent* across every possible
write path — if controllers or kubelets could write to etcd directly,
each would need to reimplement authorization and validation itself, with
inevitable drift and gaps. The trade-off: the API server becomes a
genuine availability bottleneck — if it's down, the cluster's actual
workloads keep running (kubelet caches enough to continue), but nothing
can be *changed*, including emergency remediation via `kubectl`. This is
why API server HA (multiple replicas behind a load balancer) is treated
as one of the highest-priority pieces of control-plane reliability
engineering.

**FOLLOW-UP QUESTIONS:**
- What's the difference between authentication and authorization in the
  API server's request pipeline, concretely?
- What are admission webhooks, and why do they run *after* authorization
  but *before* the object is persisted?
- What happens to already-running pods if the entire control plane
  (API server included) becomes unavailable?

**RED FLAGS:** Describing the API server as "just a REST proxy to etcd" —
misses the authn/authz/admission pipeline entirely, which is the actual
point.

---

### Q8. Why does etcd use Raft consensus, and what does that mean for cluster sizing (why odd numbers of etcd nodes)?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Platform Engineer, SRE

**ANSWER:** etcd is a distributed key-value store using the Raft consensus
algorithm to keep multiple replicas consistent. Raft requires a **majority
quorum** to commit a write, which is why etcd clusters are sized with odd
numbers (3, 5) — an odd-sized cluster tolerates `(n-1)/2` node failures
while still having a majority available; even-sized clusters don't
improve fault tolerance over the next-smaller odd size (a 4-node cluster
tolerates the same 1 failure as a 3-node cluster, at higher cost).

**SENIOR-LEVEL ANSWER:** The practical consequence senior engineers need
to internalize: etcd availability is a **quorum problem, not a simple
redundancy problem** — losing 2 of 5 nodes is fine (3 remain, still a
majority); losing 3 of 5 takes the whole cluster read/write-unavailable
even though 2 nodes are technically still up and healthy. This is why
etcd nodes should be spread across failure domains (availability zones)
deliberately, and why "just add more etcd replicas for safety" isn't
free — more replicas means more round-trips for every write to reach
quorum, directly trading write latency for fault tolerance. 5-node etcd
clusters are the common production ceiling for exactly this reason; going
larger rarely makes sense.

**FOLLOW-UP QUESTIONS:**
- What happens to the cluster if etcd loses quorum entirely — can reads
  still succeed?
- How would you safely add a member to an existing etcd cluster without
  risking quorum loss mid-operation?
- Why is etcd latency-sensitive to disk I/O specifically, more than most
  databases?

**RED FLAGS:** Not knowing that etcd availability requires a majority
quorum — leads to wrong sizing decisions ("more replicas is always
safer").

---

### Q9. What's the difference between the scheduler's *filtering* and *scoring* phases?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Kubernetes Engineer, Platform Engineer

**ANSWER:** **Filtering** eliminates nodes that *cannot* run the pod at
all (insufficient resources, taints without matching tolerations, node
affinity mismatch) — a hard yes/no per node. **Scoring** ranks the
remaining feasible nodes to pick the *best* one (spreading pods for
availability, bin-packing for efficiency, respecting topology spread
constraints) — a soft preference, not a hard requirement.

**SENIOR-LEVEL ANSWER:** Confusing these two phases is a common source of
scheduling debugging mistakes: a pod stuck `Pending` is a **filtering**
problem (no node passes the hard constraints — check
`kubectl describe pod` for the specific reason), while a pod landing on
an unexpected-but-technically-fine node is a **scoring** outcome (all
candidate nodes passed filtering, the scheduler just weighted them
differently than you expected) — these need completely different
debugging approaches, and treating a scoring "surprise" as if it were a
filtering "failure" wastes investigation time.

**FOLLOW-UP QUESTIONS:**
- Give an example of a filtering constraint and a scoring preference for
  the exact same underlying concern (e.g. spreading pods across zones).
- How would you debug a pod stuck `Pending` when `kubectl describe`
  doesn't clearly explain why?
- What's a custom scheduler, and when would you need one instead of
  configuring the default scheduler's plugins?

**RED FLAGS:** Treating scheduling as a single opaque step rather than
two distinct phases with distinct failure modes.

---

### Q10. What's the difference between a Deployment and a StatefulSet, beyond "one is for stateful apps"?

**DIFFICULTY:** 🟢 Beginner / 🔵 Intermediate
**ROLE:** Kubernetes Engineer, Platform Engineer

**ANSWER:** A Deployment's pods are interchangeable — any replica can be
replaced by any other, pod names are randomly suffixed, and there's no
guaranteed identity or ordering. A StatefulSet gives each pod a **stable,
predictable identity** (ordinal-suffixed names like `db-0`, `db-1`), a
**stable network identity** (via a headless Service), **stable storage**
(each pod gets its own PVC that survives rescheduling, matched by
ordinal), and **ordered, sequential** creation/scaling/termination.

**SENIOR-LEVEL ANSWER:** The identity/ordering guarantees exist because
many stateful systems (databases, distributed consensus systems) have
real, hard requirements around "which specific instance holds which
data/role" that a Deployment's interchangeable-pod model cannot express
at all. The practical trap: StatefulSets are sometimes reached for by
default for anything "stateful," when the actual requirement is often
just "needs a persistent volume" (which a Deployment can also have, via a
shared or dynamically-provisioned PVC per replica in some patterns) —
StatefulSet's real value is specifically the **ordinal identity and
ordering guarantees**, not persistent storage alone. If your workload
doesn't actually need stable per-pod identity, a StatefulSet adds
operational complexity (slower rolling updates due to ordering, more
complex scaling behavior) for no real benefit.

**FOLLOW-UP QUESTIONS:**
- Why does scaling down a StatefulSet remove the highest-ordinal pod
  first, always?
- What happens to a StatefulSet pod's PVC when the pod is deleted —
  does it get cleaned up automatically?
- When would a Deployment with a shared persistent volume actually be
  wrong, requiring a StatefulSet instead?

**RED FLAGS:** "Use StatefulSet for anything with a database" without
being able to explain what specifically a Deployment can't provide for
that workload.

---

### Q11. How does Kubernetes Service DNS resolution actually work — what does `my-svc.my-namespace.svc.cluster.local` resolve to?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Kubernetes Engineer, SRE

**ANSWER:** CoreDNS (running as cluster pods, per Q1's control-plane
pattern) watches the API server for Service objects and serves DNS
records for them. For a normal (ClusterIP) Service, the name resolves to
the Service's stable virtual IP; `kube-proxy` (or the CNI's equivalent
mechanism) then load-balances traffic to that virtual IP across the
Service's healthy pod Endpoints.

**SENIOR-LEVEL ANSWER:** The layer that trips people up: DNS resolution
and traffic routing are **two separate mechanisms** — DNS just resolves a
name to the Service's virtual IP; it says nothing about *which pod*
ultimately receives a given connection. This is why a DNS-level check
("the name resolves fine") doesn't prove traffic actually reaches a
healthy pod — per the Endpoints-based debugging in
`kubernetes/troubleshooting.md` Lab 3, a Service with correct DNS but zero
healthy Endpoints resolves perfectly and still routes nowhere. Debugging
"can't reach this Service" needs to check both layers independently, not
assume DNS success implies routing success.

**FOLLOW-UP QUESTIONS:**
- What's a headless Service, and why does it change what DNS returns?
- How does DNS resolution differ for a Service versus a specific Pod?
- What's the actual mechanism `kube-proxy` uses to route to Endpoints —
  iptables vs. IPVS, and why does that choice matter at scale?

**RED FLAGS:** Conflating "DNS resolves" with "the Service is working" —
these are genuinely independent failure points.

---

### Q12. Compare Ingress and the Gateway API — why does Gateway API exist when Ingress already solved HTTP routing?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Kubernetes Engineer, Platform Engineer

**ANSWER:** Ingress provides a minimal, widely-adopted spec for
HTTP(S) routing into a cluster, but its spec is deliberately narrow —
anything beyond basic host/path routing (traffic splitting, header-based
routing, non-HTTP protocols) requires vendor-specific annotations, which
aren't portable across ingress controllers. Gateway API is a newer,
more expressive, role-oriented spec designed to standardize that
richer functionality without falling back to per-vendor annotations.

**SENIOR-LEVEL ANSWER:** The "role-oriented" part is the actually
important design change, not just "more features": Gateway API
separates concerns into distinct resource types owned by different
personas — a platform team manages `GatewayClass`/`Gateway` (the
underlying infrastructure), while application teams manage `HTTPRoute`
(their own routing rules) — mirroring the same platform-engineering
separation of concerns discussed in
`platform-engineering/internal-developer-platforms/`. Ingress's single
flat resource type conflates infrastructure and application concerns,
which is part of why vendor annotations became necessary to express
anything beyond the basics — there was no clean place to put
infrastructure-level configuration separately from routing rules.

**FOLLOW-UP QUESTIONS:**
- What's a concrete routing capability Gateway API supports natively that
  Ingress can only achieve via vendor-specific annotations?
- Would you migrate an existing Ingress-based cluster to Gateway API
  today — what factors would drive that decision?
- How does Gateway API's role separation map onto RBAC design for a
  multi-tenant cluster?

**RED FLAGS:** Describing Gateway API as "just a new version of Ingress"
without mentioning the role-separation design change.

---

### Q13. Explain taints and tolerations, and how they differ from node affinity.

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Kubernetes Engineer, Platform Engineer

**ANSWER:** A **taint** on a node repels pods by default — a pod is only
schedulable there if it has a matching **toleration**. **Node affinity**
on a pod does the opposite: it *attracts* the pod toward (or away from)
nodes matching a label selector, but doesn't repel other pods that lack
the affinity rule.

**SENIOR-LEVEL ANSWER:** The practical distinction: taints/tolerations
are the right tool when the **node** needs to control who can land there
(dedicated GPU nodes that should reject anything without an explicit GPU
toleration, by default) — the node is asserting a restriction. Affinity
is the right tool when the **pod** has a preference about where it wants
to run, without needing to restrict what else *can* run there. A common
production pattern combines both: taint dedicated nodes (so nothing lands
there by accident) *and* set matching affinity/tolerations on the
workloads that should use them (so they're not just theoretically
allowed, but actually preferentially scheduled there) — using only one of
the two mechanisms alone usually doesn't fully express the actual intent.

**FOLLOW-UP QUESTIONS:**
- What's the difference between `NoSchedule`, `PreferNoSchedule`, and
  `NoExecute` taint effects?
- How would you safely drain a node using `NoExecute` without causing an
  unplanned outage for pods without matching tolerations?
- What's topology spread constraints, and how does it relate to (but
  differ from) affinity/anti-affinity?

**RED FLAGS:** Treating taints and affinity as interchangeable — they
solve different halves of the same problem (node-side restriction vs.
pod-side preference).

---

### Q14. How does Kubernetes RBAC actually evaluate a request — walk through Role, RoleBinding, ClusterRole, and ClusterRoleBinding.

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** DevSecOps, Platform Engineer, Kubernetes Engineer

**ANSWER:**
- **Role**: a set of permissions (verbs on resources), scoped to a single
  namespace.
- **ClusterRole**: the same, but cluster-scoped (applies cluster-wide, or
  can be bound namespace-scoped for reusability).
- **RoleBinding**: grants a Role (or a ClusterRole, used namespace-scoped)
  to a subject (user/group/service account), within one namespace.
- **ClusterRoleBinding**: grants a ClusterRole cluster-wide, across every
  namespace.

**SENIOR-LEVEL ANSWER:** The non-obvious, frequently-misused combination:
a **ClusterRole bound via a RoleBinding** (not a ClusterRoleBinding) is a
legitimate, common pattern — it lets you define a permission set *once*
(the ClusterRole, reusable across namespaces) while granting it
*narrowly*, one namespace at a time (the RoleBinding). Missing this
pattern leads to two bad outcomes: either duplicating identical Role
definitions across every namespace (maintenance burden), or reaching for
a ClusterRoleBinding out of convenience when only one namespace actually
needed the access (unnecessary over-privilege — the exact opposite of
least privilege). RBAC review should always check *which binding type*
was used, not just what permissions the Role/ClusterRole itself grants —
the binding type is what determines actual scope.

**FOLLOW-UP QUESTIONS:**
- How would you audit a cluster for over-privileged ClusterRoleBindings?
- What's the risk of a ServiceAccount with `cluster-admin` bound via
  ClusterRoleBinding, concretely — walk through an attack scenario?
- How does RBAC interact with admission-controller-based policy (Kyverno/
  OPA) — do they overlap or complement each other?

**RED FLAGS:** Not knowing that a ClusterRole can be bound namespace-
scoped via a RoleBinding — leads to either duplicated Roles or
unnecessary cluster-wide grants.

---

### Q15. What's an admission controller, and what's the difference between a mutating and a validating one?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** DevSecOps, Platform Engineer

**ANSWER:** Admission controllers intercept requests to the API server
*after* authentication/authorization but *before* the object is
persisted to etcd (per Q7). **Mutating** admission controllers can modify
the object (inject a sidecar, set a default resource limit).
**Validating** admission controllers can only accept or reject it, not
change it. Mutating webhooks always run before validating ones, so
validation sees the final, mutated object.

**SENIOR-LEVEL ANSWER:** The ordering guarantee (mutate-then-validate) is
what makes this a coherent policy pipeline rather than a race condition —
a mutating webhook that injects required labels, and a validating webhook
that rejects objects missing those labels, can safely compose, because
validation is guaranteed to see the post-mutation state. The operational
risk worth naming: admission webhooks are **synchronous and on the
critical path of every matching API request** — a slow or unavailable
webhook (misconfigured `failurePolicy`, network issue reaching the
webhook service) can degrade or completely block object creation
cluster-wide for whatever resource types it's configured to intercept.
`failurePolicy: Fail` (reject on webhook unavailability) is safer from a
policy-enforcement standpoint but riskier from an availability
standpoint than `failurePolicy: Ignore` — a real trade-off, not a
default to set blindly.

**FOLLOW-UP QUESTIONS:**
- What's the blast radius if a validating webhook for Pod creation
  becomes unavailable cluster-wide, under each `failurePolicy` setting?
- How would you test an admission webhook's behavior before deploying it
  to production?
- How does this relate to Kyverno/OPA Gatekeeper specifically — are they
  admission controllers themselves, or something that configures them?

**RED FLAGS:** Not recognizing that admission webhooks are synchronous
and can become an availability bottleneck — treating them as purely a
policy concern with no operational risk.

---

### Q16. Walk through a Kubernetes version upgrade — what actually needs to happen, and in what order?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Platform Engineer, SRE, Kubernetes Engineer

**ANSWER:** Control plane components upgrade first (API server, then
controller-manager/scheduler — API server must be upgraded first since
it must always be at or above the version of other control-plane
components), then etcd (if needed), then worker nodes (typically
drained-and-replaced or in-place upgraded one at a time, respecting
PodDisruptionBudgets).

**SENIOR-LEVEL ANSWER:** The real engineering discipline isn't just
knowing the order — it's respecting Kubernetes' **version skew
policy**: the API server can be at most a fixed number of minor versions
ahead of kubelet on any given node (commonly framed as "kubelet can be up
to N minor versions behind the API server," check current official skew
policy rather than assuming a fixed number never changes), which means
worker-node upgrades can safely lag the control plane by a bounded
window, not indefinitely. A senior-level upgrade plan explicitly checks
**deprecated/removed API versions** before upgrading (a workload using an
API version removed in the target version will break, not just warn) —
this is the single most common cause of upgrade-day surprises, and is
checkable in advance via tools that scan manifests/cluster state against
the target version's removed APIs, rather than discovering it live during
the upgrade.

**FOLLOW-UP QUESTIONS:**
- How would you check for deprecated/removed APIs in use before starting
  an upgrade?
- Why must the API server always be upgraded first, never last?
- How does this process change for the 120-cluster fleet scenario in
  `kubernetes/senior-scenarios.md` S2 — what's different at that scale?

**RED FLAGS:** Not mentioning API deprecation/removal checks — the most
common real-world upgrade failure mode.

---

### Q17. What's the difference between HorizontalPodAutoscaler (HPA) and VerticalPodAutoscaler (VPA), and why can't you naively use both on the same workload?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Platform Engineer, SRE, Kubernetes Engineer

**ANSWER:** HPA scales the **number of replicas** based on observed
metrics (CPU, memory, or custom metrics). VPA adjusts each pod's
**resource requests/limits** based on observed usage over time, and
requires recreating the pod to apply a new value (it cannot resize a
running container's limits in place, in most implementations).

**SENIOR-LEVEL ANSWER:** Running HPA (scaling on CPU utilization) and VPA
(changing the CPU *request* that utilization is calculated against) on
the **same metric for the same workload simultaneously** creates a
feedback loop: VPA changes the request, which changes what "80%
utilization" even means for that pod, which changes HPA's scaling
decision, which changes aggregate load per pod, which VPA then reacts to
again. This is a well-known anti-pattern — if combining them at all, VPA
should manage a **different** resource dimension than the one HPA scales
on (e.g. VPA manages memory requests, HPA scales on CPU), or a
`updateMode` on VPA that only recommends rather than automatically
applies changes.

**FOLLOW-UP QUESTIONS:**
- What's VPA's `updateMode: Off` used for, if it doesn't actually change
  anything automatically?
- How does KEDA relate to HPA — is it a replacement or a superset?
- Why does VPA typically require pod recreation to apply a new resource
  value, and what's the availability impact of that?

**RED FLAGS:** Suggesting HPA and VPA on the same metric as a
straightforward combination — misses the feedback-loop risk entirely.

---

### Q18. What's the difference between a Job and a CronJob's failure handling, and what does `backoffLimit` actually control?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Kubernetes Engineer, Platform Engineer

**ANSWER:** A Job runs a pod (or several, per `completions`/`parallelism`)
to completion, retrying failed pods up to `backoffLimit` times before
marking the Job itself as failed. A CronJob schedules Jobs on a cron
schedule, with its own separate concerns: `concurrencyPolicy` (what
happens if a previous run is still active when the next is due) and
`startingDeadlineSeconds` (how late a missed schedule can still start
before being skipped).

**SENIOR-LEVEL ANSWER:** The `concurrencyPolicy` default (`Allow`,
letting overlapping runs execute concurrently) is a common source of
production incidents for CronJobs whose work isn't safely
parallelizable/idempotent — a job that takes longer than its schedule
interval under load will silently start overlapping instances, which for
something like a database migration or a non-idempotent batch job can
cause real data problems, not just wasted compute. `Forbid` (skip the new
run if one's still active) or `Replace` (kill the old, start the new) are
frequently the *actually intended* behavior and need to be set explicitly
— relying on the `Allow` default is rarely a deliberate choice, usually
just an oversight.

**FOLLOW-UP QUESTIONS:**
- What happens to a Job's pods after the Job completes successfully — are
  they cleaned up automatically?
- How would you debug a CronJob that silently stopped running on
  schedule?
- What's the risk of a very long-running Job combined with a tight
  `activeDeadlineSeconds`?

**RED FLAGS:** Not knowing `concurrencyPolicy` exists or defaults to
`Allow` — a real, common production incident source.

---

### Q19. What's the difference between a ConfigMap and a Secret, given both just store key-value data?

**DIFFICULTY:** 🟢 Beginner / 🔵 Intermediate
**ROLE:** All infra/platform roles, DevSecOps

**ANSWER:** Functionally, both inject configuration data into pods (as
environment variables or mounted files) via nearly identical mechanisms.
The distinction is entirely about **intent and handling**: Secrets are
base64-encoded (not encrypted by default — a common misconception) and
Kubernetes/tooling treats them with additional care in places (excluded
from some logging, `kubectl get` doesn't show values by default), signaling
"this is sensitive," whereas ConfigMaps carry no such signal or handling.

**SENIOR-LEVEL ANSWER:** The "base64 is not encryption" point matters
operationally — a Secret stored in etcd without **encryption at rest**
configured is only obfuscated, not protected; anyone with etcd access (or
API access to read Secrets, given sufficient RBAC permissions) can
trivially decode it. Real protection requires either etcd encryption at
rest, or better, not storing genuinely sensitive values as native
Kubernetes Secrets at all — using an external secrets platform (per the
Secrets Management Platform case study in
`system-design/case-studies/`) with the External Secrets Operator syncing
short-lived values in, so the source of truth and its access controls
live outside Kubernetes' own (comparatively weaker, by default) Secret
handling.

**FOLLOW-UP QUESTIONS:**
- How would you verify whether etcd encryption at rest is actually
  enabled on a given cluster?
- What RBAC permissions would let someone read Secret values, and how
  would you audit for over-broad grants?
- Why is mounting a Secret as a volume generally considered safer than
  injecting it as an environment variable?

**RED FLAGS:** Believing Secrets are encrypted by default just because
they're a distinct resource type from ConfigMaps.

---

### Q20. What's a Custom Resource Definition (CRD), and how does it relate to the Operator pattern discussed in Q3?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Platform Engineer, Kubernetes Engineer

**ANSWER:** A CRD extends the Kubernetes API with a new object type — once
registered, instances of that type (Custom Resources) can be created, read,
updated, watched, and RBAC-controlled exactly like any built-in object
(Pods, Deployments). A CRD alone just defines the *schema*; it does
nothing on its own. An Operator (Q3) is the controller that actually
watches instances of that CRD and reconciles real-world state to match.

**SENIOR-LEVEL ANSWER:** This CRD-plus-controller pattern is what makes
Kubernetes genuinely **extensible as a platform**, not just a container
scheduler — it's the mechanism underneath GitOps tools (Argo CD's
`Application` CRD), policy engines (Kyverno's `ClusterPolicy` CRD), and
essentially every "Kubernetes-native" tool you install. The senior-level
distinction worth naming in review: a CRD with **no corresponding
controller running** is inert — you can create the objects, but nothing
reconciles them, so they're just inert API data. This is a real
operational gotcha during migrations/upgrades: if an Operator is
mistakenly removed or fails to start while its CRDs and CR instances
still exist, everything *looks* fine at the API level (`kubectl get`
still works) while nothing is actually being reconciled anymore —
silent, not loud, failure.

**FOLLOW-UP QUESTIONS:**
- How would you detect that a CRD's controller has stopped reconciling,
  given the API objects themselves still look normal?
- What's the difference between a CRD and API aggregation (a fully custom
  API server), and when would you need the latter?
- How does CRD versioning/conversion work when you need to change a
  Custom Resource's schema without breaking existing instances?

**RED FLAGS:** Conflating "CRD exists" with "something is actively
managing it" — these are independent facts.

---

### Q21. What's the difference between `ResourceQuota` and `LimitRange`, and why do you often need both?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Platform Engineer

**ANSWER:** `ResourceQuota` caps **aggregate** resource consumption
(and/or object counts) within a namespace — total CPU/memory requested
across all pods, or a max number of Services. `LimitRange` sets
**per-object** defaults and min/max bounds (a default request if a pod
spec doesn't specify one, or a hard min/max a single container's request
can be) within a namespace.

**SENIOR-LEVEL ANSWER:** They solve different failure modes, which is
why real production namespaces typically need both. `ResourceQuota`
alone doesn't stop one enormous pod from consuming the *entire* quota by
itself, starving everything else in the namespace — `LimitRange`'s
per-object max prevents that specific failure. Conversely, `LimitRange`
alone doesn't cap total namespace consumption across *many* reasonably-
sized pods — `ResourceQuota`'s aggregate cap is what prevents that. This
is directly the multi-tenant isolation pattern discussed generally in
`kubernetes/senior-scenarios.md` S3 (CI build-agent isolation) — that
scenario's "mandatory resource requests via policy" plus "ResourceQuota +
LimitRange per namespace" recommendation is these two mechanisms working
together for exactly the reason explained here.

**FOLLOW-UP QUESTIONS:**
- What happens when a pod is submitted that would exceed the namespace's
  ResourceQuota — is it rejected, or does it schedule and get evicted
  later?
- How would `LimitRange` defaults interact with a pod spec that sets a
  request for CPU but not memory?
- How do these interact with cluster-level (not namespace-level) capacity
  planning?

**RED FLAGS:** Using only one of the two mechanisms and not recognizing
the specific failure mode the other one exists to prevent.

---

### Q22. What's the actual mechanism by which `kubectl logs` retrieves output, and why does it fail differently for a crashed container versus a container stuck in `ImagePullBackOff`?

**DIFFICULTY:** 🟠 Senior
**ROLE:** SRE, Kubernetes Engineer

**ANSWER:** `kubectl logs` asks the API server, which proxies the request
to the **kubelet** on the node running that pod, which in turn reads the
container's stdout/stderr log stream from the container runtime (via
CRI). For a container that never started (`ImagePullBackOff`), there's no
log stream to read at all — the error you get is fundamentally different
in kind (a scheduling/pull failure, surfaced via `kubectl describe`/
events) from a container that started, produced logs, and then crashed
(where `--previous` per the kubectl cheat sheet retrieves the crashed
instance's actual output).

**SENIOR-LEVEL ANSWER:** Recognizing which category a failure falls into
— **never started** vs. **started then failed** — immediately tells you
which command actually has a chance of surfacing useful information,
which matters under real time pressure: running `kubectl logs` against a
pod that never started wastes a debugging cycle for information that
was never going to exist, when `kubectl describe`/events was the right
first move. This distinction is the same "isolate which layer failed
before debugging that layer" discipline discussed generally in the
[Follow the Request](../mental-models/follow-the-request.md) mental model,
applied specifically to container lifecycle rather than a network
request.

**FOLLOW-UP QUESTIONS:**
- What's the full container lifecycle state machine (`Waiting`,
  `Running`, `Terminated`) and which states does each map to?
- Why can `kubectl logs` sometimes work against a node even when the API
  server itself is under heavy load — what's actually being proxied?
- What's `kubectl debug` / ephemeral containers useful for, that `kubectl
  logs`/`exec` can't provide on their own?

**RED FLAGS:** Running the same debugging command reflexively regardless
of which failure category applies — signals no real mental model of the
container lifecycle.

---

### Q23. What's topology spread constraints, and how is it different from (and complementary to) pod anti-affinity?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Kubernetes Engineer, SRE

**ANSWER:** Pod anti-affinity expresses "don't co-locate with pods
matching this label" as a binary preference/requirement per pod pair.
Topology spread constraints express a **quantitative, cluster-wide
evenness goal** across a topology domain (zone, node, custom label) —
"keep the max skew between any two zones' pod counts at or below N" —
which scales far better to large replica counts than pairwise
anti-affinity rules, which get computationally expensive and harder to
reason about as replica count grows.

**SENIOR-LEVEL ANSWER:** The senior-level distinction: anti-affinity
answers "should THIS pod avoid THAT pod," while topology spread answers
"is the WHOLE SET evenly distributed" — for a workload with many replicas
where the actual goal is genuine even spread across failure domains
(availability, not just "don't put two on the same node"), topology
spread constraints are the more correct and more scalable tool, and
combining `whenUnsatisfiable: DoNotSchedule` (hard requirement) with a
reasonable `maxSkew` gives you availability guarantees anti-affinity
rules alone don't cleanly express at scale.

**FOLLOW-UP QUESTIONS:**
- What's the difference between `whenUnsatisfiable: DoNotSchedule` and
  `ScheduleAnyway` for topology spread constraints?
- How would you verify actual pod distribution matches your topology
  spread intent, after the fact?
- When would you still want pod anti-affinity even if using topology
  spread constraints for the primary spread goal?

**RED FLAGS:** Not knowing topology spread constraints exist as a
distinct mechanism from anti-affinity — defaults to pairwise
anti-affinity even for large-replica-count spread goals where it scales
poorly.

---

### Q24. What's the CSI (Container Storage Interface), and why does dynamic volume provisioning depend on it?

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Platform Engineer, Kubernetes Engineer

**ANSWER:** CSI is a standard interface storage vendors implement so their
storage systems work with Kubernetes without vendor-specific code baked
into Kubernetes core (mirroring CNI/CRI's role for networking/runtimes,
per Q1). A `StorageClass` references a CSI driver; when a `PersistentVolumeClaim`
requests that StorageClass, the CSI driver dynamically provisions an
actual volume on the backing storage system and Kubernetes binds it to
the claim — no cluster admin needs to pre-create volumes by hand.

**SENIOR-LEVEL ANSWER:** Before CSI (and its in-tree predecessor
mechanisms), storage vendor integrations lived directly in Kubernetes'
own codebase — meaning a storage vendor needed to get code merged into
core Kubernetes and wait for a release cycle to ship a fix or new
capability. CSI decouples that entirely: a storage vendor ships and
versions their own driver independently, and clusters just install
whichever CSI driver(s) they need. Operationally, this means storage
reliability for a given backend is now largely a function of that
specific CSI driver's maturity/quality, not Kubernetes core — when
diagnosing a stuck `PersistentVolumeClaim`, checking the CSI driver
controller's own logs (not just Kubernetes events) is frequently where
the actual answer lives.

**FOLLOW-UP QUESTIONS:**
- What's the difference between a CSI controller plugin and a CSI node
  plugin — what does each actually run and do?
- What would cause a PVC to stay `Pending` indefinitely, and how would
  you narrow down whether it's a Kubernetes-level or CSI-driver-level
  issue?
- How does volume snapshotting relate to CSI — is it a separate spec?

**RED FLAGS:** Not knowing that storage driver logic lives outside
Kubernetes core via CSI — leads to debugging storage issues purely
through `kubectl`/Kubernetes events while ignoring the CSI driver's own
logs.

---

### Q25. What's the difference between `kubectl delete pod` and letting a Deployment's rolling update replace a pod — why does the distinction matter operationally?

**DIFFICULTY:** 🟠 Senior
**ROLE:** SRE, Platform Engineer

**ANSWER:** `kubectl delete pod` directly against a Deployment-managed pod
triggers the **ReplicaSet controller** to notice the missing replica and
create a new one immediately, with no control over rollout pacing —
functionally a manual, instantaneous, single-pod restart. A rolling
update (changing the Deployment's pod template) is governed by
`maxUnavailable`/`maxSurge` and proceeds through **all** replicas in a
controlled, paced sequence, respecting readiness checks before proceeding
to the next batch.

**SENIOR-LEVEL ANSWER:** The operational risk of reaching for
`kubectl delete pod` as a "quick fix" (restarting a pod that seems stuck)
is that it bypasses every rollout-pacing safeguard entirely — deleting
pods manually and rapidly (e.g. via a loop, or deleting several at once
under pressure during an incident) can trigger simultaneous replacement
of many pods at once, momentarily dropping available capacity far below
what a properly-paced rolling update would ever allow, especially if
combined with a PodDisruptionBudget that wasn't designed to account for
this manual path (per the PDB fundamentals question — PDBs govern
*voluntary* disruption broadly, but a burst of manual deletes can still
create a worse availability dip than a deliberate rollout would). The
senior instinct under incident pressure: prefer `kubectl rollout restart
deployment/<name>` (which *does* respect rollout pacing) over manually
deleting individual pods, unless there's a specific reason the paced
rollout path itself is unavailable.

**FOLLOW-UP QUESTIONS:**
- What does `kubectl rollout restart` actually change under the hood to
  trigger new pods, given the pod template itself doesn't change?
- How would `maxUnavailable: 0` change the risk profile of a rolling
  update, and what does it cost you in return?
- Walk through what happens if you delete pods faster than the
  ReplicaSet controller can reconcile — is there a rate limit?

**RED FLAGS:** Treating `kubectl delete pod` as a routine "quick fix"
technique without acknowledging it bypasses rollout pacing and PDB-aware
sequencing.
