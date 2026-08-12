#!/usr/bin/env python3
"""Generate provider-specific cloud content packs for AWS, Azure, and GCP."""
from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

PROVIDERS = {
    "aws": {
        "name": "AWS",
        "identity": "IAM roles, STS, Organizations SCPs, IAM Identity Center, IRSA, and KMS-backed secret access patterns.",
        "networking": "VPCs, subnets, route tables, Transit Gateway, VPC endpoints, Route 53, Global Accelerator, and PrivateLink.",
        "compute": "EC2, Auto Scaling Groups, Lambda, ECS, EKS, and Nitro-based isolation.",
        "storage": "S3, EBS, EFS, FSx, lifecycle tiers, and encryption patterns.",
        "databases": "RDS, Aurora, DynamoDB, ElastiCache, and cross-region replication choices.",
        "observability": "CloudWatch, X-Ray, CloudTrail, VPC Flow Logs, GuardDuty, and centralized log archives.",
        "security": "Multi-account landing zones, SCP guardrails, workload identity, KMS, Security Hub, and Detective.",
        "cost": "Savings Plans, reserved capacity, tagging, CUR analysis, and cost allocation across accounts.",
        "resilience": "Multi-AZ by default where possible, region evacuation planning, and explicit DR tiers per workload.",
        "regions": "Use AWS Regions for fault domains and data locality; use Route 53, Global Accelerator, or application-level replication for failover.",
        "services": [
            ("IAM and Organizations", "Identity, policy boundaries, and account-level governance."),
            ("VPC and Route 53", "Network segmentation, routing, DNS, and hybrid connectivity."),
            ("EC2, Lambda, ECS, and EKS", "Compute choices spanning VM, serverless, container, and Kubernetes models."),
            ("S3, EBS, EFS, and FSx", "Object, block, and shared file storage."),
            ("RDS, Aurora, DynamoDB, and ElastiCache", "Transactional, key-value, and caching data services."),
            ("CloudWatch, CloudTrail, and X-Ray", "Metrics, logs, traces, and auditability."),
        ],
        "fundamentals": [
            "What is the difference between an AWS account boundary and a VPC boundary?",
            "How do IAM roles differ from IAM users in production AWS environments?",
            "What problem do availability zones solve in AWS architecture?",
            "How does a subnet become public or private in AWS?",
            "What does a security group control compared with a network ACL?",
            "When should you choose EC2 over Lambda or ECS?",
            "How does S3 durability differ from application availability?",
            "What is the operational difference between RDS Multi-AZ and read replicas?",
            "How does AWS Organizations help platform teams scale governance?",
            "What is STS and why is it central to secure AWS operations?",
            "How does IRSA work for EKS workloads?",
            "What trade-offs exist between NAT gateways and VPC endpoints?",
            "How does Route 53 participate in resilient multi-region systems?",
            "What is the difference between ALB, NLB, and API Gateway?",
            "How does KMS influence the design of secure cloud applications?",
            "What makes Aurora operationally different from self-managed PostgreSQL on EC2?",
            "How do Auto Scaling Groups actually decide to add or remove capacity?",
            "How should teams think about AWS quotas as an architectural constraint?",
            "How do you design a landing zone for many teams and regulated workloads?",
            "What is a good multi-account strategy for platform engineering on AWS?",
            "How do you approach hybrid connectivity with Direct Connect and Transit Gateway?",
            "What are the production trade-offs of EKS versus ECS for a platform team?",
            "How should disaster recovery tiers shape AWS service selection?",
            "How do you centralize observability without breaking team ownership?",
            "What are the most important cost-control levers in AWS at scale?",
        ],
        "questions": [
            "How would you explain the difference between blast radius reduction and convenience in AWS account design?",
            "Why do mature AWS estates prefer role assumption over long-lived credentials?",
            "How would you design private service access without exposing traffic to the public internet?",
            "When does a single VPC per environment stop being sufficient?",
            "What are the operational consequences of choosing Lambda for latency-sensitive services?",
            "How do you reason about stateful workloads on EKS?",
            "Why do many teams misuse security groups during incidents?",
            "How would you debug intermittent database failures from private subnets?",
            "What should a senior engineer mention when comparing EKS and ECS?",
            "How do you explain eventual consistency trade-offs in S3-backed designs?",
            "What does a good KMS key-management model look like in a multi-team org?",
            "How would you discuss failover strategy between two AWS regions?",
            "What should you monitor first for NAT gateway saturation or cost spikes?",
            "How do SCPs change the way teams troubleshoot permissions?",
            "What are the architectural trade-offs between Aurora, DynamoDB, and self-managed databases?",
            "How would you control observability cost without losing incident response quality?",
            "What does a strong answer about AWS network segmentation sound like?",
            "How do you structure account vending and guardrails for a platform team?",
            "How should teams use Route 53 health checks and failover policies safely?",
            "When is PrivateLink better than VPC peering or Transit Gateway?",
            "How would you talk through a zero-trust identity strategy on AWS?",
            "What would you optimize first in a multi-account cost reduction program?",
            "How should a senior engineer reason about quotas before a region launch?",
            "How do you explain AWS backup and DR choices to non-specialists?",
            "What would a strong staff-level answer about enterprise AWS platforms include?",
        ],
        "troubleshooting": [
            "An IAM role assumption path suddenly fails after a policy rollout",
            "Private subnets can reach some endpoints but not S3 or STS",
            "Route 53 resolves correctly but requests still fail from one region",
            "ALB shows healthy listeners while users receive 502 responses",
            "EKS nodes join the cluster but workloads cannot pull images",
            "An EBS-backed stateful workload is stuck pending after a node replacement",
            "Applications in one subnet cannot connect to RDS after a change window",
            "PrivateLink consumers time out while the service owner sees no errors",
            "TLS certificates look valid but clients reject the endpoint",
            "EC2 Auto Scaling stops scaling out during a demand spike",
            "A critical deployment fails because a regional service quota was exhausted",
            "CloudWatch dashboards are blank during an active incident",
            "Cross-region failover was triggered but traffic did not shift cleanly",
            "CUR analysis shows a sudden NAT gateway cost spike",
            "An EKS ingress controller loops because AWS load balancer provisioning fails",
            "An S3 replication policy exists but new objects do not replicate",
            "A KMS key policy blocks an application after account reorganization",
            "Lambda functions time out only when calling private services",
            "DynamoDB throttling appears after a tenant onboarding event",
            "Aurora failover completes but the application keeps using the old writer endpoint",
            "CloudTrail logs are missing for one newly vended account",
            "ECR image pulls fail from one node group but not another",
            "A Transit Gateway route propagation mistake isolates an environment",
            "An SSM Session Manager connection fails despite correct instance health",
            "A canary region stays healthy but production users still hit the failed region",
        ],
        "senior": [
            "Design a multi-account AWS landing zone for a regulated company",
            "Move a single-region workload to active-active across two AWS regions",
            "Define a DR strategy for mixed RDS, DynamoDB, and EKS workloads",
            "Create an enterprise identity model using IAM Identity Center and short-lived credentials",
            "Design network segmentation for shared services, developer accounts, and production",
            "Plan hybrid connectivity between AWS and on-prem data centers",
            "Build a centralized EKS platform for many product teams",
            "Design centralized observability across hundreds of AWS accounts",
            "Reduce cloud spend without creating platform friction",
            "Choose between ECS and EKS as the default container platform",
            "Design a workload identity strategy for containers and serverless services",
            "Standardize secrets handling across accounts and regions",
            "Plan region evacuation for a critical customer-facing platform",
            "Design secure cross-account service-to-service access",
            "Create a platform model for multi-tenant SaaS workloads",
            "Set cost guardrails for teams with unpredictable growth",
            "Choose a data residency strategy for global customers",
            "Create a migration plan from a flat account model to a multi-account model",
            "Standardize ingress and edge security across dozens of applications",
            "Design governance for self-service infrastructure while preserving auditability",
            "Plan large-scale EKS fleet management across regions",
            "Choose a backup and recovery operating model for tiered services",
            "Build a zero-trust architecture for internal engineering access",
            "Introduce shared platform services without creating a central bottleneck",
            "Lead a large cloud modernization from legacy EC2 to platform services",
        ],
        "challenges": [
            "Debug an AWS IAM policy that blocks a deployment role",
            "Design a cost-optimized but resilient multi-account network layout",
            "Improve an EKS platform suffering from noisy-neighbor workloads",
            "Secure a public S3 access pattern without breaking legitimate consumers",
            "Reduce NAT gateway and data transfer spend in a busy region",
            "Scale an event-driven Lambda system hitting concurrency limits",
            "Fix a CloudFormation stack that deadlocks on circular dependencies",
            "Fix an IRSA configuration for an application using Secrets Manager",
            "Fix a Transit Gateway routing design that leaks traffic between environments",
            "Analyze an architecture that depends on a single NAT gateway and single AZ database",
            "Design DR for a payments platform using Aurora and EKS",
            "Design multi-region failover for a latency-sensitive API",
            "Troubleshoot EKS control-plane reachability from private worker nodes",
            "Improve CloudWatch observability with sane cost controls",
            "Secure cross-account access for a shared build system",
            "Refactor a flat VPC layout into segmented subnets and shared services",
            "Fix DNS resolution for private hosted zones used across accounts",
            "Reduce S3 request cost for a data-heavy analytics workload",
            "Scale a private API mesh without making TLS management unmanageable",
            "Improve backup validation rather than only backup creation",
            "Fix a broken blue-green deployment using ALB target groups",
            "Secure a KMS key policy model after an organization restructure",
            "Analyze quota risk before onboarding a large enterprise tenant",
            "Improve region-failover runbooks after a failed game day",
            "Troubleshoot a cost spike caused by mis-tagged ephemeral infrastructure",
        ],
        "cheats": [
            ("aws sts get-caller-identity", "Shows the active AWS principal and account", "First check during IAM or auth debugging", "--profile, --region", "aws sts get-caller-identity", "Account number, ARN, and whether the expected role is active", "Helps catch wrong-role assumptions, expired sessions, or shells pointing at the wrong account."),
            ("aws configure list", "Prints the configured credential and region sources", "Confirm where credentials and defaults are coming from", "--profile", "aws configure list --profile prod-admin", "Whether values come from env vars, config files, or IMDS", "Useful when behavior differs between CI, a bastion, and a local laptop."),
            ("aws ec2 describe-instances", "Lists EC2 instance details including subnet, state, and security groups", "Inspect compute placement or missing instance metadata", "--filters, --instance-ids, --query", "aws ec2 describe-instances --filters Name=tag:Service,Values=payments", "State transitions, private IPs, attached roles, and tags", "A fast way to verify whether the expected nodes or instances even exist in the right place."),
            ("aws ec2 describe-vpcs", "Shows VPC configuration and CIDR ranges", "Validate you are in the correct network boundary", "--filters, --query", "aws ec2 describe-vpcs --filters Name=tag:Environment,Values=prod", "CIDRs, DNS settings, and tenancy", "Helpful when overlapping CIDRs or wrong VPC selection is the hidden cause."),
            ("aws ec2 describe-route-tables", "Displays VPC routing decisions", "Debug egress, peering, TGW, or private endpoint pathing", "--filters, --route-table-ids", "aws ec2 describe-route-tables --filters Name=vpc-id,Values=vpc-123456", "Default routes, propagated routes, and blackhole entries", "Look for blackhole routes and missing propagation during outages."),
            ("aws ec2 describe-security-groups", "Shows inbound and outbound SG rules", "Check whether traffic is permitted at the instance or ENI boundary", "--group-ids, --filters", "aws ec2 describe-security-groups --group-ids sg-123456", "Port, CIDR, and SG references", "Security groups often look right at a glance but fail because the source SG is wrong."),
            ("aws elbv2 describe-load-balancers", "Lists ALB and NLB configuration", "Inspect edge entry points during 4xx/5xx incidents", "--names, --load-balancer-arns", "aws elbv2 describe-load-balancers --names payments-alb", "Scheme, subnets, security groups, and DNS names", "Use this with target-health data when clients see failures."),
            ("aws elbv2 describe-target-health", "Shows target registration and health state", "Debug why a load balancer is not routing to backends", "--target-group-arn", "aws elbv2 describe-target-health --target-group-arn arn:aws:elasticloadbalancing:...", "Unhealthy reasons like timeout or failed health checks", "Critical for separating app failure from LB misconfiguration."),
            ("aws eks describe-cluster", "Returns EKS control-plane metadata", "Confirm cluster endpoint mode, version, and logging settings", "--name", "aws eks describe-cluster --name platform-prod", "Endpoint access mode, OIDC issuer, and status", "Use it when kubeconfig works inconsistently or private/public access changed."),
            ("aws eks update-kubeconfig", "Adds or refreshes kubeconfig access for an EKS cluster", "Switch kubectl access during ops or incident response", "--name, --region, --role-arn", "aws eks update-kubeconfig --name platform-prod --role-arn arn:aws:iam::123456789012:role/ops-admin", "Whether the expected context and exec auth block were written", "A frequent failure point is using the wrong role or stale kubeconfig context."),
            ("aws iam get-role", "Shows a role definition and trust policy", "Inspect who can assume a role and what service it is for", "--role-name", "aws iam get-role --role-name payments-irsa-role", "AssumeRolePolicyDocument and role path", "Trust policy errors are common when EKS IRSA or cross-account access breaks."),
            ("aws iam list-attached-role-policies", "Lists managed policies attached to a role", "Confirm effective policy attachments during permissions debugging", "--role-name", "aws iam list-attached-role-policies --role-name deployer-role", "Whether expected policies are attached at all", "Pair with inline policy checks and SCP review when access still fails."),
            ("aws s3 ls", "Lists buckets or objects", "Quick validation of S3 reachability and bucket presence", "--recursive, s3://bucket", "aws s3 ls s3://artifact-bucket/releases/", "Missing prefixes, access denied, or region mismatch clues", "Simple but useful for confirming whether auth or network is the real problem."),
            ("aws rds describe-db-instances", "Shows RDS instance state and endpoints", "Debug database connectivity, failover, or storage saturation", "--db-instance-identifier", "aws rds describe-db-instances --db-instance-identifier orders-prod", "Endpoint, Multi-AZ state, status, storage, and CA certificate", "Important during failovers when apps keep pointing at stale endpoints."),
            ("aws cloudwatch get-metric-data", "Queries CloudWatch metrics in bulk", "Pull incident evidence without opening the console", "--metric-data-queries, --start-time, --end-time", "aws cloudwatch get-metric-data --metric-data-queries file://queries.json --start-time 2026-08-11T08:00:00Z --end-time 2026-08-11T09:00:00Z", "Latency, errors, saturation, and scaling signals", "Useful when dashboards lag or when you need exact timestamps for a postmortem."),
            ("aws logs tail", "Streams CloudWatch log events", "Watch service logs live during an incident", "--follow, --since", "aws logs tail /aws/eks/platform-prod/cluster --since 15m --follow", "Burst errors, auth denials, timeout signatures", "Great for rapid triage but watch log volume and least-privilege access."),
            ("aws autoscaling describe-auto-scaling-groups", "Shows ASG desired, min, max, and instance health", "Investigate scaling failures or stuck capacity", "--auto-scaling-group-names", "aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names app-prod-asg", "Desired vs. in-service capacity and scaling activities", "Check alongside quotas, launch template issues, and subnet IP exhaustion."),
            ("aws route53 list-hosted-zones", "Lists Route 53 hosted zones", "Confirm the expected zone exists in the correct account", "--query", "aws route53 list-hosted-zones --query 'HostedZones[].Name'", "Zone names and private/public scope", "Useful when DNS changes were applied in the wrong account or zone."),
            ("aws route53 list-resource-record-sets", "Shows DNS records in a hosted zone", "Inspect failover, weighted, or alias record behavior", "--hosted-zone-id, --query", "aws route53 list-resource-record-sets --hosted-zone-id Z1234567890", "Alias targets, TTLs, health-check routing, and stale records", "Key during DNS incidents where the hostname resolves but not the way you expect."),
            ("aws secretsmanager get-secret-value", "Fetches the current secret payload or version metadata", "Verify whether a secret exists, rotated, or is readable by a role", "--secret-id, --version-stage", "aws secretsmanager get-secret-value --secret-id prod/db/password", "SecretString presence and version labels", "Handle carefully in production: avoid printing secrets into shell history or logs."),
            ("aws kms describe-key", "Returns KMS key metadata and status", "Check whether a key is enabled, rotated, or in the expected account", "--key-id", "aws kms describe-key --key-id alias/platform-prod", "Key state, manager, ARN, and rotation settings", "Critical when applications fail encryption or decryption after account or policy changes."),
        ],
    },
    "azure": {
        "name": "Azure",
        "identity": "Microsoft Entra ID, managed identities, role assignments, PIM, subscription management groups, and workload identity for AKS.",
        "networking": "VNets, subnets, NSGs, UDRs, Azure Firewall, Private Link, DNS Private Resolver, ExpressRoute, and hub-spoke topologies.",
        "compute": "VMs, VM Scale Sets, App Service, Functions, Container Apps, and AKS.",
        "storage": "Blob, Files, managed disks, lifecycle policies, geo-redundancy, and encryption settings.",
        "databases": "Azure SQL, PostgreSQL Flexible Server, Cosmos DB, Cache for Redis, and data replication choices.",
        "observability": "Azure Monitor, Log Analytics, Application Insights, Activity Logs, NSG flow logs, and Defender for Cloud.",
        "security": "Management groups, Azure Policy, Key Vault, Defender, Private Link, conditional access, and managed identities.",
        "cost": "Reservations, savings plans, cost analysis, budgets, tags, and subscription-level chargeback.",
        "resilience": "Availability zones, paired regions, zonal services, and recovery plans with Azure Site Recovery or application-level replication.",
        "regions": "Use paired regions, traffic management layers, and service-specific replication patterns to meet DR and residency goals.",
        "services": [
            ("Entra ID and RBAC", "Identity, role assignments, group-based access, and admin workflow."),
            ("VNets and Private Link", "Network isolation, service access, and hybrid connectivity."),
            ("VMs, App Service, Functions, and AKS", "Core compute choices for application platforms."),
            ("Blob Storage, Managed Disks, and Files", "Object, block, and shared file storage options."),
            ("Azure SQL, PostgreSQL Flexible Server, and Cosmos DB", "Managed database services and trade-offs."),
            ("Azure Monitor, Log Analytics, and Application Insights", "Operational visibility and correlation."),
        ],
        "fundamentals": [
            "What is the difference between a tenant, management group, subscription, and resource group in Azure?",
            "How do managed identities change the way applications authenticate in Azure?",
            "What do availability zones and region pairs solve in Azure architecture?",
            "How do NSGs differ from Azure Firewall and route tables?",
            "When should you choose VM Scale Sets over AKS or App Service?",
            "How does Private Link change the security posture of PaaS services?",
            "What is the operational difference between Blob Storage redundancy options?",
            "How does Azure SQL high availability differ from read scaling?",
            "How do management groups and Azure Policy help platform teams?",
            "What is the role of Entra ID in cloud access control?",
            "How does AKS workload identity work?",
            "What trade-offs exist between peering, hub-spoke, and virtual WAN?",
            "How do Azure DNS and Private DNS zones participate in resilient systems?",
            "What is the difference between Application Gateway and Azure Load Balancer?",
            "How does Key Vault shape secure application design in Azure?",
            "What makes Cosmos DB operationally different from PostgreSQL Flexible Server?",
            "How do autoscaling decisions work across VMSS, AKS, and App Service?",
            "How should teams think about Azure quotas and regional capacity constraints?",
            "How do you design a landing zone for many subscriptions and teams?",
            "What is a strong subscription strategy for platform engineering on Azure?",
            "How do you approach hybrid connectivity with ExpressRoute and VPN gateways?",
            "What are the production trade-offs of AKS versus App Service or Container Apps?",
            "How should disaster recovery tiers shape Azure service selection?",
            "How do you centralize observability with Log Analytics while preserving ownership?",
            "What are the most important cost-control levers in Azure at scale?",
        ],
        "questions": [
            "How would you explain blast radius reduction in Azure subscription design?",
            "Why do mature Azure estates prefer managed identities and PIM over shared credentials?",
            "How would you design private service access to PaaS resources in Azure?",
            "When does a flat VNet model stop working well on Azure?",
            "What are the operational consequences of choosing Azure Functions for critical APIs?",
            "How do you reason about stateful workloads on AKS?",
            "Why do teams misuse NSGs during incidents?",
            "How would you debug intermittent database failures from a private subnet in Azure?",
            "What should a senior engineer mention when comparing AKS and Container Apps?",
            "How do you explain consistency and partitioning trade-offs in Cosmos DB designs?",
            "What does a good Key Vault and secret-rotation model look like?",
            "How would you discuss paired-region failover strategy in Azure?",
            "What should you monitor first for NAT gateway saturation or SNAT exhaustion?",
            "How do Azure Policy and RBAC interact during permissions troubleshooting?",
            "What are the architectural trade-offs between Azure SQL, Cosmos DB, and PostgreSQL Flexible Server?",
            "How would you control Azure Monitor cost without losing incident fidelity?",
            "What does a strong answer about Azure network segmentation sound like?",
            "How do you structure subscription vending and guardrails for a platform team?",
            "How should teams use Azure Front Door or Traffic Manager for failover safely?",
            "When is Private Link better than VNet peering or service endpoints?",
            "How would you talk through a zero-trust identity strategy on Azure?",
            "What would you optimize first in a multi-subscription cost reduction program?",
            "How should a senior engineer reason about regional quota risk in Azure?",
            "How do you explain Azure backup and DR choices to non-specialists?",
            "What would a strong staff-level answer about enterprise Azure platforms include?",
        ],
        "troubleshooting": [
            "A role assignment looks correct but a deployment principal still gets authorization errors",
            "A private AKS node pool can reach some services but not a private registry",
            "Private DNS resolves the expected host but clients still fail to connect",
            "Application Gateway shows healthy probes while users receive 502 responses",
            "AKS nodes are ready but pods cannot mount secrets from Key Vault",
            "A stateful workload using managed disks fails to reschedule after node maintenance",
            "Applications in one subnet cannot connect to Azure SQL after a firewall change",
            "A Private Link consumer times out while the provider resource looks healthy",
            "TLS certificates are present in Key Vault but ingress still serves the old chain",
            "VM Scale Sets stop scaling during a demand spike",
            "A regional quota prevents a production recovery deployment",
            "Azure Monitor dashboards lose critical signals during an incident",
            "Paired-region failover starts but traffic does not move as expected",
            "Cost analysis shows a sudden egress or NAT cost spike",
            "AKS ingress provisioning loops because load balancer resources fail",
            "Blob replication is enabled but new objects are missing from the secondary region",
            "A Key Vault access policy or RBAC change breaks application startup",
            "Azure Functions time out only when calling private downstream services",
            "Cosmos DB throttling appears after a tenant onboarding event",
            "PostgreSQL Flexible Server failover completes but clients keep using stale DNS",
            "Activity Logs are missing for one newly onboarded subscription",
            "Container image pulls fail in AKS from one subnet but not another",
            "A hub-spoke route table mistake isolates one environment",
            "Azure Bastion or serial console access fails during a VM incident",
            "A canary region stays healthy but Azure Front Door still sends users to the degraded region",
        ],
        "senior": [
            "Design an Azure landing zone for a regulated enterprise",
            "Move a single-region workload to active-active across paired or chosen regions",
            "Define a DR strategy for mixed Azure SQL, Cosmos DB, and AKS workloads",
            "Create an enterprise identity model using Entra ID, PIM, and managed identities",
            "Design network segmentation for shared services, developer subscriptions, and production",
            "Plan hybrid connectivity between Azure and on-prem environments",
            "Build a centralized AKS platform for many product teams",
            "Design centralized observability across hundreds of subscriptions",
            "Reduce Azure spend without harming developer velocity",
            "Choose between AKS, App Service, and Container Apps as default platforms",
            "Design a workload identity strategy for containers and serverless services",
            "Standardize secrets handling with Key Vault across subscriptions and regions",
            "Plan region evacuation for a critical Azure platform",
            "Design secure cross-subscription service-to-service access",
            "Create a platform model for multi-tenant SaaS workloads",
            "Set cost guardrails for teams with bursty or seasonal growth",
            "Choose a data residency strategy for global customers on Azure",
            "Create a migration plan from a flat subscription model to a governed landing zone",
            "Standardize ingress and edge security across many applications",
            "Design governance for self-service infrastructure with strong auditability",
            "Plan large-scale AKS fleet management across regions",
            "Choose a backup and recovery operating model for tiered services",
            "Build a zero-trust architecture for engineering access to Azure",
            "Introduce shared platform services without becoming a blocker",
            "Lead a modernization from VM-centric hosting to managed Azure platforms",
        ],
        "challenges": [
            "Debug an Azure RBAC assignment that blocks a deployment service principal",
            "Design a cost-optimized but resilient hub-spoke network layout",
            "Improve an AKS platform suffering from noisy-neighbor workloads",
            "Secure a Blob Storage access pattern without breaking legitimate consumers",
            "Reduce NAT gateway and egress spend in a busy subscription",
            "Scale an Azure Functions system hitting concurrency or downstream limits",
            "Fix a Bicep deployment that deadlocks on resource dependencies",
            "Fix AKS workload identity for an app using Key Vault",
            "Fix a route-table design that leaks traffic between spokes",
            "Analyze an architecture that depends on one zone and one database replica",
            "Design DR for a payments platform using Azure SQL and AKS",
            "Design multi-region failover for a latency-sensitive API on Azure",
            "Troubleshoot AKS control-plane or node reachability from private networks",
            "Improve Azure Monitor observability with sane retention and cost controls",
            "Secure cross-subscription access for a shared build system",
            "Refactor a flat VNet layout into segmented subnets and shared services",
            "Fix private DNS resolution for Private Link consumers",
            "Reduce Blob request and transfer cost for analytics workloads",
            "Scale a private API mesh without making certificate management unmanageable",
            "Improve backup validation rather than only backup enablement",
            "Fix a broken blue-green rollout behind Application Gateway or Front Door",
            "Secure a Key Vault permissions model after an org restructure",
            "Analyze quota and capacity risk before onboarding a large enterprise tenant",
            "Improve region-failover runbooks after a failed game day",
            "Troubleshoot a cost spike caused by untagged ephemeral infrastructure",
        ],
        "cheats": [
            ("az account show", "Shows the active Azure subscription and tenant context", "First check during auth or wrong-subscription debugging", "--output, --query", "az account show --output table", "Subscription ID, tenant ID, and current account name", "Critical when engineers accidentally work in the wrong subscription or cloud shell context."),
            ("az configure --list-defaults", "Displays configured CLI defaults", "Confirm which group, location, and subscription defaults are applied", "", "az configure --list-defaults", "Default group, location, and output values", "Useful when scripts behave differently across shells or CI."),
            ("az vm list -d", "Lists VMs with power state and IP data", "Inspect compute placement, power state, and missing instances", "--resource-group, --query", "az vm list -d --resource-group rg-prod", "PowerState, private IP, public IP, and zones", "A quick way to confirm whether the expected VM footprint exists."),
            ("az network vnet list", "Lists VNets and address spaces", "Validate the expected network boundary", "--resource-group, --query", "az network vnet list --resource-group rg-network", "CIDRs, subnets, and resource group placement", "Helpful when overlapping address spaces or wrong-resource-group drift appear."),
            ("az network route-table route list", "Shows user-defined routes in a route table", "Debug egress, hub-spoke, or Private Link pathing", "--resource-group, --route-table-name", "az network route-table route list --resource-group rg-network --route-table-name rt-prod", "Next hop type, address prefix, and blackhole-like misroutes", "Use this when packets appear to vanish between subnets or spokes."),
            ("az network nsg rule list", "Displays effective NSG rules", "Check if traffic is blocked at the subnet or NIC boundary", "--resource-group, --nsg-name", "az network nsg rule list --resource-group rg-network --nsg-name nsg-app", "Priority order, source, destination, and access action", "NSG priority confusion is a common production failure."),
            ("az network lb show", "Shows Azure Load Balancer configuration", "Inspect L4 load balancer setup during connectivity incidents", "--resource-group, --name", "az network lb show --resource-group rg-edge --name lb-prod", "Frontend IPs, backend pools, probes, and rules", "Useful for separating backend issues from LB misconfiguration."),
            ("az network application-gateway show", "Shows Application Gateway listeners, probes, and backend settings", "Debug ingress and 502/503 problems", "--resource-group, --name", "az network application-gateway show --resource-group rg-edge --name agw-prod", "Backend health settings, listeners, TLS, and rewrite rules", "Key when the gateway looks deployed but traffic still fails."),
            ("az aks show", "Returns AKS cluster metadata", "Confirm endpoint mode, version, and identity settings", "--resource-group, --name", "az aks show --resource-group rg-platform --name aks-prod", "Private/public API, Kubernetes version, identity profile", "Use it when kubeconfig or node behavior suggests a control-plane config drift."),
            ("az aks get-credentials", "Adds or refreshes kubeconfig access for AKS", "Switch kubectl access during ops or incidents", "--resource-group, --name, --admin, --overwrite-existing", "az aks get-credentials --resource-group rg-platform --name aks-prod --overwrite-existing", "Whether the expected context was written", "Failure often comes from wrong tenant, missing cluster-user RBAC, or stale contexts."),
            ("az role assignment list", "Lists RBAC assignments for a principal or scope", "Inspect effective authorization during permission debugging", "--assignee, --scope", "az role assignment list --assignee app-spn-id --scope /subscriptions/.../resourceGroups/rg-prod", "Which role is granted at which scope", "Pair with deny assignments and policy checks when access still fails."),
            ("az storage blob list", "Lists blobs in a container", "Quick validation of Blob access and object presence", "--account-name, --container-name, --auth-mode login", "az storage blob list --account-name platprod --container-name releases --auth-mode login", "Missing prefixes, access denied, or auth mode clues", "Useful when the question is whether data is absent or simply unreadable."),
            ("az sql db show", "Shows Azure SQL database properties", "Inspect state, sku, and read scale settings during DB issues", "--resource-group, --server, --name", "az sql db show --resource-group rg-data --server sql-prod --name orders", "Status, edition, auto-pause, readScale", "Helpful when production latency hides a configuration regression."),
            ("az monitor metrics list", "Queries Azure Monitor metrics", "Pull incident evidence without opening the portal", "--resource, --metric, --interval", "az monitor metrics list --resource /subscriptions/.../providers/Microsoft.Compute/virtualMachines/vm1 --metric Percentage CPU", "Time-series values and aggregation output", "Good for precise incident timelines or automated evidence capture."),
            ("az monitor log-analytics query", "Runs Kusto queries against Log Analytics", "Inspect logs or metrics correlations during incidents", "--workspace, --analytics-query", "az monitor log-analytics query --workspace WORKSPACE_ID --analytics-query 'AppRequests | take 20'", "Returned rows, latency, and missing-signal gaps", "Critical when dashboards are too coarse and you need exact evidence."),
            ("az vmss list-instances", "Shows VM Scale Set instance state", "Investigate scaling failures or unhealthy VMSS nodes", "--resource-group, --name", "az vmss list-instances --resource-group rg-app --name vmss-prod", "Instance IDs, zones, provisioningState, latestModelApplied", "Check this with autoscale rules and quota state."),
            ("az network private-dns zone list", "Lists private DNS zones", "Confirm the expected private zone exists in the right subscription", "--resource-group", "az network private-dns zone list --resource-group rg-dns", "Zone names and resource group placement", "Useful when Private Link is configured but name resolution still fails."),
            ("az network private-dns record-set a list", "Shows A records inside a private DNS zone", "Inspect record drift or missing failover entries", "--resource-group, --zone-name", "az network private-dns record-set a list --resource-group rg-dns --zone-name privatelink.database.windows.net", "A records, TTLs, and stale entries", "Key during private name-resolution incidents."),
            ("az keyvault secret show", "Fetches Key Vault secret metadata or value", "Verify a secret exists, rotated, or is readable", "--vault-name, --name", "az keyvault secret show --vault-name kv-prod --name db-password", "Version, enabled state, contentType, and tags", "Avoid leaking the value in terminals or logs during troubleshooting."),
            ("az keyvault key show", "Returns Key Vault key metadata", "Check whether a key is enabled and in the expected vault", "--vault-name, --name", "az keyvault key show --vault-name kv-prod --name app-key", "Key type, enabled state, and recovery settings", "Important when encryption failures start after policy or vault changes."),
        ],
    },
    "gcp": {
        "name": "GCP",
        "identity": "IAM, service accounts, workload identity federation, organization policies, folders, and project-level boundaries.",
        "networking": "Global VPCs, subnets, firewall rules, Cloud NAT, Cloud DNS, Private Service Connect, Shared VPC, and Cloud Interconnect.",
        "compute": "Compute Engine, managed instance groups, Cloud Run, GKE, Cloud Functions, and autoscaled regional services.",
        "storage": "Cloud Storage, Persistent Disk, Filestore, storage classes, lifecycle rules, and CMEK options.",
        "databases": "Cloud SQL, AlloyDB, Spanner, Bigtable, Memorystore, and replication strategy trade-offs.",
        "observability": "Cloud Monitoring, Cloud Logging, Error Reporting, Cloud Trace, Audit Logs, VPC Flow Logs, and SCC.",
        "security": "Organization policies, folders, VPC Service Controls, Secret Manager, KMS, BeyondCorp-style access, and workload identity.",
        "cost": "Committed use discounts, autoscaling efficiency, labeling, budgets, and per-project chargeback.",
        "resilience": "Regional managed services, multi-zonal GKE, multi-region data services, and planned failover mechanisms.",
        "regions": "GCP uses global control planes for many services but region-specific capacity and residency still matter; design failover explicitly.",
        "services": [
            ("IAM, folders, and org policies", "Identity, project boundaries, and enterprise governance."),
            ("VPC, Shared VPC, PSC, and Cloud DNS", "Network isolation, service access, and hybrid connectivity."),
            ("Compute Engine, Cloud Run, Functions, and GKE", "Core compute choices for application delivery."),
            ("Cloud Storage, Persistent Disk, and Filestore", "Object, block, and shared file storage."),
            ("Cloud SQL, AlloyDB, Spanner, and Bigtable", "Managed database choices across consistency and scale patterns."),
            ("Cloud Monitoring, Logging, Trace, and Audit Logs", "Operational visibility and incident evidence."),
        ],
        "fundamentals": [
            "What is the difference between an organization, folder, project, and VPC boundary in GCP?",
            "How do service accounts differ from human identities in production GCP environments?",
            "What do regions and zones solve in GCP architecture?",
            "How do firewall rules and routes work in a global VPC model?",
            "When should you choose Compute Engine over Cloud Run or GKE?",
            "How does Private Service Connect change the security posture of service access?",
            "What is the operational difference between Cloud Storage classes and redundancy options?",
            "How does Cloud SQL high availability differ from read replicas?",
            "How do folders and org policies help platform teams scale governance?",
            "What is the role of Workload Identity Federation in secure cloud access?",
            "How does GKE Workload Identity work?",
            "What trade-offs exist between Shared VPC, VPC peering, and PSC?",
            "How does Cloud DNS participate in resilient multi-region systems?",
            "What is the difference between global external load balancing and regional load balancing in GCP?",
            "How does Cloud KMS influence secure application design?",
            "What makes Spanner operationally different from Cloud SQL or AlloyDB?",
            "How do autoscaling decisions work across MIGs, GKE, and Cloud Run?",
            "How should teams think about GCP quotas and regional capacity as an architectural constraint?",
            "How do you design a landing zone for many projects and regulated workloads?",
            "What is a good project strategy for platform engineering on GCP?",
            "How do you approach hybrid connectivity with Cloud Interconnect and Cloud VPN?",
            "What are the production trade-offs of GKE versus Cloud Run for a platform team?",
            "How should disaster recovery tiers shape GCP service selection?",
            "How do you centralize observability while preserving project ownership?",
            "What are the most important cost-control levers in GCP at scale?",
        ],
        "questions": [
            "How would you explain blast radius reduction in GCP project design?",
            "Why do mature GCP estates prefer short-lived credentials and workload identity over key files?",
            "How would you design private service access without public exposure in GCP?",
            "When does a single Shared VPC model stop being sufficient?",
            "What are the operational consequences of choosing Cloud Run for critical APIs?",
            "How do you reason about stateful workloads on GKE?",
            "Why do teams misuse firewall rules during incidents?",
            "How would you debug intermittent database failures from private GKE workloads?",
            "What should a senior engineer mention when comparing GKE and Cloud Run?",
            "How do you explain consistency trade-offs in Spanner-backed designs?",
            "What does a good KMS and Secret Manager model look like in a multi-team org?",
            "How would you discuss failover strategy between two GCP regions?",
            "What should you monitor first for Cloud NAT saturation or egress cost spikes?",
            "How do org policies change the way teams troubleshoot permissions?",
            "What are the architectural trade-offs between Cloud SQL, Spanner, and Bigtable?",
            "How would you control observability cost without losing incident quality?",
            "What does a strong answer about GCP network segmentation sound like?",
            "How do you structure project vending and guardrails for a platform team?",
            "How should teams use global load balancing and health checks safely?",
            "When is Private Service Connect better than peering or public endpoints?",
            "How would you talk through a zero-trust identity strategy on GCP?",
            "What would you optimize first in a multi-project cost reduction program?",
            "How should a senior engineer reason about quota risk before a regional launch?",
            "How do you explain GCP backup and DR choices to non-specialists?",
            "What would a strong staff-level answer about enterprise GCP platforms include?",
        ],
        "troubleshooting": [
            "A service account appears correct but an application still gets permission denied",
            "Private GKE nodes can reach some Google APIs but not Artifact Registry",
            "Cloud DNS resolves correctly but clients in one project still fail",
            "The external load balancer shows healthy backends while users get 502s",
            "GKE nodes are ready but workloads cannot pull container images",
            "A Persistent Disk-backed workload is stuck pending after a node replacement",
            "Applications in one subnet cannot connect to Cloud SQL after a network change",
            "Private Service Connect consumers time out while the producer looks healthy",
            "TLS certificates look valid but the Google load balancer still serves failures",
            "Managed instance groups stop scaling out during a demand spike",
            "A critical recovery deployment fails because of quota exhaustion",
            "Cloud Monitoring dashboards lose signals during an incident",
            "Cross-region failover starts but traffic does not move cleanly",
            "Cost reports show a sudden Cloud NAT or egress spike",
            "GKE ingress or gateway provisioning loops because backend resources fail",
            "Cloud Storage replication or dual-region behavior is not matching expectations",
            "A KMS IAM or key-ring policy blocks an application after project reorganization",
            "Cloud Run revisions time out only when calling private downstream services",
            "Spanner or Bigtable hotspots appear after a tenant onboarding event",
            "Cloud SQL failover completes but clients keep using stale connection assumptions",
            "Audit logs are missing for one newly created project",
            "Artifact Registry pulls fail from one GKE node pool but not another",
            "A Shared VPC or route configuration mistake isolates one environment",
            "IAP or serial console access fails during a VM incident",
            "A canary region stays healthy but the global load balancer still prefers the degraded backend",
        ],
        "senior": [
            "Design a GCP landing zone for a regulated enterprise",
            "Move a single-region workload to active-active across two GCP regions",
            "Define a DR strategy for mixed Cloud SQL, Spanner, and GKE workloads",
            "Create an enterprise identity model using workload identity and org policy guardrails",
            "Design network segmentation for shared services, developer projects, and production",
            "Plan hybrid connectivity between GCP and on-prem environments",
            "Build a centralized GKE platform for many product teams",
            "Design centralized observability across hundreds of GCP projects",
            "Reduce GCP spend without harming delivery velocity",
            "Choose between GKE and Cloud Run as the default container platform",
            "Design a workload identity strategy for containers and serverless services",
            "Standardize secrets handling with Secret Manager across projects and regions",
            "Plan region evacuation for a critical customer-facing platform",
            "Design secure cross-project service-to-service access",
            "Create a platform model for multi-tenant SaaS workloads",
            "Set cost guardrails for teams with unpredictable growth",
            "Choose a data residency strategy for global customers on GCP",
            "Create a migration plan from a flat project model to a governed folder and project model",
            "Standardize ingress and edge security across dozens of applications",
            "Design governance for self-service infrastructure while preserving auditability",
            "Plan large-scale GKE fleet management across regions",
            "Choose a backup and recovery operating model for tiered services",
            "Build a zero-trust architecture for engineering access to GCP",
            "Introduce shared platform services without creating a central bottleneck",
            "Lead a modernization from VM-centric hosting to managed GCP platforms",
        ],
        "challenges": [
            "Debug a GCP IAM binding that blocks a deployment service account",
            "Design a cost-optimized but resilient Shared VPC network layout",
            "Improve a GKE platform suffering from noisy-neighbor workloads",
            "Secure a Cloud Storage access pattern without breaking legitimate consumers",
            "Reduce Cloud NAT and egress spend in a busy region",
            "Scale an event-driven Cloud Run system hitting concurrency or downstream limits",
            "Fix a Terraform deployment that deadlocks on project or API dependencies",
            "Fix GKE Workload Identity for an application using Secret Manager",
            "Fix a routing design that leaks traffic between environments",
            "Analyze an architecture that depends on one region and one database writer",
            "Design DR for a payments platform using Cloud SQL and GKE",
            "Design multi-region failover for a latency-sensitive API on GCP",
            "Troubleshoot GKE control-plane or private-node reachability",
            "Improve Cloud Monitoring observability with sane retention and cost controls",
            "Secure cross-project access for a shared build system",
            "Refactor a flat project layout into segmented folders and shared services",
            "Fix private DNS resolution for PSC consumers",
            "Reduce Cloud Storage request and transfer cost for analytics workloads",
            "Scale a private API mesh without making certificate management unmanageable",
            "Improve backup validation rather than only backup creation",
            "Fix a broken blue-green rollout using traffic splitting or load balancing",
            "Secure a KMS permissions model after a project restructure",
            "Analyze quota risk before onboarding a large enterprise tenant",
            "Improve region-failover runbooks after a failed game day",
            "Troubleshoot a cost spike caused by unlabeled ephemeral infrastructure",
        ],
        "cheats": [
            ("gcloud config list", "Shows the active gcloud configuration, project, and account", "First check during auth or wrong-project debugging", "--format", "gcloud config list", "Active account, project, and compute defaults", "Useful when CI, local shells, and jump boxes behave differently."),
            ("gcloud auth list", "Lists authenticated accounts and the active account", "Confirm which identity is actually being used", "", "gcloud auth list", "Active account marker and service account vs human account", "Critical when service account impersonation or stale login state causes confusion."),
            ("gcloud compute instances list", "Lists VM instances and placement data", "Inspect compute presence, zone placement, and status", "--filter, --format", "gcloud compute instances list --filter='labels.service=payments'", "Status, internal IP, external IP, and zone", "Quickly tells you whether the expected compute footprint exists."),
            ("gcloud compute networks list", "Shows VPC networks", "Validate the expected network boundary", "--format", "gcloud compute networks list", "Auto/subnet mode and network names", "Useful when Shared VPC or wrong-project selection is the hidden problem."),
            ("gcloud compute routes list", "Displays effective routes", "Debug egress, hybrid, or PSC pathing", "--filter, --format", "gcloud compute routes list --filter='network=platform-vpc'", "Next hop, priority, destRange, and blackhole-like misroutes", "Look for unexpected priorities or routes pointing at the wrong next hop."),
            ("gcloud compute firewall-rules list", "Shows firewall rules", "Check whether traffic is permitted at the VPC boundary", "--filter, --format", "gcloud compute firewall-rules list --filter='network=platform-vpc'", "Direction, priority, source ranges, target tags, and allowed ports", "Firewall priority and target-tag mismatches are common outage causes."),
            ("gcloud compute backend-services get-health", "Returns backend health for load-balanced services", "Debug why a load balancer is not routing to backends", "--global or --region", "gcloud compute backend-services get-health payments-backend --global", "Healthy vs unhealthy backends and reasons", "Helps separate application failure from load-balancer config issues."),
            ("gcloud compute url-maps describe", "Shows URL map routing configuration", "Inspect path routing during 404/502 incidents", "--global", "gcloud compute url-maps describe edge-routing --global", "Host rules, path matchers, default service", "Useful when the service is fine but requests route to the wrong backend."),
            ("gcloud container clusters describe", "Returns GKE cluster metadata", "Confirm private/public endpoint mode, version, and workload identity", "--region or --zone", "gcloud container clusters describe platform-prod --region europe-west1", "Endpoint mode, release channel, workload pool, logging", "Use it when kubeconfig or node behavior suggests control-plane drift."),
            ("gcloud container clusters get-credentials", "Adds or refreshes kubeconfig access for GKE", "Switch kubectl access during ops or incidents", "--region or --zone, --project", "gcloud container clusters get-credentials platform-prod --region europe-west1 --project prod-platform", "Whether the expected kube context was written", "Failures often come from wrong project context or missing IAM permissions."),
            ("gcloud projects get-iam-policy", "Shows IAM policy bindings for a project", "Inspect effective authorization during permissions debugging", "--flatten, --format", "gcloud projects get-iam-policy prod-platform", "Which members hold which roles", "Pair with folder or org policy review when access still fails."),
            ("gcloud storage ls", "Lists buckets or objects", "Quick validation of Cloud Storage access and object presence", "--recursive", "gcloud storage ls gs://artifact-bucket/releases/", "Missing prefixes, access denied, or project mismatch clues", "Useful for telling data absence apart from access failure."),
            ("gcloud sql instances describe", "Shows Cloud SQL instance properties", "Inspect state, region, failover config, and networking", "instance name", "gcloud sql instances describe orders-prod", "IP config, HA, storage, region, and activation policy", "Helpful when connectivity failures hide a database config regression."),
            ("gcloud monitoring time-series list", "Queries Cloud Monitoring time-series data", "Pull incident evidence without using the console", "--filter, --interval", "gcloud monitoring time-series list --filter='metric.type=\"compute.googleapis.com/instance/cpu/utilization\"'", "Metric values and timestamps", "Useful for exact timelines or automated incident evidence."),
            ("gcloud logging read", "Runs log queries against Cloud Logging", "Inspect logs across services during incidents", "--limit, --freshness", "gcloud logging read 'resource.type=\"k8s_container\" severity>=ERROR' --freshness=1h --limit=50", "Error bursts, auth denials, and timeout signatures", "Powerful for fast triage; be careful with broad queries in high-volume projects."),
            ("gcloud compute instance-groups managed list-instances", "Shows MIG instance state", "Investigate autoscaling failures or unhealthy instances", "--region or --zone", "gcloud compute instance-groups managed list-instances web-mig --region europe-west1", "Current action, instance status, and version", "Check alongside autoscaler config and quota headroom."),
            ("gcloud dns managed-zones list", "Lists Cloud DNS zones", "Confirm the expected zone exists in the correct project", "--format", "gcloud dns managed-zones list", "Zone names, visibility, and DNS names", "Useful when DNS changes were made in the wrong project."),
            ("gcloud dns record-sets list", "Shows DNS records in a managed zone", "Inspect failover or stale DNS state", "--zone", "gcloud dns record-sets list --zone prod-example-com", "A, CNAME, and TXT records plus TTLs", "Key during DNS incidents where resolution exists but points at the wrong target."),
            ("gcloud secrets versions access latest", "Fetches a secret value from Secret Manager", "Verify whether a secret exists and is readable", "--secret", "gcloud secrets versions access latest --secret=db-password", "Successful retrieval or explicit permission errors", "Avoid printing secret material into logs or shell history."),
            ("gcloud kms keys describe", "Returns KMS key metadata", "Check whether a key is enabled and in the expected key ring", "--location, --keyring", "gcloud kms keys describe app-key --location=europe-west1 --keyring=platform-prod", "Primary version, rotation, labels, and protection level", "Important when encryption or decryption failures begin after IAM or project changes."),
        ],
    },
}


