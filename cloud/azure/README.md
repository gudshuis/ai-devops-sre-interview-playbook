# Azure

## What this cloud platform is

Azure is a general-purpose cloud platform that gives teams managed primitives for identity, networking, compute, data, observability, and governance. The engineering challenge is not memorizing product names; it is understanding how the platform's boundaries shape production reliability, security, cost, and developer speed.

## Core architecture

Production architecture on Azure usually starts with strong isolation boundaries, explicit network paths, workload identity, managed observability, and deliberate regional design. Mature teams separate foundational platform concerns from application concerns so that access, networking, compliance, and logging do not have to be reinvented by every product team.

## Main services

- **Entra ID and RBAC:** Identity, role assignments, group-based access, and admin workflow.
- **VNets and Private Link:** Network isolation, service access, and hybrid connectivity.
- **VMs, App Service, Functions, and AKS:** Core compute choices for application platforms.
- **Blob Storage, Managed Disks, and Files:** Object, block, and shared file storage options.
- **Azure SQL, PostgreSQL Flexible Server, and Cosmos DB:** Managed database services and trade-offs.
- **Azure Monitor, Log Analytics, and Application Insights:** Operational visibility and correlation.

## Identity

Microsoft Entra ID, managed identities, role assignments, PIM, subscription management groups, and workload identity for AKS.

## Networking

VNets, subnets, NSGs, UDRs, Azure Firewall, Private Link, DNS Private Resolver, ExpressRoute, and hub-spoke topologies.

## Compute

VMs, VM Scale Sets, App Service, Functions, Container Apps, and AKS.

## Containers/Kubernetes

Managed Kubernetes is valuable when teams need a consistent scheduling and policy layer, but it also shifts responsibility toward cluster lifecycle, node security, admission controls, and cross-team platform ownership.

## Storage

Blob, Files, managed disks, lifecycle policies, geo-redundancy, and encryption settings.

## Databases

Azure SQL, PostgreSQL Flexible Server, Cosmos DB, Cache for Redis, and data replication choices.

## Observability

Azure Monitor, Log Analytics, Application Insights, Activity Logs, NSG flow logs, and Defender for Cloud.

## Security

Management groups, Azure Policy, Key Vault, Defender, Private Link, conditional access, and managed identities.

## Cost management

Reservations, savings plans, cost analysis, budgets, tags, and subscription-level chargeback.

## Resilience

Availability zones, paired regions, zonal services, and recovery plans with Azure Site Recovery or application-level replication.

## Multi-region

Use paired regions, traffic management layers, and service-specific replication patterns to meet DR and residency goals.

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

## Question 01 — How would you explain blast radius reduction in Azure subscription design?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 02 — Why do mature Azure estates prefer managed identities and PIM over shared credentials?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 03 — How would you design private service access to PaaS resources in Azure?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 04 — When does a flat VNet model stop working well on Azure?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 05 — What are the operational consequences of choosing Azure Functions for critical APIs?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 06 — How do you reason about stateful workloads on AKS?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 07 — Why do teams misuse NSGs during incidents?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 08 — How would you debug intermittent database failures from a private subnet in Azure?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 09 — What should a senior engineer mention when comparing AKS and Container Apps?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 10 — How do you explain consistency and partitioning trade-offs in Cosmos DB designs?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 11 — What does a good Key Vault and secret-rotation model look like?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 12 — How would you discuss paired-region failover strategy in Azure?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 13 — What should you monitor first for NAT gateway saturation or SNAT exhaustion?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 14 — How do Azure Policy and RBAC interact during permissions troubleshooting?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 15 — What are the architectural trade-offs between Azure SQL, Cosmos DB, and PostgreSQL Flexible Server?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 16 — How would you control Azure Monitor cost without losing incident fidelity?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 17 — What does a strong answer about Azure network segmentation sound like?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 18 — How do you structure subscription vending and guardrails for a platform team?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 19 — How should teams use Azure Front Door or Traffic Manager for failover safely?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 20 — When is Private Link better than VNet peering or service endpoints?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 21 — How would you talk through a zero-trust identity strategy on Azure?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 22 — What would you optimize first in a multi-subscription cost reduction program?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 23 — How should a senior engineer reason about regional quota risk in Azure?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 24 — How do you explain Azure backup and DR choices to non-specialists?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
## Question 25 — What would a strong staff-level answer about enterprise Azure platforms include?

**Answer:** In Azure, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.
