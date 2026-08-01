# Implementation Plan Adversarial Review — python-foundry

- **Artifact type:** Adversarial review
- **Program:** python-foundry
- **Stage:** `plan-review`
- **Status:** Complete — pending independent validation and human acceptance
- **Version:** 0.1
- **Created / review date:** 2026-08-01
- **Last updated:** 2026-08-01
- **Subject:** `docs/plans/01-implementation-plan.md` (v0.1, Proposed — pending plan adversarial review; stage-accepted; **not** delivery authority)
- **Implementation authority:** `docs/specifications/02-definitive-specification-revised.md` v0.2 (accepted; commit `faffbdc`)
- **Commissioning prompt:** `docs/prompts/08-implementation-plan-review-prompt.md`
- **Finding range allocated:** FND-200..FND-399
- **Findings used:** FND-200..FND-205
- **Implementation gate (summary):** **Conditional**
- **Depends on:** Accepted implementation plan stage (`implementation-plan`, `ab728951a52c1d69cc30e6151034d2af256bed5b`)

> Contract: `program/contracts/adversarial-review.md` (implementation-plan review attacks).  
> Finding template: `program/templates/finding.md` (**Proposed Plan Diff** in place of specification diff).  
> Plan contract: `program/contracts/implementation-plan.md`.

---

## 1. Artifact Metadata

| Field | Value |
| ----- | ----- |
| Program ID | python-foundry |
| Stage ID | `plan-review` |
| Reviewer posture | Adversarial (sequencing / delivery safety; no product redesign) |
| Subject status at review | Proposed — pending plan adversarial review (stage accepted; not delivery authority) |
| Subject version | 0.1 |
| Plan date | 2026-08-01 |
| Phase / milestone surface | PHASE-01..06; MS-001..MS-006 |
| REQ surface (cited only) | REQ-001..REQ-091 as traced in plan §19 |
| DEC records at review | None under `decisions/` |
| Finding IDs used | FND-200, FND-201, FND-202, FND-203, FND-204, FND-205 |
| Gate recommendation | **Conditional** — plan-revision must dispose High findings before delivery authority |

---

## 2. Review Scope and Method

### 2.1 Scope

Adversarial review of the **accepted proposed implementation plan** for:

- Circular or ambiguous phase dependencies; exit criteria that depend on later phases
- Missing prerequisites for claimed exit evidence
- Overlarge phases; milestones without integration / observable acceptance evidence
- Acceptance or exit criteria that do not prove claimed outcomes
- Late residual-risk discovery (ty, fnox/dotenv, lock network, `--plan` bind)
- Delayed dogfooding / hybrid template vs catalog breadth
- Thin E2E honesty (PHASE-03 / MS-002 claim)
- Security / testing / ops gaps by phase; weak or circular rollback triggers
- Phase boundaries vs revised-spec §30–31 / REQ phase tags
- Plan steps that reinterpret architecture or REQ semantics
- Order that hardens wrong decisions before spikes
- Coding-backlog creep disguised as milestones
- Unexecutable “readiness” (MS-006 / residual-accept theater)

**Not in scope:** product taste; reverse of locks (ty Required, fnox+age, no dotenv secrets, AGENTS.md-only, no Claude, exclusive place, closed catalog, custom engine, generate-time `uv.lock`, verify CLI > TOML > default, optional `--plan` bind); reopening Blueprint non-goals; coding backlog; plan or spec rewrite in this stage.

### 2.2 Method

1. Read Blueprint, Charter, commissioning prompt, attachment manifest, adversarial-review contract, finding template, implementation-plan contract, authority ladder, AGENTS.md.
2. Read full proposed plan v0.1 (metadata through completion checklist).
3. Read revised definitive specification v0.2 with focus on REQs, §16.3 spikes, §24 risks, §29.2 product DoD, §30 handoff, §31 phases.
4. Inventory dependency graph, phase entry/exit, milestones, spike gates, dogfood, hybrid path, rollback, REQ→phase table.
5. Trace delivery path: pure pipeline → fs → thin generate → catalog breadth → hybrid/dogfood → harden.
6. Apply implementation-plan review attacks; prefer strong findings with failure scenarios; drop preference-as-defect.

### 2.3 Explicit out of scope for this review

- Revising the implementation plan (downstream `plan-revision`)
- Revising the definitive specification or inventing REQs
- Product implementation / PHASE-01 coding
- Feature ideation; stack preference; branding as architecture
- Marking stages accepted; inventing DECs

### 2.4 Plan-review attack seeds (disposition)

