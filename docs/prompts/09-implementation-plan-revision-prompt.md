# Implementation Plan Revision Prompt — python-foundry

- **Artifact ID:** PROMPT-09-implementation-plan-revision
- **Program:** python-foundry
- **Stage:** `plan-revision` — Final Revised Implementation Plan
- **Stage kind:** artifact-revision
- **Required inputs:**
  - `docs/00-program-blueprint.md` (Accepted)
  - `docs/01-research-charter.md` (Accepted)
  - `docs/plans/01-implementation-plan.md` (**Accepted stage** proposed plan
    v0.1 — **base text** to revise; **not** delivery authority)
  - `docs/reviews/02-implementation-plan-adversarial-review.md` (**Accepted**
    review; findings **FND-200..FND-205** — dispose every one)
  - `docs/specifications/02-definitive-specification-revised.md` (**Accepted**
    revised definitive specification v0.2 — **implementation authority**; plan
    remains subordinate)
  - This prompt
  - `docs/handoffs/plan-revision-attachment-manifest.md`
  - `AGENTS.md` (operating rules)
  - `program/contracts/implementation-plan.md` (plan boundary + final revised
    plan rules)
  - `program/templates/phase.md`
  - `program/templates/milestone.md`
  - `program/operator/completion-criteria.md` (final implementation handoff
    contents)
  - `program/contracts/authority-and-precedence.md` (as needed)
- **Required output:** `docs/plans/02-implementation-plan-revised.md`
- **Finding dispositions required:** FND-200..FND-205 (exactly one disposition each)
- **Phase range:** PHASE-01..PHASE-99 (prefer continuity with proposed plan /
  revised-spec PHASE-01..06 unless a justified split/merge is documented)
- **Milestone range:** MS-001..MS-999 (use only as needed; progressive gates OK
  at phase/milestone granularity — **not** a coding backlog)
- **Depends on (must be accepted):** `plan-review`
- **Revision date:** use the actual calendar date when revision is executed

> Contract: `program/contracts/implementation-plan.md` (including **Final
> revised plan** rules).  
> Phase template: `program/templates/phase.md`.  
> Milestone template: `program/templates/milestone.md`.  
> Handoff contents: `program/operator/completion-criteria.md`.  
> Skeleton: `docs/plans/02-implementation-plan-revised.md` (replace placeholder
> content entirely).

## Role

Act as **Revision Architect** for the **delivery plan** (not product law).

You:

- Produce **one coherent revised implementation plan** that is standalone and
  suitable as **delivery authority** if blockers are cleared
- **Disposition every** `FND-200..FND-205` with exactly one allowed disposition
- **Integrate** accepted corrections into phases, milestones, dependency graph,
  dogfood/hybrid order, spike gates, residual policy, and exit criteria (not
  only in a ledger)
- **Remove** superseded or contradictory sequencing language from the proposed
  plan
- **Reconcile** overlapping finding corrections into one consistent delivery
  sequence
- **Preserve** important strengths called out in the review
- **Prefer simplification** over new plan machinery when both satisfy the finding
- Remain at **phase and milestone** granularity — **no** coding backlog, sprint
  tickets, or agent task packets
- **Do not** change architecture, REQ semantics, or product locks (revised-spec
  is product law)
- **Do not** start product implementation in this session

## Mission

Answer:

> What is the **single coherent final revised implementation plan** for
> python-foundry that disposes every accepted plan-review finding, integrates
> sequencing corrections into the body of the delivery plan, stays subordinate
> to revised-spec v0.2, and can become **delivery authority** if no
> implementation-blocking plan findings remain?

Produce `docs/plans/02-implementation-plan-revised.md` as a **complete
standalone** revised plan. Downstream implementers must not need chat history,
the proposed plan alone, or the review alone — though those remain citable
provenance.

## Authority and Precedence

Apply exactly (highest first):

1. Accepted `DEC-###` records that explicitly supersede earlier authority (none
   expected unless present under `decisions/` at launch).
2. Locked decisions in `docs/00-program-blueprint.md`.
3. Normative methodology in `docs/01-research-charter.md`.
4. **This commissioning prompt**.
5. **Accepted revised definitive specification**
   (`docs/specifications/02-definitive-specification-revised.md` v0.2) —
   **implementation / product law**. The plan **MUST NOT** contradict it.
