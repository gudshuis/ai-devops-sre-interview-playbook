# Solution: 03 — OOMKilled Despite Low Application-Reported Memory

## Reading the evidence

- `pod.yaml`: container memory **limit is 3500Mi**; `-Xmx3200m` sets the
  **JVM heap max to 3200Mi** — note this is already suspiciously close to
  the container limit, leaving only 300Mi of headroom for everything
  *outside* the heap (native memory, thread stacks, JIT code cache,
  metaspace, direct buffers).
- `memory-events.txt`: `oom_kill 1` confirms the kernel OOM killer fired
  for this cgroup specifically. `high 412` shows the `memory.high` soft
  throttle was hit **412 times** before the hard kill — the container was
  under sustained memory pressure well before the final OOM, not a sudden
  spike.
- `logs.txt`: the JVM's own heap dashboard tops out at **1840Mi at time of
  kill** — only ~57% of the 3200Mi heap max, and only ~53% of the
  container's 3500Mi limit. The heap was nowhere near its own ceiling
  when the container was killed.
- `logs.txt` startup banner: **native crypto provider (JNI)**, a
  **25-channel gRPC connection pool**, and **3 background threads** — all
  of these consume memory *outside* the JVM heap the dashboard measures:
  JNI-loaded native libraries allocate off-heap, each gRPC channel holds
  off-heap buffers, and every thread has its own stack (outside heap,
  sized by JVM default unless explicitly tuned).

## Root cause

The container's memory limit (3500Mi) constrains the **entire process's**
memory footprint — heap, off-heap native allocations (the JNI crypto
provider), direct buffers (the 25-channel gRPC pool), thread stacks (the
background threads plus whatever the gRPC/connection-pool machinery
spins up), metaspace, and JIT code cache. The JVM heap dashboard only
measures the heap portion. With `-Xmx3200m` against a 3500Mi limit, there
was only ~300Mi of budget for everything else — nowhere near enough for a
JNI-heavy, high-connection-count workload like this one, so the
container's *total* memory crossed 3500Mi and triggered the cgroup OOM
kill well before the JVM heap itself ever got close to its own 3200Mi
ceiling.

This is the exact failure pattern discussed generally in
[`kubernetes/troubleshooting.md` Lab 1](../../../kubernetes/troubleshooting.md#lab-1-pod-is-oomkilled-but-application-level-memory-metrics-never-showed-high-usage)
— this challenge is the hands-on version of that lab with concrete
evidence to actually work through.

## Resolution

1. **Widen the gap between `-Xmx` and the container limit** — for a
   JNI/native-heavy workload like this, heap at roughly 55-65% of the
   container limit (rather than the current ~91%) leaves realistic
   headroom for off-heap usage. A reasonable first fix here:
   `-Xmx2000m` against the existing 3500Mi limit (or raise the container
   limit if 2000Mi of heap is genuinely required for this workload's
   throughput).
2. **Add JVM Native Memory Tracking** (`-XX:NativeMemoryTracking=summary`,
   queried via `jcmd <pid> VM.native_memory summary`) to get a real
   breakdown of where off-heap memory is actually going, rather than
   guessing between the crypto provider, gRPC pool, and thread stacks.
3. **Reconsider the 25-channel gRPC pool size** if NMT shows connection
   buffers as the dominant off-heap consumer — connection pools are
   frequently sized generously "to be safe" without being tied to actual
   measured concurrency needs.

## Prevention

Alert on **container-level memory usage** (from the kubelet/cAdvisor
metric, e.g. `container_memory_working_set_bytes`) approaching the limit,
not just the application's self-reported heap metric — this class of
problem is structurally invisible to heap-only monitoring, by definition,
since the gap is entirely in memory the heap metric doesn't measure.
