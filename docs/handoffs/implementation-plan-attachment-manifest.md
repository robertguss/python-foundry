# Attachment Manifest — implementation-plan

## Stage

| Field | Value |
| ----- | ----- |
| Stage ID | `implementation-plan` |
| Name | Implementation Plan |
| Prompt | `docs/prompts/07-implementation-plan-prompt.md` |
| Output | `docs/plans/01-implementation-plan.md` |
| Status at package time | `prompt-ready` (after prompt install) |

## Required Full Artifacts

1. `docs/00-program-blueprint.md` — locked scope, success criteria, non-goals
2. `docs/01-research-charter.md` — evidence rules, methodology, anti-patterns
3. `docs/prompts/07-implementation-plan-prompt.md` — commissioning prompt (sole stage mission)
4. `docs/specifications/02-definitive-specification-revised.md` — **Accepted** revised specification v0.2 (**implementation authority**)
5. `docs/reviews/01-specification-adversarial-review.md` — Accepted review (residual risk / gate context; findings already disposed in revised spec)
6. `AGENTS.md` — repository operating rules for agents
7. `program/contracts/implementation-plan.md` — required plan shape and boundaries
8. `program/templates/phase.md` — phase write-up shape
9. `program/templates/milestone.md` — milestone write-up shape
10. `program/contracts/authority-and-precedence.md` — precedence ladder
11. `docs/handoffs/implementation-plan-attachment-manifest.md` — this manifest

## Required Decision Records

- None at package time. If any `decisions/DEC-*.md` is accepted before launch,
  attach it in full and treat as highest authority.

## Required Handoff Digests

- None required separately: **full** revised specification is attached.
  Navigation aids only:
  - Revised spec §R2 Finding Disposition Ledger (what was fixed for planning)
  - Revised spec §30 Updated Implementation Handoff
  - Revised spec §31 High-Level Implementation Phases
  - Revised spec §22 Normative Requirements (traceability source)
  - Revised spec §24 Risk Register

## Explicitly Excluded Artifacts

| Path | Why excluded |
| ---- | ------------ |
| `docs/specifications/01-definitive-specification.md` | Superseded by revised v0.2 as authority |
| `docs/reports/01`–`03` full reports | Provenance only; revised spec is authority — retrieve in-repo if needed for spike context |
| Prior stage prompts (`01`–`06`) | Already executed |
| `docs/prompts/NN-*` remaining skeletons | Not commissioned |
| `docs/plans/02-implementation-plan-revised.md` | Downstream of plan-review |
| `docs/reviews/02-implementation-plan-adversarial-review.md` | Placeholder; wrong stage |
| Full go-foundry repositories | Prior art already dispositioned in spec |
| `HANDOFF.md` | Resume aid only |
| `docs/validations/*` | Process records |
| Prior handoff packages | Superseded by this manifest for launch |

## Authority Notes

1. The **revised definitive specification v0.2** is **implementation authority**.
   The plan sequences delivery; it does not change product law.
2. Blueprint non-goals and User decisions remain binding.
3. Prefer revised-spec PHASE-01..06 seeds; document any merge/split rationale.
4. **No coding backlog** — phases and milestones only.
5. Do not use packaging-session chat history as authority.
6. Owner preference: **one stage at a time** — do not chain plan-review in the
   same substantive session.

## Expected Output

`docs/plans/01-implementation-plan.md`

(Replace the placeholder skeleton entirely.)

## Identifier Ranges

| Kind | Range | Notes |
| ---- | ----- | ----- |
| PHASE | PHASE-01..99 | Prefer continuity with spec seeds |
| MS | MS-001..999 | Executable acceptance evidence |
| REQ | Cite only | Trace to phases; do not mint/renumber REQs |
| RSK / OQ / SPK | Carry / schedule | Delivery sequencing |
| FND | Cite only | Spec findings already dispositioned |
| DEC | DEC-001..999 | Do not invent formal DECs without human process |

## Fresh-session policy

Execute this stage in a **new session** with only the attachments above (plus
in-repo retrieval if the agent can read the workspace). Do not chain plan
adversarial review in the same substantive session.
