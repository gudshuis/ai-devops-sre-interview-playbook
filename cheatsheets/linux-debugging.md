# Linux Debugging Cheat Sheet

## "Why was this process killed?"

```bash
dmesg -T | grep -i "out of memory"
```
Use when: a process died unexpectedly with no application-level error —
confirms (or rules out) the kernel OOM killer before you go looking
anywhere else. See [`foundations/linux/README.md`](../foundations/linux/README.md)
Q1 for the full cgroup-aware investigation this feeds into.

```bash
journalctl -u <service> --since "-10 min"
```
Use when: a systemd-managed process needs correlating against what it was
doing right before an incident — narrower and faster than paging through
full journal output.

## "Is this a memory or a CPU problem?"

```bash
cat /sys/fs/cgroup/memory.current /sys/fs/cgroup/memory.max
cat /sys/fs/cgroup/memory.events
```
Use when: you have direct access to the cgroup filesystem and want the
ground truth rather than a higher-level tool's summary — `memory.events`'
`oom_kill` counter specifically tells you if this cgroup has hit its
limit before, not just right now.

```bash
cat /proc/<pid>/status | grep -i vm
```
Use when: you need a single process's memory breakdown (VmRSS, VmSize,
etc.) without going through cgroup files — useful when you're not sure
which cgroup a process even belongs to yet.

## "Is the network actually the problem?"

```bash
ss -tulpn
```
Use when: checking what's actually listening on what port — faster and
more modern than `netstat` for this.

```bash
tcpdump -i <iface> host <ip> and port <port> -w capture.pcap
```
Use when: you need to see the actual packets, not just "it's failing" —
per the TCP/TLS/application-layer isolation approach in
[`foundations/networking/README.md`](../foundations/networking/README.md).
Write to a file (`-w`) rather than watching live output scroll by if
you'll need to actually analyze it afterward.

## "What does this process actually have open/mapped?"

```bash
nsenter -t <pid> -n ss -tulpn
```
Use when: debugging networking *inside* a container's network namespace
from the host, without needing a shell inside the container itself —
useful when the container image doesn't even have basic networking tools
installed.

```bash
lsof -p <pid>
```
Use when: suspecting a file-descriptor leak, or needing to know exactly
what files/sockets a process currently holds open.
