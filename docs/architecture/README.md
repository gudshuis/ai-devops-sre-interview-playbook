# Repository Architecture Notes

Why this repository is organized the way it is — useful if you're
navigating unfamiliar territory or contributing new content and unsure
where it belongs.

## Design principle: domain-first, depth-second

Content is grouped by **domain** (Kubernetes, AI engineering, system
design...) rather than by **difficulty** (a single "beginner questions"
folder, a single "senior questions" folder). Within each domain, depth
progresses from fundamentals through staff/principal scenarios.

This is a deliberate choice: someone prepping for a Senior SRE interview
needs *SRE* content across all difficulty levels far more than they need
every domain's beginner content in one place. Grouping by domain keeps a
learning path coherent; grouping by difficulty would scatter it.

## Why AI engineering is one parent folder with subfolders, not 15 flat top-level folders

LLM, RAG, MCP, agents, AI infrastructure, AI security, and related topics
are deeply interconnected — a question about MCP security inevitably
touches agent authorization and tool permissions, for instance. Nesting
them under `ai-engineering/` keeps that relationship visible in the
directory structure itself, and keeps the repository root readable (a
50-entry flat root is harder to navigate than ~12 well-named top-level
domains).

## Why `senior-scenarios/` exists separately from per-domain senior content

Most senior content lives inside its own domain folder (e.g.
`kubernetes/senior-scenarios.md`). The top-level `senior-scenarios/`
folder is specifically for **cross-cutting** scenarios that don't belong
to one domain — e.g. "you operate 120 Kubernetes clusters across three
clouds" touches Kubernetes, cloud architecture, platform engineering, and
FinOps simultaneously. Forcing a cross-cutting scenario into a single
domain folder would misrepresent what it's actually testing.

## Why `interview-question-bank/` exists

A flat, lighter-weight index across every domain — useful if you want to
sample breadth quickly (e.g. "give me one senior question from every
domain") rather than following a full learning path. It links out to
content rather than duplicating it.

## Folder contract

Every content folder has its own `README.md` that states:

- What belongs in this folder (and what doesn't — e.g. why a
  Kubernetes-specific security question lives in `kubernetes/`, not
  `platform-engineering/devsecops-and-cloud-security/`)
- Current content status (full coverage vs. first-pass/starter, per the
  [ROADMAP](../../ROADMAP.md))
- Links to everything in that folder

If you're contributing and unsure where something belongs, check the
target folder's `README.md` "what belongs here" section first.
