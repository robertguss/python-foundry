# Attachment Manifest — plan-revision

## Stage

| Field | Value |
| ----- | ----- |
| Stage ID | `plan-revision` |
| Name | Final Revised Implementation Plan |
| Prompt | `docs/prompts/09-implementation-plan-revision-prompt.md` |
| Output | `docs/plans/02-implementation-plan-revised.md` |
| Status at package time | `prompt-ready` (after prompt install) |

## Required Full Artifacts

1. `docs/00-program-blueprint.md` — locked scope, success criteria, non-goals
2. `docs/01-research-charter.md` — evidence rules, methodology, anti-patterns
3. `docs/prompts/09-implementation-plan-revision-prompt.md` — commissioning prompt (sole stage mission)
4. `docs/plans/01-implementation-plan.md` — **Accepted stage** proposed plan v0.1 (**base text**; not delivery authority)
5. `docs/reviews/02-implementation-plan-adversarial-review.md` — **Accepted** review; FND-200..205 to dispose
6. `docs/specifications/02-definitive-specification-revised.md` — **Accepted** revised specification v0.2 (**implementation authority**; plan must stay subordinate)
7. `AGENTS.md` — repository operating rules for agents
8. `program/contracts/implementation-plan.md` — plan boundary + final revised plan rules
9. `program/templates/phase.md` — phase write-up shape
10. `program/templates/milestone.md` — milestone write-up shape
11. `program/operator/completion-criteria.md` — final implementation handoff contents
12. `program/contracts/authority-and-precedence.md` — precedence ladder
13. `docs/handoffs/plan-revision-attachment-manifest.md` — this manifest

## Required Decision Records

- None at package time. If any `decisions/DEC-*.md` is accepted before launch,
  attach it in full and treat as highest authority.

## Required Handoff Digests

- None required separately: **full** proposed plan, **full** review, and **full**
  revised specification are attached. Navigation aids only:
  - Review finding index FND-200..205 and gate **Conditional**
  - Review §3 strengths to preserve; §5 sequencing themes
  - Proposed plan §6–§9 — dependency graph, phases, milestones (base sequencing)
  - Proposed plan §15–§19 — dogfood, risks, rollback, REQ traceability
  - Revised-spec §30–§31 — phase gates; product DoD §29.2
  - Contract final revised plan rules in `implementation-plan.md`
  - Handoff fields in `program/operator/completion-criteria.md`

## Explicitly Excluded Artifacts

| Path | Why excluded |
| ---- | ------------ |
| `docs/specifications/01-definitive-specification.md` | Superseded by revised v0.2 as product law |
| `docs/reviews/01-specification-adversarial-review.md` | Findings already disposed in revised spec |
| `docs/reports/01`–`03` full reports | Provenance only; revised spec is product law |
| Prior stage prompts (`01`–`08`) | Already executed; outputs are authority |
| `docs/prompts/NN-*` remaining skeletons | Not commissioned |
| `docs/plans/02-implementation-plan-revised.md` | **Output** path (placeholder until written) |
| `docs/validations/*` | Process records; not delivery authority |
| Full go-foundry repositories | Prior art already dispositioned |
| `HANDOFF.md` | Resume aid only |
| Prior handoff packages (`plan-review-*`, etc.) | Superseded by this manifest for launch |

## Authority Notes

1. Revised specification v0.2 is **implementation authority**. The revised plan
   becomes **delivery authority** only when artifact status and human stage
   acceptance allow.
2. The **accepted plan-review** proposes sequencing corrections; dispositions may
   Reject or modify with rationale. Silent FND loss is a defect.
3. The **proposed plan** is the base text; do not treat it as frozen against
   accepted findings.
4. Locks (ty, fnox, AGENTS-only, no Claude, exclusive place, custom engine) are
   not reversed by preference or as “plan fixes.”
5. Prefer simplification over new plan machinery when disposing findings.
6. Phases/milestones only — no coding backlog.
7. Do not use packaging-session chat history as authority.
8. Owner preference: **one stage at a time** — do not chain product
   implementation in the same substantive session.

## Expected Output

`docs/plans/02-implementation-plan-revised.md`

(Replace the placeholder skeleton entirely.)

## Identifier Ranges

| Kind | Range | Notes |
| ---- | ----- | ----- |
| FND | FND-200..205 | Disposition only; do not mint new FNDs |
| PHASE | PHASE-01..99 | Prefer continuity; document justified split/merge |
| MS | MS-001..999 | Progressive gates OK; no task packets |
| REQ | Cite only | Do not mint or renumber REQs |
| RSK / OQ / SPK | Carry / update | Bound any new spikes; do not renumber upstream IDs |
| DEC | DEC-001..999 | Do not invent formal DECs without human process |

## Fresh-session policy

Execute this stage in a **new session** with only the attachments above (plus
in-repo retrieval if the agent can read the workspace). Do not chain product
implementation in the same substantive session.