def difficulty(idx: int, mode: str) -> str:
    if mode == "fundamentals":
        return "Beginner" if idx <= 8 else "Intermediate" if idx <= 17 else "Advanced"
    if mode == "senior":
        return "Senior" if idx <= 10 else "Staff" if idx <= 20 else "Principal"
    return "Intermediate" if idx <= 8 else "Advanced" if idx <= 18 else "Senior"


def create_readme(cfg: dict) -> str:
    qas = []
    for idx, q in enumerate(cfg["questions"], start=1):
        qas.append(
            f"## Question {idx:02d} — {q}\n\n"
            f"**Answer:** In {cfg['name']}, a strong answer starts with the control boundary involved, then explains how identity, networking, compute, data, and operations interact around that decision. "
            f"Senior candidates should connect the mechanism to blast radius, observability, cost, and rollback rather than giving a console-tour answer.\n"
        )
    services = "\n".join([f"- **{name}:** {desc}" for name, desc in cfg["services"]])
    return f"""# {cfg['name']}

## What this cloud platform is

{cfg['name']} is a general-purpose cloud platform that gives teams managed primitives for identity, networking, compute, data, observability, and governance. The engineering challenge is not memorizing product names; it is understanding how the platform's boundaries shape production reliability, security, cost, and developer speed.

## Core architecture

Production architecture on {cfg['name']} usually starts with strong isolation boundaries, explicit network paths, workload identity, managed observability, and deliberate regional design. Mature teams separate foundational platform concerns from application concerns so that access, networking, compliance, and logging do not have to be reinvented by every product team.

## Main services

{services}

## Identity

{cfg['identity']}

## Networking

{cfg['networking']}

## Compute

{cfg['compute']}

## Containers/Kubernetes

Managed Kubernetes is valuable when teams need a consistent scheduling and policy layer, but it also shifts responsibility toward cluster lifecycle, node security, admission controls, and cross-team platform ownership.

## Storage

{cfg['storage']}

## Databases

{cfg['databases']}

## Observability

{cfg['observability']}

## Security

{cfg['security']}

## Cost management

{cfg['cost']}

## Resilience

{cfg['resilience']}

## Multi-region

{cfg['regions']}

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

{''.join(qas)}
"""


