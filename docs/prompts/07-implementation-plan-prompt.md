# Implementation Plan Prompt — python-foundry

- **Artifact ID:** PROMPT-07-implementation-plan
- **Program:** python-foundry
- **Stage:** `implementation-plan` — Implementation Plan
- **Stage kind:** implementation-plan
- **Required inputs:**
  - `docs/00-program-blueprint.md` (Accepted)
  - `docs/01-research-charter.md` (Accepted)
  - `docs/specifications/02-definitive-specification-revised.md` (**Accepted**
    revised definitive specification v0.2 — **implementation authority**)
  - `docs/reviews/01-specification-adversarial-review.md` (Accepted — residual
    risk / phase-gate context; findings already disposed in the revised spec)
  - This prompt
  - `docs/handoffs/implementation-plan-attachment-manifest.md`
  - `AGENTS.md` (operating rules)
  - `program/contracts/implementation-plan.md`
  - `program/templates/phase.md`
  - `program/templates/milestone.md`
  - `program/contracts/authority-and-precedence.md` (as needed)
- **Required output:** `docs/plans/01-implementation-plan.md`
- **Phase range:** PHASE-01..PHASE-99 (use only as needed; prefer continuity with
  revised-spec PHASE-01..06 unless a justified split/merge is documented)
- **Milestone range:** MS-001..MS-999 (use only as needed)
- **Depends on (must be accepted):** `spec-revision`
- **Plan date:** use the actual calendar date when the plan is written

> Contract: `program/contracts/implementation-plan.md`.  
> Phase template: `program/templates/phase.md`.  
> Milestone template: `program/templates/milestone.md`.  
> Skeleton: `docs/plans/01-implementation-plan.md` (replace placeholder entirely).

## Role

Act as **Implementation Planning Architect** for python-foundry.

You:

- Translate the **accepted revised specification** into a **safe delivery
  sequence**
- Define **how to build**, not what the architecture should become
- Stay at **phase and milestone** granularity
- **Do not** invent architecture, reopen locks, or add product scope
- **Do not** create a granular coding backlog or coding-agent task packets
- **Do not** start plan-review or product implementation in this session

## Mission

Answer:

> What is the **phase-and-milestone delivery plan** to implement python-foundry
> v1 under the accepted revised definitive specification — with executable
> entry/exit criteria, early end-to-end capability, continuous integration,
> dogfooding, spikes, and rollback triggers — without a coding task backlog?

Produce `docs/plans/01-implementation-plan.md` as a **complete standalone**
implementation plan. Downstream plan review and implementers must not need chat
history.

## Authority and Precedence

Apply exactly (highest first):

1. Accepted `DEC-###` (none expected unless present under `decisions/`).
2. Locked decisions in `docs/00-program-blueprint.md`.
3. Normative methodology in `docs/01-research-charter.md`.
4. **This commissioning prompt**.
5. **Accepted revised definitive specification**
   (`docs/specifications/02-definitive-specification-revised.md` v0.2) —
   **implementation authority**. The plan is **subordinate** to it.
6. Accepted adversarial review (context for residual risks / gates already
   integrated into the revised spec).
7. Accepted research reports (provenance only; do not re-select tools).
8. This plan (output) — delivery sequence proposal until plan-review + revision
   acceptance as delivery authority.
9. `research-program.toml` as index only.
10. Model preference (lowest).

Chat history is **not** authority. The plan **must not contradict** the revised
specification. If a sequencing need appears to require a product change, record
an open question or rollback trigger — do **not** silently change REQs.

## Locked Context (do not undo via “planning”)

### Product locks (from revised spec)

- Hybrid foundry: CLI + Core emit + GitHub template snapshot
- `validate` → `plan` → `generate` (+ optional `generate --plan` bind)
- Exclusive place; closed catalog; custom engine (not Copier runtime)
- Effective verify: CLI > TOML > `default`; default = tooling-sync green (not pytest)
- Generate-time `uv.lock` production; `uv sync --locked` in default/strict
- ty Required; fnox+age; no dotenv secrets; AGENTS.md + `.agents/` only; MCP none;
  no Claude adapters
- Kind-qualified catalog UX; scripts archetype emit contract
- Frozen public template cell (cli, profiles `[]`, …)

### Non-goals

Windows; notebooks/GUI; marketplace; framework zoo; coding backlog as program
output; existing-project update/merge in v1; demoting ty/fnox without DEC.

### Revised-spec phase seeds (start here; refine, do not ignore)

| Phase | Name (spec seed) | Must incorporate (spec §30.3) |
| ----- | ---------------- | ------------------------------ |
| PHASE-01 | Pure pipeline | Profile set order; plan_sha256; verify fields; error_class; `--plan` bind shape |
| PHASE-02 | Filesystem | Stage identity; exclusive place; stage_path |
| PHASE-03 | Generate + verify + lock | Lock production; verify tiers; bind e2e |
| PHASE-04 | Catalog + emit | Core/AI-native; scripts; kind UX; forbidden paths |
| PHASE-05 | Hybrid + dogfood | Frozen template CI; dogfood foundry on Core |
| PHASE-06 | Harden | Residual risk; admission; polish |

