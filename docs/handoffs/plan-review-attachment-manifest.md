# Attachment Manifest — plan-review

## Stage

| Field | Value |
| ----- | ----- |
| Stage ID | `plan-review` |
| Name | Implementation Plan Adversarial Review |
| Prompt | `docs/prompts/08-implementation-plan-review-prompt.md` |
| Output | `docs/reviews/02-implementation-plan-adversarial-review.md` |
| Status at package time | `prompt-ready` (after prompt install) |

## Required Full Artifacts

1. `docs/00-program-blueprint.md` — locked scope, success criteria, non-goals
2. `docs/01-research-charter.md` — evidence rules, methodology, anti-patterns
3. `docs/prompts/08-implementation-plan-review-prompt.md` — commissioning prompt (sole stage mission)
4. `docs/plans/01-implementation-plan.md` — **Accepted stage** proposed plan v0.1 (**attack surface**; not delivery authority)
5. `docs/specifications/02-definitive-specification-revised.md` — **Accepted** revised specification v0.2 (**implementation authority**; plan must not contradict)
6. `AGENTS.md` — repository operating rules for agents
7. `program/contracts/adversarial-review.md` — review posture, severity, plan-review attacks
8. `program/templates/finding.md` — FND write-up shape
9. `program/contracts/implementation-plan.md` — plan boundary and required shape
10. `program/contracts/authority-and-precedence.md` — precedence ladder
11. `docs/handoffs/plan-review-attachment-manifest.md` — this manifest

## Required Decision Records

- None at package time. If any `decisions/DEC-*.md` is accepted before launch,
  attach it in full and treat as highest authority.

## Required Handoff Digests

- None required separately: **full** plan and **full** revised specification are
  attached. Navigation aids only:
  - Plan §6–§9 — dependency graph, phases, milestones
  - Plan §16–§19 — risks, open questions, rollback, REQ traceability
  - Revised spec §30–§31 — handoff phase gates and high-level phases
  - Revised spec §22 / §24 — REQs and risks the plan must sequence
  - Contract: implementation-plan review attacks in `adversarial-review.md`

## Explicitly Excluded Artifacts

| Path | Why excluded |
| ---- | ------------ |
| `docs/specifications/01-definitive-specification.md` | Superseded by revised v0.2 as product law |
| `docs/reviews/01-specification-adversarial-review.md` | Findings already disposed in revised spec; not the subject |
| `docs/reports/01`–`03` full reports | Provenance only; revised spec is product law |
| Prior stage prompts (`01`–`07`) | Already executed |
| `docs/prompts/NN-*` remaining skeletons | Not commissioned |
| `docs/plans/02-implementation-plan-revised.md` | Downstream of this review |
| `docs/validations/01-implementation-plan-validation.md` | Process record; advisory only if retrieved in-repo |
| Full go-foundry repositories | Prior art already dispositioned |
| `HANDOFF.md` | Resume aid only |
| Prior handoff packages | Superseded by this manifest for launch |

## Authority Notes

1. Revised specification v0.2 is **implementation authority**. The plan is
   subordinate delivery sequencing; findings must not reverse product locks as
   “taste.”
2. The plan is **stage-accepted** but **not** delivery authority until
   plan-revision produces accepted `02-implementation-plan-revised.md`.
3. Attack **sequencing**, not architecture redesign. If a fix requires product
   law change, say so and require DEC/spec path.
4. Findings propose plan corrections; they do not rewrite the plan in this stage.
5. Preference-as-defect and feature ideation are invalid review outcomes.
6. FND range is **FND-200..FND-399** only (separate from spec-review FND-001..199).
7. Do not use packaging-session chat history as authority.
8. Owner preference: **one stage at a time** — do not chain plan-revision in the
   same substantive session.

## Expected Output

`docs/reviews/02-implementation-plan-adversarial-review.md`

(Replace the placeholder skeleton entirely.)

## Identifier Ranges

| Kind | Range | Notes |
| ---- | ----- | ----- |
| FND | FND-200..FND-399 | Stage allocation; use only as justified |
| PHASE / MS | Cite only | May find defects; do not invent coding backlog |
| REQ | Cite only | Do not mint or renumber REQs |
| RSK / OQ / SPK | Carry / cite | May recommend sequencing changes; do not renumber upstream IDs |
| DEC | DEC-001..999 | Do not invent formal DECs without human process |

## Fresh-session policy

Execute this stage in a **new session** with only the attachments above (plus
in-repo retrieval if the agent can read the workspace). Do not chain
plan-revision or product implementation in the same substantive session.
