# HANDOFF — python-foundry research program

**Purpose:** Self-contained context so a **fresh agent session** can resume
without chat history. Git-tracked artifacts remain authority; this file is a
resume aid, not a substitute for the Blueprint, Charter, or accepted reports.

| Field | Value |
| ----- | ----- |
| **As of** | 2026-08-01 |
| **Repo** | https://github.com/robertguss/python-foundry |
| **Branch** | `main` |
| **HEAD (at handoff)** | verify with `git log -1 --oneline` |
| **Program status** | `active` |
| **Rigor** | `standard` |
| **Owner** | robertguss |
| **Next stage** | `synthesis` — **planned** (architecture accepted; package JIT prompt next) |

**Verify on resume:** `git log -1 --oneline` and `research-program.toml`.

---

## 1. What this program is

**python-foundry** is a **research program repository** (not the product codebase)
to design a personal, open-sourceable, **AI-native hybrid Python foundry**:

1. A **Python/`uv` CLI generator** (validate → plan dry-run → generate)
2. A **strong default Core** for Generated Projects
3. Optional **capability profiles**
4. Usable also as a **GitHub template** surface
5. **Agent-first** layout/docs/skills/MCP/LSP — standards **`AGENTS.md`** + **`.agents/`** (Grok, Cursor, Codex, similar; **not** Claude Code as a design target)

**Stops at:** accepted revised definitive specification + revised implementation
plan as **phases and milestones** — not a granular coding backlog.

**Prior art (transferable, not governing):**

- https://github.com/robertguss/go-foundry-research
- https://github.com/robertguss/go-foundry-cli

This research methodology was abstracted from the go-foundry research process.

---

## 2. Operating rules (do not skip)

1. **Git artifacts are authority** — not chat, not this handoff alone if they conflict.
2. Precedence: accepted `DEC-###` → Blueprint → Charter → stage prompt → revised
   spec → research reports → reviews → plans → `research-program.toml` (index).
3. **Fresh session per substantive stage** (research, synthesis, review, revision).
   Preparing JIT packages / mechanical fixes is OK in a packaging session.
4. **Human approval gates** before acceptance; humans own git commits (agents may
   commit when the human explicitly asks).
5. Placeholders never unlock work. Validation before acceptance.
6. Skills: `.agents/skills/` — `research-program`, `research-stage`, `research-validate`.
7. Commands: `just status`, `just check` (no git).

Read: `AGENTS.md`, `README.md`, `program/operator/resume-protocol.md`.

---

## 3. Program graph and status

```text
discovery ✅
    ↓
charter ✅
    ↓
    ├── research-python-ecosystem ✅  (G1)  ← DONE
    └── research-ai-native        ✅  (G1)  ← DONE
              ↓
    research-foundry-architecture ✅  (accepted)  ← DONE
              ↓
    synthesis ⬜  ← NEXT (package then fresh session)
              ↓
    spec-review → spec-revision
              ↓
    implementation-plan → plan-review → plan-revision
```

| Stage ID | Status | Output / notes |
| -------- | ------ | -------------- |
| `discovery` | **accepted** | `docs/00-program-blueprint.md` — commit `14019e8…` |
| `charter` | **accepted** | `docs/01-research-charter.md` — commit `16ec8a9…` |
| `research-python-ecosystem` | **accepted** | `docs/reports/01-modern-python-ecosystem.md` v0.2 — accepting commit `1435c65…` |
| `research-ai-native` | **accepted** | `docs/reports/02-ai-native-agent-workflow.md` v0.2 — content commit `7741755…` |
| `research-foundry-architecture` | **accepted** | `docs/reports/03-foundry-architecture.md` v0.1.1 — see `accepted_commit` in manifest |
| `synthesis` | **planned** | `docs/specifications/01-definitive-specification.md` — prompt not installed yet |
| Spine (spec-review…plan-revision) | **planned** | Skeleton prompts under `docs/prompts/NN-*.md` |

