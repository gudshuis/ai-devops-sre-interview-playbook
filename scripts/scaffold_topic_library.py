#!/usr/bin/env python3
"""Scaffold a consistent topic library across the repository.

Creates or upgrades topic folders so they follow the canonical shape:

sub-folder/
├── README.md
├── fundamentals.md
├── questions.md
├── troubleshooting.md
├── senior-scenarios.md
├── challenges.md
├── cheatsheet.md
├── architecture/
│   ├── 01-basic-flow.md
│   ├── 02-production-flow.md
│   └── 03-enterprise-flow.md
└── assets/
    └── hero.svg

The content is intentionally structured and specific enough to be useful,
while remaining maintainable as a generated first pass.
"""
from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

QUESTION_PATTERN = re.compile(r"^###\s+(Q|S)\d+\.|^##\s+(Question|Scenario)\s+\d+", re.MULTILINE)
LAB_PATTERN = re.compile(r"^##\s+Lab\s+\d+:|^##\s+Scenario\s+\d+", re.MULTILINE)
CHALLENGE_PATTERN = re.compile(r"^##\s+Challenge\s+\d+", re.MULTILINE)


def title_from_slug(slug: str) -> str:
    return slug.replace("-", " ").replace("/", " / ").title().replace("Ai", "AI").replace("Mcp", "MCP").replace("Llm", "LLM").replace("Cicd", "CI/CD").replace("Sre", "SRE").replace("Rag", "RAG")


