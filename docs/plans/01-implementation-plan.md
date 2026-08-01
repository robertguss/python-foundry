# Implementation Plan — python-foundry

- **Artifact type:** Implementation plan
- **Program:** python-foundry
- **Status:** Proposed — pending plan adversarial review
- **Version:** 0.1
- **Plan date:** 2026-08-01
- **Delivery status:** Not delivery authority (proposed sequence only)
- **Implementation authority:** `docs/specifications/02-definitive-specification-revised.md` v0.2 (accepted; commit `faffbdc`)
- **Depends on:** Accepted revised definitive specification (`spec-revision`)
- **Stage:** `implementation-plan`
- **Commissioning prompt:** `docs/prompts/07-implementation-plan-prompt.md`
- **Phase range used:** PHASE-01..PHASE-06 (continuity with revised-spec §31)
- **Milestone range used:** MS-001..MS-006
- **This artifact does not supersede** Blueprint locks, Charter methodology, or revised-spec REQs

> Translates the accepted revised specification into a **safe delivery sequence**.
> Defines **how to build**, not what the architecture should become.
> **Phases and milestones only** — no coding backlog, sprint tickets, or agent
> task packets. Contract: `program/contracts/implementation-plan.md`.

---

## 1. Artifact Metadata

| Field | Value |
| ----- | ----- |
| Program ID | python-foundry |
| Plan ID | `docs/plans/01-implementation-plan.md` |
| Plan version | 0.1 |
| Plan date | 2026-08-01 |
| Status | **Proposed — pending plan adversarial review** |
| Rigor tier | standard |
| Host OS targets | macOS + Linux only |
| Provisional CLI name | `foundry` (OQ-105 branding; package `python-foundry`) |
| Operator | robertguss |
| Upstream authority commit (revised spec) | `faffbdc` |
| Plan HEAD at write time | see Git when committed |

---

## 2. Implementation Authority

| Authority | Role |
| --------- | ---- |
| Accepted `DEC-###` | Highest; none present under `decisions/` at plan time |
| `docs/00-program-blueprint.md` | Locked scope, non-goals, success criteria |
| `docs/01-research-charter.md` | Evidence and methodology rules |
| **`docs/specifications/02-definitive-specification-revised.md` v0.2** | **Product law / implementation authority** |
| This plan | Delivery sequencing proposal only until plan-review + plan-revision acceptance |

**Subordination rule:** This plan MUST NOT change architecture, REQ semantics,
locks, or non-goals. If sequencing appears to require a product change, record an
open question or rollback trigger — do not silently amend REQs.

**Starting phase model:** revised-spec §30.3 phase gates and §31 PHASE-01..06.
No merge or split of phases; refinements are executable entry/exit criteria and
milestone acceptance evidence only.

---

## 3. Objectives

Deliver python-foundry **v1** under the revised specification by sequencing work so that:

1. **Load-bearing unknowns** (ty, fnox, lock network cost, plan bind) are gated
   by spikes before they harden wrong defaults.
2. **Thin end-to-end capability** appears early: pure Construct → stage →
   lock → default verify → exclusive place for a minimal `cli` cell, before full
   catalog content breadth.
3. **Continuous integration** of pure pipeline, filesystem, generate, and catalog
   emit — not a big-bang late integration.
4. **Dogfood** the foundry product repo on Generated Project Core conventions
   before broad expansion and release polish.
5. **Hybrid surface** lands as a CI-frozen GitHub template snapshot from the
   catalog SoT (frozen cell: archetype `cli`, `profiles=[]`, …).
6. Every **Must REQ** maps to at least one phase with observable exit evidence.
7. Residual risks called out in §30.4 (ty, fnox/dotenv, lock cost, agents skip
   `--plan`, provisional CLI name) are explicitly sequenced.

Success aligns with revised-spec §29.2 product v1 DoD and Blueprint §8 success
criteria — without reopening non-goals.

---

## 4. Non-Goals

### Plan non-goals (this artifact)

- Granular coding backlog, sprint tickets, or coding-agent task packets
- Changing REQs, architecture, or tool selections
- Starting `plan-review`, `plan-revision`, or product implementation in the
  research-program packaging sense as the output of *this* stage
- Inventing formal `DEC-###` records

### Product non-goals (inherited — MUST NOT become v1 scope without DEC / Blueprint amendment)

From Blueprint §6 and revised-spec §5.2 / §27:

- Windows support
- Notebooks, GUI apps, mobile
- Framework zoo / multi-stack marketplace
- Remote/plugin catalogs or template marketplace
- dotenv / `.env` as secret storage
- Claude adapters / `CLAUDE.md` / `.claude/` Core emit
- Default MCP kitchen-sink catalogs
- Copier/Cookiecutter as the foundry runtime engine
- Existing-project update/merge in v1
- Demoting **ty** or **fnox** from Core without DEC
- Treating default verify success as pytest DoD (pytest remains agent DoD / strict)

---

## 5. Assumptions

1. Revised specification v0.2 remains implementation authority for the duration
   of delivery unless superseded by an accepted DEC or a later accepted
   specification revision.
2. Product implementation may live in this repository or a linked product tree;
   phase acceptance is defined by **observable behavior and tests**, not by which
   monorepo path holds code.
3. Operator environment has **uv**, network (for lock/sync where required), and
   ability to run **ruff**, **ty**, **pytest** as specified for verify tiers.
4. Host OS for development and CI: **Linux required**; macOS optional (OQ-005).
5. CLI binary name remains provisional `foundry` until owner DEC (OQ-105);
   package identity `python-foundry` is stable.
6. Closed catalog units for v1 are exactly those in revised-spec §11.3
   (core; archetypes `cli`|`scripts`|`data-etl`; profiles `http`|`hooks-hk`|`data-etl`).
7. go-foundry is prior art only (REQ-083 / §9.10); stage-root confinement is
   sufficient for v1 (no FD-level openat parity required to exit PHASE-02).
8. No accepted DECs exist at plan time that alter locks.
9. Greenfield product: no production user migration (see §11).

---

## 6. Dependency Graph

```text
PHASE-01 Pure pipeline
    │
    ▼
PHASE-02 Filesystem (stage + exclusive place)
    │
    ▼
PHASE-03 Generate + verify + lock  ◄── thin E2E (minimal catalog cell)
    │
    ▼
PHASE-04 Catalog content + emit  ◄── SPK-002 / SPK-050 / SPK-052 gates
    │
    ▼
PHASE-05 Hybrid template + dogfood + docs
    │
    ▼
PHASE-06 Harden + residual risk acceptance
```

