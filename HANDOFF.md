# HANDOFF — python-foundry

**Purpose:** Resume packet for a **fresh session**. Git artifacts are authority;
this file only says what to do next and what not to re-open.

| Field | Value |
| ----- | ----- |
| **As of** | 2026-08-01 |
| **Branch** | `main` |
| **Verify** | `git log -1 --oneline` · `research-program.toml` |
| **Program** | `active` · rigor `standard` |
| **Done** | discovery … **implementation-plan accepted** (proposed plan; not delivery authority) |
| **Next** | **`plan-review` packaging** — JIT package **not** written yet |

---

## Do next (this is the only work)

### Stage: `plan-review` — Implementation Plan Adversarial Review

| | |
| - | - |
| **Kind** | adversarial-review |
| **Status** | `planned` (package first) |
| **Output** | `docs/reviews/02-implementation-plan-adversarial-review.md` |
| **Depends on** | implementation-plan — **accepted** (`ab72895`) |
| **Skeleton prompt** | `docs/prompts/NN-implementation-plan-review-prompt.md` |
| **Finding range** | FND-200..FND-399 |
| **Review target** | `docs/plans/01-implementation-plan.md` v0.1 |

### Packaging session (allowed now)

1. Read `AGENTS.md` and skill `.agents/skills/research-stage/SKILL.md`.
2. Produce the **five-item JIT package** for `plan-review` only:
   - canonical stage prompt under `docs/prompts/` (stable number)
   - attachment manifest → `docs/handoffs/plan-review-attachment-manifest.md`
   - launch message → `docs/handoffs/plan-review-launch-message.md`
   - validation task → `docs/handoffs/plan-review-validation-task.md`
   - set stage status → **`prompt-ready`** in `research-program.toml`
3. **Do not** write the adversarial review in the packaging session unless the
   human explicitly overrides fresh-session policy.
4. **Do not** mark stages `accepted` without human approval + commit hash.

### Research session (after package; prefer fresh chat)

Paste the launch message. Agent attacks the **proposed implementation plan**
(sequencing, not product taste) → validate → human accept → commit → then
plan-revision.

### Authority reminder

| Artifact | Role |
| -------- | ---- |
| Revised spec v0.2 | **Implementation authority** (product law) |
| Plan `01-` v0.1 | **Proposed** delivery sequence (stage accepted; not delivery authority) |
| Plan `02-` (future) | Delivery authority only after plan-review + plan-revision |

### Attach for plan-review (when packaging)

| Path | Why |
| ---- | --- |
| `docs/00-program-blueprint.md` | Locks, non-goals, success criteria |
| `docs/01-research-charter.md` | Methodology |
| `docs/specifications/02-definitive-specification-revised.md` | Implementation authority (plan must not contradict) |
| `docs/plans/01-implementation-plan.md` | Review target |
| Stage prompt (once installed) | Sole mission |
| `program/contracts/adversarial-review.md` | Review contract |
| `program/contracts/implementation-plan.md` | Plan shape / boundary |
| `AGENTS.md` | Operating rules |

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
   reports → reviews → **proposed plan** → `research-program.toml` (index only).
2. Fresh session per **substantive** stage; packaging is OK now.
3. Placeholders never unlock work. Validate before acceptance.
4. Skills: `research-program`, `research-stage`, `research-validate`.
5. Plan review attacks **sequencing**, not architecture taste; do not rewrite REQs.

---

## Paste into a fresh packaging session

```text
Resume python-foundry from HANDOFF.md only as a pointer; Git is authority.

Next: plan-review packaging only (one stage). Implementation-plan is accepted
(proposed plan; not delivery authority).

1. Read AGENTS.md, research-program.toml, Blueprint, Charter, revised
   specification, and docs/plans/01-implementation-plan.md.
2. Use research-stage to install the JIT package for plan-review
   (prompt, manifest, launch message, validation task; status → prompt-ready).
3. Do not write the adversarial review unless I explicitly ask.
4. Do not mark stages accepted without my approval.
```

---

## Do not

- Treat this handoff as higher authority than Blueprint / Charter / revised spec
- Treat the proposed plan as **delivery authority** (that is plan-revision `02-`)
- Start **plan-revision** before plan-review is accepted
- Start product implementation as a substitute for final revised plan acceptance
  (owner may accept residual risk; program graph still wants plan-review)
- Reopen Windows, dotenv secrets, Claude adapters, or demote ty/fnox without a DEC
- Invent acceptance without human + `accepted_commit`

---

*Replace this file when plan-review is packaged or accepted (or when next-stage changes).*
