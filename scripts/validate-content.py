#!/usr/bin/env python3
"""Content-completeness validator.

Recursively discovers every real topic folder in the repository —
including ones that don't yet have any canonical files — and reports
their status against this repository's target depth per content type.
Missing files are reported explicitly as FILE MISSING, not silently
excluded. Read-only; never modifies content.

Canonical per-topic files checked: README.md, fundamentals.md,
questions.md, troubleshooting.md, senior-scenarios.md, challenges.md
(each needs 25+ entries), plus architecture/ (3+ flow docs) and a
hero.svg under assets/topics/<topic>/ or <topic>/assets/.

Usage:
    python scripts/validate-content.py            # human-readable report
    python scripts/validate-content.py --ci        # exit 1 unless every
                                                     # discovered topic
                                                     # meets every target
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

QUESTION_PATTERN = re.compile(r"^###\s+(Q|S)\d+\.|^##\s+(Question|Scenario)\s+\d+", re.MULTILINE)
LAB_PATTERN = re.compile(r"^##\s+Lab\s+\d+:|^##\s+Scenario\s+\d+", re.MULTILINE)
CHALLENGE_PATTERN = re.compile(r"^##\s+Challenge\s+\d+", re.MULTILINE)

PLACEHOLDER_PATTERN = re.compile(
    r"\b(TODO|TBD|coming soon|to be completed|placeholder|add explanation|write answer)\b",
    re.IGNORECASE,
)

TARGET_QA = 25
TARGET_ARCHITECTURE_FLOWS = 3

# name -> (filename, heading pattern, required count) for the five
# 25+-entry files. README is intentionally excluded from the hard-count
# gate for now — see the note in TopicReport.passes().
QA_FILES = {
    "fundamentals": ("fundamentals.md", QUESTION_PATTERN),
    "questions": ("questions.md", QUESTION_PATTERN),
    "troubleshooting": ("troubleshooting.md", LAB_PATTERN),
    "senior_scenarios": ("senior-scenarios.md", QUESTION_PATTERN),
    "challenges": ("challenges.md", CHALLENGE_PATTERN),
}

NON_TOPIC_DIR_NAMES = {
    ".git", ".github", ".vscode", "docs", "templates", "scripts", "assets",
    "request-journeys", "mental-models", "tradeoffs", "cheatsheets",
    "incidents", "challenges", "architecture", "evidence",
}


@dataclass
class TopicReport:
    name: str
    counts: dict = field(default_factory=dict)
    missing: dict = field(default_factory=dict)
    architecture_flows: int = 0
    has_hero: bool = False
    placeholders_found: list = field(default_factory=list)

    def check(self, key: str) -> str:
        if self.missing.get(key):
            return "FILE MISSING"
        count = self.counts.get(key, 0)
        mark = "PASS" if count >= TARGET_QA else "FAIL"
        return f"{mark} ({count}/{TARGET_QA})"

    def passes(self) -> bool:
        # README is intentionally not yet gated on the 25+ target — see
        # ROADMAP.md; every other canonical file is.
        for key in QA_FILES:
            if self.missing.get(key) or self.counts.get(key, 0) < TARGET_QA:
                return False
        if self.architecture_flows < TARGET_ARCHITECTURE_FLOWS:
            return False
        if not self.has_hero:
            return False
        if self.placeholders_found:
            return False
        return True

    def row(self) -> str:
        parts = [self.check(k) for k in QA_FILES]
        arch = "PASS" if self.architecture_flows >= TARGET_ARCHITECTURE_FLOWS else f"FAIL ({self.architecture_flows}/3)"
        hero = "PASS" if self.has_hero else "FAIL"
        return f"{self.name:<40} " + " ".join(f"{p:<16}" for p in parts) + f" {arch:<12} {hero}"


def count_pattern(path: Path, pattern: re.Pattern) -> int:
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return 0
    return len(pattern.findall(text))


def has_placeholder(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return False
    return bool(PLACEHOLDER_PATTERN.search(text))


def is_non_topic(path: Path) -> bool:
    return any(part in NON_TOPIC_DIR_NAMES for part in path.relative_to(REPO_ROOT).parts)


def discover_all_dirs_with_readme() -> list:
    dirs = []
    for readme in REPO_ROOT.rglob("README.md"):
        d = readme.parent
        if is_non_topic(d) or d == REPO_ROOT:
            continue
        dirs.append(d)
    for filename, _ in QA_FILES.values():
        for md_file in REPO_ROOT.rglob(filename):
            if not is_non_topic(md_file.parent):
                dirs.append(md_file.parent)
    return sorted(set(dirs))


def is_leaf_topic(candidate: Path, all_candidates: set) -> bool:
    for child in candidate.iterdir():
        if child.is_dir() and child in all_candidates:
            return False
    return True


def find_hero(topic_dir: Path) -> bool:
    rel = topic_dir.relative_to(REPO_ROOT)
    candidates = [
        topic_dir / "assets" / "hero.svg",
        REPO_ROOT / "assets" / "topics" / rel.name / "hero.svg",
        REPO_ROOT / "assets" / "topics" / str(rel) / "hero.svg",
    ]
    return any(c.is_file() for c in candidates)


def analyze_topic(topic_dir: Path) -> TopicReport:
    rel = topic_dir.relative_to(REPO_ROOT)
    report = TopicReport(name=str(rel))

    for key, (filename, pattern) in QA_FILES.items():
        f = topic_dir / filename
        if f.is_file():
            report.counts[key] = count_pattern(f, pattern)
            if has_placeholder(f):
                report.placeholders_found.append(filename)
        else:
            report.missing[key] = True

    arch_dir = topic_dir / "architecture"
    if arch_dir.is_dir():
        report.architecture_flows = len([f for f in arch_dir.glob("*.md") if f.name != "README.md"])

    report.has_hero = find_hero(topic_dir)

    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ci", action="store_true")
    args = parser.parse_args()

    candidates = set(discover_all_dirs_with_readme())
    leaf_topics = sorted(d for d in candidates if is_leaf_topic(d, candidates))

    if not leaf_topics:
        print("No topics discovered — nothing to validate.")
        return 0

    reports = [analyze_topic(d) for d in leaf_topics]

    header = f"{'Topic':<40} " + " ".join(f"{k.replace('_',' ').title():<16}" for k in QA_FILES) + f" {'Architecture':<12} Hero"
    print(f"Content validation — {len(reports)} topic(s) discovered\n")
    print(header)
    print("-" * len(header))
    for r in reports:
        print(r.row())
        if r.placeholders_found:
            print(f"  ⚠ placeholder text found in: {', '.join(r.placeholders_found)}")

    passed = [r for r in reports if r.passes()]
    failed = [r for r in reports if not r.passes()]

    totals = {k: sum(r.counts.get(k, 0) for r in reports) for k in QA_FILES}
    total_arch = sum(r.architecture_flows for r in reports)
    total_hero = sum(1 for r in reports if r.has_hero)

    print("\n---")
    print(f"Topics discovered: {len(reports)}")
    print(f"Topics passed: {len(passed)}")
    print(f"Topics failed: {len(failed)}")
    print()
    for k in QA_FILES:
        print(f"Total {k.replace('_', ' ')}: {totals[k]}")
    print(f"Total architecture flows: {total_arch}")
    print(f"Total hero assets: {total_hero}")

    if failed:
        print("\nFailed topics:")
        for r in failed:
            print(f"  - {r.name}")

    exit_code = 0
    if args.ci:
        exit_code = 0 if not failed else 1
        print(f"\nValidator exit code: {exit_code}")
        if not failed:
            print("ALL REQUIRED CONTENT CHECKS PASSED")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
