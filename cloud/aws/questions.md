# AWS Interview Questions

## Question 01 — How would you explain the difference between blast radius reduction and convenience in AWS account design?

**Difficulty:** Intermediate
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 02 — Why do mature AWS estates prefer role assumption over long-lived credentials?

**Difficulty:** Intermediate
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 03 — How would you design private service access without exposing traffic to the public internet?

**Difficulty:** Intermediate
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 04 — When does a single VPC per environment stop being sufficient?

**Difficulty:** Intermediate
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 05 — What are the operational consequences of choosing Lambda for latency-sensitive services?

**Difficulty:** Intermediate
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 06 — How do you reason about stateful workloads on EKS?

**Difficulty:** Intermediate
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 07 — Why do many teams misuse security groups during incidents?

**Difficulty:** Intermediate
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 08 — How would you debug intermittent database failures from private subnets?

**Difficulty:** Intermediate
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 09 — What should a senior engineer mention when comparing EKS and ECS?

**Difficulty:** Advanced
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 10 — How do you explain eventual consistency trade-offs in S3-backed designs?

**Difficulty:** Advanced
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 11 — What does a good KMS key-management model look like in a multi-team org?

**Difficulty:** Advanced
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 12 — How would you discuss failover strategy between two AWS regions?

**Difficulty:** Advanced
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 13 — What should you monitor first for NAT gateway saturation or cost spikes?

**Difficulty:** Advanced
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 14 — How do SCPs change the way teams troubleshoot permissions?

**Difficulty:** Advanced
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 15 — What are the architectural trade-offs between Aurora, DynamoDB, and self-managed databases?

**Difficulty:** Advanced
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 16 — How would you control observability cost without losing incident response quality?

**Difficulty:** Advanced
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 17 — What does a strong answer about AWS network segmentation sound like?

**Difficulty:** Advanced
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 18 — How do you structure account vending and guardrails for a platform team?

**Difficulty:** Advanced
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 19 — How should teams use Route 53 health checks and failover policies safely?

**Difficulty:** Senior
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 20 — When is PrivateLink better than VPC peering or Transit Gateway?

**Difficulty:** Senior
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 21 — How would you talk through a zero-trust identity strategy on AWS?

**Difficulty:** Senior
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 22 — What would you optimize first in a multi-account cost reduction program?

**Difficulty:** Senior
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 23 — How should a senior engineer reason about quotas before a region launch?

**Difficulty:** Senior
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 24 — How do you explain AWS backup and DR choices to non-specialists?

**Difficulty:** Senior
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?

## Question 25 — What would a strong staff-level answer about enterprise AWS platforms include?

**Difficulty:** Senior
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant AWS choice and the primary trade-off behind it.

### Detailed answer

A strong answer explains how the decision changes identity boundaries, network paths, deployment safety, service quotas, observability, and incident response. It should also mention why a team might intentionally choose a less feature-rich but simpler model.

### Production example

Use a concrete example: a platform team serving many applications, a regulated workload, or a migration from a simpler model to a more governed one. Explain what changed, what signals mattered, and which constraint forced the decision.

### Trade-offs

- Simplicity versus flexibility
- Central control versus team autonomy
- Cost efficiency versus reliability margin
- Managed abstraction versus operational control

### What a strong senior candidate should mention

They should mention blast radius, failure isolation, runbooks, observability, rollback, quota risk, and how the design evolves as team count and workload criticality increase.

### Common weak answer

A weak answer lists features or provider products without showing how the decision affects production behavior, incident recovery, or organizational scaling.

### Follow-up questions

- What would break first if this assumption were wrong?
- How would you test this design before an outage tests it for you?
- When would you deliberately choose the alternative?
