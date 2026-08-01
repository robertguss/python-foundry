# HANDOFF — python-foundry

**Purpose:** Resume packet for a **fresh session**. Git artifacts are authority;
this file only says what to do next and what not to re-open.

| Field | Value |
| ----- | ----- |
| **As of** | 2026-08-01 |
| **Branch** | `main` |
| **Verify** | `git log -1 --oneline` · `research-program.toml` |
| **Program** | `active` · rigor `standard` |
| **Done** | discovery, charter, ecosystem, AI-native, **architecture** (all **accepted**) |
| **Next** | **`synthesis`** — still `planned` (JIT package **not** written yet) |

---

## Do next (this is the only work)

### Stage: `synthesis` — Definitive Specification Synthesis

| | |
| - | - |
| **Kind** | chief-architect-synthesis |
| **Output** | `docs/specifications/01-definitive-specification.md` |
| **IDs** | REQ-001..299 |
| **Depends on** | all three research reports — **accepted** |
| **Skeleton prompt** | `docs/prompts/NN-chief-architect-synthesis-prompt.md` |

### Packaging session (allowed now)

1. Read `AGENTS.md` and skill `.agents/skills/research-stage/SKILL.md`.
2. Produce the **five-item JIT package** for `synthesis` only:
   - canonical stage prompt (install under `docs/prompts/` with a stable number)
   - attachment manifest → `docs/handoffs/synthesis-attachment-manifest.md`
   - launch message → `docs/handoffs/synthesis-launch-message.md`
   - validation task → `docs/handoffs/synthesis-validation-task.md`
   - set stage status → **`prompt-ready`** in `research-program.toml`
3. **Do not** write the definitive specification in the packaging session unless
   the human explicitly overrides fresh-session policy.
4. **Do not** mark stages `accepted` without human approval + commit hash.

### Research session (after package; prefer fresh chat)

Paste the launch message. Agent writes the specification → `research-validate` →
human accept → commit.

### Attach for synthesis (full artifacts, not digests alone)

| Path | Why |
| ---- | --- |
| `docs/00-program-blueprint.md` | Locks, scope, success criteria |
| `docs/01-research-charter.md` | Evidence / REQ methodology |
| `docs/reports/01-modern-python-ecosystem.md` | Accepted Core/profiles (v0.2) |
| `docs/reports/02-ai-native-agent-workflow.md` | Accepted agent surface (v0.2) |
| `docs/reports/03-foundry-architecture.md` | Accepted generator architecture (v0.1.1) |
| Stage prompt (once installed) | Sole mission for the session |
| `program/contracts/` synthesis + definitive-spec contracts | Required shape |
| `AGENTS.md` | Operating rules |

Owner preference: **one stage at a time**.

---

## Load-bearing locks (do not silently undo)

Point to full reports for detail. Synthesis **traces** these into REQs; it does
not re-litigate them without a DEC.

**Ecosystem Core** (`docs/reports/01-…` v0.2): Python ≥3.12 / default 3.13; **uv**
+ lockfile; **src/**; Ruff; **ty** Required; pytest; pre-commit Default; **fnox**
+ **age**; **no `.env` secrets**; GHA; Typer default CLI; profiles `http`,
`hooks-hk`, `data-etl`; command surface REC-013.

**AI-native** (`docs/reports/02-…` v0.2): root **`AGENTS.md` only**; skills under
**`.agents/skills/` only**; MCP default **none**; no Claude adapters; amplify
REC-013; fnox exec secrets.

**Architecture** (`docs/reports/03-…` v0.1.1): planner-led CLI `validate` →
`plan` → `generate`; TOML spec; plan-as-contract; stage → verify → exclusive
place; closed catalog; custom engine (not Copier runtime); GitHub template =
generated snapshot; emit Core + agent surface as invariants.

**Non-goals:** Windows; notebooks/GUI; marketplace; framework zoo; coding backlog
as program output.

---

## Rules (short)

1. Precedence: accepted `DEC-###` → Blueprint → Charter → stage prompt → revised
   spec → reports → reviews → plans → `research-program.toml` (index only).
2. Fresh session per **substantive** stage; packaging/mechanical work is OK now.
3. Placeholders never unlock work. Validate before acceptance.
4. Skills: `research-program`, `research-stage`, `research-validate` under
   `.agents/skills/`.

---

## Paste into a fresh packaging session

```text
Resume python-foundry from HANDOFF.md only as a pointer; Git is authority.

Next: synthesis packaging only (one stage). Architecture is already accepted.

1. Read AGENTS.md, research-program.toml, Blueprint, Charter, and accepted
   reports 01, 02, 03 in full as needed for the attachment manifest.
2. Use research-stage to install the JIT package for synthesis
   (prompt, manifest, launch message, validation task; status → prompt-ready).
3. Do not write the definitive specification unless I explicitly ask.
4. Do not mark stages accepted without my approval.
```

---

## Do not

- Treat this handoff as higher authority than Blueprint / Charter / accepted reports
- Start **spec-review** or implementation planning before synthesis is accepted
- Reopen Windows, dotenv secrets, Claude adapters, or demote ty/fnox without a DEC
- Invent acceptance without human + `accepted_commit` in the manifest

---

*Replace this file when synthesis is accepted (or when the next next-stage changes).*
