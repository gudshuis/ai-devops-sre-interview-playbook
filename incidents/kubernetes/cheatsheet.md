# Kubernetes Cheatsheet

## 1. Quick Mental Model

Kubernetes should help you answer two questions quickly: where the control boundary is, and what evidence proves the runtime state matches the intended state.

```text
┌──────────────────┐
│      Client      │
└────────┬─────────┘
         ↓
┌──────────────────┐
│   DNS / Edge     │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Ingress / LB     │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Service / Policy │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Pod / Container  │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Dependency Layer │
└──────────────────┘
```

## 2. Most Useful Commands

### Command

```bash
kubectl config get-contexts
```

**Purpose:**  
List kube contexts

**When to use:**  
Verify the cluster before acting

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Wrong cluster is the first incident risk

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl config get-contexts` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl config use-context prod
```

**Purpose:**  
Switch kube context

**When to use:**  
Move to the intended cluster

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Confirm after switch

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl config use-context prod` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl get ns
```

**Purpose:**  
List namespaces

**When to use:**  
Understand tenant layout

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Missing or terminating namespaces

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl get ns` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl get pods -A -o wide
```

**Purpose:**  
List pods with node placement

**When to use:**  
Check workload spread and failures

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
CrashLoop, Pending, skew

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl get pods -A -o wide` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl describe pod api-123 -n prod
```

**Purpose:**  
Detailed pod state

**When to use:**  
Explain scheduling or runtime failures

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Events, probes, image pull errors

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl describe pod POD` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl logs api-123 -n prod --previous
```

**Purpose:**  
Read previous container logs

**When to use:**  
Catch crash loops

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Startup exceptions

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl logs POD --previous` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl exec -it api-123 -n prod -- sh
```

**Purpose:**  
Enter a running container

**When to use:**  
Debug live container state

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
DNS, env vars, mounted files

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl exec -it POD -- sh` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl top pod -A
```

**Purpose:**  
Pod resource usage

**When to use:**  
Check CPU/memory pressure

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Hot pods or memory leaks

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl top pod -A` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl top node
```

**Purpose:**  
Node resource usage

**When to use:**  
Detect node saturation

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
High pressure or imbalance

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl top node` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl get deploy,sts,ds -A
```

**Purpose:**  
Workload summary

**When to use:**  
See rollout and controller health

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Unavailable replicas

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl get deploy,sts,ds -A` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl rollout status deploy/api -n prod
```

**Purpose:**  
Watch rollout progress

**When to use:**  
Validate deployments safely

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Stuck or degraded rollout

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl rollout status deploy/name` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl rollout undo deploy/api -n prod
```

**Purpose:**  
Rollback a deployment

**When to use:**  
Restore last known good state

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Fast mitigation

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl rollout undo deploy/name` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl get svc -A
```

**Purpose:**  
List services

**When to use:**  
Inspect exposure model

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Wrong ports or ClusterIP state

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl get svc -A` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl get endpoints,endpointslices -A
```

**Purpose:**  
Backend endpoint mapping

**When to use:**  
Debug service to pod wiring

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Empty endpoints cause 503s

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl get endpoints,endpointslices -A` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl get ingress -A
```

**Purpose:**  
List ingresses

**When to use:**  
Check external routing

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Address assignment and host rules

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl get ingress -A` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl describe ingress app -n prod
```

**Purpose:**  
Ingress detail

**When to use:**  
Investigate 4xx/5xx at the edge

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Annotation mismatches, backend refs

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl describe ingress NAME` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl get events -A --sort-by=.lastTimestamp
```

**Purpose:**  
Recent cluster events

**When to use:**  
Timeline investigation

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Scheduling, pull, or volume failures

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl get events -A --sort-by=.lastTimestamp` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl get nodes -o wide
```

**Purpose:**  
Node inventory

**When to use:**  
Check node readiness and versions

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
NotReady nodes, version skew

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl get nodes -o wide` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl describe node ip-10-0-0-1
```

