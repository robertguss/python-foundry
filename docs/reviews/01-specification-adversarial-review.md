# Specification Adversarial Review — python-foundry

- **Artifact type:** Adversarial review
- **Program:** python-foundry
- **Stage:** `spec-review`
- **Status:** Complete — pending independent validation and human acceptance
- **Version:** 0.1
- **Created / review date:** 2026-08-01
- **Last updated:** 2026-08-01
- **Subject:** `docs/specifications/01-definitive-specification.md` (v0.1, Proposed — pending adversarial review; synthesis accepted)
- **Commissioning prompt:** `docs/prompts/05-specification-adversarial-review-prompt.md`
- **Finding range allocated:** FND-001..FND-199
- **Findings used:** FND-001..FND-012
- **Implementation gate (summary):** **Conditional**
- **Depends on:** Accepted proposed definitive specification (synthesis)

> Contract: `program/contracts/adversarial-review.md`.  
> Finding template: `program/templates/finding.md`.

---

## 1. Artifact Metadata

| Field | Value |
| ----- | ----- |
| Program ID | python-foundry |
| Stage ID | `spec-review` |
| Reviewer posture | Adversarial (attack; no feature ideation) |
| Subject status at review | Proposed — pending adversarial review (synthesis stage accepted) |
| Subject version | 0.1 |
| REQ surface reviewed | REQ-001..REQ-083 (sparse; 50 REQs) |
| Upstream reports (provenance) | Ecosystem v0.2; AI-native v0.2; Architecture v0.1.1 |
| DEC records at review | None under `decisions/` |

---

## 2. Review Scope and Method

### 2.1 Scope

Software-first review of the **accepted proposed definitive specification** for:

- Product scope and non-goals honesty
- Requirement completeness and testability
- Architecture / data / interface consistency
- End-to-end user and agent workflows (happy path + failure)
- Security, filesystem, determinism, dependencies
- Testing, CI, operations, greenfield migration stance
- Phase boundaries and agent legibility
- Silent expansion / framework creep
- Acceptance criteria that do not prove claimed outcomes

### 2.2 Method

1. Read Blueprint, Charter, commissioning prompt, attachment manifest, adversarial-review contract, finding template, authority ladder.
2. Read the full proposed specification (metadata through phases).
3. Cross-check load-bearing locks against reports 01–03 (provenance only; no re-selection of tools).
4. Trace workflows: `validate` → `plan` → `generate`; exclusive place; verify abort; agent DoD; GitHub snapshot path.
5. Attack polished sections (plan-as-contract, Core emit, verify tiers, catalog composition).
6. Prefer strong findings with failure scenarios; drop preference-as-defect.

### 2.3 Explicit out of scope for this review

- Revising the specification (downstream `spec-revision`)
- Implementation planning detail (downstream)
- Reopening Windows, dotenv secrets, Claude adapters, demoting ty/fnox, or Copier-as-engine as product scope
- Feature ideation (“add interactive wizard”, “add MCP profile”)
- Product implementation

### 2.4 Spec §30.1 attack seeds

| Seed | Disposition in this review |
| ---- | -------------------------- |
| Missing REQs (plan equality, forbidden paths, verify abort) | Partially covered: plan equality binding gap (FND-004); forbidden paths/verify abort largely present |
| Emit contracts vs CLI defaults | FND-001 (verify precedence); FND-005 (DoD vs default verify) |
| Under/over-specified TOML | FND-001, FND-002, FND-008 |
| quality-gates vs AGENTS.md | Cross-cutting note; not elevated to standalone defect |
| ty/fnox residual risk vs sequencing | Cross-cutting; residual risks already registered — no silent demotion |
| Phase boundaries without spikes | Cross-cutting advisory |
| Provisional CLI name `foundry` | Cross-cutting (branding/collision); not a product-scope reverse |
| data-etl dual naming | FND-007 |
| Lockfile edge cases | FND-003, FND-008 |
| Silent expansion paths | Cross-cutting; admission REQs largely hold |

---

## 3. Executive Assessment

The proposed specification is **coherent, lock-faithful, and largely standalone**. It correctly freezes hybrid product shape, Core/AI-native emit invariants, planner-led lifecycle, plan-as-contract *intent*, exclusive place, and closed catalog. The REC disposition ledger and sparse REQ set are strengths. Blueprint non-goals and User decisions (ty, fnox+age, no dotenv secrets, AGENTS.md-only, no Claude) are preserved.

**Primary failure modes are not “wrong stack” — they are underspecified control planes** that agents will invent inconsistently:

1. **Who wins** when the same concern appears in TOML and CLI (`verify`).
2. **What order** profiles actually apply (TOML array vs catalog order).
3. **How `uv.lock` stays truthful** under `python_version` and generate-time resolution.
4. **What “plan-as-contract” means operationally** when generate always rebuilds and never binds to an inspected plan artifact.

No **Critical** finding was justified: nothing forces catastrophic secret leakage by design, Windows scope creep, or silent demotion of locked tools. Implementation of pure pipeline work (PHASE-01) can proceed with care, but **generate/emit hardening should not freeze** until High findings are disposed in revision.

**Strengths to preserve in revision:** closed Core + closed agent surface; exclusive place + fail-closed dest; full REC ledger; hybrid template single SoT; non-interactive first; forbidden-path discipline.