| Seed | Disposition in this review |
| ---- | -------------------------- |
| Circular / ambiguous phase depends_on | Graph is linear 01→06 — **N/A as graph cycle**; **FND-200** covers post-exit reopen (exit durability) |
| Missing prerequisites for exit evidence | Covered under **FND-201**, **FND-202**, **FND-205** |
| Overlarge phases | **FND-201** (PHASE-04) |
| Milestones without integration evidence | **FND-201**, **FND-203**, **FND-204** |
| Acceptance/exit that do not prove outcomes | **FND-204**, **FND-205**; MS-006 largely OK |
| Late residual risk discovery | **FND-202** (ty); fnox/lock/`--plan` sequencing mostly honest |
| Delayed dogfooding / hybrid | **FND-200**, **FND-203** |
| Thin E2E too late vs PHASE-03 claim | **N/A** — MS-002 / PHASE-03 claim is honest (strength) |
| Security/test/ops gaps; weak rollback | **FND-200** (reopen), **FND-205** (residual-accept); otherwise present |
| Phase boundaries vs §30–31 / REQ tags | Continuity preserved; no contradiction finding |
| Plan reinterprets architecture/REQs | **N/A** as defect — subordination language holds |
| Order hardens wrong decisions before spikes | **FND-202**, **FND-201** |
| Coding-backlog creep | **N/A** — phases/milestones only (strength) |
| MS-006 / readiness theater | Partially **FND-205**; MS-006 not elevated alone |
| Provisional CLI name as blocker | **N/A** — correctly non-blocking |

---

## 3. Executive Assessment

The proposed plan is a **coherent, lock-faithful delivery sequence** subordinate to revised-spec v0.2. It preserves PHASE-01..06 continuity, places **thin E2E at PHASE-03 / MS-002** before catalog breadth, schedules spikes as gates, traces Must REQs, sequences residual risks (ty, fnox, lock network, plan-bind), and correctly refuses coding backlog and product-law rewrite. Locks (ty, fnox+age, AGENTS-only, exclusive place, custom engine, closed catalog, generate-time lock, verify precedence, optional `--plan`) are not quietly reversed.

**Primary failure modes are sequencing durability and freeze timing — not wrong architecture:**

1. **Catalog “freeze” exits PHASE-04 before dogfood can falsify Core emit**, then rollback language reopens PHASE-04 after exit (**FND-200**).
2. **PHASE-04 is a single all-or-nothing content freeze** (three archetypes + Core + AI-native + four spikes) without progressive integration milestones (**FND-201**).
3. **ty is already part of MS-002 default-verify success** while **SPK-002** (practical ty config / maturity) is only a PHASE-04 freeze gate (**FND-202**).
4. **Hybrid snapshot (MS-004) and product dogfood (MS-005) are unordered** inside PHASE-05 (**FND-203**).
5. **MS-005 acceptance leans on owner attestation** rather than fully observable Core-alignment evidence (**FND-204**).
6. **PHASE-04 residual-accept of spikes** can undercut Must REQ honesty without a hard residual policy (**FND-205**).

No **Critical** finding is justified: nothing forces catastrophic secret leakage by design, Windows/marketplace creep, or demotion of locked tools. Early pure-pipeline work (PHASE-01) and filesystem work (PHASE-02) can proceed under owner risk; **catalog freeze, hybrid public claim, and v1 readiness must not treat the proposed plan as delivery authority until plan-revision disposes High findings.**

**Strengths to preserve in plan-revision:** linear phase graph; thin E2E before breadth; SPK-100..103 and SPK-002/050/052 placement intent; Must REQ table; residual risk register with no dotenv/Claude fallback; subordination to revised spec; no coding backlog; honest “proposed not delivery authority” status.

---

## 4. Findings

## FND-200 — Catalog freeze exits before dogfood can falsify Core; rollback reopens PHASE-04 after exit

- **Severity:** High
- **Confidence:** High
- **Category:** Sequencing / dogfooding / exit durability
- **Affected sections:** Plan §6–§8 (PHASE-04 exit, PHASE-05 scope/rollback), §9 (MS-003, MS-005), §15 Dogfooding, §18 Rollback
- **Affected requirements:** REQ-001, REQ-050..078 (emit), REQ-076 (foundry vs Generated surfaces)
- **Affected phases:** PHASE-04, PHASE-05
- **Blocks implementation:** Named phase (PHASE-04 content freeze claim; PHASE-05 hybrid “done”)

### Problem

