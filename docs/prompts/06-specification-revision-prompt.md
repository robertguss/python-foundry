# Specification Revision Prompt — python-foundry

- **Artifact ID:** PROMPT-06-specification-revision
- **Program:** python-foundry
- **Stage:** `spec-revision` — Revised Definitive Specification
- **Stage kind:** artifact-revision
- **Required inputs:**
  - `docs/00-program-blueprint.md` (Accepted)
  - `docs/01-research-charter.md` (Accepted)
  - `docs/specifications/01-definitive-specification.md` (**Accepted proposed**
    specification v0.1 — base text to revise)
  - `docs/reviews/01-specification-adversarial-review.md` (**Accepted** review;
    findings **FND-001..FND-012** — dispose every one)
  - `docs/reports/01-modern-python-ecosystem.md` (Accepted **v0.2** — full;
    lock provenance)
  - `docs/reports/02-ai-native-agent-workflow.md` (Accepted **v0.2** — full)
  - `docs/reports/03-foundry-architecture.md` (Accepted **v0.1.1** — full)
  - This prompt
  - `docs/handoffs/spec-revision-attachment-manifest.md`
  - `AGENTS.md` (operating rules)
  - `program/contracts/definitive-specification.md` (revision rules + structure)
  - `program/templates/requirement.md` (REQ shape when adding/changing REQs)
  - `program/contracts/authority-and-precedence.md` (as needed)
- **Required output:** `docs/specifications/02-definitive-specification-revised.md`
- **Finding dispositions required:** FND-001..FND-012 (exactly one disposition each)
- **Requirement range:** REQ-001..REQ-299 — **retain** stable IDs where the
  subject remains the same; allocate **new** IDs only from unused numbers
  (proposed spec used sparse IDs through REQ-083; REQ-084..299 available)
- **Depends on (must be accepted):** `spec-review`
- **Revision date:** use the actual calendar date when revision is executed

> Contract: `program/contracts/definitive-specification.md` (including revised
> specification rules).  
> Skeleton outline: `docs/specifications/02-definitive-specification-revised.md`
> (replace placeholder content entirely).

## Role

Act as **Revision Architect** for python-foundry.

You:

- Produce **one coherent revised definitive specification** that is standalone
  and implementation-ready
- **Disposition every** `FND-001..FND-012` with exactly one allowed disposition
- **Integrate** accepted corrections throughout affected sections (not only in a
  ledger)
- **Remove** superseded or contradictory language from the base proposed spec
- **Reconcile** overlapping finding corrections into one consistent design
- **Preserve** important strengths called out in the review
- **Prefer simplification** over new machinery when both satisfy the finding
- **Retain** stable `REQ-###` IDs when the subject remains the same
- Add new REQs only from unused identifiers; do not renumber existing REQs
- Do **not** reopen locked non-goals or User decisions (ty, fnox+age, no dotenv
  secrets, AGENTS.md-only, no Claude adapters) without a DEC path
- Do **not** start implementation planning or product implementation in this
  session

## Mission

Answer:

> What is the **single coherent revised definitive specification** for
> python-foundry that disposes every accepted-review finding, integrates
> corrections into the body of the product law, and can become implementation
> authority if all Critical and implementation-blocking findings are resolved
> or validly rejected?

Produce `docs/specifications/02-definitive-specification-revised.md` as a
**complete standalone** revised specification. Downstream implementation
planning must not need chat history, the proposed-only spec alone, or the
review alone — though those remain citable provenance.

## Authority and Precedence

Apply exactly (highest first):

1. Accepted `DEC-###` records that explicitly supersede earlier authority (none
   expected unless present under `decisions/` at launch).
2. Locked decisions in `docs/00-program-blueprint.md`.
3. Normative methodology in `docs/01-research-charter.md`.
4. **This commissioning prompt**.
5. **This revised specification** (output) — after human acceptance becomes
   **implementation authority** if status warrants.
6. Accepted proposed specification
   (`docs/specifications/01-definitive-specification.md`) — base text; may be
   corrected by dispositions.
7. Accepted adversarial review
   (`docs/reviews/01-specification-adversarial-review.md`) — findings to dispose;
   not automatic law (may Reject with rationale).
8. Accepted focused research reports (evidence + recommendation provenance).
9. Implementation plans — N/A (downstream).
10. `research-program.toml` as operational index only.
11. Model preference (lowest; never load-bearing alone).

Chat history, model memory, and uncommitted notes are **not** authority.
Handoff digests **never** replace full artifacts.

## Locked Context (do not silently undo)

### Blueprint non-goals

Windows; notebooks/GUI/mobile; marketplace / unlimited plugin catalog; framework
zoo; unlimited MCP/skill catalog; new package manager; coding backlog as program
output; full product implementation in this research repo.

### Ecosystem Core locks (v0.2)