---

## 4. Findings

## FND-001 — Verify mode precedence (TOML vs CLI) undefined

- **Severity:** High
- **Confidence:** High
- **Category:** Interfaces / workflows / consistency
- **Affected sections:** §9.5, §11.1 (`verify` field), §13.1 (`--verify`), REQ-080
- **Affected requirements:** REQ-080, REQ-020, REQ-024
- **Affected phases:** PHASE-01, PHASE-03
- **Blocks implementation:** Named phase (PHASE-03 generate defaults; also CLI flag design in PHASE-01)

### Problem

The Project Spec may set `verify`, and the CLI may pass `--verify strict|none` (and implies default when omitted). The specification never states **precedence**, **mutual exclusion**, or **merge rules**. Plan recording of verify mode (§9.5, REQ-080) therefore has no deterministic input resolution rule.

### Evidence

- §11.1: optional field `verify` ∈ {`default`,`strict`,`none`}; else CLI default `default`.
- §13.1 step 4: `foundry generate --spec … (optional --verify strict|none)`.
- REQ-080: mode must be recorded in the plan and default must be `default`.
- No table or REQ states: CLI overrides TOML | TOML wins | conflict hard-fails | last-writer rules.

### Failure Scenario

1. Spec contains `verify = "strict"`.
2. Agent runs `foundry generate --spec project.toml` (no flag) expecting strict, or runs `--verify none` expecting offline escape.
3. Two implementers choose opposite precedence.
4. Agent CI scripts diverge: one project places after ruff/ty only while author believed pytest ran in generate; another always fails offline because TOML strict cannot be overridden without editing the file.

### Impact

Non-deterministic generate behavior; plan_sha256 inputs unclear; agent automation unreliable; false confidence in verify gates.

### Root Cause

Two configuration surfaces for one plan field without a resolution rule.

### Required Correction

In revision, add an explicit normative rule, for example (choose one and REQ it):

1. **CLI flag overrides TOML when present; else TOML; else `default`**, and record effective mode + source in the plan; or
2. **Hard-fail if both specify and disagree**; or
3. **Remove TOML `verify`** and keep CLI-only (or inverse).

Document the rule in §9.5, §11.1, §13.1, and REQ-080 (or a new REQ). Include negative tests in verification path.

### Proposed Specification Diff

- §11.1: add “Effective verify resolution” subsection.
- REQ-080: add MUST resolution algorithm and plan fields `verify_mode` + `verify_source`.
- §13.1: show examples for override and conflict (if conflict rule chosen).

### Acceptance Evidence

Fixture matrix: (absent,absent)→default; (toml only); (cli only); (both equal); (both disagree) matches chosen rule; plan JSON records effective mode.

### Alternatives Considered

Keep both without precedence — rejected (agent hazard). CLI-only — simpler but loses declarative reproducers in committed specs.

### Residual Risk

Operators still misuse `none`; mitigated by loud warning already required.

### Related Findings

FND-004 (plan inputs must be total); FND-005 (verify vs DoD).

---

## FND-002 — Profile application order is contradictory

- **Severity:** High
- **Confidence:** High
- **Category:** Data model / architecture / determinism
- **Affected sections:** §9.7, §11.1 (`profiles` array), REQ-043
- **Affected requirements:** REQ-043, REQ-024, REQ-041
- **Affected phases:** PHASE-01
- **Blocks implementation:** Named phase (PHASE-01 resolve/plan goldens)

### Problem

Composition is described two ways:

- §9.7 / REQ-043: apply `core` → archetype → profiles in **catalog-defined order**.
- §9.7 also says profiles are an **“ordered”** subset; §11.1 types `profiles` as an array (order-bearing in TOML).

It is unspecified whether:

- TOML array order is ignored (catalog total order filters membership only),
- TOML array order is the apply order,
- or both must match catalog order and mismatch fails.

Path collision “later wins if `override = true`” depends on apply order.

### Evidence

- §9.7: “Profiles: ordered application of a subset… Apply: core → archetype → profiles (**catalog order**).”
- REQ-043: “profiles in **catalog-defined order**.”
- §11.1: `profiles` = array (e.g. `["http"]`) with no order-semantics sentence.
- Architecture REC-205 lean is catalog-defined order, but the proposed spec’s dual wording leaves implementers free to diverge.

### Failure Scenario

Spec: `profiles = ["data-etl", "http"]` vs `["http", "data-etl"]` with overlapping template paths where one unit sets `override = true`.

- Implementation A applies catalog order → stable plans regardless of array order.
- Implementation B applies TOML order → different file winners and different `plan_sha256`.
- Golden tests pass in one tree and fail in another for “the same” spec.

### Impact

Breaks plan-as-contract determinism (REQ-024), composition goldens (SPK-102), and agent mental models.

### Root Cause

“Ordered profiles” language mixed with “catalog-defined order” without a single normative rule for the TOML array.

### Required Correction

Normatively freeze one rule, recommended:

- **Membership** from the `profiles` array (set semantics; duplicates fail).
- **Apply order** = catalog total order restricted to selected profiles.
- TOML array order **MUST NOT** affect plan body (or MUST match catalog order else hard-fail — pick one).

State the rule in §9.7, §11.1, and REQ-043. Add fixtures for permuted arrays.

### Proposed Specification Diff