| From | To | Dependency kind |
| ---- | -- | --------------- |
| PHASE-01 | PHASE-02 | Construct + plan bind API shape stable enough to drive stage inputs |
| PHASE-02 | PHASE-03 | Stage/place primitives callable from generate orchestration |
| PHASE-03 | PHASE-04 | Generate lifecycle green on minimal cell; lock+verify semantics proven |
| PHASE-04 | PHASE-05 | Full archetype goldens + forbidden-path conformance; dogfood inputs ready |
| PHASE-05 | PHASE-06 | Hybrid CI + dogfood evidence; release path exercised at least once |
| SPK-100 | PHASE-01 exit | Pure plan golden for minimal CLI |
| SPK-101 | PHASE-02 exit | Stage + exclusive place |
| SPK-103 | PHASE-03 exit | Default verify cost / network disclosure acceptable |
| SPK-102 | PHASE-04 exit | Catalog expand + forbidden paths |
| SPK-002, SPK-050, SPK-052 | PHASE-04 mid/exit | ty, multi-agent skills surface, fnox+age before freeze |
| SPK-001 | Before heavy template reliance in PHASE-04 | uv+ruff+ty+pytest smoke on sample trees |

**No circular phase dependencies.** Later phases must not redefine earlier exit
criteria.

---

## 7. Phase Overview

| Phase | Name | Depends on | User-visible outcome |
| ----- | ---- | ---------- | -------------------- |
| **PHASE-01** | Pure pipeline | None | `validate` / `plan` produce deterministic Construct; kind-qualified resolve; verify fields + `plan_sha256` + `error_class`; `--plan` bind API shape testable without writes |
| **PHASE-02** | Filesystem | PHASE-01 | Sibling unique stage; path confinement; exclusive place; fail non-empty dest; failures emit absolute `stage_path` |
| **PHASE-03** | Generate + verify + lock | PHASE-02 | First real `generate` to empty dest: lock production, default/strict/none, optional plan bind e2e, place only on success |
| **PHASE-04** | Catalog content + emit | PHASE-03 | Closed Core + AI-native + profiles + scripts contract; forbidden paths; kind-qualified catalog UX complete |
| **PHASE-05** | Hybrid + dogfood | PHASE-04 | Frozen public template CI green; foundry dogfoods Core; editor docs; release packaging path |
| **PHASE-06** | Harden | PHASE-05 | Residual risks accepted or mitigated; admission discipline; performance/ops polish; v1 readiness evidence |

---

## 8. Phases

## PHASE-01 — Pure pipeline

- **Status:** Planned
- **Objective:** Implement the write-free pipeline: parse/validate Project Spec,
  load closed catalog, resolve archetype + profiles (set membership; catalog apply
  order), resolve effective verify fields, Construct Generation Plan with
  `plan_sha256` and machine-readable `error_class` taxonomy; expose optional
  `--plan` bind **API shape** (match/mismatch) without performing stage writes.
- **User-visible outcome:** Operator/agent can run `foundry validate` and
  `foundry plan` (text/JSON) on a TOML spec and get a stable, hashable plan for
  the minimal `cli` cell; catalog list/show kind-qualified.
- **Depends on:** None
- **Requirements:** REQ-010 (partial: validate/plan), REQ-011, REQ-013,
  REQ-020..026, REQ-040..043, REQ-041, REQ-082 (purity), REQ-084 (plan fields),
  REQ-086 (bind shape), REQ-087 (kind in plan/catalog), REQ-091; REQ-001/003/083
  discipline
- **Milestones:** MS-001
- **Primary risks:** RSK-100 (non-determinism), RSK-109 (dual-id confusion),
  RSK-108 (bind path education later)

### Entry Criteria

- Revised specification v0.2 accepted as implementation authority.
- This plan proposed (and preferably accepted as delivery authority after
  plan-review/revision — product coding may start under owner risk before that,
  but phase *acceptance* for program delivery authority follows the revised plan).
- Empty or scaffold product package able to host pure modules per §10.1.

### Scope

- Package layout skeleton respecting purity: `spec`, `catalog`, `resolve`,
  `plan`, `report`; CLI wiring for `validate`, `plan`, `catalog list|show`,
  `version` (stub generate OK).
- TOML schema = 1 validation; unknown keys/profiles hard-fail; no secrets fields.
- Profile set semantics + catalog total apply order (FND-002).
- Effective verify resolution recorded on plan: `verify_mode`, `verify_source`
  (CLI > TOML > `default`) even though runners are later (FND-001).
- Plan-as-contract fields (§9.3); canonicalization + fixed `plan_sha256` test
  vector (FND-009).
- JSON error_class closed set for validation/resolve/plan_bind/internal (§12.1.1).
- Optional `--plan` load + recompute + hard-fail on digest/version/catalog
  mismatch **before** any write API is invoked (FND-004 shape).
- Kind-qualified catalog list/show and plan unit references (FND-007).
- Minimal catalog manifests sufficient for resolve (may use stub file inventories).

### Explicit Non-Goals

- Stage, place, render-to-disk, lock, or verify runners.
- Full template body content for all archetypes.
- GitHub template hybrid, dogfood, PyPI publish.
- Copier/Cookiecutter engine.

### Architecture and Components

- Follow revised-spec §10.1 map; enforce `plan` does not import `fsx` /
  `generate` / `cli` (REQ-082).
- Catalog as package data; digest in every plan (REQ-041).

### Integrations

- None external required (no network for validate/plan by default).

### Data or Migration Work

- N/A (greenfield). Schema version fixed at `1`.

### Evidence Spikes

| ID | Intent | Gate |
| -- | ------ | ---- |
| **SPK-100** | Pure plan golden for minimal CLI Construct | **PHASE-01 exit** |

### Testing and Verification

- Unit tests: pure packages only; no FS side effects for validate/plan.
- Golden: plan JSON (and text if applicable) for minimal `cli` + empty profiles.
- Fixture matrix: verify_source cli/toml/default; profile membership order
  independence; duplicate profiles fail; plan_sha256 vector; bind match/mismatch.
- Architecture test: import boundary purity.

### Security and Reliability

- Reject secret material in Project Spec (REQ-022).
- Deterministic plan body: no wall-clock/random in contract fields (RSK-100).

### Dogfooding or Operational Validation

- Not yet (dogfood is PHASE-05). Operators may exercise CLI manually.

### Rollback and Reconsideration Triggers

- Cannot produce stable `plan_sha256` across platforms → stop; fix
  canonicalization before PHASE-02.
- Purity boundary violated (plan imports write path) → reconsider layout before
  filesystem work.

### Exit Criteria

Observable evidence **all** true:

1. SPK-100 complete: checked-in golden plan for minimal `cli` matches
   recomputed Construct.
2. Fixed `plan_sha256` test vector passes.
3. Profile apply order fixtures: reordered TOML arrays with same membership
   yield identical plan body (excluding non-contract noise).
4. Verify fields present on plan; precedence matrix tests pass (REQ-084).
5. Kind-qualified catalog list/show distinguishes archetype/profile `data-etl`.
6. `--plan` bind mismatch fails with `error_class=plan_bind` without creating
   stage directories.
