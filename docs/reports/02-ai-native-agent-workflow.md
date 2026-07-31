# AI-Native Repository & Agent Workflow

- **Artifact type:** Focused Research Report
- **Program:** python-foundry
- **Stage:** `research-ai-native`
- **Status:** Draft — awaiting validation and human acceptance
- **Version:** 0.1
- **Created:** 2026-07-31
- **Last updated:** 2026-07-31
- **Actual research date:** 2026-07-31
- **Depends on:** Accepted Program Blueprint; Accepted Research Charter; Accepted ecosystem report v0.2
- **Commissioning prompt:** `docs/prompts/02-ai-native-agent-workflow-prompt.md`
- **Recommendation range:** REC-100..REC-112 (remaining REC-113..199 reserved)
- **Evidence base:** Exa Deep (`deep-reasoning`) multi-query run
  `scripts/exa-output/ai-native-20260731T231539Z/` (local raw dumps; not governing);
  Grok harness `/deep-research` runs (smoke; command/LSP/fnox; skills/foundry catalog — Partial status with verified sources);
  Tier-1 primary docs fetched 2026-07-31 (agents.md, Claude Code, xAI Grok Build, agentskills.io, Astral, fnox, MCP)

> Research reports are **evidence and recommendations**, not commandments.
> Architecture and synthesis consume this report after acceptance.
> Ecosystem Core locks (ty, fnox+age, no dotenv secrets, REC-013 command surface)
> are **inherited constraints**, not reopened tool-selection questions.

## 1. Artifact Metadata

| Field | Value |
| ----- | ----- |
| Program ID | python-foundry |
| Stage ID | research-ai-native |
| Primary question | How should the foundry and Generated Projects be structured, documented, and instrumented so AI coding agents work optimally (skills, MCP, LSP, instructions, checks)? |
| Rigor | standard |
| Operator | robertguss |
| Agent implementers | Primary (Grok, Claude Code, Cursor, and similar) |

## 2. Executive Answer

**Portable-first, closed agent surface** for both the foundry product and Generated Projects:

| Layer | Recommendation |
| ----- | -------------- |
| Instructions | Root **`AGENTS.md`** Required (portable SoT). Thin **`CLAUDE.md`** Required adapter (`@AGENTS.md` import or symlink on macOS/Linux). **`.cursor/rules`** Optional only for glob/frontmatter needs. |
| Skills layout | Canonical **`.agents/skills/<name>/SKILL.md`** (agentskills.io). Claude adapter: **`.claude/skills/`** symlink or dual-path when native discovery of `.agents/skills` is not verified. Do not unbounded dual-copy skill *bodies*. |
| Core skill catalog (Generated Projects) | Closed set: `quality-gates`, `secrets-fnox`, `add-cli-command` (CLI archetype), `add-script` (script archetype) — purposes only; architecture emits bodies later. |
| Foundry-only skills | Research/program skills (`research-program`, `research-stage`, `research-validate`) stay in the research/foundry repos — **not** Generated Project Core. |
| MCP | Default **none** committed. Opt-in minimal project MCP only when needed. Kitchen-sink catalogs **Rejected**. |
| LSP / diagnostics | Editor: official **Ruff** + **ty** language servers/extensions. Agents: CLI gates via `uv run ruff` / `uv run ty check` for definition-of-done (do not assume agents ship ty LSP by default). |
| Command surface | Amplify ecosystem **REC-013**: `uv sync`, `uv run ruff check/format`, `uv run ty check`, `uv run pytest`, `uv run pre-commit run --all-files`, `fnox exec -- …` |
| Secrets | Agents use **`fnox exec -- …`** only; age provider; **forbid** dotenv/`.env` secret storage in docs and skills (ecosystem REC-008). |
| Multi-agent strategy | Portable-first + thin adapters; product-only trees only when portable layer cannot express the need. |
| Definition of done | Agent may not claim complete until documented quality gates pass (ruff, ty, pytest; pre-commit when configured); empty “0 tests collected” is not success for package/CLI archetypes. |

**Closed Core agent emit set (Generated Projects):**

```text
AGENTS.md
CLAUDE.md          # @AGENTS.md or symlink
.agents/skills/    # closed Core skills only
fnox.toml          # from ecosystem Core (age)
# no default .mcp.json / kitchen-sink MCP
# optional: .cursor/rules only if profile needs globs
```

## 3. Scope and Exclusions

### In scope

- Agent instruction files; portable skills; curated MCP/LSP; command surface for agents; secrets operability for agents; foundry vs Generated Project surfaces; multi-agent adapters; definition of done; closed catalog discipline.

### Out of scope

- Generator engine (spec → plan → generate) — architecture track
- Re-selecting uv/ruff/ty/pytest/fnox — accepted ecosystem report
- Building every MCP server; multi-agent orchestration product; model training
- Windows; notebooks; framework zoo; unlimited skill/MCP catalogs
- Granular coding backlog

## 4. Inherited Constraints

### Blueprint locks (selected)

| ID | Constraint |
| -- | ---------- |
| L3 | macOS + Linux only; never Windows |
| L9 | AI-native first: portable skills; curated MCP/LSP; agent-operable docs |
| Non-goal | Unlimited MCP/skill catalog — closed, curated only |

### Ecosystem Core locks (Accepted v0.2 — do not silently undo)

| Lock | Source |
| ---- | ------ |
| uv + lockfile; src layout; Ruff; **ty** Required; pytest; pre-commit Default; **fnox+age**; no dotenv secrets | REC-001..014 |
| Command surface `uv sync` / `uv run …` / `fnox exec -- …` | REC-013 |
| AI-native must document ty diagnostics, fnox skills, forbid dotenv secrets | Ecosystem Handoff Digest §17 |