- REQ-043: explicit “array order ignored | array order authoritative | array must be catalog-sorted.”
- §11.1: one sentence on array semantics.
- Plan fields: list `profiles_selected` in apply order.

### Acceptance Evidence

Two specs differing only in profile array permutation produce identical plans under the chosen rule (or deterministic hard-fail if equality required).

### Alternatives Considered

TOML order authoritative — more agent-surprising vs closed catalog SoT; possible but must be exclusive of “catalog order” wording.

### Residual Risk

Catalog authors must maintain a documented total order for profiles.

### Related Findings

FND-007 (data-etl dual IDs raise collision odds).

---

## FND-003 — Committed `uv.lock` emit lacks generate-time truth rules

- **Severity:** High
- **Confidence:** High
- **Category:** Dependencies / emit / verification
- **Affected sections:** §6.2, §11.1 (`python_version`), §11.4, §12.3, REQ-050, REQ-051, REQ-052, REQ-080
- **Affected requirements:** REQ-050, REQ-051, REQ-052, REQ-080
- **Affected phases:** PHASE-03, PHASE-04
- **Blocks implementation:** Named phase (PHASE-04 Core emit; also PHASE-03 verify with `uv sync`)

### Problem

Every successful plan MUST emit a **committed `uv.lock`** (REQ-050/052, §12.3, OQ-104). Default verify runs **`uv sync`** (typically locked) before place (REQ-080). Separately, specs may set `python_version` (≥ floor) else default pin 3.13 (REQ-051, §11.1).

The specification does **not** define:

1. Whether `uv.lock` is **catalog-authored static** content, **generate-time produced**, or **regenerated when resolution inputs change**.
2. What happens when `python_version` (or profile deps) differs from the lock baked into catalog templates.
3. Whether verify uses `uv sync --locked` (CI for Generated Projects does — §12.4) and thus **fails** on lock/metadata mismatch after render.

### Evidence

- REQ-052 / §11.4: v1 Generated Projects MUST commit `uv.lock`.
- REQ-051: default pin 3.13; optional `python_version` if ≥ floor.
- REQ-080 / §9.5: default verify includes `uv sync` before place.
- §12.4 Generated Project CI: `uv sync --locked`.
- No REQ states lock regeneration algorithm, failure mode, or forbidding `python_version` overrides that invalidate catalog locks.

### Failure Scenario

1. Catalog goldens ship `uv.lock` for Python 3.13 + cli + no profiles.
2. Agent sets `python_version = "3.12"` or adds `profiles = ["http"]` changing deps.
3. Generate renders stale lock + new `pyproject.toml`.
4. Default verify `uv sync` / `--locked` fails every generate, or succeeds unlocked and commits a lying lock relative to CI `--locked`.
5. Implementers “fix” by skipping lock commits — violating REQ-052 — or by ignoring `python_version`.

### Impact

Core emit invariants become unsatisfiable together; generate success rate collapses; agents learn to use `--verify none` and ship broken locks (relates to RSK-102).

### Root Cause

Lockfile policy frozen as **emit presence** without **lifecycle** (author-time vs generate-time) and without binding to resolution inputs.

### Required Correction

Add a normative lock lifecycle, for example:

1. **Generate MUST produce or refresh `uv.lock` to match resolved pyproject + python pin + profiles** before/during verify (network disclosed); commit that lock; or
2. **v1 forbids `python_version` overrides and profile dep changes without per-matrix catalog locks** (closed matrix only); or
3. Hybrid: static locks only for golden matrix cells; any off-matrix resolution hard-fails at plan time.

Align REQ-050/051/052/080 and §11.4. State whether verify uses `--locked`. Document offline implications.

### Proposed Specification Diff

- New subsection under §11.4 or §12.3: “Lockfile production rules.”
- REQ-052 expansion or new REQ-05x for lock regeneration/matrix.
- REQ-080: clarify `uv sync` flags and failure if lock inconsistent.
- Plan: record python pin + lock digest.

### Acceptance Evidence

Matrix tests: each allowed (archetype × profile × python pin) cell yields generate+verify success with CI-equivalent `--locked` sync; off-matrix fails closed at plan or generate with actionable error.

### Alternatives Considered

Drop committed lock for v1 — rejected (contradicts accepted OQ-104 / ecosystem lock). Catalog-only locks without `python_version` field — viable simplification.

### Residual Risk

Network for lock refresh (RSK-102); pin churn (RSK-001).

### Related Findings

FND-005, FND-008.

---

## FND-004 — Plan-as-contract does not bind generate to an inspected plan

- **Severity:** High
- **Confidence:** High
- **Category:** Architecture / agent workflows / determinism
- **Affected sections:** §9.2–§9.3, §13.1, REQ-024, REQ-025, REQ-026
- **Affected requirements:** REQ-024, REQ-025, REQ-026
- **Affected phases:** PHASE-01..03
- **Blocks implementation:** Named phase (PHASE-03 semantics; agent trust model)

### Problem

REQ-024 requires the Generation Plan to be the immutable contract and that `generate` rebuild with the same Construct rules and fail closed if inputs would diverge from a trustworthy dry-run. REQ-025 makes **on-disk plan under `.foundry/` optional** and not required. There is **no** generate flag to execute a previously emitted plan artifact (by path or `plan_sha256`).