Indicative milestones from spec: MS-001..MS-005 — expand/refine with executable
acceptance evidence; do not invent a ticket backlog under them.

### Residual risks the plan must sequence

RSK-002 (ty), RSK-007/050 (fnox/dotenv), RSK-107 (lock network cost), RSK-108
(agents skip `--plan`), OQ-105 (CLI name branding).

## Plan Boundary

### Included

1. One implementation plan at the required output path.
2. Full structure per `program/contracts/implementation-plan.md` and skeleton.
3. **Phases** with entry/exit criteria that are **observable and executable**.
4. **Milestones** with acceptance evidence (not task lists).
5. Dependency graph; cross-phase integration; testing/security/ops by phase.
6. Evidence spikes scheduled as gates (carry SPK IDs from the revised spec).
7. Dogfooding strategy; rollback/reconsideration triggers.
8. Requirement-to-phase traceability for normative REQs (at least Must REQs).
9. Risk register and open questions for **delivery** (not re-architecting).
10. Definition of plan completion.

### Excluded

1. Changing product architecture or REQ semantics (spec is authority).
2. Granular coding backlog, sprint tickets, or agent task packets.
3. Reopening non-goals or User decisions.
4. Writing plan-review findings as the main deliverable.
5. Product implementation / shipping code as this stage’s output.
6. Editing Blueprint, Charter, revised specification, or this prompt.
7. Marking the stage `accepted` without human process.
8. Starting `plan-review` or `plan-revision` in this session.

## Sequencing Principles

From the contract — enforce them:

1. Resolve unknowns (spikes) **before** they harden wrong architecture.
2. Produce **thin end-to-end capability early** (not only pure functions forever).
3. Integrate continuously; **dogfood before** broad feature expansion.
4. Keep risky decisions **reversible**.
5. Avoid phases that are only horizontal infrastructure with no usable outcome.
6. Avoid circular entry/exit criteria and acceptance that depends on later phases.
7. Prefer the revised-spec phase order unless a justified merge/split is explicit.

## Methodology

1. Read the **full** revised specification (especially REQs, phases §31, handoff
   §30, risks, FND dispositions R2).
2. Inventory Must REQs and map them to phases (traceability table).
3. Draft phase overview with user-visible outcomes per phase.
4. Expand each phase with `program/templates/phase.md` fields.
5. Define milestones with executable acceptance evidence.
6. Add integration, testing, security, ops, dogfooding, rollback.
7. Status of the plan artifact: **`Proposed — pending plan adversarial review`**
   (or equivalent non-placeholder “proposed” wording). Do **not** claim
   `Accepted — delivery authority` in this stage.
8. Do not mark program stage accepted; do not edit upstream accepted artifacts.

## Required Output Structure

Replace the placeholder skeleton entirely. Include at least:

1. Artifact Metadata  
2. Implementation Authority (point to revised spec v0.2 + commit if known)  
3. Objectives  
4. Non-Goals  
5. Assumptions  
6. Dependency Graph  
7. Phase Overview table  
8. Phases (one section per PHASE-## using phase template fields)  
9. Milestones (MS-### using milestone template fields)  
10. Cross-Phase Integration  
11. Data or Migration Sequencing (greenfield / N/A explicit)  
12. Testing Strategy by Phase  
13. Security Activities by Phase  
14. Operations and Release Readiness  
15. Dogfooding  
16. Risk Register (delivery)  
17. Open Questions  
18. Rollback and Reconsideration Triggers  
19. Requirement-to-Phase Traceability  
20. Definition of Plan Completion  
21. Completion Checklist  

## Completion Checklist

- [ ] All required plan sections present and non-placeholder
- [ ] Actual plan date recorded
- [ ] Status: proposed pending plan adversarial review (not delivery authority yet)
- [ ] Subordinate to revised specification (no REQ/architecture contradictions)
- [ ] Phases/milestones only — **no** coding backlog or task packets
- [ ] Executable entry/exit criteria (observable evidence)
- [ ] Early thin end-to-end path present (not infrastructure-only forever)
- [ ] Spikes scheduled as gates where load-bearing
- [ ] Dogfooding and hybrid template sequencing present
- [ ] Security, testing, ops addressed by phase
- [ ] Rollback/reconsideration triggers present
- [ ] Requirement-to-phase traceability for Must REQs
- [ ] Residual risks (ty, fnox, lock network, plan-bind) sequenced
- [ ] Blueprint non-goals preserved
- [ ] Allowed file scope only (plan path)
- [ ] No plan-review or implementation started as main work

## Allowed File Scope

| Path | Action |
| ---- | ------ |
| `docs/plans/01-implementation-plan.md` | **Write** (primary output; replace placeholder) |
| Other paths | **Read only** |

Do not modify `research-program.toml`, Blueprint, Charter, revised specification,
prompts, or handoff package files in the substantive planning session
(validators/humans own status transitions after validation).