def create_fundamentals(cfg: dict) -> str:
    blocks = []
    for idx, q in enumerate(cfg["fundamentals"], start=1):
        blocks.append(
            f"""## Question {idx:02d} — {q}

**Difficulty:** {difficulty(idx, "fundamentals")}

**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### What the interviewer is testing

Whether you understand the provider primitive behind this question well enough to explain normal behavior, failure boundaries, and how that primitive influences platform decisions.

### Answer

The direct answer should explain the relevant {cfg['name']} boundary, what service or control plane makes the decision, and what assumptions must hold true for the feature to behave as expected in production.

### How it works

In {cfg['name']}, this topic works by combining identity, network reachability, service configuration, and managed control-plane behavior. A complete answer should describe which layer is authoritative and which adjacent layers only influence the result indirectly.

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

"""
        )
    return f"# {cfg['name']} Fundamentals\n\n{''.join(blocks)}"


def create_questions(cfg: dict) -> str:
    blocks = []
    for idx, q in enumerate(cfg["questions"], start=1):
        blocks.append(
            f"""## Question {idx:02d} — {q}

**Difficulty:** {difficulty(idx, "questions")}
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Short answer

The short answer should define the relevant {cfg['name']} choice and the primary trade-off behind it.

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

"""
        )
    return f"# {cfg['name']} Interview Questions\n\n{''.join(blocks)}"