Operationally, “plan then generate” in §13.1 is two independent Construct invocations. Any change to foundry version, packaged catalog, or spec between steps yields a **different** plan without the agent noticing unless they manually diff JSON.

“Fail closed if inputs would diverge from a trustworthy dry-run” is **unimplementable** without defining what the trusted dry-run artifact is.

### Evidence

- §9.2: generate rebuilds Construct from the same inputs and executes.
- REQ-024: fail closed if inputs diverge from trustworthy dry-run — no artifact identity defined.
- REQ-025: persisting plan under `.foundry/` NOT required; JSON via stdout/flags only.
- §13.1: steps 3–4 are separate commands with no `--plan` binding.

### Failure Scenario

1. Agent runs `foundry plan --json` and reviews file list (security-sensitive paths, digests).
2. Foundry package or catalog is upgraded (or another process edits the TOML).
3. Agent runs `foundry generate` assuming reviewed plan.
4. Generate places a different tree (extra files, different pins). Destination is “successful” exclusive place of the **wrong** contract.

### Impact

Agent trust model of dry-run is false; plan_sha256 is only useful within a single invocation; security review of plan text is non-binding.

### Root Cause

Plan-as-contract is specified as **pure function purity**, not as **user-visible binding** between review and side effects.

### Required Correction

Revision must pick and REQ one operational model:

1. **Bind generate to plan artifact:** e.g. `generate --plan plan.json` (or `--plan-sha256` + recompute and hard-fail on mismatch) where plan includes foundry version + catalog digest; or
2. **Explicitly demote** “trustworthy dry-run” language to “same process inputs only,” and document that plan and generate are **not** a two-phase commit — agents must treat generate as sole authority and re-diff via `--json` in the same invocation pipeline; or
3. **Single command mode** that prints plan and requires `--yes` (still not two-command safe).

Recommended for agent-first product: (1) optional but normative when `--plan` supplied; default rebuild remains, with docs warning.

### Proposed Specification Diff

- REQ-024: define “trusted plan” artifact fields and generate binding behavior.
- REQ-025: if binding exists, specify required plan JSON fields for generate.
- §13.1: workflow for safe agent path (`plan --json > p.json && generate --plan p.json`).
- Errors: mismatch of catalog digest / plan_sha256 / foundry version.

### Acceptance Evidence

Tests: generate with matching plan succeeds; mutated plan or catalog digest mismatch hard-fails before stage writes; rebuild-only path documented.

### Alternatives Considered

Do nothing — leaves REQ-024’s “trustworthy dry-run” phrase as false advertising.

### Residual Risk

Stale plan files after intentional catalog upgrades — mitigated by digest checks.

### Related Findings

FND-001 (effective inputs must be total); FND-009 (hash stability).

---

## FND-005 — “Runnable project” / agent DoD overclaims relative to default verify

- **Severity:** Medium
- **Confidence:** High
- **Category:** Testing / acceptance criteria / consistency
- **Affected sections:** §5.1 goal 6, §9.5, §13.5, REQ-056, REQ-074, REQ-080
- **Affected requirements:** REQ-056, REQ-074, REQ-080
- **Affected phases:** PHASE-03..04
- **Blocks implementation:** No (does not block coding start; blocks honest success criteria)

### Problem

Product goals and verification narrative imply generate yields a **runnable** / quality-gated project. Default verify is only `uv sync` + ruff + ty — **not pytest**. Agent DoD (§13.5 / REQ-074) **requires pytest** (and rejects empty collection for package/CLI). Templates must ship ≥1 smoke test (REQ-056), but default generate can **place** a tree whose tests are red or never run.

### Evidence

- §5.1 goal 6: empty → validate/plan → generate → **runnable** project.
- §9.5 / REQ-080: default verify excludes pytest; strict adds pytest.
- §13.5 / REQ-074: agents must not claim done without pytest green.
- REQ-056: templates include smoke tests so collection is non-empty.

### Failure Scenario

Agent runs `foundry generate` (default), sees exit 0, claims “project ready.” Smoke test is wrong/import-broken. CI on first push fails pytest. Agent believes foundry DoD was satisfied because generate verified.

### Impact

False success signal; support burden; weakens “runnable” success criterion from Blueprint/program goals.

### Root Cause

Tiered verify is sound engineering, but success language was not aligned to the default tier.

### Required Correction

Either:

1. Redefine default success as “tooling-sync green, tests not yet proven” and **remove or qualify “runnable”** in goals/DoD cross-links; require docs to say **first agent task includes pytest**; or
2. Promote pytest into default verify (cost/latency tradeoff; disclose network); or
3. Keep tiers but add REQ: generate text report MUST state “tests not run” when mode ≠ strict.

At minimum, align §5.1, §13.5, REQ-074, REQ-080 vocabulary.

### Proposed Specification Diff

- §5.1 goal 6 wording.
- REQ-080 acceptance notes: what “success” means per tier.
- AGENTS.md emit requirements: post-generate checklist includes pytest when default was used.

### Acceptance Evidence

Docs/fixtures show distinct success meanings; no remaining claim that default verify implies pytest green.

### Alternatives Considered

Default=strict — heavier (RSK-102); acceptable if owner prioritizes runnable over speed.

### Residual Risk

Agents still skip pytest after place; skill content must remain firm (REQ-074).

### Related Findings

