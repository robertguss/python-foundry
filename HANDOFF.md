# HANDOFF — python-foundry

**Purpose:** Resume packet for a **fresh session**. Git artifacts are authority;
this file only says what to do next and what not to re-open.

| Field | Value |
| ----- | ----- |
| **As of** | 2026-08-01 |
| **Branch** | `main` |
| **Verify** | `git log -1 --oneline` · `research-program.toml` |
| **Program** | `active` · rigor `standard` |
| **Done** | discovery … **spec-review accepted**; **spec-revision accepted** (v0.2 implementation authority) |
| **Next** | **`implementation-plan` packaging** — JIT package **not** written yet |

---

## Do next (this is the only work)

### Stage: `implementation-plan` — Implementation Plan

| | |
| - | - |
| **Kind** | implementation-plan |
| **Status** | `planned` (package first) |
| **Output** | `docs/plans/01-implementation-plan.md` |
| **Depends on** | spec-revision — **accepted** (`faffbdc`) |
| **Skeleton prompt** | `docs/prompts/NN-implementation-plan-prompt.md` |
| **Authority** | Revised definitive specification v0.2 |

### Packaging session (allowed now)

1. Read `AGENTS.md` and skill `.agents/skills/research-stage/SKILL.md`.
2. Produce the **five-item JIT package** for `implementation-plan` only:
   - canonical stage prompt under `docs/prompts/` (stable number)
   - attachment manifest → `docs/handoffs/implementation-plan-attachment-manifest.md`
   - launch message → `docs/handoffs/implementation-plan-launch-message.md`
   - validation task → `docs/handoffs/implementation-plan-validation-task.md`
   - set stage status → **`prompt-ready`** in `research-program.toml`
3. **Do not** write the implementation plan in the packaging session unless the
   human explicitly overrides fresh-session policy.
4. **Do not** mark stages `accepted` without human approval + commit hash.

### Research session (after package; prefer fresh chat)

Paste the launch message. Agent writes the plan from the **revised**
specification → validate → human accept → commit → then plan-review.

### Implementation authority

`docs/specifications/02-definitive-specification-revised.md` v0.2  
(FND-001..012 disposed; High findings resolved.)

### Attach for implementation-plan (when packaging)

| Path | Why |
| ---- | --- |
| `docs/00-program-blueprint.md` | Locks, success criteria |
| `docs/01-research-charter.md` | Methodology |
| `docs/specifications/02-definitive-specification-revised.md` | **Implementation authority** |
| `docs/reviews/01-specification-adversarial-review.md` | Finding context / residual risk |
| Stage prompt (once installed) | Sole mission |
| `program/contracts/implementation-plan.md` | Required plan shape |
| `AGENTS.md` | Operating rules |

Owner preference: **one stage at a time**.

---

## Load-bearing locks (do not silently undo)

**Ecosystem Core** (v0.2): Python ≥3.12 / default 3.13; **uv** + lockfile;
**src/**; Ruff; **ty** Required; pytest; pre-commit Default; **fnox** + **age**;
**no `.env` secrets**; GHA; Typer; profiles; REC-013.

**AI-native** (v0.2): root **`AGENTS.md` only**; skills under **`.agents/skills/`
only**; MCP default **none**; no Claude adapters.

**Architecture** (v0.1.1 + revision): `validate` → `plan` → `generate` (+ optional
`--plan` bind); exclusive place; closed catalog; custom engine; generate-time
`uv.lock`; verify CLI > TOML > default.

**Non-goals:** Windows; notebooks/GUI; marketplace; framework zoo; coding backlog
as program output.

---

## Rules (short)

1. Precedence: accepted `DEC-###` → Blueprint → Charter → stage prompt →
   **revised spec** → reports → reviews → plans → `research-program.toml` (index).
2. Fresh session per **substantive** stage; packaging is OK now.
3. Placeholders never unlock work. Validate before acceptance.
4. Skills: `research-program`, `research-stage`, `research-validate`.

---

## Paste into a fresh packaging session

```text
Resume python-foundry from HANDOFF.md only as a pointer; Git is authority.

Next: implementation-plan packaging only (one stage). Spec-revision is accepted.

1. Read AGENTS.md, research-program.toml, Blueprint, Charter, and the revised
   definitive specification (implementation authority).
2. Use research-stage to install the JIT package for implementation-plan
   (prompt, manifest, launch message, validation task; status → prompt-ready).
3. Do not write the implementation plan unless I explicitly ask.
4. Do not mark stages accepted without my approval.
```

---

## Do not

- Treat this handoff as higher authority than Blueprint / Charter / revised spec
- Start **plan-review** before the implementation plan is accepted
- Implement the product as a substitute for an accepted plan
- Reopen Windows, dotenv secrets, Claude adapters, or demote ty/fnox without a DEC
- Invent acceptance without human + `accepted_commit`

---

*Replace this file when implementation-plan is accepted (or when the next next-stage changes).*