def create_troubleshooting(cfg: dict) -> str:
    blocks = []
    for idx, title in enumerate(cfg["troubleshooting"], start=1):
        blocks.append(
            f"""## Scenario {idx:02d} — {title}

**Difficulty:** {"Intermediate" if idx <= 8 else "Advanced" if idx <= 18 else "Senior"}
**Roles:** Cloud Engineer / DevOps / SRE / Platform Engineer / Security Engineer

### Situation

A production workload on {cfg['name']} is degraded and this scenario is the most visible symptom reported by users or operators.

### Symptoms

- User-facing errors, latency, or failed deployments
- Conflicting console and runtime signals
- Unclear boundary between identity, networking, service health, and application behavior

### What would you investigate first?

Start by proving the failing boundary: identity, DNS, routing, edge, compute, data, or quota. Confirm recent changes and whether the blast radius is regional, environmental, or tenant-specific.

### Investigation flow

1. Verify whether the issue is isolated or systemic.
2. Confirm identity and policy context for the failing actor.
3. Inspect network path and name resolution.
4. Check control-plane health, quota state, and recent config drift.
5. Validate backend dependency health before concluding the application is broken.

### Commands / evidence

Use the provider CLI, audit logs, metrics, service health views, and workload-level logs. Prefer evidence that narrows the boundary quickly over broad screenshot-driven guessing.

### What evidence are we looking for?

The evidence should tell us which layer is making the deny, dropping the packet, serving stale DNS, failing TLS, exhausting quota, or misreporting backend health.

### Possible root causes

- Permissions or trust-policy drift
- Routing, firewall, or private-endpoint mistakes
- Load balancer or ingress misconfiguration
- Quota exhaustion or autoscaling limits
- Stale certificates, DNS, or failover assumptions
- Missing logs or telemetry pipelines

### Most likely diagnosis

The most likely diagnosis is the narrowest explanation that fits the user impact, recent changes, and the observed {cfg['name']} control-plane signals. A senior engineer should explicitly say why adjacent hypotheses were ruled out.

### Resolution

Apply the smallest safe corrective action first: revert a policy, restore a route, rotate a certificate, correct an endpoint, scale the blocked resource, or roll back the last change.

### Prevention

Turn the fix into a guardrail: tests, policy checks, quota monitoring, safer deployment sequencing, or runbook updates that make recurrence less likely.

### Observability

Identify which metric, log, trace, or audit event should have shortened time-to-diagnosis. If the signal was absent, call that out as its own engineering problem.

### Security considerations

Avoid solving outages by widening permissions or opening networks permanently. Use temporary access only with clear expiry and auditability.

### Senior engineer discussion

The senior discussion should explain how to reduce uncertainty fastest, protect users during investigation, and keep the team from repeating manual steps in future incidents.

### Follow-up questions

- What single signal would you add if this happened again tomorrow?
- Which unsafe quick fix should the team avoid?
- How would you validate recovery before closing the incident?

"""
        )
    return f"# {cfg['name']} Troubleshooting\n\n{''.join(blocks)}"