FND-003 (sync/lock), FND-006 (strict costs).

---

## FND-006 — `strict` verify assumes git + pre-commit installability

- **Severity:** Medium
- **Confidence:** High
- **Category:** Reliability / testing / workflows
- **Affected sections:** §9.5, REQ-080, REQ-057
- **Affected requirements:** REQ-080, REQ-057, REQ-031
- **Affected phases:** PHASE-03
- **Blocks implementation:** Named phase (PHASE-03 strict path)

### Problem

Strict verify = default + pytest (+ cov if configured) + **pre-commit when present**. Fresh exclusive-place destinations are **not** specified to be `git init`’d. `pre-commit run --all-files` commonly requires a git repo and often network to install hook environments on first run. Generate stage is a temporary tree; failure preserves stage but semantics of “pre-commit when present” are underspecified (config file present vs hooks installed vs git present).

### Evidence

- §9.5 strict row includes pre-commit when present.
- REQ-057: emit pre-commit config by default.
- No REQ requires `git init` in stage before strict verify.
- §13.4 documents `pre-commit run --all-files` for later agent use — different context than pre-place verify.

### Failure Scenario

User/agent runs `--verify strict` on first generate. Stage has `.pre-commit-config.yaml` but no `.git`. pre-commit exits non-zero. Generate aborts place forever until they use `default`/`none` or we special-case pre-commit — undocumented.

### Impact

Strict mode is a footgun; agents learn to avoid the higher gate; false belief that strict == CI parity (CI uses GHA steps, not necessarily pre-commit).

### Root Cause

Hook runner semantics copied from developer machines into pre-place verify without environmental prerequisites.

### Required Correction

Normatively define strict pre-commit behavior, e.g.:

1. Strict **does not** run pre-commit pre-place; document CI/agent DoD separately; or
2. Strict runs pre-commit only if git repo exists and hooks installed; else skip with warning; or
3. Generate performs `git init` in stage before strict pre-commit (declare side effects).

Align REQ-080 with GHA reality (§12.4 does not require pre-commit in CI).

### Proposed Specification Diff

- §9.5 strict row rewrite.
- REQ-080 exceptions/prerequisites.
- Note RSK for pre-commit-in-verify.

### Acceptance Evidence

e2e: strict on non-git stage matches written rule (pass/skip/fail) deterministically.

### Alternatives Considered

Always git init in stage — possible but expands generate side effects (must be explicit).

### Residual Risk

pre-commit latency (SPK-003) if retained.

### Related Findings

FND-005.

---

## FND-007 — `data-etl` dual identity (archetype and profile)

- **Severity:** Medium
- **Confidence:** High
- **Category:** Agent legibility / data model
- **Affected sections:** §9.6–§9.7, §11.1, §11.3, REQ-040, REQ-042, REQ-061
- **Affected requirements:** REQ-040, REQ-042, REQ-061, REQ-071
- **Affected phases:** PHASE-01, PHASE-04
- **Blocks implementation:** No (implementable; high confusion cost)

### Problem

The closed catalog uses the **same string id** `data-etl` for an **archetype** and a **profile**. Agents and humans routinely confuse “I selected data-etl” (which axis?). Composition `archetype = "data-etl"` with or without `profiles = ["data-etl"]` is easy to mis-author. Error messages and catalog list UX are unspecified regarding disambiguation.

### Evidence

- §11.3: archetype ids include `data-etl`; profile ids include `data-etl`.
- REQ-042 / REQ-040 encode both.
- Validation advisory and spec §30.1 seed already flag this.
- REC-103 modification uses `add-script` for data-etl archetype — another overloaded term cluster.

### Failure Scenario

Agent writes `archetype = "cli"` and `profiles = ["data-etl"]` when it meant data-etl archetype layout, or inverse. Plan succeeds with wrong tree shape. Time lost; skills (`add-script` vs data domain) misaligned.

### Impact

Support/agent error rate; golden matrix cardinality misunderstood; docs verbosity tax.

### Root Cause

Shared label across orthogonal catalog kinds without mandatory qualification in CLI/UX.

### Required Correction

Revision must either:

1. **Rename** one id (e.g. profile `data-stack` / `polars` or archetype `etl-app`) with disposition notes; or
2. Keep ids but **require** fully-qualified references in CLI/plan/docs (`archetype:data-etl`, `profile:data-etl`) and catalog list columns; hard-fail ambiguous bare tokens in any future unified field.

Do not leave “intentional but confusing” without UX/REQ mitigations.

### Proposed Specification Diff

- §11.3 + REQ-040/042 id table; or rename + ledger note.
- §12.1 catalog list/show fields.
- Examples in §11.1 showing valid combinations.

### Acceptance Evidence

Usability: catalog show distinguishes kinds; at least one negative fixture for confused specs if applicable; docs examples cover both axes.

### Alternatives Considered

Document-only warning — weak for agents; better than nothing but inferior to rename or qualified ids.

### Residual Risk

Rename churn if delayed past first public templates.

### Related Findings

FND-002 (composition order).

---

## FND-008 — `scripts` archetype emit contract under-specified vs package archetypes

- **Severity:** Medium
- **Confidence:** Medium
- **Category:** Requirements completeness / testing
- **Affected sections:** §11.4, §12.3, REQ-053, REQ-056, REQ-052
- **Affected requirements:** REQ-053, REQ-056, REQ-050, REQ-052
- **Affected phases:** PHASE-04
- **Blocks implementation:** Named phase (PHASE-04 scripts goldens)