7. `validate` and `plan` leave destination tree untouched (property or e2e check).
8. MS-001 acceptance evidence recorded.

---

## PHASE-02 — Filesystem

- **Status:** Planned
- **Objective:** Implement fail-closed write primitives: unique sibling stage
  identity, path confinement under stage root, exclusive place to empty
  destination, preserve stage and emit absolute `stage_path` on failure.
- **User-visible outcome:** Generate orchestration can stage files and either
  atomically place a complete tree or leave the destination untouched with a
  recoverable stage path (still may use stub render content).
- **Depends on:** PHASE-01
- **Requirements:** REQ-012 (partial), REQ-030..032, REQ-090; REQ-083 (no
  blocking on FD openat); supports later REQ-031 place semantics
- **Milestones:** supports MS-002 (does not complete it alone)
- **Primary risks:** RSK-101 (leftover stages), RSK-105 (over-copy go-foundry FD)

### Entry Criteria

- PHASE-01 exit criteria met.
- Plan Construct available to name planned paths for stage writes (even if
  content is fixture bytes).

### Scope

- Stage naming: `.foundry-stage-<dest-basename>-<unique>`; collision allocates new
  name; never deletes prior failed stages (FND-011 / REQ-090).
- Fail if destination exists and is non-empty (REQ-030).
- Path confinement: no escape outside stage root (REQ-032).
- Exclusive place stage → destination; destination untouched on failure.
- Error/JSON reports include absolute `stage_path` after stage creation.
- Prefer same-filesystem parent for rename place (ops guidance §15).

### Explicit Non-Goals

- Full verify runners and lock production (PHASE-03).
- Full catalog emit content (PHASE-04).
- Existing-project merge/update (forbidden v1).
- FD-level openat transaction parity.

### Architecture and Components

- `fsx` module only for stage/place; no plan content invention (§10.2).
- `generate` may be thin driver for tests; full verify lifecycle is PHASE-03.

### Integrations

- OS filesystem only; Linux CI required.

### Data or Migration Work

- N/A. Failed stages are operator-deletable artifacts, not migrated data.

### Evidence Spikes

| ID | Intent | Gate |
| -- | ------ | ---- |
| **SPK-101** | Stage + exclusive place; fail non-empty dest | **PHASE-02 exit** |

### Testing and Verification

- e2e: empty dest place succeeds; non-empty dest fails; two consecutive failures
  leave two stages; `stage_path` parseable from JSON stderr report.
- Confinement tests: reject `..` / symlink escape attempts in planned paths.
- No destination mutation on mid-stage failure injection.

### Security and Reliability

- Fail-closed destination (partial generation never leaves half-written dest).
- Stage retention on failure for agent recovery (RSK-101 mitigated by clear
  `stage_path` messaging).

### Dogfooding or Operational Validation

- Manual failure injection acceptable; not product dogfood yet.

### Rollback and Reconsideration Triggers

- Cannot achieve exclusive place without dest corruption on Linux CI → block
  PHASE-03.
- Temptation to implement in-place merge for “convenience” → reject; requires
  DEC + spec change (REQ-033).

### Exit Criteria

1. SPK-101 complete with automated e2e.
2. REQ-030, REQ-031 (stage+place portion), REQ-032, REQ-090 acceptance evidence
   from revised-spec satisfied.
3. Documented stage naming and failure recovery notes for agents (can be brief
   in product AGENTS later expanded PHASE-04/05).
4. Ready to call fsx from generate orchestration in PHASE-03.

---

## PHASE-03 — Generate + verify + lock

- **Status:** Planned
- **Objective:** Complete the generate lifecycle on a **minimal catalog cell**
  (at least `cli` + core stub sufficient for lock+verify): optional plan bind
  e2e, render into stage, generate-time `uv.lock` produce/refresh, verify tiers
  default/strict/none with CLI>TOML>default precedence, exclusive place only on
  success; network disclosure for lock/sync.
- **User-visible outcome:** First successful `foundry generate --spec …` into an
  empty destination with **default verify** producing a tooling-sync-green tree
  (sync + ruff + ty — **not** pytest as default success).
- **Depends on:** PHASE-02
- **Requirements:** REQ-010..013, REQ-024 (bind execute), REQ-080, REQ-084,
  REQ-085, REQ-086 (e2e), REQ-091; partial REQ-052 lock behavior
- **Milestones:** MS-002
- **Primary risks:** RSK-102, RSK-107 (network/cost), RSK-001 (uv churn),
  RSK-100, RSK-108

### Entry Criteria

- PHASE-02 exit criteria met.
- PHASE-01 plan bind shape and verify field recording available.
- Operator tools installed for default verify: uv, ruff, ty.

### Scope

- `generate` orchestration: bind-or-rebuild → stage → lock → verify → place.
- Lock production before default/strict verify (FND-003 / REQ-085).
- Verify tiers per §9.5; strict = default + pytest; **no** pre-commit pre-place
  (FND-006).
- `--verify none`: loud warning; best-effort lock rules per spec; still no silent
  stale lock on successful place.
- Network need disclosed in docs/CLI help/warnings.
- Minimal emit content: enough pyproject + sources for ruff/ty/sync (full Core
  inventory is PHASE-04).
- JSON reports with `error_class` in {`render`,`lock`,`verify`,`place`,…}.

### Explicit Non-Goals

- Completing all three archetypes and all profiles (PHASE-04).
- Hybrid GitHub template CI (PHASE-05).
- Claiming multi-agent skill surface completeness (SPK-050 in PHASE-04).
- Pytest as default verify success.

### Architecture and Components

- `render`, `generate`, `verify` modules; tool runners sandboxable in tests.
- Custom engine only (REQ engine lock).

### Integrations

- uv lock/sync (network); ruff; ty; pytest (strict).

### Data or Migration Work

- N/A.

### Evidence Spikes

| ID | Intent | Gate |
| -- | ------ | ---- |
| **SPK-103** | Default verify cost/time and network disclosure acceptable for owner CI | **PHASE-03 exit** |
| SPK-001 (partial) | uv+ruff+ty+pytest smoke on generated minimal tree | Before expanding templates in PHASE-04 |

### Testing and Verification

- e2e matrix: default / strict / none; CLI vs TOML verify disagreement.
- Bind e2e: matching plan places; bit-flipped plan fails before stage writes with
  `plan_bind`.
- Lock matrix (minimal): default python pin; optional alternate pin if already
  supported; failure of lock aborts place.
- Verify failure aborts place; dest empty/untouched.
- Mock/sandbox runners where full tool cost is excessive; at least one real-tool
  e2e on Linux CI.

### Security and Reliability

- Fail-closed place; disclose network (RSK-102/107).
- No secrets in spec; no dotenv introduction in minimal templates.

