# Agents & Agentic AI

**Status: deep first-pass content** (priority section for V1).

## What belongs here

Agent design principles — planning, tool use, memory, multi-agent
orchestration, and production concerns (reliability, cost, rollback,
blast radius). Framework specifics (LangGraph, CrewAI, etc.) are mentioned
where genuinely relevant but this folder focuses on principles that
outlive any specific framework. MCP's protocol-level tool/context
mechanics live in [`ai-engineering/mcp/`](../mcp/README.md); this folder
is about the agent's reasoning loop that decides to *use* those tools.

## Contents

- [fundamentals.md](fundamentals.md) — agent loops, planning, memory,
  agents vs. deterministic workflows
- [senior-scenarios.md](senior-scenarios.md) — multi-agent orchestration,
  production reliability, agent identity and blast radius