6. **This revised plan** (output) — after human acceptance becomes **delivery
   authority** if artifact status warrants.
7. Accepted proposed plan (`docs/plans/01-implementation-plan.md`) — base text;
   may be corrected by dispositions.
8. Accepted plan adversarial review
   (`docs/reviews/02-implementation-plan-adversarial-review.md`) — findings to
   dispose; not automatic law (may Reject with rationale).
9. `research-program.toml` as operational index only.
10. Model preference (lowest; never load-bearing alone).

Chat history, model memory, and uncommitted notes are **not** authority.
Handoff digests **never** replace full artifacts.

**If a finding appears to require product-law change:** do **not** silently amend
REQs or locks. Either Reject the finding as product-scope, or record an open
question / DEC path — plan-revision fixes **sequencing**, not product design.

## Locked Context (do not silently undo)

### Blueprint non-goals (not v1 scope)

Windows; notebooks/GUI/mobile; marketplace / remote catalogs; framework zoo;
unlimited MCP/skill catalog; new package manager; coding backlog as program
output; full product implementation as a substitute for an accepted revised plan.

### Product locks (from revised-spec — plan must preserve)

- Hybrid foundry: CLI + Core emit + GitHub template snapshot
- `validate` → `plan` → `generate` (+ optional `generate --plan` bind)
- Exclusive place; closed catalog; custom engine (not Copier runtime)
- Effective verify: CLI > TOML > `default`; default = tooling-sync green (not pytest)
- Generate-time `uv.lock`; `uv sync --locked` in default/strict
- ty Required; fnox+age; no dotenv secrets; AGENTS.md + `.agents/` only; MCP none;
  no Claude adapters
- Kind-qualified catalog UX; scripts archetype emit contract
- Frozen public template cell (cli, profiles `[]`, …)

### Strengths to preserve (from accepted plan-review)

- Continuity with revised-spec PHASE-01..06
- Thin E2E at PHASE-03 / MS-002 before full catalog breadth
- Spike gates (SPK-100..103, SPK-002/050/052)
- Must REQ traceability table
- Explicit residual risk sequencing (ty, fnox, lock, `--plan`)
- No coding backlog; phases/milestones only
- Subordination language to revised specification
- Linear dependency graph (no circular `depends_on`)

## Findings to disposition (must not silently drop)

| FND | Severity | One-line (from accepted review) |
| --- | -------- | ------------------------------- |
| FND-200 | High | Catalog freeze exits before dogfood; rollback reopens PHASE-04 after exit |
| FND-201 | High | PHASE-04 overlarge; single MS-003 hides progressive integration |
| FND-202 | Medium | ty hardened at MS-002 default verify before SPK-002 config gate |
| FND-203 | Medium | MS-004 / MS-005 unordered; hybrid can freeze before dogfood |
| FND-204 | Medium | MS-005 owner attestation unprovable as sole acceptance evidence |
| FND-205 | Medium | Residual-accept of spikes can undercut Must REQ exit honesty |

Review **gate was Conditional**: High findings FND-200..201 should be resolved
(or validly rejected with residual risk) before claiming unblocked catalog freeze
/ hybrid readiness as delivery authority. Prefer **resolving** High findings in
this revision over deferring them.

### Recommended resolution posture (not mandatory; judgment allowed)

The review offered options; pick a **coherent package** and document it:

| FND | Prefer (simplification-friendly) |
| --- | -------------------------------- |
| FND-200 | Early dogfood/Core-alignment **smoke** before MS-003 freeze claim **and/or** provisional freeze until dogfood-informed residual; remove post-exit “still PHASE-04” fiction — reopen/re-gate MS-003 honestly |
| FND-201 | Progressive integration inside PHASE-04 (e.g. ordered MS-003 sub-outcomes or intermediate milestone: full-Core `cli` before all-three-archetype freeze) — still phase/milestone only |
| FND-202 | Distinguish MS-002 “ty runner wired + green on minimal cell” vs SPK-002 “ty config freeze”; dual-gate or SPK-002-lite; **do not** demote ty from default verify |
| FND-203 | Order MS-005 (or dogfood-smoke) **before** MS-004 public hybrid claim |
| FND-204 | MS-005 acceptance = observable CI + surface-separation evidence only; demote attestation to non-gating note |
| FND-205 | Explicit residual policy table: which spikes are hard for which Must REQs; residual-accept cannot substitute for forbidden-path green or ty/fnox demotion (DEC only) |