### Problem

`cli` / package-shaped trees get concrete layout, scripts entry points, and ≥1 smoke test rules. The `scripts` archetype is described as “PEP 723 + `uv run` oriented layout **per catalog**” (REQ-053) without normative file inventory, whether `src/` is required, whether `uv.lock` still applies identically, and whether empty pytest collection is allowed.

REQ-056’s empty-collection ban is scoped to “package/CLI-shaped templates,” silently creating a third behavior class without defining scripts shape membership.

### Evidence

- REQ-053: scripts bullet is catalog-relative only.
- REQ-056: ≥1 smoke for package/CLI; scripts not mentioned.
- §12.3: `src/<package>/` “per archetype” — conflicts with pure PEP 723 script trees if taken literally for all archetypes.
- §11.4: all v1 Generated Projects application-shaped MUST commit `uv.lock` — may be wrong for script-only layouts depending on uv project model.

### Failure Scenario

Two implementers emit different scripts archetypes (flat scripts/ vs src package + scripts). Conformance tests disagree. Agents cannot know DoD for “scripts-only” repos.

### Impact

PHASE-04 thrash; archetype promises without REQ teeth; lock policy may not fit.

### Root Cause

Closed set includes three archetypes; only two are specified to implementable depth.

### Required Correction

Add a normative scripts emit inventory: required paths, dependency model (uv project vs script metadata), lockfile rule, test policy (explicit allow empty **or** require ≥1), and AGENTS.md command examples. Align §12.3 table (“per archetype”) so it does not imply universal `src/<package>/`.

### Proposed Specification Diff

- REQ-053 expansion or REQ-053a scripts contract.
- REQ-056 scope table by archetype.
- §12.3 split rows by archetype.

### Acceptance Evidence

Golden path inventory for `scripts` alone and with each profile; conformance suite green.

### Alternatives Considered

Defer scripts archetype to post-v1 — scope change requiring disposition against Blueprint L6; not preferred without owner DEC.

### Residual Risk

PEP 723 ecosystem evolution.

### Related Findings

FND-003.

---

## FND-009 — `plan_sha256` lacks canonicalization algorithm

- **Severity:** Medium
- **Confidence:** High
- **Category:** Data model / determinism
- **Affected sections:** §9.3, REQ-026, REQ-024
- **Affected requirements:** REQ-026, REQ-024
- **Affected phases:** PHASE-01
- **Blocks implementation:** Named phase (PHASE-01 goldens; cross-language agents comparing hashes)

### Problem

REQ-026 requires `plan_sha256` over canonical JSON excluding that field. The specification never defines canonicalization: key sort order, integer formatting, path separators, Unicode normalization, float policy (should be none), exclusion set beyond the hash field, or hash algorithm (assumed SHA-256 but encoding of preimage not frozen).

### Evidence

- §9.3: `plan_sha256` over canonical JSON excluding that field.
- REQ-026: same; verification = hash stability tests.
- RSK-100 notes non-determinism risk but does not supply algorithm.

### Failure Scenario

Python `json.dumps` default vs `sort_keys=True` vs JCS (RFC 8785) produce different hashes for “equal” plans. Agent tools in another runtime cannot verify plan integrity. Goldens flake across platforms if path normalization differs (`./x` vs `x`).

### Impact

Plan integrity feature is non-portable; REQ-024 equality claims weaken.

### Root Cause

Integrity field specified without normative preimage algorithm.

### Required Correction

Freeze a canonicalization profile, e.g.:

- UTF-8 JSON, sorted object keys, no insignificant whitespace, paths as POSIX relative normalized strings, hash = SHA-256 hex of preimage bytes;
- or cite RFC 8785 JCS.

List excluded fields and required plan schema version field.

### Proposed Specification Diff

- REQ-026 algorithm subsection.
- §9.3 pointer.
- Test vectors (minimal plan → fixed hash).

### Acceptance Evidence

Published test vector; multi-implementation or multi-call stability.

### Alternatives Considered

Drop plan_sha256 — loses comparison aid; worse than specifying algorithm.

### Residual Risk

Schema evolution must version canonical rules.

### Related Findings

FND-004.

---

## FND-010 — GitHub template snapshot inputs not frozen

- **Severity:** Medium
- **Confidence:** High
- **Category:** Hybrid product / CI / scope
- **Affected sections:** §9.9, REQ-001, REQ-081
- **Affected requirements:** REQ-001, REQ-081
- **Affected phases:** PHASE-05
- **Blocks implementation:** Named phase (PHASE-05 hybrid)

### Problem

Hybrid shape requires a GitHub template that is a **generated snapshot** from catalog SoT with CI drift checks (REQ-081). The specification never freezes the **Project Spec inputs** for that snapshot: archetype, profiles, python pin, name/destination placeholders, verify mode. §13.3 says profiles beyond snapshot defaults need the CLI — without defining defaults.

### Evidence

- §9.9: “fixed public template spec” — not enumerated.
- REQ-081: snapshot from catalog; drift fails CI.
- §13.3: template workflow; profiles beyond defaults → CLI.

### Failure Scenario

