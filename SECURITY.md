# Security Policy

This is an educational content repository — it does not ship running
software, so there's no traditional "vulnerability" in the usual sense.
This policy instead covers the two things that actually matter here.

## 1. No real secrets, ever

Nothing in this repository should ever contain:

- Real API keys, tokens, or credentials of any kind
- Real private keys or certificates
- Real cloud account IDs, internal hostnames, or internal IP ranges
- Real employer names or proprietary/confidential architecture details
- Any information covered by an NDA

Every command, YAML manifest, Terraform snippet, or shell example must use
obviously fake placeholder values (`<REDACTED>`, `example.internal`,
`sk-example-...`, RFC 5737/RFC 1918 example ranges, etc.).

**If you find a real secret or confidential detail committed anywhere in
this repository** (including in git history, not just the current tree),
please report it privately rather than opening a public issue — open a
private security advisory on the repository, or contact a maintainer
directly. Do not post the discovered secret itself in any public channel.

## 2. Technical accuracy in security-related content

The `platform-engineering/devsecops-and-cloud-security/` and
`ai-engineering/ai-security/` sections cover real security concepts
(threat modeling, zero trust, prompt injection, supply-chain security,
etc.). If you find content that is factually wrong in a way that could lead
someone to a genuinely unsafe production decision (e.g. an incorrect claim
about what a control actually protects against), please open an issue or
PR — this is treated as a priority correction, not routine content
maintenance.

## Automated scanning

CI includes a best-effort secret-scanning check on every PR (see
`.github/workflows/`). It is a safety net, not a substitute for the
guidance above — automated scanners miss things; review your own
contributions before submitting.
