# Debug This: 03 — OOMKilled Despite Low Application-Reported Memory

**Difficulty:** 🟠 Senior

## Situation

A Java payments-processing service, `payments-worker`, is restarting
every 15-40 minutes with `OOMKilled`. The team's own JVM heap dashboard
never shows heap usage above ~55% of the container's memory limit before
each restart.

Investigate using the evidence below. Form your own hypothesis before
opening `solution.md`.

## Evidence

- [`evidence/pod.yaml`](evidence/pod.yaml)
- [`evidence/kubectl-describe.txt`](evidence/kubectl-describe.txt)
- [`evidence/memory-events.txt`](evidence/memory-events.txt)
- [`evidence/logs.txt`](evidence/logs.txt)

## Questions to answer before opening the solution

1. Where does the container's actual memory limit come from, and what
   does it constrain — everything the JVM reports, or something broader?
2. What in the evidence points at *where* the "missing" memory (limit
   minus reported heap usage) is actually going?
3. What would you check next that isn't already provided here?
