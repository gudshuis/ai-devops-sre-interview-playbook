# Troubleshooting Scenario Template

Copy this block per scenario into the relevant domain's
`troubleshooting.md`. See
[`kubernetes/troubleshooting.md`](../kubernetes/troubleshooting.md) for
five fully worked real examples using this exact shape.

---

## Lab 1: [Symptom, phrased the way a user/on-call engineer would actually report it]

**Symptoms:** [What's observed, in plain terms — the initial report, not
the diagnosis.]

**Available evidence:** [Whatever's already known/observable — command
output, dashboard state, log lines. This is what the reader has to work
with; don't include the answer here.]

**Investigation steps:**

1. [First thing to check, and *why that's the right first check* — not
   just a command, but the reasoning for checking it before anything
   else.]
2. [Next step, informed by what step 1 would show.]
3. [Continue until the evidence points at a specific cause.]

**Likely root cause:** [State it plainly, and connect it back to the
specific evidence that confirms it — not just an assertion.]

**Resolution:** [The actual fix.]

**Prevention:** [What would catch this earlier next time — an alert, a
policy, a design change. This is often the highest-value part of the
whole entry; don't skip it.]
