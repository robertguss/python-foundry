# HANDOFF — python-foundry

**Purpose:** Resume packet for a **fresh session**. Git artifacts are authority;
this file only says what to do next and what not to re-open.

| Field | Value |
| ----- | ----- |
| **As of** | 2026-08-01 |
| **Branch** | `main` |
| **Verify** | `git log -1 --oneline` · `research-program.toml` |
| **Program** | `active` · rigor `standard` |
| **Done** | discovery … **implementation-plan accepted**; **plan-review packaged** (`prompt-ready`) |
| **Next** | **`plan-review` substantive session** — adversarial review of the plan (**fresh chat required**) |

---

## Do next (this is the only work)

### Stage: `plan-review` — Implementation Plan Adversarial Review

| | |
| - | - |
| **Kind** | adversarial-review |
| **Status** | `prompt-ready` |
| **Prompt** | `docs/prompts/08-implementation-plan-review-prompt.md` |
| **Output** | `docs/reviews/02-implementation-plan-adversarial-review.md` |
| **Depends on** | implementation-plan — **accepted** (`ab72895`) |
| **Finding range** | FND-200..FND-399 |
| **Manifest** | `docs/handoffs/plan-review-attachment-manifest.md` |
| **Launch** | `docs/handoffs/plan-review-launch-message.md` |
| **Validate** | `docs/handoffs/plan-review-validation-task.md` |
| **Subject** | `docs/plans/01-implementation-plan.md` v0.1 (proposed; not delivery authority) |
| **Product law** | `docs/specifications/02-definitive-specification-revised.md` v0.2 |

### Research session (**fresh chat** — do not run in packaging session)

1. Open a **new** agent session.
2. Paste everything below the horizontal rule in
   `docs/handoffs/plan-review-launch-message.md`.
3. Ensure attachment set from the manifest is available.
4. Agent writes `docs/reviews/02-implementation-plan-adversarial-review.md` only
   → `research-validate` via validation task → human accept → commit.
5. **Do not** mark stages `accepted` without human approval + commit hash.
6. **Do not** start `plan-revision` until `plan-review` is accepted.
7. Attack **sequencing**, not product taste; do not rewrite REQs or the plan.

### Attach for plan-review

| Path | Why |
| ---- | --- |
| `docs/00-program-blueprint.md` | Locks, non-goals |
| `docs/01-research-charter.md` | Methodology |
| `docs/prompts/08-implementation-plan-review-prompt.md` | Sole mission |
| `docs/plans/01-implementation-plan.md` | Attack surface |
| `docs/specifications/02-definitive-specification-revised.md` | Implementation authority |
| `program/contracts/adversarial-review.md` | Review contract |
| `program/templates/finding.md` | Finding shape |
| `program/contracts/implementation-plan.md` | Plan boundary |
| `AGENTS.md` | Operating rules |
| `docs/handoffs/plan-review-attachment-manifest.md` | Attachment list |

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
   proposed plan → this review → `research-program.toml` (index only).
2. Fresh session per **substantive** stage (plan-review is substantive).
3. Placeholders never unlock work. Validate before acceptance.
4. Skills: `research-program`, `research-stage`, `research-validate`.
5. FND-200..399 only; do not reuse FND-001..199.

---

## Paste into a fresh research session

Use the full launch message in:

`docs/handoffs/plan-review-launch-message.md`

(Copy everything **below** the horizontal rule.)

Short pointer:

```text
Resume python-foundry from HANDOFF.md only as a pointer; Git is authority.

Next: plan-review substantive session only (one stage). Packaging is done;
proposed plan is stage-accepted but not delivery authority.

1. Read AGENTS.md and docs/handoffs/plan-review-attachment-manifest.md.
2. Execute docs/prompts/08-implementation-plan-review-prompt.md.
3. Write docs/reviews/02-implementation-plan-adversarial-review.md only
   (FND-200..399; sequencing attacks).
4. Do not start plan-revision or product implementation.
5. Do not mark stages accepted without my approval.
```

---

## Do not

- Write the adversarial review in this packaging-only session
- Treat HANDOFF as higher authority than Blueprint / Charter / revised spec
- Treat the proposed plan as **delivery authority**
- Start **plan-revision** before plan-review is accepted
- Reverse ty/fnox/AGENTS/no-Claude locks via “findings”
- Create a coding backlog as review output
- Invent acceptance without human + `accepted_commit`

---

*Replace this file when plan-review is accepted (or when the next next-stage changes).*