TOPICS = [
    {
        "path": "ai-engineering/agents-and-agentic-ai",
        "title": "Agents and Agentic AI",
        "summary": "Designing, governing, and debugging AI agents that plan, call tools, and operate safely in production.",
        "roles": "AI Engineer, AI Platform Engineer, Staff Engineer",
        "tags": ["agent planning", "tool use", "state", "memory", "guardrails", "evaluation"],
        "force": False,
    },
    {
        "path": "ai-engineering/ai-infrastructure",
        "title": "AI Infrastructure",
        "summary": "Running inference, training-adjacent workloads, model gateways, and GPU-aware infrastructure reliably.",
        "roles": "AI Infrastructure Engineer, Platform Engineer, SRE",
        "tags": ["gpu scheduling", "inference serving", "capacity", "latency", "observability", "cost"],
        "force": True,
    },
    {
        "path": "ai-engineering/ai-platform-engineering",
        "title": "AI Platform Engineering",
        "summary": "Building internal platforms that let teams ship models, RAG systems, evals, and agents safely at scale.",
        "roles": "AI Platform Engineer, Platform Engineer, Staff Engineer",
        "tags": ["control plane", "tenant isolation", "platform APIs", "golden paths", "policy", "governance"],
        "force": True,
    },
    {
        "path": "ai-engineering/ai-security",
        "title": "AI Security",
        "summary": "Securing LLM systems, agent workflows, prompts, tools, and model-integrated data paths.",
        "roles": "Security Engineer, AI Engineer, Staff Engineer",
        "tags": ["prompt injection", "authorization", "exfiltration", "least privilege", "supply chain", "auditability"],
        "force": True,
    },
    {
        "path": "ai-engineering/context-engineering",
        "title": "Context Engineering",
        "summary": "Structuring the right context so models receive relevant information with predictable latency and quality.",
        "roles": "AI Engineer, LLM Engineer, Product Engineer",
        "tags": ["context windows", "retrieval", "ranking", "prompt assembly", "compression", "freshness"],
        "force": True,
    },
    {
        "path": "ai-engineering/evals",
        "title": "Evals",
        "summary": "Designing evaluation systems that measure quality, regressions, safety, and operational readiness for AI features.",
        "roles": "AI Engineer, AI Platform Engineer, Engineering Manager",
        "tags": ["offline evals", "online evals", "golden sets", "drift", "review loops", "metrics"],
        "force": True,
    },
    {
        "path": "ai-engineering/foundations",
        "title": "AI Foundations",
        "summary": "Core concepts behind modern AI systems, from tokens and embeddings to inference trade-offs and deployment realities.",
        "roles": "Software Engineer, AI Engineer, Interview Candidate",
        "tags": ["tokens", "embeddings", "transformers", "context", "latency", "cost"],
        "force": True,
    },
    {
        "path": "ai-engineering/llm",
        "title": "LLM Engineering",
        "summary": "Working with large language models in production, including prompting, reliability, latency, and serving patterns.",
        "roles": "LLM Engineer, AI Engineer, Platform Engineer",
        "tags": ["prompting", "latency", "hallucination", "tool calling", "model selection", "fallbacks"],
        "force": True,
    },
    {
        "path": "ai-engineering/llmops-and-mlops",
        "title": "LLMOps and MLOps",
        "summary": "Operational disciplines for shipping models, datasets, experiments, and production AI changes safely.",
        "roles": "ML Engineer, AI Platform Engineer, SRE",
        "tags": ["release process", "artifacts", "deployment", "rollbacks", "lineage", "monitoring"],
        "force": True,
    },
    {
        "path": "ai-engineering/rag",
        "title": "RAG",
        "summary": "Designing retrieval-augmented generation systems with predictable quality, freshness, and governance.",
        "roles": "AI Engineer, Search Engineer, Staff Engineer",
        "tags": ["retrieval", "chunking", "grounding", "reranking", "freshness", "citations"],
        "force": True,
    },
    {
        "path": "ai-engineering/vector-databases",
        "title": "Vector Databases",
        "summary": "Managing embeddings, nearest-neighbor indexes, metadata filters, and retrieval infrastructure at scale.",
        "roles": "AI Engineer, Platform Engineer, Database Engineer",
        "tags": ["indexing", "similarity search", "filters", "recall", "sharding", "rebuilds"],
        "force": True,
    },
    {
        "path": "architecture-challenges",
        "title": "Architecture Challenges",
        "summary": "Open-ended design prompts that force trade-off reasoning across reliability, cost, scale, and organizational complexity.",
        "roles": "Senior Engineer, Staff Engineer, Principal Engineer",
        "tags": ["trade-offs", "bounded context", "scale", "compliance", "cost", "roadmaps"],
        "force": True,
    },
    {
        "path": "cloud",
        "title": "Cloud",
        "summary": "Cross-cloud architecture, governance, networking, identity, and reliability trade-offs.",
        "roles": "Cloud Engineer, Platform Engineer, Staff Engineer",
        "tags": ["identity", "networking", "landing zones", "multi-region", "resilience", "governance"],
        "force": True,
    },
    {
        "path": "cloud/aws",
        "title": "AWS",
        "summary": "AWS architecture, operational patterns, and production trade-offs across compute, networking, storage, and IAM.",
        "roles": "Cloud Engineer, Platform Engineer, SRE",
        "tags": ["iam", "vpc", "eks", "s3", "rds", "observability"],
        "force": True,
    },
    {
        "path": "cloud/azure",
        "title": "Azure",
        "summary": "Azure architecture, operational patterns, and governance choices across networking, identity, and platform services.",
        "roles": "Cloud Engineer, Platform Engineer, SRE",
        "tags": ["entra", "vnet", "aks", "private link", "landing zones", "policy"],
        "force": True,
    },
    {
        "path": "cloud/gcp",
        "title": "GCP",
        "summary": "GCP architecture, networking, workload identity, and platform operations for modern production systems.",
        "roles": "Cloud Engineer, Platform Engineer, SRE",
        "tags": ["gke", "project structure", "vpc", "service accounts", "bigquery", "operations"],
        "force": True,
    },
    {
        "path": "forward-deployed-engineering",
        "title": "Forward Deployed Engineering",
        "summary": "Customer-embedded engineering, ambiguous delivery, high-trust execution, and technical leadership under changing constraints.",
        "roles": "Forward Deployed Engineer, Solutions Architect, Staff Engineer",
        "tags": ["ambiguity", "stakeholders", "delivery", "integration", "trust", "roadmapping"],
        "force": True,
    },
    {
        "path": "foundations/containers",
        "title": "Containers",
        "summary": "Container runtime basics, isolation primitives, images, resource controls, and production debugging.",
        "roles": "Software Engineer, SRE, Platform Engineer",
        "tags": ["namespaces", "cgroups", "images", "runtime", "storage", "networking"],
        "force": True,
    },
    {
        "path": "foundations/databases",
        "title": "Databases",
        "summary": "Core data-system concepts, operational behaviors, and production trade-offs for relational and distributed databases.",
        "roles": "Backend Engineer, Database Engineer, SRE",
        "tags": ["transactions", "indexes", "replication", "consistency", "locking", "backups"],
        "force": True,
    },
    {
        "path": "foundations/distributed-systems",
        "title": "Distributed Systems",
        "summary": "Failure modes, consistency trade-offs, concurrency control, and scaling patterns in distributed architectures.",
        "roles": "Backend Engineer, Staff Engineer, SRE",
        "tags": ["consensus", "consistency", "availability", "queues", "coordination", "failure"],
        "force": True,
    },
    {
        "path": "foundations/git",
        "title": "Git",
        "summary": "Version-control mechanics, collaboration workflows, history rewriting trade-offs, and recovery patterns.",
        "roles": "Software Engineer, DevOps Engineer, Tech Lead",
        "tags": ["commit graph", "rebase", "merge", "recovery", "bisect", "branching"],
        "force": True,
    },
    {
        "path": "foundations/linux",
        "title": "Linux",
        "summary": "Process model, filesystems, networking, memory, and real operational debugging on Linux systems.",
        "roles": "Software Engineer, SRE, Platform Engineer",
        "tags": ["processes", "memory", "filesystems", "network", "permissions", "performance"],
        "force": True,
    },
    {
        "path": "foundations/networking",
        "title": "Networking",
        "summary": "Packets, routing, DNS, TLS, load balancing, and debugging connectivity across distributed systems.",
        "roles": "SRE, Platform Engineer, Backend Engineer",
        "tags": ["dns", "tcp", "tls", "routing", "load balancers", "latency"],
        "force": True,
    },
    {
        "path": "interview-question-bank",
        "title": "Interview Question Bank",
        "summary": "Cross-domain interview prompts that let candidates sample breadth quickly while still practicing reasoned answers.",
        "roles": "Interview Candidate, Hiring Manager, Technical Interviewer",
        "tags": ["breadth", "calibration", "cross-domain", "follow-ups", "trade-offs", "storytelling"],
        "force": True,
    },
    {
        "path": "platform-engineering/devsecops-and-cloud-security",
        "title": "DevSecOps and Cloud Security",
        "summary": "Shifting security into delivery pipelines, platform controls, and cloud runtime enforcement without breaking developer velocity.",
        "roles": "Platform Engineer, Security Engineer, SRE",
        "tags": ["policy", "secrets", "supply chain", "runtime controls", "identity", "compliance"],
        "force": True,
    },
    {
        "path": "platform-engineering/finops",
        "title": "FinOps",
        "summary": "Managing cloud and platform cost with engineering rigor, service ownership, and actionable consumption data.",
        "roles": "Platform Engineer, Engineering Manager, Staff Engineer",
        "tags": ["cost allocation", "waste", "rightsizing", "chargeback", "unit economics", "forecasting"],
        "force": True,
    },
    {
        "path": "platform-engineering/gitops-and-cicd",
        "title": "GitOps and CI/CD",
        "summary": "Delivery systems, promotion models, deployment safety, and change visibility across modern engineering platforms.",
        "roles": "Platform Engineer, DevOps Engineer, SRE",
        "tags": ["pipelines", "promotion", "drift", "rollouts", "artifact provenance", "automation"],
        "force": True,
    },
    {
        "path": "platform-engineering/internal-developer-platforms",
        "title": "Internal Developer Platforms",
        "summary": "Golden paths, self-service infrastructure, platform APIs, and adoption strategies for product engineering teams.",
        "roles": "Platform Engineer, Staff Engineer, Engineering Manager",
        "tags": ["self-service", "portals", "templates", "governance", "product thinking", "adoption"],
        "force": True,
    },
    {
        "path": "platform-engineering/observability",
        "title": "Observability",
        "summary": "Logs, metrics, traces, event correlation, and the operational workflows that make telemetry actionable.",
        "roles": "SRE, Platform Engineer, Backend Engineer",
        "tags": ["signals", "slo", "tracing", "logs", "cardinality", "alerting"],
        "force": True,
    },
    {
        "path": "platform-engineering/sre",
        "title": "Site Reliability Engineering",
        "summary": "Reliability engineering, SLO policy, incident response, automation, and system-level risk management.",
        "roles": "SRE, Staff Engineer, Engineering Manager",
        "tags": ["slo", "toil", "automation", "incident response", "capacity", "risk"],
        "force": True,
    },
    {
        "path": "request-journeys/browser-to-kubernetes",
        "title": "Browser to Kubernetes",
        "summary": "Following a user request from browser click through DNS, CDN, ingress, service mesh, and application response.",
        "roles": "Backend Engineer, SRE, Platform Engineer",
        "tags": ["dns", "cdn", "tls", "ingress", "service routing", "response path"],
        "force": True,
    },
    {
        "path": "request-journeys/commit-to-production",
        "title": "Commit to Production",
        "summary": "Tracing a code change through source control, CI, artifacts, promotion, deployment, and production verification.",
        "roles": "Software Engineer, Platform Engineer, SRE",
        "tags": ["git", "ci", "artifacts", "promotion", "deployments", "verification"],
        "force": True,
    },
    {
        "path": "request-journeys/prompt-to-rag-response",
        "title": "Prompt to RAG Response",
        "summary": "Following an AI query from prompt assembly through retrieval, ranking, generation, and grounded response delivery.",
        "roles": "AI Engineer, Platform Engineer, Product Engineer",
        "tags": ["prompt", "retrieval", "ranking", "generation", "citations", "latency"],
        "force": True,
    },
    {
        "path": "request-journeys/agent-to-mcp-tool",
        "title": "Agent to MCP Tool",
        "summary": "Tracing an agent decision from user intent through tool discovery, authorization, invocation, and result handling.",
        "roles": "AI Engineer, AI Platform Engineer, Security Engineer",
        "tags": ["tool discovery", "authorization", "execution", "streaming", "audit", "fallbacks"],
        "force": True,
    },
    {
        "path": "senior-scenarios",
        "title": "Senior Scenarios",
        "summary": "Cross-cutting senior and staff-level scenarios that require judgment under organizational, operational, and technical constraints.",
        "roles": "Senior Engineer, Staff Engineer, Principal Engineer",
        "tags": ["trade-offs", "leadership", "ambiguity", "risk", "execution", "alignment"],
        "force": True,
    },
    {
        "path": "system-design/backend",
        "title": "Backend System Design",
        "summary": "Designing backend systems for reliability, scale, correctness, and operability under real production constraints.",
        "roles": "Backend Engineer, Staff Engineer, SRE",
        "tags": ["apis", "queues", "data models", "reliability", "consistency", "capacity"],
        "force": True,
    },
    {
        "path": "system-design/case-studies",
        "title": "System Design Case Studies",
        "summary": "Worked design exercises with explicit assumptions, trade-offs, architecture flows, and operational considerations.",
        "roles": "Senior Engineer, Staff Engineer, Interview Candidate",
        "tags": ["case study", "requirements", "trade-offs", "capacity", "security", "operations"],
        "force": True,
    },
    {
        "path": "system-design/frontend",
        "title": "Frontend System Design",
        "summary": "Designing frontend architectures around rendering, performance, state, reliability, and operational visibility.",
        "roles": "Frontend Engineer, Staff Engineer, Product Engineer",
        "tags": ["rendering", "state", "edge delivery", "performance", "resilience", "observability"],
        "force": True,
    },
    {
        "path": "troubleshooting-labs",
        "title": "Troubleshooting Labs",
        "summary": "Hands-on troubleshooting practice designed around symptoms, evidence, narrowing hypotheses, and root-cause analysis.",
        "roles": "SRE, Platform Engineer, Interview Candidate",
        "tags": ["symptoms", "signals", "hypotheses", "evidence", "remediation", "postmortems"],
        "force": True,
    },
    {
        "path": "incidents/kubernetes",
        "title": "Kubernetes Incidents",
        "summary": "Incident write-ups and scenario packs focused on Kubernetes production failures and recovery patterns.",
        "roles": "SRE, Platform Engineer, Incident Commander",
        "tags": ["outages", "ingress", "scheduling", "oom", "control plane", "rollback"],
        "force": True,
    },
    {
        "path": "incidents/networking",
        "title": "Networking Incidents",
        "summary": "Production networking failures across DNS, TLS, routing, load balancing, and packet-level debugging.",
        "roles": "SRE, Network Engineer, Platform Engineer",
        "tags": ["dns", "tls", "routing", "balancers", "packet loss", "timeouts"],
        "force": True,
    },
    {
        "path": "incidents/database",
        "title": "Database Incidents",
        "summary": "Operational database failures involving replication, locks, saturation, storage pressure, and recovery decisions.",
        "roles": "Backend Engineer, Database Engineer, SRE",
        "tags": ["replication", "locking", "corruption", "backups", "storage", "failover"],
        "force": True,
    },
    {
        "path": "incidents/security",
        "title": "Security Incidents",
        "summary": "Security response scenarios spanning access misuse, credential exposure, policy failures, and containment choices.",
        "roles": "Security Engineer, SRE, Staff Engineer",
        "tags": ["containment", "credentials", "forensics", "blast radius", "recovery", "communications"],
        "force": True,
    },
    {
        "path": "incidents/observability",
        "title": "Observability Incidents",
        "summary": "Incidents where telemetry gaps, pipeline failures, or noisy signals block fast diagnosis and safe recovery.",
        "roles": "SRE, Observability Engineer, Platform Engineer",
        "tags": ["dropped traces", "logging outages", "metrics gaps", "alert storms", "sampling", "correlation"],
        "force": True,
    },
    {
        "path": "incidents/ai",
        "title": "AI Incidents",
        "summary": "Production AI failures involving hallucinations, tool misuse, retrieval regressions, and unsafe automation.",
        "roles": "AI Engineer, AI Platform Engineer, SRE",
        "tags": ["hallucination", "tool misuse", "retrieval drift", "latency", "governance", "safety"],
        "force": True,
    },
]