## 5. Methodology

1. Read Blueprint, Charter, commissioning prompt, and **full** ecosystem report v0.2.
2. Smoke-compared Exa Deep vs Grok harness `/deep-research` on instruction-file layout (agreement on AGENTS.md + CLAUDE.md adapter; Grok stronger on Grok product docs and uncertainty).
3. Ran Exa Deep **`deep-reasoning`** multi-query across 8 decision areas (`scripts/exa_ai_native_evidence.py` → `scripts/exa-output/ai-native-20260731T231539Z/`).
4. Ran Grok `/deep-research` on command surface / LSP / fnox (Partial, verified sources).
5. Fetched Tier-1 primary pages (agents.md, Claude memory/skills/MCP, xAI project-rules, agentskills.io, Astral ruff/ty/uv, fnox, MCP intro).
6. One primary recommendation per decision area; residual uncertainty as OQ/RSK; no ID reuse of ecosystem ranges for new subjects.

## 6. Source Quality and Limitations

| Strength | Limitation |
| -------- | ---------- |
| Strong Tier-1 for Claude CLAUDE.md / `@AGENTS.md`, agents.md portable format, agentskills.io SKILL.md, Astral ruff/ty LSP+CLI, fnox exec, MCP opt-in | No single official “generator emit matrix” for all agents |
| Grok Build docs confirm AGENTS.md primary + multi-family compatibility reads | Claude Code documents **`.claude/skills/`** as native project skill path; native auto-discovery of `.agents/skills` not established in inspected Claude skills page |
| MCP context-cost guidance from MCP client best practices + Claude MCP docs | Config filenames fragment (`.mcp.json`, `.cursor/mcp.json`, `.vscode/mcp.json`, Grok config) |
| Ecosystem REC-008/013 as accepted program constraints for secrets/commands | Agent compliance with “never invent dotenv” is behavioral risk (RSK-050), not proven by docs alone |

Exa dumps and Grok workflow scratch reports are **evidence**, not governing artifacts.

## 7. Evidence Spikes

| ID | Intent | Status |
| -- | ------ | ------ |
| SPK-050 | Sample Generated Project tree: AGENTS.md + CLAUDE.md `@AGENTS.md` load behavior across agents | **Recommended** before implementation (multi-agent) |
| SPK-051 | Whether Claude Code discovers `.agents/skills` without `.claude/skills` adapter | **Recommended** — residual OQ-051 |
| SPK-052 | `fnox exec` + age smoke on Linux with agent-facing docs only | **Recommended** with ecosystem SPK residual |

No SPK executed in this research session; documentary evidence was sufficient for recommendations at standard rigor with explicit residual risk.

## 8. Comparative Analysis

### 8.1 Instruction files

| Option | Fit | Verdict |
| ------ | --- | ------- |
| AGENTS.md only | Portable; **fails Claude Code** (reads CLAUDE.md, not AGENTS.md natively) | Incomplete |
| CLAUDE.md only | Claude-good; weak multi-agent portability | Rejected as sole surface |
| AGENTS.md + thin CLAUDE.md (`@AGENTS.md` or symlink) | Portable SoT + Claude adapter; official Claude coexistence pattern | **Default/Required** |
| AGENTS.md + full dual-maintained CLAUDE.md body | Drift risk | Rejected |
| `.cursor/rules` only | Cursor-rich; loses AGENTS.md consumers | Rejected as sole surface |
| AGENTS.md + optional `.cursor/rules` for globs | Cursor advanced features without forking everything | Optional |

### 8.2 Skills layout

| Option | Fit | Verdict |
| ------ | --- | ------- |
| `.agents/skills/<name>/SKILL.md` only | Portable convention; Codex/Cursor/Grok often scan it | **Default canonical** |
| Product forks only (`.claude/skills`, `.cursor/skills`) | Unbounded maintenance | Rejected as sole strategy |
| Canonical `.agents/skills` + Claude adapter (symlink or thin dual path) | Addresses Claude native path | **Required until OQ-051 resolved** |
| Dual full copies of every skill | Drift | Rejected |

### 8.3 MCP

| Option | Fit | Verdict |
| ------ | --- | ------- |
| Kitchen-sink default MCP set | Context cost; kitchen sink non-goal | **Rejected** |
| Minimal always-on MCP (e.g. filesystem) | Often redundant with agent native tools | Optional Exception only |
| Default **none**; opt-in when needed | Matches personal CLI/scripts; closed catalog | **Default** |

### 8.4 LSP vs CLI diagnostics

| Path | Role |
| ---- | ---- |
| `ruff server` / Ruff extension; `ty server` / ty extension | Live editor diagnostics |
| `uv run ruff check/format`; `uv run ty check` | Agent DoD, pre-commit, CI |
| Assume stock Claude Python LSP = Pyright | **Do not** — Core is ty; agents must use CLI gates and optional custom ty LSP |

### 8.5 Multi-agent strategy

Portable-first + thin adapters beats per-product instruction/skill zoos. Product trees only for features the portable layer cannot express (Cursor globs, Claude slash-command packaging quirks, Grok-specific rules if ever required).

## 9. Recommendations

### REC-100 — Generated Project instruction files: AGENTS.md + CLAUDE.md adapter

- **Classification:** Required
- **Applies to:** Generated Projects (all archetypes)
- **Confidence:** High
- **Decision urgency:** Required now
- **Evidence quality:** Strong
- **Related decisions:** Blueprint L9; ecosystem REC-013

#### Recommendation

Emit:

1. **`AGENTS.md`** at repo root — portable source of truth (conventions, command surface, layout, DoD, secrets rules).
2. **`CLAUDE.md`** that either:
   - starts with `@AGENTS.md` and optional Claude-only notes below, **or**
   - is a symlink `CLAUDE.md → AGENTS.md` on macOS/Linux when no Claude-specific content is needed.

Do **not** emit product-only instruction trees as the sole surface. Keep `AGENTS.md` concise (prefer well under product caps; Grok documents large files with practical size pressure).

#### Requirements and Constraints

- Document the REC-013 command surface and fnox/no-dotenv rules inside `AGENTS.md`.
- Nested `AGENTS.md` allowed for monorepos; closest/more-specific wins (product-dependent merge rules).

#### Rationale

AGENTS.md is the open multi-agent “README for agents.” Claude Code officially coexists via `@AGENTS.md` import or symlink, not by natively loading AGENTS.md alone. Cursor and Grok Build treat AGENTS.md as a primary or first-class project instruction surface.

#### Evidence

EVD-100..103; [agents.md](https://agents.md/); [Claude memory](https://code.claude.com/docs/en/memory); [xAI project rules](https://docs.x.ai/build/features/project-rules); Exa `instruction-files`; Grok deep-research smoke.

#### Evidence Spikes

SPK-050 recommended.

#### Tradeoffs

One extra adapter file vs multi-agent breakage for Claude.

#### Failure Modes

Agents maintain divergent CLAUDE.md and AGENTS.md bodies; Claude-only projects skip AGENTS.md and lose portability.

#### Alternatives Considered

CLAUDE.md-only; AGENTS.md-only; full dual prose; `.cursorrules` legacy sole file.

#### Downstream Implications

Generator templates; architecture catalog of emitted files.

#### Revisit Triggers

Claude ships native AGENTS.md load; agents.md format becomes a formal standard with required schema.

---

### REC-101 — Foundry-repo agent surface differs from Generated Projects

- **Classification:** Required
- **Applies to:** Foundry product + research program repos
- **Confidence:** High
- **Decision urgency:** Required before implementation
- **Evidence quality:** Moderate–Strong (program structure + product patterns)
- **Related decisions:** REC-100, REC-103

#### Recommendation

| Surface | Foundry / research program | Generated Project |
| ------- | -------------------------- | ----------------- |
| `AGENTS.md` | Program authority, stage rules, skills index | Project conventions + command surface + DoD |
| Skills | Research methodology + foundry CLI skills | Closed Core skills only (REC-103) |
| MCP | May use richer owner MCP for research (Exa, GitHub) **without** baking into Generated Project defaults | Default none |
| Docs tree | Blueprint/Charter/reports contracts | Minimal README + AGENTS.md |

Do not ship research-program skills into every Generated Project.

#### Rationale

Foundry work is meta (spec, research, generation). Generated Projects are ordinary Python apps/scripts. Conflating them reintroduces oral tradition and skill bloat.

#### Evidence

EVD-104; Blueprint product shape; this repository’s `.agents/skills/` practice.

#### Downstream Implications

Architecture must emit different skill/instruction packages for foundry dogfood vs Generated Projects.

---

### REC-102 — Portable skills layout: `.agents/skills/` canonical

- **Classification:** Default (Required path convention for Core skills)
- **Applies to:** Foundry + Generated Projects
- **Confidence:** High (layout); Medium (Claude auto-discovery)
- **Decision urgency:** Required now
- **Evidence quality:** Strong (agentskills.io + multi-product scan); Medium (Claude `.agents/skills`)
- **Related decisions:** REC-100, REC-103, OQ-051

#### Recommendation

1. Author all Core skills as **`.agents/skills/<skill-name>/SKILL.md`** per [agentskills.io specification](https://agentskills.io/specification): YAML frontmatter `name` + `description` (name matches directory; lowercase/hyphens; description states when to use).
2. Keep bodies progressive-disclosure friendly (prefer &lt; ~500 lines; optional `scripts/`, `references/`, `assets/`).
3. **Do not** dual-maintain full copies under every product path.
4. Until OQ-051 is resolved: for Claude Code compatibility, emit a **thin adapter** — either symlink `.claude/skills/<name> → ../../.agents/skills/<name>` or document generator dual-path emit of the same skill directory for Claude-targeted templates.

#### Rationale

agentskills.io defines the skill package format; multi-product clients increasingly scan `.agents/skills`. Claude’s inspected docs emphasize `.claude/skills/` as the project skill root — residual adapter needed for closed multi-agent support without kitchen-sink forks.

#### Evidence

EVD-105..107; agentskills.io; Claude skills docs; Cursor/Codex skill paths via Exa `skills-layout`; Grok multi-path skill discovery (Exa multi-agent adapters).

#### Evidence Spikes

SPK-051.

#### Tradeoffs

Symlink/adapter complexity vs dual-copy drift.

#### Alternatives Considered

Product-only skills; dual full copies; no skills (instructions only).

#### Downstream Implications

Architecture generation of skill tree; skill authoring standards in foundry.

#### Revisit Triggers

Claude documents native `.agents/skills` discovery; agentskills.io location becomes normative.

---

### REC-103 — Closed Core skill catalog (Generated Projects)

- **Classification:** Required (closed set)
- **Applies to:** Generated Projects
- **Confidence:** Medium (catalog composition is program judgment on strong layout evidence)
- **Decision urgency:** Required before implementation
- **Evidence quality:** Moderate (inferred from Core tools + agent failure modes; no official “Python foundry skill list”)
- **Related decisions:** REC-005, REC-008, REC-013 (ecosystem); REC-102, REC-106, REC-107

#### Recommendation

**Core skills (always emit for package/CLI Generated Projects):**

| Skill id | Purpose |
| -------- | ------- |
| `quality-gates` | How/when to run ruff, ty, pytest, pre-commit; DoD checklist |
| `secrets-fnox` | `fnox exec`, age key hygiene, **forbid dotenv secrets** |

**Archetype skills (emit with archetype):**

| Skill id | Purpose | When |
| -------- | ------- | ---- |
| `add-cli-command` | Add Typer console command in src layout | CLI archetype |
| `add-script` | Add/maintain PEP 723 script + `uv run` | Script archetype |
| `data-etl-entry` | Entry patterns for data-etl profile (polars/duckdb) | `data-etl` profile |

**Explicitly not Core (Rejected as default emit):**

- Framework zoo skills (Django/FastAPI/notebooks)
- Unlimited MCP operator skill packs
- Research-program skills
- Generic “write anything” mega-skills

Optional profile skills may be added only with a named profile and justification (same closed-set discipline).

#### Rationale

Blueprint forbids unlimited catalogs. Skills must encode the decisions already locked (command surface, secrets, layout) so agents do not reinvent them.

#### Evidence

EVD-108; Blueprint non-goal unlimited catalogs; ecosystem REC-003/008/010/013; Exa definition-of-done + secrets.

#### Tradeoffs

Small skill set may need extension later vs kitchen-sink maintenance. A stricter minimal catalog (Grok deep-research skills/foundry run) puts **only** a secrets/fnox procedure skill in Core and leaves ruff/ty/pytest/pre-commit as always-on `AGENTS.md` facts—not micro-skills. This report still recommends a thin `quality-gates` skill because DoD is multi-step and agents under-run checks when only listed as prose; architecture may demote `quality-gates` to AGENTS.md-only if templates prove sufficient (revisit).

#### Failure Modes

Skill sprawl; skills that contradict AGENTS.md; one-line micro-skills that duplicate the command list.

#### Downstream Implications

Architecture maps skills into generate plan; synthesis → REQ skill IDs. Prefer **fewer** skills if agent compliance with AGENTS.md DoD is high.

#### Revisit Triggers

Repeated agent failure modes not covered by Core skills; owner DEC expanding catalog; evidence that AGENTS.md alone suffices for quality gates (demote `quality-gates`).

---

### REC-104 — MCP: default none; opt-in minimal only

- **Classification:** Default (none); Rejected (kitchen sink)
- **Applies to:** Generated Projects (foundry repo may use owner MCP without shipping defaults)
- **Confidence:** High
- **Decision urgency:** Required now
- **Evidence quality:** Strong
- **Related decisions:** Blueprint non-goal unlimited MCP

#### Recommendation

1. **Do not** commit a default MCP server catalog in Generated Projects.
2. Operators may add project MCP (e.g. Claude `.mcp.json`, Cursor `.cursor/mcp.json`) only when a concrete need exists.
3. If architecture later offers generator flags for MCP snippets, keep them **opt-in**, minimal (≤1–2 servers), secrets via env interpolation + fnox policy — never plaintext secrets in MCP config.
4. Document that each connected MCP server costs context and degrades tool selection when large.

#### Rationale

MCP is an optional integration standard, not a required app dependency. Claude and MCP client guidance emphasize context cost and progressive tool discovery. Personal CLI/scripts rarely need committed MCP at generation time.

#### Evidence

EVD-109..111; [MCP intro](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro); Claude MCP docs; Exa `mcp-curation`; Grok smoke research.

#### Alternatives Considered

Always-on filesystem MCP; always-on GitHub+Playwright (cloud-agent defaults — not templates for local personal CLIs).

#### Failure Modes

Kitchen-sink `.mcp.json`; secrets in MCP config; agents enabling 30+ tools.

#### Downstream Implications

Architecture: no Core MCP catalog requirement; optional profile only if justified later.

---

### REC-105 — LSP and diagnostics: Ruff + ty for editors; CLI for agent gates

- **Classification:** Required (CLI gates); Default (editor LSP)
- **Applies to:** Generated Projects + foundry dogfood
- **Confidence:** High (Astral surfaces); Medium (agent-default LSP marketplaces)
- **Decision urgency:** Required now
- **Evidence quality:** Strong
- **Related decisions:** Ecosystem REC-004, REC-005, REC-013; RSK-002

#### Recommendation

1. **Editors:** Document official Ruff editor integration (`ruff server` / Marketplace extension) and ty editor integration (`ty server` / official extension). Prefer Astral-native servers over deprecated `ruff-lsp`.
2. **Agents:** Treat **CLI** as the portable definition-of-done path: `uv run ruff check`, `uv run ruff format` / `format --check`, `uv run ty check`. Do not assume the agent’s default Python LSP is ty (Claude marketplace paths often emphasize Pyright).
3. Optional: where agents support custom LSP plugins, prefer Ruff+ty to match Core — but never drop CLI gates.
4. Document residual ty maturity risk (ecosystem RSK-002) so agents do not over-trust silence from ty.

#### Rationale

Core locks ty and ruff. Live diagnostics belong in LSP; verification and CI belong in CLI. Agent stock plugins may not match Core — CLI is the equalizer.

#### Evidence

EVD-112..114; [Ruff editors](https://docs.astral.sh/ruff/editors/); [ty](https://docs.astral.sh/ty/); Grok deep-research cmd-lsp-fnox; Exa `lsp-diagnostics`.

#### Failure Modes

Agents use only Pyright and ignore ty CI; dual conflicting type checkers as dual-default.

#### Downstream Implications

AGENTS.md + `quality-gates` skill; CI already requires ty per ecosystem.

---

### REC-106 — Agent command surface (amplify REC-013)

- **Classification:** Required
- **Applies to:** AGENTS.md, skills, templates
- **Confidence:** High
- **Decision urgency:** Required now
- **Evidence quality:** Strong
- **Related decisions:** Ecosystem REC-013

#### Recommendation

Document this **closed** surface (names stable):

```text
uv sync
uv run ruff check .
uv run ruff format .          # or: uv run ruff format --check   (CI/DoD)
uv run ty check
uv run pytest
uv run pre-commit run --all-files   # when pre-commit is configured
fnox exec -- uv run <entry>         # when secrets required
```

Optional thin `just`/`make` wrappers that **only** call the above. Do not document parallel competing workflows (poetry run, pip+venv primary, dotenv run).

#### Rationale

Official uv/ruff/ty/pytest/pre-commit/fnox entry points already exist; the agent need is naming a single closed set and sticking to it.

#### Evidence

EVD-115; ecosystem REC-013; Astral uv project docs; Grok cmd-lsp-fnox; Exa `command-surface-agents`.

#### Failure Modes

Five ways to run tests; docs that show `.env` “quick start.”

---

### REC-107 — Agent secrets protocol: fnox exec + age; forbid dotenv secrets

- **Classification:** Required
- **Applies to:** Generated Projects + foundry; skills and AGENTS.md
- **Confidence:** High (policy); Medium (fnox ecosystem maturity — ecosystem RSK-007)
- **Decision urgency:** Required now
- **Evidence quality:** Strong (fnox docs + accepted User decision)
- **Related decisions:** Ecosystem REC-008; RSK-050

#### Recommendation

1. Agents run secret-consuming work only via **`fnox exec -- <command>`** (typically `fnox exec -- uv run …`).
2. Committed **`fnox.toml`** holds encrypted secrets / structure; default provider **age** (ecosystem).
3. Age private keys and local overrides stay **out of git** (`FNOX_AGE_KEY` / `FNOX_AGE_KEY_FILE`, gitignored local files).
4. Skills and AGENTS.md **must forbid** teaching `.env` / python-dotenv / committed env files as secret storage.
5. Optional advanced: fnox MCP with tight tool allowlists is an Exception for agents that support it — not Required Core for all products.

#### Rationale

Owner User decision locks fnox+age and rejects dotenv secrets. Agent instructions are the main relapse surface for dotenv “convenience.”

#### Evidence

EVD-116..117; [fnox](https://fnox.jdx.dev/); fnox age provider docs; ecosystem REC-008; Grok cmd-lsp-fnox; Exa `secrets-agents-fnox`.

#### Failure Modes

Agents invent `.env`; commit age private keys; `fnox get` piped into shell history.

#### Downstream Implications

`secrets-fnox` skill; template gitignore; CI secret injection without dotenv files.

---

### REC-108 — Multi-agent strategy: portable-first + thin adapters

- **Classification:** Default
- **Applies to:** Generator emit policy
- **Confidence:** High
- **Decision urgency:** Required now
- **Evidence quality:** Strong
- **Related decisions:** REC-100, REC-102

#### Recommendation

1. **Portable layer:** `AGENTS.md` + `.agents/skills/` + command/secrets contracts.
2. **Thin adapters:** `CLAUDE.md`; Claude skills path adapter; optional Cursor rules only when globs/frontmatter required.
3. **Reject** unbounded per-product instruction and skill forks as the default generation mode.
4. Prefer nested AGENTS.md for monorepo packages over product-specific forks.

#### Rationale

Maximizes multi-agent coverage with minimal drift surface; matches official coexistence patterns.

#### Evidence

EVD-100..107; Exa `multi-agent-adapters`; Grok smoke research.

---

### REC-109 — Fresh-session / context packaging for Generated Projects

- **Classification:** Default
- **Applies to:** Generated Project docs layout
- **Confidence:** Medium
- **Decision urgency:** Required before implementation
- **Evidence quality:** Moderate (agent-ops practice + AGENTS.md convention)
- **Related decisions:** REC-100, REC-106

#### Recommendation

Generated Projects should be operable in a fresh agent session with:

1. `README.md` — human quickstart (short)
2. `AGENTS.md` — agent authority for conventions/commands/DoD
3. Skills under `.agents/skills/` for procedures
4. No dependence on uncommitted chat history

Optional `docs/` only when needed; avoid duplicate long prose in README and AGENTS.md (link or single source).

#### Rationale

Blueprint success criterion: agents extend projects without oral tradition.

#### Evidence

EVD-118; agents.md purpose statement; program fresh-session policy analogy.

---

### REC-110 — Definition of done for agent implementers

- **Classification:** Required
- **Applies to:** AGENTS.md + `quality-gates` skill
- **Confidence:** High (gates); Medium (exact “0 tests” policy edge cases)
- **Decision urgency:** Required now
- **Evidence quality:** Strong for tool exit codes; inferred for agent policy
- **Related decisions:** REC-106, ecosystem REC-006/012/013

#### Recommendation

An agent must not claim work complete until:

1. Documented lint/format checks pass (`ruff check`; format clean or `format --check` in CI-style DoD).
2. `ty check` passes (no masking with exit-zero flags in DoD).
3. `pytest` passes; for installable package/CLI archetypes, **reject “0 tests collected”** as success unless the change is docs-only and explicitly scoped.
4. When pre-commit is configured, `pre-commit run --all-files` is green (or equivalent CI parity).
5. Secrets-related changes do not introduce dotenv secret storage.

#### Rationale

Listed commands in AGENTS.md are expected to be run; CI parity requires local gates to match.

#### Evidence

EVD-119; pytest/ruff/ty exit semantics; Exa `definition-of-done`; Grok cmd-lsp-fnox; AGENTS.md convention.

---

### REC-111 — Anti-patterns (agent surface)

- **Classification:** Required (reject list)
- **Applies to:** Templates, skills, docs
- **Confidence:** High
- **Decision urgency:** Required now
- **Evidence quality:** Strong (composite)

#### Recommendation

| Anti-pattern | Why rejected |
| ------------ | ------------ |
| Unlimited skill/MCP catalogs | Blueprint non-goal; context cost |
| Dual full instruction bodies (AGENTS.md ≈ CLAUDE.md copy) | Drift |
| Dotenv/`.env` secret quick starts | Ecosystem REC-008 |
| Documenting five equivalent command ecosystems | Decision fatigue |
| Windows-only agent paths | L3 |
| Silent demotion of ty or fnox in agent docs | Core locks |
| Kitchen-sink MCP at generate time | Context + scope |
| Oral-tradition-only conventions | Program failure mode |

---

### REC-112 — Editor recommendation note (non-blocking)

- **Classification:** Default
- **Applies to:** Docs only
- **Confidence:** Medium
- **Decision urgency:** May defer
- **Evidence quality:** Moderate

#### Recommendation

Document VS Code/Cursor-class setup with official Ruff + ty extensions as the supported editor path on macOS/Linux. Do not require a specific IDE for Generated Projects. Neovim users may use `ruff server` / `ty server` per Astral docs.

#### Evidence

EVD-112..113; Astral editor docs.

## 10. Evidence Ledger

| ID | Claim | Class | Sources | Confidence |
| -- | ----- | ----- | ------- | ---------- |
| EVD-100 | AGENTS.md is a portable multi-agent instruction format | Official claim / verified | https://agents.md/ | High |
| EVD-101 | Claude Code reads CLAUDE.md; coexists via `@AGENTS.md` or symlink | Official claim | https://code.claude.com/docs/en/memory | High |
| EVD-102 | Grok Build reads AGENTS.md family + CLAUDE.md + rules dirs; deeper wins | Official claim | https://docs.x.ai/build/features/project-rules | High |
| EVD-103 | Cursor supports AGENTS.md as simple alternative to project rules | Official claim | https://cursor.com/docs/rules | High |
| EVD-104 | Foundry vs Generated Project surfaces should differ | Judgment | Blueprint + program practice | High |
| EVD-105 | Agent Skills SKILL.md requires name+description frontmatter | Official claim | https://agentskills.io/specification | High |
| EVD-106 | Claude project skills load from `.claude/skills/` | Official claim | https://code.claude.com/docs/en/skills | High |
| EVD-107 | Multi-product clients often also scan `.agents/skills` | Official claim / inference | Exa skills-layout; Cursor/Codex docs via Exa | Medium–High |
| EVD-108 | Closed skill catalog is required by Blueprint non-goals | User decision / Blueprint | Blueprint §6 non-goal 6 | High |
| EVD-109 | MCP is optional connector standard, not mandatory project core | Official claim | MCP getting started | High |
| EVD-110 | Large MCP tool sets cost context and hurt selection | Official claim | Claude MCP / MCP client best practices (Exa) | High |
| EVD-111 | Default MCP none is appropriate for personal CLI generators | Judgment | EVD-109..110 + personal scope | High |
| EVD-112 | Ruff provides `ruff server` LSP; prefer over ruff-lsp | Official claim | https://docs.astral.sh/ruff/editors/ | High |
| EVD-113 | ty provides type checking + language server | Official claim | https://docs.astral.sh/ty/ | High |
| EVD-114 | Agent default Python LSP may be Pyright, not ty | Official claim / inference | Grok deep-research citing Claude plugins | Medium |
| EVD-115 | uv run is the project-scoped command entry | Official claim | https://docs.astral.sh/uv/guides/projects/ | High |
| EVD-116 | fnox exec injects secrets into child process env | Official claim | https://fnox.jdx.dev/ | High |
| EVD-117 | Ecosystem locks fnox+age and rejects dotenv secrets | User decision | docs/reports/01-modern-python-ecosystem.md REC-008 | High |
| EVD-118 | Fresh sessions need attachable repo artifacts, not chat | Program rule | AGENTS.md program; agents.md purpose | High |
| EVD-119 | Quality gates must be runnable and exit non-zero on failure | Official claim | ruff/ty/pytest docs | High |
| EVD-120 | Exa multi-query + Grok deep-research agree on AGENTS.md+CLAUDE.md+MCP none | Experiment | scripts/exa-output/ai-native-* ; smoke + cmd-lsp-fnox reports | High |

## 11. Recommendation Ledger

| REC | Title | Classification |
| --- | ----- | -------------- |
| REC-100 | AGENTS.md + CLAUDE.md adapter | Required |
| REC-101 | Foundry vs Generated Project agent surfaces | Required |
| REC-102 | `.agents/skills/` canonical layout | Default/Required path |
| REC-103 | Closed Core skill catalog | Required |
| REC-104 | MCP default none | Default; kitchen sink Rejected |
| REC-105 | Ruff+ty LSP editors; CLI agent gates | Required/Default |
| REC-106 | Closed command surface (REC-013 amplify) | Required |
| REC-107 | fnox exec secrets protocol | Required |
| REC-108 | Portable-first multi-agent strategy | Default |
| REC-109 | Fresh-session packaging | Default |
| REC-110 | Definition of done | Required |
| REC-111 | Anti-patterns reject list | Required |
| REC-112 | Editor setup note | Default |

## 12. Risks

### RSK-050 — Agents reintroduce dotenv secrets despite docs

- **Severity:** High
- **Likelihood:** Medium
- **Related:** REC-107, ecosystem RSK-007
- **Mitigation:** `secrets-fnox` skill; AGENTS.md forbid list; templates without `.env.example` secrets patterns; validation checks in architecture later

### RSK-051 — Instruction file conflict / drift (AGENTS.md vs CLAUDE.md)

- **Severity:** Medium
- **Likelihood:** Medium
- **Mitigation:** Thin adapter only (`@AGENTS.md` / symlink); no dual prose

### RSK-052 — Claude misses portable skills if only `.agents/skills` emitted

- **Severity:** Medium
- **Likelihood:** Medium–High until OQ-051 closed
- **Mitigation:** Claude path adapter (REC-102); SPK-051

### RSK-053 — MCP kitchen-sink creep via “helpful” generator defaults

- **Severity:** Medium
- **Likelihood:** Medium
- **Mitigation:** REC-104; architecture admission control for any MCP profile

### RSK-054 — Agent uses Pyright path and ignores ty Core

- **Severity:** Medium
- **Likelihood:** Medium
- **Mitigation:** CLI DoD + CI ty; skills name `ty check`; no dual-default typechecker docs

### RSK-055 — Skill catalog sprawl after v1

- **Severity:** Medium
- **Likelihood:** High over time
- **Mitigation:** REC-103 closed set; profile admission; DEC for expansions

### RSK-056 — Multi-product precedence ambiguities (AGENTS.md vs rules)

- **Severity:** Low–Medium
- **Likelihood:** Medium
- **Mitigation:** Prefer single AGENTS.md; minimize simultaneous rule systems; OQ-052

## 13. Weak Evidence

- Exact Cursor merge precedence when both AGENTS.md and `.cursor/rules` apply simultaneously.
- Whether Claude Code auto-discovers `.agents/skills` (not established in inspected primary skills page).
- Optimal Core skill *bodies* (only purposes recommended here).
- Whether `env = "exec"` top-level fnox setting is available/stable in all fnox versions agents will pin (Exa cited PR/docs; verify at implementation).

## 14. Conflicting Evidence

- Stock agent Python LSP ecosystems (often Pyright) vs Core **ty** — resolved by CLI gates + editor recommendation, not by changing Core.
- Some community guides still teach dotenv for agents — **rejected** by accepted ecosystem User decision; treat as anti-pattern, not open debate.
- Cloud-agent default MCP sets (e.g. GitHub+Playwright) vs local personal CLI generators — not applicable as defaults here.
- **Skill catalog size:** Grok deep-research (skills/foundry) argues Core skills should be **secrets-only**, with quality gates always-on in `AGENTS.md` only; this report recommends a thin `quality-gates` skill plus archetype skills (REC-103). Not a contradiction on layout—both reject kitchen sinks. Architecture may choose the stricter minimal set if DoD prose proves sufficient.

## 15. Assumptions

- ASM-050: Owner continues multi-agent use (at least Grok + Claude Code class tools).
- ASM-051: Ecosystem Core locks remain accepted through architecture/synthesis.
- ASM-052: macOS/Linux only remains true (symlinks acceptable).
- ASM-053: Generator can emit small static file sets and skill skeletons.

## 16. Open Questions

### OQ-050 — Exact CLAUDE.md emit form: `@AGENTS.md` vs symlink default?

- **Blocking?** No (both acceptable per Claude docs)
- **Resolution path:** Architecture template choice; prefer `@AGENTS.md` if any Claude-only notes expected
- **Deadline:** Implementation plan

### OQ-051 — Does Claude Code natively load `.agents/skills`?

- **Blocking?** For single-path emit purity — yes for “no adapter”
- **Resolution path:** SPK-051 / official docs re-check at implementation
- **Deadline:** Before generator skill emit finalization

### OQ-052 — Cursor precedence when AGENTS.md and `.cursor/rules` both present

- **Blocking?** No if we avoid dual systems by default
- **Resolution path:** Product docs / spike
- **Deadline:** If Cursor rules profile is added

### OQ-053 — Should any MCP server ever be a named Core profile (e.g. `mcp-docs`)?

- **Blocking?** No
- **Resolution path:** Architecture only if concrete foundry need appears
- **Deadline:** Profile admission

### OQ-054 — Foundry product CLI agent skills catalog (beyond research skills)

- **Blocking?** For foundry implementation phases — partially
- **Resolution path:** Architecture track after this report
- **Deadline:** Architecture report

### OQ-055 — Enforce “≥1 test collected” mechanically in templates?

- **Blocking?** No
- **Resolution path:** Architecture/pytest config / CI policy
- **Deadline:** Implementation

## 17. Handoff Digest

### Decisions supported

- Portable-first agent surface: AGENTS.md + thin CLAUDE.md
- Canonical skills under `.agents/skills` with Claude adapter residual
- Closed Core skill purposes for Generated Projects
- MCP default none
- Ruff+ty diagnostics: LSP for editors, CLI for agent DoD
- Amplify REC-013 command surface; fnox exec secrets; forbid dotenv secrets
- Distinct foundry vs Generated Project agent packaging

### Recommendations accepted by this report

REC-100..REC-112 as written.

### Recommendations challenged

- Dual full product skill trees as default — **rejected**
- Default committed MCP catalog — **rejected**
- AGENTS.md-only without Claude adapter — **rejected** for multi-agent Core

### Evidence strength summary

Strong on instruction coexistence, skills format, Astral diagnostics, fnox exec, MCP opt-in; medium on exact Core skill roster composition and Claude `.agents/skills` discovery.

### Weak and conflicting evidence

See §13–§14.

### Assumptions

See §15.

### Risks

RSK-050..056.

### Open questions

OQ-050..055.

### Required downstream decisions

| Consumer | Needs |
| -------- | ----- |
| Architecture | Emit file set; skill skeletons; Claude adapter mechanism; no default MCP; command/DoD in templates |
| Synthesis | Trace REC-100..112 → REQs; keep ecosystem RECs linked |
| Owner | Confirm Claude adapter default (OQ-050); skill catalog size (REC-103) |

### Relevant identifiers

REC-100..112; RSK-050..056; OQ-050..055; SPK-050..052 (planned); EVD-100..120; inherits ecosystem REC-001..014, RSK-002, RSK-007.

### Full-report sections that must be read before deciding

§2 Executive Answer; §9 REC-100..107, REC-110; §12 Risks; §16 OQs.

## 18. Source Ledger

| Title | URL | Publisher | Access date | Used for |
| ----- | --- | --------- | ----------- | -------- |
| AGENTS.md | https://agents.md/ | agents.md / AAIF | 2026-07-31 | REC-100, REC-109 |
| How Claude remembers your project | https://code.claude.com/docs/en/memory | Anthropic | 2026-07-31 | REC-100 |
| Extend Claude with skills | https://code.claude.com/docs/en/skills | Anthropic | 2026-07-31 | REC-102, OQ-051 |
| Connect Claude Code to tools via MCP | https://code.claude.com/docs/en/mcp | Anthropic | 2026-07-31 | REC-104 |
| AGENTS.md / project rules (Grok Build) | https://docs.x.ai/build/features/project-rules | xAI | 2026-07-31 | REC-100, REC-108 |
| Agent Skills Specification | https://agentskills.io/specification | agentskills | 2026-07-31 | REC-102 |
| Cursor Rules | https://cursor.com/docs/rules | Cursor | 2026-07-31 | REC-100 |
| Ruff Editor Integration | https://docs.astral.sh/ruff/editors/ | Astral | 2026-07-31 | REC-105 |
| ty | https://docs.astral.sh/ty/ | Astral | 2026-07-31 | REC-105 |
| uv projects guide | https://docs.astral.sh/uv/guides/projects/ | Astral | 2026-07-31 | REC-106 |
| fnox | https://fnox.jdx.dev/ | jdx | 2026-07-31 | REC-107 |
| MCP getting started | https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro | MCP | 2026-07-31 | REC-104 |
| Modern Python ecosystem report v0.2 | `docs/reports/01-modern-python-ecosystem.md` | program | 2026-07-31 | Inherited Core locks |
| Exa AI-native evidence INDEX | `scripts/exa-output/ai-native-20260731T231539Z/INDEX.md` | local | 2026-07-31 | EVD-120 (non-portable raw) |
| Grok deep-research smoke | session workflow scratch / `scripts/exa-output/.../grok/smoke.md` | local | 2026-07-31 | EVD-120 |
| Grok deep-research cmd/LSP/fnox | `scripts/exa-output/.../grok/cmd-lsp-fnox.md` | local | 2026-07-31 | REC-105..107 |
| Grok deep-research skills/foundry | `scripts/exa-output/.../grok/skills-foundry.md` | local | 2026-07-31 | REC-101..103; §14 catalog tension |

## 19. Completion Checklist

- [x] All required report sections present
- [x] Actual research date recorded (2026-07-31)
- [x] Primary and subsidiary questions answered or OQ’d
- [x] REC-100..112 in range REC-100..199
- [x] RSK/OQ/SPK within assigned ranges (050+); no reuse of ecosystem IDs for new subjects
- [x] Inherited ecosystem Core locks respected (ty, fnox+age, no dotenv secrets, REC-013)
- [x] Evidence Ledger for load-bearing claims
- [x] Source ledger with URLs and access dates
- [x] Required tables present (§2, §8, REC-103, REC-111)
- [x] Credible alternatives compared for major decision areas
- [x] Handoff Digest complete
- [x] Allowed file scope respected (report + local evidence scripts/dumps only)
- [x] No downstream stages started

## 20. Required Tables (consolidated)

### Agent instruction surface

| File | Audience | Membership | Purpose |
| ---- | -------- | ---------- | ------- |
| `AGENTS.md` | All agents | Required | Portable conventions, commands, DoD, secrets |
| `CLAUDE.md` | Claude Code | Required adapter | `@AGENTS.md` or symlink |
| `.cursor/rules/*.mdc` | Cursor | Optional | Glob/frontmatter rules |
| `.grok/rules/` | Grok | Optional | Only if portable layer insufficient |
| `.claude/rules/` | Claude | Optional | Path-specific Claude rules |

### Core skill catalog

See REC-103.

### MCP catalog

| Server set | Status |
| ---------- | ------ |
| Default committed servers | **None** (Rejected kitchen sink) |
| Opt-in project MCP | Optional Exception |
| Foundry-owner research MCP | Allowed in foundry repo only |

### LSP / diagnostics map

| Tool | Editor path | Agent DoD path | Core? |
| ---- | ----------- | -------------- | ----- |
| Ruff | `ruff server` / extension | `uv run ruff check/format` | Yes |
| ty | `ty server` / extension | `uv run ty check` | Yes |
| Pyright | Escape hatch only | Not Default | Exception only |

### Command surface for agents

See REC-106 (inherits REC-013).

### Foundry vs Generated Project

See REC-101.

### Anti-patterns

See REC-111.