def create_senior(cfg: dict) -> str:
    blocks = []
    for idx, title in enumerate(cfg["senior"], start=1):
        blocks.append(
            f"""## Scenario {idx:02d} — {title}

**Difficulty:** {difficulty(idx, "senior")}

### Situation

The organization depends on {cfg['name']} and the current architecture or operating model no longer fits the scale, risk, or compliance expectations of the business.

### Candidate should clarify

- What is the real driver: growth, regulation, availability, cost, migration, or platform standardization?
- Which services and teams are in scope?
- What recovery objectives, data residency constraints, and identity dependencies matter?

### Functional requirements

The design must support existing workloads, self-service team workflows, safe deployments, and a clear migration path from the current model.

### Non-functional requirements

Availability, security, auditability, platform operability, tenant isolation, cost visibility, and time-to-recovery must all be addressed directly.

### Architecture

A strong architecture answer defines the tenancy boundary, identity model, network segmentation, workload platform, data layer, and shared services such as secrets, observability, and CI/CD.

### Request/data flow

Explain how users, services, and operators move through identity, network, compute, and data boundaries. Be explicit about where control planes sit and where failover decisions are made.

### Components

- Identity and policy controls
- Network and connectivity model
- Compute and workload platform
- Data and storage services
- Observability, audit, and security tooling
- Automation and platform interfaces

### Scaling strategy

Describe how capacity, tenant growth, team growth, and regional expansion will be handled without forcing a full redesign.

### Reliability

State the HA model, failover expectations, backup validation, and the boundary between service-level resilience and platform-level resilience.

### Security boundaries

Call out the hard isolation layers: account or subscription or project boundaries, network segmentation, private service access, secrets, and short-lived identities.

### Observability

Explain how logs, metrics, traces, and audit events are centralized while still preserving team-level ownership and useful dashboards.

### Failure scenarios

Discuss region loss, quota exhaustion, misrouted traffic, revoked identity, dependency drift, and observability gaps.

### Cost

Cover steady-state spend, failover or idle DR cost, platform tax, transfer costs, and the reporting model for service owners.

### Trade-offs

The best design is not the one with the most products. It is the one that fits the risk profile, platform maturity, and migration budget of the organization.

### Senior-level answer

A senior answer sequences the change: stabilize the riskiest boundary first, standardize interfaces second, and only then add deeper automation. It makes the system safer before making it more abstract.

### Staff / Principal extension

A staff or principal answer adds organization design, platform-product thinking, cross-team adoption strategy, and the explicit controls needed for hundreds of engineers or many regulated workloads.

### Follow-up questions

- What would you centralize versus leave with application teams?
- How would you prove this design is safer than the current one?
- What migration step creates the highest risk and how would you de-risk it?

"""
        )
    return f"# {cfg['name']} Senior Scenarios\n\n{''.join(blocks)}"


