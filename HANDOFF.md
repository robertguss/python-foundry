# HANDOFF — python-foundry

**Purpose:** Resume packet for a **fresh session**. Git artifacts are authority;
this file only says what to do next and what not to re-open.

| Field | Value |
| ----- | ----- |
| **As of** | 2026-08-01 |
| **Branch** | `main` |
| **Verify** | `git log -1 --oneline` · `research-program.toml` |
| **Program** | `active` · rigor `standard` |
| **Done** | discovery … **spec-review accepted**; **spec-revision packaged** (`prompt-ready`) |
| **Next** | **`spec-revision` substantive session** — write the revised specification (prefer **fresh chat**) |

---

## Do next (this is the only work)

### Stage: `spec-revision` — Revised Definitive Specification

| | |
| - | - |
| **Kind** | artifact-revision |
| **Status** | `prompt-ready` |
| **Prompt** | `docs/prompts/06-specification-revision-prompt.md` |
| **Output** | `docs/specifications/02-definitive-specification-revised.md` |
| **Depends on** | spec-review — **accepted** (`9d11cd8`) |
| **Manifest** | `docs/handoffs/spec-revision-attachment-manifest.md` |
| **Launch** | `docs/handoffs/spec-revision-launch-message.md` |
| **Validate** | `docs/handoffs/spec-revision-validation-task.md` |
| **Dispose** | Every **FND-001..FND-012** |

### Research session (prefer fresh chat)

1. Open a **new** agent session.
2. Paste the launch message from
   `docs/handoffs/spec-revision-launch-message.md` (content below the horizontal
   rule).
3. Attach (or ensure workspace read access to) every path in
   `docs/handoffs/spec-revision-attachment-manifest.md`.
4. Agent writes the revised specification → run `research-validate` using
   `docs/handoffs/spec-revision-validation-task.md` → human accept → commit.
5. **Do not** mark stages `accepted` without human approval + commit hash.
6. **Do not** start `implementation-plan` until `spec-revision` is accepted.

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

### Attach for spec-revision (full artifacts)

| Path | Why |
| ---- | --- |
| `docs/00-program-blueprint.md` | Locks, non-goals |
| `docs/01-research-charter.md` | Methodology |
| `docs/prompts/06-specification-revision-prompt.md` | Sole mission |
| `docs/specifications/01-definitive-specification.md` | Base proposed spec |
| `docs/reviews/01-specification-adversarial-review.md` | Accepted findings |
| `docs/reports/01`–`03` | Provenance / lock checks |
| `program/contracts/definitive-specification.md` | Revision rules |
| `program/templates/requirement.md` | REQ shape |
| `AGENTS.md` | Operating rules |
| `docs/handoffs/spec-revision-attachment-manifest.md` | Attachment list |

Owner preference: **one stage at a time**.

---

## Load-bearing locks (do not silently undo)

**Ecosystem Core** (v0.2): Python ≥3.12 / default 3.13; **uv** + lockfile;
**src/**; Ruff; **ty** Required; pytest; pre-commit Default; **fnox** + **age**;
**no `.env` secrets**; GHA; Typer; profiles; REC-013.

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

## Paste into a fresh research session

Use the full launch message in:

`docs/handoffs/spec-revision-launch-message.md`

(Copy everything **below** the horizontal rule in that file.)

Short pointer if needed:

```text
Resume python-foundry from HANDOFF.md only as a pointer; Git is authority.

Next: spec-revision substantive session only (one stage). Packaging is done;
spec-review is accepted.

1. Read AGENTS.md and docs/handoffs/spec-revision-attachment-manifest.md.
2. Execute docs/prompts/06-specification-revision-prompt.md.
3. Write docs/specifications/02-definitive-specification-revised.md only.
4. Dispose every FND-001..012; integrate corrections; prefer simplification.
5. Do not start implementation-plan or mark stages accepted without my approval.
```

---

## Do not

- Treat this handoff as higher authority than Blueprint / Charter / accepted artifacts
- Start **implementation-plan** before the revised specification is accepted
- Silently drop any FND-001..012
- Reopen Windows, dotenv secrets, Claude adapters, or demote ty/fnox without a DEC
- Invent acceptance without human + `accepted_commit` in the manifest
- Write the revised specification in a packaging-only session unless the human
  explicitly overrides fresh-session policy

---

*Replace this file when spec-revision is accepted (or when the next next-stage changes).*
