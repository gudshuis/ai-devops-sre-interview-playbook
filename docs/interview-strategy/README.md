# Interview Strategy

Notes on how to actually use this repository's content under interview
conditions — not more technical content, but process and framing advice.

## How to answer a senior-level question

A useful structure, roughly:

1. **State your assumption.** Senior questions are often deliberately
   underspecified. Say what you're assuming ("I'll assume this is a
   stateless service behind a load balancer") before diving in — it shows
   you noticed the ambiguity instead of guessing silently.
2. **Give the direct answer first**, then the reasoning. Don't make the
   interviewer wait through five minutes of scene-setting before you say
   anything concrete.
3. **Name the trade-off explicitly.** "I'd use X because Y, at the cost of
   Z" reads as senior. "X is the best practice" reads as junior, even if
   the underlying knowledge is the same.
4. **Bring a failure mode unprompted.** If you propose a design, say what
   breaks it. This is usually the single highest-signal thing you can do
   in a system-design round.
5. **Answer the follow-up you're afraid of.** If you know your design has
   a weak point, raise it yourself before the interviewer finds it — it
   reads as far more senior than hoping they don't ask.

## Common red flags to avoid (see also each question's own RED FLAGS section)

- Reciting a definition when asked "how would you..."
- No mention of cost, security, or operational burden in a design answer
- Treating "add more monitoring" as a complete answer to a reliability
  question
- Confident, specific-sounding answers to questions you're actually
  guessing on — interviewers generally prefer "I'd verify X before
  committing to that" over confident fabrication

## Using the troubleshooting labs effectively

The labs in [`troubleshooting-labs/`](../../troubleshooting-labs/README.md)
deliberately give you symptoms and evidence, not the diagnosis. Resist
jumping to the answer section:

1. Write down what you'd check first, and why, before reading further.
2. Narrow using the evidence given — don't ask for information the
   scenario didn't provide, reason from what's there (this mirrors how a
   real interviewer will push back if you ask for infinite information).
3. Only then compare against the documented investigation path.

## Level calibration

If you're not sure whether you're "Senior" or "Staff" for interview
purposes, a rough signal: Senior designs and defends a system within a
known problem space. Staff/Principal additionally reasons about
**organizational and cross-system** trade-offs — when a good technical
solution is still the wrong call because of team topology, migration cost,
or blast radius across systems they don't own. Read a few
`staff-scenarios` items even if you're prepping at Senior — the gap is
usually smaller than it looks.
