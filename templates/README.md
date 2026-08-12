# Templates

The exact format every content type in this repository follows. Use these
when adding new content so depth and structure stay consistent across
domains.

- [fundamentals-template.md](fundamentals-template.md) — a single
  fundamentals question
- [troubleshooting-template.md](troubleshooting-template.md) — a single
  production troubleshooting scenario
- [senior-scenario-template.md](senior-scenario-template.md) — a single
  senior/staff/principal design scenario
- [architecture-template.md](architecture-template.md) — a full
  architecture deep-dive document

## Why a fixed template

A fixed structure is what makes the difficulty/role/reasoning consistent
enough to actually be useful under interview pressure — see
`docs/interview-strategy/README.md` for how these fields map to how you'd
actually answer in an interview. It also makes
[`scripts/validate-content.py`](../scripts/validate-content.py) able to
count real content reliably (it looks for these exact heading patterns).

## Heading convention (important for the validator)

- Fundamentals/senior-scenario questions use `### Q<n>.` or `### S<n>.`
  at the start of the line.
- Troubleshooting scenarios use `## Lab <n>:` (see
  [`kubernetes/troubleshooting.md`](../kubernetes/troubleshooting.md) for
  the established pattern) — kept as `##` rather than `###` since each lab
  is a larger, self-contained unit than a single Q&A.

Keep new content consistent with whichever pattern already exists in that
folder rather than introducing a third variant.