### Dogfooding or Operational Validation

- Owner runs one real generate outside CI (optional but recommended).
- Full repo dogfood still PHASE-05.

### Rollback and Reconsideration Triggers

- Default verify cost unacceptable after SPK-103 → options: document `none` for
  offline, optimize runners, or owner DEC to adjust **only** via formal process
  (must not silently drop ty from default).
- Cannot produce honest locks on CI → block PHASE-04 content freeze.
- Agents systematically skip `--plan` (observed later) → strengthen docs/skills
  in PHASE-04/05 (RSK-108); not an architecture reopen.

### Exit Criteria

1. MS-002 acceptance evidence: documented command path yields successful generate
   to empty dest with default verify.
2. SPK-103 recorded (cost notes + disclosure present in user-facing help/docs).
3. Precedence matrix and bind e2e green.
4. Default success definition documented as tooling-sync green (not pytest).
5. Lock production path exercised; `uv sync --locked` used in default/strict.

---

## PHASE-04 — Catalog content + emit

- **Status:** Planned
- **Objective:** Flesh the closed catalog to full v1 Core, archetypes, profiles,
  and AI-native emit contracts; kind-qualified UX complete; forbidden-path
  conformance; scripts archetype inventory (REQ-088); lock matrix across
  pins/profiles; gate on ty/fnox/agent-surface spikes before freeze.
- **User-visible outcome:** Generating any of `cli` | `scripts` | `data-etl`
  with allowed profiles yields projects that match normative inventories,
  pass default verify, include AGENTS.md + closed skills only, and never emit
  dotenv secrets or Claude adapters.
- **Depends on:** PHASE-03
- **Requirements:** REQ-040, REQ-044 (admission process start), REQ-050..078
  (except REQ-077 → PHASE-05), REQ-087, REQ-088; REQ-052..063, REQ-070..076,
  REQ-078; supports REQ-001 hybrid prep
- **Milestones:** MS-003
- **Primary risks:** RSK-002 (ty), RSK-007/050 (fnox/dotenv), RSK-051, RSK-053,
  RSK-054, RSK-055, RSK-104, RSK-109

### Entry Criteria

- PHASE-03 exit criteria met (thin E2E generate path works).
- SPK-001 smoke green enough to author templates confidently.

### Scope

- Full catalog tree per §9.6 / §11.3 with versions lock.
- Core toolchain emit: uv, ruff, ty, pytest, pre-commit Default, fnox+age, GHA
  (REQ-050..058, REQ-062).
- Archetypes: `cli` (Typer Default), `scripts` (REQ-088), `data-etl` layout.
- Profiles: `http`, `hooks-hk`, `data-etl` composition rules.
- AI-native: AGENTS.md only; skills under `.agents/skills` only; MCP none;
  secrets protocol; definition of done; fresh-session packaging notes;
  anti-patterns (REQ-070..076, REQ-078).
- Forbidden-path tests: no `.env` secret storage patterns, no Claude paths, no
  kitchen-sink MCP.
- Kind-qualified catalog CLI complete (REQ-087).
- Catalog admission notes for future units (REQ-044) — process, not open catalog.
- Generate-time lock matrix: default pin; alternate `python_version`; with/without
  `http` profile (REQ-085 acceptance).

### Explicit Non-Goals

- Public GitHub template repo publish (PHASE-05).
- Foundry product dogfood conversion complete (PHASE-05).
- Editor integration docs (REQ-077 → PHASE-05).
- Renaming profile `data-etl` (OQ-106 deferred).
- Promoting hk to Core (requires DEC).
- MCP opt-in profile.

### Architecture and Components

- Catalog authoring tree packaged as data; custom renderer only.
- Foundry vs Generated agent surfaces separated (REQ-076): research skills do not
  ship into Generated Projects.

### Integrations

- GitHub Actions templates for Generated Projects.
- fnox + age local key workflow (documented).

### Data or Migration Work

- N/A for users. Catalog versioning via foundry version + catalog digest only.

### Evidence Spikes

| ID | Intent | Gate |
| -- | ------ | ---- |
| **SPK-002** | ty sample CLI tree + CI; freeze practical ty config | Before locking ty template defaults hard (OQ-001/002) |
| **SPK-050** | AGENTS.md + `.agents/skills` operable on target agents | Before claiming multi-agent emit completeness |
| **SPK-052** | fnox exec + age smoke | Before secrets skill freeze |
| **SPK-102** | Catalog expand + forbidden paths | **PHASE-04 exit** |
| SPK-003 | hk vs pre-commit latency | **Only if** promoting hk (out of default path) |

### Testing and Verification

- Golden plans per archetype × representative profile subsets.
- Conformance inventories: required paths present; forbidden absent.
- scripts archetype inventory tests (REQ-088).
- e2e generate all three archetypes with default verify.
- Forbidden-path suite (RSK-104).
- Dual-id docs/examples review (RSK-109).

### Security and Reliability

- fnox+age only for secrets; skills teach `fnox exec`; age keys out of git.
- No dotenv secret storage (RSK-007/050).
- Path confinement remains enforced on full file sets.

### Dogfooding or Operational Validation

- Generate sample projects used as fixtures; full foundry-repo dogfood PHASE-05.
- Optional: agent session tries add-cli-command / add-script skills (SPK-050).

### Rollback and Reconsideration Triggers

- SPK-002 shows ty unusable on Core sample → **do not demote ty silently**;
  escalate residual RSK-002 with owner DEC options (pin, config change, or formal
  exception path already required by REQ-055 risk linkage).
- SPK-052 fails → block secrets skill freeze; do not introduce dotenv fallback.
- Forbidden-path suite fails → block MS-003 / PHASE-04 exit.
- Catalog sprawl pressure → enforce REQ-044 admission; no open catalog.

### Exit Criteria

1. MS-003: all three archetypes golden emit + default verify e2e green.
2. SPK-002, SPK-050, SPK-052, SPK-102 complete or residual risk **explicitly**
   accepted by owner with documented limitations (no silent skip of Must REQs).
3. scripts inventory conformance passes (REQ-088).
4. Forbidden paths absent across goldens.
5. Kind-qualified catalog UX goldens stable.
6. Agent DoD docs emit honestly (pytest after place; default ≠ pytest).

---

## PHASE-05 — Hybrid template + dogfood

- **Status:** Planned
- **Objective:** Ship hybrid GitHub template as CI-generated snapshot of frozen
  public template Project Spec cell; dogfood foundry product on Core conventions;
  editor documentation; release packaging path; polish operator docs including
  plan-bind workflow (RSK-108).
- **User-visible outcome:** Public template path and CLI path stay single-SoT;
  foundry itself develops under Core-like conventions; release/tag story clear.
