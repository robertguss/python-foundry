# Implementation Plan Adversarial Review Prompt — python-foundry

- **Artifact ID:** PROMPT-08-implementation-plan-review
- **Program:** python-foundry
- **Stage:** `plan-review` — Implementation Plan Adversarial Review
- **Stage kind:** adversarial-review
- **Required inputs:**
  - `docs/00-program-blueprint.md` (Accepted)
  - `docs/01-research-charter.md` (Accepted)
  - `docs/plans/01-implementation-plan.md` (**Accepted stage** proposed plan v0.1 —
    subject under attack; **not** delivery authority)
  - `docs/specifications/02-definitive-specification-revised.md` (**Accepted**
    revised definitive specification v0.2 — **implementation authority**; plan
    must remain subordinate)
  - This prompt
  - `docs/handoffs/plan-review-attachment-manifest.md`
  - `AGENTS.md` (operating rules)
  - `program/contracts/adversarial-review.md`
  - `program/templates/finding.md`
  - `program/contracts/implementation-plan.md`
  - `program/contracts/authority-and-precedence.md` (as needed)
- **Required output:** `docs/reviews/02-implementation-plan-adversarial-review.md`
- **Finding range:** FND-200..FND-399
- **Depends on (must be accepted):** `implementation-plan`
- **Review date:** use the actual calendar date when review is executed

> Contract: `program/contracts/adversarial-review.md` (implementation-plan review
> attacks).  
> Finding template: `program/templates/finding.md`.  
> Plan contract: `program/contracts/implementation-plan.md`.  
> Skeleton: `docs/reviews/02-implementation-plan-adversarial-review.md`
> (replace placeholder content entirely).

## Role

Act as an **adversarial reviewer** of the proposed implementation plan.

You:

- **Attack sequencing and delivery safety**, not product taste or stack preference
- Find circular dependencies, missing prerequisites, unprovable exit criteria,
  late risk discovery, deferred integration/dogfooding, overlarge phases,
  milestones without integration evidence, and plan steps that **reinterpret**
  architecture or REQs
- Produce a **small number of strong findings** rather than meeting a quota
- Prefer concrete failure scenarios and required **plan** corrections
- **Do not add features** or invent attractive subsystems
- **Do not** treat preference, taste, or “I would sequence differently for
  style” as defects unless the plan is unsafe, non-total, or contradicts
  authority
- **Do not** revise the plan or the specification in this stage (review only)
- **Do not** reopen locked non-goals or User decisions without framing them as
  **findings about plan consistency/risk** — not as license to reverse locks

## Mission

Answer:

> What is wrong with the **accepted proposed implementation plan** such that
> plan-revision must correct it before delivery authority — covering circular or
> unexecutable sequencing, missing spike gates, late thin-E2E/dogfood/hybrid
> integration, acceptance criteria that do not prove outcomes, security/test/ops
> gaps across phases, and any reinterpretation of the revised specification?

Produce `docs/reviews/02-implementation-plan-adversarial-review.md` as a
**complete standalone** adversarial review. Downstream plan-revision must dispose
every `FND-###` without chat history.

## Authority and Precedence

Apply exactly (highest first):

1. Accepted `DEC-###` (none expected unless present under `decisions/`).
2. Locked decisions in `docs/00-program-blueprint.md`.
3. Normative methodology in `docs/01-research-charter.md`.
4. **This commissioning prompt**.
5. **Accepted revised definitive specification v0.2**
   (`docs/specifications/02-definitive-specification-revised.md`) —
   **implementation / product law**. The plan must not contradict it; findings
   that require product-law change must say so and point to DEC/spec-revision —
   do not silently treat the plan as higher authority.
6. The **proposed implementation plan** under review
   (`docs/plans/01-implementation-plan.md`) — **attack surface**; stage-accepted
   but **not** delivery authority.
7. This review (output) — proposals for plan-revision, not product law and not
   delivery sequence until revision is accepted.
8. `research-program.toml` as operational index only.
9. Model preference (lowest; never load-bearing alone).

Chat history, model memory, and uncommitted notes are **not** authority.

**Important:** Locks and User decisions (ty Required, fnox+age, no dotenv
secrets, AGENTS.md-only, no Claude adapters, plan-as-contract, exclusive place,
closed catalog, custom engine, generate-time `uv.lock`, verify CLI > TOML >
default, optional `generate --plan` bind, macOS+Linux only) are **not** defects
because a reviewer prefers alternatives. Attack **sequencing risk,
unprovable gates, inconsistency with REQs/phases, or false confidence** — do not
reverse product locks as plan “fixes.”

## Locked Context (do not silently undo via “findings”)

### Blueprint non-goals (not v1 scope)

