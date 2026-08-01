# Specification Adversarial Review Prompt — python-foundry

- **Artifact ID:** PROMPT-05-specification-adversarial-review
- **Program:** python-foundry
- **Stage:** `spec-review` — Specification Adversarial Review
- **Stage kind:** adversarial-review
- **Required inputs:**
  - `docs/00-program-blueprint.md` (Accepted)
  - `docs/01-research-charter.md` (Accepted)
  - `docs/specifications/01-definitive-specification.md` (**Accepted proposed**
    specification — synthesis complete; status may still read “Proposed —
    pending adversarial review”)
  - `docs/reports/01-modern-python-ecosystem.md` (Accepted **v0.2** — full)
  - `docs/reports/02-ai-native-agent-workflow.md` (Accepted **v0.2** — full)
  - `docs/reports/03-foundry-architecture.md` (Accepted **v0.1.1** — full)
  - This prompt
  - `docs/handoffs/spec-review-attachment-manifest.md`
  - `AGENTS.md` (operating rules)
  - `program/contracts/adversarial-review.md`
  - `program/templates/finding.md`
  - `program/contracts/authority-and-precedence.md` (as needed)
  - `program/contracts/definitive-specification.md` (as needed for shape checks)
- **Required output:** `docs/reviews/01-specification-adversarial-review.md`
- **Finding range:** FND-001..FND-199
- **Depends on (must be accepted):** `synthesis`
- **Review date:** use the actual calendar date when review is executed

> Contract: `program/contracts/adversarial-review.md`.  
> Finding template: `program/templates/finding.md`.  
> Skeleton outline: `docs/reviews/01-specification-adversarial-review.md`
> (replace placeholder content entirely).

## Role

Act as an **adversarial reviewer** of the proposed definitive specification.

You:

- **Attack** polished sections; do not polish them further
- Find what is wrong, contradictory, unsafe, non-total, under-specified,
  over-engineered, unprovable, hard to implement, hard to test, or likely to
  fail in real use
- Produce a **small number of strong findings** rather than meeting a quota
- Prefer concrete failure scenarios and required corrections over vague critique
- **Do not add features** or invent attractive subsystems
- **Do not** treat preference, taste, or “nice to have” as defects
- **Do not** revise the specification in this stage (review only)
- **Do not** reopen locked non-goals or User decisions without framing them as
  **findings about consistency/risk** — not as license to reverse locks

## Mission

Answer:

> What is wrong with the **accepted proposed definitive specification** such
> that revision must correct it before implementation authority — covering
> contradictions, missing REQs, weak verification, unsafe write/security
> semantics, non-total workflows, over-engineering, and silent expansion paths?

Produce `docs/reviews/01-specification-adversarial-review.md` as a **complete
standalone** adversarial review. Downstream revision must be able to dispose
every `FND-###` without chat history.

## Authority and Precedence

Apply exactly (highest first):

1. Accepted `DEC-###` records that explicitly supersede earlier authority (none
   expected unless present under `decisions/` at launch).
2. Locked decisions in `docs/00-program-blueprint.md`.
3. Normative methodology in `docs/01-research-charter.md` (evidence vocabulary,
   quality bar, anti-patterns).
4. **This commissioning prompt**.
5. The **proposed definitive specification** under review
   (`docs/specifications/01-definitive-specification.md`) — attack surface, not
   yet implementation authority.
6. Accepted focused research reports (evidence + recommendation provenance for
   lock/provenance checks):
   - `docs/reports/01-modern-python-ecosystem.md` (v0.2)
   - `docs/reports/02-ai-native-agent-workflow.md` (v0.2)
   - `docs/reports/03-foundry-architecture.md` (v0.1.1)
7. This review (output of this stage) — proposals for revision, not product law.
8. Implementation plans — N/A (downstream).
9. `research-program.toml` as operational index only.
10. Model preference (lowest; never load-bearing alone).

Chat history, model memory, and uncommitted notes are **not** authority.
Handoff digests **never** replace full reports or the full specification.

**Important:** Locks and User decisions (ty Required, fnox+age, no dotenv
secrets, AGENTS.md-only, no Claude adapters, plan-as-contract, exclusive place,
closed catalog, custom engine, macOS+Linux only) are **not** defects merely
because a reviewer prefers alternatives. Attack **implementation risk,
inconsistency with REQs, under-specification, or false confidence** around those
locks — do not reverse them as product scope.

