# Mental Model: Follow the Memory

## The model

When memory behavior is confusing (OOM despite low reported usage,
gradually degrading performance, unexplained restarts), walk the same
hierarchy every time, outside-in:

```text
Node total memory
  ↓
cgroup (container) memory.max
  ↓
Nested cgroups (if any — see kubernetes/senior-scenarios.md S1)
  ↓
Process RSS (everything: heap + off-heap + stacks + mmap)
  ↓
Application-reported metric (often ONLY heap, or only what it can see)
```

At each level, ask:

```text
What's the limit at this level?
What's actually consumed at this level, right now?
Does the level below fully explain the consumption at this level,
  or is there an unaccounted gap?
```

## The trap this model exists to catch

The most common mistake: comparing an **application-level metric** (JVM
heap, a language runtime's own memory reporting) directly against a
**container-level limit**, and concluding "the limit must be wrong" when
they don't match — worked through in full, with real evidence, in
[`challenges/debug-this/03-oomkill/`](../challenges/debug-this/03-oomkill/README.md).
The gap between "what the app reports" and "what the container limit
constrains" is almost always real memory usage the app-level metric
simply doesn't measure (native/off-heap allocations, thread stacks,
memory-mapped files) — not a bug in the limit itself.

## Where it's used throughout this repository

- [`kubernetes/senior-scenarios.md` S1](../kubernetes/senior-scenarios.md#s1-a-container-has-an-8-gib-kubernetes-memory-limit-inside-it-the-application-spawns-a-child-process-group-with-memorymax6g-in-its-own-cgroup-v2-subtree-walk-through-exactly-what-happens-as-memory-usage-climbs-and-who-gets-oom-killed)
  is this model applied to a nested-cgroup scenario specifically.
- [`kubernetes/troubleshooting.md` Lab 1](../kubernetes/troubleshooting.md#lab-1-pod-is-oomkilled-but-application-level-memory-metrics-never-showed-high-usage)
  and [`challenges/debug-this/03-oomkill/`](../challenges/debug-this/03-oomkill/README.md)
  are both this model applied to real evidence.