GLOBAL_CHEATSHEETS = [
    ("git-cheatsheet.md", "Git"),
    ("kubernetes-cheatsheet.md", "Kubernetes"),
    ("linux-cheatsheet.md", "Linux"),
    ("docker-cheatsheet.md", "Docker"),
    ("ai-cheatsheet.md", "AI"),
    ("mcp-cheatsheet.md", "MCP"),
    ("llm-cheatsheet.md", "LLM"),
    ("rag-cheatsheet.md", "RAG"),
    ("aws-cheatsheet.md", "AWS"),
    ("azure-cheatsheet.md", "Azure"),
    ("gcp-cheatsheet.md", "GCP"),
]


def count_questions(path: Path, pattern: re.Pattern) -> int:
    if not path.exists():
        return 0
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return 0
    return len(pattern.findall(text))


def should_write(path: Path, kind: str, force: bool) -> bool:
    if not path.exists():
        return True
    if not force:
        return False
    if kind == "qa":
        return count_questions(path, QUESTION_PATTERN) < 25
    if kind == "labs":
        return count_questions(path, LAB_PATTERN) < 25
    if kind == "challenges":
        return count_questions(path, CHALLENGE_PATTERN) < 25
    return True


def topic_links() -> list[tuple[str, str]]:
    return [(t["path"], t["title"]) for t in TOPICS if not t["path"].startswith("incidents/")]