## Locked Context (do not silently undo via “findings”)

### Blueprint non-goals (not v1 scope)

Windows; notebooks/GUI/mobile; marketplace / unlimited plugin catalog; framework
zoo; unlimited MCP/skill catalog; new package manager; coding backlog as program
output; full product implementation in this research repo.

### Ecosystem Core locks (v0.2)

Python ≥3.12 / default 3.13; **uv** + lockfile; **src/**; Ruff; **ty** Required;
pytest; pre-commit Default; **fnox** + **age**; **no `.env` secrets**; GHA;
Typer Default for CLI; profiles `http`, `hooks-hk`, `data-etl`; REC-013 command
surface.

### AI-native locks (v0.2)

Root **`AGENTS.md` only**; skills under **`.agents/skills/` only**; MCP default
**none**; no Claude Code adapters as Core emit; amplify REC-013; fnox exec
secrets protocol.

### Architecture locks (v0.1.1)

Planner-led CLI **`validate` → `plan` → `generate`**; TOML Project Spec;
plan-as-contract; stage → verify → **exclusive place**; closed catalog; **custom
engine** (not Copier runtime); GitHub template = **generated snapshot**; emit
Core + AI-native surfaces as invariants.

### Spec handoff attack list (seed; not exhaustive)

From specification §30.1 — use as starting attack surface, not as a checklist
that limits findings:

1. Missing REQs for load-bearing behaviors (plan equality, forbidden paths,
   verify abort).
2. Contradictions between emit contracts and CLI defaults.
3. Under-specified or over-specified TOML fields.
4. `quality-gates` skill necessity vs AGENTS.md-only (REC-103 tension).
5. Residual risk acceptance for ty/fnox vs implementation sequencing.
6. Phase boundaries: foundational work deferred without spike.
7. Provisional CLI name `foundry` collisions / branding.
8. `data-etl` as both archetype and profile names.
9. Lockfile policy edge cases (e.g. workspaces).
10. Silent expansion paths (plugins, MCP, Claude “just one file”).

### Strengths to preserve (do not “find” them away)

Closed Core + closed agent surface; plan-as-contract + exclusive place; User
decisions honored; full REC disposition ledger; hybrid template with single SoT.

### Validation advisory notes (non-authoritative; may inspire findings)

From synthesis validation (advisory only):

- REC-103 Accepted with modification (data-etl skill = `add-script`)
- Provisional CLI name `foundry` (OQ-105)
- `data-etl` dual naming
- Sparse REQ numbering is intentional (not missing disposals)
- Residual RSK-002 (ty) and RSK-007/050 (fnox/dotenv)

## Stage Boundary

### Included

1. One **adversarial review** at the required output path.
2. Full structure per this prompt (metadata through completion checklist).
3. Findings **`FND-001..FND-199`** as needed (use only what is justified; leave
   unused IDs unallocated — never invent padding findings).
4. Each finding uses `program/templates/finding.md` fields (severity, confidence,
   problem, evidence, failure scenario, impact, root cause, required correction,
   proposed specification diff, acceptance evidence, alternatives, residual risk,
   related findings).
5. **Executive assessment** and **implementation gate** recommendation
   (Open | Conditional | Blocked) with rationale.
6. **Cross-cutting issues** (themes spanning multiple findings or sections).
7. Whether an **additional review round** is recommended under risk-triggered
   policy (`program/contracts/adversarial-review.md`) — not automatic.
8. Honest completion checklist.

### Excluded

1. Revising the definitive specification (downstream `spec-revision`).
2. Writing or starting the implementation plan (downstream).
3. Reopening Windows, notebooks, marketplace, framework zoo, dotenv secrets,
   Claude adapters, demoting ty/fnox, or Copier-as-engine as product scope
   (unless framed only as **risk/inconsistency** findings with required
   correction short of scope reversal — e.g. document residual risk better).
4. Feature ideation disguised as defects.
5. New focused research tracks or re-running tool selection.
6. Product implementation or coding task packets.
7. Editing Blueprint, Charter, accepted reports, specification, or this prompt.
8. Marking this stage `accepted` or inventing DEC records without human process.
9. Starting `spec-revision`, `implementation-plan`, or any later stage.

## Review Method

1. Read **all required inputs completely** — full Blueprint, Charter,
   specification, three reports, contracts, this prompt, attachment manifest.
2. Inventory load-bearing REQs, locks, phases, risks, open questions, and REC
   dispositions before drafting findings.
3. Attack with software-first scope
   (`program/contracts/adversarial-review.md`):
   - Product scope and non-goals honesty
   - Requirements completeness and testability
   - Architecture and data/interfaces consistency
   - User workflows end-to-end (happy path + failure)
   - Security, filesystem, determinism, dependencies
   - Testing, CI, operations, migration
   - Implementation phases and agent legibility
   - Framework creep / silent expansion
   - Acceptance criteria that do not prove outcomes
4. Trace **end-to-end workflows**: validate → plan → generate; exclusive place;
   verify abort; agent definition-of-done; GitHub template snapshot path.
5. Check **failure, cancellation, rollback, cleanup** (stage dirs, partial
   writes, non-empty dest, verify fail).
6. Check **consistency** across prose, REQs, tables, examples, appendices,
   disposition ledger, and phases.
7. Attempt to **delete unnecessary machinery** (if under-justified complexity is
   a defect, say so; do not invent replacements).
8. Prefer **strong findings** with concrete failure scenarios. Merge weak nits
   into Low severity or drop them.
9. Do **not** mark stage accepted; do not edit the specification.

## Severity Guide

| Level | Meaning |
| ----- | ------- |
| **Critical** | Blocks all implementation or risks catastrophic harm |
| **High** | Blocks the affected phase or creates major invalid behavior |
| **Medium** | Must be fixed before the affected phase completes |
| **Low** | Should be corrected in revision; does not block early work |

Every finding must state whether it **blocks implementation**: Entire program |
Named phase | No.

## Finding Rules

- Allocate only **FND-001..FND-199**; never reuse IDs; do not use plan-review
  range FND-200..FND-399.
- One finding = one coherent defect theme (may list multiple affected REQs).
- **Required Correction** must be actionable for `spec-revision` (what to change
  in the specification — not code patches).
- **Proposed Specification Diff** may be prose section/REQ-level (“add REQ for
  …”, “reconcile §X with REQ-Y”) — not a full rewritten specification.
- **Acceptance Evidence** = how revision proves the finding is addressed.
- Cite evidence from the specification (and reports for provenance) with section
  or REQ IDs. Prefer portable references over chat claims.
- Preference-as-defect is invalid. “I would use X instead of ty” is not a finding
  unless the **spec is inconsistent or unsafe** about ty.

## Required Output Structure

Replace the placeholder skeleton entirely. Include at least:

1. **Artifact Metadata** (program, stage, subject path, version reviewed,
   review date, finding range used, gate recommendation summary)
2. **Review Scope and Method** (what was read; attack method; explicit
   out-of-scope)
3. **Executive Assessment** (overall quality; top risks; preserve strengths)
4. **Findings** — one `## FND-### — Title` section per finding (template fields)
5. **Cross-Cutting Issues**
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
- [ ] Findings use only FND-001..FND-199; no out-of-range IDs; no silent reuse
- [ ] Each finding has severity, failure scenario, required correction
- [ ] No feature ideation disguised as defects
- [ ] Preference-as-defect avoided; locks not silently reversed
- [ ] Spec §30.1 attack seeds considered (addressed or explicitly N/A)
- [ ] Strengths to preserve acknowledged (not “fixed away”)
- [ ] Implementation gate recommendation present and consistent with severities
- [ ] Additional review round recommendation present
- [ ] Finding index table complete
- [ ] Allowed file scope only (review path)
- [ ] Specification not modified
- [ ] No downstream stage started (no revised specification content as main work)

## Allowed File Scope

| Path | Action |
| ---- | ------ |
| `docs/reviews/01-specification-adversarial-review.md` | **Write** (primary output; replace placeholder) |
| Other paths | **Read only** |

Do not modify `research-program.toml`, Blueprint, Charter, reports,
specification, prompts, or handoff package files in the substantive review
session (validators/humans own status transitions after validation).
