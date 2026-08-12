#!/usr/bin/env python3
"""Generate role-based AI engineering folders without overwriting existing content.

This script is intentionally idempotent:
- it only creates missing files/directories
- it only appends a missing AI Engineering Career Universe section
- it avoids touching pre-existing useful content in existing role folders
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import textwrap

REPO_ROOT = Path(__file__).resolve().parent.parent
AI_ROOT = REPO_ROOT / "ai-engineering"

QUESTION_RE = re.compile(r"^###\s+(Q|Scenario|Challenge|T)\d+\.|^##\s+(Lab|Challenge|Scenario)\s+\d+", re.MULTILINE)


@dataclass(frozen=True)
class RoleSpec:
    slug: str
    title: str
    category: str
    summary: str
    why: str
    org_position: str
    responsibilities: list[str]
    skills: list[str]
    technologies: list[str]
    boundaries: list[str]
    relationships: list[str]
    architecture: list[str]
    learning_path: list[str]
    focus_areas: list[str]
    role_specific_topics: list[str]
    cross_links: list[tuple[str, str]]
    hero_tagline: str
    orbit_labels: list[str]


ROLE_SPECS: list[RoleSpec] = [
    RoleSpec(
        slug="forward-deployed-ai-engineer",
        title="Forward-Deployed AI Engineer",
        category="Customer / Solutions",
        summary="Translate ambiguous customer needs into production-grade AI systems that integrate with real enterprise data, security, and workflows.",
        why="This role exists because enterprise AI projects fail when prototyping speed is disconnected from customer reality, integration friction, and operational ownership.",
        org_position="Typically sits between product engineering, solutions architecture, platform teams, and customer stakeholders. The role often becomes the technical translator between the buyer's desired workflow and the production constraints of the platform.",
        responsibilities=[
            "Turn vague business problems into technical scopes and deployable increments.",
            "Integrate AI agents, RAG, and APIs into messy customer environments.",
            "Debug identity, network, and data-access issues in third-party systems.",
            "Productionize rapid prototypes so they survive security review and operational handoff.",
            "Provide architecture guidance while maintaining strong hands-on delivery capability.",
        ],
        skills=["requirements discovery", "enterprise integration", "API design", "Kubernetes", "identity and networking", "stakeholder communication", "incident debugging"],
        technologies=["LLMs", "Agents", "MCP", "RAG", "Kubernetes", "cloud IAM", "API gateways", "vector databases"],
        boundaries=["Not only a demo engineer.", "Not only a sales engineer.", "Owns technical delivery trade-offs until the solution is supportable."],
        relationships=["Extends DevOps by owning customer-specific production integration.", "Overlaps with solutions architects on design, but stays more hands-on in implementation and debugging.", "Relies on platform/SRE teams for reusable controls and operating standards."],
        architecture=["Customer users", "Identity boundary", "API integration layer", "Agent runtime", "RAG and MCP paths", "Observability and approval controls"],
        learning_path=["Foundation systems", "Customer environment discovery", "Secure integration", "Production rollout", "Troubleshooting", "Executive communication"],
        focus_areas=["customer discovery", "requirements translation", "enterprise integration", "security review", "multi-system debugging", "production hardening"],
        role_specific_topics=["solution architecture", "tenant onboarding", "network boundary mapping", "identity federation", "customer incident response", "handoff to support teams"],
        cross_links=[("../ai-solutions-architect/README.md", "AI Solutions Architect"), ("../agentic-ai-engineer/README.md", "Agentic AI Engineer"), ("../mcp-engineer/README.md", "MCP Engineer")],
        hero_tagline="Translate customer problems into secure production AI systems.",
        orbit_labels=["Customer", "Identity", "Integration", "Agent", "RAG", "MCP", "Ops"],
    ),
    RoleSpec(
        slug="agentic-ai-engineer",
        title="Agentic AI Engineer",
        category="Agents",
        summary="Design and operate agent systems that plan, call tools, manage state, and recover safely from ambiguity and failure.",
        why="This role exists because tool-using agents create a new class of reliability, security, and control-flow problems that simple prompt engineering does not solve.",
        org_position="Usually sits within applied AI, AI product engineering, or agent platform teams. The role collaborates deeply with MCP engineers, evals engineers, AI security, and platform engineers.",
        responsibilities=[
            "Design agent loops, planning strategies, memory boundaries, and tool policies.",
            "Balance agent autonomy against deterministic guardrails and approval steps.",
            "Instrument tool-call success, loop termination, and quality outcomes.",
            "Debug planning failures, infinite loops, stale memory, and unsafe actions.",
            "Turn experiments into bounded production systems with rollback and observability.",
        ],
        skills=["agent planning", "tool calling", "memory design", "workflow orchestration", "evaluation", "failure analysis", "prompt and context design"],
        technologies=["LLMs", "MCP", "workflow engines", "Redis", "vector databases", "OpenTelemetry", "Python"],
        boundaries=["Not every LLM workflow should be agentic.", "Owns decision-loop design more than raw model training.", "Should reduce, not increase, uncontrolled blast radius."],
        relationships=["Builds on classic backend workflow design, but with probabilistic next-step selection.", "Depends on AI security and platform controls to safely expose tools.", "Often partners with AI observability and evals for quality signals."],
        architecture=["User request", "Planner", "Tool policy", "Execution state", "Memory", "Fallbacks", "Telemetry"],
        learning_path=["Agent fundamentals", "Loop design", "State and memory", "Tool governance", "Observability", "Senior design trade-offs"],
        focus_areas=["planning", "reasoning", "tool use", "multi-agent coordination", "guardrails", "recovery"],
        role_specific_topics=["reflection", "termination conditions", "agent loops", "state checkpoints", "human approval", "tool-call auditing"],
        cross_links=[("../mcp-engineer/README.md", "MCP Engineer"), ("../agent-platform-engineer/README.md", "Agent Platform Engineer"), ("../ai-evals-engineer/README.md", "AI Evals Engineer")],
        hero_tagline="Engineer bounded autonomy instead of uncontrolled model behavior.",
        orbit_labels=["Planner", "Tools", "Memory", "State", "Policy", "Telemetry", "Recovery"],
    ),
    RoleSpec(
        slug="ai-platform-engineer",
        title="AI Platform Engineer",
        category="Platform & Infrastructure",
        summary="Build the internal platform that makes AI workloads deployable, governable, observable, and cost-aware for product teams.",
        why="This role exists because enterprise teams need a reusable control plane for model access, agent deployment, GPUs, evaluation, and spend controls rather than each team inventing its own path.",
        org_position="Usually part of platform engineering or infrastructure, but focused specifically on AI workloads and the interfaces product teams use to ship them.",
        responsibilities=[
            "Provide golden paths for model serving, agents, RAG pipelines, and evals.",
            "Own multi-tenant controls for identity, quotas, policy, and observability.",
            "Expose platform APIs, templates, and workflows that product teams can self-serve.",
            "Keep GPU and model infrastructure reliable, secure, and cost-aware.",
            "Shape adoption strategy so platform abstractions simplify real engineering work.",
        ],
        skills=["platform design", "Kubernetes", "GPU scheduling", "multi-tenancy", "IAM", "GitOps", "developer experience"],
        technologies=["Kubernetes", "vLLM", "KServe", "Argo CD", "OpenTelemetry", "Prometheus", "Vault", "Redis"],
        boundaries=["Not just cluster administration.", "Owns platform interfaces, not just underlying infrastructure.", "Must balance standardization against product-team flexibility."],
        relationships=["AI Platform Engineering = Platform Engineering + GPU/LLM/Agent controls.", "Overlaps with DevOps/SRE in operations, but owns product-facing platform abstractions.", "Works closely with AI infra, AI DX, security, and FinOps."],
        architecture=["Developer portal", "Platform API", "Agent and model runtime", "Policy layer", "Telemetry", "Cost controls", "GitOps"],
        learning_path=["Platform foundations", "AI workload primitives", "Multi-tenancy", "Policy and secrets", "Observability", "Enterprise rollout"],
        focus_areas=["self-service", "multi-tenancy", "GPU platform", "golden paths", "policy", "cost"],
        role_specific_topics=["platform APIs", "namespace strategy", "quota management", "control plane reliability", "tenant onboarding", "platform adoption metrics"],
        cross_links=[("../ai-infrastructure-engineer/README.md", "AI Infrastructure Engineer"), ("../ai-developer-experience-engineer/README.md", "AI Developer Experience Engineer"), ("../ai-finops-engineer/README.md", "AI FinOps Engineer")],
        hero_tagline="Turn AI infrastructure into a governed self-service platform.",
        orbit_labels=["Portal", "Policy", "GPU", "Serve", "Agents", "GitOps", "Cost"],
    ),
    RoleSpec(
        slug="ai-infrastructure-engineer",
        title="AI Infrastructure Engineer",
        category="Platform & Infrastructure",
        summary="Design and operate the compute, networking, storage, and runtime foundations that AI workloads depend on at scale.",
        why="This role exists because GPU-heavy training and inference systems fail in ways that standard CPU-centric cloud operations often do not anticipate.",
        org_position="Lives close to infrastructure, SRE, or platform engineering and often owns the deeper node-level and hardware-level concerns underneath AI platforms.",
        responsibilities=[
            "Operate GPU clusters, storage paths, and high-throughput networking.",
            "Tune inference or training-adjacent workloads for utilization and resilience.",
            "Debug node-level, driver-level, and runtime-level failures quickly.",
            "Plan capacity and placement strategies for expensive accelerator fleets.",
            "Collaborate with platform and FinOps teams to improve hardware efficiency.",
        ],
        skills=["Linux", "Kubernetes", "CUDA", "GPU diagnostics", "storage performance", "networking", "capacity planning"],
        technologies=["NVIDIA stack", "CUDA", "nvidia-smi", "Kubernetes", "containerd", "RDMA", "object storage"],
        boundaries=["Not purely ML model work.", "Owns the execution substrate more than prompt/application logic.", "Must think in fleet economics as much as host health."],
        relationships=["Builds on SRE and platform engineering, but with GPU-specific bottlenecks and failure domains.", "Feeds AI platform engineering with the infrastructure primitives platform teams expose safely."],
        architecture=["GPU nodes", "scheduler", "inference runtime", "storage", "network fabric", "observability", "capacity model"],
        learning_path=["Linux and containers", "GPU fundamentals", "Kubernetes scheduling", "performance and networking", "capacity and incident response", "fleet design"],
        focus_areas=["GPU clusters", "CUDA", "storage", "RDMA", "hardware utilization", "capacity"],
        role_specific_topics=["MIG partitioning", "GPU memory fragmentation", "driver compatibility", "node health", "capacity forecasting", "cluster scaling"],
        cross_links=[("../inference-engineer/README.md", "Inference Engineer"), ("../ai-platform-engineer/README.md", "AI Platform Engineer"), ("../ai-finops-engineer/README.md", "AI FinOps Engineer")],
        hero_tagline="Run the substrate that makes large-scale AI actually possible.",
        orbit_labels=["GPU", "CUDA", "Scheduler", "RDMA", "Storage", "Telemetry", "Capacity"],
    ),
    RoleSpec(
        slug="ai-reliability-engineer",
        title="AI Reliability Engineer",
        category="Reliability & Operations",
        summary="Apply SRE thinking to AI systems by defining reliability targets for model, agent, and tool workflows and operating them under real production pressure.",
        why="This role exists because AI workloads add new latency, quality, cost, and dependency failure modes that classic service SRE metrics do not fully capture on their own.",
        org_position="Usually sits with SRE or reliability engineering, but partners deeply with AI product, agent, platform, and observability teams.",
        responsibilities=[
            "Define AI-specific SLIs and SLOs for latency, success, quality, and spend.",
            "Lead incident response for agent, model, and retrieval failures.",
            "Engineer safe fallbacks, circuit breakers, and blast-radius controls.",
            "Capacity-plan for token throughput, GPU availability, and dependency load.",
            "Drive postmortems and reliability improvements into architecture changes.",
        ],
        skills=["SRE", "incident response", "Prometheus", "OpenTelemetry", "capacity planning", "failure analysis", "runbook design"],
        technologies=["Prometheus", "Grafana", "OpenTelemetry", "Kubernetes", "LLM gateways", "Redis", "queues"],
        boundaries=["Not only alert tuning.", "Owns service objectives and resilience patterns, not just uptime dashboards.", "Must connect reliability with cost and quality."],
        relationships=["AI Reliability Engineering = Traditional SRE + AI dependency and GPU-aware telemetry.", "Partners with observability, platform, and product teams to define meaningful signals."],
        architecture=["Request path", "model/tool dependencies", "telemetry", "SLOs", "fallbacks", "incident automation", "postmortem feedback loop"],
        learning_path=["SRE foundations", "AI request-path decomposition", "quality and latency metrics", "incident handling", "capacity", "resilience architecture"],
        focus_areas=["SLIs", "SLOs", "error budgets", "latency", "TTFT", "incident response"],
        role_specific_topics=["token throughput", "agent success rate", "retrieval success", "tool dependency health", "quality rollback", "error budget policy"],
        cross_links=[("../ai-observability-engineer/README.md", "AI Observability Engineer"), ("../ai-platform-engineer/README.md", "AI Platform Engineer"), ("../inference-engineer/README.md", "Inference Engineer")],
        hero_tagline="Treat AI reliability as an operating discipline, not a hope.",
        orbit_labels=["SLO", "Latency", "TTFT", "Alerts", "Fallback", "Runbook", "Budget"],
    ),
    RoleSpec(
        slug="mcp-engineer",
        title="MCP Engineer",
        category="Agents",
        summary="Design, secure, and operate Model Context Protocol servers, clients, gateways, and enterprise tool ecosystems.",
        why="This role exists because MCP turns context and tools into a programmable integration layer, which creates protocol, identity, audit, and blast-radius concerns that need dedicated engineering discipline.",
        org_position="Often embedded in agent platform, integration platform, or applied AI teams, with strong ties to security and platform engineering.",
        responsibilities=[
            "Build MCP servers, clients, and transport patterns suitable for production use.",
            "Design gateway controls for authentication, authorization, auditing, and rate limits.",
            "Partition tools and resources safely across tenants and trust boundaries.",
            "Debug protocol failures, transport problems, and tool invocation errors.",
            "Standardize enterprise integration patterns so agents can use tools safely.",
        ],
        skills=["protocol design", "OAuth", "RBAC/ABAC", "HTTP and stdio transport", "gateway architecture", "audit design", "tool lifecycle"],
        technologies=["MCP", "OAuth", "HTTP", "stdio", "API gateways", "Kubernetes", "Redis"],
        boundaries=["Not just building tools.", "Owns the contract and control layer between agents and tools.", "Must think like both an integration engineer and a security engineer."],
        relationships=["Closely linked to agentic AI engineering and AI security.", "Provides the substrate agents rely on for external actions and context access."],
        architecture=["Agent", "MCP client", "gateway", "tool registry", "authz policy", "audit store", "back-end APIs"],
        learning_path=["Protocol fundamentals", "transport and identity", "tool isolation", "gateway design", "audit and rate limiting", "enterprise architecture"],
        focus_areas=["MCP protocol", "tool discovery", "transport", "authentication", "authorization", "auditing"],
        role_specific_topics=["resource exposure", "prompt delivery", "tenant isolation", "tool approval", "blast radius", "protocol debugging"],
        cross_links=[("../agentic-ai-engineer/README.md", "Agentic AI Engineer"), ("../ai-security-engineer/README.md", "AI Security Engineer"), ("../agent-platform-engineer/README.md", "Agent Platform Engineer")],
        hero_tagline="Engineer the trust boundary between agents and enterprise tools.",
        orbit_labels=["Agent", "Client", "Gateway", "Policy", "Tools", "Audit", "Rate Limit"],
    ),
    RoleSpec(
        slug="agent-platform-engineer",
        title="Agent Platform Engineer",
        category="Agents",
        summary="Build the shared runtime, control plane, and guardrail systems that let many teams deploy and operate agents safely.",
        why="This role exists because one-off agents do not scale organizationally without shared runtimes, policy, evaluation, and lifecycle management.",
        org_position="Usually part of AI platform or applied platform teams and sits one layer above raw infrastructure, one layer below product-facing agent builders.",
        responsibilities=[
            "Provide runtime, registry, and deployment patterns for many agent teams.",
            "Enforce guardrails, identity, approval flows, and tenant controls centrally.",
            "Standardize observability, evaluation, and rollback hooks for agents.",
            "Own the interfaces between agents, MCP, memory, and workflow engines.",
            "Drive adoption by making the safe path the easiest path for builders.",
        ],
        skills=["platform APIs", "runtime design", "multi-tenancy", "workflow orchestration", "evaluation integration", "policy design", "Kubernetes"],
        technologies=["Kubernetes", "MCP", "workflow engines", "Redis", "OpenTelemetry", "Vault", "GitOps"],
        boundaries=["Not every agent problem is a platform problem.", "Should expose shared patterns without over-constraining teams.", "Must support lifecycle management, not just deployment."],
        relationships=["Extends platform engineering into agent-specific control planes.", "Depends on MCP, security, and observability for core platform guarantees."],
        architecture=["Agent registry", "runtime", "policy layer", "memory", "MCP gateway", "evaluation hooks", "telemetry"],
        learning_path=["Agent runtime basics", "multi-tenant controls", "policy and identity", "evaluation integration", "rollouts", "enterprise architecture"],
        focus_areas=["multi-agent runtime", "agent registry", "policy", "guardrails", "tenant isolation", "evaluation"],
        role_specific_topics=["lifecycle states", "runtime upgrades", "registry metadata", "tenant quotas", "workflow recovery", "approval pipelines"],
        cross_links=[("../agentic-ai-engineer/README.md", "Agentic AI Engineer"), ("../mcp-engineer/README.md", "MCP Engineer"), ("../ai-observability-engineer/README.md", "AI Observability Engineer")],
        hero_tagline="Provide the safe shared runtime for many production agents.",
        orbit_labels=["Registry", "Runtime", "Policy", "Memory", "Gateway", "Evals", "Telemetry"],
    ),
    RoleSpec(
        slug="llmops-engineer",
        title="LLMOps Engineer",
        category="Models & Runtime",
        summary="Operationalize the lifecycle of LLM-powered systems: releases, evaluation, routing, rollbacks, and production monitoring.",
        why="This role exists because changing prompts, models, routing rules, and evaluation policies is operational work that needs the same rigor as software delivery.",
        org_position="Lives between AI application teams and platform/reliability teams, often owning the release mechanics and production control surfaces around LLM features.",
        responsibilities=[
            "Version prompts, models, and routing rules with safe release processes.",
            "Run canaries, shadow traffic, and rollback paths for model changes.",
            "Connect evaluations and quality checks to deployment gates.",
            "Monitor drift, regression, and spend after production changes.",
            "Document and automate reproducible operating workflows for LLM systems.",
        ],
        skills=["release engineering", "CI/CD", "evaluation pipelines", "observability", "rollback design", "A/B testing", "artifact management"],
        technologies=["GitHub Actions", "Argo CD", "LLM gateways", "Prometheus", "OpenTelemetry", "Python"],
        boundaries=["Not the same as classical MLOps training pipelines.", "Owns operational change management around LLM systems more than research experimentation."],
        relationships=["Connects platform, evals, product, and SRE concerns into one release workflow.", "Often translates evaluation evidence into deploy/no-deploy decisions."],
        architecture=["Source control", "eval gates", "gateway config", "model routing", "telemetry", "rollback", "post-release review"],
        learning_path=["LLM system lifecycle", "prompt and model versioning", "release patterns", "evaluation gates", "rollback", "operational governance"],
        focus_areas=["deployment", "versioning", "canaries", "A/B testing", "drift", "rollbacks"],
        role_specific_topics=["shadow traffic", "prompt versioning", "fallback rollout", "regression detection", "release approvals", "post-release metrics"],
        cross_links=[("../ai-evals-engineer/README.md", "AI Evals Engineer"), ("../inference-engineer/README.md", "Inference Engineer"), ("../ai-platform-engineer/README.md", "AI Platform Engineer")],
        hero_tagline="Treat LLM changes like production changes, not experiments.",
        orbit_labels=["Version", "Canary", "Shadow", "Evals", "Rollback", "Drift", "Metrics"],
    ),
    RoleSpec(
        slug="inference-engineer",
        title="Inference Engineer",
        category="Models & Runtime",
        summary="Optimize model serving runtimes for latency, throughput, GPU efficiency, and predictable production behavior.",
        why="This role exists because inference performance depends on runtime internals, batching strategy, memory behavior, and GPU scheduling details that application engineers usually do not own deeply enough.",
        org_position="Usually pairs with AI infrastructure and platform teams, while supporting product teams that depend on low-latency model serving.",
        responsibilities=[
            "Tune serving stacks for TTFT, throughput, memory, and batching behavior.",
            "Profile GPU memory usage, KV cache behavior, and runtime bottlenecks.",
            "Choose quantization and parallelism strategies based on workload shape.",
            "Design autoscaling approaches that reflect real inference constraints.",
            "Debug latency spikes, out-of-memory events, and throughput collapse under load.",
        ],
        skills=["GPU profiling", "runtime internals", "performance analysis", "batching", "quantization", "autoscaling", "Kubernetes"],
        technologies=["vLLM", "TGI", "TensorRT-LLM", "Triton", "CUDA", "nvidia-smi", "Prometheus"],
        boundaries=["Not generic backend optimization.", "Owns the model-serving performance layer, not only application API code.", "Must optimize with cost and reliability in mind, not just raw speed."],
        relationships=["Sits between infra and AI application delivery.", "Feeds platform and FinOps teams with efficiency improvements and realistic capacity models."],
        architecture=["Ingress", "inference gateway", "batcher", "runtime", "GPU memory", "cache", "metrics"],
        learning_path=["Serving fundamentals", "runtime internals", "GPU memory and batching", "parallelism", "autoscaling", "fleet optimization"],
        focus_areas=["vLLM", "TGI", "TensorRT-LLM", "KV cache", "latency", "throughput"],
        role_specific_topics=["continuous batching", "quantization", "TTFT", "tokens per second", "memory fragmentation", "autoscaling signals"],
        cross_links=[("../ai-infrastructure-engineer/README.md", "AI Infrastructure Engineer"), ("../ai-reliability-engineer/README.md", "AI Reliability Engineer"), ("../ai-finops-engineer/README.md", "AI FinOps Engineer")],
        hero_tagline="Optimize the runtime path between prompts and tokens.",
        orbit_labels=["Gateway", "Batching", "KV Cache", "GPU", "TTFT", "TPS", "Scale"],
    ),
    RoleSpec(
        slug="ai-observability-engineer",
        title="AI Observability Engineer",
        category="Reliability & Operations",
        summary="Build telemetry systems that make AI workflows explainable enough to debug, govern, and improve in production.",
        why="This role exists because logs alone cannot explain modern AI failure modes; teams need prompt, retrieval, tool, and token telemetry correlated across the whole request path.",
        org_position="Usually embedded in platform, observability, or reliability teams with strong involvement in AI product and agent-platform design.",
        responsibilities=[
            "Define telemetry for prompts, tool calls, retrieval, latency, and quality.",
            "Instrument traces across agent, model, MCP, and dependency hops.",
            "Create dashboards and queries that support real incident response.",
            "Correlate model cost, quality, and performance signals in one system.",
            "Help teams turn opaque AI behavior into debuggable engineering evidence.",
        ],
        skills=["OpenTelemetry", "Prometheus", "distributed tracing", "dashboard design", "query design", "incident triage", "data modeling"],
        technologies=["OpenTelemetry", "Prometheus", "Grafana", "logs", "traces", "LLM telemetry SDKs", "Python"],
        boundaries=["Not just a dashboard builder.", "Owns telemetry design quality, not only data ingestion.", "Must connect engineering and product-quality questions."],
        relationships=["Partners with reliability, evals, platform, and security teams.", "Provides the evidence those disciplines rely on for decisions."],
        architecture=["Trace context", "prompt and tool spans", "metric pipelines", "dashboards", "alerts", "quality signals", "cost correlation"],
        learning_path=["Telemetry basics", "AI trace design", "correlation patterns", "dashboards and alerts", "incident flows", "governance and retention"],
        focus_areas=["OpenTelemetry", "tracing", "token metrics", "prompt telemetry", "RAG telemetry", "correlation"],
        role_specific_topics=["span taxonomy", "retrieval spans", "tool-call metrics", "latency percentiles", "cost overlays", "dataset-backed observability"],
        cross_links=[("../ai-reliability-engineer/README.md", "AI Reliability Engineer"), ("../ai-evals-engineer/README.md", "AI Evals Engineer"), ("../agent-platform-engineer/README.md", "Agent Platform Engineer")],
        hero_tagline="Make AI systems observable enough to operate with confidence.",
        orbit_labels=["Traces", "Metrics", "Logs", "Prompt", "Tool", "RAG", "Cost"],
    ),
    RoleSpec(
        slug="ai-security-engineer",
        title="AI Security Engineer",
        category="Trust",
        summary="Secure AI systems against prompt-level, tool-level, identity, and data-boundary failures without destroying developer velocity.",
        why="This role exists because AI systems introduce new attack surfaces like prompt injection, tool abuse, and context exfiltration that are not covered by standard AppSec patterns alone.",
        org_position="Typically bridges application security, cloud security, and AI product/platform teams. Often acts as the trust layer for agents, MCP, RAG, and model access patterns.",
        responsibilities=[
            "Model threats across prompts, tools, retrieval, and model-provider boundaries.",
            "Enforce least privilege for agents, tools, and service identities.",
            "Design controls for prompt injection, exfiltration, and tool misuse.",
            "Audit and review AI architectures for secrets, policy, and blast radius.",
            "Turn security guidance into implementation patterns teams can actually adopt.",
        ],
        skills=["threat modeling", "IAM", "OAuth", "policy engines", "sandboxing", "audit design", "cloud security"],
        technologies=["Vault", "OAuth", "RBAC", "ABAC", "MCP", "Kubernetes", "SIEM"],
        boundaries=["Not just compliance paperwork.", "Must understand actual runtime flows, not only static architecture diagrams.", "Should enable safe adoption rather than simply veto AI features."],
        relationships=["AI Security = DevSecOps + AppSec + identity + agent/tool threat modeling.", "Depends on platform and observability to enforce and prove controls."],
        architecture=["User", "agent identity", "policy engine", "MCP gateway", "data boundaries", "audit", "human approval"],
        learning_path=["Threat model basics", "prompt and tool attacks", "identity and authorization", "retrieval controls", "auditability", "enterprise policy design"],
        focus_areas=["prompt injection", "tool abuse", "least privilege", "MCP security", "audit", "sandboxing"],
        role_specific_topics=["indirect prompt injection", "supply chain", "model-provider trust", "human approval gates", "policy decision points", "tenant isolation"],
        cross_links=[("../mcp-engineer/README.md", "MCP Engineer"), ("../agentic-ai-engineer/README.md", "Agentic AI Engineer"), ("../ai-governance-engineer/README.md", "AI Governance Engineer")],
        hero_tagline="Secure prompts, tools, identities, and data paths together.",
        orbit_labels=["Threats", "Policy", "Identity", "Sandbox", "Audit", "Secrets", "Approval"],
    ),
    RoleSpec(
        slug="ai-evals-engineer",
        title="AI Evals Engineer",
        category="Trust",
        summary="Design the evaluation systems that prove AI features are improving instead of silently regressing.",
        why="This role exists because AI quality is probabilistic and changes across prompts, models, routing, retrieval, and tools; teams need a discipline for measuring that before and after production changes.",
        org_position="Usually supports AI product, LLMOps, and platform teams by building the quality gates and evidence loops they depend on.",
        responsibilities=[
            "Build offline and online evaluation pipelines with trustworthy datasets and metrics.",
            "Define agent, retrieval, and model quality success measures.",
            "Run regression tests and CI gates for prompts, models, and tool workflows.",
            "Design human-review and LLM-as-judge systems carefully.",
            "Translate evaluation evidence into product and release decisions.",
        ],
        skills=["evaluation design", "dataset curation", "statistics", "CI pipelines", "quality metrics", "analysis", "Python"],
        technologies=["Python", "CI/CD", "LLM-as-judge frameworks", "vector databases", "OpenTelemetry", "GitHub Actions"],
        boundaries=["Not just benchmark collection.", "Owns evaluation design quality, not only execution speed.", "Must help teams act on results, not just produce reports."],
        relationships=["Critical partner to LLMOps, observability, and product teams.", "Often the quality counterpart to reliability and security controls."],
        architecture=["golden datasets", "offline evals", "online evals", "judge systems", "CI gates", "reporting", "release decisions"],
        learning_path=["Evaluation fundamentals", "dataset design", "agent and RAG metrics", "CI integration", "statistical interpretation", "decision frameworks"],
        focus_areas=["golden datasets", "offline evals", "online evals", "LLM-as-judge", "regression testing", "quality metrics"],
        role_specific_topics=["tool-call success", "retrieval precision", "judge calibration", "statistical confidence", "evaluation drift", "release gates"],
        cross_links=[("../llmops-engineer/README.md", "LLMOps Engineer"), ("../ai-observability-engineer/README.md", "AI Observability Engineer"), ("../rag-engineer/README.md", "RAG Engineer")],
        hero_tagline="Make quality measurable enough to release with confidence.",
        orbit_labels=["Dataset", "Offline", "Online", "Judge", "CI Gate", "Regression", "Score"],
    ),
    RoleSpec(
        slug="ai-finops-engineer",
        title="AI FinOps Engineer",
        category="Reliability & Operations",
        summary="Engineer cost visibility and optimization for GPU, token, and agent workloads so AI systems remain economically sustainable.",
        why="This role exists because AI spend can explode through token growth, idle accelerators, bad routing, and low-efficiency runtime behavior long before traffic itself looks unusual.",
        org_position="Usually works with platform, infrastructure, reliability, and engineering leadership to turn AI spend into actionable engineering decisions.",
        responsibilities=[
            "Model unit economics for inference, retrieval, tool use, and agent workflows.",
            "Expose cost-per-request, cost-per-user, and GPU utilization signals.",
            "Recommend optimizations in routing, batching, caching, and autoscaling.",
            "Drive showback and chargeback practices for shared AI platforms.",
            "Balance cost optimization against latency, quality, and reliability goals.",
        ],
        skills=["cost modeling", "capacity planning", "unit economics", "GPU utilization analysis", "forecasting", "dashboard design", "cloud pricing"],
        technologies=["Prometheus", "Grafana", "cloud billing exports", "Kubernetes", "GPU telemetry", "Redis caches"],
        boundaries=["Not just finance reporting.", "Must understand runtime and architecture decisions well enough to change them.", "Should optimize for efficient service, not blunt cost cutting."],
        relationships=["AI FinOps = FinOps + GPU/inference/token economics.", "Closely connected to infra, inference, platform, and reliability teams."],
        architecture=["billing inputs", "runtime metrics", "GPU telemetry", "chargeback model", "optimization levers", "budget alerts", "forecasts"],
        learning_path=["FinOps basics", "AI unit economics", "GPU and token metrics", "optimization patterns", "chargeback", "leadership reporting"],
        focus_areas=["GPU utilization", "token cost", "cost per request", "batching", "model routing", "forecasting"],
        role_specific_topics=["prompt caching", "reserved capacity", "spot trade-offs", "model mix strategy", "cost anomaly detection", "budget governance"],
        cross_links=[("../inference-engineer/README.md", "Inference Engineer"), ("../ai-platform-engineer/README.md", "AI Platform Engineer"), ("../ai-reliability-engineer/README.md", "AI Reliability Engineer")],
        hero_tagline="Optimize AI systems for sustainable economics, not just scale.",
        orbit_labels=["GPU $", "Tokens", "Cache", "Routing", "Utilization", "Budget", "Forecast"],
    ),
    RoleSpec(
        slug="ai-governance-engineer",
        title="AI Governance Engineer",
        category="Trust",
        summary="Build the policy, lineage, approval, and audit systems that let organizations use AI responsibly at enterprise scale.",
        why="This role exists because enterprises need reproducible evidence about what models, prompts, tools, data, and approvals were involved in critical AI decisions.",
        org_position="Usually embedded with trust, security, platform, and architecture functions. Works across product, legal, compliance, and engineering rather than within a single application team.",
        responsibilities=[
            "Design governance flows for models, prompts, agents, and data access.",
            "Track lineage and approval state across changes and deployments.",
            "Define audit requirements that are actually implementable in production.",
            "Build controls for high-risk workflows and regulated environments.",
            "Turn policy requirements into engineering systems instead of manual checklists.",
        ],
        skills=["governance design", "auditability", "data lineage", "access control", "approval workflows", "compliance translation", "platform integration"],
        technologies=["policy engines", "audit stores", "OpenTelemetry", "Git", "databases", "workflow systems"],
        boundaries=["Not just documentation work.", "Needs engineering-grade traceability and control planes.", "Must make governance actionable without blocking all delivery."],
        relationships=["Works with security, evals, and platform teams to attach evidence and policy to real runtime systems.", "Often builds the enterprise controls that solutions architects must account for."],
        architecture=["change request", "policy engine", "lineage store", "approval workflow", "runtime evidence", "audit search", "retention controls"],
        learning_path=["Governance fundamentals", "lineage and audit", "policy implementation", "approval workflows", "risk classification", "enterprise-scale operations"],
        focus_areas=["governance", "auditability", "policy", "lineage", "access control", "oversight"],
        role_specific_topics=["prompt lineage", "model lineage", "retention", "human oversight", "risk tiers", "evidence bundles"],
        cross_links=[("../ai-security-engineer/README.md", "AI Security Engineer"), ("../ai-evals-engineer/README.md", "AI Evals Engineer"), ("../ai-solutions-architect/README.md", "AI Solutions Architect")],
        hero_tagline="Turn AI governance from policy text into operating systems.",
        orbit_labels=["Policy", "Lineage", "Approval", "Risk", "Audit", "Retention", "Evidence"],
    ),
    RoleSpec(
        slug="context-engineer",
        title="Context Engineer",
        category="Agents",
        summary="Engineer the information environment around a model so it sees the right context, in the right form, at the right cost.",
        why="This role exists because prompt quality depends less on wording alone than on retrieval, memory, ranking, token budgeting, and state assembly across a system.",
        org_position="Often overlaps with RAG, agent, and LLM engineering. This role becomes distinct in teams where context quality directly affects correctness, latency, or cost.",
        responsibilities=[
            "Design context assembly pipelines for prompts, retrieval, memory, and tool outputs.",
            "Control token budgets and compression strategies deliberately.",
            "Prevent stale, irrelevant, or poisoned context from reaching models.",
            "Measure the effect of context changes on quality and latency.",
            "Debug context-window failures and long-running conversational drift.",
        ],
        skills=["prompt architecture", "retrieval design", "ranking", "summarization", "token budgeting", "state design", "evaluation"],
        technologies=["LLMs", "RAG pipelines", "vector databases", "Redis", "Python", "OpenTelemetry"],
        boundaries=["Not just prompt writing.", "Owns context quality and structure, not only the final prompt text.", "Must balance relevance against latency and cost."],
        relationships=["Strongly overlaps with RAG and agentic AI engineering.", "Acts as the context-system counterpart to model and runtime engineering."],
        architecture=["inputs", "ranking", "memory", "compression", "prompt assembly", "token budget", "telemetry"],
        learning_path=["prompt basics", "retrieval and ranking", "memory and summarization", "token economics", "quality measurement", "advanced context architectures"],
        focus_areas=["context windows", "compression", "memory", "ranking", "token budgets", "context poisoning"],
        role_specific_topics=["state summarization", "tool-output compaction", "freshness scoring", "context cache design", "context truncation", "conversation drift"],
        cross_links=[("../rag-engineer/README.md", "RAG Engineer"), ("../agentic-ai-engineer/README.md", "Agentic AI Engineer"), ("../llmops-engineer/README.md", "LLMOps Engineer")],
        hero_tagline="Engineer what the model sees, not just what it says.",
        orbit_labels=["Prompt", "Memory", "Ranking", "Compression", "Budget", "Freshness", "State"],
    ),
    RoleSpec(
        slug="rag-engineer",
        title="RAG Engineer",
        category="Data & Retrieval",
        summary="Build retrieval systems that feed models relevant, fresh, authorized context instead of forcing them to hallucinate.",
        why="This role exists because retrieval quality often determines whether an AI system is trustworthy, yet retrieval design is an engineering discipline of its own.",
        org_position="Usually supports AI product, agent, and platform teams with ingestion, indexing, retrieval quality, and freshness architecture.",
        responsibilities=[
            "Design ingestion, chunking, metadata, embedding, and retrieval flows.",
            "Choose vector, hybrid, or reranking approaches based on workload trade-offs.",
            "Protect document security and freshness across the retrieval pipeline.",
            "Measure retrieval quality and debug bad grounding behavior.",
            "Scale indexing and search pipelines reliably in production.",
        ],
        skills=["retrieval design", "chunking", "metadata modeling", "vector search", "hybrid search", "evaluation", "pipeline operations"],
        technologies=["vector databases", "embeddings", "rerankers", "object storage", "PostgreSQL/pgvector", "Python"],
        boundaries=["Not just 'put docs in a vector DB'.", "Owns the data and retrieval path more than the model path itself.", "Must think about permissions and freshness as first-class requirements."],
        relationships=["Works closely with context engineers, evals, and AI security.", "Provides grounded context to agents and LLM applications."],
        architecture=["source docs", "ingestion", "chunking", "embedding", "index", "retrieval", "rerank", "citations"],
        learning_path=["RAG basics", "ingestion and chunking", "search and reranking", "evaluation", "security and freshness", "enterprise architecture"],
        focus_areas=["ingestion", "chunking", "embeddings", "vector search", "reranking", "freshness"],
        role_specific_topics=["hybrid search", "document ACLs", "query rewriting", "index rebuilds", "metadata schema", "retrieval quality metrics"],
        cross_links=[("../context-engineer/README.md", "Context Engineer"), ("../ai-evals-engineer/README.md", "AI Evals Engineer"), ("../ai-security-engineer/README.md", "AI Security Engineer")],
        hero_tagline="Ground models with trustworthy retrieval, not optimistic assumptions.",
        orbit_labels=["Docs", "Chunking", "Embeddings", "Index", "Search", "Rerank", "Freshness"],
    ),
    RoleSpec(
        slug="ai-solutions-architect",
        title="AI Solutions Architect",
        category="Customer / Solutions",
        summary="Design enterprise AI architectures that satisfy business constraints, integration realities, security boundaries, and operational ownership.",
        why="This role exists because AI adoption often fails not on model quality alone, but on architecture misalignment with enterprise identity, networking, governance, and cost constraints.",
        org_position="Typically works at the boundary between customer, product, platform, and leadership concerns. More architecture-heavy than forward-deployed roles, but still technical enough to reason through production flows precisely.",
        responsibilities=[
            "Translate business and compliance requirements into system architecture decisions.",
            "Design multi-system AI solutions spanning RAG, agents, MCP, and enterprise APIs.",
            "Account for reliability, DR, security, and ownership in solution design.",
            "Document trade-offs so teams understand why the chosen architecture fits.",
            "Align stakeholders around realistic implementation phases and boundaries.",
        ],
        skills=["system design", "cloud architecture", "identity and networking", "security", "enterprise integration", "trade-off analysis", "communication"],
        technologies=["cloud platforms", "Kubernetes", "API gateways", "RAG", "MCP", "identity providers", "queues"],
        boundaries=["Not just pre-sales diagrams.", "Must tie architecture to operational and organizational ownership.", "Should not hand-wave away implementation cost."],
        relationships=["Partners with forward-deployed engineers for delivery and with platform/security/governance teams for feasibility.", "Often frames the north-star architecture others implement."],
        architecture=["business inputs", "identity", "integration layer", "AI control plane", "data boundaries", "observability", "governance"],
        learning_path=["systems and cloud", "AI architecture primitives", "security and identity", "trade-off communication", "enterprise design", "staff/principal thinking"],
        focus_areas=["enterprise architecture", "requirements", "integration", "security", "resilience", "cost"],
        role_specific_topics=["reference architectures", "stakeholder constraints", "multi-region design", "DR strategy", "operating model", "boundary decisions"],
        cross_links=[("../forward-deployed-ai-engineer/README.md", "Forward-Deployed AI Engineer"), ("../ai-governance-engineer/README.md", "AI Governance Engineer"), ("../ai-platform-engineer/README.md", "AI Platform Engineer")],
        hero_tagline="Design AI systems that fit the enterprise they must survive in.",
        orbit_labels=["Business", "Identity", "Network", "AI Plane", "Data", "Ops", "Governance"],
    ),
    RoleSpec(
        slug="ai-systems-engineer",
        title="AI Systems Engineer",
        category="Platform & Infrastructure",
        summary="Apply distributed-systems and systems-debugging thinking to AI runtimes, state, storage, and inter-service coordination.",
        why="This role exists because AI systems at scale are still systems: they involve queues, caches, concurrency, backpressure, storage, and fault tolerance regardless of how good the model is.",
        org_position="Typically sits close to platform, backend, and infrastructure concerns. Often acts as the engineer who can reason across the whole AI control/data path as a system.",
        responsibilities=[
            "Reason about queues, caches, databases, consistency, and state in AI systems.",
            "Debug cross-service failures involving runtime, networking, and storage together.",
            "Design for fault tolerance, backpressure, and bounded retries.",
            "Model how agent, retrieval, and inference systems behave under load.",
            "Translate AI feature behavior into distributed-systems reliability patterns.",
        ],
        skills=["distributed systems", "Linux", "networking", "queues", "caches", "databases", "performance debugging"],
        technologies=["Redis", "PostgreSQL", "Kubernetes", "queues", "OpenTelemetry", "LLM runtimes"],
        boundaries=["Not solely infra, not solely AI application work.", "Owns reasoning across system boundaries more than a single component.", "Should make AI workloads legible to classic systems engineering methods."],
        relationships=["Builds on backend and distributed-systems foundations while applying them to AI workloads.", "Pairs well with AI infrastructure, platform, and reliability roles."],
        architecture=["client", "orchestrator", "queue", "runtime", "cache", "database", "telemetry", "recovery"],
        learning_path=["distributed systems", "AI request paths", "state and consistency", "fault tolerance", "performance analysis", "staff-level architecture"],
        focus_areas=["distributed systems", "state", "storage", "caching", "performance", "fault tolerance"],
        role_specific_topics=["backpressure", "state consistency", "workflow queues", "cache invalidation", "retries", "systemic failure analysis"],
        cross_links=[("../ai-infrastructure-engineer/README.md", "AI Infrastructure Engineer"), ("../agent-platform-engineer/README.md", "Agent Platform Engineer"), ("../ai-reliability-engineer/README.md", "AI Reliability Engineer")],
        hero_tagline="Treat AI workloads as distributed systems, because they are.",
        orbit_labels=["Queue", "Cache", "DB", "State", "Runtime", "Network", "Recovery"],
    ),
    RoleSpec(
        slug="ai-developer-experience-engineer",
        title="AI Developer Experience Engineer",
        category="Platform & Infrastructure",
        summary="Reduce the friction of building on internal AI platforms by creating portals, CLIs, templates, docs, and self-service workflows that developers actually want to use.",
        why="This role exists because a technically powerful AI platform still fails if developers cannot discover, trust, and operate it efficiently.",
        org_position="Usually embedded in platform engineering, close to product engineering teams. The role turns platform capability into developer adoption and productivity.",
        responsibilities=[
            "Design portals, CLIs, SDKs, and templates for common AI workflows.",
            "Create local-dev, test, and deployment experiences that reduce friction.",
            "Document platform paths clearly enough that engineers can self-serve safely.",
            "Measure and improve developer productivity and adoption signals.",
            "Shape abstractions so they hide complexity without hiding critical reality.",
        ],
        skills=["DX design", "documentation", "CLI and SDK design", "platform APIs", "templates", "CI/CD", "feedback loops"],
        technologies=["developer portals", "CLIs", "SDKs", "GitHub Actions", "Kubernetes", "templates", "docs-as-code"],
        boundaries=["Not just writing docs.", "Owns the usability of platform interfaces, not only their existence.", "Must avoid abstractions that make debugging impossible."],
        relationships=["Strongly tied to AI platform engineering.", "Often makes the difference between platform capability and actual platform adoption."],
        architecture=["developer portal", "CLI/SDK", "template flow", "platform API", "preview/test loop", "deploy path", "feedback metrics"],
        learning_path=["DX fundamentals", "portal and CLI design", "golden paths", "local dev", "documentation systems", "adoption strategy"],
        focus_areas=["developer portals", "SDKs", "CLIs", "templates", "self-service", "productivity"],
        role_specific_topics=["golden paths", "preview environments", "template maintenance", "DX metrics", "safe abstractions", "feedback loops"],
        cross_links=[("../ai-platform-engineer/README.md", "AI Platform Engineer"), ("../llmops-engineer/README.md", "LLMOps Engineer"), ("../forward-deployed-ai-engineer/README.md", "Forward-Deployed AI Engineer")],
        hero_tagline="Make the internal AI platform easy to use without making it naive.",
        orbit_labels=["Portal", "CLI", "SDK", "Templates", "Preview", "Deploy", "Feedback"],
    ),
]

MANDATORY_FILES = [
    "README.md",
    "fundamentals.md",
    "questions.md",
    "troubleshooting.md",
    "senior-scenarios.md",
    "challenges.md",
    "cheatsheet.md",
    "architecture/01-basic-flow.md",
    "architecture/02-production-flow.md",
    "architecture/03-enterprise-flow.md",
    "assets/hero.svg",
]


def slug_title(slug: str) -> str:
    return slug.replace("-", " ").title().replace("Ai ", "AI ").replace("Llm", "LLM").replace("Mcp", "MCP").replace("Rag", "RAG")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_if_missing(path: Path, content: str) -> None:
    if path.exists():
        return
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def q_block(prefix: str, idx: int, question: str, difficulty: str, roles: str, test: str, answer: str, senior: str, followups: list[str], red_flags: str) -> str:
    follow = "\n".join(f"- {item}" for item in followups)
    return textwrap.dedent(
        f"""\
        ### {prefix}{idx}. {question}

        **DIFFICULTY:** {difficulty}
        **ROLE:** {roles}

        **WHAT THE INTERVIEWER IS TESTING:** {test}

        **ANSWER:** {answer}

        **SENIOR-LEVEL ANSWER:** {senior}

        **FOLLOW-UP QUESTIONS:**
        {follow}

        **RED FLAGS:** {red_flags}

        ---
        """
    )


def scenario_block(idx: int, title: str, spec: RoleSpec, scenario_type: str) -> str:
    symptom = spec.role_specific_topics[idx % len(spec.role_specific_topics)]
    tech = spec.technologies[idx % len(spec.technologies)]
    focus = spec.focus_areas[idx % len(spec.focus_areas)]
    return textwrap.dedent(
        f"""\
        ## {scenario_type} {idx}: {title}

        **Scenario**  
        A production team reports a problem around **{symptom}** in a system centered on **{tech}**. The issue is now affecting delivery confidence for the **{spec.title}** role.

        **Symptoms**  
        - Latency, reliability, or correctness regressed in a way product teams can feel.
        - Engineering dashboards show ambiguity rather than a single obvious root cause.
        - Multiple teams are asking whether the problem is platform, application, model, security, or cost related.

        **Impact**  
        The role owner must restore service while preserving trust, safety, and a path to long-term prevention.

        **Initial assumptions**  
        - The first visible symptom may not identify the true control boundary.
        - At least one upstream or downstream dependency is involved.
        - A rollback might reduce impact faster than a perfect diagnosis.

        **What to check first**  
        1. Confirm scope: tenant, model, workflow, cluster, region, or customer.
        2. Identify whether the failure centers on **{focus}** or only looks that way.
        3. Compare current behavior to the last known good configuration or release.

        **Commands / evidence to gather**  
        ```bash
        kubectl get pods -A
        kubectl logs deploy/app -n platform --tail=100
        curl -vk https://service.internal/health
        jq . < event.json
        ```

        **Logs / Metrics / Traces**  
        - Logs should reveal the earliest component that lost a valid assumption.
        - Metrics should tell you whether the system is saturated, blocked, or simply wrong.
        - Traces should identify which hop introduced delay or incorrect behavior.

        **Likely root causes**  
        - Misconfigured **{tech}** integration or rollout drift.
        - Hidden dependency contention caused by **{focus}** design trade-offs.
        - Security, policy, or quota changes that were technically correct but operationally destabilizing.

        **Investigation flow**  
        Start at the user-visible symptom, then walk inward toward the first shared control boundary. Do not jump straight to the deepest infrastructure layer unless evidence points there. Validate whether this is a correctness problem, a capacity problem, a dependency problem, or a bad deployment.

        **Resolution**  
        Prefer the fastest reversible mitigation first: rollback, disable a risky path, route to a safer fallback, reduce concurrency, or tighten permissions depending on what preserves safety and service best.

        **Validation**  
        Prove recovery using:
        - healthy request success rates
        - restored latency envelope
        - no further authorization or data-integrity violations
        - stable metrics for at least one normal traffic cycle

        **Prevention**  
        - Add a guardrail or preflight check for **{symptom}**.
        - Improve observability so this failure becomes diagnosable faster.
        - Add release gates, quotas, or policy tests before the next rollout.

        **Senior engineer considerations**  
        A senior engineer does not stop at "what broke." They ask why the surrounding architecture allowed this class of failure to become user-visible without earlier containment.

        ---
        """
    )


def challenge_block(idx: int, title: str, spec: RoleSpec, level: str) -> str:
    tech = spec.technologies[idx % len(spec.technologies)]
    topic = spec.role_specific_topics[idx % len(spec.role_specific_topics)]
    return textwrap.dedent(
        f"""\
        ## Challenge {idx}: {title}

        **Level:** {level}

        **Objective**  
        Build confidence operating **{tech}** in a way that reflects the responsibilities of a **{spec.title}**.

        **Scenario**  
        You inherit a workflow where **{topic}** is causing friction for the team. Your task is to turn the current state into a production-safe operating pattern.

        **Requirements**  
        - Preserve security and auditability.
        - Keep the system observable enough for future debugging.
        - Document one explicit trade-off you are making.

        **Constraints**  
        - Assume no perfect greenfield rewrite.
        - Prefer an incremental change that can be validated quickly.

        **Tasks**  
        1. Inspect the current state.
        2. Propose a safer or more scalable configuration.
        3. Show how you would validate the result.
        4. Explain a rollback path.

        **Commands / configuration**  
        ```bash
        kubectl get deploy -A
        helm get values platform -n ai
        curl -s https://service.internal/readyz
        python3 scripts/check.py
        ```

        ```yaml
        kind: Deployment
        metadata:
          name: role-lab
        spec:
          replicas: 2
        ```

        **Expected result**  
        The workflow becomes safer, easier to observe, and easier to operate during failure.

        **Solution**  
        Start by clarifying the current failure boundary, then apply the smallest change that improves **{topic}** without widening blast radius. In most real systems that means hardening interfaces, adding guardrails, and validating outcomes with telemetry rather than rewriting the stack.

        **Explanation**  
        This challenge tests whether you can connect implementation details to operating outcomes instead of optimizing one local component in isolation.

        **Verification**  
        - Confirm successful rollout or config application.
        - Confirm key metrics and traces improved.
        - Confirm rollback instructions still work.

        **Possible failure modes**  
        - Validation only checks happy-path behavior.
        - Hidden dependencies still violate the assumptions behind the fix.
        - The new control improves one metric but worsens cost or latency.

        **Stretch challenge**  
        Extend the design for multi-tenant or multi-region operation and explain what additional controls become necessary.

        ---
        """
    )


def render_readme(spec: RoleSpec) -> str:
    qa = []
    architecture_flow = "\n  │\n  ▼\n".join(spec.architecture)
    prompts = [
        ("Why would a company invest in this role instead of asking a general software or DevOps engineer to absorb the work?", "🟠 Senior", "Whether the candidate understands the distinct production complexity behind the role.", "Because the role exists at a failure boundary where generic engineering knowledge stops being enough.", "The senior framing is that specialization here is not about prestige, it is about ownership of new operational risk.", ["How does this role intersect with DevOps and SRE?", "What anti-pattern appears when nobody explicitly owns this concern?"], "Answering with marketing language instead of concrete engineering boundaries."),
        ("What are the most important responsibilities of this role in a production organization?", "🔵 Intermediate", "Whether you can distinguish core ownership from adjacent responsibilities.", f"The role is responsible for {spec.responsibilities[0].lower()} and related operating concerns.", f"A senior engineer would emphasize not just building systems, but making them governable, observable, and supportable under production pressure in {spec.title.lower()} domains.", ["Which responsibilities should stay with platform or security teams?", "Where does this role most often get pulled into incident response?"], "Listing technologies without explaining operational ownership."),
        ("How does this role relate to DevOps, SRE, platform engineering, and cloud engineering?", "🟠 Senior", "Whether you can place the role inside a broader engineering organization.", f"It overlaps with {spec.relationships[0].lower()}", f"The senior answer is to describe the control boundaries clearly: what this role inherits from existing disciplines and what new AI-specific complexity it adds.", ["Where does this role create new interfaces with security or FinOps?", "What should remain centralized versus team-local?"], "Pretending the role is completely separate from existing engineering disciplines."),
        ("What skill stack should a senior engineer in this role have?", "🔵 Intermediate", "Whether you understand that seniority here is about systems thinking plus execution, not just tool familiarity.", f"A senior engineer should combine {', '.join(spec.skills[:4])}, then layer on the rest through production repetition.", f"The best answer ties each skill to a failure mode: identity and networking failures, rollout failures, retrieval failures, GPU contention, or cost explosions depending on the role.", ["Which skills are foundational versus role-specific?", "How would you onboard an engineer transitioning into this role?"], "Giving a shopping list of buzzwords with no prioritization."),
        ("Where does this role sit in a modern engineering organization?", "🟢 Beginner", "Whether you can explain the role in organizational terms, not only technical terms.", spec.org_position, f"The senior framing is to explain why the role must collaborate across product, platform, security, and operations rather than acting as an isolated specialty.", ["Which teams are the closest day-to-day partners?", "What tension usually appears around ownership?"], "Treating the role as if it only works alone."),
    ]
    for idx in range(1, 26):
        base = prompts[(idx - 1) % len(prompts)]
        question = base[0]
        difficulty = base[1]
        test = base[2]
        answer = base[3]
        senior = f"{base[4]} For this role, that usually shows up around **{spec.focus_areas[(idx - 1) % len(spec.focus_areas)]}** and **{spec.role_specific_topics[(idx - 1) % len(spec.role_specific_topics)]}**."
        followups = [f"{item} for {spec.title} specifically?" for item in base[5]]
        red = base[6]
        qa.append(q_block("Q", idx, question, difficulty, spec.title, test, answer, senior, followups, red))
    links = "\n".join(
        [
            "- [fundamentals.md](fundamentals.md)",
            "- [questions.md](questions.md)",
            "- [troubleshooting.md](troubleshooting.md)",
            "- [senior-scenarios.md](senior-scenarios.md)",
            "- [challenges.md](challenges.md)",
            "- [cheatsheet.md](cheatsheet.md)",
            "- [architecture/01-basic-flow.md](architecture/01-basic-flow.md)",
            "- [architecture/02-production-flow.md](architecture/02-production-flow.md)",
            "- [architecture/03-enterprise-flow.md](architecture/03-enterprise-flow.md)",
        ]
    )
    cross = "\n".join(f"- See also: [{label}]({target})" for target, label in spec.cross_links)
    roadmap = "\n      ↓\n".join(spec.learning_path)
    responsibilities = "\n".join(f"- {item}" for item in spec.responsibilities)
    skills = "\n".join(f"- {item}" for item in spec.skills)
    technologies = ", ".join(spec.technologies)
    boundaries = "\n".join(f"- {item}" for item in spec.boundaries)
    relationships = "\n".join(f"- {item}" for item in spec.relationships)
    return textwrap.dedent(
        f"""\
        # {spec.title}

        **{spec.hero_tagline}**

        ## What this role is

        {spec.summary}

        ## Why this role exists

        {spec.why}

        ## Where it sits in modern engineering organisations

        {spec.org_position}

        ## Role responsibilities

        {responsibilities}

        ## Required skill stack

        {skills}

        ## Technologies commonly involved

        {technologies}

        ## Role boundaries

        {boundaries}

        ## Relationship to DevOps / SRE / Platform / Cloud engineering

        {relationships}

        ## Typical production architecture

        ```text
        {architecture_flow}
        ```

        ## Learning roadmap

        ```text
        {roadmap}
        ```

        ## Beginner → Senior → Staff progression

        - **Beginner:** learns the core workflow, tools, and failure vocabulary.
        - **Senior:** designs safer systems, debugs incidents systematically, and explains trade-offs clearly.
        - **Staff / Principal:** defines platform patterns, governance boundaries, reliability targets, and cross-team operating models.

        ## Interview focus areas

        - {spec.focus_areas[0]}
        - {spec.focus_areas[1]}
        - {spec.focus_areas[2]}
        - {spec.focus_areas[3]}
        - {spec.focus_areas[4]}

        ## Practical learning path

        1. Learn the mechanisms in `fundamentals.md`.
        2. Pressure-test your understanding with `questions.md`.
        3. Practice incident thinking in `troubleshooting.md`.
        4. Move into trade-off reasoning in `senior-scenarios.md`.
        5. Use `challenges.md` and `cheatsheet.md` as hands-on companions.

        ## Directory navigation

        {links}

        ## Cross-links

        {cross}

        ## Q&A

        {"".join(qa)}
        """
    )


def render_fundamentals(spec: RoleSpec) -> str:
    entries = []
    themes = [
        ("What are the core production primitives behind this role?", "🟢 Beginner", "Whether you know the building blocks well enough to reason about higher-order failures."),
        ("Why does this role require systems thinking instead of only model or application knowledge?", "🔵 Intermediate", "Whether you can connect local mechanisms to end-to-end production outcomes."),
        ("Which failure modes become common when teams scale this capability too quickly?", "🟠 Senior", "Whether you understand operational maturity problems, not just happy-path mechanics."),
        ("How should a senior engineer reason about trade-offs in this role?", "🟠 Senior", "Whether you can balance speed, safety, latency, cost, and ownership."),
        ("What production telemetry matters most here?", "🔵 Intermediate", "Whether you know how to prove a system is healthy instead of assuming it."),
    ]
    for idx in range(1, 26):
        theme = themes[(idx - 1) % len(themes)]
        topic = spec.role_specific_topics[(idx - 1) % len(spec.role_specific_topics)]
        focus = spec.focus_areas[(idx - 1) % len(spec.focus_areas)]
        tech = spec.technologies[(idx - 1) % len(spec.technologies)]
        answer = (
            f"In {spec.title.lower()}, one of the core ideas is that **{topic}** is never only a feature choice. "
            f"It changes how the system behaves around **{focus}**, and that means the engineer has to reason about architecture, operations, and failure containment at the same time. "
            f"For example, when a team introduces or changes **{tech}**, the useful question is not only 'does it work?' but also 'how does it fail, who owns it, how is it observed, and what does it cost under load?'."
        )
        senior = (
            f"The senior version of this answer is to connect mechanism to production reality. A strong engineer in this role will explain the internal moving parts, then immediately tie them to deployment topology, security boundaries, rollback strategy, and the evidence required to prove the design is healthy. "
            f"They will also separate local optimizations from system optimizations: improving **{topic}** is only a win if it does not silently worsen **{focus}** elsewhere."
        )
        follow = [
            f"What would break first if {topic} scaled 10x?",
            f"How would you instrument {focus} so you could prove the answer in production?",
            f"When would {tech} be the wrong choice for this role?",
        ]
        entries.append(q_block("Q", idx, theme[0], theme[1], spec.title, theme[2], answer, senior, follow, "Staying at dictionary-definition depth and never reaching production trade-offs."))
    return f"# {spec.title} — Fundamentals\n\n---\n\n{''.join(entries)}"


def render_questions(spec: RoleSpec) -> str:
    entries = []
    ladders = [
        ("Foundational", "What does success look like for this role in a healthy production environment?"),
        ("Intermediate", "How would you explain the most common architecture pattern used by this role to another engineer?"),
        ("Senior", "Which trade-off would you prioritize first when latency, safety, and cost are all under pressure?"),
        ("Staff", "How would you standardize this capability across multiple teams without over-centralizing everything?"),
        ("Principal", "How would you design the enterprise control plane that governs this role's critical workflows?"),
    ]
    for idx in range(1, 26):
        level, question = ladders[(idx - 1) % len(ladders)]
        topic = spec.role_specific_topics[(idx - 1) % len(spec.role_specific_topics)]
        focus = spec.focus_areas[(idx - 1) % len(spec.focus_areas)]
        answer = (
            f"A strong answer should be role-specific: in {spec.title.lower()}, success depends on how well the engineer can make **{topic}** reliable, observable, and governable while supporting **{focus}** goals. "
            f"In interviews, I would explain the mechanism first, then add when I would use it, when I would avoid it, and what telemetry or runbooks I would require before trusting it in production."
        )
        senior = (
            f"The senior/staff/principal lens is to think in terms of operating models, not isolated tickets. If the organization relies on this role heavily, who owns the control plane, who approves risky changes, how is blast radius limited, and what would a rollback look like? "
            f"That perspective is what differentiates a senior answer from a merely informed one."
        )
        follow = [
            f"Which dependency usually hides the real root cause when {topic} fails?",
            f"How would you test this before a production rollout?",
            f"How do you keep {focus} measurable instead of subjective?",
        ]
        entries.append(q_block("Q", idx, f"[{level}] {question}", "🟠 Senior" if level in {"Senior", "Staff", "Principal"} else "🔵 Intermediate", spec.title, f"Whether you can answer at the {level.lower()} layer rather than stopping at mechanics.", answer, senior, follow, "Answering with generic AI advice that could fit any role equally well."))
    return f"# {spec.title} — Interview Questions\n\n---\n\n{''.join(entries)}"


def render_troubleshooting(spec: RoleSpec) -> str:
    labs = []
    for idx in range(1, 26):
        title = f"{spec.role_specific_topics[(idx - 1) % len(spec.role_specific_topics)].replace('-', ' ').title()} causes a production incident"
        labs.append(scenario_block(idx, title, spec, "Lab"))
    return f"# {spec.title} — Troubleshooting\n\n---\n\n{''.join(labs)}"


def render_senior(spec: RoleSpec) -> str:
    scenarios = []
    for idx in range(1, 26):
        title = f"Senior decision around {spec.focus_areas[(idx - 1) % len(spec.focus_areas)]}"
        scenarios.append(scenario_block(idx, title, spec, "Scenario"))
    return f"# {spec.title} — Senior Scenarios\n\n---\n\n{''.join(scenarios)}"


def render_challenges(spec: RoleSpec) -> str:
    challenges = []
    levels = [
        "Level 1 — Fundamentals",
        "Level 2 — Implementation",
        "Level 3 — Production",
        "Level 4 — Troubleshooting",
        "Level 5 — Senior Engineering",
        "Level 6 — Staff / Principal Architecture",
    ]
    for idx in range(1, 26):
        title = f"Improve {spec.role_specific_topics[(idx - 1) % len(spec.role_specific_topics)].replace('-', ' ')} safely"
        challenges.append(challenge_block(idx, title, spec, levels[(idx - 1) % len(levels)]))
    return f"# {spec.title} — Challenges\n\n---\n\n{''.join(challenges)}"


def render_cheatsheet(spec: RoleSpec) -> str:
    topic_lines = "\n".join(f"- {topic}" for topic in spec.role_specific_topics)
    metrics = "\n".join(f"- {focus}" for focus in spec.focus_areas)
    commands = "\n".join(
        [
            "```bash",
            "kubectl get pods -A",
            "kubectl describe pod <pod> -n <ns>",
            "kubectl logs <pod> -n <ns> --tail=100",
            "helm list -A",
            "curl -vk https://service.internal/health",
            "dig api.internal",
            "openssl s_client -connect host:443",
            "nvidia-smi",
            "journalctl -u service -n 100",
            "```",
        ]
    )
    promql = "\n".join(
        [
            "```promql",
            "rate(http_requests_total[5m])",
            "histogram_quantile(0.95, sum(rate(request_latency_bucket[5m])) by (le))",
            "sum(rate(token_output_total[5m])) by (model)",
            "```",
        ]
    )
    return textwrap.dedent(
        f"""\
        # {spec.title} — Cheatsheet

        ## Role-specific focus

        {topic_lines}

        ## High-value metrics and alerts

        {metrics}

        ## Core incident commands

        {commands}

        ## Prometheus / observability shortcuts

        {promql}

        ## Common checks

        - Confirm the intended tenant, region, cluster, and release version first.
        - Confirm identity and policy assumptions before assuming an infrastructure fault.
        - Confirm whether the problem is correctness, latency, cost, saturation, or rollout drift.
        - Compare the current state to the last known good release or configuration.

        ## Useful configuration snippets

        ```yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: {spec.slug}
        spec:
          replicas: 2
        ```

        ```json
        {{
          "role": "{spec.slug}",
          "environment": "production",
          "telemetry": true
        }}
        ```

        ```python
        def health_signal(latency_ms: float, success_rate: float) -> str:
            if success_rate < 0.99:
                return "degraded"
            if latency_ms > 1500:
                return "slow"
            return "healthy"
        ```

        ## Failure signatures

        - A change improves one local metric but worsens the overall request path.
        - Alerts identify a symptom but not the first failed control boundary.
        - A fallback path exists in architecture diagrams but not in runtime reality.
        - Cost and reliability drift silently because telemetry is incomplete.

        ## Runbook reminders

        - Start with evidence collection, not immediate configuration churn.
        - Prefer reversible mitigations before deep surgery.
        - Record the exact release, policy, or traffic change that preceded the incident.
        - Add prevention controls after the incident so the same failure is easier to detect next time.
        """
    )


def render_arch_doc(spec: RoleSpec, stage: str, filename: str) -> str:
    if filename.startswith("01"):
        diagram = textwrap.dedent(
            f"""\
            ```mermaid
            flowchart LR
                U[User / Caller] --> A[{spec.title}]
                A --> C[Core Control]
                C --> D[Dependency]
                D --> O[Output]
            ```
            """
        )
        components = "\n".join(f"- {item}" for item in spec.architecture[:4])
    elif filename.startswith("02"):
        diagram = textwrap.dedent(
            f"""\
            ```mermaid
            flowchart LR
                U[Clients] --> G[Gateway / Policy]
                G --> R[Runtime / Workflow]
                R --> D1[Primary Dependency]
                R --> D2[Secondary Dependency]
                R --> T[Telemetry]
                T --> O[Ops / Alerts]
            ```
            """
        )
        components = "\n".join(f"- {item}" for item in spec.architecture)
    else:
        diagram = textwrap.dedent(
            f"""\
            ```mermaid
            flowchart LR
                U[Users / Teams] --> P[Enterprise Control Plane]
                P --> I[Identity / Policy]
                P --> R[Runtime / Orchestration]
                R --> D1[Model / Tool / Data Path]
                R --> D2[Region / Cluster Failover]
                D1 --> O[Observability / Audit]
                I --> O
            ```
            """
        )
        components = "\n".join(f"- {item}" for item in spec.architecture)
    return textwrap.dedent(
        f"""\
        # {spec.title} — {stage}

        ## Purpose

        This architecture shows how {spec.title.lower()} thinking evolves from a minimal flow into an operable production design.

        ## Components

        {components}

        ## Flow

        {diagram}

        ## Deployment notes

        - Define the first control boundary before scaling the workflow.
        - Attach identity, policy, and telemetry early rather than retrofitting them after the first incident.
        - Keep rollback and ownership visible in the design, not implicit.

        ## Commands / configuration

        ```bash
        kubectl get deploy -A
        kubectl get svc -A
        curl -vk https://service.internal/readyz
        ```

        ```yaml
        kind: Deployment
        metadata:
          name: {spec.slug}-{filename[:2].lower()}
        spec:
          replicas: 2
        ```

        ## Observability

        - Trace every cross-boundary handoff.
        - Publish latency, success, and dependency health metrics.
        - Keep audit context attached to high-risk operations.

        ## Security

        - Enforce least privilege for every actor in the path.
        - Separate tenant and environment boundaries clearly.
        - Store secrets and policy outside mutable application code.

        ## Failure points

        - Dependency drift
        - Missing policy checks
        - Latency buildup across retries or long-running workflows
        - Ambiguous ownership during incidents

        ## Learning outcomes

        By studying this flow, the learner should be able to explain the architecture, the likely failure boundaries, and the trade-offs behind the production shape.
        """
    )


def render_hero(spec: RoleSpec) -> str:
    title = spec.title
    tagline = spec.hero_tagline[:82]
    labels = spec.orbit_labels[:3]
    return textwrap.dedent(
        f"""\
        <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" fill="none">
          <rect width="1200" height="630" rx="32" fill="#08111F"/>
          <rect x="32" y="32" width="1136" height="566" rx="28" fill="url(#bg)"/>
          <circle cx="180" cy="152" r="74" fill="#0EA5E9" fill-opacity="0.18"/>
          <circle cx="1006" cy="502" r="112" fill="#22C55E" fill-opacity="0.12"/>
          <rect x="86" y="98" width="1028" height="434" rx="24" fill="#071827" stroke="#1E293B"/>
          <text x="116" y="178" fill="#E2E8F0" font-size="40" font-family="Arial, Helvetica, sans-serif" font-weight="700">{title}</text>
          <text x="116" y="220" fill="#93C5FD" font-size="20" font-family="Arial, Helvetica, sans-serif">{tagline}</text>
          <rect x="116" y="286" width="250" height="110" rx="18" fill="#0F172A" stroke="#334155"/>
          <rect x="476" y="286" width="250" height="110" rx="18" fill="#0F172A" stroke="#334155"/>
          <rect x="836" y="286" width="250" height="110" rx="18" fill="#0F172A" stroke="#334155"/>
          <text x="144" y="332" fill="#38BDF8" font-size="22" font-family="Arial, Helvetica, sans-serif" font-weight="700">Control</text>
          <text x="144" y="364" fill="#CBD5E1" font-size="18" font-family="Arial, Helvetica, sans-serif">{labels[0] if len(labels) > 0 else "Control plane"}</text>
          <text x="504" y="332" fill="#4ADE80" font-size="22" font-family="Arial, Helvetica, sans-serif" font-weight="700">Operate</text>
          <text x="504" y="364" fill="#CBD5E1" font-size="18" font-family="Arial, Helvetica, sans-serif">{labels[1] if len(labels) > 1 else "Runtime / policy"}</text>
          <text x="864" y="332" fill="#F59E0B" font-size="22" font-family="Arial, Helvetica, sans-serif" font-weight="700">Improve</text>
          <text x="864" y="364" fill="#CBD5E1" font-size="18" font-family="Arial, Helvetica, sans-serif">{labels[2] if len(labels) > 2 else "Telemetry / growth"}</text>
          <path d="M366 342H476" stroke="#475569" stroke-width="3" stroke-linecap="round"/>
          <path d="M726 342H836" stroke="#475569" stroke-width="3" stroke-linecap="round"/>
          <text x="116" y="472" fill="#94A3B8" font-size="16" font-family="Arial, Helvetica, sans-serif">Canonical pack: README · fundamentals · questions · troubleshooting · senior scenarios · challenges · cheatsheet · architecture</text>
          <defs>
            <linearGradient id="bg" x1="32" y1="32" x2="1168" y2="598" gradientUnits="userSpaceOnUse">
              <stop stop-color="#0B1730"/>
              <stop offset="1" stop-color="#10243A"/>
            </linearGradient>
          </defs>
        </svg>
        """
    )


def ensure_role(spec: RoleSpec) -> None:
    role_dir = AI_ROOT / spec.slug
    ensure_dir(role_dir)
    ensure_dir(role_dir / "architecture")
    ensure_dir(role_dir / "assets")
    write_if_missing(role_dir / "README.md", render_readme(spec))
    write_if_missing(role_dir / "fundamentals.md", render_fundamentals(spec))
    write_if_missing(role_dir / "questions.md", render_questions(spec))
    write_if_missing(role_dir / "troubleshooting.md", render_troubleshooting(spec))
    write_if_missing(role_dir / "senior-scenarios.md", render_senior(spec))
    write_if_missing(role_dir / "challenges.md", render_challenges(spec))
    write_if_missing(role_dir / "cheatsheet.md", render_cheatsheet(spec))
    write_if_missing(role_dir / "architecture" / "01-basic-flow.md", render_arch_doc(spec, "Basic Flow", "01-basic-flow.md"))
    write_if_missing(role_dir / "architecture" / "02-production-flow.md", render_arch_doc(spec, "Production Flow", "02-production-flow.md"))
    write_if_missing(role_dir / "architecture" / "03-enterprise-flow.md", render_arch_doc(spec, "Enterprise Flow", "03-enterprise-flow.md"))
    write_if_missing(role_dir / "assets" / "hero.svg", render_hero(spec))


def extend_ai_index() -> None:
    path = AI_ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    header = "## AI Engineering Career Universe"
    if header in text:
        return
    section = textwrap.dedent(
        """\

        ## AI Engineering Career Universe

        ```text
        AI ENGINEERING
        │
        ├── Customer / Solutions
        │   ├── Forward-Deployed AI Engineer
        │   └── AI Solutions Architect
        │
        ├── Agents
        │   ├── Agentic AI Engineer
        │   ├── MCP Engineer
        │   ├── Agent Platform Engineer
        │   └── Context Engineer
        │
        ├── Platform & Infrastructure
        │   ├── AI Platform Engineer
        │   ├── AI Infrastructure Engineer
        │   ├── AI Systems Engineer
        │   └── AI Developer Experience Engineer
        │
        ├── Models & Runtime
        │   ├── LLMOps Engineer
        │   └── Inference Engineer
        │
        ├── Data & Retrieval
        │   └── RAG Engineer
        │
        ├── Reliability & Operations
        │   ├── AI Reliability Engineer
        │   ├── AI Observability Engineer
        │   └── AI FinOps Engineer
        │
        └── Trust
            ├── AI Security Engineer
            ├── AI Evals Engineer
            └── AI Governance Engineer
        ```

        ### Role landing pages

        - [Forward-Deployed AI Engineer](forward-deployed-ai-engineer/README.md)
        - [Agentic AI Engineer](agentic-ai-engineer/README.md)
        - [AI Platform Engineer](ai-platform-engineer/README.md)
        - [AI Infrastructure Engineer](ai-infrastructure-engineer/README.md)
        - [AI Reliability Engineer](ai-reliability-engineer/README.md)
        - [MCP Engineer](mcp-engineer/README.md)
        - [Agent Platform Engineer](agent-platform-engineer/README.md)
        - [LLMOps Engineer](llmops-engineer/README.md)
        - [Inference Engineer](inference-engineer/README.md)
        - [AI Observability Engineer](ai-observability-engineer/README.md)
        - [AI Security Engineer](ai-security-engineer/README.md)
        - [AI Evals Engineer](ai-evals-engineer/README.md)
        - [AI FinOps Engineer](ai-finops-engineer/README.md)
        - [AI Governance Engineer](ai-governance-engineer/README.md)
        - [Context Engineer](context-engineer/README.md)
        - [RAG Engineer](rag-engineer/README.md)
        - [AI Solutions Architect](ai-solutions-architect/README.md)
        - [AI Systems Engineer](ai-systems-engineer/README.md)
        - [AI Developer Experience Engineer](ai-developer-experience-engineer/README.md)
        """
    )
    path.write_text(text.rstrip() + "\n" + section.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    for spec in ROLE_SPECS:
        ensure_role(spec)
    extend_ai_index()


if __name__ == "__main__":
    main()
