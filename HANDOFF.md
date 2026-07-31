# HANDOFF — python-foundry research program

**Purpose:** Self-contained context so a **fresh agent session** can resume
without chat history. Git-tracked artifacts remain authority; this file is a
resume aid, not a substitute for the Blueprint, Charter, or accepted reports.

| Field | Value |
| ----- | ----- |
| **As of** | 2026-07-31 |
| **Repo** | https://github.com/robertguss/python-foundry |
| **Branch** | `main` |
| **HEAD (at handoff)** | verify with `git log -1 --oneline` (packaging may be uncommitted) |
| **Program status** | `active` |
| **Rigor** | `standard` |
| **Owner** | robertguss |
| **Next stage** | `research-ai-native` — **prompt-ready** (package installed; research not started) |

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
    └── research-ai-native        📦  (G1)  ← prompt-ready; research not started
              ↓
    research-foundry-architecture ⬜  (needs both G1)
              ↓
    synthesis → spec-review → spec-revision
              ↓
    implementation-plan → plan-review → plan-revision
```

| Stage ID | Status | Output / notes |
| -------- | ------ | -------------- |
| `discovery` | **accepted** | `docs/00-program-blueprint.md` — commit `14019e8…` |
| `charter` | **accepted** | `docs/01-research-charter.md` — commit `16ec8a9…` |
| `research-python-ecosystem` | **accepted** | `docs/reports/01-modern-python-ecosystem.md` v0.2 — accepting commit `1435c65…` |
| `research-ai-native` | **prompt-ready** | Prompt + handoff package installed; report not written |
| `research-foundry-architecture` | **planned** | Blocked on both G1 reports accepted |
| Spine (synthesis…plan-revision) | **planned** | Skeleton prompts under `docs/prompts/NN-*.md` |

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

### Next stage: `research-ai-native` — package ready

**Name:** AI-Native Repository & Agent Workflow  
**Kind:** independent focused research (G1 — ecosystem already accepted; inherit Core locks)  
**Primary question (Blueprint):** How should the foundry and generated projects be
structured, documented, and instrumented so AI coding agents work optimally
(skills, MCP, LSP, instructions, checks)?  
**IDs:** REC-100..199; RSK-050..099; OQ-050..099; SPK-050..099  
**Output:** `docs/reports/02-ai-native-agent-workflow.md`  
**Prompt (installed):** `docs/prompts/02-ai-native-agent-workflow-prompt.md`  
**Package:**

| Item | Path |
| ---- | ---- |
| Attachment manifest | `docs/handoffs/research-ai-native-attachment-manifest.md` |
| Launch message | `docs/handoffs/research-ai-native-launch-message.md` |
| Validation task | `docs/handoffs/research-ai-native-validation-task.md` |

### How to run the research (fresh session)

1. Open a **new** agent session (do not continue packaging chat for substantive work).
2. Attach files listed in the attachment manifest (Blueprint, Charter, prompt,
   **full** ecosystem report, AGENTS.md, contracts/templates, manifest).
3. Paste the body of `docs/handoffs/research-ai-native-launch-message.md` (below the line).
4. Research session writes report → **research-validate** → human accept → commit.
5. Do **not** mark `accepted` without human approval and commit hash in the manifest.

### Inputs (already listed in attachment manifest)

- Accepted Blueprint + Charter
- Accepted ecosystem report **in full** (Core tools, command surface, ty, fnox+age,
  forbid dotenv secrets)
- Commissioning prompt
- `AGENTS.md`, contracts for focused research + recommendations

### After both G1 reports are accepted

Package and run **`research-foundry-architecture`** (depends on ecosystem + AI-native),
then the fixed spine (synthesis → reviews → revised spec → plan).

Owner preference: **one stage at a time** (no parallel G1 execution going forward
unless they change that).

---

## 7. Exa Deep evidence tooling (optional for next tracks)

Not MCP — use REST + `EXA_API_KEY` (stdlib scripts):

| Script | Role |
| ------ | ---- |
| `scripts/exa_deep_smoke.py` | Single Deep / deep-reasoning smoke test |
| `scripts/exa_ecosystem_evidence.py` | Multi-query runner for ecosystem decision areas |

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

Ecosystem Exa run (reference, local only):  
`scripts/exa-output/ecosystem-20260731T170320Z/INDEX.md`

---

## 8. Key file map

| Path | Role |
| ---- | ---- |
| `AGENTS.md` | Agent operating rules |
| `research-program.toml` | Stage status index |
| `docs/00-program-blueprint.md` | Accepted Blueprint |
| `docs/01-research-charter.md` | Accepted Charter |
| `docs/prompts/01-modern-python-ecosystem-prompt.md` | Ecosystem commissioning prompt |
| `docs/prompts/02-ai-native-agent-workflow-prompt.md` | **Installed** AI-native commissioning prompt |
| `docs/reports/01-modern-python-ecosystem.md` | **Accepted** ecosystem report |
| `docs/reports/02-ai-native-agent-workflow.md` | AI-native report (**not written yet**) |
| `docs/validations/01-modern-python-ecosystem-validation.md` | Validation Pass (re-validation) |
| `docs/handoffs/research-python-ecosystem-*.md` | Ecosystem stage package |
| `docs/handoffs/research-ai-native-*.md` | AI-native stage package (launch/manifest/validation) |
| `program/` | Methodology library (contracts, templates, reference) |
| `.agents/skills/` | research-program / research-stage / research-validate |
| `decisions/` | DEC-### (empty of DECs so far — only README) |

---

## 9. Identifier ranges (remaining)

| Track | REC range |
| ----- | --------- |
| Ecosystem (done) | REC-001..099 (used 001–014) |
| AI-native (next) | REC-100..199 |
| Architecture | REC-200..299 |
| Spec REQs | REQ-001..299 |
| Spec findings | FND-001..199 |
| Plan findings | FND-200..399 |
| RSK / OQ / SPK | shared 001..999 (ecosystem used RSK-001..007, OQ-001..006, SPK-001..003 planned) |

Never reuse IDs.

---

## 10. Suggested first message in a fresh research session

Packaging for `research-ai-native` is done. For the **research** session:

```text
Execute research-ai-native for python-foundry.

Use the package already in the repo:
- docs/handoffs/research-ai-native-launch-message.md (paste launch body)
- docs/handoffs/research-ai-native-attachment-manifest.md
- docs/prompts/02-ai-native-agent-workflow-prompt.md

Attach: Blueprint, Charter, ecosystem report v0.2 (full), AGENTS.md, report
contracts/templates, and the attachment manifest.

Inherit Core locks: ty, fnox+age, no dotenv secrets, REC-013 command surface.
Write docs/reports/02-ai-native-agent-workflow.md only.
Do not start architecture or mark acceptance.
```

After the report exists: run validation task → human accept → commit.

---

## 11. Anti-patterns to avoid on resume

- Treating this HANDOFF as higher authority than accepted Blueprint/Charter/report
- Running architecture before AI-native is accepted
- Reopening Windows / notebooks / framework zoo
- Reintroducing `.env` secrets “for simplicity”
- Inventing acceptance without human + commit hash in manifest
- Multiple substantive stages in one context without human override

---

## 12. Recent git history (context)

```text
5f6705f Record research-python-ecosystem accepting commit hash in the manifest.
1435c65 docs: accept modern python ecosystem research report
de2cbc2 docs: revise ecosystem report for Core ty, fnox, and age secrets
3b66811 docs: add modern python ecosystem research report
5ea2961 docs: add modern python ecosystem research prompt
… charter + blueprint acceptance earlier
```

---

*End of handoff. Update or replace this file when the next stage is accepted.*
