# HANDOFF — python-foundry

**Purpose:** Self-contained resume packet for a **fresh session**. Git-tracked
artifacts are authority; this file tells the next agent **exactly what to do**
and what not to re-open. Prefer reading the full attached paths below over chat
history.

| Field | Value |
| ----- | ----- |
| **As of** | 2026-08-01 |
| **Branch** | `main` |
| **HEAD (packaging)** | `5eeadb6` — `docs: add implementation plan review prompt` |
| **Verify** | `git log -1 --oneline` · `research-program.toml` · `just check` |
| **Program** | `active` · rigor `standard` |
| **Done** | discovery … **implementation-plan accepted** (`ab72895`); **plan-review packaged** (`prompt-ready`) |
| **Next** | **`plan-review` substantive session only** — write the adversarial review |

---

## Mission (execute this stage now)

You are executing **Implementation Plan Adversarial Review** (`plan-review`) of
the **python-foundry** research program.

### Stage card

| | |
| - | - |
| **Kind** | adversarial-review |
| **Status** | `prompt-ready` (do **not** mark `accepted` without human + commit) |
| **Prompt (sole mission)** | `docs/prompts/08-implementation-plan-review-prompt.md` |
| **Output (only write)** | `docs/reviews/02-implementation-plan-adversarial-review.md` |
| **Depends on** | `implementation-plan` — **accepted** (`ab728951a52c1d69cc30e6151034d2af256bed5b`) |
| **Finding range** | **FND-200..FND-399** only (never reuse FND-001..199) |
| **Subject (attack surface)** | `docs/plans/01-implementation-plan.md` v0.1 — stage-accepted, **Proposed — pending plan adversarial review**, **not** delivery authority |
| **Product law** | `docs/specifications/02-definitive-specification-revised.md` v0.2 (`faffbdc`) — **implementation authority** |
| **Manifest** | `docs/handoffs/plan-review-attachment-manifest.md` |
| **Validation task** | `docs/handoffs/plan-review-validation-task.md` |
| **Skill after write** | `research-validate` |

### Steps (in order)

1. Read **AGENTS.md**, then every path in **Attachments** below (full files).
2. Execute **`docs/prompts/08-implementation-plan-review-prompt.md` completely**.
3. Replace the placeholder at
   **`docs/reviews/02-implementation-plan-adversarial-review.md`** with a
   complete standalone adversarial review.
4. Run independent validation per
   `docs/handoffs/plan-review-validation-task.md` / skill `research-validate`;
   write `docs/validations/02-implementation-plan-adversarial-review-validation.md`
   if that is the local convention.
5. Stop for **human accept** before marking the stage accepted or starting
   `plan-revision`.
6. After human accept: commit review; record `accepted_commit` on `plan-review`
   in `research-program.toml` (human-owned process).

### End-of-session deliverables

1. Complete review artifact (on disk or full Markdown).
2. Brief execution summary outside the artifact.
3. Any unmet requirement and why.
4. Any remaining blocker.

---

## Attachments (read completely before writing)

| # | Path | Role |
| - | ---- | ---- |
| 1 | `docs/00-program-blueprint.md` | Accepted Blueprint — locks, non-goals, success criteria |
| 2 | `docs/01-research-charter.md` | Accepted Charter — methodology, evidence rules |
| 3 | `docs/prompts/08-implementation-plan-review-prompt.md` | **Sole stage mission** |
| 4 | `docs/plans/01-implementation-plan.md` | **Attack surface** (proposed plan) |
| 5 | `docs/specifications/02-definitive-specification-revised.md` | **Implementation authority** (plan must not contradict) |
| 6 | `AGENTS.md` | Operating rules for agents in this repo |
| 7 | `program/contracts/adversarial-review.md` | Posture, severity, **implementation-plan review attacks** |
| 8 | `program/templates/finding.md` | FND write-up shape |
| 9 | `program/contracts/implementation-plan.md` | Plan boundary (phases/milestones only) |
| 10 | `program/contracts/authority-and-precedence.md` | Precedence ladder |
| 11 | `docs/handoffs/plan-review-attachment-manifest.md` | Attachment list (this set) |

**Optional in-repo (not required attach):** plan validation report
`docs/validations/01-implementation-plan-validation.md` (process only).

**Do not treat as authority:** chat history, this HANDOFF over Blueprint/Charter/spec,
placeholder `docs/plans/02-*`, `docs/reviews/02-*` until you replace it.

---

## Authority and precedence (highest first)

1. Accepted `DEC-###` (none expected under `decisions/` unless present).
2. `docs/00-program-blueprint.md` locks and non-goals.
3. `docs/01-research-charter.md` methodology.
4. `docs/prompts/08-implementation-plan-review-prompt.md` (this stage).
5. **Revised specification v0.2** — product law; plan is subordinate.
6. **Proposed plan** — attack surface only; not delivery authority.
7. This review (output) — proposals for plan-revision only.
8. `research-program.toml` — index only.
9. Model preference — lowest.

