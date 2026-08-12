# GCP

## What this cloud platform is

GCP is a general-purpose cloud platform that gives teams managed primitives for identity, networking, compute, data, observability, and governance. The engineering challenge is not memorizing product names; it is understanding how the platform's boundaries shape production reliability, security, cost, and developer speed.

## Core architecture

Production architecture on GCP usually starts with strong isolation boundaries, explicit network paths, workload identity, managed observability, and deliberate regional design. Mature teams separate foundational platform concerns from application concerns so that access, networking, compliance, and logging do not have to be reinvented by every product team.

## Main services

- **IAM, folders, and org policies:** Identity, project boundaries, and enterprise governance.
- **VPC, Shared VPC, PSC, and Cloud DNS:** Network isolation, service access, and hybrid connectivity.
- **Compute Engine, Cloud Run, Functions, and GKE:** Core compute choices for application delivery.
- **Cloud Storage, Persistent Disk, and Filestore:** Object, block, and shared file storage.
- **Cloud SQL, AlloyDB, Spanner, and Bigtable:** Managed database choices across consistency and scale patterns.
- **Cloud Monitoring, Logging, Trace, and Audit Logs:** Operational visibility and incident evidence.

## Identity

IAM, service accounts, workload identity federation, organization policies, folders, and project-level boundaries.

## Networking

Global VPCs, subnets, firewall rules, Cloud NAT, Cloud DNS, Private Service Connect, Shared VPC, and Cloud Interconnect.

## Compute

Compute Engine, managed instance groups, Cloud Run, GKE, Cloud Functions, and autoscaled regional services.

## Containers/Kubernetes

Managed Kubernetes is valuable when teams need a consistent scheduling and policy layer, but it also shifts responsibility toward cluster lifecycle, node security, admission controls, and cross-team platform ownership.

## Storage

Cloud Storage, Persistent Disk, Filestore, storage classes, lifecycle rules, and CMEK options.

## Databases

Cloud SQL, AlloyDB, Spanner, Bigtable, Memorystore, and replication strategy trade-offs.

## Observability

Cloud Monitoring, Cloud Logging, Error Reporting, Cloud Trace, Audit Logs, VPC Flow Logs, and SCC.

## Security

Organization policies, folders, VPC Service Controls, Secret Manager, KMS, BeyondCorp-style access, and workload identity.

## Cost management

Committed use discounts, autoscaling efficiency, labeling, budgets, and per-project chargeback.

## Resilience

Regional managed services, multi-zonal GKE, multi-region data services, and planned failover mechanisms.

## Multi-region

GCP uses global control planes for many services but region-specific capacity and residency still matter; design failover explicitly.

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

## Question 01 — How would you explain blast radius reduction in GCP project design?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 02 — Why do mature GCP estates prefer short-lived credentials and workload identity over key files?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 03 — How would you design private service access without public exposure in GCP?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 04 — When does a single Shared VPC model stop being sufficient?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 05 — What are the operational consequences of choosing Cloud Run for critical APIs?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 06 — How do you reason about stateful workloads on GKE?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 07 — Why do teams misuse firewall rules during incidents?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 08 — How would you debug intermittent database failures from private GKE workloads?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 09 — What should a senior engineer mention when comparing GKE and Cloud Run?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 10 — How do you explain consistency trade-offs in Spanner-backed designs?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 11 — What does a good KMS and Secret Manager model look like in a multi-team org?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 12 — How would you discuss failover strategy between two GCP regions?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 13 — What should you monitor first for Cloud NAT saturation or egress cost spikes?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 14 — How do org policies change the way teams troubleshoot permissions?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 15 — What are the architectural trade-offs between Cloud SQL, Spanner, and Bigtable?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 16 — How would you control observability cost without losing incident quality?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 17 — What does a strong answer about GCP network segmentation sound like?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 18 — How do you structure project vending and guardrails for a platform team?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 19 — How should teams use global load balancing and health checks safely?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 20 — When is Private Service Connect better than peering or public endpoints?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 21 — How would you talk through a zero-trust identity strategy on GCP?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 22 — What would you optimize first in a multi-project cost reduction program?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 23 — How should a senior engineer reason about quota risk before a regional launch?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 24 — How do you explain GCP backup and DR choices to non-specialists?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 25 — What would a strong staff-level answer about enterprise GCP platforms include?

**Answer:** In GCP, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