Release engineering picks `cli+http` one month and `scripts` the next. Drift CI checks “goldens” that move with opinion. Public template users get unstable baselines; docs disagree with repo contents.

### Impact

Hybrid surface fails product promise of consistent Core showcase; PHASE-05 bikeshedding.

### Root Cause

SoT rule without freezing the public matrix cell.

### Required Correction

Normatively specify v1 public template spec (e.g. archetype `cli`, profiles `[]` or `["http"]`, python default 3.13, non-secret placeholders). Require that cell to be a CI golden. Document upgrade process when template defaults change (versioned release notes).

### Proposed Specification Diff

- §9.9 “Public template Project Spec (normative).”
- REQ-081 reference to that frozen spec.
- §13.3 defaults sentence.

### Acceptance Evidence

Checked-in template spec file used by CI generate+diff; matches docs.

### Alternatives Considered

Multiple templates — out of v1 scope / marketplace smell; reject without DEC.

### Residual Risk

Single snapshot cannot demo all profiles (already accepted; CLI covers).

### Related Findings

None.

---

## FND-011 — Stage identity, retention, and collision semantics incomplete

- **Severity:** Low
- **Confidence:** High
- **Category:** Filesystem / reliability / agent legibility
- **Affected sections:** §9.4, §15, REQ-031, RSK-101
- **Affected requirements:** REQ-031
- **Affected phases:** PHASE-02
- **Blocks implementation:** No

### Problem

Generate creates a sibling staging directory, preserves it on failure, places on success. Missing norms:

- Directory naming pattern (predictable vs random).
- Behavior if a previous failed stage directory still exists (reuse, refuse, new name).
- Success-path cleanup if place uses copy+delete vs rename.
- Whether stages may land on a different filesystem despite SHOULD same-parent guidance.
- How errors present the stage path (required content).

RSK-101 acknowledges agent confusion but requirements do not force machine-parseable stage path in errors.

### Evidence

- §9.4 steps 2–6; REQ-031; §15 stage retention row; RSK-101.

### Failure Scenario

Repeated failed generates create `project.stage`, `project.stage2`, or fail on name collision with unclear recovery. Agent deletes the wrong directory and loses debug evidence — or cannot find stage path in noisy logs.

### Impact

Operability friction; rare data-loss if user removes “wrong” folder adjacent to dest.

### Root Cause

Write algorithm specified at intent level without operational identity rules.

### Required Correction

Specify stage naming, collision policy, success cleanup, and **MUST** print absolute stage path on failure (stable field in JSON error report).

### Proposed Specification Diff

- REQ-031 bullet list expansion.
- §15 operations table.

### Acceptance Evidence

Failure-injection e2e asserts path in stderr/JSON; second failure behavior matches spec.

### Alternatives Considered

Always wipe prior stages — risky if user inspects; must be explicit opt-in if chosen.

### Residual Risk

Disk fill from retained stages — document manual cleanup.

### Related Findings

None.

---

## FND-012 — Machine-readable failure taxonomy under-specified

- **Severity:** Low
- **Confidence:** Medium
- **Category:** Interfaces / agent operability
- **Affected sections:** §12.1, REQ-010
- **Affected requirements:** REQ-010, REQ-025
- **Affected phases:** PHASE-01..03
- **Blocks implementation:** No

### Problem

§12.1 says distinct exit codes SHOULD be used where practical and documented in foundry AGENTS.md — not a Must REQ table. JSON reports are required for plan/generate modes, but stable **error code enum** (validation vs resolve vs verify vs place) is not normative. Agents cannot reliably branch without scraping strings.

### Evidence

- §12.1 exit codes SHOULD.
- REQ-010 lists commands but not error contract.
- Agent-first Blueprint success criterion implies scriptable failures.

### Failure Scenario

Agent wrapper treats all non-zero equally, retries verify failures as if they were validation errors, enters loops, or ignores preserve-stage paths.

### Impact

Weaker agent operability than product goals claim.

### Root Cause

CLI surface frozen for commands more than for result schema.

### Required Correction

Add a minimal normative error taxonomy (even if exit codes collapse to one non-zero) via **JSON report fields**: `error_class`, `stage_path?`, `verify_mode?`. Promote from SHOULD docs to Must for generate/plan JSON failure objects.

### Proposed Specification Diff

- §12.1 error report schema table.
- REQ under §22.2 or §22.8.

### Acceptance Evidence

Contract tests for failure JSON on representative faults.

### Alternatives Considered

Exit-code-only matrix — brittle on Windows-free Unix still; JSON better for agents.

### Residual Risk

Over-detailed enums churn — keep small closed set.

### Related Findings

FND-011.

---

## 5. Cross-Cutting Issues

### 5.1 Locks and User decisions

No finding requires demoting **ty**, **fnox+age**, forbidding dotenv secrets, AGENTS.md-only, no Claude adapters, exclusive place, closed catalog, or custom engine. Residual maturity risks (RSK-002, RSK-007/050) remain correctly registered; revision should keep mitigations and sequencing (SPK-002/052) explicit when touching emit phases.

### 5.2 Preference rejected

Not filed as defects: choice of Typer, polars default, pre-commit Default vs hk profile, MCP none, no Cursor rules v1, provisional name `foundry` as pure branding taste. **CLI/PyPI name collision** is a residual branding risk (OQ-105) — owner DEC before PyPI publish; not a specification logic hole.