PHASE-04 exit and MS-003 claim a **complete** closed-catalog emit contract (all three archetypes, Core, AI-native, forbidden paths) **before** any primary dogfood of the foundry product on Core conventions (MS-005 / PHASE-05). When dogfood later shows Core emit unusable for foundry itself, the plan’s own rollback says to “fix catalog in **PHASE-04 scope**” — i.e. the prior phase **exit was not durable**. That is an exit criterion that depends on later-phase evidence.

### Evidence

- Plan §6: PHASE-04 → PHASE-05 only after “Full archetype goldens + forbidden-path conformance; dogfood inputs ready.”
- Plan PHASE-04 exit: MS-003 all three archetypes + spikes/forbidden paths; dogfood “full foundry-repo dogfood PHASE-05.”
- Plan PHASE-05 rollback: “Dogfood reveals Core emit unusable for foundry itself → fix catalog in PHASE-04 scope before calling hybrid ‘done’; do not invent a second Core.”
- Plan §15: primary dogfood gate is PHASE-05 / MS-005; PHASE-03 only “one real minimal generate.”
- Revised-spec §29.2 product DoD and §31 PHASE-05 both expect dogfood; they do **not** require dogfood *after* an irreversible catalog freeze — the plan over-claims freeze durability.

### Failure Scenario

1. Team exits PHASE-04 with green goldens for `cli` / `scripts` / `data-etl` on fixture trees.
2. PHASE-05 dogfood applies Core gates (uv locked sync, ruff, ty, pytest, AGENTS discipline) to the foundry product repo.
3. Core emit proves painful or wrong for a real application-shaped uv project (layout, ty config, skill surface, CI, research-skill leakage).
4. Catalog and goldens must change after MS-003 was declared complete; hybrid snapshot work may already have started; “PHASE-04 done” becomes fiction and schedules thrash.

### Impact

False confidence at MS-003; rework of frozen content and hybrid path; delayed discovery of the highest-value integration risk (foundry-as-Core consumer).

### Root Cause

Dogfood is sequenced only as a late hybrid-phase gate, while catalog **freeze language** treats PHASE-04 exit as content-complete. Rollback acknowledges the coupling but does not make exit criteria depend on it honestly.

### Required Correction

In plan-revision, make catalog freeze **durable** relative to dogfood without inventing product REQs. At least one of:

1. **Early dogfood smoke (preferred):** After MS-002 (or early in PHASE-04 before multi-archetype freeze), require foundry-product Core *tooling* alignment smoke (product CI: locked sync + ruff + ty + pytest; product AGENTS surface rules without shipping research skills into Generated emit) as a named prerequisite to MS-003 freeze; and/or  
2. **Provisional freeze:** State explicitly that MS-003 / PHASE-04 exit is **content-complete only after** a dogfood-informed residual check (or that MS-003 blocks public hybrid claim until MS-005 smoke), and remove language that treats PHASE-04 exit as irreversible freeze while PHASE-05 can “reopen PHASE-04 scope”; and/or  
3. **Ordered PHASE-05:** Require dogfood evidence that can falsify Core *before* declaring hybrid snapshot “done” (see also FND-203).

Do **not** reverse locks or demote ty/fnox to “make dogfood work.”

### Proposed Plan Diff

- §6 dependency notes / §8 PHASE-04 exit / §9 MS-003: add dogfood-smoke prerequisite or provisional-freeze wording.
- §8 PHASE-05 rollback: replace “fix in PHASE-04 scope after exit” with explicit reopen/re-gate of MS-003 (or a named content-freeze milestone) when dogfood falsifies Core.
- §15: align “dogfood before broad expansion” with closed-catalog reality — at least smoke before multi-archetype freeze.

### Acceptance Evidence

Revised plan shows either (a) observable dogfood/Core-alignment evidence before MS-003 freeze claim, or (b) MS-003 explicitly provisional until dogfood/hybrid residual, with no post-exit “still PHASE-04” fiction. No Must REQ residual-accepted solely because dogfood was late.

### Alternatives Considered

Keep dogfood only at PHASE-05 as in §31 naming — rejected as **sole** freeze gate because freeze durability fails. Move all of PHASE-04 after dogfood — overcorrects and conflicts with needing emit content to dogfood against.

### Residual Risk

Owner may still skip early smoke; mitigated by making it a hard MS-003 prerequisite in the revised plan.

### Related Findings

FND-201 (PHASE-04 size), FND-203 (MS-004/005 order), FND-204 (MS-005 evidence quality).

---

## FND-201 — PHASE-04 is overlarge: single MS-003 exit hides non-integrable breadth

