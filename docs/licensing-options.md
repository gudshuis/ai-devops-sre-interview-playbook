# Licensing Options

This repository currently uses the **MIT License** (see [`LICENSE`](../LICENSE)).
This document explains what that means, what alternatives exist, and —
importantly — what a license does and doesn't control, since that's
commonly misunderstood.

## Two separate things: repository permissions vs. license

These are frequently conflated and they control completely different
things:

- **Repository permissions** (who can push to *your* GitHub repository) —
  covered in [`docs/repository-governance.md`](repository-governance.md).
  This controls write access to your specific copy of the repo.
- **License** (what anyone is legally permitted to do with the content,
  by anyone, anywhere, forever, once it's public) — covered in this
  document.

**Locking down your GitHub repository's push permissions does nothing to
restrict what someone does with content they've already cloned or
forked.** Once code/content is public under a permissive license, a fork
is that person's own copy to do with as the license allows — you cannot
use repository settings to control behavior inside someone else's fork.
If you want to prevent certain uses of the content itself (not just
prevent people from pushing to your specific repo), that has to be a
license decision, not a GitHub-settings decision.

## Your stated goals

You want people to be able to: read, learn from, clone, and fork the
content — while you retain copyright and control over the **upstream**
repository. That's a coherent, common goal, and several license choices
support it reasonably well, with different trade-offs.

## Option 1: MIT License (current choice)

**What it allows:** essentially anything — use, copy, modify,
merge, publish, distribute, sublicense, even sell — with the only
requirement being that the original copyright notice and license text
are preserved.

**Trade-off:** maximally permissive, which is exactly right for "I want
this to spread and be useful" but means someone *could* legally take your
content, rebrand it, and redistribute it without attribution beyond the
technical requirement of keeping the license file — the practical
protection against that isn't legal, it's that a rebranded copy of a
public GitHub repository with visible history is easy to point out as
derivative, and MIT doesn't prevent you from saying so publicly, just
prevents you from suing over it as a copyright violation as long as they
kept the license notice.

## Option 2: Creative Commons (CC BY 4.0 or CC BY-SA 4.0)

More natural fit for **prose/documentation content** specifically (as
opposed to MIT, which is primarily a *software* license and is a slightly
unusual choice for a repository that's mostly markdown documentation, even
though it's extremely common in practice for exactly this kind of
repository).

- **CC BY 4.0**: anyone can share/adapt, with attribution required. Similar
  spirit to MIT but written for creative/educational content rather than
  software.
- **CC BY-SA 4.0** ("ShareAlike"): same as above, but derivative works
  must be licensed under the same terms — this is the option that comes
  closest to "people can learn from and build on this, but can't take it
  proprietary/closed" if that matters to you.

**Trade-off:** less familiar to a software-engineering audience than MIT
(who may expect a standard OSI software license on a GitHub repo), and CC
licenses are generally not recommended for repositories that also contain
actual runnable code (the Terraform/YAML/shell examples throughout this
content) — there's some genuine ambiguity in the OSS community about
applying CC to code specifically, which is part of why MIT (a real
software license, applied loosely to documentation too) is the more
common practical choice for repos like this one, despite the slight
mismatch.

## Option 3: Dual-license (MIT for code snippets, CC BY 4.0 for prose)

Technically the most "correct" option, rarely worth the complexity for a
repository this size — most similar repositories just pick one license
for the whole repo (usually MIT) rather than splitting by content type.
Only worth considering if licensing precision becomes a real concern later
(e.g. someone specifically asks about reusing just the code examples under
different terms).

## Recommendation

**Stay with MIT** (already in place) unless you specifically want the
ShareAlike "derivatives must stay open" property — it's the most familiar
choice to your target audience (software engineers), avoids the
code-vs-prose licensing ambiguity of CC licenses, and already satisfies
your stated goal (people can read/learn/clone/fork; you retain copyright
via the notice requirement). Revisit only if you find people are taking
the content in a direction (e.g. closed, rebranded, monetized SaaS
products with no attribution) that specifically bothers you enough to want
CC BY-SA's stronger "stay open" requirement — that's a real trade-off
decision, not a default one.