- **Depends on:** PHASE-04
- **Requirements:** REQ-001, REQ-077, REQ-081, REQ-089; release aspects of
  REQ-010 `version`; Blueprint hybrid L1
- **Milestones:** MS-004, MS-005
- **Primary risks:** RSK-103 (template drift), RSK-108, RSK-005 (macOS CI cost),
  OQ-105 branding

### Entry Criteria

- PHASE-04 exit criteria met.
- Frozen cell fields available as checked-in template Project Spec (§9.9 / REQ-089).

### Scope

- Checked-in frozen public template Project Spec:
  `archetype=cli`, `profiles=[]`, name `python-foundry-template`, python 3.13
  default (REQ-089).
- CI job: generate snapshot from catalog SoT and fail on drift (REQ-081).
- Process docs: forbid hand-editing template as second catalog.
- Dogfood: foundry product repository adopts Core conventions appropriate to an
  application-shaped uv project (tooling, AGENTS.md discipline, quality gates)
  without violating research-program vs product surface rules (REQ-076).
- Editor documentation only (REQ-077) — no mandatory `.cursor/rules` emit.
- Release: version command reports foundry version + catalog digest; uv/PyPI
  install path decision recorded in ops notes (spec defers details to plan —
  choose **uv-native publish** path; exact registry steps are milestone evidence,
  not a backlog).
- Teach validate → plan → `generate --plan` in Generated Project and foundry
  AGENTS/skills (RSK-108).

### Explicit Non-Goals

- Marketplace distribution.
- Dual-maintaining template content by hand.
- Windows CI.
- Closing all residual ecosystem risks (PHASE-06).

### Architecture and Components

- Template repo or published snapshot artifact is **output** of generate, not SoT.
- Catalog remains SoT inside foundry product package.

### Integrations

- GitHub Actions (foundry CI + template drift job).
- Optional macOS CI (not required for exit).

### Data or Migration Work

- N/A. Snapshot regeneration replaces prior snapshot wholly.

### Evidence Spikes

- None new required; carry residual SPK outcomes into dogfood validation.

### Testing and Verification

- CI generate+diff for frozen cell.
- Golden alignment: template snapshot matches catalog goldens for that cell.
- Dogfood: foundry CI runs ruff, ty, pytest on the product itself.
- Docs lint/link checks as practical.

### Security and Reliability

- Release artifacts free of secrets; age keys never published.
- Template snapshot contains no secret material.

### Dogfooding or Operational Validation

- **Primary dogfood gate:** MS-005 — foundry repo uses Core conventions and is
  developed/verified with the same command surface philosophy as Generated
  Projects (uv, ruff, ty, pytest, AGENTS.md).
- Owner generates a real project from CLI and from template path once.

### Rollback and Reconsideration Triggers

- Template drift CI flaky due to non-determinism → reopen PHASE-01/03
  determinism before release.
- Dogfood reveals Core emit unusable for foundry itself → fix catalog in
  PHASE-04 scope before calling hybrid “done”; do not invent a second Core.
- CLI rename (OQ-105) if required → branding-only change set; must not rewrite
  architecture.

### Exit Criteria

1. MS-004: template snapshot CI green with checked-in frozen spec.
2. MS-005: dogfood evidence recorded (product CI + Core conventions in-repo).
3. REQ-081/089 acceptance evidence present.
4. REQ-077 editor docs published at agreed doc path.
5. Plan-bind workflow documented for agents (mitigate RSK-108).
6. Version + catalog digest reported by CLI.

---

## PHASE-06 — Harden

- **Status:** Planned
- **Objective:** Accept or mitigate residual delivery risks; performance and ops
  polish; catalog admission discipline proven; optional strict-tuning notes;
  declare v1 implementation readiness against revised-spec §29.2.
- **User-visible outcome:** Stable v1 suitable for owner daily use; known
  limitations documented; no open Must REQ without evidence or explicit residual
  acceptance.
- **Depends on:** PHASE-05
- **Requirements:** residual of REQ-002, REQ-003, REQ-033, REQ-044, REQ-083;
  performance expectations §19; ops §15–17
- **Milestones:** MS-006
- **Primary risks:** RSK-001, RSK-002 residual, RSK-055, RSK-107 residual,
  RSK-006 methodology (no new load-bearing claims)

### Entry Criteria

- PHASE-05 exit criteria met (hybrid + dogfood).

### Scope

- Performance spot-checks against §19 expectations (plan pure speed; generate
  cost already informed by SPK-103).
- Residual risk register review: each High/Medium delivery risk either mitigated
  with evidence or owner-accepted with limitation text.
- Catalog admission dry-run: process for adding a unit is documented; no actual
  marketplace.
- Strict verify tuning notes (still no pre-commit pre-place).
- Offline/generate `none` documentation hardened.
- Final conformance sweep: Must REQs traceability checklist complete.
- OQ-105 resolved by owner decision or explicitly left provisional in release
  notes.

### Explicit Non-Goals

- Post-v1 deferred work (§26): update/merge, remote catalogs, MCP profile,
  monorepo workspaces, etc.
- Reopening rejected work (§27).
- Building a coding backlog for v2.

### Architecture and Components

- No architecture changes; harden tests, docs, CI only unless a blocking defect
  forces a fix within existing REQs.

### Integrations

- Release pipeline stabilization (tag ↔ version command).

### Data or Migration Work

- N/A.

### Evidence Spikes

- Only reopen SPK-002/052 if residual regressions appear.

### Testing and Verification

- Full regression: unit + golden + conformance + e2e generate matrix.
- Negative tests: non-goals still rejected (Windows paths not supported;
  unknown profiles fail; non-empty dest fails).

### Security and Reliability

- Final forbidden-path and secrets protocol audit.
- Stage hygiene docs for agents (RSK-101).

### Dogfooding or Operational Validation

- Continued dogfood; at least one full owner project generated post-harden
  candidate.

### Rollback and Reconsideration Triggers

- Must REQ still red with no residual acceptance → not v1; return to owning phase.
- Pressure to add Windows/marketplace/dotenv → refuse without Blueprint/DEC.

### Exit Criteria

1. MS-006 acceptance evidence (v1 readiness).
2. Must REQ traceability table marked satisfied or residual-accepted with owner.
3. Delivery risk register (§16) reviewed; each High/Medium item mitigated or owner-accepted.
4. No Critical open delivery defects against revised-spec v0.2.
5. Release notes list known limitations (ty residual, network for lock, provisional
   CLI name if still provisional).

---

## 9. Milestones

### MS-001 — `foundry plan` golden stable for cli

- **Phase:** PHASE-01
- **Outcome:** Deterministic plan Construct for minimal `cli` archetype is golden
  and hash-stable.