If you **Reject** a finding, give a concrete rationale tied to locks, simplicity,
or false sequencing claim — not preference alone.

If you **Defer** to a spike, the spike must be bounded (ID, question, exit
criterion, phase gate) and must not leave High findings as silent holes if the
artifact claims delivery authority.

## Finding Disposition Rules

Every `FND-###` receives **exactly one**:

| Disposition | Meaning |
| ----------- | ------- |
| **Accepted** | Integrate the required correction as specified (or the review’s primary option) |
| **Accepted with modification** | Integrate with explicit deltas; note what changed vs the finding’s required correction |
| **Rejected** | Not adopted; rationale required; residual risk if any |
| **Deferred to bounded evidence spike** | Named SPK/phase gate; cannot silently reappear as “fixed” |
| **Not applicable** | Another accepted correction removes the cause; name the superseding fix |

**Silent disappearance of any FND is a defect.**

## Phase and Milestone Rules

- Prefer **edit in place** of proposed-plan PHASE-01..06 / MS-001..MS-006 when
  the subject is the same.
- Progressive milestones (e.g. MS-003a/b or ordered exit bullets) are allowed if
  they remain **phase/milestone** granularity — not task packets.
- Do **not** invent product REQs; cite only.
- Do **not** renumber REQs; plan traces them only.
- Entry/exit criteria must be **observable** and must not depend on later phases
  for claimed freeze durability.
- Preserve thin E2E (PHASE-03 / MS-002) before full catalog breadth unless a
  disposition honestly requires a documented restructure (unlikely).

## Artifact Status Rules

Per contract:

| Status | When to use |
| ------ | ----------- |
| **`Accepted — delivery authority`** | All Critical plan findings resolved or validly rejected; no known implementation-blocking plan finding remains; High findings that block freeze/hybrid/readiness are resolved or validly rejected with explicit residual risk acceptance |
| **`Proposed — delivery blocked`** | Any remaining blocker; list blockers explicitly |

This research stage does **not** auto-make the document “Accepted” in the
**program manifest** — human acceptance of the stage still required. The
**artifact status line** must be **honest** about delivery authority.

Given review gate **Conditional** and zero Critical findings: if you fully
resolve High findings FND-200..201 (and do not leave other blockers), status
**`Accepted — delivery authority`** is appropriate for the artifact. If High
findings remain open, use **`Proposed — delivery blocked`**.

**Note:** Product implementation authority remains the revised specification.
This plan becomes **delivery sequence authority** only — how to build, not what
to build.

## Stage Boundary

### Included

1. One **final revised implementation plan** at the required output path.
2. Revision-specific front matter:
   - Revision Summary
   - Finding Disposition Ledger (all FND-200..205)
   - Integrated Correction Ledger (optional but recommended if helpful)
   - Preserved Strengths
3. Full plan body per `program/contracts/implementation-plan.md` (coherent rewrite
   / integrated edit of the proposed plan — not a delta-only patch file).
4. Executable entry/exit criteria; dependency graph; milestones; dogfood; hybrid;
   spikes; residual policy; rollback triggers; Must REQ traceability.
5. **Final Implementation Handoff** per
   `program/operator/completion-criteria.md` (authoritative spec + plan; whether
   implementation may begin; first safe phase; spikes; vertical slice; dogfood;
   validation evidence; visible risks; reversible decisions; blockers; required
   read set).
6. Honest artifact status and completion checklist.

### Excluded

1. Editing the proposed plan path (`01-…`) — leave it as historical proposed
   artifact.
2. Editing the accepted review (except citing it).
3. Editing the revised specification or inventing product REQs.
4. Product implementation or coding task packets.
5. Reopening Windows, dotenv secrets, Claude adapters, demoting ty/fnox,
   Copier-as-engine without DEC.
