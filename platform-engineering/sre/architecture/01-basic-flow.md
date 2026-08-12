# Site Reliability Engineering Basic Flow

## Intent

Show how site reliability engineering evolves from a simple mechanism into a governed production system.

## Flow summary

Reliability engineering, SLO policy, incident response, automation, and system-level risk management.

## Key design choices

- Slo is explicitly accounted for in this flow.
- Toil is explicitly accounted for in this flow.
- Automation is explicitly accounted for in this flow.
- Incident Response is explicitly accounted for in this flow.

## Failure boundaries

- Identify the first user-visible symptom.
- Define the control point that contains blast radius.
- Add telemetry that proves each handoff is working.

## Senior notes

The value of a basic flow is not its diagram density. It is the ability to explain ownership, rollback, and operating assumptions clearly enough that another engineer could critique the design before an outage does it for them.
