# Backend System Design — Principles

---

### Q1. When would you choose synchronous request/response between two services versus an asynchronous message queue?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Backend Engineer, Solutions Architect

**SENIOR-LEVEL ANSWER:** The determining question isn't "which is
faster" (async isn't inherently faster — it trades immediate response for
decoupling) — it's **does the caller need to know the outcome before
proceeding, and can the operation tolerate delayed processing.**
Synchronous makes sense when the caller's next action genuinely depends on
the result (a payment authorization the checkout flow can't proceed
without). Async makes sense when the caller just needs to know the
request was *accepted* (an email-send, a report generation) and the
actual processing can happen on its own timeline, with the queue also
providing natural backpressure and retry semantics the synchronous
alternative doesn't get for free. The trade-off to name: async introduces
**eventual completion** as a state your system now has to represent and
handle (was this processed yet? did it fail? how does the caller find
out?) — real added complexity, not a free upgrade.

**FOLLOW-UP QUESTIONS:**
- How would you let a caller know an async operation eventually failed,
  if they've already moved on?
- What's the risk of using a queue for something that actually needed
  synchronous consistency?

**RED FLAGS:** "Async is always more scalable, so use it everywhere" —
ignores the real complexity cost and cases where synchronous is correct.

---

### Q2. Explain idempotency keys and why they matter for retry-safe APIs.

**DIFFICULTY:** 🔵 Intermediate
**ROLE:** Backend Engineer

**ANSWER:** An idempotency key is a client-generated unique identifier
sent with a request (typically for a side-effecting operation like
"charge this payment") that the server uses to detect and safely ignore
duplicate submissions — if the same key arrives twice, the server returns
the original result instead of performing the operation again.

**SENIOR-LEVEL ANSWER:** This matters because **network failures are
ambiguous by nature** — if a client sends a request and the connection
drops before it gets a response, it genuinely cannot tell whether the
server received and processed it or not. Without idempotency keys, the
"safe" retry behavior is actually unsafe for non-idempotent operations
(retrying a payment charge could double-charge). The server-side
implementation detail that actually matters: the idempotency key + result
needs to be stored **atomically with the operation's own effect** (same
transaction, or an equivalent guarantee) — storing the key separately
after the fact reintroduces the exact race condition the mechanism exists
to prevent.

**FOLLOW-UP QUESTIONS:**
- How long should an idempotency key remain valid/stored?
- What happens if two requests with the same idempotency key but
  genuinely different payloads arrive — how should the server handle that?

**RED FLAGS:** Describing idempotency keys as just deduplication without
explaining *why* retries are unsafe in the first place (the fundamental
network-ambiguity reasoning).
