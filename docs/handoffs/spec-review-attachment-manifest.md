# Attachment Manifest — spec-review

## Stage

| Field | Value |
| ----- | ----- |
| Stage ID | `spec-review` |
| Name | Specification Adversarial Review |
| Prompt | `docs/prompts/05-specification-adversarial-review-prompt.md` |
| Output | `docs/reviews/01-specification-adversarial-review.md` |
| Status at package time | `prompt-ready` (after prompt install) |

## Required Full Artifacts

1. `docs/00-program-blueprint.md` — locked scope, graph, success criteria, non-goals
2. `docs/01-research-charter.md` — evidence rules, methodology, anti-patterns
3. `docs/prompts/05-specification-adversarial-review-prompt.md` — commissioning prompt (sole stage mission)
4. `docs/specifications/01-definitive-specification.md` — **Accepted proposed** specification under attack (subject)
5. `docs/reports/01-modern-python-ecosystem.md` — **Accepted v0.2 full report** (provenance / lock checks)
6. `docs/reports/02-ai-native-agent-workflow.md` — **Accepted v0.2 full report** (provenance / lock checks)
7. `docs/reports/03-foundry-architecture.md` — **Accepted v0.1.1 full report** (provenance / lock checks)
8. `AGENTS.md` — repository operating rules for agents
9. `program/contracts/adversarial-review.md` — required review posture and severity
10. `program/templates/finding.md` — FND write-up shape
11. `program/contracts/authority-and-precedence.md` — precedence ladder
12. `program/contracts/definitive-specification.md` — specification shape (consistency checks)
13. `docs/handoffs/spec-review-attachment-manifest.md` — this manifest

## Required Decision Records

- None at package time (only `decisions/README.md` exists). If any
  `decisions/DEC-*.md` is accepted before launch, attach it in full and treat as
  highest authority per the precedence ladder.

## Required Handoff Digests

- None required separately: **full** specification and **full** reports are
  attached (required for adversarial review). Navigation aids only:
  - Specification §30 — handoff to adversarial review (attack seeds + strengths)
  - Ecosystem §17 — Core locks; residual ty/fnox risks
  - AI-native §17 — AGENTS.md + `.agents/` only; no Claude; MCP none
  - Architecture §17 — planner-led CLI; plan-as-contract; exclusive place

## Explicitly Excluded Artifacts

| Path | Why excluded |
| ---- | ------------ |
| `docs/prompts/01-modern-python-ecosystem-prompt.md` | Already executed; **report** is authority |
| `docs/prompts/02-ai-native-agent-workflow-prompt.md` | Already executed; **report** is authority |
| `docs/prompts/03-foundry-architecture-prompt.md` | Already executed; **report** is authority |
| `docs/prompts/04-chief-architect-synthesis-prompt.md` | Already executed; **specification** is subject |
| `docs/prompts/NN-*` remaining skeletons | Not commissioned; out of scope |
| `docs/reviews/02-implementation-plan-adversarial-review.md` | Placeholder; wrong stage |
| `docs/plans/*` | Placeholders / not accepted; not inputs to spec-review |
| `docs/specifications/02-definitive-specification-revised.md` | Downstream of this review |
| Full go-foundry repositories as mandatory attach | Prior art already dispositioned; available in-repo if needed |
| Entire `program/reference/*` | Available in-repo if needed; not required attachments |
| Raw Exa dumps under `scripts/exa-output/` | Prior-stage evidence only; not review authority |
| `HANDOFF.md` | Resume aid only; not higher authority than Blueprint/Charter/spec |
| `docs/validations/*` | Process records; advisory notes may be read from workspace but are not product authority |
| `docs/handoffs/synthesis-*` | Prior stage packaging; superseded by this manifest for launch |

## Authority Notes

1. Blueprint locks beat Charter methodology beats this prompt beats the proposed
   specification for **product constraints**; the specification is the **attack
   surface**. Reports remain provenance for lock checks.
2. Accepted ecosystem **v0.2**, AI-native **v0.2**, and architecture **v0.1.1**
   locks are **hard product invariants** unless a DEC supersedes them. Findings
   may address risk, inconsistency, or under-specification around locks — not
   reverse locks as preference.
3. The proposed specification is **not yet implementation authority**. Revision
   after this review produces implementation authority (when accepted).
4. Findings propose corrections; they do not rewrite the specification in this
   stage. Silent finding loss in later revision is a defect (revision disposes
   every FND).
5. Preference-as-defect and feature ideation are invalid review outcomes.
6. Do not use chat history from the packaging session as authority.
7. Owner preference: **one stage at a time** — do not chain specification
   revision or implementation planning in the same substantive session.

## Expected Output

`docs/reviews/01-specification-adversarial-review.md`

(Replace the placeholder skeleton entirely.)

## Identifier Ranges

| Kind | Range | Notes |
| ---- | ----- | ----- |
| FND | FND-001..FND-199 | Stage allocation; use only as justified |
| REQ | (inherited) | Reference only; do not mint or renumber REQs |
| REC | (inherited) | Provenance only; do not re-disposition RECs as the main deliverable |
| RSK / OQ | Carry / cite | May recommend new residual risks; do not renumber upstream IDs |
| PHASE | Cite only | May find phase defects; do not invent implementation plan detail |
| DEC | DEC-001..999 | Do not invent acceptance; human process for formal DECs |

## Fresh-session policy

Execute this stage in a **new session** with only the attachments above (plus
in-repo retrieval of contracts/templates if the agent can read the workspace).
Do not chain specification revision or implementation planning in the same
substantive session.