def create_readme(topic: dict) -> str:
    title = topic["title"]
    summary = topic["summary"]
    tags = ", ".join(topic["tags"])
    faq = []
    for i in range(1, 26):
        focus = topic["tags"][(i - 1) % len(topic["tags"])]
        faq.append(
            f"## Question {i}. How should a senior engineer reason about {focus} in {title}?\n\n"
            f"**Answer:** Start with the user-visible outcome, then map the control points, failure modes, and operational trade-offs around {focus}. "
            f"In {title}, a strong answer ties mechanism to production consequences, the metrics that prove health, and the rollback path if the decision is wrong.\n"
        )
    return f"""# {title}

{summary}

## Canonical structure

- [fundamentals.md](fundamentals.md)
- [questions.md](questions.md)
- [troubleshooting.md](troubleshooting.md)
- [senior-scenarios.md](senior-scenarios.md)
- [challenges.md](challenges.md)
- [cheatsheet.md](cheatsheet.md)
- [architecture/](architecture/README.md)

## What this topic covers

This folder focuses on {title.lower()} through the lens of how production systems really behave. The material is organized so a learner can move from mechanism-level understanding into debugging, architecture, and leadership judgment without switching formats or naming conventions.

## Focus areas

`{tags}`

## 25 quick questions and answers

{''.join(faq)}
"""


