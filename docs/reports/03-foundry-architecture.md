# Foundry Architecture

- **Artifact type:** Focused Research Report
- **Program:** python-foundry
- **Stage:** `research-foundry-architecture`
- **Status:** Accepted
- **Version:** 0.1.1
- **Created:** 2026-08-01
- **Last updated:** 2026-08-01
- **Actual research date:** 2026-08-01
- **Accepted:** 2026-08-01 (human approval; Git commit in `research-program.toml`)
- **Validation:** Pass with mechanical corrections (`docs/validations/03-foundry-architecture-validation.md`)
- **Depends on:** Accepted Program Blueprint; Accepted Research Charter; Accepted
  ecosystem report v0.2; Accepted AI-native report v0.2
- **Commissioning prompt:** `docs/prompts/03-foundry-architecture-prompt.md`
- **Recommendation range:** REC-200..REC-212 (remaining REC-213..299 reserved)
- **Evidence base:**
  - Exa Deep (`deep-reasoning`) multi-query run
    `scripts/exa-output/architecture-20260801T000131Z/` (~$0.15; local raw; not governing)
  - Grok session deep-research memos under that run’s `grok/` (lifecycle/plan/write;
    catalog/emit; go-foundry transfer)
  - Primary prior art: [go-foundry-research](https://github.com/robertguss/go-foundry-research)
    architecture report; [go-foundry-cli](https://github.com/robertguss/go-foundry-cli)
    tree and source (catalog, plan, fsx, generate, spec)
  - Official generator docs: Copier, Cookiecutter, GitHub template repositories
  - Inherited G1 reports (full)

> Research reports are **evidence and recommendations**, not commandments.
> Synthesis consumes this report after acceptance.
> Ecosystem Core locks and AI-native surface locks are **inherited emit
> constraints**, not reopened tool-selection or agent-product questions.
> **go-foundry is prior art only** — adapt with explicit Adopt/Adapt/Reject.

## 1. Artifact Metadata

| Field | Value |
| ----- | ----- |
| Program ID | python-foundry |
| Stage ID | research-foundry-architecture |
| Primary question | What architecture implements hybrid generation (spec → plan → generate), Core/profiles/catalog, and AI-native surfaces for a Python/uv foundry CLI, adapting go-foundry where appropriate? |
| Rigor | standard |
| Operator | robertguss |

## 2. Executive Answer

Implement **python-foundry** as a **planner-led Python/`uv` CLI** that:

1. Reads a **strict TOML Project Specification** (`schema = 1`)
2. Resolves **exactly one archetype** + a **closed ordered profile set**
3. Builds an **immutable Generation Plan** (text + JSON; content digests)
4. Renders into a **sibling staging directory**
5. Optionally runs **tiered verification** (`uv sync` / ruff / ty / pytest)
6. **Exclusively places** the finished tree at the destination (no merge, no
   default overwrite of existing non-empty destinations)
7. Emits **locked Core** and **AI-native surfaces as invariants**, not optional extras

| Layer | Recommendation |
| ----- | -------------- |
| CLI lifecycle | `foundry validate`, `foundry plan`, `foundry generate`, `foundry catalog list\|show`, `foundry version` |
| Spec | TOML Project Spec, explicit `--spec` (or path arg); non-interactive first |
| Plan | **Plan-as-contract** — validate/plan share pure pipeline; generate executes the same plan |
| Writes | Sibling stage → verify (tiered) → exclusive place; fail if dest exists/non-empty |
| Catalog | Closed `core` + `archetypes/{cli,scripts,data-etl}` + `profiles/{http,hooks-hk,data-etl}` + `versions.toml` |
| Engine | **Custom planner-led renderer** (not Copier/Cookiecutter-as-engine) |
| Foundry layout | `src/python_foundry/{cli,spec,catalog,resolve,plan,render,fsx,generate,verify,report}` |
| GitHub template | **Generated artifact** from catalog (CI), not dual-edited SoT |
| AI-native emit | Root `AGENTS.md` + `.agents/skills/*` only; **no** Claude adapters; MCP none |
| Post-gen DoD | Document REC-013; default verify tier before place; strict tier optional |

**go-foundry transfer (summary):** Adopt lifecycle, TOML spec, immutable plan,
closed catalog shape, conservative writes, pure validate/plan. Adapt embed
(package data), verify tools (uv/ruff/ty/pytest), archetypes/profiles for Python.
Reject TUI archetype, Go-only stacks, remote/plugin catalogs, v1 update-sync,
Windows, Claude adapters.

## 3. Scope and Exclusions

### In scope

- Foundry CLI commands and lifecycle
- Project Specification format and validation
- Generation Plan model and binding
- Filesystem / write / conflict semantics
- Closed catalog model; archetype × profile composition
- Emit contracts for ecosystem Core and AI-native surfaces
- Foundry product module layout (Python/uv)
- GitHub template surface coherence
- go-foundry Adopt/Adapt/Reject
- Post-generate verification policy
- v1 extension / closed-set discipline

### Out of scope

- Re-selecting uv/ruff/ty/pytest/fnox or reopening AI-native standards
- Product implementation / shipping the binary
- Granular coding backlog
- Unlimited profiles, plugins, MCP marketplaces
- Windows; notebooks; web framework zoo
- Existing-project upgrade/sync as v1 requirement
- Synthesis REQs (downstream)

## 4. Inherited Constraints

### Blueprint locks (selected)

| ID | Constraint |
| -- | ---------- |
| L1 | Hybrid: generator CLI + strong default Core + GitHub template surface |
| L2 | Foundry itself is Python/`uv` |
| L3 | macOS + Linux only; never Windows |
| L6 | Archetypes: CLI + scripts; data/ETL in scope; no notebooks |
| L9 | AI-native first; closed agent tooling |
| L10 | go-foundry adapt, do not copy blindly |

### Ecosystem Core locks (Accepted v0.2)

| Lock | Source |
| ---- | ------ |
| Python ≥3.12 / default 3.13; uv + lockfile; src/; Ruff; **ty** Required; pytest; pre-commit Default; **fnox+age**; no dotenv secrets; GHA; Typer CLI default | REC-001..014 |
| Command surface `uv sync` / `uv run …` / `fnox exec -- …` | REC-013 |
| Profiles: `http`, `hooks-hk`, `data-etl` | REC-014 |

### AI-native locks (Accepted v0.2)

| Lock | Source |
| ---- | ------ |
| Root **AGENTS.md only**; skills under **`.agents/skills/` only** | REC-100..102 |
| MCP default none; no kitchen sink | REC-104 |
| No Claude Code design target; no `CLAUDE.md` / `.claude/` Core emit | REC-100; EVD-121 |
| Amplify REC-013; fnox exec secrets protocol | REC-105..107 |
| Core skill purposes: `quality-gates`, `secrets-fnox`, `add-cli-command`, `add-script` | REC-103 |

## 5. Methodology

1. Read Blueprint, Charter, commissioning prompt, and **full** accepted G1 reports.
2. Ran **10 Exa Deep `deep-reasoning` queries** via
   `scripts/exa_architecture_evidence.py` (2026-08-01, ~$0.15).
3. Produced **three Grok session deep-research memos** (lifecycle/plan/write;
   catalog/emit; go-foundry transfer) under the Exa run directory.
4. Inspected **go-foundry-research** architecture report and **go-foundry-cli**
   source layout (catalog manifests, plan, fsx transaction, generate, spec).
5. Fetched official Copier, Cookiecutter, and GitHub template documentation.
6. Compared alternatives per decision area; scored against locks.
7. Where Exa preferred Copier-as-engine / plan-as-preview / YAML, **challenged**
   with go-foundry planner-led evidence and G1 emit-invariant needs.
8. No local executable spike in this pass (architecture contracts documentary +
   prior-art inspection); SPK-100.. recommended for early implementation.

**Limitations:** Exa/Grok outputs are synthesized evidence; load-bearing claims
cite primary URLs or inspected prior-art paths. Raw dumps are not Git authority.

## 6. Source Quality and Limitations

| Tier | Use |
| ---- | --- |
| 1 — Official docs (Copier, Cookiecutter, GitHub, Astral) | Write flags, template surfaces, tool commands |
| 1 — go-foundry-cli source + research report | Transfer analysis (parity hypotheses until adapted) |
| 2 — Exa deep-reasoning multi-query | Landscape comparison; structured alternatives |
| 2 — Session deep-research memos | Cross-check and transfer disposition |
| 3 — Community generator issues | Failure modes (partial write, empty names) |

**Not sufficient alone:** stars, “everyone uses X,” unexamined go-foundry copy.

## 7. Evidence Spikes

None executed in this research session.

| ID | Proposed spike | Why |
| -- | -------------- | --- |
| SPK-100 | Pure pipeline: TOML spec → resolve → plan JSON golden for minimal CLI | Plan-as-contract load-bearing |
| SPK-101 | Stage-dir render + exclusive place on Linux (empty dest; fail on non-empty) | Write safety load-bearing |
| SPK-102 | Catalog expand: cli + `http` profile file inventory + forbidden-path check (no `.env`, no CLAUDE.md) | Emit invariants |
| SPK-103 | Default verify tier: `uv sync` + ruff + ty on staged tree (time/cost) | Verify policy |

## 8. Comparative Analysis

### 8.1 CLI lifecycle

| Approach | Fit | Verdict |
| -------- | --- | ------- |
| Single `generate --pretend` (Copier-like) | Simple; weak inspectable plan | Reject as sole model |
| validate / plan / generate (go-foundry) | Agent/scriptable; pure dry-run | **Required** |
| Terraform plan-file apply only | Strong contract; UX heavy | Adapt digests, not full state lineage |

### 8.2 Spec format

| Approach | Fit | Verdict |
| -------- | --- | ------- |
| TOML schema version (go-foundry) | Agent-editable; tomllib; comments | **Default/Required** |
| Copier YAML questionnaire | Rich prompts; couples to Copier | Reject as engine input model |
| Cookiecutter JSON | Flat; weak validation | Reject |
| Flags-only | Poor replay/plan | Reject as sole input |

### 8.3 Plan binding

| Approach | Fit | Verdict |
| -------- | --- | ------- |
| Plan-as-preview only | Easy; generate can drift | Reject as Default |
| Plan-as-contract (same Construct) | Trustworthy dry-run | **Required** |
| Optional plan file for CI | Nice-to-have later | Optional later (OQ) |

### 8.4 Write semantics

| Approach | Fit | Verdict |
| -------- | --- | ------- |
| In-place overwrite with force | Drift/risk | Reject Default |
| Per-file atomic only | Partial tree on crash | Insufficient alone |
| Sibling stage + exclusive place | Fail-closed whole project | **Required** |
| Merge/update existing repos | High complexity | **Reject v1** |

### 8.5 Catalog / engine

| Approach | Fit | Verdict |
| -------- | --- | ------- |
| Custom catalog + planner (go-foundry style) | Closed set; invariants; plan purity | **Required** |
| Copier multi-template composition as product | Fast scaffolding; weaker plan purity | Reject as engine |
| Remote/plugin catalogs | Marketplace creep | **Reject** |

### 8.6 Template vs generator

| Approach | Fit | Verdict |
| -------- | --- | ------- |
| Dual-edit template repo + catalog | Drift | Reject |
| Catalog SoT; CI generates template snapshot | Single SoT | **Required** |
| Template-only (no CLI) | Fails hybrid Blueprint | Reject |

### 8.7 Post-generate verification

| Approach | Fit | Verdict |
| -------- | --- | ------- |
| Never verify in generator | Fast; agents may skip | Reject as sole policy |
| Always full pytest matrix | Slow/flaky envs | Optional strict |
| Tiered default/strict before place | Balance | **Default** |

### 8.8 Required architecture tables (index)

Prompt-required tables are satisfied as follows (content lives in REC bodies;
this index is for validators and synthesis):

| # | Required table | Location |
| - | -------------- | -------- |
| 1 | CLI lifecycle | REC-200 (below expanded) |
| 2 | Spec model | REC-201 + table 8.8.2 |
| 3 | Plan model | table 8.8.3 |
| 4 | Write semantics | table 8.8.4 |
| 5 | Catalog inventory (v1 closed set) | table 8.8.5 |
| 6 | Archetype × profile composition | REC-205 + table 8.8.6 |
| 7 | Emit contract | REC-206, REC-207 |
| 8 | Foundry module map | REC-208 + table 8.8.8 |
| 9 | go-foundry transfer | REC-210 |
| 10 | Anti-patterns | REC-212 |

#### 8.8.1 CLI lifecycle (command → inputs → outputs → fail)

| Command | Inputs | Outputs | Fail conditions |
| ------- | ------ | ------- | --------------- |
| `validate` | `--spec` (path or `-`) | text/JSON success report; no plan body required | parse/schema/resolve/plan-construct errors; exit ≠ 0 |
| `plan` | `--spec`; verify mode flags | Generation Plan (text + optional JSON) | same pure-pipeline failures as validate |
| `generate` | `--spec`; verify mode | staged tree → placed destination; report | pure-pipeline fail; stage render fail; verify fail; dest exists/non-empty; place fail |
| `catalog list` | none / filters | unit list | catalog load/integrity fail |
| `catalog show` | unit id | unit detail | unknown id |
| `version` | none | version + catalog digest | none expected |

#### 8.8.2 Spec model

| Field / dimension | Required? | Validation rules |
| ----------------- | --------- | ---------------- |
| `schema` | Required | Must be supported integer (v1 → `1`); unsupported → hard fail |
| `name` | Required | Non-empty project name |
| `description` | Optional | Free text |
| `archetype` | Required | Exactly one of `cli` \| `scripts` \| `data-etl` |
| `destination` | Required | Path; basename SHOULD match `name` |
| `profiles` | Required key; may be `[]` | Each id ∈ closed catalog; unknown → hard fail |
| unknown keys | — | Hard fail |
| secrets in spec | Forbidden | No secret material in file |

#### 8.8.3 Plan model

| Plan element | Binding strength | Visibility |
| ------------ | ---------------- | ---------- |
| foundry version + catalog digest | Contract | human + JSON |
| validated/normalized spec | Contract | human + JSON |
| resolved archetype + ordered profiles | Contract | human + JSON |
| planned files (path, mode, render, content digest) | Contract | human + JSON |
| dependencies / pins | Contract | human + JSON |
| external steps + verify mode | Contract | human + JSON |
| `plan_sha256` | Integrity | JSON (and text summary) |
| warnings | Non-binding notes | human + JSON |

#### 8.8.4 Write semantics

| Scenario | Behavior |
| -------- | -------- |
| Destination missing | Create via exclusive place of stage |
| Destination exists and non-empty | **Fail** (no default overwrite) |
| Render failure mid-stage | Preserve stage; destination untouched; exit ≠ 0 |
| Verify failure | Preserve stage; do not place; exit ≠ 0 |
| Place success | Destination is complete tree; stage consumed/renamed |
| Existing-project merge/update | **Out of v1** |

#### 8.8.5 Catalog inventory (v1 closed set)

| Kind | Id | Emits (summary) | Membership |
| ---- | -- | --------------- | ---------- |
| core | `core` | uv/src/ruff/ty/pytest/fnox/GHA/AGENTS.md/skills base | Always |
| archetype | `cli` | Typer CLI package layout + `add-cli-command` skill | Exactly one archetype |
| archetype | `scripts` | Script-oriented layout + `add-script` skill | Exactly one archetype |
| archetype | `data-etl` | Data/ETL-oriented package layout | Exactly one archetype |
| profile | `http` | httpx dependency + docs | Opt-in |
| profile | `hooks-hk` | hk instead of/beside pre-commit default | Opt-in |
| profile | `data-etl` | polars+pyarrow (+ extras policy) | Opt-in |
| lock | `versions.toml` | Exact pins for tools/deps/actions | Always loaded |

#### 8.8.6 Archetype × profile composition (allowed)

| Archetype | `http` | `hooks-hk` | `data-etl` profile |
| --------- | ------ | ---------- | ------------------ |
| `cli` | allowed | allowed | allowed |
| `scripts` | allowed | allowed | allowed |
| `data-etl` | allowed | allowed | allowed (stack focus) |

Path collisions: later unit wins only if `override = true`; else resolve fails.
Unknown profile IDs fail before plan complete.

#### 8.8.8 Foundry module map

| Package | Responsibility |
| ------- | -------------- |
| `cli` | Typer wiring; no domain logic |
| `spec` | Parse + validate (pure) |
| `catalog` | Load manifests, digests, package data |
| `resolve` | Archetype/profile resolution (pure) |
| `plan` | Construct plan (pure given inputs) |
| `render` | Static + template → bytes |
| `fsx` | Stage + exclusive place |
| `generate` | Lifecycle orchestration |
| `verify` | uv/ruff/ty/pytest runners |
| `report` | Text/JSON encoding |

## 9. Recommendations

### REC-200 — Foundry CLI lifecycle

- **Classification:** Required
- **Applies to:** Foundry product CLI
- **Confidence:** High
- **Decision urgency:** Required before implementation
- **Evidence quality:** Strong
- **Related decisions:** None

#### Recommendation

Ship a non-interactive-first CLI with:

| Command | Writes? | Role |
| ------- | ------- | ---- |
| `foundry validate --spec PATH` | No | Full pure pipeline; discard plan; exit 0/1 |
| `foundry plan --spec PATH` | No | Emit complete Generation Plan (text default; JSON mode) |
| `foundry generate --spec PATH` | Yes | Execute plan: stage → verify tier → place |
| `foundry catalog list` | No | List closed catalog units |
| `foundry catalog show ID` | No | Show unit details |
| `foundry version` | No | Version + catalog digest |

Optional later: `--dest` override with same pure observation rules as go-foundry.

#### Requirements and Constraints

- `validate` and `plan` MUST be write-free (no FS mutation, no network by default).
- `generate` is the only command that mutates the destination parent/stage.
- Interactive prompts are NOT required for v1 (MAY add later; never sole path).

#### Rationale

Matches proven go-foundry lifecycle and agent scripting needs; clearer than a
single generate with pretend flags. Exa landscape agrees on multi-stage + dry-run
separation; naming follows go-foundry (`generate` not `apply`).

#### Evidence

go-foundry-cli `internal/cli/commands.go`; Exa `cli-lifecycle`; Grok memo
`lifecycle-plan-write.md`.

#### Evidence Spikes

SPK-100.

#### Tradeoffs

More commands to document vs single-shot generators.

#### Failure Modes

Agents invent `foundry init` with different semantics — mitigate via AGENTS.md
and skill for foundry product (product repo only).

#### Alternatives Considered

Copier single-command + pretend; flags-only generate.

#### Downstream Implications

Synthesis REQs for CLI surface and exit codes.

#### Revisit Triggers

Need for `update` command; JSON machine envelopes standardization.

---

### REC-201 — Project Specification format (TOML)

- **Classification:** Required
- **Applies to:** Spec input
- **Confidence:** High
- **Decision urgency:** Required before implementation
- **Evidence quality:** Strong
- **Related decisions:** None

#### Recommendation

Use a **versioned TOML** Project Spec (`schema = 1`) as the sole declarative
product intent document. Minimum fields (v1):

```toml
schema = 1
name = "example-cli"
description = "…"
archetype = "cli"          # cli | scripts | data-etl
destination = "./example-cli"
profiles = ["http"]        # subset of closed set; may be []
# python_version pin optional; default from Core (3.13)
```

- Explicit `--spec` path (or positional path); support `--spec -` for stdin.
- Unknown fields / unsupported schema / unknown profile IDs → hard fail.
- No secret material in the spec file.

#### Requirements and Constraints

- MUST reject unknown keys and unknown profile IDs.
- MUST NOT require interactive questionnaire for CI/agents.
- Destination basename SHOULD match `name` (validate with clear error).

#### Rationale

TOML is comment-friendly, agent-editable, and first-class in the Python
ecosystem (`tomllib`). go-foundry already proved TOML specs for this product
family. Exa’s Copier YAML lean optimizes for questionnaire engines we **reject**
as the foundry runtime.

#### Evidence

go-foundry minimal-cli.toml; go-foundry architecture report (TOML choice);
Python tomllib; Exa `spec-format` (alternative YAML considered).

#### Evidence Spikes

SPK-100 invalid-spec suite.

#### Tradeoffs

Less “pretty questionnaire” UX than Copier; acceptable for agent-first product.

#### Failure Modes

Agents invent free-form YAML/JSON specs — reject at parse.

#### Alternatives Considered

YAML Copier-style; JSON Cookiecutter; flags-only.

#### Downstream Implications

JSON Schema or equivalent for docs optional; TOML is normative wire format.

#### Revisit Triggers

Need for multi-file includes (reject unless DEC).

---

### REC-202 — Generation Plan as contract

- **Classification:** Required
- **Applies to:** plan / generate pipeline
- **Confidence:** High
- **Decision urgency:** Required before implementation
- **Evidence quality:** Strong
- **Related decisions:** REC-200

#### Recommendation

The Generation Plan is the **immutable contract** between pure interpretation and
side effects:

- Constructed by a pure function of: validated spec, catalog digest, verify mode,
  foundry version, resolved archetype/profiles, planned files (path, mode,
  render kind, content digest), dependencies, external steps, warnings.
- `plan` prints it; `generate` **rebuilds with the same Construct** and executes
  it (byte-stable plan body for identical inputs).
- Text summary for humans; full JSON for agents/CI.
- Include `plan_sha256` (hash of canonical JSON excluding that field).

#### Requirements and Constraints

- Plan construction MUST NOT write the destination or require network.
- `generate` MUST fail closed if resolution would diverge from the inspected plan
  inputs (spec path content, catalog digest, flags).

#### Rationale

go-foundry treats plan as authoritative dry-run; Exa’s preview-only default is
weaker for agent trust. Contract model prevents “plan said X, generate wrote Y.”

#### Evidence

go-foundry `internal/plan/doc.go`; plan_generate equality tests; Exa
`plan-binding` (contract mode); Grok memo.

#### Evidence Spikes

SPK-100.

#### Tradeoffs

More engineering than pretend-only; worth it for hybrid foundry.

#### Failure Modes

Non-determinism (map order, timestamps) — ban time/randomness in plan body.

#### Alternatives Considered

Preview-only; terraform state lineage (overkill).

#### Downstream Implications

Golden tests for plans; report package encoding.

#### Revisit Triggers

Serialized plan file for offline apply (optional later).

---

### REC-203 — Filesystem write and placement semantics

- **Classification:** Required
- **Applies to:** generate
- **Confidence:** High
- **Decision urgency:** Required before implementation
- **Evidence quality:** Strong
- **Related decisions:** REC-202

#### Recommendation

For **new project generation** (v1):

1. Resolve destination; **fail** if path exists and is non-empty (no default
   overwrite; no merge).
2. Create **sibling staging directory** under the destination parent
   (e.g. `.foundry-<name>-<random>`).
3. Render all planned files into the stage (per-file temp+replace inside stage).
4. Run selected verify tier **inside stage**.
5. On success, **exclusive place** stage → destination (no-replace rename).
6. On failure, **preserve stage** for inspection; exit non-zero; leave destination
   untouched.

v1 **MUST NOT** implement existing-project update/merge.

#### Requirements and Constraints

- No silent partial success at destination.
- No symlink-escape into unexpected trees (confine paths under stage root).
- macOS + Linux only.

#### Rationale

go-foundry transaction model + Copier/Cookiecutter fail-on-exists defaults.
Exa write-semantics agrees on staging + atomic primitives.

#### Evidence

go-foundry `internal/fsx/transaction.go`; Exa `write-semantics`; Cookiecutter
OutputDirExistsException pattern.

#### Evidence Spikes

SPK-101.

#### Tradeoffs

No “regenerate in place” v1 — correct for safety.

#### Failure Modes

Cross-device rename failures — document same-filesystem parent requirement.

#### Alternatives Considered

In-place force overwrite; per-file only without staging.

#### Downstream Implications

fsx module; e2e tests for preexisting dest.

#### Revisit Triggers

Explicit `foundry update` stage with conflict policy (future DEC).

---

### REC-204 — Closed catalog model

- **Classification:** Required
- **Applies to:** Foundry catalog
- **Confidence:** High
- **Decision urgency:** Required before implementation
- **Evidence quality:** Strong
- **Related decisions:** REC-205, REC-206

#### Recommendation

Ship a **closed, git-visible catalog** as package data:

```text
catalog/
  versions.toml          # exact pins (tools, deps, action SHAs)
  core/manifest.toml     # always-on files + deps
  archetypes/<id>/…
  profiles/<id>/…
```

- Unit kinds: `core` | `archetype` | `profile`
- File entries: `static` | `template` with explicit path + mode
- **No** remote catalog fetch, plugin discovery, or user-installed catalog units in v1
- Catalog digest included in every plan
- Development override path MAY load from filesystem for catalog authors only

#### Requirements and Constraints

- Unknown unit IDs fail resolution.
- Catalog validation fails on lock entries unused or versions unpinned.

#### Rationale

Direct adapt of go-foundry catalog that maps cleanly onto G1 Core/profiles.
Rejects marketplace. Python uses `importlib.resources` instead of Go embed.

#### Evidence

go-foundry `catalog/` tree; Exa `catalog-model` (closed allowlist); Grok
`catalog-emit-template.md`.

#### Evidence Spikes

SPK-102.

#### Tradeoffs

Less flexible than remote templates; intentional.

#### Failure Modes

Catalog sprawl — admission process for new units (OQ / later DEC).

#### Alternatives Considered

Copier multi-template composition; cookiecutter+cruft as engine.

#### Downstream Implications

Catalog admission rules in implementation plan.

#### Revisit Triggers

Need for optional external catalog (default reject).

---

### REC-205 — Archetype and profile composition

- **Classification:** Required
- **Applies to:** resolve step
- **Confidence:** High
- **Decision urgency:** Required before implementation
- **Evidence quality:** Strong
- **Related decisions:** REC-204; ecosystem REC-014

#### Recommendation

**Exactly one archetype** per project:

| Archetype | Role |
| --------- | ---- |
| `cli` | Installable Typer CLI package (src layout) |
| `scripts` | Script-oriented layout (PEP 723 + package as needed) |
| `data-etl` | Data/ETL-oriented package layout |

**Profiles** (opt-in, closed, ordered application):

| Profile | From G1 |
| ------- | ------- |
| `http` | httpx |
| `hooks-hk` | hk (vs pre-commit default) |
| `data-etl` | polars+pyarrow (+ documented extras policy) |

Composition rules:

- Apply `core` always → archetype → profiles in catalog-defined order.
- Path collisions: later unit wins only if declared `override = true`; else fail.
- Conflict table (v1): e.g. `hooks-hk` replaces pre-commit hook files rather than
  dual-shipping both as Default; document precisely in catalog manifests.
- Unknown combinations fail at resolve (before plan complete).

#### Requirements and Constraints

- No open-ended plugin profiles.
- Profile IDs in spec MUST be subset of catalog.

#### Rationale

Matches Blueprint archetypes + ecosystem REC-014 without combinatorial templates.

#### Evidence

Ecosystem REC-014; go-foundry resolve/profiles; Exa `archetype-profiles`.

#### Evidence Spikes

SPK-102 matrix subset.

#### Tradeoffs

3×3 matrix discipline vs freeform templates.

#### Failure Modes

Agents invent `web` archetype — reject.

#### Alternatives Considered

Single mega-template with conditionals only; cookie-composer layers.

#### Downstream Implications

Resolve package pure tests.

#### Revisit Triggers

New G1-accepted profiles via program amendment.

---

### REC-206 — Core toolchain emit contract

- **Classification:** Required
- **Applies to:** catalog core + generate
- **Confidence:** High
- **Decision urgency:** Required before implementation
- **Evidence quality:** Strong
- **Related decisions:** ecosystem REC-001..014

#### Recommendation

Every successful plan for any archetype **MUST** include emit of:

| Invariant | Notes |
| --------- | ----- |
| `pyproject.toml` + uv project metadata | floor 3.12; default pin 3.13 |
| `uv.lock` policy | committed lock for apps; document library caveat |
| `src/` package layout | per archetype rules (REC-003) |
| Ruff config + scripts | check + format |
| ty config | Required Core |
| pytest (+ cov default) | tests layout |
| pre-commit config | unless `hooks-hk` profile replaces |
| `fnox.toml` + age provider | **no** `.env` secret templates |
| GitHub Actions | setup-uv + ruff + ty + pytest (Linux required) |
| Docs command surface | REC-013 commands in README/AGENTS |

**MUST NOT** emit dotenv secret storage patterns or alternate Core typecheckers
as Default.

#### Requirements and Constraints

Catalog tests enforce presence/absence invariants on every golden plan.

#### Rationale

Architecture’s job is to **wire** accepted ecosystem Core, not re-pick tools.

#### Evidence

Ecosystem report v0.2; Exa `emit-ai-native-core`.

#### Evidence Spikes

SPK-102.

#### Tradeoffs

Less “minimal empty repo”; intentional strong default.

#### Failure Modes

Profile accidentally strips Core — resolve tests.

#### Alternatives Considered

Optional Core à la carte — rejected by Blueprint.

#### Downstream Implications

Golden inventories per archetype.

#### Revisit Triggers

DEC changing ty/fnox Core status.

---

### REC-207 — AI-native emit contract

- **Classification:** Required
- **Applies to:** catalog core + generate
- **Confidence:** High
- **Decision urgency:** Required before implementation
- **Evidence quality:** Strong
- **Related decisions:** AI-native REC-100..112

#### Recommendation

Every Generated Project plan **MUST** emit:

```text
AGENTS.md
.agents/skills/quality-gates/SKILL.md
.agents/skills/secrets-fnox/SKILL.md
# plus archetype skills:
#   cli     → add-cli-command
#   scripts → add-script
#   data-etl → (add-script or data-specific skill only if catalog admits; default add-script)
```

**MUST NOT** emit:

- `CLAUDE.md`, `.claude/`, Claude-only skill forks
- Default committed MCP server catalogs / kitchen-sink `.mcp.json`

Optional: `.cursor/rules` only if a future profile needs globs (not Core).

Skills document REC-013 commands and forbid dotenv secrets.

#### Requirements and Constraints

Forbidden-path linter in catalog validation and generate conformance.

#### Rationale

Direct emit of accepted AI-native locks; closes oral tradition gap.

#### Evidence

AI-native report v0.2; go-foundry core emits AGENTS.md; Exa emit query.

#### Evidence Spikes

SPK-102 forbidden paths.

#### Tradeoffs

Always-on skill files vs ultra-minimal tree — accept small closed set.

#### Failure Modes

Contributors re-add Claude adapters — RSK-051 inherit.

#### Alternatives Considered

AGENTS.md only without skills — weaker DoD compliance (G1 chose thin skills).

#### Downstream Implications

Skill body content in implementation; architecture locks paths/purposes.

#### Revisit Triggers

Owner expands Core skill set via DEC.

---

### REC-208 — Foundry product module layout

- **Classification:** Default
- **Applies to:** Foundry product repo
- **Confidence:** High
- **Decision urgency:** Required before implementation
- **Evidence quality:** Moderate–Strong
- **Related decisions:** REC-200..205

#### Recommendation

Dogfood ecosystem Core. Package layout:

```text
src/python_foundry/
  cli/          # Typer app; command wiring only
  spec/         # parse + validate (pure)
  catalog/      # load manifests, digests, package data
  resolve/      # archetype/profile resolution (pure)
  plan/         # Construct plan (pure given inputs)
  render/       # static + template render to bytes
  fsx/          # stage + place
  generate/     # lifecycle orchestration
  verify/       # tool runners (uv/ruff/ty/pytest)
  report/       # text/JSON encoding
catalog/        # authoring tree (packaged as data)
tests/
```

Layering: `plan` must not import `fsx`/`generate`/`cli`. Pure packages unit-tested
without filesystem side effects.

#### Requirements and Constraints

Foundry itself uses uv, ruff, ty, pytest, fnox per Core where applicable.

#### Rationale

Mirrors go-foundry internal packages in Python idiom; Exa module-layout agrees.

#### Evidence

go-foundry `internal/*`; Exa `python-cli-module-layout`; ecosystem REC-003.

#### Evidence Spikes

None required for layout choice.

#### Tradeoffs

More packages vs monolith — clearer purity boundaries.

#### Failure Modes

Circular imports — arch tests / import linters.

#### Alternatives Considered

Flat package; plugin entry points for catalog (reject v1).

#### Downstream Implications

Implementation plan phases by package.

#### Revisit Triggers

Need for library API beyond CLI.

---

### REC-209 — GitHub template surface vs generator SoT

- **Classification:** Required
- **Applies to:** hybrid product
- **Confidence:** High
- **Decision urgency:** Required before implementation
- **Evidence quality:** Strong
- **Related decisions:** REC-204

#### Recommendation

- **Single source of truth:** closed catalog in the foundry product repository.
- **GitHub template repository:** a **generated snapshot** (CI job runs
  `foundry generate` with a fixed public template spec) published for
  “Use this template” UX.
- Do **not** hand-edit the template repo as a second catalog.
- Document that advanced users should prefer the CLI for profiles beyond the
  snapshot’s fixed defaults.

#### Requirements and Constraints

CI must fail if template snapshot drifts from catalog goldens.

#### Rationale

GitHub templates cannot express multi-profile composition well; dual-edit drifts.
Exa and Grok memos agree on generate-from-catalog SoT.

#### Evidence

GitHub template docs; Exa `template-vs-generator`; Blueprint L1 hybrid.

#### Evidence Spikes

None in research; CI drift check in implementation.

#### Tradeoffs

Template snapshot is a subset of full CLI power — acceptable.

#### Failure Modes

Manual PRs to template repo — protect with CODEOWNERS/CI.

#### Alternatives Considered

Template-as-SoT; dual-path without CI.

#### Downstream Implications

Release pipeline for template repo.

#### Revisit Triggers

GitHub adds parameterized templates (revisit only).

---

### REC-210 — go-foundry transfer disposition

- **Classification:** Required
- **Applies to:** architecture inheritance
- **Confidence:** High
- **Decision urgency:** Required now
- **Evidence quality:** Strong
- **Related decisions:** All REC-200..209

#### Recommendation

| Pattern | Disposition | Rationale (short) |
| ------- | ----------- | ----------------- |
| validate / plan / generate + catalog/version | **Adopt** | Proven lifecycle; agent-scriptable |
| TOML Project Spec + schema version | **Adopt** | Matches prior art + Python tomllib |
| Immutable Generation Plan + pure Construct | **Adopt** | Plan-as-contract trust |
| Closed core / archetype / profile catalog | **Adopt** (Python units) | Closed-set maps to G1 Core/profiles |
| versions lock file | **Adapt** (uv/deps/actions) | Same pin discipline; different toolchain |
| Sibling stage + exclusive place | **Adopt** | Fail-closed placement |
| FD-level openat transaction | **Adapt** (stage-root confinement first) | Avoid over-copying Go FD complexity in v1 |
| Binary embed catalog | **Adapt** (`importlib.resources`) | Python packaging, not Go embed |
| Tiered verify before place | **Adapt** (uv/ruff/ty/pytest) | Same idea; Python Core tools |
| Non-interactive first + JSON reports | **Adopt/Adapt** | Agent-first; JSON mode optional |
| TUI archetype | **Reject** | Out of Blueprint scope |
| Go/Cobra/go.mod generation | **Reject** | Python/uv/Typer stack |
| Remote/plugin catalogs | **Reject** | Marketplace non-goal |
| Existing-project sync/update v1 | **Reject** | Complexity; deferred |
| Windows | **Reject** | Blueprint L3 |
| Claude-specific emit | **Reject** | AI-native EVD-121 |

#### Requirements and Constraints

- go-foundry is **prior art only** — never sole authority for Python/uv design.
- Synthesis MUST cite this table when tracing REQ provenance for transferred patterns.
- New go-foundry features require re-eval (do not auto-import).

#### Rationale

Transfer only what fits Python/uv and accepted G1 locks.

#### Evidence

go-foundry research report executive summary; CLI tree; Grok transfer memo.

#### Evidence Spikes

None.

#### Tradeoffs

N/A — explicit matrix.

#### Failure Modes

Blind copy of Go FD complexity before needed.

#### Alternatives Considered

Ignore go-foundry (lose proven model); full copy (wrong stack).

#### Downstream Implications

Synthesis cites this table for REQ provenance.

#### Revisit Triggers

New go-foundry features worth re-eval.

---

### REC-211 — Post-generate verification policy

- **Classification:** Default
- **Applies to:** generate `--verify`
- **Confidence:** Medium–High
- **Decision urgency:** Required before implementation
- **Evidence quality:** Moderate
- **Related decisions:** REC-013, REC-203

#### Recommendation

| Mode | Steps (in stage, before place) |
| ---- | ------------------------------ |
| `default` | `uv sync` + `uv run ruff check` + `uv run ruff format --check` + `uv run ty check` |
| `strict` | default + `uv run pytest` (+ cov if configured) + `pre-commit run --all-files` when pre-commit present |
| `none` | Explicit opt-out; **loud warning**; still emit DoD docs |

- Record chosen mode and planned external steps **in the plan**.
- Always emit AGENTS.md DoD listing REC-013 regardless of mode.
- Network: `uv sync` may need network — disclose in plan; offline generate uses
  `none` or cached uv only (document limitation).

#### Requirements and Constraints

Verify failures abort place; preserve stage.

#### Rationale

go-foundry verifies before place; Exa preferred docs-only default — too weak for
“runnable project” success criterion. Tiered compromise.

#### Evidence

go-foundry verify package; Exa `post-generate-verify`; Blueprint fast path success.

#### Evidence Spikes

SPK-103.

#### Tradeoffs

Slower generate; higher confidence.

#### Failure Modes

Cold cache timeouts — document; allow `none` with warning.

#### Alternatives Considered

Never verify; always full strict.

#### Downstream Implications

toolrun/verify module; CI for foundry e2e.

#### Revisit Triggers

SPK-103 cost data; owner prefers none-by-default.

---

### REC-212 — Closed-set / anti-marketplace discipline

- **Classification:** Required
- **Applies to:** product scope
- **Confidence:** High
- **Decision urgency:** Required now
- **Evidence quality:** Strong
- **Related decisions:** Blueprint non-goals

#### Recommendation

v1 **rejects**: plugin APIs, remote catalog registries, arbitrary template URLs as
Default path, MCP kitchen sinks, unbounded skill catalogs, framework zoos,
Windows, notebooks, existing-repo mutation.

New catalog units require explicit admission (manifest + pins + goldens + tests).

| Anti-pattern | Why rejected | Mitigation REC |
| ------------ | ------------ | -------------- |
| Plugin / remote catalog APIs | Marketplace creep; non-goal | REC-204, REC-212 |
| Dual-edit GitHub template + catalog | Drift | REC-209 |
| Plan-as-preview only (no contract) | generate may diverge from dry-run | REC-202 |
| In-place overwrite / merge v1 | Partial writes; complexity | REC-203 |
| Copier/Cookiecutter as foundry engine | Weaker plan purity / catalog control | REC-204, REC-210 |
| dotenv / `.env` secret emit | Ecosystem lock | REC-206; inherit REC-008 |
| Claude adapters (`CLAUDE.md`, `.claude/`) | AI-native lock EVD-121 | REC-207 |
| Default MCP kitchen sink | AI-native lock | REC-207 |
| Windows / notebooks / framework zoo | Blueprint non-goals | REC-212 |

#### Requirements and Constraints

- New catalog units REQUIRE admission: manifest + pins + goldens + tests.
- Scope expansions that re-open rejected rows REQUIRE a DEC or Blueprint amendment.
- Closed-set discipline applies to skills and MCP as well as templates.

#### Rationale

Blueprint non-goals + go-foundry anti-platform stance.

#### Evidence

Blueprint; go-foundry architecture rejections; Exa catalog caveats.

#### Evidence Spikes

None.

#### Tradeoffs

Slower feature expansion — intentional.

#### Failure Modes

“Just add one plugin hook” — require DEC.

#### Alternatives Considered

Extensible plugin core — rejected.

#### Downstream Implications

Admission checklist in plan phase.

#### Revisit Triggers

Program scope amendment only.

## 10. Evidence Ledger

| ID | Claim | Class | Source | Access | Confidence | Used by |
| -- | ----- | ----- | ------ | ------ | ---------- | ------- |
| EVD-200 | go-foundry uses validate/plan/generate with pure plan pipeline | Verified fact | go-foundry-cli source | 2026-08-01 | High | REC-200, 202 |
| EVD-201 | go-foundry Project Spec is TOML schema=1 | Verified fact | minimal-cli.toml | 2026-08-01 | High | REC-201 |
| EVD-202 | go-foundry catalog is core/archetypes/profiles + versions lock | Verified fact | catalog/ tree | 2026-08-01 | High | REC-204, 210 |
| EVD-203 | go-foundry stages then exclusive-places | Official claim / source | fsx/transaction.go | 2026-08-01 | High | REC-203 |
| EVD-204 | Copier supports pretend, overwrite/skip, answers files | Official claim | copier docs | 2026-08-01 | High | §8 comparisons |
| EVD-205 | Cookiecutter fails if output dir exists unless force | Official claim | cookiecutter docs | 2026-08-01 | High | REC-203 |
| EVD-206 | GitHub templates copy tree; not parameterized multi-profile | Official claim | GitHub docs | 2026-08-01 | High | REC-209 |
| EVD-207 | Exa 10-query deep-reasoning run completed | Experiment | architecture-20260801T000131Z | 2026-08-01 | High | Methodology |
| EVD-208 | Exa leans Copier/YAML/preview; weaker plan contract | Inference | Exa INDEX | 2026-08-01 | Medium | §8 challenges |
| EVD-209 | G1 ecosystem Core locks must be emitted | User decision / accepted report | report 01 v0.2 | 2026-07-31 | High | REC-206 |
| EVD-210 | G1 AI-native AGENTS.md + .agents only; no Claude | User decision / accepted report | report 02 v0.2 | 2026-07-31 | High | REC-207 |
| EVD-211 | Planner-led custom engine better fits plan purity than Copier-as-engine | Judgment | synthesis of EVD-200..208 | 2026-08-01 | Medium–High | REC-204, 210 |

## 11. Recommendation Ledger

| ID | Title | Classification |
| -- | ----- | -------------- |
| REC-200 | Foundry CLI lifecycle | Required |
| REC-201 | Project Specification format (TOML) | Required |
| REC-202 | Generation Plan as contract | Required |
| REC-203 | Filesystem write and placement semantics | Required |
| REC-204 | Closed catalog model | Required |
| REC-205 | Archetype and profile composition | Required |
| REC-206 | Core toolchain emit contract | Required |
| REC-207 | AI-native emit contract | Required |
| REC-208 | Foundry product module layout | Default |
| REC-209 | GitHub template surface vs generator SoT | Required |
| REC-210 | go-foundry transfer disposition | Required |
| REC-211 | Post-generate verification policy | Default |
| REC-212 | Closed-set / anti-marketplace discipline | Required |

## 12. Risks

### RSK-100 — Plan/generate non-determinism

- **Severity:** High if present
- **Mitigation:** Canonical JSON field order; sorted maps; ban time/random in plan; goldens

### RSK-101 — Partial stage left behind confuses agents

- **Severity:** Medium
- **Mitigation:** Document stage path in error output; optional cleanup flag later

### RSK-102 — Verify default needs network (`uv sync`)

- **Severity:** Medium
- **Mitigation:** Plan discloses network; `none` mode; cache guidance

### RSK-103 — Catalog drift vs GitHub template snapshot

- **Severity:** Medium
- **Mitigation:** CI regenerate + fail on diff (REC-209)

### RSK-104 — Contributors reintroduce dotenv or Claude adapters in catalog

- **Severity:** High (policy)
- **Mitigation:** Forbidden-path tests; REC-206/207; inherit RSK-050/051

### RSK-105 — Over-copying go-foundry FD complexity slows Python v1

- **Severity:** Medium
- **Mitigation:** Adapt stage-root first; defer openat hardcore

### RSK-106 — Exa overclaim without primary re-read

- **Severity:** Medium
- **Mitigation:** Primary citations; challenged Copier-as-engine lean

## 13. Weak Evidence

- Exact default verify duration on cold uv cache (needs SPK-103).
- Whether `data-etl` archetype needs a distinct skill beyond `add-script`.
- Long-term maintenance cost of custom renderer vs thin Copier wrapper (judgment).

## 14. Conflicting Evidence

| Topic | Tension | Resolution |
| ----- | ------- | ---------- |
| Spec format | Exa: YAML/Copier; go-foundry: TOML | **TOML** (REC-201) |
| Plan binding | Exa: preview default; go-foundry: contract | **Contract** (REC-202) |
| Engine | Exa: Copier-based emit; go-foundry: custom planner | **Custom planner** (REC-204) |
| Verify in generate | Exa: docs-only default; go-foundry: verify before place | **Tiered default** (REC-211) |

## 15. Assumptions

- ASM-200: G1 Core and AI-native locks remain accepted through synthesis.
- ASM-201: Foundry product ships as installable uv Python package (not only template).
- ASM-202: Same-filesystem parent for stage rename is acceptable for personal use.
- ASM-203: Owner prefers safety and plan inspectability over maximal generator speed.
- ASM-204: go-foundry-cli remains public reference for parity checks.

## 16. Open Questions

### OQ-100 — Exact TOML field set beyond minimum

- **Status:** Open
- **Resolution path:** Synthesis + owner review of examples
- **Blocks:** Spec REQ freeze

### OQ-101 — Default verify mode (`default` vs `none`)

- **Status:** Open (research recommends `default`)
- **Resolution path:** SPK-103 + owner
- **Blocks:** Generate UX REQ

### OQ-102 — Whether to ship JSON plan file on disk under `.foundry/`

- **Status:** Open
- **Resolution path:** Implementation simplicity vs agent attachment
- **Blocks:** Optional only

### OQ-103 — data-etl archetype skill set

- **Status:** Open
- **Resolution path:** AI-native OQ carry-forward + catalog admission
- **Blocks:** Skill emit for data-etl

### OQ-104 — Library vs application lockfile policy nuance in templates

- **Status:** Open (ecosystem noted apps commit lock)
- **Resolution path:** Synthesis
- **Blocks:** Core pyproject golden variants

### OQ-105 — Foundry product CLI name (`foundry` vs `python-foundry` vs `pyfoundry`)

- **Status:** Open
- **Resolution path:** Owner branding
- **Blocks:** Packaging metadata only

## 17. Handoff Digest

### Decisions supported

- Planner-led hybrid foundry CLI (not Copier-as-engine)
- validate → plan → generate with plan-as-contract
- TOML Project Spec; closed catalog; conservative stage+place writes
- Emit ecosystem Core + AI-native surfaces as invariants
- GitHub template is generated snapshot from catalog SoT
- go-foundry Adopt/Adapt/Reject matrix

### Recommendations accepted by this report

REC-200..REC-212 as written in v0.1.

### Recommendations challenged

- Exa Copier-engine / YAML / preview-default leans — **not adopted** as primary
  architecture (see §14)

### Evidence strength summary

Strong on lifecycle, plan contract, catalog shape, write policy, and G1 emit
wiring via go-foundry + official generator docs; medium on verify timing and
skill bodies for data-etl.

### Weak and conflicting evidence

See §13–§14.

### Assumptions

See §15.

### Risks

RSK-100..106.

### Open questions

OQ-100..105.

### Required downstream decisions

| Consumer | Needs |
| -------- | ----- |
| **Synthesis** | Trace REC-200..212 + G1 RECs → REQs; freeze CLI/spec/plan/write/catalog/emit |
| Implementation plan | Phase by package (spec/plan pure → catalog → fsx → generate → verify) |
| Owner | OQ-101 verify default; OQ-105 CLI name; confirm no v1 update-sync |

### Relevant identifiers

REC-200..212; RSK-100..106; OQ-100..105; SPK-100..103 (planned); EVD-200..211;
inherits ecosystem REC-001..014, AI-native REC-100..112, RSK-002/007/050/051.

### Full-report sections that must be read before deciding

§2 Executive Answer; §9 REC-200..212; §12–§16; §10 Evidence Ledger; REC-210 table.

## 18. Source Ledger

| Source | URL / path | Publisher | Access | Used for |
| ------ | ---------- | --------- | ------ | -------- |
| go-foundry architecture report | github.com/robertguss/go-foundry-research `docs/reports/03-…` | robertguss | 2026-08-01 | Transfer |
| go-foundry-cli | github.com/robertguss/go-foundry-cli | robertguss | 2026-08-01 | Prior art implementation |
| Copier docs | https://copier.readthedocs.io/en/stable/ | copier-org | 2026-08-01 | Comparisons |
| Cookiecutter docs | https://cookiecutter.readthedocs.io/en/stable/ | cookiecutter | 2026-08-01 | Comparisons |
| GitHub template repos | https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template | GitHub | 2026-08-01 | REC-209 |
| Ecosystem report v0.2 | `docs/reports/01-modern-python-ecosystem.md` | program | 2026-07-31 | REC-206 |
| AI-native report v0.2 | `docs/reports/02-ai-native-agent-workflow.md` | program | 2026-07-31 | REC-207 |
| Blueprint | `docs/00-program-blueprint.md` | program | 2026-07-30 | Locks |
| Charter | `docs/01-research-charter.md` | program | 2026-07-30 | Methodology |
| Exa architecture INDEX | `scripts/exa-output/architecture-20260801T000131Z/INDEX.md` | local | 2026-08-01 | EVD-207 |
| Grok memos | `scripts/exa-output/architecture-20260801T000131Z/grok/` | local | 2026-08-01 | Dual stream |
| Exa Deep blog | https://exa.ai/blog/exa-deep | Exa | 2026-07-31 | Methodology |
| Exa search API guide | https://exa.ai/docs/reference/search-api-guide | Exa | 2026-07-31 | Methodology |

## 19. Completion Checklist

- [x] All required report sections present
- [x] Actual research date recorded
- [x] Primary and subsidiary questions answered or explicitly OQ’d
- [x] REC-200..REC-299 used correctly; no out-of-range IDs
- [x] RSK/OQ/SPK within assigned ranges; no reuse of G1 IDs for new subjects
- [x] Inherited ecosystem Core locks respected
- [x] Inherited AI-native locks respected
- [x] go-foundry transfer table present (REC-210)
- [x] Evidence Ledger complete for load-bearing claims
- [x] Source ledger with URLs and access dates
- [x] Required tables complete (§8.8 index + REC-200..212 bodies)
- [x] Credible alternatives compared for major decision areas
- [x] Handoff Digest complete (synthesis-oriented)
- [x] Allowed file scope respected
- [x] No downstream stages started