- **Severity:** High
- **Confidence:** High
- **Category:** Overlarge phase / integration evidence
- **Affected sections:** Plan §7–§8 PHASE-04, §9 MS-003, §10 Cross-Phase Integration, §12 Testing
- **Affected requirements:** REQ-050..078, REQ-087, REQ-088, REQ-085 (lock matrix)
- **Affected phases:** PHASE-04
- **Blocks implementation:** Named phase (PHASE-04 exit / MS-003 as sole content gate)

### Problem

PHASE-04 packages **full Core toolchain**, **three archetypes**, **all profiles**, **AI-native emit contracts**, **forbidden-path suite**, **kind-qualified UX completion**, **generate-time lock matrix**, and **four spike gates** (SPK-002, SPK-050, SPK-052, SPK-102) under **one** milestone (MS-003) and one phase exit. There is no intermediate integration milestone that proves a full-Core `cli` cell before scripts/data-etl breadth. Failures late in the phase invalidate the whole freeze with no partial durable gate.

### Evidence

- Plan PHASE-04 objective/scope: “Flesh the closed catalog to full v1 Core, archetypes, profiles, and AI-native…; gate on ty/fnox/agent-surface spikes before freeze.”
- Plan §9 MS-003: sole content milestone — “all three archetypes golden emit”; prerequisites list SPK-002, SPK-052, SPK-102, and SPK-050 for agent claims.
- Plan §12: PHASE-04 e2e = “generate ×3 archetypes” in one testing cell; no progressive MS between minimal-cell lifecycle (MS-002) and full triple freeze.
- Revised-spec §31 also names a single PHASE-04 / MS-003 — the plan was allowed to refine with executable entry/exit; it did not add progressive integration evidence inside that boundary.

### Failure Scenario

1. Full-Core `cli` is nearly green; scripts inventory (REQ-088) and data-etl composition fight path-collision / profile order issues.
2. SPK-050 multi-agent skill surface fails while emit inventories look green.
3. Team either (a) holds the entire phase open for months with no durable “cli Core done” claim, or (b) softens exit via residual-accept (FND-205) and freezes incomplete agent surface.
4. PHASE-05 hybrid freezes the public `cli` cell while scripts/data-etl remain half-integrated — continuous-integration rule violated in practice.

### Impact

Big-bang content integration; schedule opacity; pressure to residual-accept Must-adjacent work; hybrid and dogfood start on an unclear freeze.

### Root Cause

Indicative MS-003 from the spec was expanded into full freeze without intermediate **phase-local** integration milestones (still phase/milestone granularity — not a coding backlog).

### Required Correction

In plan-revision, keep PHASE-04 as the content phase (do not invent architecture phases) but add **progressive integration gates**, for example:

- **MS-003a** (or equivalent wording under MS-003): full-Core `cli` + empty profiles golden + default verify e2e + forbidden-path on that cell + SPK-002/052 as applicable to Core secrets/ty.
- **MS-003b:** scripts + data-etl + profiles matrix + SPK-102 + SPK-050 before claiming multi-agent completeness.
- Or ordered exit criteria: “cli Core green” is a hard prerequisite listed **before** “all three archetypes green,” with continuous CI of earlier goldens.

Still no sprint tickets — milestones/exit bullets only.

### Proposed Plan Diff

- §9: expand MS-003 into ordered sub-outcomes or add one intermediate milestone still in PHASE-04.
- §8 PHASE-04 exit criteria: number progressive checks; forbid claiming multi-archetype freeze while cli Core is red.
- §10: state continuous integration of archetype goldens as they land (do not wait for triple green to check first).

### Acceptance Evidence

Revised plan has at least one durable intermediate integration claim between MS-002 and full MS-003; exit cannot be “all green or nothing” without partial evidence.

### Alternatives Considered

Split PHASE-04 into two formal phases — possible but not required if progressive MS/exit bullets suffice. Leave single MS-003 — rejected (hides non-integrable work).

### Residual Risk

Progressive gates can become backlog-like if over-granular; keep at archetype/Core seams only.

### Related Findings

FND-200, FND-205.

---

## FND-202 — Default verify hardens ty at MS-002 before SPK-002 gates practical ty config

- **Severity:** Medium
- **Confidence:** High
- **Category:** Late residual-risk discovery / spike timing
- **Affected sections:** Plan §6 SPK table, §8 PHASE-03 exit / SPK-103, §8 PHASE-04 SPK-002, §9 MS-002, §16 RSK-002
- **Affected requirements:** REQ-055, REQ-080, REQ-084
- **Affected phases:** PHASE-03, PHASE-04
- **Blocks implementation:** Named phase (PHASE-03 exit claim that default = tooling-sync green **including ty** as durable; PHASE-04 ty freeze)

### Problem

