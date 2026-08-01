# HANDOFF — python-foundry

**Purpose:** Resume packet for a **fresh session**. Git artifacts are authority;
this file only says what to do next and what not to re-open.

| Field | Value |
| ----- | ----- |
| **As of** | 2026-08-01 |
| **Branch** | `main` |
| **Verify** | `git log -1 --oneline` · `research-program.toml` |
| **Program** | `active` · rigor `standard` |
| **Done** | discovery … architecture (**accepted**); **synthesis accepted** (proposed definitive specification) |
| **Next** | **`spec-review`** — still `planned` (JIT package **not** written yet) |

---

## Do next (this is the only work)

### Stage: `spec-review` — Specification Adversarial Review

| | |
| - | - |
| **Kind** | adversarial-review |
| **Output** | `docs/reviews/01-specification-adversarial-review.md` |
| **IDs** | FND-001..FND-199 |
| **Depends on** | synthesis — **accepted** |
| **Skeleton prompt** | `docs/prompts/NN-specification-adversarial-review-prompt.md` |

### Packaging session (allowed now)

1. Read `AGENTS.md` and skill `.agents/skills/research-stage/SKILL.md`.
2. Produce the **five-item JIT package** for `spec-review` only:
   - canonical stage prompt (install under `docs/prompts/` with a stable number)
   - attachment manifest → `docs/handoffs/spec-review-attachment-manifest.md`
   - launch message → `docs/handoffs/spec-review-launch-message.md`
   - validation task → `docs/handoffs/spec-review-validation-task.md`
   - set stage status → **`prompt-ready`** in `research-program.toml`
3. **Do not** write the adversarial review in the packaging session unless the
   human explicitly overrides fresh-session policy.
4. **Do not** mark stages `accepted` without human approval + commit hash.

### Research session (after package; prefer fresh chat)

Paste the launch message. Agent writes the review → `research-validate` →
human accept → commit.

### Attach for spec-review (full artifacts, not digests alone)

| Path | Why |
| ---- | --- |
| `docs/00-program-blueprint.md` | Locks, non-goals, success criteria |
| `docs/01-research-charter.md` | Evidence / review methodology |
| `docs/specifications/01-definitive-specification.md` | **Accepted proposed** spec under attack |
| `docs/reports/01-modern-python-ecosystem.md` | Provenance / lock checks |
| `docs/reports/02-ai-native-agent-workflow.md` | Provenance / lock checks |
| `docs/reports/03-foundry-architecture.md` | Provenance / lock checks |
| Stage prompt (once installed) | Sole mission for the session |
| `program/contracts/adversarial-review.md` | Required review shape |
| `AGENTS.md` | Operating rules |

Owner preference: **one stage at a time**.

---

## Load-bearing locks (do not silently undo)

Point to full reports and the accepted proposed specification for detail.

**Ecosystem Core** (v0.2): Python ≥3.12 / default 3.13; **uv** + lockfile;
**src/**; Ruff; **ty** Required; pytest; pre-commit Default; **fnox** + **age**;
**no `.env` secrets**; GHA; Typer; profiles `http`, `hooks-hk`, `data-etl`;
REC-013.

**AI-native** (v0.2): root **`AGENTS.md` only**; skills under **`.agents/skills/`
only**; MCP default **none**; no Claude adapters; amplify REC-013; fnox exec.

**Architecture** (v0.1.1): planner-led CLI `validate` → `plan` → `generate`;
TOML spec; plan-as-contract; stage → verify → exclusive place; closed catalog;
custom engine; GitHub template = generated snapshot; emit Core + agent surface
as invariants.

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

Next: spec-review packaging only (one stage). Synthesis is already accepted.

1. Read AGENTS.md, research-program.toml, Blueprint, Charter, the accepted
   proposed definitive specification, and reports 01–03 as needed for the
   attachment manifest.
2. Use research-stage to install the JIT package for spec-review
   (prompt, manifest, launch message, validation task; status → prompt-ready).
3. Do not write the adversarial review unless I explicitly ask.
4. Do not mark stages accepted without my approval.
```

---

## Do not

- Treat this handoff as higher authority than Blueprint / Charter / accepted artifacts
- Start **spec-revision** or implementation planning before spec-review is accepted
- Reopen Windows, dotenv secrets, Claude adapters, or demote ty/fnox without a DEC
- Invent acceptance without human + `accepted_commit` in the manifest

---

*Replace this file when spec-review is accepted (or when the next next-stage changes).*
