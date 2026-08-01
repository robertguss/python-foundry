# Attachment Manifest — synthesis

## Stage

| Field | Value |
| ----- | ----- |
| Stage ID | `synthesis` |
| Name | Definitive Specification Synthesis |
| Prompt | `docs/prompts/04-chief-architect-synthesis-prompt.md` |
| Output | `docs/specifications/01-definitive-specification.md` |
| Status at package time | `prompt-ready` (after prompt install) |

## Required Full Artifacts

1. `docs/00-program-blueprint.md` — locked scope, graph, success criteria, non-goals
2. `docs/01-research-charter.md` — evidence rules, methodology, anti-patterns
3. `docs/prompts/04-chief-architect-synthesis-prompt.md` — commissioning prompt (sole stage mission)
4. `docs/reports/01-modern-python-ecosystem.md` — **Accepted v0.2 full report** (Core/profiles, REC-001..014)
5. `docs/reports/02-ai-native-agent-workflow.md` — **Accepted v0.2 full report** (agent surface, REC-100..112)
6. `docs/reports/03-foundry-architecture.md` — **Accepted v0.1.1 full report** (generator architecture, REC-200..212)
7. `AGENTS.md` — repository operating rules for agents
8. `program/contracts/synthesis.md` — synthesis behavior and disposition rules
9. `program/contracts/definitive-specification.md` — required specification shape
10. `program/templates/requirement.md` — REQ write-up shape
11. `program/contracts/authority-and-precedence.md` — precedence ladder
12. `docs/handoffs/synthesis-attachment-manifest.md` — this manifest

## Required Decision Records

- None at package time (only `decisions/README.md` exists). If any
  `decisions/DEC-*.md` is accepted before launch, attach it in full and treat as
  highest authority per the precedence ladder.

## Required Handoff Digests

- None required separately: **full** reports are attached (required for synthesis).
  Each report’s Handoff Digest (§17) must still be read as a navigation aid:
  - Ecosystem §17 — Core locks; synthesis traces RECs → REQs; OQ-001/004/006 notes
  - AI-native §17 — AGENTS.md + `.agents/` only; no Claude; MCP none; REC-100..112
  - Architecture §17 — planner-led CLI; plan-as-contract; emit contracts; REC-200..212

## Explicitly Excluded Artifacts

| Path | Why excluded |
| ---- | ------------ |
| `docs/prompts/01-modern-python-ecosystem-prompt.md` | Already executed; **report** is authority |
| `docs/prompts/02-ai-native-agent-workflow-prompt.md` | Already executed; **report** is authority |
| `docs/prompts/03-foundry-architecture-prompt.md` | Already executed; **report** is authority |
| Spine prompts still `NN-*` (spec-review, plan, etc.) | Not commissioned; out of scope |
| `docs/reviews/*`, `docs/plans/*` | Placeholders / not accepted; not inputs to first synthesis |
| `docs/specifications/02-definitive-specification-revised.md` | Downstream of review |
| Full go-foundry repositories as mandatory attach | Prior art already dispositioned in architecture REC-210 |
| Entire `program/reference/*` | Available in-repo if needed; not required attachments |
| Raw Exa dumps under `scripts/exa-output/` | Prior-stage evidence only; not synthesis authority |
| `HANDOFF.md` | Resume aid only; not higher authority than Blueprint/Charter/reports |
| `docs/validations/*` | Process records; not product authority |

## Authority Notes

1. Blueprint locks beat Charter methodology beats this prompt beats research
   recommendations for **product** constraints; reports remain the evidence base
   for *what* to disposition into REQs.
2. Accepted ecosystem **v0.2**, AI-native **v0.2**, and architecture **v0.1.1**
   locks are **hard emit / product invariants** unless a DEC supersedes them.
   Synthesis **traces** them into REQs; it does not re-litigate tool selection or
   agent product support.
3. Research reports are recommendations until the **revised** definitive
   specification is accepted as implementation authority. This stage produces
   **Proposed — pending adversarial review**.
4. Disposition every REC (Accepted / with modification / Merged / Deferred /
   Rejected / Superseded / Not applicable). Silent REC loss is a defect.
5. go-foundry is prior art only; follow architecture Adopt/Adapt/Reject.
6. Do not use chat history from the packaging session as authority.
7. Owner preference: **one stage at a time** — do not chain adversarial review
   or implementation planning in the same substantive session.

## Expected Output

`docs/specifications/01-definitive-specification.md`

(Replace the placeholder skeleton entirely.)

## Identifier Ranges

| Kind | Range | Notes |
| ---- | ----- | ----- |
| REQ | REQ-001..REQ-299 | Stage allocation; use only as needed |
| REC | (inherited) | Disposition only; do not mint new RECs in synthesis |
| RSK | Carry upstream IDs | RSK-001..007, 050..056, 100..106; add new only if truly new |
| OQ | Carry upstream IDs | Resolve or restate; do not renumber |
| SPK | Carry / schedule | Map residual spikes into phases; do not invent unbounded spikes |
| PHASE | PHASE-01..PHASE-99 | High-level only |
| DEC | DEC-001..999 | Do not invent acceptance; human process for formal DECs |

## Fresh-session policy

Execute this stage in a **new session** with only the attachments above (plus
in-repo retrieval of contracts/templates if the agent can read the workspace).
Do not chain specification adversarial review, revision, or implementation
planning in the same substantive session.
