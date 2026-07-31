# Modern Python Ecosystem & Project Standards

- **Artifact type:** Focused Research Report
- **Program:** python-foundry
- **Stage:** `research-python-ecosystem`
- **Status:** Draft — pending re-validation and human acceptance
- **Version:** 0.2
- **Created:** 2026-07-31
- **Last updated:** 2026-07-31
- **Actual research date:** 2026-07-31
- **Owner revision:** 2026-07-31 — Core **ty** + Core **fnox** (**age** provider); **no `.env` secret storage**
- **Depends on:** Accepted Program Blueprint; Accepted Research Charter
- **Commissioning prompt:** `docs/prompts/01-modern-python-ecosystem-prompt.md`
- **Recommendation range:** REC-001..REC-014 (remaining REC-015..099 reserved)
- **Evidence base:** Exa Deep (`deep-reasoning`) multi-query run
  `scripts/exa-output/ecosystem-20260731T170320Z/` (local raw dumps; not governing)
  plus primary sources cited below; owner User decisions on ty/fnox/secrets

> Research reports are **evidence and recommendations**, not commandments.
> Architecture and synthesis consume this report after acceptance.
> Where owner **User decisions** override research preference, residual risk is
> recorded explicitly (Charter: User decision class).

## 1. Artifact Metadata

| Field | Value |
| ----- | ----- |
| Program ID | python-foundry |
| Stage ID | research-python-ecosystem |
| Primary question | What tooling, libraries, layouts, testing, and CI should define Core and profiles for CLI, scripts, and data/ETL on macOS/Linux with uv in 2026? |
| Rigor | standard |
| Operator | robertguss |
| Agent implementers | Primary (Grok, Claude Code, etc.) |

## 2. Executive Answer

**Core (always on for Generated Projects that are installable packages/CLIs):**