def create_fundamentals(topic: dict) -> str:
    blocks = []
    title = topic["title"]
    for i in range(1, 26):
        tag = topic["tags"][(i - 1) % len(topic["tags"])]
        blocks.append(
            f"""### Q{i}. What is the core concept behind {tag} in {title}?

**DIFFICULTY:** {"🟢 Beginner" if i <= 8 else "🔵 Intermediate" if i <= 18 else "🟠 Senior"}
**ROLE:** {topic["roles"]}

**WHAT THE INTERVIEWER IS TESTING:** Whether you can explain the mechanism behind {tag} clearly before jumping into tooling or slogans.

**ANSWER:** The core concept behind {tag} in {title} is understanding what boundary is being controlled, what assumptions the system makes, and which inputs determine the outcome. A correct baseline answer names the moving parts and explains the normal happy-path behavior.

**SENIOR-LEVEL ANSWER:** A senior answer goes one layer deeper and explains where {tag} becomes operationally expensive or risky. That means calling out the blast radius of bad defaults, the metrics that reveal drift, the dependency edges that usually surprise teams, and the practical trade-off between simplicity, scale, and governance in a production environment.

**FOLLOW-UP QUESTIONS:**
1. What breaks first if the assumptions behind {tag} stop holding?
2. Which metrics or logs would you inspect to prove your answer in production?
3. When would you intentionally choose a weaker but simpler approach?

**RED FLAGS:** Answering with a tool name or buzzword without explaining the control boundary, the operating assumptions, or the failure mode.

"""
        )
    return f"# {title} - Fundamentals\n\n---\n\n{''.join(blocks)}"


def create_questions(topic: dict) -> str:
    blocks = []
    title = topic["title"]
    for i in range(1, 26):
        tag = topic["tags"][(i - 1) % len(topic["tags"])]
        blocks.append(
            f"""### Q{i}. How would you answer a senior interview question about {tag} in {title}?

**DIFFICULTY:** {"🔵 Intermediate" if i <= 12 else "🟠 Senior" if i <= 22 else "🔴 Staff"}
**ROLE:** {topic["roles"]}

**WHAT THE INTERVIEWER IS TESTING:** Whether you can connect mechanism, trade-offs, and production judgment when discussing {tag}.

**ANSWER:** Start by framing the purpose of {tag}, then describe the main decision points and what a correct implementation or operating model looks like. Keep the answer concrete enough that another engineer could inspect a real system and verify the claims.

**SENIOR-LEVEL ANSWER:** A strong answer adds nuance: how the choice changes under scale, what the observability plan is, which guardrails prevent accidental misuse, and where organizational factors like ownership or compliance reshape the ideal design. In practice, the best answers show how you would protect user impact while still keeping delivery velocity acceptable.

**FOLLOW-UP QUESTIONS:**
1. Which trade-off would you revisit first as traffic or team count grows?
2. What mistake do teams commonly make when they operationalize {tag}?
3. How would you explain this to a cross-functional stakeholder?

**RED FLAGS:** Giving a purely theoretical answer with no mention of measurement, rollback, or production constraints.

"""
        )
    return f"# {title} - Questions\n\n---\n\n{''.join(blocks)}"


