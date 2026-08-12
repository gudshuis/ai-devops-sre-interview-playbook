# Security Incidents Basic Flow

## Intent

Show how security incidents evolves from a simple mechanism into a governed production system.

## Flow summary

Security response scenarios spanning access misuse, credential exposure, policy failures, and containment choices.

## Key design choices

- Containment is explicitly accounted for in this flow.
- Credentials is explicitly accounted for in this flow.
- Forensics is explicitly accounted for in this flow.
- Blast Radius is explicitly accounted for in this flow.

## Failure boundaries

- Identify the first user-visible symptom.
- Define the control point that contains blast radius.
- Add telemetry that proves each handoff is working.

## Senior notes

The value of a basic flow is not its diagram density. It is the ability to explain ownership, rollback, and operating assumptions clearly enough that another engineer could critique the design before an outage does it for them.
