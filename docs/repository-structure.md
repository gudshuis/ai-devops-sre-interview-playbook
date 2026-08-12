# Repository Structure

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
