# Attachment Manifest — spec-revision

## Stage

| Field | Value |
| ----- | ----- |
| Stage ID | `spec-revision` |
| Name | Revised Definitive Specification |
| Prompt | `docs/prompts/06-specification-revision-prompt.md` |
| Output | `docs/specifications/02-definitive-specification-revised.md` |
| Status at package time | `prompt-ready` (after prompt install) |

## Required Full Artifacts

1. `docs/00-program-blueprint.md` — locked scope, graph, success criteria, non-goals
2. `docs/01-research-charter.md` — evidence rules, methodology, anti-patterns
3. `docs/prompts/06-specification-revision-prompt.md` — commissioning prompt (sole stage mission)
4. `docs/specifications/01-definitive-specification.md` — **Accepted proposed** specification (base text)
5. `docs/reviews/01-specification-adversarial-review.md` — **Accepted** review; FND-001..012 to dispose
6. `docs/reports/01-modern-python-ecosystem.md` — **Accepted v0.2 full report** (provenance / lock checks)
7. `docs/reports/02-ai-native-agent-workflow.md` — **Accepted v0.2 full report** (provenance / lock checks)
8. `docs/reports/03-foundry-architecture.md` — **Accepted v0.1.1 full report** (provenance / lock checks)
9. `AGENTS.md` — repository operating rules for agents
10. `program/contracts/definitive-specification.md` — structure + revision/disposition rules
11. `program/templates/requirement.md` — REQ write-up shape
12. `program/contracts/authority-and-precedence.md` — precedence ladder
13. `docs/handoffs/spec-revision-attachment-manifest.md` — this manifest

## Required Decision Records

- None at package time (only `decisions/README.md` exists). If any
  `decisions/DEC-*.md` is accepted before launch, attach it in full and treat as
  highest authority per the precedence ladder.

## Required Handoff Digests

- None required separately: **full** proposed spec, **full** review, and **full**
  reports are attached. Navigation aids only:
  - Review §8 finding index (FND-001..012)
  - Review §6 gate (Conditional) and §3 strengths to preserve
  - Proposed spec §30 handoff seeds (historical)
  - Proposed spec REC disposition ledger (§28) — carry forward

## Explicitly Excluded Artifacts

| Path | Why excluded |
| ---- | ------------ |
| `docs/prompts/01`–`05` prior stage prompts | Already executed; outputs are authority |
| `docs/prompts/NN-*` remaining skeletons | Not commissioned |
| `docs/plans/*` | Placeholders; not inputs to revision |
| `docs/reviews/02-implementation-plan-adversarial-review.md` | Placeholder; wrong stage |
| `docs/specifications/02-definitive-specification-revised.md` | **Output** path (placeholder until written) |
| Full go-foundry repositories as mandatory attach | Prior art already dispositioned |
| Entire `program/reference/*` | Available in-repo if needed |
| Raw Exa dumps | Not revision authority |
| `HANDOFF.md` | Resume aid only |
| `docs/validations/*` | Process records; not product authority |
| Prior handoff packages (`synthesis-*`, `spec-review-*`) | Superseded by this manifest for launch |

## Authority Notes

1. Blueprint locks beat Charter methodology beats this prompt. The **revised**
   specification becomes implementation authority only when artifact status and
   human stage acceptance allow.
2. The **accepted review** proposes corrections; dispositions may Reject or
   modify with rationale. Silent FND loss is a defect.
3. The **proposed specification** is the base text; do not treat it as frozen
   against accepted findings.
4. Locks (ty, fnox, AGENTS-only, no Claude, exclusive place, custom engine) are
   not reversed by preference.
5. Prefer simplification over new machinery when disposing findings.
6. Do not use packaging-session chat history as authority.
7. Owner preference: **one stage at a time** — do not chain implementation
   planning in the same substantive session.

## Expected Output

`docs/specifications/02-definitive-specification-revised.md`

(Replace the placeholder skeleton entirely.)

## Identifier Ranges

| Kind | Range | Notes |
| ---- | ----- | ----- |
| FND | FND-001..012 | Disposition only; do not mint new FNDs |
| REQ | REQ-001..REQ-299 | Retain stable IDs; new only from unused (084+) |
| REC | inherited | Carry disposition ledger; do not re-open tool selection |
| RSK / OQ / SPK | Carry / update | Bound any new spikes |
| PHASE | PHASE-01..99 | Update gates if findings require |
| DEC | DEC-001..999 | Do not invent formal DECs without human process |

## Fresh-session policy

Execute this stage in a **new session** with only the attachments above (plus
in-repo retrieval if the agent can read the workspace). Do not chain
implementation planning in the same substantive session.
