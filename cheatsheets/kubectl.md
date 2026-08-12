# kubectl Cheat Sheet

Organized by **what you're trying to find out**, not alphabetically —
each command includes when you'd actually reach for it.

## "Is this thing actually running and healthy?"

```bash
kubectl get pods -n <ns> -o wide
```
Use when: first triage step, always. `-o wide` gets you the node and pod
IP for free, saving a follow-up command.

```bash
kubectl describe pod <pod> -n <ns>
```
Use when: `get pods` shows something other than `Running`/`Ready` — this
is where you actually see *why* (events, probe failures, image pull
errors) rather than just the summary status.

## "Why is there no traffic reaching this pod?"

```bash
kubectl get endpoints <service> -n <ns>
```
Use when: debugging a 503/no-route symptom — per
[`kubernetes/troubleshooting.md` Lab 3](../kubernetes/troubleshooting.md#lab-3-kubectl-reports-ingress-is-healthy-but-requests-return-503),
an empty Endpoints object (not the Service or Ingress object) is the
actual smoking gun most of the time.

```bash
kubectl get pods -l <selector-from-service>
```
Use when: Endpoints is empty — checks whether the Service's selector
actually matches any pods at all.

## "What did this pod actually log before it died?"

```bash
kubectl logs <pod> -n <ns> --previous
```
Use when: a pod has restarted (`RESTARTS > 0`) — `--previous` gets logs
from the crashed instance, not the fresh one that just started. Forgetting
`--previous` here is one of the most common wasted debugging steps.

## "Is this a resource/scheduling problem?"

```bash
kubectl top pod <pod> -n <ns> --containers
```
Use when: suspecting resource pressure — note this is a live snapshot,
not history; for a *past* OOM event you need your metrics backend's
historical data, not `top`.

```bash
kubectl get events -n <ns> --sort-by='.lastTimestamp'
```
Use when: something happened recently and you're not sure what — this is
often faster than guessing which specific `describe` to run, since events
surface scheduling failures, image pulls, OOM kills, and probe failures
all in one timeline.

## "Is Argo CD lying to me about sync status?"

```bash
argocd app diff <app>
kubectl get application <app> -n argocd -o jsonpath='{.spec.source.targetRevision}'
```
Use when: Argo CD shows `Synced`/`Healthy` but behavior doesn't match Git
— per [`kubernetes/troubleshooting.md` Lab 5](../kubernetes/troubleshooting.md#lab-5-argo-cd-shows-an-application-as-synced-and-healthy-but-the-running-behavior-doesnt-match-what-is-in-git),
check what ref is actually being tracked before assuming a bug.