Windows; notebooks/GUI/mobile; marketplace / remote catalogs; framework zoo;
unlimited MCP/skill catalog; new package manager; coding backlog as program
output; full product implementation as a substitute for an accepted revised plan
(owner residual risk is separate from program graph honesty).

### Product locks (from revised spec — plan must preserve)

- Hybrid foundry: CLI + Core emit + GitHub template snapshot
- `validate` → `plan` → `generate` (+ optional `generate --plan` bind)
- Exclusive place; closed catalog; custom engine (not Copier runtime)
- Effective verify: CLI > TOML > `default`; default = tooling-sync green (not pytest)
- Generate-time `uv.lock`; `uv sync --locked` in default/strict
- ty Required; fnox+age; no dotenv secrets; AGENTS.md + `.agents/` only; MCP none;
  no Claude adapters
- Kind-qualified catalog UX; scripts archetype emit contract
- Frozen public template cell (cli, profiles `[]`, …)

### Plan stage claims (attack surface seeds — not exhaustive)

From plan v0.1 and contract **implementation-plan review attacks**:

1. Circular or ambiguous phase dependencies; exit criteria that depend on later
   phases.
2. Missing prerequisites for a phase’s claimed exit evidence.
3. Overlarge phases that hide non-integrable work.
4. Milestones without integration / observable acceptance evidence.
5. Acceptance or exit criteria that do not prove the claimed outcome.
6. Late discovery of residual risks (ty, fnox/dotenv, lock network, plan-bind)
   relative to when they harden.
7. Delayed dogfooding or hybrid template relative to breadth expansion.
8. Deferred continuous integration (thin E2E too late vs PHASE-03 claim).
9. Security / testing / ops gaps by phase; rollback triggers weak or circular.
10. Phase boundaries that conflict with revised-spec PHASE-01..06 / REQ phase tags.
11. Plan steps that reinterpret architecture or REQ semantics.
12. Excessive parallel work or order that hardens wrong decisions before spikes.
13. Coding-backlog creep disguised as milestones or phase scope.
14. Provisional CLI name / branding treated as blocking architecture.
15. MS-006 or other expansions that reintroduce backlog granularity or
    unexecutable “readiness.”

### Strengths to preserve (do not “find” them away without cause)

- Continuity with revised-spec PHASE-01..06
- Thin E2E at PHASE-03 / MS-002 before full catalog breadth
- Spike gates (SPK-100..103, SPK-002/050/052)
- Must REQ traceability table
- Explicit residual risk sequencing (ty, fnox, lock, `--plan`)
- No coding backlog; phases/milestones only
- Subordination language to revised specification

## Stage Boundary

### Included

1. One **adversarial review** at the required output path.
2. Full structure per this prompt (metadata through completion checklist).
3. Findings **`FND-200..FND-399`** as needed (use only what is justified; leave
   unused IDs unallocated — never invent padding findings).
4. Each finding uses `program/templates/finding.md` fields (severity, confidence,
   problem, evidence, failure scenario, impact, root cause, required correction,
   proposed plan diff, acceptance evidence, alternatives, residual risk,
   related findings). For plan review, **Proposed Specification Diff** becomes
   **Proposed Plan Diff** (section/PHASE/MS-level corrections to the plan — not
   code patches and not silent REQ rewrites).
5. **Executive assessment** and **implementation gate** recommendation
   (Open | Conditional | Blocked) with rationale — gate meaning:
   - **Open:** plan may become delivery authority after mechanical polish only
   - **Conditional:** plan-revision must dispose named findings first
   - **Blocked:** Critical sequencing defects prevent treating any revision as
     delivery authority until fixed
6. **Sequencing and integration issues** (themes across phases/milestones).
7. Whether an **additional review round** is recommended under risk-triggered
   policy — not automatic.
8. Finding index table; honest completion checklist.

### Excluded

1. Revising the implementation plan (downstream `plan-revision`).
2. Revising the definitive specification or inventing product REQs.
3. Writing coding backlogs, sprint tickets, or agent task packets.
4. Reopening Windows, notebooks, marketplace, framework zoo, dotenv secrets,
   Claude adapters, demoting ty/fnox, or Copier-as-engine as product scope
   (unless framed only as **plan risk/consistency** with correction short of
   scope reversal).
5. Feature ideation disguised as defects.
6. Product implementation or starting PHASE-01 coding as this stage’s output.
7. Editing Blueprint, Charter, revised specification, plan, or this prompt.
8. Marking this stage `accepted` or inventing DEC records without human process.
9. Starting `plan-revision` or any later stage.
10. Re-running focused research or re-selecting tools.

## Review Method

1. Read **all required inputs completely** — Blueprint, Charter, full proposed
   plan, revised specification (especially REQs, §30–31, risks, phases),
   contracts, this prompt, attachment manifest.
2. Inventory plan phases, milestones, dependency graph, spike gates, dogfood,
   hybrid path, rollback triggers, and REQ→phase traceability.
