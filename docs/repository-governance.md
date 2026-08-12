# Repository Governance

How to configure `main` on GitHub so the upstream repository stays under
single-author control, matching the policy in
[CONTRIBUTING.md](../CONTRIBUTING.md): the maintainer is the only one who
can directly modify it; others may fork and modify their own copy freely.

This uses GitHub's current **Repository Rulesets** feature (Settings →
Rules → Rulesets), which has superseded the older "branch protection
rules" UI as the recommended way to configure this — branch protection
rules still work and are mentioned below as an alternative, but rulesets
are more flexible and are what GitHub now recommends.

## Recommended ruleset for `main`

**Settings → Rules → Rulesets → New branch ruleset**

| Setting | Value | Why |
|---|---|---|
| Ruleset name | `protect-main` | — |
| Enforcement status | `Active` | A ruleset with status "Disabled" or "Evaluate" doesn't actually block anything. |
| Target branches | `main` (or `Default branch`) | Scope this to `main` only — don't accidentally lock yourself out of working branches. |
| Restrict deletions | ✅ On | Prevents `main` from being deleted, even accidentally, even by an owner via API. |
| Restrict force pushes | ✅ On | Prevents history rewriting on `main` — the single highest-value setting here, since a force-push is how history gets silently altered. |
| Require a pull request before merging | Your call — see note below | If you want *even you* to go through a PR for changes (self-review discipline), enable this. Given the explicit goal here is "only I modify it directly," it's reasonable to leave this **off** and push directly as the sole maintainer — the restriction that matters is stopping *others*, not adding friction to yourself. |
| Require status checks to pass | ✅ On, select the CI jobs in `.github/workflows/ci.yml` (markdown-lint, link-check, secret-scan) | Stops a broken/secret-containing state from landing on `main`, including from your own pushes. |
| Restrict who can push | ✅ On — add only your own GitHub username (or leave as "repository admins only" if that already resolves to just you) | This is the actual access-control layer — everything else above is about *what* is allowed, this is about *who*. |
| Bypass list | Leave empty, or explicitly list yourself if "Restrict who can push" would otherwise block you too | Confirm you can still push after configuring this — test with a trivial commit before relying on it. |

## Simpler alternative: classic branch protection rules

If you prefer the older, simpler UI (**Settings → Branches → Add branch
protection rule**, pattern `main`):

- ✅ Require a pull request before merging *(optional, per the note above)*
- ✅ Require status checks to pass before merging → select your CI jobs
- ✅ Do not allow bypassing the above settings *(uncheck if you want to
  self-bypass as maintainer)*
- ✅ Restrict who can push to matching branches → add only yourself
- ✅ Do not allow force pushes
- ✅ Do not allow deletions

Functionally equivalent to the ruleset above for this repository's needs;
rulesets are just the more future-proof choice since GitHub is
consolidating around them.

## What this does *not* protect against

- **Forks**: anyone can fork this public repository and do anything they
  want in their own fork — that's normal, expected, and explicitly fine
  per this project's stated goals (learning forks are encouraged). Branch
  protection on your upstream `main` has zero effect on what happens in
  someone else's fork. See
  [`docs/licensing-options.md`](licensing-options.md) for the distinction
  between repository *permissions* (who can push to your copy) and
  *license* (what people are legally allowed to do with the content,
  including in their own fork).
- **Collaborators you explicitly add**: if you ever add another
  collaborator with write access, the "restrict who can push" list needs
  to be updated to include or exclude them deliberately — it's not
  automatic.
- **GitHub Actions/bots**: if you ever add automation that pushes back to
  the repo (e.g. an auto-formatter bot), that bot's token needs to be
  explicitly considered in the "restrict who can push" / bypass
  configuration, or it will simply fail to push once this is enabled —
  worth testing deliberately if you add such automation later.

## Verifying it worked

After configuring, test with a throwaway branch:
```bash
git checkout -b test-protection
git commit --allow-empty -m "test"
git push origin test-protection
```
Then attempt (from a non-owner account, or by checking the ruleset's own
"insights" tab) to confirm a push directly to `main` from anyone else
would be blocked. Don't test destructive operations (force-push,
deletion) against your real `main` — trust the configuration and the
GitHub documentation for what these settings do, rather than verifying by
actually force-pushing/deleting your real branch.