---

## What to attack (sequencing, not product taste)

From `program/contracts/adversarial-review.md` + commissioning prompt:

- Circular or ambiguous phase dependencies; exit criteria that depend on later phases
- Missing prerequisites for claimed exit evidence
- Overlarge phases; milestones without integration evidence
- Acceptance/exit criteria that do not prove outcomes
- Late residual-risk discovery (ty, fnox/dotenv, lock network, `--plan` bind)
- Delayed dogfooding / hybrid template vs catalog breadth
- Thin E2E too late (plan claims PHASE-03 / MS-002 — verify honesty)
- Security / testing / ops gaps by phase; weak rollback triggers
- Phase boundaries that conflict with revised-spec §30–31 / REQ phase tags
- Plan steps that **reinterpret** architecture or REQs
- Order that hardens wrong decisions before spikes
- Coding-backlog creep disguised as milestones
- Unexecutable “readiness” (e.g. MS-006 theater)

**Locks are not defects by preference.** Attack risk, inconsistency, under-spec,
or unprovable gates around:

ty Required; fnox+age; no dotenv secrets; AGENTS.md + `.agents/` only; MCP none;
no Claude; validate→plan→generate (+ optional `--plan` bind); exclusive place;
closed catalog; custom engine; generate-time `uv.lock`; verify CLI > TOML >
default; frozen public template cell.

**Non-goals (do not reopen as product scope):** Windows; notebooks/GUI;
marketplace; framework zoo; coding backlog as program output.

**Strengths to preserve unless truly defective:** PHASE-01..06 continuity; thin
E2E; spike gates; Must REQ traceability; residual risk sequencing; no coding
backlog; subordination to revised spec.

---

## Review output requirements (summary)

- Status: `Complete — pending independent validation and human acceptance` (not Placeholder)
- Findings: **FND-200..FND-399** only; strong few; full finding template fields
- Use **Proposed Plan Diff** (not product code patches; not silent REQ rewrites)
- Sections: metadata; scope/method; executive assessment; findings; sequencing &
  integration issues; gate **Open | Conditional | Blocked**; additional review
  round yes/no; finding index; completion checklist
- If fix requires product law change → say so; require DEC/spec path

Full rules: `docs/prompts/08-implementation-plan-review-prompt.md`.

---

## Allowed file scope (substantive session)

| Path | Action |
| ---- | ------ |
| `docs/reviews/02-implementation-plan-adversarial-review.md` | **Write** (primary) |
| `docs/validations/*plan-review*` or similar validation report | **Write** (validation gate only) |
| Everything else | **Read only** |

Do **not** edit: plan, revised spec, Blueprint, Charter, prompts, packaging
handoffs, or `research-program.toml` until human accept / packaging process.

---

## After the review is written

1. Validate (`docs/handoffs/plan-review-validation-task.md`).
2. Human reviews → **accept**.
3. Commit pattern: `docs: add implementation plan adversarial review`
4. Record stage `plan-review` `status = accepted` + `accepted_commit` in
   `research-program.toml` (human-owned).
5. Then package **`plan-revision`** (not in the same substantive session unless
   human overrides). Delivery authority is only
   `docs/plans/02-implementation-plan-revised.md` after plan-revision accept.

---

## Do not

- Skip reading the full plan and revised specification
- Revise the plan or the specification in this session
- Start **plan-revision** or product implementation
- Create a coding backlog / sprint tickets / agent task packets
- Reverse ty, fnox, AGENTS-only, no-Claude, exclusive place, custom engine, etc.
- Use FND-001..199 for new findings
- Treat the proposed plan as **delivery authority**
- Treat this HANDOFF as higher authority than Blueprint / Charter / revised spec
- Mark stages `accepted` without human approval + commit hash
- Ask clarifying questions unless a true blocker exists under the prompt

---

## Paste-ready short kickoff (if needed)

```text
Resume python-foundry from HANDOFF.md. Git is authority.

Next: plan-review substantive session only (one stage).

1. Read AGENTS.md and every attachment listed in HANDOFF.md.
2. Execute docs/prompts/08-implementation-plan-review-prompt.md.
3. Write docs/reviews/02-implementation-plan-adversarial-review.md only
   (FND-200..399; attack sequencing, not product taste).
4. Validate via docs/handoffs/plan-review-validation-task.md.
5. Do not start plan-revision or product implementation.
6. Do not mark stages accepted without my approval.
```

---

## Program position (index only)

| Stage | Status | Commit / note |
| ----- | ------ | ------------- |
| … through `spec-revision` | accepted | revised spec v0.2 = product law (`faffbdc`) |
| `implementation-plan` | accepted | plan artifact `ab72895` |
| `plan-review` | **prompt-ready** | **you are here** |
| `plan-revision` | planned | blocked until plan-review accepted |

Owner preference: **one stage at a time**.

---

*Replace this file when plan-review is accepted (or when next-stage work changes).*