MS-002 / PHASE-03 exit requires successful **default verify** on a generated tree, and default verify (revised-spec §9.5) includes **ty check**. SPK-002 (“ty sample CLI tree + CI; freeze practical ty config”) is gated only at **PHASE-04** “before locking ty template defaults hard.” Residual risk RSK-002 is therefore only formally spike-gated **after** the thin E2E already treats ty-green as generate success. That is late discovery relative to when the load-bearing claim hardens.

### Evidence

- Revised-spec §9.5.2: default = sync --locked + ruff + **ty check** (not pytest).
- Plan PHASE-03 user-visible outcome: default verify tooling-sync-green (**sync + ruff + ty**).
- Plan MS-002: default verify ran tooling-sync steps including ty.
- Plan SPK-002: PHASE-04 mid/exit; OQ-002 “before PHASE-04 ty freeze.”
- Plan §16 RSK-002 gate column: PHASE-04 only.
- SPK-103 covers **cost/network** for default verify, not ty config maturity (RSK-002).

### Failure Scenario

1. PHASE-03 uses a minimal ty config that passes on a stub `cli` tree; MS-002 exits.
2. PHASE-04 expands Core samples; SPK-002 shows ty unusable or config must change substantially.
3. MS-002 goldens and default-verify contract need rework; or team freezes a weak ty config because “MS-002 already proved ty.”
4. Owner residual-accepts RSK-002 late while public messaging still says default generate is ty-green.

### Impact

False confidence that MS-002 proved Core ty; rework of verify path; pressure toward informal ty softening (forbidden without DEC).

### Root Cause

Spike schedule follows revised-spec §16.3 “before locking ty template defaults hard” without reconciling that **default verify already requires ty** at PHASE-03.

### Required Correction

Without demoting ty from default verify (lock):

1. Add an **explicit early ty smoke** as PHASE-03 exit / MS-002 companion: either run SPK-002 (or a named SPK-002-lite on the minimal cell + foundry CI) before claiming MS-002 complete; **or**
2. Document that MS-002 proves only **runner wiring** for ty, and that **practical ty config freeze** remains SPK-002 — and require that MS-002 not freeze template ty defaults; list config as provisional until SPK-002; **and**
3. Keep SPK-002 as hard gate before MS-003 / Core emit freeze (already present) with clear residual/DEC path (already present — preserve).

Prefer (1) or a hybrid: MS-002 requires real `uv run ty check` green on minimal cell **and** records provisional config; SPK-002 still freezes Core defaults.

### Proposed Plan Diff

- §8 PHASE-03 exit / §9 MS-002: distinguish “ty runner wired and green on minimal cell” vs “ty config frozen.”
- §6 / §16: move or dual-gate SPK-002 (or SPK-002-lite) so RSK-002 is not first engaged only at multi-archetype freeze.
- Rollback: SPK-002 failure still no silent ty demotion (preserve).

### Acceptance Evidence

Revised plan states what MS-002 does and does not prove about ty; SPK-002 (or lite) is a hard prerequisite before any “ty defaults frozen” claim; default verify still includes ty.

### Alternatives Considered

Remove ty from default until SPK-002 — **rejected** (product-law / User decision; requires DEC). Leave as-is — rejected (late risk discovery).

### Residual Risk

ty ecosystem churn after freeze remains (RSK-002 residual); pin + CI fail-closed still required.

### Related Findings

FND-201, FND-205.

---

## FND-203 — MS-004 (hybrid freeze) and MS-005 (dogfood) are unordered inside PHASE-05

- **Severity:** Medium
- **Confidence:** High
- **Category:** Sequencing / hybrid integration
- **Affected sections:** Plan §8 PHASE-05, §9 MS-004, MS-005, §10, §15
- **Affected requirements:** REQ-001, REQ-081, REQ-089, REQ-076
- **Affected phases:** PHASE-05
- **Blocks implementation:** Named phase (PHASE-05 hybrid public claim)

### Problem

MS-004 (template snapshot CI green) and MS-005 (foundry dogfood Core) both live in PHASE-05 with **no dependency order**. Hybrid snapshot can be declared green and process docs can claim single-SoT **before** dogfood falsifies Core conventions that the frozen cell embeds.

### Evidence

- Plan §9 MS-004 blocks: “public hybrid claim; MS-006 hybrid portion.”
- Plan §9 MS-005 blocks: “MS-006 readiness claim.”
- Neither MS lists the other as prerequisite.
- PHASE-05 exit requires both, but parallel completion allows MS-004 first.
- Frozen cell is `cli` + `profiles=[]` — same surface dogfood is meant to stress.

### Failure Scenario

