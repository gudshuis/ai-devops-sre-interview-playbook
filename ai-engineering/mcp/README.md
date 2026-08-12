# Model Context Protocol (MCP)

**Status: deep first-pass content** (priority section for V1).

## What belongs here

MCP architecture, client/server design, transports, and MCP-specific
security. General agent design (how an agent decides *when* to call a
tool) lives in
[`ai-engineering/agents-and-agentic-ai/`](../agents-and-agentic-ai/README.md)
— this folder is about the protocol layer connecting models to tools and
context, not agent reasoning itself.

## Contents

- [fundamentals.md](fundamentals.md) — architecture, clients/servers,
  tools/resources/prompts, transports, authn/authz basics
- [senior-scenarios.md](senior-scenarios.md) — enterprise MCP gateway
  design, tool discovery/authorization at scale
- [security.md](security.md) — tool poisoning, prompt injection via tool
  results, credential leakage, malicious/untrusted servers, sandboxing