**Purpose:**  
Detailed node state

**When to use:**  
Debug taints, pressure, kubelet issues

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Conditions and allocatable resources

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl describe node NODE` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl cordon node-1
```

**Purpose:**  
Mark node unschedulable

**When to use:**  
Contain failures

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Protect cluster during remediation

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl cordon NODE` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl drain node-1 --ignore-daemonsets
```

**Purpose:**  
Evict workloads safely

**When to use:**  
Maintenance or bad node handling

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Pod disruption blockers

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl drain NODE --ignore-daemonsets` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl uncordon node-1
```

**Purpose:**  
Return node to service

**When to use:**  
Post-maintenance recovery

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Capacity restored

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl uncordon NODE` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl get pvc,pv -A
```

**Purpose:**  
Storage attachment view

**When to use:**  
Debug pending or stuck volumes

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Unbound claims

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl get pvc,pv -A` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl describe pvc data -n prod
```

**Purpose:**  
Detailed claim state

**When to use:**  
Explain storage provisioning failures

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
StorageClass, events

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl describe pvc NAME` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl get netpol -A
```

**Purpose:**  
List network policies

**When to use:**  
Check traffic restrictions

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Unexpected deny boundaries

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl get netpol -A` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl auth can-i get secrets -n prod
```

**Purpose:**  
Check RBAC authorization

**When to use:**  
Debug access issues

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Whether RBAC is the blocker

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl auth can-i ACTION RESOURCE` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
helm list -A
```

**Purpose:**  
List Helm releases

**When to use:**  
Map workloads to release ownership

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Failed or pending upgrades

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `helm list -A` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
helm get values ingress-nginx -n ingress
```

**Purpose:**  
Inspect deployed values

**When to use:**  
Debug chart config drift

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Wrong configuration inputs

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `helm get values RELEASE -n NS` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl diff -f deploy.yaml
```

**Purpose:**  
Preview manifest changes

**When to use:**  
Safer deploy review

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Risk before apply

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl diff -f file.yaml` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl apply -f deploy.yaml
```

**Purpose:**  
Apply manifests

**When to use:**  
Deploy or patch resources

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Created vs configured output

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl apply -f file.yaml` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl delete pod api-123 -n prod
```

**Purpose:**  
Force pod recreation

**When to use:**  
Recover from stuck state when safe

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Controller should recreate it

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl delete pod POD` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
crictl ps
```

**Purpose:**  
Container runtime inventory

**When to use:**  
Node-level runtime debugging

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Container exists even if kube state is stale

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `crictl ps` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
ctr -n k8s.io containers ls
```

**Purpose:**  
Containerd inventory

**When to use:**  
Deep runtime inspection

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Lower-level runtime truth

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `ctr -n k8s.io containers ls` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
nsenter -t 1 -n ss -tulpn
```

**Purpose:**  
Enter namespaces for node-level checks

**When to use:**  
Debug host network from container context

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Host-level listeners and ports

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `nsenter -t PID -n ss -tulpn` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
dig kube-dns.kube-system.svc.cluster.local
```

**Purpose:**  
Query cluster DNS

**When to use:**  
Debug service resolution

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
DNS response or timeout

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `dig service.ns.svc.cluster.local` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
openssl s_client -connect app.example.com:443
```

**Purpose:**  
Inspect TLS handshake

**When to use:**  
Debug ingress or mTLS

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Cert chain, SNI issues

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `openssl s_client -connect host:443` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
tcpdump -i any port 53
```

**Purpose:**  
Packet capture on nodes

**When to use:**  
Prove DNS path

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Dropped queries or wrong destination

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `tcpdump -i any port 53` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl api-resources
```

**Purpose:**  
List API kinds

**When to use:**  
Check CRDs and resource availability

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Missing CRDs during deploys

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl api-resources` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl get apiservices
```

**Purpose:**  
Extension API health