- **Prerequisites:** Spec/catalog/resolve/plan modules; SPK-100.
- **Acceptance evidence:**
  - Checked-in golden plan JSON for minimal `cli` + `profiles=[]`.
  - `plan_sha256` fixed test vector passes on Linux CI.
  - Reordered profile membership fixtures (when profiles present) do not change
    apply order relative to catalog.
  - Kind-qualified unit references present in plan output.
- **Blocks:** PHASE-02 start as *accepted* program gate; PHASE-03 bind e2e.

### MS-002 — First successful `generate` to empty dest with default verify

- **Phase:** PHASE-03
- **Outcome:** Thin end-to-end generate works.
- **Prerequisites:** MS-001; PHASE-02 (SPK-101); lock + default verify runners.
- **Acceptance evidence:**
  - Automated e2e: empty destination; `generate` with effective `default`; exit 0;
    dest contains project; stage not left behind on success.
  - Default verify ran tooling-sync steps (sync --locked, ruff, ty) — not pytest
    as the success criterion.
  - Failure injection: verify fail → dest untouched + `stage_path` reported.
  - Optional `--plan` match succeeds; mismatch → `error_class=plan_bind` before
    stage writes.
- **Blocks:** PHASE-04 full catalog freeze; MS-003.

### MS-003 — All three archetypes golden emit

- **Phase:** PHASE-04
- **Outcome:** `cli`, `scripts`, and `data-etl` emit contracts are complete and
  tested.
- **Prerequisites:** MS-002; SPK-002, SPK-052, SPK-102 (and SPK-050 for agent
  surface claims).
- **Acceptance evidence:**
  - Golden plan + conformance inventory per archetype.
  - scripts inventory satisfies REQ-088.
  - Default verify e2e green for each archetype at default python pin.
  - Forbidden-path suite green (no dotenv secret storage, no Claude adapters,
    MCP default none).
  - AI-native paths present: AGENTS.md + required skills only.
- **Blocks:** MS-004, MS-005.

### MS-004 — Template snapshot CI green

- **Phase:** PHASE-05
- **Outcome:** Hybrid GitHub template is a generated snapshot of the frozen cell.
- **Prerequisites:** MS-003; checked-in frozen public template Project Spec.
- **Acceptance evidence:**
  - Frozen spec file matches REQ-089 field set.
  - CI job regenerates snapshot and fails on drift vs catalog goldens for that cell.
  - Process doc forbids hand-edit as second SoT.
- **Blocks:** public hybrid claim; MS-006 hybrid portion.

### MS-005 — Dogfood: foundry repo uses Core conventions

- **Phase:** PHASE-05
- **Outcome:** Foundry product is developed under Core-aligned tooling and agent
  surface discipline.
- **Prerequisites:** MS-003; product CI capable of ruff/ty/pytest.
- **Acceptance evidence:**
  - Product CI runs locked uv sync + ruff + ty + pytest on foundry itself.
  - Product AGENTS.md (or equivalent product rules) exists without shipping
    research-only skills into Generated Project templates.
  - Owner attestation or checklist that daily development uses the Core command
    surface (no parallel undocumented toolchain).
- **Blocks:** MS-006 readiness claim.

### MS-006 — v1 delivery readiness

- **Phase:** PHASE-06
- **Outcome:** Implementation is ready for owner v1 use under revised-spec §29.2.
- **Prerequisites:** MS-004, MS-005; residual risk review.
- **Acceptance evidence:**
  - Must REQ traceability complete (satisfied or owner residual-accepted).
  - Regression suite green on Linux.
  - Release notes list limitations (RSK-002/107/108, OQ-105 as applicable).
  - No open Critical defects against implementation authority.
- **Blocks:** Formal “v1 shipped” declaration (owner).

---

## 10. Cross-Phase Integration

| Integration seam | Phases | Strategy |
| ---------------- | ------ | -------- |
| Plan → Generate bind | 01→03 | Shape in 01; e2e in 03; teach in 04–05 |
| Construct → Stage paths | 01→02→03 | Plan file list drives render; confinement tests span 02–04 |
| Verify fields → Runners | 01→03 | Record early; execute later; single precedence implementation |
| Minimal cell → Full catalog | 03→04 | Do not rewrite lifecycle; only expand catalog data + goldens |
| Catalog SoT → Template snapshot | 04→05 | Generate-only snapshot; CI drift gate |
| Generated Core → Foundry dogfood | 04→05 | Adopt conventions; keep research skills out of emit |
| Error taxonomy | 01–03 | Extend coverage as new failure classes become reachable |
| Kind-qualified IDs | 01→04 | Plan/catalog in 01; full UX + docs in 04 |

**Continuous integration rule:** Each phase adds automated tests that remain green
in later phases (no deleting goldens to “move fast”).

**Thin E2E rule:** PHASE-03 must produce a usable generate path before PHASE-04
breadth; avoid multi-phase infrastructure with no user-visible generate.

---

## 11. Data or Migration Sequencing

| Topic | Plan |
| ----- | ---- |
| User data migration | **N/A** — greenfield generator; no existing-project update (REQ-033) |
| Schema evolution | Project Spec `schema = 1` only in v1; bump requires explicit support |
| Catalog evolution | Closed admission (REQ-044); digest changes invalidate unbound assumptions; bind path detects digest mismatch |
| Failed stages | Not migrated; operator deletes; unique names prevent clobber |
| Template snapshots | Full regenerate/replace, not merge |
| Secrets | Never migrate plaintext; fnox ciphertext only if present |

---

## 12. Testing Strategy by Phase

| Phase | Unit | Golden | Conformance | e2e | Spikes |
| ----- | ---- | ------ | ----------- | --- | ------ |
| PHASE-01 | spec/resolve/plan pure | plan JSON cli | kind-qualified catalog | write-free CLI | SPK-100 |
| PHASE-02 | fsx helpers | — | path confinement | stage/place/fail | SPK-101 |
| PHASE-03 | verify orchestration | minimal generate tree | — | generate default/strict/none + bind | SPK-103 |
| PHASE-04 | render edge cases | all archetypes × profiles subset | inventories + forbidden | generate ×3 archetypes | SPK-002/050/052/102 |
| PHASE-05 | — | frozen cell snapshot | template=catalog | CI drift job; dogfood CI | — |
| PHASE-06 | regression | full golden suite | full forbidden | full matrix | residual only |

**Foundry product tests** follow revised-spec §16.1. **Generated Project tests**
are emitted content (§16.2) validated via conformance and strict verify.

---

## 13. Security Activities by Phase

| Phase | Activities |
| ----- | ---------- |
| PHASE-01 | Reject secrets in Project Spec; deterministic plans; no network by default for plan |
| PHASE-02 | Path confinement; fail-closed destination; stage path disclosure without leaking secrets |
| PHASE-03 | Network disclosure for lock/sync; no place on verify fail; avoid embedding secrets in errors |
| PHASE-04 | fnox+age templates + skills; forbidden dotenv/Claude/MCP kitchen-sink; SPK-052 |
| PHASE-05 | Release/template snapshot secret hygiene; dogfood without committing age private keys |
| PHASE-06 | Final forbidden-path audit; residual RSK-050/051/104 review |

