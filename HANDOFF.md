# HANDOFF — python-foundry

**Purpose:** Resume packet for a **fresh session**. Git artifacts are authority;
this file only says what to do next and what not to re-open.

| Field | Value |
| ----- | ----- |
| **As of** | 2026-08-01 |
| **Branch** | `main` |
| **Verify** | `git log -1 --oneline` · `research-program.toml` |
| **Program** | `active` · rigor `standard` |
| **Done** | discovery … synthesis **accepted**; **spec-review accepted** (FND-001..012, Conditional gate) |
| **Next** | **`spec-revision` packaging** — JIT package **not** written yet |

---

## Do next (this is the only work)

### Stage: `spec-revision` — Revised Definitive Specification

| | |
| - | - |
| **Kind** | artifact-revision |
| **Status** | `planned` (package first) |
| **Output** | `docs/specifications/02-definitive-specification-revised.md` |
| **Depends on** | spec-review — **accepted** (`9d11cd8`) |
| **Skeleton prompt** | `docs/prompts/NN-specification-revision-prompt.md` |
| **Subject inputs** | Proposed spec + accepted review (dispose **every** FND-001..012) |

### Packaging session (allowed now)

1. Read `AGENTS.md` and skill `.agents/skills/research-stage/SKILL.md`.
2. Produce the **five-item JIT package** for `spec-revision` only:
   - canonical stage prompt (install under `docs/prompts/` with a stable number)
   - attachment manifest → `docs/handoffs/spec-revision-attachment-manifest.md`
   - launch message → `docs/handoffs/spec-revision-launch-message.md`
   - validation task → `docs/handoffs/spec-revision-validation-task.md`
   - set stage status → **`prompt-ready`** in `research-program.toml`
3. **Do not** write the revised specification in the packaging session unless the
   human explicitly overrides fresh-session policy.
4. **Do not** mark stages `accepted` without human approval + commit hash.

### Research session (after package; prefer fresh chat)

Paste the launch message. Agent writes the revised specification with a
**Finding Disposition Ledger** for FND-001..012 → `research-validate` → human
accept → commit.

### Findings that revision must address

| Severity | IDs | Theme |
| -------- | --- | ----- |
| High | FND-001 | TOML vs CLI `verify` precedence |
| High | FND-002 | Profile apply order (catalog vs array) |
| High | FND-003 | `uv.lock` generate-time truth |
| High | FND-004 | Plan→generate binding gap |
| Medium | FND-005..010 | DoD vs default verify; strict+git; data-etl dual name; scripts under-spec; plan_sha256; template snapshot |
| Low | FND-011..012 | Stage retention; error taxonomy |

Gate from review: **Conditional** — dispose High findings before freezing
generate defaults / Core lock emit / public template snapshot.

### Attach for spec-revision (when packaging)

| Path | Why |
| ---- | --- |
| `docs/00-program-blueprint.md` | Locks, non-goals |
| `docs/01-research-charter.md` | Methodology |
| `docs/specifications/01-definitive-specification.md` | Proposed spec being revised |
| `docs/reviews/01-specification-adversarial-review.md` | **Accepted** findings to dispose |
| `docs/reports/01`–`03` | Provenance / lock checks as needed |
| Stage prompt (once installed) | Sole mission |
| `program/contracts/definitive-specification.md` | Revision rules + disposition |
| `AGENTS.md` | Operating rules |

Owner preference: **one stage at a time**.

---

## Load-bearing locks (do not silently undo)

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

Next: spec-revision packaging only (one stage). Spec-review is already accepted.

1. Read AGENTS.md, research-program.toml, Blueprint, Charter, the proposed
   definitive specification, the accepted adversarial review (FND-001..012),
   and reports 01–03 as needed for the attachment manifest.
2. Use research-stage to install the JIT package for spec-revision
   (prompt, manifest, launch message, validation task; status → prompt-ready).
3. Do not write the revised specification unless I explicitly ask.
4. Do not mark stages accepted without my approval.
```

---

## Do not

- Treat this handoff as higher authority than Blueprint / Charter / accepted artifacts
- Start **implementation-plan** before the revised specification is accepted
- Reopen Windows, dotenv secrets, Claude adapters, or demote ty/fnox without a DEC
- Invent acceptance without human + `accepted_commit` in the manifest
- Silently drop any FND-001..012 in revision (every finding needs a disposition)

---

*Replace this file when spec-revision is accepted (or when the next next-stage changes).*
