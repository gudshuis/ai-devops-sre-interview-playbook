# Changelog

All notable changes to this repository are documented here. Format loosely
follows [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased] — V1

### Added

- Initial repository architecture: `foundations/`, `kubernetes/`, `cloud/`,
  `platform-engineering/`, `ai-engineering/`, `system-design/`,
  `forward-deployed-engineering/`, `troubleshooting-labs/`,
  `architecture-challenges/`, `senior-scenarios/`,
  `interview-question-bank/`, `docs/`
- Governance docs: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`,
  `LICENSE`, `ROADMAP.md`
- Tooling: `.gitignore`, `.editorconfig`, `.markdownlint.json`,
  `.vscode/settings.json`, `.vscode/extensions.json`
- CI: markdown lint, internal link check, best-effort secret scan,
  content-completeness validation
- First-pass content across all domain folders, with deep initial coverage
  in Kubernetes, AI engineering (LLM/RAG/MCP/Agentic AI/AI Security), and
  System Design
- Premium root README: animated SVG hero, real (not fabricated) content
  stats, choose-your-path table, "what would you do?" teasers, engineering
  universe diagram, architecture spotlight
- `templates/` — fixed format for fundamentals questions, troubleshooting
  scenarios, senior/staff scenarios, and architecture deep-dives
- `architecture/rag/` — three fully worked flows (basic, enterprise,
  agentic), the demonstrated pattern for future domain architecture docs
- `challenges/debug-this/03-oomkill/` and `challenges/design-this/design-rag-platform/`
  — first worked examples of hands-on challenge formats
- `request-journeys/prompt-to-rag-response.md`,
  `mental-models/follow-the-request.md` + `follow-the-memory.md`,
  `tradeoffs/rag-vs-fine-tuning.md` + `agent-vs-workflow.md`,
  `cheatsheets/kubectl.md` + `linux-debugging.md`,
  `incidents/kubernetes/checkout-503-cascade.md`
- `scripts/validate-content.py` — real, working content-completeness
  validator, wired into CI
- `docs/repository-governance.md` (branch-protection/ruleset guidance),
  `docs/licensing-options.md`
- Contribution policy corrected to reflect single-author curation (no
  external content PRs currently accepted) — see `CONTRIBUTING.md` and
  `.github/ISSUE_TEMPLATE/technical-issue.md`