def create_challenges(cfg: dict) -> str:
    blocks = []
    for idx, title in enumerate(cfg["challenges"], start=1):
        blocks.append(
            f"""## Challenge {idx:02d} — {title}

### Problem

This challenge forces you to reason about a realistic {cfg['name']} production problem instead of reciting provider trivia.

### Evidence / context

Assume you have partial telemetry, recent infrastructure changes, team pressure for a quick fix, and at least one hidden constraint involving identity, network reachability, quotas, or service behavior.

### Your task

Explain how you would diagnose or redesign the situation, what evidence you would gather first, and which change you would make before anything else.

### Hints

- Identify the narrowest control boundary involved.
- Separate runtime failure from control-plane misconfiguration.
- Think about rollback, not just the forward fix.

### Recommended solution

A good solution establishes the failing boundary quickly, applies the smallest safe correction, and then converts the incident lesson into a durable guardrail such as policy, automated validation, or a platform default.

### Why this works

It reduces uncertainty fast, limits blast radius, and leaves behind a repeatable operating improvement instead of a one-off hero fix.

### Alternative approaches

Alternative approaches may be valid if they improve recovery time or reduce migration risk, but they should still preserve auditability and avoid permanently widening permissions or exposure.

### Senior extension

Explain how you would encode the fix into platform standards, training, CI checks, or governance so the next team does not rediscover the same failure mode.

"""
        )
    return f"# {cfg['name']} Challenges\n\n{''.join(blocks)}"


