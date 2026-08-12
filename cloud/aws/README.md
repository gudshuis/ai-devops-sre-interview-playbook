# AWS

## What this cloud platform is

AWS is a general-purpose cloud platform that gives teams managed primitives for identity, networking, compute, data, observability, and governance. The engineering challenge is not memorizing product names; it is understanding how the platform's boundaries shape production reliability, security, cost, and developer speed.

## Core architecture

Production architecture on AWS usually starts with strong isolation boundaries, explicit network paths, workload identity, managed observability, and deliberate regional design. Mature teams separate foundational platform concerns from application concerns so that access, networking, compliance, and logging do not have to be reinvented by every product team.

## Main services

- **IAM and Organizations:** Identity, policy boundaries, and account-level governance.
- **VPC and Route 53:** Network segmentation, routing, DNS, and hybrid connectivity.
- **EC2, Lambda, ECS, and EKS:** Compute choices spanning VM, serverless, container, and Kubernetes models.
- **S3, EBS, EFS, and FSx:** Object, block, and shared file storage.
- **RDS, Aurora, DynamoDB, and ElastiCache:** Transactional, key-value, and caching data services.
- **CloudWatch, CloudTrail, and X-Ray:** Metrics, logs, traces, and auditability.

## Identity

IAM roles, STS, Organizations SCPs, IAM Identity Center, IRSA, and KMS-backed secret access patterns.

## Networking

VPCs, subnets, route tables, Transit Gateway, VPC endpoints, Route 53, Global Accelerator, and PrivateLink.

## Compute

EC2, Auto Scaling Groups, Lambda, ECS, EKS, and Nitro-based isolation.

## Containers/Kubernetes

Managed Kubernetes is valuable when teams need a consistent scheduling and policy layer, but it also shifts responsibility toward cluster lifecycle, node security, admission controls, and cross-team platform ownership.

## Storage

S3, EBS, EFS, FSx, lifecycle tiers, and encryption patterns.

## Databases

RDS, Aurora, DynamoDB, ElastiCache, and cross-region replication choices.

## Observability

CloudWatch, X-Ray, CloudTrail, VPC Flow Logs, GuardDuty, and centralized log archives.

## Security

Multi-account landing zones, SCP guardrails, workload identity, KMS, Security Hub, and Detective.

## Cost management

Savings Plans, reserved capacity, tagging, CUR analysis, and cost allocation across accounts.

## Resilience

Multi-AZ by default where possible, region evacuation planning, and explicit DR tiers per workload.

## Multi-region

Use AWS Regions for fault domains and data locality; use Route 53, Global Accelerator, or application-level replication for failover.

## Disaster recovery

DR should be explicit per service tier: recovery time objective, recovery point objective, identity dependencies, control-plane dependencies, replication patterns, backup validation, and region-failover runbooks.

## Production design considerations

- Design around clear blast-radius boundaries before optimizing for convenience.
- Prefer short-lived identities and centrally enforced policy over local exceptions.
- Make network paths observable and intentionally private where possible.
- Pick compute abstractions that match the team’s operational maturity.
- Treat quotas, regional limits, and service dependencies as first-class architecture inputs.
- Standardize evidence collection so incident response does not depend on portal clicks.

## Learning and interview Q&A

## Question 01 — How would you explain the difference between blast radius reduction and convenience in AWS account design?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 02 — Why do mature AWS estates prefer role assumption over long-lived credentials?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 03 — How would you design private service access without exposing traffic to the public internet?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 04 — When does a single VPC per environment stop being sufficient?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 05 — What are the operational consequences of choosing Lambda for latency-sensitive services?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 06 — How do you reason about stateful workloads on EKS?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 07 — Why do many teams misuse security groups during incidents?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 08 — How would you debug intermittent database failures from private subnets?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 09 — What should a senior engineer mention when comparing EKS and ECS?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 10 — How do you explain eventual consistency trade-offs in S3-backed designs?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 11 — What does a good KMS key-management model look like in a multi-team org?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 12 — How would you discuss failover strategy between two AWS regions?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 13 — What should you monitor first for NAT gateway saturation or cost spikes?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 14 — How do SCPs change the way teams troubleshoot permissions?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 15 — What are the architectural trade-offs between Aurora, DynamoDB, and self-managed databases?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 16 — How would you control observability cost without losing incident response quality?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 17 — What does a strong answer about AWS network segmentation sound like?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 18 — How do you structure account vending and guardrails for a platform team?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 19 — How should teams use Route 53 health checks and failover policies safely?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 20 — When is PrivateLink better than VPC peering or Transit Gateway?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 21 — How would you talk through a zero-trust identity strategy on AWS?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 22 — What would you optimize first in a multi-account cost reduction program?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 23 — How should a senior engineer reason about quotas before a region launch?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 24 — How do you explain AWS backup and DR choices to non-specialists?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 25 — What would a strong staff-level answer about enterprise AWS platforms include?

**Answer:** In AWS, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