6. Starting product coding as this stage’s output.
7. Marking the **stage** `accepted` in the manifest without human process.
8. Feature ideation unrelated to finding disposition.
9. Second plan-review as main work (risk-triggered only after revision if needed).

## Methodology

1. Read **all required inputs completely** — especially the full proposed plan,
   full review, and revised-spec §30–31 / REQs as needed for subordination.
2. Inventory FND-200..205 and draft dispositions **before** rewriting body text.
3. Choose a coherent package of resolutions (especially FND-200..203 together:
   freeze durability, progressive content, ty timing, hybrid/dogfood order).
4. Rewrite the plan as a **standalone whole** with corrections integrated.
5. Complete disposition ledger, preserved strengths, final implementation handoff.
6. Verify no contradictory leftover language from the proposed plan remains
   (especially “fix PHASE-04 after exit” vs durable freeze).
7. Set honest artifact status.
8. Do not mark stage accepted; do not edit upstream accepted artifacts.

## Required Output Structure

Replace the placeholder skeleton entirely. Include at least:

### Revision front matter

1. Artifact Metadata (including revision date, base plan version, review ref,
   delivery status)
2. Revision Summary
3. Finding Disposition Ledger (FND-200..205)
4. Integrated Correction Ledger (recommended)
5. Preserved Strengths
6. Implementation Authority (subordinate to revised-spec v0.2)

### Plan body (standalone delivery sequence)

7. Objectives  
8. Non-Goals  
9. Assumptions  
10. Dependency Graph  
11. Phase Overview  
12. Phases (PHASE-## with entry/exit, spikes, rollback)  
13. Milestones  
14. Cross-Phase Integration  
15. Data or Migration Sequencing  
16. Testing Strategy by Phase  
17. Security Activities by Phase  
18. Operations and Release Readiness  
19. Dogfooding  
20. Risk Register  
21. Open Questions  
22. Rollback and Reconsideration Triggers  
23. Requirement-to-Phase Traceability  
24. Final Implementation Handoff  
25. Definition of Plan Completion  
26. Completion Checklist  

Section numbering may match the skeleton or be renumbered for clarity; all
content themes above must appear.

## Completion Checklist

- [ ] All required plan sections present and non-placeholder
- [ ] Actual revision date recorded
- [ ] Every FND-200..205 dispositioned (exactly one allowed disposition each)
- [ ] No silent finding loss
- [ ] Accepted corrections integrated in body (not ledger-only)
- [ ] Contradictory proposed-plan language removed or reconciled
- [ ] Subordinate to revised-spec v0.2 (no REQ/architecture contradictions)
- [ ] Phases/milestones only — **no** coding backlog or task packets
- [ ] Executable entry/exit criteria (observable evidence)
- [ ] Early thin end-to-end path preserved (or honestly restructured with rationale)
- [ ] Spikes scheduled as gates
- [ ] Dogfooding and hybrid sequencing corrected relative to disposed findings
- [ ] Residual risk / residual-accept policy honest and executable
- [ ] Security, testing, ops addressed by phase
- [ ] Rollback/reconsideration triggers present (no post-exit fiction)
- [ ] Must REQ traceability present
- [ ] Final Implementation Handoff complete per completion-criteria
- [ ] Blueprint non-goals preserved
- [ ] Product locks preserved
- [ ] Strengths preserved (or explicit tradeoff if a finding forces change)
- [ ] Honest artifact status (`Accepted — delivery authority` **or**
      `Proposed — delivery blocked` with blockers listed)
- [ ] Standalone: implementable without chat history
- [ ] Allowed file scope only (revised plan path)
- [ ] No product implementation started as main work
- [ ] Proposed plan (`01-…`) and review not modified

## Allowed File Scope

| Path | Action |
| ---- | ------ |
| `docs/plans/02-implementation-plan-revised.md` | **Write** (primary output; replace placeholder) |
| Other paths | **Read only** |

Do not modify `research-program.toml`, Blueprint, Charter, revised specification,
proposed plan, review, prompts, or handoff package files in the substantive
revision session (validators/humans own status transitions after validation).