### 5.3 quality-gates skill vs AGENTS.md

Duplication risk exists (REC-103 tension). Not elevated: REQ-071/074 can be satisfied with thin skill wrappers. Revision may note “skills MUST NOT contradict AGENTS.md; AGENTS.md wins on conflict” if desired — optional Low polish, not required for gate.

### 5.4 Phase boundary pressure

High findings FND-001..004 should be disposed **before** treating PHASE-03/04 goldens as stable. PHASE-01 can start on pure parse/resolve once FND-002/009 rules are chosen. Spikes SPK-100..103 remain appropriate gates; do not invent unbounded new research tracks.

### 5.5 Silent expansion

REQ-003/044/078 and forbidden-path language are directionally strong. Residual pressure paths (manual MCP, Claude “just one file,” dotenv “for local only”) are agent-behavior risks already in RSK-050/051/053 — keep content tests; no additional Critical gap found.

### 5.6 Spec §30 seeds not turned into findings

Missing REQs for exclusive place / forbidden paths / verify abort are **largely present** (REQ-030..032, REQ-050, REQ-080). Remaining holes are control-plane totality (this review), not absence of those three themes.

---

## 6. Implementation Gate Recommendation

| Field | Value |
| ----- | ----- |
| **Gate** | **Conditional** |
| **Rationale** | No Critical defects. Four **High** findings (FND-001..004) make generate/verify/emit behavior non-total for agents and threaten plan determinism and lock honesty. Pure pipeline scaffolding may proceed after FND-002/009 resolution; **do not** freeze generate defaults, Core lock emit, or public hybrid snapshot until High findings are dispositioned in `spec-revision`. Medium findings (FND-005..010) should be fixed before or during the phases they name; Low findings (FND-011..012) should not block early work. |

### Gate conditions (summary)

| ID | Before |
| -- | ------ |
| FND-001 | PHASE-03 default generate CLI freeze |
| FND-002 | PHASE-01 resolve/plan goldens |
| FND-003 | PHASE-04 lock emit + PHASE-03 verify locked sync |
| FND-004 | Claiming agent-safe plan→generate workflow |
| FND-005..006 | Docs/DoD honesty; strict mode e2e |
| FND-007..008 | PHASE-04 catalog UX + scripts goldens |
| FND-009 | PHASE-01 plan_sha256 goldens |
| FND-010 | PHASE-05 template release |
| FND-011..012 | Should fix early; non-blocking |

---

## 7. Whether an Additional Review Round Is Recommended

| Field | Value |
| ----- | ----- |
| **Recommended?** | **Conditional yes** |
| **Trigger** | If revision introduces **plan-artifact binding** (FND-004 option 1) or **generate-time lock regeneration** (FND-003 option 1) as substantial new machinery, run a **focused** second pass on those mechanisms only (risk-triggered policy). |
| **Not recommended** | Endless full re-review for Low-only polish, or automatic second round if revision only clarifies precedence/order text without new subsystems. |

---

## 8. Finding Index Table

| FND | Severity | Blocks | One-line summary |
| --- | -------- | ------ | ---------------- |
| FND-001 | High | PHASE-03 (CLI/defaults) | TOML vs CLI `verify` precedence undefined |
| FND-002 | High | PHASE-01 | Profile apply order: catalog vs TOML array contradiction |
| FND-003 | High | PHASE-03/04 | `uv.lock` emit lacks generate-time truth rules with `python_version`/profiles |
| FND-004 | High | PHASE-03 agent trust | Plan-as-contract does not bind generate to inspected plan |
| FND-005 | Medium | No | Default verify vs “runnable” / pytest DoD overclaim |
| FND-006 | Medium | PHASE-03 strict | Strict pre-commit assumes git/hooks environment |
| FND-007 | Medium | No | `data-etl` dual archetype/profile identity |
| FND-008 | Medium | PHASE-04 | `scripts` archetype emit/tests/lock under-specified |
| FND-009 | Medium | PHASE-01 | `plan_sha256` canonicalization algorithm missing |
| FND-010 | Medium | PHASE-05 | Public GitHub template Project Spec inputs not frozen |
| FND-011 | Low | No | Stage naming/retention/collision semantics incomplete |
| FND-012 | Low | No | Machine-readable error taxonomy under-specified |

**Counts:** Critical 0 · High 4 · Medium 6 · Low 2 · **Total 12** (FND-001..012).

---

## 9. Completion Checklist

- [x] All required review sections present and non-placeholder
- [x] Status is not Placeholder
- [x] Actual review date recorded in metadata (2026-08-01)
- [x] Findings use only FND-001..FND-199; no out-of-range IDs; no silent reuse
- [x] Each finding has severity, failure scenario, required correction
- [x] No feature ideation disguised as defects
- [x] Preference-as-defect avoided; locks not silently reversed
- [x] Spec §30.1 attack seeds considered (addressed or explicitly N/A)
- [x] Strengths to preserve acknowledged
- [x] Implementation gate recommendation present and consistent with severities
- [x] Additional review round recommendation present
- [x] Finding index table complete
- [x] Allowed file scope only (review path)
- [x] Specification not modified
- [x] No downstream stage started (no revised specification as main work)

---

*End of specification adversarial review v0.1 — pending independent validation and human acceptance.*