---

## 14. Operations and Release Readiness

| Concern | When | Policy |
| ------- | ---- | ------ |
| Linux CI | PHASE-01 onward | Required: uv locked sync, ruff, ty, pytest as product hardens |
| macOS CI | optional | OQ-005; not an exit gate |
| Catalog validation in CI | PHASE-01/04 | Validate catalog + golden plans |
| Template drift CI | PHASE-05 | Generate+diff frozen cell |
| Versioning | PHASE-05 | `foundry version` ↔ release tag; catalog digest reported |
| Publish | PHASE-05/06 | uv-native package publish path documented; PyPI optional per owner |
| Offline ops | PHASE-03+ | Document `--verify none` + cached uv limitations |
| Stage cleanup | PHASE-02+ | Docs for leftover stages (RSK-101) |
| Incident/rollback | all | Destination never half-written; rerun generate on empty dest |

Release readiness for owner v1 = MS-006 + PHASE-06 exit, not merely MS-002.

---

## 15. Dogfooding

| Stage | Dogfood activity |
| ----- | ---------------- |
| PHASE-01–02 | Optional manual CLI only |
| PHASE-03 | Owner runs one real minimal generate |
| PHASE-04 | Use generated fixtures as day-to-day samples; agent skill trials (SPK-050) |
| PHASE-05 | **MS-005:** convert/align foundry product repo to Core conventions; develop foundry with Core gates |
| PHASE-06 | Generate at least one real personal project from release candidate |

**Rule:** Dogfood before broad feature expansion beyond the closed v1 catalog.
Do not add new archetypes/profiles during dogfood to “make dogfood work” without
REQ-044 admission and spec authority.

**Hybrid dogfood:** Template path and CLI path must produce the same frozen cell
bytes (modulo documented non-goals).

---

## 16. Risk Register

Delivery-focused register (product risks from revised-spec §24 carried forward
with sequencing). Severity is residual **during delivery**.

| ID | Risk | Sev | Sequencing / mitigation | Phase gate |
| -- | ---- | --- | ----------------------- | ---------- |
| RSK-002 | ty maturity as Core | Med–High | SPK-002 before template freeze; pin ty; CI fail-closed; no silent demotion | PHASE-04 |
| RSK-007 | fnox Core + no dotenv fallback | Med | Templates + skills; SPK-052 | PHASE-04 |
| RSK-050 | Agents reintroduce dotenv secrets | High | Forbidden paths + secrets skill + reviews | PHASE-04–06 |
| RSK-107 | Generate-time uv lock network/cost | Med | SPK-103; disclose; document offline `none` | PHASE-03 |
| RSK-108 | Agents skip `--plan` bind | Med | AGENTS.md + skills teach bind; docs in PHASE-05 | PHASE-04–05 |
| RSK-100 | Plan/generate non-determinism | High if present | Canonical JSON; goldens; ban time/random | PHASE-01–03 |
| RSK-101 | Leftover stage confuses agents | Med | `stage_path` mandatory; docs | PHASE-02 |
| RSK-102 | Verify needs network | Med | Disclose; `none` mode | PHASE-03 |
| RSK-103 | Template snapshot drift | Med | CI regenerate+diff | PHASE-05 |
| RSK-104 | Catalog reintroduces dotenv/Claude | High | Forbidden-path tests SPK-102 | PHASE-04 |
| RSK-001 | uv pre-1.0 churn | Med | Pin uv; lockfiles | PHASE-03–06 |
| RSK-051 | Claude adapters reintroduced | Med | Forbidden paths | PHASE-04 |
| RSK-053 | MCP kitchen-sink creep | Med | REQ-072 emit none | PHASE-04 |
| RSK-054 | Agents use Pyright, ignore ty | Med | DoD + CI ty | PHASE-04–05 |
| RSK-055 | Skill catalog sprawl | Med | Closed set; admission | PHASE-04–06 |
| RSK-105 | Over-copy go-foundry FD complexity | Med | Stage-root first; stop condition | PHASE-02 |
| RSK-109 | data-etl dual-id confusion | Low | Kind-qualified UX | PHASE-01–04 |
| RSK-005 | macOS CI cost | Low | Optional macOS | PHASE-05 |
| OQ-105 | CLI name provisional | Branding | Owner DEC anytime; non-blocking | PHASE-05–06 |

---

## 17. Open Questions

Delivery / sequencing questions only. Product OQs resolved in the revised spec
are **not** reopened here.

| ID | Topic | Blocking? | Notes |
| -- | ----- | --------- | ----- |
| OQ-105 | Final CLI binary name | No | Provisional `foundry`; rename is branding |
| OQ-002 | SPK-002 exact calendar timing | No | Must complete before PHASE-04 ty freeze |
| OQ-054 | Foundry product closed skill set beyond research | Partial | Product implementation concern; not Generated Core |
| OQ-PLAN-01 | Product code in this repo vs separate implementation repo | No | Phase evidence is behavioral; owner chooses layout |
| OQ-PLAN-02 | PyPI publish vs uv private/index only for v1 | No | Decide by PHASE-05 release notes |
| OQ-106 | Rename profile `data-etl` | No | Deferred; kind-qualified UX first |

If a sequencing conflict appears to require REQ change → escalate as plan-review
finding or DEC; do not edit REQs from this plan.

---

## 18. Rollback and Reconsideration Triggers

| Trigger | Action |
| ------- | ------ |
| Stable `plan_sha256` impossible across CI | Halt before PHASE-02; fix canonicalization |
| Exclusive place corrupts dest on failure | Halt before PHASE-03; fix fsx |
| Default verify cost impossible after SPK-103 | Owner options within REQ-080; no silent ty drop |
| SPK-002 ty failure | Residual RSK-002 process; **no** dotenv-like “fallback toolchain” without DEC |
| SPK-052 fnox failure | Block secrets freeze; **no** dotenv fallback |
| Forbidden-path failures | Block MS-003 / release |
| Template drift non-determinism | Return to plan determinism + lock honesty |
| Demand for Windows / marketplace / update-merge | Refuse; Blueprint/DEC only |
| Demand to demote ty or fnox | Refuse without DEC |
| Agents ignore `--plan` in dogfood | Strengthen docs/skills; consider UX warnings; not architecture rewrite |
| Must REQ red at PHASE-06 | Not v1; return to owning phase |

**Reversibility preference:** Prefer catalog content and docs changes over
lifecycle redesign once PHASE-03 has exited.

---

## 19. Requirement-to-Phase Traceability

Must-priority and normative REQs mapped to **primary** delivery phases.
Cross-cutting REQs list all phases that provide evidence. Cite only; do not
renumber REQs.