def create_troubleshooting(topic: dict) -> str:
    labs = []
    title = topic["title"]
    for i in range(1, 26):
        tag = topic["tags"][(i - 1) % len(topic["tags"])]
        labs.append(
            f"""## Lab {i}: {title} behavior looks healthy on dashboards, but {tag} is causing user pain

**Symptoms:** Latency, errors, or confusing operator signals suggest that {tag} is not behaving the way the team expected.

**What you should check first:** Confirm user impact, identify the narrowest failing boundary, and compare the current state against the most recent known-good deployment or operating change.

**Investigation path:**
1. Validate whether the issue is localized to one dependency, environment, tenant, or workflow.
2. Inspect the most relevant telemetry around {tag}, including saturation, errors, retries, and configuration drift.
3. Reproduce the failure path with the smallest safe test that gives deterministic evidence.

**Likely root causes:** Mis-scoped configuration, stale assumptions about capacity, hidden coupling between systems, or poor visibility into the real control point.

**Senior-level answer:** The goal is not to enumerate random commands but to narrow uncertainty quickly. A senior engineer chooses the fastest evidence-producing path, protects the user-facing system while investigating, and documents which hypotheses were ruled out so the team does not loop.

**Remediation:** Apply the smallest safe fix, verify recovery through live signals, and capture the prevention step that would have made this failure cheaper to detect.

"""
        )
    return f"# {title} - Troubleshooting\n\n---\n\n{''.join(labs)}"


def create_senior_scenarios(topic: dict) -> str:
    scenarios = []
    title = topic["title"]
    for i in range(1, 26):
        tag = topic["tags"][(i - 1) % len(topic["tags"])]
        scenarios.append(
            f"""### S{i}. Your organization depends on {title.lower()} and the next scaling bottleneck is {tag}. What do you do?

**DIFFICULTY:** {"🟠 Senior" if i <= 15 else "🔴 Staff" if i <= 23 else "🟣 Principal"}
**ROLE:** {topic["roles"]}

**SCENARIO:** Multiple teams now rely on the same {tag} boundary, and the original design assumptions no longer hold. Incidents are still rare, but delivery speed is slowing and confidence is dropping.

**GOOD ANSWER:** Start by naming the concrete risk: reliability, cost, governance, organizational ownership, or time-to-recovery. Then define the near-term stabilizing moves, the medium-term architectural reshaping, and the explicit trade-offs you are choosing not to solve immediately.

**SENIOR-LEVEL ANSWER:** The distinguishing move is sequencing. Strong senior engineers avoid a grand rewrite and instead establish a control plane for the problem: ownership, guardrails, migration path, metrics, and a rollback story. They know when to standardize, when to preserve local team flexibility, and how to explain the decision in terms that product, security, and operations leaders can all support.

**FOLLOW-UP QUESTIONS:**
1. What signals would tell you the platform intervention is actually working?
2. What would you deliberately leave decentralized for now?
3. How would you keep delivery moving while the new model is adopted?

**RED FLAGS:** Jumping to a new platform or vendor without describing migration risk, blast radius, or governance.

"""
        )
    return f"# {title} - Senior Scenarios\n\n---\n\n{''.join(scenarios)}"


def create_challenges(topic: dict) -> str:
    blocks = []
    title = topic["title"]
    for i in range(1, 26):
        tag = topic["tags"][(i - 1) % len(topic["tags"])]
        blocks.append(
            f"""## Challenge {i}

**Prompt:** Design or improve a {title.lower()} system where {tag} is the primary source of complexity.

**Constraints:** Assume imperfect ownership boundaries, a non-zero compliance burden, and the need to keep shipping while the system evolves.

**What a strong answer includes:** Clear assumptions, a simple first version, operational guardrails, observability, and a migration plan that does not strand existing consumers.

**Answer:** A practical solution starts with the narrowest architecture that can enforce the critical control point around {tag}. It then layers in automation, policy, and visibility only where the system has already demonstrated pain. This keeps the design grounded in actual risk instead of hypothetical future scale.

**Why this matters:** These challenges test whether you can convert broad technical ambition into a safe sequence of engineering decisions.

"""
        )
    return f"# {title} - Challenges\n\n---\n\n{''.join(blocks)}"


def create_cheatsheet(topic: dict) -> str:
    items = []
    for i, tag in enumerate(topic["tags"], start=1):
        items.append(
            f"## {i}. {tag.title()}\n\n"
            f"- Use this area to anchor fast reviews of {tag}.\n"
            f"- Confirm the control boundary, the owner, the failure signal, and the rollback move.\n"
            f"- In interviews, tie {tag} back to reliability, latency, cost, and governance.\n\n"
        )
    return f"# {topic['title']} Cheatsheet\n\nQuick operating notes for {topic['title'].lower()}.\n\n{''.join(items)}"