| Layer | Recommendation |
| ----- | -------------- |
| Python | Floor **3.12**; default pin **3.13** (`requires-python >= 3.12`, `.python-version` → 3.13) |
| Project tool | **uv** (project, lock, run, build/publish path) |
| Layout | **src/** packages + top-level `tests/`; scripts via **PEP 723** + `uv run` |
| Lint/format | **Ruff** (`check` + `format`) |
| Types | **ty** Required Core type checker (**User decision**; residual maturity risk RSK-002) |
| Tests | **pytest** Required; **pytest-cov** Default; **pytest-xdist** Optional |
| Hooks | **pre-commit** Default Core; **hk** Optional profile (owner preference partially honored via jdx secrets) |
| Secrets | **fnox** Required Core with default provider **age** — **no `.env` / python-dotenv secret storage** (**User decision**) |
| CI | **GitHub Actions** + `astral-sh/setup-uv` + ruff + **ty** + pytest on **ubuntu** (macOS optional matrix) |
| Commands | Document **`uv sync` / `uv run …` / `fnox exec …`** as the agent-facing surface |

**Profiles (opt-in):**

| Profile | Contents |
| ------- | -------- |
| `http` | **httpx** (sync default for CLI/scripts) |
| `hooks-hk` | **hk** instead of or beside pre-commit when owner wants jdx hooks |
| `data-etl` | Default **polars + pyarrow**; extras **duckdb**, **pandas** |
| `cli-typer` | **Typer** as Default CLI framework for CLI archetype (can be Core for CLI archetype only) |

**L5 owner-candidate disposition (summary):**

| Candidate | Disposition |
| --------- | ----------- |
| uv | **Confirm Required/Default Core** |
| ruff | **Confirm Required/Default Core** |
| ty | **Confirm Required Core** (User decision over research Watchlist preference) |
| pytest | **Confirm Required Core** |
| hk | **Optional profile** — pre-commit remains Default hooks unless profiled |
| fnox | **Confirm Required Core** (User decision; **no dotenv/`.env` secrets**) |
| httpx | **Optional `http` profile** |

Closed Core stays intentional: Astral stack (uv, ruff, **ty**) + pytest + **fnox** secrets + GHA. Research still records residual risk where maturity evidence was weaker (ty, fnox).

## 3. Scope and Exclusions

### In scope

- Python version policy; uv packaging; layouts; ruff; type checkers; pytest; hooks; secrets; HTTP client; CLI frameworks; data/ETL libraries; GitHub Actions; command surface; Core vs profile split.

### Out of scope (per Blueprint / prompt)

- Foundry generator engine (spec → plan → generate)
- Full agent skills / MCP / LSP catalogs (AI-native track)
- Windows, notebooks, web framework zoo, GUI/mobile
- Product implementation beyond evidence gathering

## 4. Inherited Constraints

From accepted Blueprint locks L1–L14 and Charter methodology: macOS+Linux only; hybrid foundry product (this report designs **Generated Project Core**, not the generator); AI-agent-primary implementation; personal primary user; standard rigor; go-foundry is prior art only; popularity is not proof; evidence before confidence.

## 5. Methodology

1. Read Blueprint, Charter, and commissioning prompt.
2. Ran **13 Exa Deep `deep-reasoning` queries** (one per decision area) via
   `scripts/exa_ecosystem_evidence.py` on **2026-07-31** (~$0.195 total).
3. Preferred official docs via `includeDomains` where practical.
4. Compared alternatives per area; classified Core vs profile.
5. **Challenged** owner L5 favorites where maturity/simplicity evidence was weak
   (ty, hk-as-Required, fnox-as-Required, httpx-in-Core) in v0.1.
6. **Owner revision (v0.2):** User decisions lock **ty** and **fnox** into Core and
   **forbid `.env`-based secret storage**; research demotions for those items are
   superseded with residual risk retained.
7. No local evidence spikes executed in this pass (documentary + Exa grounding
   sufficient for draft RECs; spikes listed — SPK-002 now **recommended** because
   ty is Core).
8. Synthesized into this standalone report with portable citations.

**Limitations:** Exa output is synthesized; load-bearing claims must remain
tied to primary URLs in the Source Ledger. Raw Exa JSON is not Git authority.

## 6. Source Quality and Limitations

| Strength | Limitation |
| -------- | ---------- |
| Strong Tier-1 coverage for uv, ruff, pytest, packaging.python.org, Python version status | ty maturity is issue/GitHub-heavy; still beta narrative — **accepted as Core via User decision** |
| hk and fnox have official sites but smaller ecosystems | **fnox Core + no `.env`** is User decision; hk remains Optional profile |
| Data stack versions active in 2026 | Profile defaults (polars vs pandas) are judgment + maintenance evidence, not universal truth |
| GHA + setup-uv well documented | Action major versions drift; pin SHAs in implementation |

## 7. Evidence Spikes

**None executed** in this pass.

| ID | Candidate spike | Why deferred |
| -- | --------------- | ------------ |
| SPK-001 | `uv init --package` + ruff + pyright + pytest smoke on Linux | Documentary path clear; run before implementation Phase 1 |
| SPK-002 | ty on a sample CLI tree (errors, config, `uv run ty`, CI) | **Recommended** — ty is now Required Core; bound residual risk |
| SPK-003 | hk vs pre-commit hook latency on same ruff/pytest config | Needed only if promoting hk to Default Core |

## 8. Comparative Analysis

### 8.1 Python version

| Option | Fit | Notes |
| ------ | --- | ----- |
| 3.10 | Reject | EOL Oct 2026 — too close for new projects on research date |
| 3.11 | Weak floor | EOL Oct 2027 — short runway |
| 3.12 | **Min floor** | Security support into 2028; uv Tier 1 |
| 3.13 | **Default pin** | Balance of maturity and support window |
| 3.14 | Optional latest | Fine for longevity; slightly higher ecosystem risk |

### 8.2 Project manager

| Tool | Role |
| ---- | ---- |
| **uv** | Winner for Core — lockfile, run, scripts, speed, official docs |
| Poetry / PDM / Hatch | Credible alternatives; migration paths exist; not Default |
| pip+venv+pip-tools | Baseline legacy; more agent decision surface |

### 8.3 Layout

| Archetype | Pattern |
| --------- | ------- |
| CLI / package | `uv init --package`, **src/**, `[project.scripts]`, `tests/` |
| Script | PEP 723 inline metadata + `uv run` |
| Data/ETL | Same as package CLI unless pure script |

src layout preferred over flat for installable packages (packaging.python.org).

### 8.4 Lint/format

Ruff as single lint+format tool dominates flake8+isort+black for closed defaults and agent simplicity. Pair with a type checker separately.

### 8.5 Type checking

| Tool | Verdict |
| ---- | ------- |
| **ty** | **Required Core (User decision)** — fast Astral checker; residual beta/maturity risk |
| **Pyright / BasedPyright** | Strong alternatives; not Default Core after owner lock on ty |
| mypy | Viable alternative; not Default |

### 8.6 Testing

pytest is Required. Coverage plugin Default. xdist Optional (personal scale).

### 8.7 Hooks

| Tool | Verdict |
| ---- | ------- |
| **pre-commit** | Default Core — universal, YAML, agent-familiar |
| **hk** | Optional profile — performance, jdx stack, Pkl config learning cost |
| prek | Mentioned alternative; not Core |

### 8.8 Secrets

| Approach | Verdict |
| -------- | ------- |
| **fnox** | **Required Core (User decision)** — default provider **age**; `fnox exec` |
| `.env` / python-dotenv | **Rejected for secrets** (User decision) — do not template secret storage this way |
| direnv / 1Password SDK alone | Not Core; may back fnox providers |

### 8.9 HTTP

httpx best modern default **when HTTP is needed** → profile, not Core.
Sync Client default for CLI/scripts.

### 8.10 CLI framework

Typer Default for CLI archetype (type-hint driven, agent-friendly). Click as stability/light-weight fallback. argparse not Default. cyclopts Watchlist.

### 8.11 Data/ETL

None in Core. Profile defaults to polars+pyarrow; duckdb and pandas as extras (owner often uses pandas/duckdb — both first-class extras).

### 8.12 CI

GitHub Actions + setup-uv + locked sync + ruff + pytest; Linux required; macOS optional for cost.

## 9. Recommendations

### REC-001 — Python version floor and default

- **Classification:** Default
- **Applies to:** All Generated Projects (Core)
- **Confidence:** High
- **Decision urgency:** Required now
- **Evidence quality:** Strong
- **Related decisions:** None

#### Recommendation

Set **minimum** Python to **3.12** and **default project pin** to **3.13**. Express as `requires-python = ">=3.12"` and `.python-version` / `uv python pin 3.13`. Reject 3.10 for new projects. Treat 3.14 as optional latest, not forced default.

#### Requirements and Constraints

macOS/Linux; uv Tier 1 support; AI agents must not assume 3.14-only syntax by default.

#### Rationale

As of 2026-07-31, 3.10 is near EOL; 3.12–3.14 are uv Tier 1. 3.13 balances support window and library maturity better than forcing 3.14 as the only pin.

#### Evidence

EVD-001, EVD-002; [devguide versions](https://devguide.python.org/versions/); [uv Python support](https://docs.astral.sh/uv/reference/policies/python/).

#### Evidence Spikes

None.

#### Tradeoffs

3.12 floor may exclude bleeding-edge 3.14-only features; 3.13 default may lag “latest” docs examples that show 3.14.

#### Failure Modes

Agents emit 3.14-only syntax while CI runs 3.12; pin drift across projects.

#### Alternatives Considered

3.12-only pin; 3.14 default; 3.11 floor (rejected).

#### Downstream Implications

Architecture templates; CI matrix; archetype pyproject defaults.

#### Revisit Triggers

Python EOL calendar change; uv Tier policy change; foundry forces 3.14-only features.

---

### REC-002 — uv as project and package manager

- **Classification:** Required
- **Applies to:** Core
- **Confidence:** High
- **Decision urgency:** Required now
- **Evidence quality:** Strong
- **Related decisions:** None

#### Recommendation

**uv** is Required Core for dependency management, virtualenvs, lockfile (`uv.lock` committed), `uv run`, and script/package workflows. Prefer official uv project workflow over Poetry/PDM/Hatch/pip-tools for new projects.

#### Requirements and Constraints

Commit `uv.lock`; use PEP 621 metadata; dependency groups for dev tools; console scripts via `[project.scripts]`.

#### Rationale

Single tool covers project lifecycle with strong official docs, speed, and agent-simple commands (`uv sync`, `uv run`).

#### Evidence

EVD-003; [uv projects](https://docs.astral.sh/uv/guides/projects/); [uv layout](https://docs.astral.sh/uv/concepts/projects/layout/).

#### Evidence Spikes

SPK-001 recommended before implementation.

#### Tradeoffs

Pre-1.0 version churn; pin uv in CI.

#### Failure Modes

Lockfile noise across OS; agents inventing pip-only flows.

#### Alternatives Considered

Poetry, PDM, Hatch, pip+venv+pip-tools.

#### Downstream Implications

Foundry generator always emits uv projects; dogfood foundry CLI itself with uv.

#### Revisit Triggers

uv 1.0 stability story changes; packaging.python.org strongly recommends a different single tool.

---

### REC-003 — Project layout by archetype

- **Classification:** Default
- **Applies to:** Core layouts
- **Confidence:** High
- **Decision urgency:** Required now
- **Evidence quality:** Strong
- **Related decisions:** REC-002

#### Recommendation

- **CLI / installable package / data-ETL app:** `src/<package>/`, `[project.scripts]`, top-level `tests/`, package init via uv package flow.
- **Script archetype:** single module with **PEP 723** inline metadata; run via `uv run`.
- Prefer **src layout** over flat for packaged projects.

#### Requirements and Constraints

No notebooks; three archetypes only for v1.

#### Rationale

Matches packaging.python.org and uv init guidance; reduces import confusion; clear for agents.

#### Evidence

EVD-004; [src vs flat](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/); [uv init](https://docs.astral.sh/uv/concepts/projects/init/).

#### Evidence Spikes

None.

#### Tradeoffs

src layout needs proper install/editable semantics for local runs.

#### Failure Modes

Agents running modules as scripts from `src/` incorrectly; packaging tests inside the package.

#### Alternatives Considered

Flat layout; monorepo workspaces (defer).

#### Downstream Implications

Generator catalog templates; AI-native docs paths.

#### Revisit Triggers

uv changes default init layout materially.

---

### REC-004 — Ruff for lint and format

- **Classification:** Required
- **Applies to:** Core
- **Confidence:** High
- **Decision urgency:** Required now
- **Evidence quality:** Strong
- **Related decisions:** REC-013

#### Recommendation

**Ruff** is Required Core for **lint and format** (`ruff check`, `ruff format`). Do not ship black/isort/flake8 as Default Core.

#### Requirements and Constraints

Pin ruff via uv dev dependency; configure in `pyproject.toml`; CI must fail on check/format.

#### Rationale

One tool replaces multi-tool stacks; excellent docs; Astral alignment with uv; simpler for agents.

#### Evidence

EVD-005; [Ruff FAQ](https://docs.astral.sh/ruff/faq/); [Ruff configuration](https://docs.astral.sh/ruff/configuration/).

#### Evidence Spikes

None.

#### Tradeoffs

Default rule-set expansions across minor versions may surprise upgrades — pin versions.

#### Failure Modes

Unpinned ruff major/minor churn in CI.

#### Alternatives Considered

flake8+isort+black; ruff lint + black format hybrid.

#### Downstream Implications

Hook and CI steps; agent command surface.

#### Revisit Triggers

Ruff formatter diverges unacceptably from team preference; custom lint plugins required.

---

### REC-005 — Type checking: ty Required Core (User decision)

- **Classification:** Required
- **Applies to:** Core typecheck
- **Confidence:** Medium (tool maturity) / **High** (owner lock)
- **Decision urgency:** Required now
- **Evidence quality:** Strong on existence/docs; Medium on production readiness
- **Related decisions:** REC-013, REC-014

#### Recommendation

**ty** is **Required Core** as the static type checker for Generated Projects and the foundry dogfood path. Wire `uv run ty` (or documented equivalent) into the command surface and CI. Pyright/BasedPyright/mypy are **not** Default Core but remain documented escape hatches if ty blocks a project (Exception path, not dual-default).

#### Requirements and Constraints

- **User decision (2026-07-31):** owner requires ty in Core despite research v0.1 Watchlist preference.
- Residual risk **RSK-002** (beta/incomplete type system) is **accepted**, not ignored.
- **SPK-002** is recommended before heavy implementation reliance.
- AI-native track should document ty LSP/agent diagnostics.

#### Rationale

Owner prioritizes Astral monostack coherence (uv + ruff + ty) and agent-simple one-vendor toolchain. Research still notes maturity limits; User decision outranks research preference for this personal foundry.

#### Evidence

EVD-006 (maturity caveats); EVD-016 (User decision); [astral-sh/ty](https://github.com/astral-sh/ty).

#### Evidence Spikes

**SPK-002 recommended** — sample CLI: config, common typing patterns, CI integration.

#### Tradeoffs

Higher risk of false negatives/positives and breaking ty upgrades vs Pyright stability; lower multi-vendor complexity.

#### Failure Modes

Agents over-trust ty; CI flakes on ty upgrades; need emergency Exception to another checker.

#### Alternatives Considered

Pyright/BasedPyright Default with ty Watchlist (v0.1 research preference — **superseded** by User decision); mypy Default; no type checker (rejected).

#### Downstream Implications

pyproject `[tool.ty]` (or current ty config); CI typecheck step; AI-native LSP defaults.

#### Revisit Triggers

ty abandonment or blocking bugs; SPK-002 failure; owner DEC to switch checkers.

---

### REC-006 — pytest Required Core

- **Classification:** Required
- **Applies to:** Core
- **Confidence:** High
- **Decision urgency:** Required now
- **Evidence quality:** Strong
- **Related decisions:** REC-003, REC-013

#### Recommendation

**pytest** is Required Core. **pytest-cov** Default. **pytest-xdist** Optional. Tests under top-level `tests/` with config in `pyproject.toml`.

#### Requirements and Constraints

`uv run pytest` must work on a fresh sync; CLI archetype includes at least a smoke test template.

#### Rationale

De facto standard; best agent ergonomics (plain assert, fixtures, selection flags).

#### Evidence

EVD-007; [pytest get started](https://docs.pytest.org/en/stable/getting-started.html); [pytest configuration](https://docs.pytest.org/en/stable/reference/customize.html).

#### Evidence Spikes

None.

#### Tradeoffs

Plugin sprawl if unrestricted — keep Optional list short.

#### Failure Modes

Empty test suites that still “pass”; coverage theater without meaningful tests.

#### Alternatives Considered

unittest-only; tox/nox as primary (heavier).

#### Downstream Implications

CI job; hooks optionally run pytest.

#### Revisit Triggers

None expected.

---

### REC-007 — Git hooks: pre-commit Default; hk Optional

- **Classification:** Default (pre-commit); Optional (hk)
- **Applies to:** Core hooks vs `hooks-hk` profile
- **Confidence:** High
- **Decision urgency:** Required now
- **Evidence quality:** Strong (ecosystem); owner preference is User decision if overridden
- **Related decisions:** REC-004, REC-008, REC-014

#### Recommendation

- **Default Core:** **pre-commit** with local/`uv run` hooks for ruff and tests as appropriate.
- **Optional profile `hooks-hk`:** **hk** for owners who want jdx tooling and performance.
- Do **not** require hk in every Generated Project solely from owner taste without accepting residual ecosystem risk.

#### Requirements and Constraints

Blueprint L5 listed hk as candidate — **demoted from Required** on evidence; available as profile to preserve owner workflow.

#### Rationale

pre-commit is universal, YAML-configured, and widely understood by agents and docs. hk is capable and documented but newer, Pkl-configured, and less universal.

#### Evidence

EVD-008; [hk docs](https://hk.jdx.dev/getting_started.html); [pre-commit](https://pre-commit.com/).

#### Evidence Spikes

SPK-003 if owner insists on hk Default.

#### Tradeoffs

Owner’s preferred stack not 100% Core; profile adds a branch in the generator.

#### Failure Modes

Shipping both without clear default confuses agents.

#### Alternatives Considered

hk-as-Required Core (not recommended unless User decision DEC); no hooks (rejected).

#### Downstream Implications

Generator profiles; AI-native hook docs.

#### Revisit Triggers

Owner DEC to force hk Core; hk becomes de-facto standard; SPK-003 shows large wins.

---

### REC-008 — Secrets: fnox Required Core; no `.env` secret storage (User decision)

- **Classification:** Required (fnox); **Rejected** (`.env`/dotenv for secrets)
- **Applies to:** Core secrets model
- **Confidence:** Medium (fnox ecosystem) / **High** (owner lock)
- **Decision urgency:** Required now
- **Evidence quality:** Moderate–Strong (fnox docs); User decision on no-dotenv
- **Related decisions:** REC-013, REC-014

#### Recommendation

- **fnox** is **Required Core** for secrets: committed `fnox.toml`; run via **`fnox exec -- …`** (or documented equivalent) so secrets inject as env vars at runtime.
- **Default provider: `age`** (User decision). Core templates and docs assume age-encrypted secrets (ciphertext in-repo or age-managed keys per machine), not 1Password/AWS/etc. as the default path.
- Other fnox providers remain **allowed Exception/profile extensions**, not the Core default.
- **Do not** use **`.env` / python-dotenv / committed env files** as the secret-storage pattern for Generated Projects. Do not ship `.env.example` as a secrets template that trains agents to keep secrets in dotenv files.
- Gitignore any local override files fnox uses (e.g. `fnox.local.toml` if applicable); never commit plaintext secrets or age private keys.
- Non-secret configuration may still use ordinary config files (TOML/YAML/flags) — this REC is about **secrets**, not all config.

#### Requirements and Constraints

- **User decision (2026-07-31):** owner requires fnox in Core, rejects `.env` secret storage, and selects **age** as the default provider.
- Templates and agent docs must not reintroduce dotenv “for convenience.”
- Residual risk **RSK-007** (fnox install/learning curve; age key management for agents).

#### Rationale

Owner does not want secrets in dotenv files. fnox + **age** matches offline-friendly, git-friendly encrypted secrets without requiring a cloud secret manager for the personal default path.

#### Evidence

EVD-009; EVD-016; EVD-017; [fnox](https://fnox.jdx.dev/).

#### Evidence Spikes

Optional later: smoke `fnox exec` + **age** provider on Linux/macOS for template docs.

#### Tradeoffs

Higher onboarding cost than dotenv; every project depends on fnox + age key hygiene; multi-machine needs age key distribution story.

#### Failure Modes

Agents invent `.env` anyway; missing fnox/age keys in CI/dev; mis-committed plaintext or **private** age keys in git.

#### Alternatives Considered

dotenv Core + fnox profile (v0.1 — **superseded**); 1Password as default provider (**not selected**); direnv-only.

#### Downstream Implications

Core template includes `fnox.toml` skeleton with **age** provider; docs for age key setup; command surface uses `fnox exec`; AI-native skills forbid dotenv secrets; CI uses mocks or age-compatible secret injection without `.env` files.

#### Revisit Triggers

fnox abandonment; owner DEC re-allowing dotenv or switching default provider; SPK proving agent failure rate too high.

---

### REC-009 — HTTP client profile (httpx)

- **Classification:** Optional
- **Applies to:** `profile:http`
- **Confidence:** Medium–High
- **Decision urgency:** Required before implementation (profile shape)
- **Evidence quality:** Strong (docs)
- **Related decisions:** REC-014

#### Recommendation

Do **not** put **httpx** in universal Core. Ship **`profile:http`** with **httpx**, defaulting to **sync** API for CLI/scripts. Prefer httpx over requests for new HTTP work when the profile is enabled.

#### Requirements and Constraints

L5 “httpx when networking” → profile, not always-on dependency.

#### Rationale

Many CLIs need zero HTTP; Core must stay minimal. httpx is the better modern default when needed (timeouts, typing, sync+async).

#### Evidence

EVD-010; [httpx](https://www.python-httpx.org/); [timeouts](https://www.python-httpx.org/advanced/timeouts/).

#### Evidence Spikes

None.

#### Tradeoffs

Projects that always HTTP still one profile flag away.

#### Failure Modes

Pulling httpx into every template bloats simple tools.

#### Alternatives Considered

httpx Core; requests Default; urllib only.

#### Downstream Implications

Generator profile; examples.

#### Revisit Triggers

Foundry decides all templates are network CLIs.

---

### REC-010 — CLI framework default (Typer)

- **Classification:** Default
- **Applies to:** CLI archetype Core
- **Confidence:** High
- **Decision urgency:** Required now
- **Evidence quality:** Strong
- **Related decisions:** REC-003

#### Recommendation

Default CLI framework: **Typer**. Offer **Click** as alternate template/profile for minimalism/stability. Do not default to argparse. Keep cyclopts on Watchlist.

#### Requirements and Constraints

CLI archetype only; scripts may use argparse/typer lightly or plain `main`.

#### Rationale

Type-hint driven CLIs reduce boilerplate and help agents; mature docs.

#### Evidence

EVD-011; Typer docs/releases; [Click](https://click.palletsprojects.com/).

#### Evidence Spikes

None.

#### Tradeoffs

Typer dependency weight and occasional API churn vs Click stability.

#### Failure Modes

Agents mixing Click and Typer patterns in one app.

#### Alternatives Considered

Click Default; argparse Default; cyclopts Default.

#### Downstream Implications

CLI template code; skills for adding commands.

#### Revisit Triggers

Typer major break; owner prefers Click-only.

---

### REC-011 — Data/ETL optional profile

- **Classification:** Optional
- **Applies to:** `profile:data-etl`
- **Confidence:** High
- **Decision urgency:** Required before implementation (profile contents)
- **Evidence quality:** Strong
- **Related decisions:** REC-003, REC-014

#### Recommendation

No data libraries in universal Core. **`profile:data-etl`**: default **polars + pyarrow**; **extras: duckdb, pandas** (explicit opt-in within profile). No notebooks.

#### Requirements and Constraints

Owner uses pandas/duckdb regularly — supported as first-class extras, not forced defaults for every ETL project.

#### Rationale

Heavy native deps must stay optional; polars+pyarrow is a modern zero-friction DataFrame+interop baseline; duckdb/pandas remain important and available.

#### Evidence

EVD-012; Polars install docs; DuckDB Python docs; pandas 3.x notes from research pass.

#### Evidence Spikes

None.

#### Tradeoffs

pandas-not-default may surprise owner — mitigate with easy extra and docs.

#### Failure Modes

Core bloat; conflicting pandas+polars dual-stack without need.

#### Alternatives Considered

pandas+duckdb as profile defaults (owner-shaped); all four always-on (rejected).

#### Downstream Implications

Generator profile flags; example ETL project.

#### Revisit Triggers

Owner DEC to make pandas+duckdb the profile default instead of polars.

---

### REC-012 — GitHub Actions Core CI

- **Classification:** Required
- **Applies to:** Core
- **Confidence:** High
- **Decision urgency:** Required now
- **Evidence quality:** Strong
- **Related decisions:** REC-002, REC-004, REC-005, REC-006

#### Recommendation

Ship **GitHub Actions** workflow as Core:

- `permissions: contents: read` (minimum)
- **ubuntu-latest** required; **macos-latest** optional (cost-sensitive)
- Matrix over supported Python versions from `requires-python`
- **astral-sh/setup-uv** with cache
- `uv sync --locked` (or equivalent locked install)
- ruff check + format check
- typecheck step: **`uv run ty`** (or project-documented ty invocation) per REC-005
- `uv run pytest`
- No Windows runners
- Secrets: CI must not rely on committed `.env`; use GitHub Actions secrets + fnox providers or non-secret test fixtures

#### Requirements and Constraints

Blueprint L7; pin actions by SHA in implementation; ty Core implies typecheck job is not optional.

#### Rationale

Official uv GHA guide; closed, agent-visible quality gate; matches dogfooding with ty.

#### Evidence

EVD-013; [uv in GitHub Actions](https://docs.astral.sh/uv/guides/integration/github/); [ruff-action](https://github.com/astral-sh/ruff-action).

#### Evidence Spikes

None.

#### Tradeoffs

macOS minutes cost; matrix explosion if too many Python versions; ty version pins in CI.

#### Failure Modes

Unpinned actions; ty breakage on upgrade; agents smuggling `.env` into workflows.

#### Alternatives Considered

Linux-only matrix always; no typecheck in CI (rejected); Pyright in CI instead of ty (superseded by REC-005).

#### Downstream Implications

Template workflow file; evidence gates for foundry product later.

#### Revisit Triggers

Astral changes recommended GHA pattern.

---

### REC-013 — Agent/human command surface

- **Classification:** Default
- **Applies to:** Core documentation and templates
- **Confidence:** High
- **Decision urgency:** Required now
- **Evidence quality:** Strong
- **Related decisions:** REC-002, REC-004, REC-005, REC-006, REC-007

#### Recommendation

Document a **minimal uv-first + fnox** command surface:

```text
uv sync
uv run ruff check .
uv run ruff format .
uv run ty check          # or project-documented ty CLI form
uv run pytest
uv run pre-commit run --all-files
fnox exec -- uv run <entry>    # when the command needs secrets
```

Optional: `just`/`make` wrappers that only call the above. Do not document dotenv workflows for secrets.

#### Requirements and Constraints

AI-native track will amplify these commands in skills; keep stable names; secrets always via fnox (REC-008).

#### Rationale

`uv run` is the official project-scoped entry point; `fnox exec` is the owner-required secrets boundary.

#### Evidence

EVD-014; EVD-016; [uv tools](https://docs.astral.sh/uv/concepts/tools/); [fnox](https://fnox.jdx.dev/).

#### Evidence Spikes

None.

#### Tradeoffs

Hooks tool name changes if `hooks-hk` profile selected; agents must learn fnox.

#### Failure Modes

Docs listing five equivalent ways to run tests; docs showing `.env` “quick start.”

#### Alternatives Considered

tox/nox primary; poetry run; dotenv-based run (rejected for secrets).

#### Downstream Implications

README/AGENTS.md in Generated Projects; AI-native skills; forbid dotenv secret patterns.

#### Revisit Triggers

uv changes `uv run` semantics; fnox CLI UX changes.

---

### REC-014 — Core vs profile membership and L5 disposition

- **Classification:** Required (program structure)
- **Applies to:** Generator Core definition
- **Confidence:** High
- **Decision urgency:** Required now
- **Evidence quality:** Strong (composite)
- **Related decisions:** REC-001..REC-013

#### Recommendation

Adopt the membership tables in §2 Executive Answer as the v1 closed set. Explicit L5 dispositions:

| L5 candidate | Disposition | REC |
| ------------ | ----------- | --- |
| uv | **Confirm** Required Core | REC-002 |
| ruff | **Confirm** Required Core | REC-004 |
| ty | **Confirm** Required Core (**User decision**) | REC-005 |
| pytest | **Confirm** Required Core | REC-006 |
| hk | Optional profile `hooks-hk`; Default pre-commit | REC-007 |
| fnox | **Confirm** Required Core (**User decision**); provider **age**; **no `.env` secrets** | REC-008 |
| httpx | Optional profile `http` | REC-009 |

#### Requirements and Constraints

Closed sets over kitchen sinks (Charter). User decisions on ty/fnox/no-dotenv are locked for v1 unless amended.

#### Rationale

Evidence-backed Core plus explicit owner locks on Astral types and jdx secrets; remaining preferences (hk, httpx, data) stay profiled.

#### Evidence

Composite EVD-001..014; EVD-016; Exa run index.

#### Evidence Spikes

SPK-001..003 as listed (SPK-002 elevated).

#### Tradeoffs

Core includes tools with residual maturity risk (ty, fnox) per owner priority.

#### Failure Modes

Silent re-expansion of Core; reintroduction of dotenv secrets by agents/templates.

#### Alternatives Considered

v0.1 demotions of ty/fnox (superseded by User decision); empty Core (rejected).

#### Downstream Implications

Architecture catalog; synthesis REQs; AI-native secret and typecheck skills.

#### Revisit Triggers

DEC records; tool maturity changes; SPK results.

## 10. Evidence Ledger

| ID | Claim | Classification | Source / spike | Tier | Access date | Confidence | Limitations | Downstream |
| -- | ----- | -------------- | -------------- | ---- | ----------- | ---------- | ----------- | ---------- |
| EVD-001 | CPython 3.10–3.14 support windows / EOL matter for 2026 defaults | Official claim | [devguide.python.org/versions](https://devguide.python.org/versions/) | 1 | 2026-07-31 | High | Dates move; re-check at implementation | REC-001 |
| EVD-002 | uv Tier 1 includes 3.10–3.14 | Official claim | [uv Python support](https://docs.astral.sh/uv/reference/policies/python/) | 1 | 2026-07-31 | High | Policy can change | REC-001, REC-002 |
| EVD-003 | uv project workflow, lock, scripts are first-class | Official claim | [uv projects](https://docs.astral.sh/uv/guides/projects/), [layout](https://docs.astral.sh/uv/concepts/projects/layout/) | 1 | 2026-07-31 | High | Pre-1.0 churn | REC-002 |
| EVD-004 | src layout preferred for packages | Official claim | [src vs flat](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) | 1 | 2026-07-31 | High | Flat OK for trivial apps | REC-003 |
| EVD-005 | Ruff replaces flake8/isort/black for most lint/format | Official claim | [Ruff FAQ](https://docs.astral.sh/ruff/faq/), [config](https://docs.astral.sh/ruff/configuration/) | 1 | 2026-07-31 | High | Rule defaults expand over time | REC-004 |
| EVD-006 | ty has beta/maturity caveats vs mature pyright line | Inference + maintainer/repo signals | [astral-sh/ty](https://github.com/astral-sh/ty); Exa type-checking query grounding | 1–4 | 2026-07-31 | High | Residual risk accepted via User decision Core | REC-005, RSK-002 |
| EVD-007 | pytest is standard test runner with pyproject config | Official claim | [pytest docs](https://docs.pytest.org/en/stable/getting-started.html) | 1 | 2026-07-31 | High | Plugin defaults partial | REC-006 |
| EVD-008 | pre-commit is mature default; hk is capable alternative | Official claim + comparison | [pre-commit.com](https://pre-commit.com/), [hk.jdx.dev](https://hk.jdx.dev/getting_started.html) | 1 | 2026-07-31 | High | Owner may still force hk | REC-007 |
| EVD-009 | fnox is a viable secrets tool with committed config + providers | Official claim + judgment | [fnox.jdx.dev](https://fnox.jdx.dev/) | 1–3 | 2026-07-31 | Medium | Youth of fnox; Core by User decision | REC-008 |
| EVD-016 | Owner requires Core ty + Core fnox; forbids `.env` secret storage | User decision | Owner instruction 2026-07-31 (recorded in report v0.2+) | User | 2026-07-31 | High | Durable only via this report / later DEC | REC-005, REC-008, REC-014 |
| EVD-017 | Owner selects **age** as default fnox provider for Core templates | User decision | Owner instruction 2026-07-31 | User | 2026-07-31 | High | Other providers optional later | REC-008, OQ-006 closed |
| EVD-010 | httpx is modern HTTP default when needed | Official claim | [python-httpx.org](https://www.python-httpx.org/) | 1 | 2026-07-31 | Medium–High | Pre-1.0 notes | REC-009 |
| EVD-011 | Typer is strong agent-friendly CLI default; Click is stable alt | Official claim + judgment | Typer docs; [Click](https://click.palletsprojects.com/) | 1–3 | 2026-07-31 | High | Typer churn episodes | REC-010 |
| EVD-012 | Data libs belong in profile; polars/duckdb/pandas/pyarrow active 2026 | Official claim + judgment | Polars/DuckDB/pandas/Arrow docs via Exa pass | 1–3 | 2026-07-31 | High | Profile default is judgment | REC-011 |
| EVD-013 | setup-uv + locked sync + pytest is recommended GHA pattern | Official claim | [uv GHA guide](https://docs.astral.sh/uv/guides/integration/github/) | 1 | 2026-07-31 | High | Action versions drift | REC-012 |
| EVD-014 | `uv run` is the project-scoped command entry | Official claim | [uv tools](https://docs.astral.sh/uv/concepts/tools/) | 1 | 2026-07-31 | High | — | REC-013 |
| EVD-015 | Exa multi-query pass completed 13/13 deep-reasoning | Experimental result | `scripts/exa-output/ecosystem-20260731T170320Z/run-meta.json` | 3 | 2026-07-31 | High | Local path; not portable authority | Methodology |

## 11. Recommendation Ledger

| ID | Title | Classification | Confidence | Core/Profile |
| -- | ----- | -------------- | ---------- | ------------ |
| REC-001 | Python version floor/default | Default | High | Core |
| REC-002 | uv packaging | Required | High | Core |
| REC-003 | Layout by archetype | Default | High | Core |
| REC-004 | Ruff lint+format | Required | High | Core |
| REC-005 | Type checker ty Required Core | Required | Medium/High | Core (User decision) |
| REC-006 | pytest | Required | High | Core |
| REC-007 | Hooks pre-commit / hk | Default + Optional | High | Core + profile |
| REC-008 | Secrets fnox Core; no `.env` | Required + Rejected dotenv | Medium/High | Core (User decision) |
| REC-009 | httpx HTTP profile | Optional | Medium–High | profile:http |
| REC-010 | Typer CLI default | Default | High | CLI archetype |
| REC-011 | data-etl profile | Optional | High | profile:data-etl |
| REC-012 | GitHub Actions CI | Required | High | Core |
| REC-013 | Command surface | Default | High | Core |
| REC-014 | Core membership / L5 disposition | Required | High | Program |

## 12. Risks

### RSK-001 — uv pre-1.0 churn

- **Likelihood:** Medium | **Impact:** Medium
- **Mitigation:** Pin uv version in CI and docs; lockfiles
- **Residual:** Breaking uv upgrades
- **Related:** REC-002

### RSK-002 — ty maturity as Required Core

- **Likelihood:** Medium | **Impact:** Medium–High
- **Mitigation:** Pin ty version; SPK-002; Exception path to alternate checker documented; CI fail-closed on ty
- **Residual:** Beta gaps / false confidence remain **accepted** per User decision
- **Related:** REC-005, EVD-006, EVD-016

### RSK-003 — hk still demoted (owner may want later)

- **Likelihood:** Low–Medium | **Impact:** Low
- **Mitigation:** `hooks-hk` profile remains available
- **Related:** REC-007

### RSK-004 — Data profile default (polars) mismatches owner pandas habits

- **Likelihood:** Medium | **Impact:** Low
- **Mitigation:** pandas/duckdb as easy extras; optional DEC for default swap
- **Related:** REC-011

### RSK-005 — CI macOS cost

- **Likelihood:** Medium | **Impact:** Low
- **Mitigation:** Linux-required; macOS optional
- **Related:** REC-012

### RSK-006 — Exa synthesis overclaim without primary re-read

- **Likelihood:** Medium | **Impact:** Medium
- **Mitigation:** Source ledger primary URLs; validation pass; spikes before implement
- **Related:** Methodology, EVD-015

### RSK-007 — fnox as Required Core; no dotenv fallback

- **Likelihood:** Medium | **Impact:** Medium
- **Mitigation:** Template `fnox.toml` skeleton with **age** provider; agent skills forbidding `.env` secrets; age key setup docs; CI patterns without dotenv
- **Residual:** Agents reintroduce `.env`; missing age keys; fnox not installed in some environments
- **Related:** REC-008, EVD-016, EVD-017

## 13. Weak Evidence

- Exact “production ready” bar for **ty** beyond repo/beta messaging — **Core anyway** via User decision; bound with SPK-002 + pins.
- **fnox** long-term Python-ecosystem adoption — Medium confidence; Core via User decision.
- **httpx** exact release train at research date — Medium confidence on version pins.
- Whether packaging.python.org “endorses uv as the single tool” in prose — use uv + packaging tutorial alignment carefully; do not overclaim.

## 14. Conflicting Evidence

| Topic | Conflict | Resolution in this report |
| ----- | -------- | ------------------------- |
| Type checker | Research preferred Pyright; owner wants ty | **ty Required Core** (User decision); residual RSK-002 |
| Hooks | Owner likes hk; ecosystem default pre-commit | pre-commit Default; hk profile (unchanged) |
| Secrets | Research preferred dotenv; owner forbids `.env` secrets | **fnox Required Core**; dotenv rejected for secrets |
| Data defaults | Owner pandas/duckdb; research polars-first profile | polars default + pandas/duckdb extras |
| Python default | Some docs show 3.14 examples; safety says 3.13 pin | Floor 3.12; default 3.13 |

## 15. Assumptions

1. Personal foundry prioritizes owner-locked Astral types + jdx secrets over research’s more conservative defaults.
2. Residual maturity risk on ty/fnox is acceptable to the owner for v1.
3. macOS CI is desirable but not mandatory for every personal repo.
4. Owner accepts profiles for **hk** and **httpx** (not forced Core).
5. Exa `deep-reasoning` outputs are leads requiring primary URL grounding (done selectively in ledger).
6. “No `.env` secrets” does not ban non-secret config files.

## 16. Open Questions

### OQ-001 — Exact ty CLI/config defaults in templates

- **Blocking?** No for architecture high-level; **Yes** before template freeze
- **Resolution path:** ty docs + SPK-002; AI-native LSP wiring
- **Deadline:** Before synthesis template REQs finalize

### OQ-002 — SPK-002 timing (before vs during implementation Phase 1)

- **Blocking?** No for accepting this report; recommended before heavy codegen
- **Resolution path:** Schedule SPK-002
- **Deadline:** Implementation gate

### OQ-003 — Force hk into Core via User DEC?

- **Blocking?** Only if owner rejects pre-commit Default
- **Resolution path:** Explicit DEC-### 
- **Deadline:** Before Blueprint-affecting Core freeze in synthesis

### OQ-004 — data-etl default engine pandas+duckdb vs polars+pyarrow

- **Blocking?** No
- **Resolution path:** Owner preference DEC or leave as recommended default
- **Deadline:** Before data profile implementation

### OQ-005 — macOS matrix always-on vs opt-in

- **Blocking?** No
- **Resolution path:** Cost preference
- **Deadline:** Implementation plan

### OQ-006 — Default fnox provider (age vs 1Password vs other) in Core templates

- **Status:** **Resolved (2026-07-31)**
- **Resolution:** Default provider is **`age`** (User decision / EVD-017).
- **Residual:** Document age key setup for agents and multi-machine; other providers remain non-default options.

## 17. Handoff Digest

### Decisions supported

- uv + ruff + **ty** + pytest + **fnox** + GHA + src layout + uv/fnox command surface as Core backbone
- **No `.env` secret storage**
- **fnox default provider: age**
- Profiles for HTTP, hooks-hk, data-etl only (fnox is Core, not a secrets profile)
- Python ≥3.12 with 3.13 default pin

### Recommendations accepted by this report

REC-001..REC-014 as written in **v0.2**.

### Recommendations challenged / revised

- v0.1 ty Watchlist → **v0.2 ty Required Core** (User decision) (REC-005)
- v0.1 dotenv Core / fnox profile → **v0.2 fnox Core; dotenv rejected for secrets** (User decision) (REC-008)
- hk as Required Core → **Optional profile** (REC-007) — still demoted unless owner amends
- httpx as universal Core → **Optional profile** (REC-009) — unchanged

### Evidence strength

Strong for uv/ruff/pytest/layout/CI; **User decision** elevates ty/fnox despite medium maturity evidence; residual **RSK-002**, **RSK-007**.

### Weak and conflicting evidence

See §13–§14.

### Assumptions

See §15.

### Risks

RSK-001..RSK-007.

### Open questions

OQ-001..OQ-006.

### Required downstream decisions

| Consumer | Needs |
| -------- | ----- |
| AI-native track | Command surface REC-013; **ty** LSP; **fnox** skills; **forbid dotenv secrets** |
| Architecture | Core/profile catalog from REC-014; layouts REC-003; CI with ty REC-012; generator emits uv+fnox+ty |
| Synthesis | Trace RECs → REQs; resolve OQ-001/004/006 with owner if needed |
| Owner | Confirm v0.2 Core locks (ty, fnox+age, no dotenv secrets) |

### Relevant identifiers

REC-001..014; RSK-001..007; OQ-001..006 (006 resolved); EVD-001..017; SPK-001..003 (planned).

### Full-report sections that must be read before deciding

§2 Executive Answer; §9 REC-005/008/014; §12–§16; §10 Evidence Ledger.

## 18. Source Ledger

| Title | URL | Publisher | Access date | Used for |
| ----- | --- | --------- | ----------- | -------- |
| Status of Python versions | https://devguide.python.org/versions/ | Python devguide | 2026-07-31 | REC-001 |
| uv Python support | https://docs.astral.sh/uv/reference/policies/python/ | Astral | 2026-07-31 | REC-001 |
| uv projects guide | https://docs.astral.sh/uv/guides/projects/ | Astral | 2026-07-31 | REC-002 |
| uv project layout | https://docs.astral.sh/uv/concepts/projects/layout/ | Astral | 2026-07-31 | REC-002 |
| uv creating projects | https://docs.astral.sh/uv/concepts/projects/init/ | Astral | 2026-07-31 | REC-003 |
| src vs flat layout | https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/ | PyPA | 2026-07-31 | REC-003 |
| Ruff FAQ | https://docs.astral.sh/ruff/faq/ | Astral | 2026-07-31 | REC-004 |
| Ruff configuration | https://docs.astral.sh/ruff/configuration/ | Astral | 2026-07-31 | REC-004 |
| astral-sh/ty | https://github.com/astral-sh/ty | Astral | 2026-07-31 | REC-005 |
| pytest get started | https://docs.pytest.org/en/stable/getting-started.html | pytest | 2026-07-31 | REC-006 |
| pytest configuration | https://docs.pytest.org/en/stable/reference/customize.html | pytest | 2026-07-31 | REC-006 |
| pre-commit | https://pre-commit.com/ | pre-commit | 2026-07-31 | REC-007 |
| hk getting started | https://hk.jdx.dev/getting_started.html | jdx | 2026-07-31 | REC-007 |
| fnox | https://fnox.jdx.dev/ | jdx | 2026-07-31 | REC-008 |
| HTTPX | https://www.python-httpx.org/ | encode | 2026-07-31 | REC-009 |
| Click docs | https://click.palletsprojects.com/ | Pallets | 2026-07-31 | REC-010 |
| Polars installation | https://docs.pola.rs/user-guide/installation/ | Polars | 2026-07-31 | REC-011 |
| uv GitHub Actions | https://docs.astral.sh/uv/guides/integration/github/ | Astral | 2026-07-31 | REC-012 |
| ruff-action | https://github.com/astral-sh/ruff-action | Astral | 2026-07-31 | REC-012 |
| uv tools concept | https://docs.astral.sh/uv/concepts/tools/ | Astral | 2026-07-31 | REC-013 |
| Exa Deep blog | https://exa.ai/blog/exa-deep | Exa | 2026-07-31 | Methodology |
| Exa search API guide | https://exa.ai/docs/reference/search-api-guide | Exa | 2026-07-31 | Methodology |
| Local Exa run index | `scripts/exa-output/ecosystem-20260731T170320Z/INDEX.md` | local | 2026-07-31 | EVD-015 (non-portable) |

## 19. Completion Checklist

- [x] All required report sections present
- [x] Actual research date recorded (2026-07-31)
- [x] Primary and subsidiary questions answered or OQ’d
- [x] REC-001..014 in range REC-001..099
- [x] RSK/OQ/SPK within assigned ranges
- [x] Evidence Ledger for load-bearing claims
- [x] Source ledger with URLs and access dates
- [x] Core vs profile tables complete
- [x] L5 candidates dispositioned
- [x] Credible alternatives compared for major tools
- [x] Handoff Digest complete
- [x] Allowed file scope respected (report + prior scripts only)
- [x] No downstream stages started
- [x] Owner revision v0.2 (ty + fnox Core; no `.env` secrets)
- [ ] Independent re-validation after v0.2
- [ ] Human acceptance
- [ ] Manifest accepted_commit recorded

## 20. Required tables (consolidated)

### Core membership

| Component | Membership | REC |
| --------- | ---------- | --- |
| Python ≥3.12 (default 3.13) | Required/Default | REC-001 |
| uv + uv.lock | Required | REC-002 |
| src layout / PEP 723 scripts | Default | REC-003 |
| ruff check+format | Required | REC-004 |
| **ty** | **Required** (User decision) | REC-005 |
| pytest | Required | REC-006 |
| pytest-cov | Default | REC-006 |
| pre-commit | Default | REC-007 |
| **fnox** + provider **age** (no `.env` secrets) | **Required** (User decision) | REC-008 |
| GitHub Actions CI | Required | REC-012 |
| uv run + fnox exec command docs | Default | REC-013 |
| Typer (CLI archetype) | Default | REC-010 |

### Profiles

| Profile ID | Contents | When |
| ---------- | -------- | ---- |
| `http` | httpx (sync default) | Networked tools |
| `hooks-hk` | hk | Owner jdx hooks preference |
| `data-etl` | polars+pyarrow; extras duckdb, pandas | ETL/pipelines |

### Archetype layout

| Archetype | Layout |
| --------- | ------ |
| CLI | src package + console script + tests/ |
| Script | PEP 723 single file |
| Data/ETL | Package layout + data-etl profile deps |

### CI matrix (recommended)

| OS | Python | Jobs |
| -- | ------ | ---- |
| ubuntu-latest | matrix from requires-python | ruff, **ty**, pytest |
| macos-latest | optional same | same |
| windows-latest | **never** | — |

### Command surface

See REC-013.

### L5 disposition

See REC-014.