**When to use:**  
Debug aggregated API issues

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Unavailable extension services

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl get apiservices` to narrow the failing boundary quickly and gather evidence before changing configuration.

### Command

```bash
kubectl get componentstatuses
```

**Purpose:**  
Legacy control-plane quick check

**When to use:**  
Very rough control-plane glance on older clusters

**Important flags:**  
Use default flags first; add filters or output flags to narrow evidence.

**What to look for:**  
Not authoritative, but hints

**Production example:**  
A DevOps, SRE, platform, or cloud engineer would use `kubectl get componentstatuses` to narrow the failing boundary quickly and gather evidence before changing configuration.


## 3. Fast Troubleshooting Commands

First 5 minutes:

- `kubectl config get-contexts`
- `kubectl config use-context prod`
- `kubectl get ns`
- `kubectl get pods -A -o wide`
- `kubectl describe pod POD`

## 4. Files and Locations

```text
/etc/hosts
/etc/resolv.conf
/var/log/
/etc/systemd/system/
~/.kube/config
~/.aws/config
~/.azure/
~/.config/gcloud/
```

Use the topic-relevant configuration first, then confirm environment-specific overrides and generated runtime state.

## 5. Useful Tools

`curl`, `jq`, `yq`, `dig`, `openssl`, `tcpdump`, `ss`, `lsof`, `journalctl`

Add provider or platform-specific tools where the topic naturally supports them.

## 6. Network / Ports / Protocols

| Port | Protocol | Purpose | Security concern |
| --- | --- | --- | --- |
| 53 | UDP/TCP | DNS | Misrouting or spoofed answers |
| 80 | TCP | HTTP | Unexpected plaintext exposure |
| 443 | TCP | HTTPS / APIs | TLS policy and certificate drift |
| 6443 | TCP | Kubernetes API | Cluster-admin exposure |
| 5432 | TCP | PostgreSQL | Unintended east-west access |

## 7. Logs

- Query service logs first.
- Check audit logs for auth or policy changes.
- Compare application logs with infrastructure logs around the same timestamp.

## 8. Metrics

- Error rate
- Latency
- Saturation
- Queue depth or backlog
- Capacity headroom
- Deployment or rollout health

## 9. Traces

Where traces apply, verify whether the request reaches the next dependency and whether retries or fan-out patterns changed latency.

## 10. Health Checks

- Readiness or service health endpoints
- CLI status commands
- Dependency reachability probes
- Certificate and DNS validation

## 11. Security Checks

- Confirm caller identity.
- Check effective permissions.
- Inspect secret sources and age.
- Verify TLS chain and endpoint exposure.
- Ensure temporary mitigations do not become permanent widening of access.

## 12. Performance Checks

- CPU, memory, and IO saturation
- Thread or worker exhaustion
- Network retransmits or DNS latency
- Database or queue backlog
- Autoscaling lag

## 13. Cost Checks

- Egress and NAT-like charges
- Idle compute or oversized nodes
- Log volume and retention
- Duplicate storage copies
- High-cardinality metrics

## 14. Keyboard / CLI Shortcuts

- `Ctrl-r` shell history search
- `!!` rerun last command in shells that support it
- `| jq` for readable JSON
- `--watch` or repeated polling where supported

## 15. Common Failure Patterns

- Auth fails → check caller identity first
- DNS resolves wrong target → inspect resolver, zone, or private DNS drift
- Service healthy but users fail → inspect edge, endpoints, or certificates
- Rollout hangs → check quota, probes, config, and events

## 16. Incident Quick Reference

Symptom  
↓  
Confirm identity and target environment  
↓  
Run the smallest command that proves the failing boundary  
↓  
Gather logs, metrics, and config evidence  
↓  
Apply the smallest safe fix  
↓  
Verify recovery and add prevention

## 17. Interview Quick Recall

- Name the control boundary.
- Explain the first evidence-gathering commands.
- Talk about blast radius, rollback, and observability.
- Mention the production shortcut that is dangerous if used blindly.