def create_architecture_readme(topic: dict) -> str:
    return f"""# {topic['title']} Architecture

Three standard architecture views are maintained for every topic:

- [01-basic-flow.md](01-basic-flow.md) - smallest useful explanation
- [02-production-flow.md](02-production-flow.md) - operational production path
- [03-enterprise-flow.md](03-enterprise-flow.md) - multi-team governed platform view
"""


def create_arch_doc(topic: dict, level: str, title: str) -> str:
    tags = topic["tags"]
    bullets = "\n".join([f"- {tag.title()} is explicitly accounted for in this flow." for tag in tags[:4]])
    return f"""# {title}

## Intent

Show how {topic['title'].lower()} evolves from a simple mechanism into a governed production system.

## Flow summary

{topic['summary']}

## Key design choices

{bullets}

## Failure boundaries

- Identify the first user-visible symptom.
- Define the control point that contains blast radius.
- Add telemetry that proves each handoff is working.

## Senior notes

The value of a {level.lower()} flow is not its diagram density. It is the ability to explain ownership, rollback, and operating assumptions clearly enough that another engineer could critique the design before an outage does it for them.
"""


def create_hero_svg(topic: dict) -> str:
    safe_title = topic["title"].replace("&", "&amp;")
    subtitle = topic["summary"][:84].replace("&", "&amp;")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" fill="none">
  <rect width="1200" height="630" rx="32" fill="#08111F"/>
  <rect x="32" y="32" width="1136" height="566" rx="28" fill="url(#bg)"/>
  <circle cx="180" cy="152" r="74" fill="#0EA5E9" fill-opacity="0.18"/>
  <circle cx="1006" cy="502" r="112" fill="#22C55E" fill-opacity="0.12"/>
  <rect x="86" y="98" width="1028" height="434" rx="24" fill="#071827" stroke="#1E293B"/>
  <text x="116" y="178" fill="#E2E8F0" font-size="44" font-family="Arial, Helvetica, sans-serif" font-weight="700">{safe_title}</text>
  <text x="116" y="220" fill="#93C5FD" font-size="20" font-family="Arial, Helvetica, sans-serif">{subtitle}</text>
  <rect x="116" y="286" width="250" height="110" rx="18" fill="#0F172A" stroke="#334155"/>
  <rect x="476" y="286" width="250" height="110" rx="18" fill="#0F172A" stroke="#334155"/>
  <rect x="836" y="286" width="250" height="110" rx="18" fill="#0F172A" stroke="#334155"/>
  <text x="144" y="332" fill="#38BDF8" font-size="22" font-family="Arial, Helvetica, sans-serif" font-weight="700">Learn</text>
  <text x="144" y="364" fill="#CBD5E1" font-size="18" font-family="Arial, Helvetica, sans-serif">Mechanisms and baseline models</text>
  <text x="504" y="332" fill="#4ADE80" font-size="22" font-family="Arial, Helvetica, sans-serif" font-weight="700">Debug</text>
  <text x="504" y="364" fill="#CBD5E1" font-size="18" font-family="Arial, Helvetica, sans-serif">Signals, failures, recovery paths</text>
  <text x="864" y="332" fill="#F59E0B" font-size="22" font-family="Arial, Helvetica, sans-serif" font-weight="700">Design</text>
  <text x="864" y="364" fill="#CBD5E1" font-size="18" font-family="Arial, Helvetica, sans-serif">Scale, governance, leadership</text>
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


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def scaffold_topic(topic: dict) -> None:
    topic_dir = REPO_ROOT / topic["path"]
    topic_dir.mkdir(parents=True, exist_ok=True)
    force = topic["force"]

    files = [
        (topic_dir / "README.md", create_readme(topic), "always"),
        (topic_dir / "fundamentals.md", create_fundamentals(topic), "qa"),
        (topic_dir / "questions.md", create_questions(topic), "qa"),
        (topic_dir / "troubleshooting.md", create_troubleshooting(topic), "labs"),
        (topic_dir / "senior-scenarios.md", create_senior_scenarios(topic), "qa"),
        (topic_dir / "challenges.md", create_challenges(topic), "challenges"),
        (topic_dir / "cheatsheet.md", create_cheatsheet(topic), "always"),
    ]
    for path, content, kind in files:
        if should_write(path, kind, force):
            write(path, content)

    arch_dir = topic_dir / "architecture"
    arch_docs = [
        (arch_dir / "README.md", create_architecture_readme(topic)),
        (arch_dir / "01-basic-flow.md", create_arch_doc(topic, "Basic", f"{topic['title']} Basic Flow")),
        (arch_dir / "02-production-flow.md", create_arch_doc(topic, "Production", f"{topic['title']} Production Flow")),
        (arch_dir / "03-enterprise-flow.md", create_arch_doc(topic, "Enterprise", f"{topic['title']} Enterprise Flow")),
    ]
    for path, content in arch_docs:
        if not path.exists() or force:
            write(path, content)

    hero = topic_dir / "assets" / "hero.svg"
    if not hero.exists() or force:
        write(hero, create_hero_svg(topic))