1. MS-004 lands: CI generate+diff green; template repo snapshot published as hybrid path.
2. MS-005 dogfood later forces Core emit / AGENTS / CI changes for the frozen cell.
3. Snapshot regenerates late; external consumers of the hybrid path saw an intermediate false “done.”
4. Or MS-005 is soft-attested (FND-204) while MS-004 hard-CI is treated as the real gate.

### Impact

Hybrid drift risk (RSK-103) under false completion; public path ahead of dogfood truth.

### Root Cause

PHASE-05 packs hybrid + dogfood + docs + release without ordering the two milestones that share Core freeze truth.

### Required Correction

Order milestones explicitly, e.g.:

- **MS-005 dogfood smoke (or full MS-005) before MS-004 public hybrid claim**, or  
- **MS-004 allowed only after dogfood checklist items that affect the frozen cell** (product CI gates + no research-skill leakage into emit path).

Document that hybrid “done” implies dogfood-informed Core stability for the frozen cell.

### Proposed Plan Diff

- §9 MS-004 prerequisites: add MS-005 (or named dogfood-smoke subset).
- §8 PHASE-05 exit: order bullets (dogfood → snapshot claim → release notes).
- §10 seam “Catalog SoT → Template snapshot”: note dogfood-informed freeze.

### Acceptance Evidence

Revised plan has a directed dependency MS-005 (or smoke) → MS-004 for public hybrid claim; PHASE-05 exit cannot check MS-004 alone as hybrid complete.

### Alternatives Considered

Keep parallel and regenerate snapshot always — mitigates drift technically but not false “hybrid done” signaling. Merge MS-004/005 into one milestone — acceptable if acceptance evidence still includes both classes of proof.

### Residual Risk

Dogfood never fully equals Generated Project shape (foundry is research+product); keep REQ-076 separation.

### Related Findings

FND-200, FND-204.

---

## FND-204 — MS-005 acceptance evidence includes unprovable owner attestation

- **Severity:** Medium
- **Confidence:** High
- **Category:** Acceptance criteria / unprovable gates
- **Affected sections:** Plan §9 MS-005, §8 PHASE-05 dogfood, §15
- **Affected requirements:** REQ-076; Blueprint success criteria (agent operability / consistency)
- **Affected phases:** PHASE-05
- **Blocks implementation:** Named phase (PHASE-05 / MS-005)

### Problem

MS-005 acceptance evidence includes: “Owner attestation or checklist that daily development uses the Core command surface (no parallel undocumented toolchain).” Attestation alone does **not** prove the claimed outcome. A checklist without mandatory, reviewable artifacts is easy to tick without behavioral change.

### Evidence

- Plan §9 MS-005 acceptance evidence third bullet: owner attestation or checklist.
- Other bullets (product CI ruff/ty/pytest; product AGENTS.md without shipping research skills) are stronger — but the attestation is still listed as acceptance evidence for “daily development uses Core.”
- Contract attack: “acceptance criteria that do not prove the claimed outcome.”

### Failure Scenario

1. Product CI is green on a CI-only toolchain config.
2. Owner attests daily use; actual day-to-day still uses ad-hoc Pyright, non-locked sync, or research-only habits that will not match Generated Project DoD.
3. MS-005 and then MS-006 readiness claim pass; dogfood value is theater.

### Impact

False dogfood completion; residual agent/operability gaps discovered after “v1 ready.”

### Root Cause

Soft process evidence mixed with hard CI evidence under the same milestone without ranking hard gates.

### Required Correction

Make MS-005 acceptance **observable-only** (or hard-first):

- Required: product CI locked sync + ruff + ty + pytest green; product AGENTS (or product rules) present; research skills not emitted into Generated templates (test or inventory check).
- Optional narrative: owner note — **not** sufficient alone.
- Prefer a **checked-in dogfood checklist artifact** in-repo with dated commands/results (still not a coding backlog — single acceptance record).

### Proposed Plan Diff

- §9 MS-005: demote attestation to non-gating note; require CI + surface separation evidence only.
- §8 PHASE-05 exit criterion 2: align wording with hard evidence.

### Acceptance Evidence

Revised MS-005 has no sole path through “owner says so”; CI + surface separation are necessary and sufficient.

### Alternatives Considered

Drop MS-005 entirely — rejected (dogfood is load-bearing for §29.2). Keep attestation as optional color — OK if non-gating.

### Residual Risk

CI can be green while local dev drifts; residual only, documented.

### Related Findings

FND-200, FND-203.

---

## FND-205 — PHASE-04 residual-accept of spikes can undercut Must REQ exit honesty

