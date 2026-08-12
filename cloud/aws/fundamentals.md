# AWS Fundamentals

## Question 01 — What is the difference between an AWS account boundary and a VPC boundary?

**Difficulty:** Beginner

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 02 — How do IAM roles differ from IAM users in production AWS environments?

**Difficulty:** Beginner

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 03 — What problem do availability zones solve in AWS architecture?

**Difficulty:** Beginner

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 04 — How does a subnet become public or private in AWS?

**Difficulty:** Beginner

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 05 — What does a security group control compared with a network ACL?

**Difficulty:** Beginner

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 06 — When should you choose EC2 over Lambda or ECS?

**Difficulty:** Beginner

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 07 — How does S3 durability differ from application availability?

**Difficulty:** Beginner

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 08 — What is the operational difference between RDS Multi-AZ and read replicas?

**Difficulty:** Beginner

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 09 — How does AWS Organizations help platform teams scale governance?

**Difficulty:** Intermediate

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 10 — What is STS and why is it central to secure AWS operations?

**Difficulty:** Intermediate

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 11 — How does IRSA work for EKS workloads?

**Difficulty:** Intermediate

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 12 — What trade-offs exist between NAT gateways and VPC endpoints?

**Difficulty:** Intermediate

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 13 — How does Route 53 participate in resilient multi-region systems?

**Difficulty:** Intermediate

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 14 — What is the difference between ALB, NLB, and API Gateway?

**Difficulty:** Intermediate

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 15 — How does KMS influence the design of secure cloud applications?

**Difficulty:** Intermediate

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 16 — What makes Aurora operationally different from self-managed PostgreSQL on EC2?

**Difficulty:** Intermediate

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 17 — How do Auto Scaling Groups actually decide to add or remove capacity?

**Difficulty:** Intermediate

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 18 — How should teams think about AWS quotas as an architectural constraint?

**Difficulty:** Advanced

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 19 — How do you design a landing zone for many teams and regulated workloads?

**Difficulty:** Advanced

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 20 — What is a good multi-account strategy for platform engineering on AWS?

**Difficulty:** Advanced

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 21 — How do you approach hybrid connectivity with Direct Connect and Transit Gateway?

**Difficulty:** Advanced

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 22 — What are the production trade-offs of EKS versus ECS for a platform team?

**Difficulty:** Advanced

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 23 — How should disaster recovery tiers shape AWS service selection?

**Difficulty:** Advanced

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 24 — How do you centralize observability without breaking team ownership?

**Difficulty:** Advanced

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

## Question 25 — What are the most important cost-control levers in AWS at scale?

**Difficulty:** Advanced

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant AWS boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In AWS, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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