def create_cheatsheet(cfg: dict) -> str:
    sections = []
    for command, does, when, flags, example, look, failure in cfg["cheats"]:
        flags_block = flags if flags else "None required beyond normal command context"
        sections.append(
            f"""### `{command}`

**What it does:**  
{does}

**When to use it:**  
{when}

**Important flags/parameters:**  
`{flags_block}`

**Example:**

```bash
{example}
```

**What output to look for:**  
{look}

**Common failure or production use case:**  
{failure}

"""
        )
    return f"# {cfg['name']} Cheatsheet\n\nReal commands and operational notes for {cfg['name']} incident response, validation, and architecture debugging.\n\n{''.join(sections)}"


def create_arch_readme(cfg: dict) -> str:
    return f"""# {cfg['name']} Architecture

- [01-basic-flow.md](01-basic-flow.md)
- [02-production-flow.md](02-production-flow.md)
- [03-enterprise-flow.md](03-enterprise-flow.md)
"""


def create_arch_doc(cfg: dict, title: str, mode: str) -> str:
    return f"""# {title}

## Purpose

Explain how a workload on {cfg['name']} should flow through identity, network, compute, data, and observability boundaries at the {mode.lower()} level.

## Flow

1. A user or upstream service authenticates through the provider identity boundary.
2. Traffic enters through the provider edge or private connectivity model.
3. Network segmentation and policy determine the reachable application path.
4. Compute and orchestration layers serve the workload.
5. Data services persist or retrieve state with explicit identity and network rules.
6. Logs, metrics, traces, and audit signals are collected for operators.

## Key design decisions

- Use short-lived identity over static credentials.
- Keep service-to-service traffic private when possible.
- Make regional failover an explicit design, not an assumption.
- Standardize observability and secrets handling before scale multiplies drift.

## Failure points

- Mis-scoped IAM or RBAC
- DNS or route drift
- Quota exhaustion
- Certificate or endpoint mismatch
- Database failover assumptions

## What senior engineers should notice

The important architectural question is not only whether the components connect, but whether the path is debuggable, governable, and survivable when one region, control plane, or shared service behaves unexpectedly.
"""


