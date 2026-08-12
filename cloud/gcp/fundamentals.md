# GCP Fundamentals

## Question 01 — What is the difference between an organization, folder, project, and VPC boundary in GCP?

**Difficulty:** Beginner

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 02 — How do service accounts differ from human identities in production GCP environments?

**Difficulty:** Beginner

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 03 — What do regions and zones solve in GCP architecture?

**Difficulty:** Beginner

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 04 — How do firewall rules and routes work in a global VPC model?

**Difficulty:** Beginner

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 05 — When should you choose Compute Engine over Cloud Run or GKE?

**Difficulty:** Beginner

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 06 — How does Private Service Connect change the security posture of service access?

**Difficulty:** Beginner

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 07 — What is the operational difference between Cloud Storage classes and redundancy options?

**Difficulty:** Beginner

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 08 — How does Cloud SQL high availability differ from read replicas?

**Difficulty:** Beginner

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 09 — How do folders and org policies help platform teams scale governance?

**Difficulty:** Intermediate

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 10 — What is the role of Workload Identity Federation in secure cloud access?

**Difficulty:** Intermediate

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 11 — How does GKE Workload Identity work?

**Difficulty:** Intermediate

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 12 — What trade-offs exist between Shared VPC, VPC peering, and PSC?

**Difficulty:** Intermediate

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 13 — How does Cloud DNS participate in resilient multi-region systems?

**Difficulty:** Intermediate

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 14 — What is the difference between global external load balancing and regional load balancing in GCP?

**Difficulty:** Intermediate

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 15 — How does Cloud KMS influence secure application design?

**Difficulty:** Intermediate

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 16 — What makes Spanner operationally different from Cloud SQL or AlloyDB?

**Difficulty:** Intermediate

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 17 — How do autoscaling decisions work across MIGs, GKE, and Cloud Run?

**Difficulty:** Intermediate

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 18 — How should teams think about GCP quotas and regional capacity as an architectural constraint?

**Difficulty:** Advanced

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 19 — How do you design a landing zone for many projects and regulated workloads?

**Difficulty:** Advanced

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 20 — What is a good project strategy for platform engineering on GCP?

**Difficulty:** Advanced

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 21 — How do you approach hybrid connectivity with Cloud Interconnect and Cloud VPN?

**Difficulty:** Advanced

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 22 — What are the production trade-offs of GKE versus Cloud Run for a platform team?

**Difficulty:** Advanced

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 23 — How should disaster recovery tiers shape GCP service selection?

**Difficulty:** Advanced

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 24 — How do you centralize observability while preserving project ownership?

**Difficulty:** Advanced

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?

## Question 25 — What are the most important cost-control levers in GCP at scale?

**Difficulty:** Advanced

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant GCP boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In GCP, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

### Example

A practical example would walk through one real workload, such as a private application using managed identity, internal networking, a managed database, and centralized observability. The goal is to show how this concept becomes visible in an actual deployment instead of staying abstract.

### Why it matters in production

Production systems fail when teams misunderstand boundaries. If an engineer cannot say whether the behavior is enforced by identity policy, network policy, a managed service limit, or application logic, the resulting architecture tends to be fragile and hard to debug.

### Common mistakes

- Treating the feature like a checkbox instead of a control boundary.
- Ignoring regional, quota, or tenancy implications.
- Assuming console state and runtime state are always aligned.
- Explaining the feature without mentioning observability or rollback.

### Key points to remember

- Name the controlling boundary.
- State the key dependency edges.
- Call out blast radius and operator visibility.
- Tie the mechanism to a production consequence.

### Follow-up questions

- What evidence would prove this is working correctly?
- Which adjacent control could still break the workload even if this feature is configured correctly?
- How would your answer change at enterprise scale?