| REQ | Priority (spec) | Phase(s) | Milestone / evidence notes |
| --- | --------------- | -------- | -------------------------- |
| REQ-001 | Must | PHASE-01..05 | Hybrid complete at MS-004 |
| REQ-002 | Must | All | macOS/Linux only; enforced by CI targets |
| REQ-003 | Must | All | Non-goals tests / review gates |
| REQ-010 | Must | PHASE-01..03 | Commands online by MS-002 |
| REQ-011 | Must | PHASE-01 | Write-free validate/plan |
| REQ-012 | Must | PHASE-02..03 | Sole dest mutator |
| REQ-013 | Must | PHASE-01 | Non-interactive first |
| REQ-020 | Must | PHASE-01 | Schema 1 parse |
| REQ-021 | Must | PHASE-01 | Unknown keys/profiles fail |
| REQ-022 | Must | PHASE-01 | No secrets in spec |
| REQ-023 | Must | PHASE-01 | Path + stdin |
| REQ-024 | Must | PHASE-01..03 | Plan-as-contract + bind |
| REQ-025 | Must | PHASE-01 | Plan encoding |
| REQ-026 | Must | PHASE-01 | plan_sha256 |
| REQ-030 | Must | PHASE-02 | Non-empty dest fail |
| REQ-031 | Must | PHASE-02 | Stage + exclusive place |
| REQ-032 | Must | PHASE-02 | Path confinement |
| REQ-033 | Must | All | No update/merge |
| REQ-040 | Must | PHASE-01..04 | Closed catalog |
| REQ-041 | Must | PHASE-01 | Catalog digest in plan |
| REQ-042 | Must | PHASE-01 | Exactly one archetype |
| REQ-043 | Must | PHASE-01 | Profile composition |
| REQ-044 | Must | PHASE-04+ | Admission discipline |
| REQ-050 | Must | PHASE-04 | Core toolchain invariants |
| REQ-051 | Must | PHASE-04 | Python version policy |
| REQ-052 | Must | PHASE-03..04 | uv + lock commit behavior |
| REQ-053 | Must | PHASE-04 | Layout by archetype |
| REQ-054 | Must | PHASE-04 | Ruff |
| REQ-055 | Must | PHASE-04 | ty Required (+ SPK-002) |
| REQ-056 | Must | PHASE-04 | pytest Required emit |
| REQ-057 | Must | PHASE-04 | Hooks Default pre-commit |
| REQ-058 | Must | PHASE-04 | fnox+age; no dotenv secrets |
| REQ-059 | Must | PHASE-04 | HTTP profile |
| REQ-060 | Must | PHASE-04 | Typer Default CLI |
| REQ-061 | Must | PHASE-04 | data-etl profile defaults |
| REQ-062 | Must | PHASE-04 | GHA Core CI |
| REQ-063 | Must | PHASE-04 | Command surface docs |
| REQ-070 | Must | PHASE-04 | AGENTS.md only |
| REQ-071 | Must | PHASE-04 | Skills under `.agents/skills` |
| REQ-072 | Must | PHASE-04 | MCP default none |
| REQ-073 | Must | PHASE-04 | Agent secrets protocol |
| REQ-074 | Must | PHASE-04 | Definition of done |
| REQ-075 | Must | PHASE-04 | Fresh-session packaging |
| REQ-076 | Must | PHASE-04..05 | Foundry vs Generated surfaces |
| REQ-077 | Should | PHASE-05 | Editor documentation |
| REQ-078 | Must | PHASE-04 | AI-native anti-patterns |
| REQ-080 | Must | PHASE-03 | Default verify mode |
| REQ-081 | Must | PHASE-05 | Template snapshot SoT |
| REQ-082 | Should | PHASE-01..03 | Module layout / purity |
| REQ-083 | Must | All | go-foundry transfer discipline |
| REQ-084 | Must | PHASE-01,03 | Effective verify resolution |
| REQ-085 | Must | PHASE-03,04 | Generate-time uv.lock |
| REQ-086 | Must | PHASE-01..03 | Optional `--plan` bind |
| REQ-087 | Must | PHASE-01,04 | Kind-qualified catalog identity |
| REQ-088 | Must | PHASE-04 | scripts archetype contract |
| REQ-089 | Must | PHASE-05 | Frozen public template cell |
| REQ-090 | Must | PHASE-02 | Stage identity + failure path |
| REQ-091 | Must | PHASE-01..03 | JSON error_class taxonomy |

---

## 20. Definition of Plan Completion

This **implementation plan artifact** is complete when:

1. All sections required by `program/contracts/implementation-plan.md` are present
   and non-placeholder.
2. Status remains **Proposed — pending plan adversarial review** until
   plan-review and plan-revision produce delivery authority
   (`docs/plans/02-implementation-plan-revised.md` per program graph).
3. Phases PHASE-01..06 and milestones MS-001..MS-006 have executable entry/exit
   or acceptance evidence.
4. Must REQs are traced; residual risks from §30.4 are sequenced.
5. No coding backlog is included.
6. Independent `research-validate` passes mechanical checks.
7. Human accepts the stage and records `accepted_commit` in
   `research-program.toml` (human-owned; not claimed by this writing session).

This plan is **not** product v1 completion. Product v1 completion is MS-006 /
PHASE-06 against revised-spec §29.2.

---

## 21. Completion Checklist

- [x] All required plan sections present and non-placeholder
- [x] Actual plan date recorded (2026-08-01)
- [x] Status: **Proposed — pending plan adversarial review** (not delivery authority)
- [x] Subordinate to revised specification v0.2 (no REQ/architecture contradictions)
- [x] Phases/milestones only — **no** coding backlog or task packets
- [x] Executable entry/exit criteria (observable evidence)
- [x] Early thin end-to-end path present (PHASE-03 / MS-002)
- [x] Spikes scheduled as gates (SPK-100..103, SPK-001/002/050/052)
- [x] Dogfooding and hybrid template sequencing present (PHASE-05 / MS-004..005)
- [x] Security, testing, ops addressed by phase
- [x] Rollback/reconsideration triggers present
- [x] Requirement-to-phase traceability for Must REQs
- [x] Residual risks (ty, fnox, lock network, plan-bind) sequenced
- [x] Blueprint non-goals preserved
- [x] Allowed file scope only (`docs/plans/01-implementation-plan.md`)
- [x] No plan-review or implementation started as main work
- [x] Independent validation passed (`docs/validations/01-implementation-plan-validation.md`)
- [x] Human approval obtained (2026-08-01)
- [x] `accepted_commit` recorded in manifest (`ab728951a52c1d69cc30e6151034d2af256bed5b`)

---

*End of implementation plan v0.1 — proposed delivery sequence; pending plan
adversarial review. Implementation authority remains revised specification v0.2.*