- **Severity:** Medium
- **Confidence:** Medium
- **Category:** Exit criteria / residual policy / unprovable readiness
- **Affected sections:** Plan §8 PHASE-04 exit criterion 2, §9 MS-003 prerequisites, §16–§18, §20 Definition of plan completion / PHASE-06 residual theme
- **Affected requirements:** REQ-055, REQ-058, REQ-070..076, REQ-088 (Must surface)
- **Affected phases:** PHASE-04, PHASE-06
- **Blocks implementation:** Named phase (PHASE-04 exit; feeds MS-006 residual theater)

### Problem

PHASE-04 exit criterion 2 allows SPK-002, SPK-050, SPK-052, SPK-102 to be “complete **or** residual risk **explicitly** accepted by owner with documented limitations (no silent skip of Must REQs).” That pairs two incompatible postures without a decision table: which spikes are **hard** for which Must REQs, and what residual acceptance is allowed without a DEC. Combined with MS-006 “satisfied or residual-accepted,” the plan risks **readiness theater**: exit while Must REQs are effectively red under euphemism.

### Evidence

- Plan PHASE-04 exit #2: complete **or** residual-accepted.
- Plan rollback: SPK-002 failure → residual RSK-002 + DEC options; SPK-052 → block secrets freeze **no dotenv**; forbidden-path fail → block MS-003 — stronger than exit #2’s “or.”
- Plan MS-003 prerequisites list spikes as if hard; exit softens them.
- Plan MS-006 / PHASE-06: Must REQ table “satisfied or owner residual-accepted.”
- Spec: ty Required and fnox locks are User decisions — residual cannot silently demote them.

### Failure Scenario

1. SPK-050 fails on target agents; team residual-accepts “multi-agent emit completeness” while still claiming REQ-070/071 Must.
2. SPK-002 is painful; residual note is written without DEC; templates still claim ty Required Core.
3. PHASE-04 and later MS-006 checklists show green via residual column; product DoD §29.2 is not met in practice.

### Impact

Unexecutable or dishonest phase exit; pressure to ship with open Must gaps; confuses plan-revision residual policy with product DEC authority.

### Root Cause

Useful residual-risk honesty (Charter/evidence) was copied into phase **exit** without a hard matrix of which outcomes require DEC vs which are documentation-only residuals.

### Required Correction

Add a **residual policy table** for plan-revision (phase-level, not coding backlog):

| Spike / risk | Hard gate for | Residual-allowed without DEC? | Requires DEC if failing |
| ------------ | ------------- | ----------------------------- | ----------------------- |
| SPK-002 | ty config freeze / MS-003 Core ty defaults | Limitations on config keys only | Demoting ty from Core / default verify |
| SPK-052 | secrets skill freeze | Delay freeze | dotenv fallback; demote fnox |
| SPK-102 | MS-003 / forbidden paths | No | Emitting forbidden paths |
| SPK-050 | multi-agent completeness claims | Narrow agent list + docs | Claiming full multi-agent DoD |

Align PHASE-04 exit #2 and MS-003 with this table; forbid residual-accept as a substitute for green forbidden-path / no-dotenv / ty-still-Required.

### Proposed Plan Diff

- §8 PHASE-04 exit #2: replace vague “or residual-accepted” with pointer to residual policy table.
- §16 / §18: merge rollback bullets with the same table.
- §9 MS-006: residual-accept only for rows marked residual-allowed; Must red otherwise returns to owning phase (already stated — make consistent).

### Acceptance Evidence

Revised plan has an explicit residual matrix; PHASE-04 exit cannot residual-accept forbidden-path or dotenv/Claude emit; ty/fnox demotion still DEC-only.

### Alternatives Considered

Make every spike absolute hard-fail with no residual — too rigid for SPK-050 agent-surface variance. Leave soft “or” — rejected (unprovable exit).

### Residual Risk

Owner may still write vague residual notes; mitigated by requiring limitation text + which REQs remain fully green.

### Related Findings

FND-201, FND-202; MS-006 theater concern closed under this finding (not separate).

---

## 5. Sequencing and Integration Issues

Cross-cutting themes (not extra FND IDs unless elevated above):