Manifest: `research-program.toml`.

---

## 4. Product framing (locked in Blueprint)

### Problem

Repeated Python project setup; inconsistent bases; agents need oral tradition.

### Users

Primary: owner. Implementers: AI coding agents. Open-source OK; not multi-tenant.

### Non-goals (v1)

Marketplace; framework zoo; notebooks/GUI/mobile; **Windows ever**; public-first
design; unlimited MCP/skill catalog; new package manager; coding backlog as
program output.

### Success

Fast empty→runnable path; agent-operable repos; consistent Core; reduced decision
fatigue; accepted revised spec + phase/milestone plan.

---

## 5. Accepted ecosystem Core (report v0.2) — load-bearing

Full detail: `docs/reports/01-modern-python-ecosystem.md`  
Validation: `docs/validations/01-modern-python-ecosystem-validation.md` (**Pass**)

### Core (Generated Projects)

| Layer | Decision |
| ----- | -------- |
| Python | Floor **3.12**, default pin **3.13** |
| Project tool | **uv** + committed `uv.lock` |
| Layout | **src/** packages; scripts via **PEP 723** + `uv run` |
| Lint/format | **Ruff** (check + format) |
| Types | **ty** Required Core (**User decision**; residual maturity risk RSK-002) |
| Tests | **pytest** Required; pytest-cov Default |
| Hooks | **pre-commit** Default; **hk** optional profile only |
| Secrets | **fnox** Required Core; provider **`age`**; **no `.env` / dotenv secrets** |
| CI | GitHub Actions + setup-uv + ruff + ty + pytest (Linux required; macOS optional) |
| CLI framework | **Typer** Default for CLI archetype |
| Commands | `uv sync` / `uv run …` / `fnox exec -- …` |

### Profiles (opt-in)

| Profile | Contents |
| ------- | -------- |
| `http` | **httpx** (sync default) |
| `hooks-hk` | **hk** |
| `data-etl` | polars + pyarrow default; extras duckdb, pandas |

### RECs / risks / OQs (ecosystem)

- **REC-001..014** allocated (001–099 range)
- **RSK-001..007** (notably RSK-002 ty maturity, RSK-007 fnox/no-dotenv)
- **OQ-001..006** — **OQ-006 resolved** (fnox provider = age)
- **SPK-001..003** planned; **SPK-002 recommended** (ty smoke) before heavy implementation
- Research initially demoted ty/fnox; **owner overrode** to Core — recorded as User decisions EVD-016/017

### Do not silently undo

- Do not reintroduce **dotenv/`.env` secret storage** without a DEC
- Do not demote **ty** or **fnox** from Core without a DEC
- Do not add **Windows** support

---

## 6. Immediate next work

### Next stage: `synthesis` — Definitive Specification Synthesis

**Kind:** chief-architect-synthesis  
**Depends on:** all three research tracks (**all accepted**)  
**Output:** `docs/specifications/01-definitive-specification.md`  
**IDs:** REQ-001..299  
**Prompt path (skeleton):** `docs/prompts/NN-chief-architect-synthesis-prompt.md` → install as reserved numbered path via **research-stage**

### How to commission (packaging session)

1. Load **research-stage** skill
2. Produce JIT package for `synthesis` only (prompt, manifest, launch, validation; status → `prompt-ready`)
3. Run substantive synthesis in a **fresh** session
4. Do not mark accepted without human approval

### Inputs synthesis should attach

- Accepted Blueprint + Charter
- Accepted ecosystem report v0.2 **in full**
- Accepted AI-native report v0.2 **in full**
- Accepted architecture report v0.1.1 **in full**
- Commissioning prompt once written
- Contracts for synthesis / requirements

### Accepted architecture locks (load-bearing — do not silently undo)

Full detail: `docs/reports/03-foundry-architecture.md` v0.1.1  
Validation: `docs/validations/03-foundry-architecture-validation.md` (**Pass with mechanical corrections**)

| Layer | Decision |
| ----- | -------- |
| CLI | `validate` → `plan` → `generate` + catalog list/show + version |
| Spec | TOML `schema = 1` |
| Plan | Plan-as-contract (pure Construct shared by validate/plan/generate) |
| Writes | Sibling stage → verify → exclusive place; fail if dest non-empty |
| Catalog | Closed core + archetypes `cli\|scripts\|data-etl` + profiles `http\|hooks-hk\|data-etl` |
| Engine | Custom planner-led (not Copier-as-runtime) |
| Emit | Core toolchain + AGENTS.md + `.agents/skills` only; no Claude; MCP none; no dotenv secrets |
| Template surface | Catalog SoT; GitHub template = CI-generated snapshot |
| Verify | Tiered default/strict/none (default: uv sync + ruff + ty) |

Owner preference: **one stage at a time**.

---

## 7. Exa Deep evidence tooling (optional for next tracks)

Not MCP — use REST + `EXA_API_KEY` (stdlib scripts):

| Script | Role |
| ------ | ---- |
| `scripts/exa_deep_smoke.py` | Single Deep / deep-reasoning smoke test |
| `scripts/exa_ecosystem_evidence.py` | Multi-query runner for ecosystem decision areas |
| `scripts/exa_ai_native_evidence.py` | Multi-query runner for AI-native decision areas |
| `scripts/exa_architecture_evidence.py` | Multi-query runner for architecture decision areas |

```bash
export EXA_API_KEY=...
python3 scripts/exa_deep_smoke.py --type deep-reasoning
python3 scripts/exa_ecosystem_evidence.py --type deep-reasoning
python3 scripts/exa_ecosystem_evidence.py --list
```

- Prefer **`deep-reasoning`** for load-bearing decisions.
- Raw dumps under `scripts/exa-output/` (gitignored).
- Exa output is **evidence**, not the report — still write REC-format reports.
- Docs: https://exa.ai/blog/exa-deep , https://exa.ai/docs/reference/search-api-guide

Exa runs (reference, local only):  
`scripts/exa-output/ecosystem-20260731T170320Z/INDEX.md`  
`scripts/exa-output/ai-native-20260731T231539Z/INDEX.md`  
`scripts/exa-output/architecture-20260801T000131Z/INDEX.md`

---

## 8. Key file map

| Path | Role |
| ---- | ---- |
| `AGENTS.md` | Agent operating rules |
| `research-program.toml` | Stage status index |
| `docs/00-program-blueprint.md` | Accepted Blueprint |
| `docs/01-research-charter.md` | Accepted Charter |
| `docs/prompts/01-modern-python-ecosystem-prompt.md` | Ecosystem commissioning prompt |
| `docs/prompts/02-ai-native-agent-workflow-prompt.md` | AI-native commissioning prompt |
| `docs/prompts/03-foundry-architecture-prompt.md` | Architecture commissioning prompt |
| `docs/reports/01-modern-python-ecosystem.md` | **Accepted** ecosystem report |
| `docs/reports/02-ai-native-agent-workflow.md` | **Accepted** AI-native report v0.2 |
| `docs/reports/03-foundry-architecture.md` | **Accepted** architecture report v0.1.1 |
| `docs/validations/01-modern-python-ecosystem-validation.md` | Ecosystem validation Pass |
| `docs/validations/02-ai-native-agent-workflow-validation.md` | AI-native validation Pass (v0.2 re-validation) |
| `docs/validations/03-foundry-architecture-validation.md` | Architecture validation Pass w/ mechanical corrections |
| `docs/handoffs/research-python-ecosystem-*.md` | Ecosystem stage package |
| `docs/handoffs/research-ai-native-*.md` | AI-native stage package |
| `docs/handoffs/research-foundry-architecture-*.md` | Architecture stage package |
| `program/` | Methodology library (contracts, templates, reference) |
| `.agents/skills/` | research-program / research-stage / research-validate |
| `decisions/` | DEC-### (empty of DECs so far — only README) |

---

## 9. Identifier ranges (remaining)

| Track | REC range |
| ----- | --------- |
| Ecosystem (done) | REC-001..099 (used 001–014) |
| AI-native (done) | REC-100..199 (used 100–112) |
| Architecture (done) | REC-200..299 (used 200–212) |
| Synthesis REQs | REQ-001..299 |
| Spec REQs | REQ-001..299 |
| Spec findings | FND-001..199 |
| Plan findings | FND-200..399 |
| RSK / OQ / SPK | shared 001..999 (ecosystem 001–007 / 001–006; AI-native RSK-050..056, OQ-050..055) |

Never reuse IDs.

---

## 10. Suggested first message in a fresh session (next: synthesis packaging)

```text
Resume python-foundry from HANDOFF.md and Git artifacts.

Next stage: synthesis only (one at a time). Architecture is accepted.

1. Read AGENTS.md, HANDOFF.md, research-program.toml, Blueprint, Charter, and
   accepted reports 01, 02, and 03 (architecture v0.1.1).
2. Use research-stage skill to produce the JIT package for synthesis
   (prompt, attachment manifest, launch message, validation task;
   status → prompt-ready).
3. Do not run substantive synthesis until I start a fresh research session
   (or I explicitly ask you to).
4. Do not mark stages accepted without my approval.
```

Inherit locks: ecosystem Core; AI-native AGENTS.md + `.agents/`; architecture
planner-led validate/plan/generate (REC-200..212).

---

## 11. Anti-patterns to avoid on resume

- Treating this HANDOFF as higher authority than accepted Blueprint/Charter/reports
- Starting synthesis before architecture is accepted
- Reopening Windows / notebooks / framework zoo
- Reintroducing `.env` secrets “for simplicity”
- Reintroducing Claude Code adapters (`CLAUDE.md`, `.claude/`) without a DEC
- Inventing acceptance without human + commit hash in manifest
- Multiple substantive stages in one context without human override

---

## 12. Recent git history (context)

```text
(verify) docs: accept foundry architecture research report
(verify) docs: add foundry architecture research report
(verify) docs: add foundry architecture research prompt
cbf2de8 docs: accept AI-native agent workflow research report
7741755 docs: drop Claude Code from AI-native agent surface
… earlier G1 + charter + blueprint
```

---

## 13. Accepted AI-native locks (load-bearing)

Full detail: `docs/reports/02-ai-native-agent-workflow.md` v0.2  
Validation: `docs/validations/02-ai-native-agent-workflow-validation.md` (**Pass**)

| Layer | Decision |
| ----- | -------- |
| Instructions | Root **`AGENTS.md` only** — no `CLAUDE.md` / `.claude/` Core emit |
| Skills | **`.agents/skills/<name>/SKILL.md` only** |
| MCP | Default **none**; kitchen sink rejected |
| Diagnostics | Ruff + ty LSP (editors); CLI gates for agent DoD |
| Commands | Amplify REC-013 (`uv run` + `fnox exec`) |
| Secrets | `fnox exec` + age; forbid dotenv secrets in agent docs/skills |
| Targets | Grok / Cursor / Codex / similar — **not** Claude Code as design target |

---

## 14. Accepted architecture locks (load-bearing)

Full detail: `docs/reports/03-foundry-architecture.md` v0.1.1  
Validation: `docs/validations/03-foundry-architecture-validation.md` (**Pass with mechanical corrections**)

See §6 table (CLI, TOML spec, plan-as-contract, stage+place, closed catalog,
custom engine, emit invariants, template snapshot, verify tiers). REC-200..212.

---

*End of handoff. Update or replace this file when the next stage is accepted.*