def update_collection_readmes() -> None:
    cloud_children = [t for t in TOPICS if t["path"].startswith("cloud/") and t["path"].count("/") == 1]
    cloud_lines = "\n".join([f"- [{t['title']}](./{Path(t['path']).name}/README.md)" for t in cloud_children])
    write(
        REPO_ROOT / "cloud" / "README.md",
        f"""# Cloud

Cross-cloud architecture, governance, identity, networking, and operational trade-offs.

## Subtopics

{cloud_lines}

## Canonical structure

Every leaf topic in this section follows the same topic pack:

```text
sub-folder/
├── README.md
├── fundamentals.md
├── questions.md
├── troubleshooting.md
├── senior-scenarios.md
├── challenges.md
├── cheatsheet.md
├── architecture/
│   ├── 01-basic-flow.md
│   ├── 02-production-flow.md
│   └── 03-enterprise-flow.md
└── assets/
    └── hero.svg
```
""",
    )

    request_children = [t for t in TOPICS if t["path"].startswith("request-journeys/") and t["path"].count("/") == 1]
    request_lines = "\n".join([f"- [{t['title']}](./{Path(t['path']).name}/README.md)" for t in request_children])
    write(
        REPO_ROOT / "request-journeys" / "README.md",
        f"""# Request Journeys

Trace requests end to end, boundary by boundary, using the same canonical topic structure as the rest of the repository.

## Subtopics

{request_lines}
""",
    )

    incident_children = [t for t in TOPICS if t["path"].startswith("incidents/") and t["path"].count("/") == 1]
    incident_lines = "\n".join([f"- [{t['title']}](./{Path(t['path']).name}/README.md)" for t in incident_children])
    write(
        REPO_ROOT / "incidents" / "README.md",
        f"""# Production Incident Library

Structured incident study packs for practicing diagnosis, containment, and post-incident reasoning.

## Subtopics

{incident_lines}
""",
    )

    write(
        REPO_ROOT / "docs" / "repository-structure.md",
        """# Repository Structure

## Naming conventions

- Use lowercase kebab-case for topic folders and subfolders.
- Keep canonical filenames exactly the same in every topic:
  `README.md`, `fundamentals.md`, `questions.md`, `troubleshooting.md`,
  `senior-scenarios.md`, `challenges.md`, `cheatsheet.md`.
- Store architecture flows under `architecture/` with numbered filenames:
  `01-basic-flow.md`, `02-production-flow.md`, `03-enterprise-flow.md`.
- Store the topic hero asset at `assets/hero.svg` inside each leaf topic.

## Canonical tree

```text
sub-folder/
├── README.md
├── fundamentals.md
├── questions.md
├── troubleshooting.md
├── senior-scenarios.md
├── challenges.md
├── cheatsheet.md
├── architecture/
│   ├── 01-basic-flow.md
│   ├── 02-production-flow.md
│   └── 03-enterprise-flow.md
└── assets/
    └── hero.svg
```

## Maintenance idea

Use the canonical pack for every new leaf topic, keep aggregation logic in parent `README.md` files only, and rely on `scripts/scaffold_topic_library.py` plus `scripts/validate-content.py` to prevent structural drift.
""",
    )


def create_global_cheatsheets() -> None:
    cheatsheet_dir = REPO_ROOT / "cheatsheets"
    cheatsheet_dir.mkdir(parents=True, exist_ok=True)
    index_lines = []
    for filename, title in GLOBAL_CHEATSHEETS:
        path = cheatsheet_dir / filename
        sections = []
        for i in range(1, 8):
            sections.append(
                f"## {i}. {title} quick pattern {i}\n\n"
                f"- Use this section to review the most common operational move in {title}.\n"
                f"- Confirm the command, expected signal, and failure interpretation before acting.\n"
                f"- Tie every shortcut back to safety, rollback, and observability.\n\n"
            )
        write(path, f"# {title} Cheatsheet\n\n{''.join(sections)}")
        index_lines.append(f"- [{title}]({filename})")
    write(REPO_ROOT / "cheatsheets" / "README.md", "# Cheatsheets\n\n" + "\n".join(index_lines) + "\n")


def main() -> None:
    for topic in TOPICS:
        scaffold_topic(topic)
    create_global_cheatsheets()
    update_collection_readmes()


if __name__ == "__main__":
    main()
