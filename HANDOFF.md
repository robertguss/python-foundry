# HANDOFF — python-foundry

**Purpose:** Resume packet for a **fresh session**. Git artifacts are authority;
this file only says what to do next and what not to re-open.

| Field | Value |
| ----- | ----- |
| **As of** | 2026-08-01 |
| **Branch** | `main` |
| **Verify** | `git log -1 --oneline` · `research-program.toml` |
| **Program** | `active` · rigor `standard` |
| **Done** | discovery … **spec-revision accepted**; **implementation-plan packaged** (`prompt-ready`) |
| **Next** | **`implementation-plan` substantive session** — write the plan (**fresh chat required**) |

---

## Do next (this is the only work)

### Stage: `implementation-plan` — Implementation Plan

| | |
| - | - |
| **Kind** | implementation-plan |
| **Status** | `prompt-ready` |
| **Prompt** | `docs/prompts/07-implementation-plan-prompt.md` |
| **Output** | `docs/plans/01-implementation-plan.md` |
| **Depends on** | spec-revision — **accepted** (`faffbdc`) |
| **Manifest** | `docs/handoffs/implementation-plan-attachment-manifest.md` |
| **Launch** | `docs/handoffs/implementation-plan-launch-message.md` |
| **Validate** | `docs/handoffs/implementation-plan-validation-task.md` |
| **Authority** | `docs/specifications/02-definitive-specification-revised.md` v0.2 |

### Research session (**fresh chat** — do not run in packaging session)

1. Open a **new** agent session.
2. Paste everything below the horizontal rule in
   `docs/handoffs/implementation-plan-launch-message.md`.
3. Ensure attachment set from the manifest is available.
4. Agent writes `docs/plans/01-implementation-plan.md` only
   → `research-validate` via validation task → human accept → commit.
5. **Do not** mark stages `accepted` without human approval + commit hash.
6. **Do not** start `plan-review` until `implementation-plan` is accepted.
7. **Do not** write a coding backlog — phases and milestones only.

### Attach for implementation-plan

| Path | Why |
| ---- | --- |
| `docs/00-program-blueprint.md` | Locks, success criteria |
| `docs/01-research-charter.md` | Methodology |
| `docs/prompts/07-implementation-plan-prompt.md` | Sole mission |
| `docs/specifications/02-definitive-specification-revised.md` | Implementation authority |
| `docs/reviews/01-specification-adversarial-review.md` | Residual risk context |
| `program/contracts/implementation-plan.md` | Plan shape |
| `program/templates/phase.md` | Phase template |
| `program/templates/milestone.md` | Milestone template |
| `AGENTS.md` | Operating rules |
| `docs/handoffs/implementation-plan-attachment-manifest.md` | Attachment list |

Owner preference: **one stage at a time**.

---

## Load-bearing locks (do not silently undo)

ty Required; fnox+age; no dotenv secrets; AGENTS.md + `.agents/` only; MCP none;
no Claude; validate→plan→generate (+ optional `--plan` bind); exclusive place;
closed catalog; custom engine; generate-time `uv.lock`; verify CLI > TOML >
default.

**Non-goals:** Windows; notebooks/GUI; marketplace; framework zoo; coding backlog
as program output.

---

## Rules (short)

1. Precedence: DEC → Blueprint → Charter → stage prompt → **revised spec** →
   reports → reviews → plans → `research-program.toml` (index only).
2. Fresh session per **substantive** stage (plan writing is substantive).
3. Placeholders never unlock work. Validate before acceptance.
4. Skills: `research-program`, `research-stage`, `research-validate`.

---

## Paste into a fresh research session

Use the full launch message in:

`docs/handoffs/implementation-plan-launch-message.md`

(Copy everything **below** the horizontal rule.)

Short pointer:

```text
Resume python-foundry from HANDOFF.md only as a pointer; Git is authority.

Next: implementation-plan substantive session only (one stage). Packaging is
done; revised specification is implementation authority.

1. Read AGENTS.md and docs/handoffs/implementation-plan-attachment-manifest.md.
2. Execute docs/prompts/07-implementation-plan-prompt.md.
3. Write docs/plans/01-implementation-plan.md only (phases/milestones — no backlog).
4. Do not start plan-review or product implementation.
5. Do not mark stages accepted without my approval.
```

---

## Do not

- Write the implementation plan in this packaging-only session
- Treat HANDOFF as higher authority than Blueprint / Charter / revised spec
- Start **plan-review** before the plan is accepted
- Create a granular coding backlog
- Reopen Windows, dotenv secrets, Claude adapters, or demote ty/fnox without a DEC
- Invent acceptance without human + `accepted_commit`

---

*Replace this file when implementation-plan is accepted (or when the next next-stage changes).*
