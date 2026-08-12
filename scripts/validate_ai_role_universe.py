#!/usr/bin/env python3
"""Validate role-based AI engineering folders."""
from __future__ import annotations

from pathlib import Path
import re

REPO_ROOT = Path(__file__).resolve().parent.parent
AI_ROOT = REPO_ROOT / "ai-engineering"

ROLES = [
    "forward-deployed-ai-engineer",
    "agentic-ai-engineer",
    "ai-platform-engineer",
    "ai-infrastructure-engineer",
    "ai-reliability-engineer",
    "mcp-engineer",
    "agent-platform-engineer",
    "llmops-engineer",
    "inference-engineer",
    "ai-observability-engineer",
    "ai-security-engineer",
    "ai-evals-engineer",
    "ai-finops-engineer",
    "ai-governance-engineer",
    "context-engineer",
    "rag-engineer",
    "ai-solutions-architect",
    "ai-systems-engineer",
    "ai-developer-experience-engineer",
]

STRUCTURE = [
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

Q_RE = re.compile(r"^\s*###\s+Q\d+\.", re.MULTILINE)
LAB_RE = re.compile(r"^\s*##\s+Lab\s+\d+:", re.MULTILINE)
SCENARIO_RE = re.compile(r"^\s*##\s+Scenario\s+\d+:", re.MULTILINE)
CHALLENGE_RE = re.compile(r"^\s*##\s+Challenge\s+\d+:", re.MULTILINE)


def count(path: Path, pattern: re.Pattern[str]) -> int:
    return len(pattern.findall(path.read_text(encoding="utf-8")))


def main() -> None:
    header = (
        "ROLE                                README  FUND  QUES  TROUBLE  SENIOR  CHALLENGE  ARCH  SVG  STATUS"
    )
    print(header)
    print("-" * len(header))
    failures: list[str] = []
    for slug in ROLES:
        role_dir = AI_ROOT / slug
        missing = [item for item in STRUCTURE if not (role_dir / item).exists()]
        readme = count(role_dir / "README.md", Q_RE) if (role_dir / "README.md").exists() else 0
        fund = count(role_dir / "fundamentals.md", Q_RE) if (role_dir / "fundamentals.md").exists() else 0
        ques = count(role_dir / "questions.md", Q_RE) if (role_dir / "questions.md").exists() else 0
        trouble = count(role_dir / "troubleshooting.md", LAB_RE) if (role_dir / "troubleshooting.md").exists() else 0
        senior = count(role_dir / "senior-scenarios.md", SCENARIO_RE) if (role_dir / "senior-scenarios.md").exists() else 0
        challenge = count(role_dir / "challenges.md", CHALLENGE_RE) if (role_dir / "challenges.md").exists() else 0
        arch = sum(1 for item in ["architecture/01-basic-flow.md", "architecture/02-production-flow.md", "architecture/03-enterprise-flow.md"] if (role_dir / item).exists())
        svg = "PASS" if (role_dir / "assets/hero.svg").exists() and "<svg" in (role_dir / "assets/hero.svg").read_text(encoding="utf-8") else "FAIL"
        status = "PASS"
        if missing or readme < 25 or fund < 25 or ques < 25 or trouble < 25 or senior < 25 or challenge < 25 or arch < 3 or svg != "PASS":
            status = "FAIL"
            detail = f"{slug}: missing={missing}, counts=(README={readme}, FUND={fund}, QUES={ques}, TROUBLE={trouble}, SENIOR={senior}, CHALLENGE={challenge}, ARCH={arch}, SVG={svg})"
            failures.append(detail)
        print(f"{slug:<35} {readme:>6} {fund:>5} {ques:>5} {trouble:>8} {senior:>7} {challenge:>10} {arch:>5} {svg:>4}  {status}")
    if failures:
        print("\nFAILED VALIDATIONS")
        for failure in failures:
            print(f"- {failure}")


if __name__ == "__main__":
    main()
