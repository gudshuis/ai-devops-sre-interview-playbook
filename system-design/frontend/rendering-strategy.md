# Frontend Rendering Strategy

---

### Q1. You're designing an AI chat interface (think: a ChatGPT-style enterprise assistant). What rendering strategy would you choose, and why?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Frontend Engineer, Full-Stack Engineer

**WHAT THE INTERVIEWER IS TESTING:** Whether you pick a rendering
strategy based on the actual characteristics of the content (highly
dynamic, per-user, streaming) rather than defaulting to whatever's
currently fashionable.

**SENIOR-LEVEL ANSWER:** A chat interface's content is **inherently
per-user, real-time, and streaming** — none of the caching benefits that
make SSG (or ISR) valuable apply here, since there's no shared content to
pre-render across users. **CSR with server-sent streaming for the
response itself** (not full-page SSR per message) is the right shape: the
application shell (nav, layout, auth state) can be server-rendered once
for fast initial load and good perceived performance, but individual
chat turns are client-rendered and updated incrementally as tokens stream
in from the backend — full SSR per-message would mean waiting for the
*entire* model response before rendering anything, directly working
against the "watch it type" UX that's the actual point of a streaming
chat interface. The trade-off: pure CSR has a real cost — a blank/loading
initial shell until JS hydrates — which is why the shell itself still
benefits from SSR even though the chat content doesn't.

**FOLLOW-UP QUESTIONS:**
- How would you handle a network interruption mid-stream — what's the
  actual UX and technical recovery path?
- Would your answer change for a customer-facing marketing site versus
  this internal tool? Why?
- How does this interact with time-to-first-token as a UX metric, versus
  traditional page-load metrics like LCP?

**RED FLAGS:** Reflexively answering "SSR because it's better for SEO"
for an authenticated, per-user chat interface — SEO is irrelevant here,
and the answer shows the candidate is pattern-matching a memorized
"SSR is generally better" answer rather than reasoning about this
specific content's characteristics.

---

### Q2. What's Incremental Static Regeneration (ISR) actually solving, and what's its failure mode under real traffic?

**DIFFICULTY:** 🟠 Senior
**ROLE:** Frontend Engineer

**ANSWER:** ISR serves a statically-generated page (fast, cacheable) but
allows it to be regenerated in the background after a defined staleness
window, rather than requiring a full rebuild/redeploy for content updates
— a middle ground between SSG's "rebuild everything to update anything"
and SSR's "regenerate on every single request."

**SENIOR-LEVEL ANSWER:** The failure mode worth knowing: the **first
request after the staleness window expires** typically still serves the
stale page while regeneration happens in the background (a "stale-while-
revalidate" pattern) — which is usually the right trade-off, but means
ISR does **not** guarantee freshness at any specific point in time, only
eventual freshness after the next qualifying request. For content where
staleness has real consequences (pricing, inventory availability), that
gap needs to be explicitly evaluated against the business requirement,
not assumed away because "ISR handles updates."

**FOLLOW-UP QUESTIONS:**
- How would you force immediate regeneration for a specific page after a
  known content change (e.g. an editor publishing an urgent correction)?
- What's the cache-invalidation story across a CDN sitting in front of an
  ISR-enabled origin?

**RED FLAGS:** Describing ISR as "always up to date" — it explicitly
isn't, by design.