Python ≥3.12 / default 3.13; **uv** + lockfile; **src/** (where package-shaped);
Ruff; **ty** Required; pytest; pre-commit Default; **fnox** + **age**; **no
`.env` secrets**; GHA; Typer Default for CLI; profiles `http`, `hooks-hk`,
`data-etl` (or renamed per FND-007 disposition); REC-013 command surface.

### AI-native locks (v0.2)

Root **`AGENTS.md` only**; skills under **`.agents/skills/` only**; MCP default
**none**; no Claude Code adapters as Core emit; amplify REC-013; fnox exec.

### Architecture locks (v0.1.1)

Planner-led CLI **`validate` → `plan` → `generate`**; TOML Project Spec;
plan-as-contract; stage → verify → **exclusive place**; closed catalog; **custom
engine**; GitHub template = **generated snapshot**; emit Core + AI-native as
invariants.

### Strengths to preserve (from accepted review)

Closed Core + closed agent surface; plan-as-contract + exclusive place; User
decisions honored; full REC disposition ledger (carry forward); hybrid template
with single SoT; non-interactive first; forbidden-path discipline.

## Findings to disposition (must not silently drop)

| FND | Severity | One-line (from accepted review) |
| --- | -------- | ------------------------------- |
| FND-001 | High | TOML vs CLI `verify` precedence undefined |
| FND-002 | High | Profile apply order: catalog vs TOML array contradiction |
| FND-003 | High | `uv.lock` emit lacks generate-time truth rules |
| FND-004 | High | Plan-as-contract does not bind generate to inspected plan |
| FND-005 | Medium | Default verify vs “runnable” / pytest DoD overclaim |
| FND-006 | Medium | Strict pre-commit assumes git/hooks environment |
| FND-007 | Medium | `data-etl` dual archetype/profile identity |
| FND-008 | Medium | `scripts` archetype emit/tests/lock under-specified |
| FND-009 | Medium | `plan_sha256` canonicalization algorithm missing |
| FND-010 | Medium | Public GitHub template Project Spec inputs not frozen |
| FND-011 | Low | Stage naming/retention/collision semantics incomplete |
| FND-012 | Low | Machine-readable error taxonomy under-specified |

Review **gate was Conditional**: High findings should be resolved (or validly
rejected with residual risk) before claiming unblocked generate/emit freeze.
Prefer **resolving** High findings in this revision over deferring them.

### Recommended resolution posture (not mandatory; judgment allowed)

The review offered options; pick coherent designs and document them:

| FND | Prefer (simplification-friendly) |
| --- | -------------------------------- |
| FND-001 | Explicit precedence: CLI overrides TOML when present; else TOML; else `default`; record effective mode + source in plan |
| FND-002 | Membership from TOML set; **apply order = catalog order**; array order ignored (or hard-fail if not catalog-sorted — pick one) |
| FND-003 | Freeze a lock lifecycle (regenerate at generate, or closed matrix only, or forbid off-matrix `python_version`) — must be total |
| FND-004 | Prefer binding path: optional/normative `generate --plan` with digest mismatch hard-fail; **or** honestly demote two-command trust language — do not leave false advertising |
| FND-005 | Align vocabulary: default success ≠ pytest green; document tier meanings |
| FND-006 | Define strict pre-commit prerequisites or drop pre-commit from pre-place strict |
| FND-007 | Rename one id **or** qualified catalog UX + docs; do not leave bare dual id without mitigation |
| FND-008 | Normative scripts emit inventory + test/lock policy by archetype |
| FND-009 | Freeze canonicalization (e.g. sorted-key UTF-8 JSON + SHA-256 hex) + test vector |
| FND-010 | Freeze public template Project Spec cell in § hybrid |
| FND-011 | Stage naming, collision, failure path MUST in errors |
| FND-012 | Minimal JSON error taxonomy for plan/generate failures |

If you **Reject** a finding, give a concrete rationale tied to locks or
simplicity — not preference alone.

If you **Defer** to a spike, the spike must be bounded (ID, question, exit
criterion, phase gate) and must not leave High findings as silent holes if the
artifact claims implementation authority.

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

## Requirement Rules

- Prefer **edit in place** existing REQs when the subject is the same.
- New REQs only from **unused** IDs (e.g. REQ-084+).
- Never reuse IDs for different subjects.
- Must REQs need verification paths.
- Update **traceability** for new/changed REQs.
- Carry forward the **Recommendation Disposition Ledger** (REC-001..014,
  100..112, 200..212) unless a finding forces an honest delta — do not re-open
  tool selection.

## Artifact Status Rules

Per contract:

| Status | When to use |
| ------ | ----------- |
| **`Accepted — implementation authority`** | All Critical findings resolved or validly rejected; no known blocking contradiction; High findings that block generate/emit are resolved or validly rejected with explicit residual risk acceptance |
| **`Proposed — implementation blocked`** | Any remaining blocker; list blockers explicitly |

This research stage does **not** auto-make the document “Accepted” in the
**program manifest** — human acceptance of the stage still required. The
**artifact status line** must be **honest** about product implementation
authority.

Given review gate **Conditional** and zero Critical findings: if you fully
resolve High findings FND-001..004 (and do not leave other blockers), status
**`Accepted — implementation authority`** is appropriate for the artifact.
If High findings remain open, use **`Proposed — implementation blocked`**.

## Stage Boundary

### Included

1. One **revised definitive specification** at the required output path.
2. Revision-specific front matter:
   - Revision Summary
   - Finding Disposition Ledger (all FND-001..012)
   - Integrated Correction Ledger
   - Preserved Strengths
3. Full software-first specification body (coherent rewrite / integrated edit of
   the proposed spec — not a delta-only patch file).
4. Updated REC disposition ledger (carry; note deltas if any).
5. Risk register, open questions, deferred/rejected work updated for residual
   risk from dispositions.
6. High-level phases (PHASE-##) updated if findings change gates.
7. Updated implementation handoff (for downstream implementation-plan stage).
8. Honest artifact status and completion checklist.

### Excluded

1. Editing the proposed specification path (`01-…`) — leave it as historical
   proposed artifact.
2. Editing the accepted review (except citing it).
3. Implementation plan detail beyond high-level phases/milestones.
4. Product implementation or coding task packets.
5. Reopening Windows, dotenv secrets, Claude adapters, demoting ty/fnox,
   Copier-as-engine without DEC.
6. Starting `implementation-plan` or plan-review in this session.
7. Marking the **stage** `accepted` in the manifest without human process.
8. Feature ideation unrelated to finding disposition.

## Methodology

1. Read **all required inputs completely** — especially the full proposed spec
   and full review.
2. Inventory FND-001..012 and draft dispositions **before** rewriting body text.
3. Choose a coherent package of resolutions (especially FND-001..004 together).
4. Rewrite the specification as a **standalone whole** with corrections
   integrated (prose, REQs, tables, examples, phases).
5. Complete disposition ledger, integrated correction ledger, preserved
   strengths, handoff.
6. Verify no contradictory leftover language from the proposed spec remains.
7. Set honest artifact status.
8. Do not mark stage accepted; do not edit upstream accepted artifacts.

## Required Output Structure

Replace the placeholder skeleton entirely. Include at least:

### Revision front matter

1. Artifact Metadata (including revision date, base spec version, review ref)
2. Revision Summary
3. Finding Disposition Ledger (FND-001..012)
4. Integrated Correction Ledger
5. Preserved Strengths

### Specification body (standalone product law)

6. Executive Decision Summary  
7. Authority and Intended Use  
8. Problem and Product Definition  
9. Goals and Non-Goals  
10. Locked Decisions and Invariants  
11. Final Technology Stack  
12. System Context  
13. Architecture  
14. Components and Boundaries  
15. Data Model  
16. Interfaces and Integrations  
17. User Workflows  
18. Security and Privacy  
19. Reliability and Operations  
20. Testing and Verification  
21. CI and Release  
22. Migration  
23. Performance Expectations  
24. Internal Contracts  
25. Dependency Bill of Materials  
26. Normative Requirements (`REQ-###`)  
27. Traceability  
28. Risk Register  
29. Open Questions  
30. Deferred Work  
31. Rejected Work  
32. Recommendation Disposition Ledger (carry RECs)  
33. Definition of Done  
34. High-Level Implementation Phases  
35. Updated Implementation Handoff  
36. Completion Checklist  

Section numbering may match the skeleton or be renumbered for clarity; all
content themes above must appear.

## Completion Checklist

- [ ] All required sections present and non-placeholder
- [ ] Actual revision date recorded
- [ ] Every FND-001..012 dispositioned (exactly one allowed disposition each)
- [ ] No silent finding loss
- [ ] Accepted corrections integrated in body (not ledger-only)
- [ ] Contradictory proposed-spec language removed or reconciled
- [ ] Stable REQ IDs retained where subject unchanged; new IDs only from unused
- [ ] Must REQs have verification paths
- [ ] Traceability updated
- [ ] REC disposition ledger carried (deltas noted if any)
- [ ] Blueprint locks and non-goals preserved
- [ ] Ecosystem / AI-native / architecture locks preserved
- [ ] Strengths preserved (or explicit tradeoff if a finding forces change)
- [ ] Honest artifact status (`Accepted — implementation authority` **or**
      `Proposed — implementation blocked` with blockers listed)
- [ ] High-level phases present; **no** granular coding backlog
- [ ] Standalone: implementable without chat history
- [ ] Updated implementation handoff complete
- [ ] Allowed file scope only (revised specification path)
- [ ] No downstream stage started (no implementation plan as main work)
- [ ] Proposed spec (`01-…`) and review not modified

## Allowed File Scope

| Path | Action |
| ---- | ------ |
| `docs/specifications/02-definitive-specification-revised.md` | **Write** (primary output; replace placeholder) |
| Other paths | **Read only** |

Do not modify `research-program.toml`, Blueprint, Charter, reports, proposed
spec, review, prompts, or handoff package files in the substantive revision
session (validators/humans own status transitions after validation).