| Theme | Assessment |
| ----- | ---------- |
| Pure → FS → thin generate | **Sound.** PHASE-01..03 linear; MS-002 thin E2E honest. |
| Verify fields early / runners late | **Sound.** PHASE-01 records; PHASE-03 executes; single precedence. |
| Plan bind shape → e2e → teach | **Sound.** 01 → 03 → 04/05; RSK-108 mitigated late is OK. |
| Lock network cost (SPK-103) | **Sound timing** at PHASE-03 exit; keep. |
| fnox / forbidden paths | **Mostly sound** at PHASE-04; ensure not residual-softened (FND-205). |
| Catalog breadth vs dogfood | **Weak** (FND-200, FND-201, FND-203). |
| ty residual vs default verify | **Weak** (FND-202). |
| Hybrid single SoT | Intent sound; order vs dogfood weak (FND-203). |
| Rollback triggers | Present and lock-preserving; **exit durability** after dogfood reopen is the gap (FND-200). |
| Coding backlog | **None found** — preserve. |
| Spec phase continuity | **Preserved** — no boundary conflict finding. |
| MS-006 readiness | Acceptable if residual policy fixed (FND-205); not pure theater. |

---

## 6. Implementation Gate Recommendation

- **Gate:** **Conditional**
- **Rationale:**
  - No **Critical** sequencing defect that makes every delivery path impossible.
  - **High** findings **FND-200** and **FND-201** block treating PHASE-04 freeze / MS-003 (and downstream hybrid readiness) as delivery authority until plan-revision makes freeze durable and progressive.
  - **Medium** findings **FND-202..FND-205** must be disposed before the affected phase exits are treated as complete under a revised delivery plan.
  - PHASE-01 / PHASE-02 pure and filesystem work may proceed under **owner risk** with proposed-plan guidance, but **catalog freeze, hybrid public claim, and MS-006 readiness** must wait for `docs/plans/02-implementation-plan-revised.md` after disposition.

**Not Open:** residual High freeze/dogfood defects remain.  
**Not Blocked:** early pure pipeline is not catastrophically mis-sequenced; locks and thin E2E placement are strengths.

---

## 7. Whether an Additional Review Round Is Recommended

- **Recommendation:** **No** automatic second plan-review after plan-revision.
- **Risk-triggered yes if** plan-revision:
  - splits or merges phases beyond progressive milestones inside PHASE-04/05, or
  - introduces new machinery (new phase, new milestone class, or changes subordination to revised spec), or
  - leaves any High finding undisposed or invents product-law changes without DEC.
- Second review, if any, focuses only on **changed sequencing machinery**, not a full re-attack of locks.

---

## 8. Finding Index Table

| FND | Severity | Blocks | One-line summary |
| --- | -------- | ------ | ---------------- |
| FND-200 | High | PHASE-04 freeze / PHASE-05 hybrid done | Catalog freeze exits before dogfood; rollback reopens PHASE-04 after exit |
| FND-201 | High | PHASE-04 / MS-003 | Overlarge PHASE-04; single freeze milestone hides progressive integration |
| FND-202 | Medium | PHASE-03 ty claim; PHASE-04 freeze | ty hardened in default verify at MS-002 before SPK-002 config gate |
| FND-203 | Medium | PHASE-05 hybrid claim | MS-004 and MS-005 unordered; hybrid can freeze before dogfood |
| FND-204 | Medium | PHASE-05 / MS-005 | MS-005 allows unprovable owner attestation as acceptance evidence |
| FND-205 | Medium | PHASE-04 exit; MS-006 residual | Residual-accept of spikes can undercut Must REQ exit honesty |

**Unused IDs:** FND-206..FND-399 remain unallocated (not padding).

---

## 9. Completion Checklist

- [x] All required review sections present and non-placeholder
- [x] Status is not Placeholder (`Complete — pending independent validation and human acceptance`)
- [x] Actual review date recorded in metadata (2026-08-01)
- [x] Findings use only FND-200..FND-399; no FND-001..199 reuse; no silent reuse
- [x] Each finding has severity, confidence, failure scenario, required correction, Proposed Plan Diff
- [x] No feature ideation disguised as defects
- [x] Preference-as-defect avoided; product locks not silently reversed
- [x] Plan-review attack seeds considered (addressed or explicitly N/A)
- [x] Strengths to preserve acknowledged
- [x] Implementation gate recommendation present and consistent with severities (Conditional; High findings)
- [x] Additional review round recommendation present
- [x] Finding index table complete
- [x] Allowed file scope only (this review path; validation report separate)
- [x] Plan and revised specification **not** modified
- [x] No downstream stage started (no revised plan as main work)
- [x] No coding backlog introduced in the review
- [x] Independent validation passed (`docs/validations/02-implementation-plan-adversarial-review-validation.md`)
- [x] Human approval obtained (2026-08-01)
- [x] Stage `accepted` + `accepted_commit` recorded (`703297212c797f747de47448c91ce1d5aa5269de`)

---

*End of implementation plan adversarial review v0.1 — proposals for plan-revision only; not delivery authority; not product law.*