def create_hero(cfg: dict) -> str:
    name = cfg["name"]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" fill="none">
  <rect width="1200" height="630" rx="28" fill="#07111D"/>
  <rect x="32" y="32" width="1136" height="566" rx="24" fill="url(#g)" stroke="#1E293B"/>
  <text x="86" y="140" fill="#E2E8F0" font-size="58" font-family="Arial, Helvetica, sans-serif" font-weight="700">{name}</text>
  <text x="86" y="190" fill="#93C5FD" font-size="24" font-family="Arial, Helvetica, sans-serif">Identity · Networking · Compute · Data · Resilience</text>
  <rect x="86" y="250" width="260" height="120" rx="18" fill="#0F172A" stroke="#334155"/>
  <rect x="470" y="250" width="260" height="120" rx="18" fill="#0F172A" stroke="#334155"/>
  <rect x="854" y="250" width="260" height="120" rx="18" fill="#0F172A" stroke="#334155"/>
  <text x="116" y="302" fill="#38BDF8" font-size="24" font-family="Arial, Helvetica, sans-serif" font-weight="700">Foundation</text>
  <text x="116" y="336" fill="#CBD5E1" font-size="18" font-family="Arial, Helvetica, sans-serif">Core services and platform boundaries</text>
  <text x="500" y="302" fill="#4ADE80" font-size="24" font-family="Arial, Helvetica, sans-serif" font-weight="700">Operate</text>
  <text x="500" y="336" fill="#CBD5E1" font-size="18" font-family="Arial, Helvetica, sans-serif">Troubleshoot, observe, and recover</text>
  <text x="884" y="302" fill="#F59E0B" font-size="24" font-family="Arial, Helvetica, sans-serif" font-weight="700">Scale</text>
  <text x="884" y="336" fill="#CBD5E1" font-size="18" font-family="Arial, Helvetica, sans-serif">Governance, regions, platform strategy</text>
  <text x="86" y="468" fill="#94A3B8" font-size="18" font-family="Arial, Helvetica, sans-serif">Canonical pack: README · fundamentals · questions · troubleshooting · senior-scenarios · challenges · cheatsheet · architecture</text>
  <defs>
    <linearGradient id="g" x1="32" y1="32" x2="1168" y2="598" gradientUnits="userSpaceOnUse">
      <stop stop-color="#0B1730"/>
      <stop offset="1" stop-color="#10243A"/>
    </linearGradient>
  </defs>
</svg>
"""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    for slug, cfg in PROVIDERS.items():
        base = REPO_ROOT / "cloud" / slug
        write(base / "README.md", create_readme(cfg))
        write(base / "fundamentals.md", create_fundamentals(cfg))
        write(base / "questions.md", create_questions(cfg))
        write(base / "troubleshooting.md", create_troubleshooting(cfg))
        write(base / "senior-scenarios.md", create_senior(cfg))
        write(base / "challenges.md", create_challenges(cfg))
        write(base / "cheatsheet.md", create_cheatsheet(cfg))
        write(base / "architecture" / "README.md", create_arch_readme(cfg))
        write(base / "architecture" / "01-basic-flow.md", create_arch_doc(cfg, f"{cfg['name']} Basic Flow", "Basic"))
        write(base / "architecture" / "02-production-flow.md", create_arch_doc(cfg, f"{cfg['name']} Production Flow", "Production"))
        write(base / "architecture" / "03-enterprise-flow.md", create_arch_doc(cfg, f"{cfg['name']} Enterprise Flow", "Enterprise"))
        write(base / "assets" / "hero.svg", create_hero(cfg))


if __name__ == "__main__":
    main()