3. Attack with **implementation-plan review attacks** from
   `program/contracts/adversarial-review.md` plus software-first checks that
   apply to delivery sequencing (not product redesign).
4. Trace **delivery path end-to-end**: pure pipeline → fs → thin generate →
   catalog → hybrid/dogfood → harden; ask where evidence is missing.
5. Check **failure and rollback** sequencing (what happens if SPK fails; if
   default verify cost is unacceptable; if ty/fnox spikes fail).
6. Check **consistency** across plan prose, phase exit criteria, milestones,
   traceability table, and revised-spec phase tags / Must REQs.
7. Attempt to **delete unnecessary plan machinery** (if a phase/milestone is
   pure process theater without outcome, say so).
8. Prefer **strong findings** with concrete failure scenarios. Merge weak nits
   into Low severity or drop them.
9. Do **not** mark stage accepted; do not edit the plan or specification.

## Severity Guide

| Level | Meaning |
| ----- | ------- |
| **Critical** | Blocks treating any plan as delivery authority; catastrophic delivery failure |
| **High** | Blocks the affected phase gate or creates major invalid delivery behavior |
| **Medium** | Must be fixed before the affected phase is accepted as complete |
| **Low** | Should be corrected in plan-revision; does not block early delivery work |

Every finding must state whether it **blocks implementation**: Entire program |
Named phase | No.

## Finding Rules

- Allocate only **FND-200..FND-399**; never reuse IDs; do **not** use
  specification-review range FND-001..FND-199 for new plan findings.
- One finding = one coherent defect theme (may list multiple phases/MS/REQs).
- **Required Correction** must be actionable for `plan-revision` (what to change
  in the plan — not product code patches).
- **Proposed Plan Diff** may be prose section/PHASE/MS-level (“split PHASE-0X”,
  “add exit criterion …”, “move SPK-00N gate earlier”) — not a full rewritten
  plan and not a coding backlog.
- If the only honest fix is a **product** change, say so explicitly and require a
  DEC/spec path — do not hide product changes as plan nits.
- **Acceptance Evidence** = how plan-revision proves the finding is addressed.
- Cite evidence from the plan and revised spec with section / PHASE / MS / REQ
  IDs. Prefer portable references over chat claims.
- Preference-as-defect is invalid. “I would merge PHASE-04 and PHASE-05 for
  taste” is not a finding unless sequencing is unsafe or non-total.

## Required Output Structure

Replace the placeholder skeleton entirely. Include at least:

1. **Artifact Metadata** (program, stage, subject path/version, review date,
   finding range used, gate recommendation summary)
2. **Review Scope and Method** (what was read; attack method; explicit
   out-of-scope)
3. **Executive Assessment** (overall delivery-sequence quality; top risks;
   preserve strengths)
4. **Findings** — one `## FND-### — Title` section per finding (template fields;
   use **Proposed Plan Diff** in place of specification diff)
5. **Sequencing and Integration Issues** (cross-cutting themes)
6. **Implementation Gate Recommendation**
   - Gate: **Open** | **Conditional** | **Blocked**
   - Rationale (must align with Critical/High findings)
7. **Whether an Additional Review Round Is Recommended** (risk-triggered; yes/no
   + conditions)
8. **Finding Index Table** (FND | Severity | Blocks | One-line summary)
9. **Completion Checklist**

### Suggested status line for the review artifact

`Complete — pending independent validation and human acceptance`

(Do not use `Placeholder — not accepted` once the review is written.)

## Completion Checklist

- [ ] All required review sections present and non-placeholder
- [ ] Status is not Placeholder
- [ ] Actual review date recorded in metadata
- [ ] Findings use only FND-200..FND-399; no out-of-range IDs; no silent reuse
- [ ] Each finding has severity, failure scenario, required correction
- [ ] No feature ideation disguised as defects
- [ ] Preference-as-defect avoided; product locks not silently reversed
- [ ] Plan-review attack seeds considered (addressed or explicitly N/A)
- [ ] Strengths to preserve acknowledged (not “fixed away” without cause)
- [ ] Implementation gate recommendation present and consistent with severities
- [ ] Additional review round recommendation present
- [ ] Finding index table complete
- [ ] Allowed file scope only (review path)
- [ ] Plan and revised specification **not** modified
- [ ] No downstream stage started (no revised plan content as main work)
- [ ] No coding backlog introduced in the review

## Allowed File Scope

| Path | Action |
| ---- | ------ |
| `docs/reviews/02-implementation-plan-adversarial-review.md` | **Write** (primary output; replace placeholder) |
| Other paths | **Read only** |

Do not modify `research-program.toml`, Blueprint, Charter, revised specification,
implementation plan, prompts, or handoff package files in the substantive review
session (validators/humans own status transitions after validation).
