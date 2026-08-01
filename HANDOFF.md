# HANDOFF — python-foundry

**Purpose:** Self-contained resume packet for a **fresh session**. Git-tracked
artifacts are authority; this file tells the next agent **exactly what to do**
and what not to re-open. Prefer reading the full attached paths below over chat
history.

| Field | Value |
| ----- | ----- |
| **As of** | 2026-08-01 |
| **Branch** | `main` |
| **HEAD (packaging)** | see `git log -1` after packaging commit |
| **Verify** | `git log -1 --oneline` · `research-program.toml` · `just check` |
| **Program** | `active` · rigor `standard` |
| **Done** | discovery … **plan-review accepted** (`7032972`); **plan-revision packaged** (`prompt-ready`) |
| **Next** | **`plan-revision` substantive session only** — write the revised plan |

---

## Mission (execute this stage now)

You are executing **Final Revised Implementation Plan** (`plan-revision`) of the
**python-foundry** research program.

### Stage card

| | |
| - | - |
| **Kind** | artifact-revision |
| **Status** | `prompt-ready` (do **not** mark `accepted` without human + commit) |
| **Prompt (sole mission)** | `docs/prompts/09-implementation-plan-revision-prompt.md` |
| **Output (only write)** | `docs/plans/02-implementation-plan-revised.md` |
| **Depends on** | `plan-review` — **accepted** (`703297212c797f747de47448c91ce1d5aa5269de`) |
| **Findings to dispose** | **FND-200..FND-205** (exactly one disposition each) |
| **Base text** | `docs/plans/01-implementation-plan.md` v0.1 — proposed; **not** delivery authority |
| **Product law** | `docs/specifications/02-definitive-specification-revised.md` v0.2 (`faffbdc`) — **implementation authority** |
| **Manifest** | `docs/handoffs/plan-revision-attachment-manifest.md` |
| **Launch** | `docs/handoffs/plan-revision-launch-message.md` |
| **Validation task** | `docs/handoffs/plan-revision-validation-task.md` |
| **Skill after write** | `research-validate` |

### Steps (in order)

1. Read **AGENTS.md**, then every path in **Attachments** below (full files).
2. Execute **`docs/prompts/09-implementation-plan-revision-prompt.md` completely**.
3. Replace the placeholder at
   **`docs/plans/02-implementation-plan-revised.md`** with a complete standalone
   revised plan (Finding Disposition Ledger for FND-200..205; integrate
   corrections into body).
4. Run independent validation per
   `docs/handoffs/plan-revision-validation-task.md` / skill `research-validate`;
   write `docs/validations/02-implementation-plan-revised-validation.md` if that
   is the local convention.
5. Stop for **human accept** before marking the stage accepted or starting
   product implementation.
6. After human accept: commit revised plan; record `accepted_commit` on
   `plan-revision` in `research-program.toml` (human-owned process).

### End-of-session deliverables

1. Complete revised plan artifact (on disk or full Markdown).
2. Brief execution summary outside the artifact.
3. Any unmet requirement and why.
4. Any remaining blocker.

---

## Attachments (read completely before writing)

| # | Path | Role |
| - | ---- | ---- |
| 1 | `docs/00-program-blueprint.md` | Accepted Blueprint — locks, non-goals, success criteria |
| 2 | `docs/01-research-charter.md` | Accepted Charter — methodology, evidence rules |
| 3 | `docs/prompts/09-implementation-plan-revision-prompt.md` | **Sole stage mission** |
| 4 | `docs/plans/01-implementation-plan.md` | **Base text** (proposed plan) |
| 5 | `docs/reviews/02-implementation-plan-adversarial-review.md` | **Accepted** findings FND-200..205 |
| 6 | `docs/specifications/02-definitive-specification-revised.md` | **Implementation authority** |
| 7 | `AGENTS.md` | Operating rules for agents in this repo |
| 8 | `program/contracts/implementation-plan.md` | Plan boundary + final revised plan rules |
| 9 | `program/templates/phase.md` | Phase shape |
| 10 | `program/templates/milestone.md` | Milestone shape |
| 11 | `program/operator/completion-criteria.md` | Final implementation handoff fields |
| 12 | `program/contracts/authority-and-precedence.md` | Precedence ladder |
| 13 | `docs/handoffs/plan-revision-attachment-manifest.md` | Attachment list (this set) |

**Do not treat as authority:** chat history, this HANDOFF over Blueprint/Charter/spec,
placeholder `docs/plans/02-*` until you replace it.

---

## Authority and precedence (highest first)

1. Accepted `DEC-###` (none expected under `decisions/` unless present).
2. `docs/00-program-blueprint.md` locks and non-goals.
3. `docs/01-research-charter.md` methodology.
4. `docs/prompts/09-implementation-plan-revision-prompt.md` (this stage).
5. **Revised specification v0.2** — product law; plan is subordinate.
6. **This revised plan** (output) — delivery authority only after human accept
   if status is `Accepted — delivery authority`.
7. Proposed plan — base text only.
8. Accepted plan-review — findings to dispose; not automatic law.
9. `research-program.toml` — index only.
10. Model preference — lowest.

---

## Findings that revision must address

| Severity | IDs | Theme |
| -------- | --- | ----- |
| High | FND-200 | Catalog freeze before dogfood; post-exit PHASE-04 reopen fiction |
| High | FND-201 | PHASE-04 overlarge; progressive integration missing |
| Medium | FND-202 | ty at MS-002 vs SPK-002 config freeze timing |
| Medium | FND-203 | MS-004 / MS-005 unordered |
| Medium | FND-204 | MS-005 attestation unprovable |
| Medium | FND-205 | Residual-accept of spikes vs Must REQ honesty |

Gate from review: **Conditional** — dispose High findings before delivery
authority freeze claims.

---

## Allowed file scope (substantive session)

| Path | Action |
| ---- | ------ |
| `docs/plans/02-implementation-plan-revised.md` | **Write** (primary) |
| `docs/validations/*plan-revision*` or similar validation report | **Write** (validation gate only) |
| Everything else | **Read only** |

Do **not** edit: proposed plan, review, revised spec, Blueprint, Charter, prompts,
packaging handoffs, or `research-program.toml` until human accept / packaging
process.

---

## After the revised plan is written

1. Validate (`docs/handoffs/plan-revision-validation-task.md`).
2. Human reviews → **accept**.
3. Commit pattern: `docs: publish final revised implementation plan`
4. Record stage `plan-revision` `status = accepted` + `accepted_commit` in
   `research-program.toml` (human-owned).
5. Delivery authority is only the accepted revised plan. Product implementation
   may begin under that plan + revised-spec product law (owner residual risk
   remains separate).

---

## Do not

- Skip reading the full proposed plan, review, and revised specification
- Revise the proposed plan `01-`, the review, or the specification in this session
- Start product implementation as the main deliverable of this stage
- Create a coding backlog / sprint tickets / agent task packets
- Reverse ty, fnox, AGENTS-only, no-Claude, exclusive place, custom engine, etc.
- Silently drop any of FND-200..205
- Treat the proposed plan as **delivery authority**
- Treat this HANDOFF as higher authority than Blueprint / Charter / revised spec
- Mark stages `accepted` without human approval + commit hash
- Ask clarifying questions unless a true blocker exists under the prompt

---

## Paste-ready short kickoff (if needed)

```text
Resume python-foundry from HANDOFF.md. Git is authority.

Next: plan-revision substantive session only (one stage).

1. Read AGENTS.md and every attachment listed in HANDOFF.md.
2. Execute docs/prompts/09-implementation-plan-revision-prompt.md.
3. Write docs/plans/02-implementation-plan-revised.md only
   (dispose FND-200..205; integrate corrections; phases/milestones only).
4. Validate via docs/handoffs/plan-revision-validation-task.md.
5. Do not start product implementation.
6. Do not mark stages accepted without my approval.
```

---

## Program position (index only)

| Stage | Status | Commit / note |
| ----- | ------ | ------------- |
| … through `spec-revision` | accepted | revised-spec v0.2 = product law (`faffbdc`) |
| `implementation-plan` | accepted | proposed plan `ab72895` (not delivery authority) |
| `plan-review` | accepted | review `7032972` · FND-200..205 · Conditional |
| `plan-revision` | **prompt-ready** | **you are here** (package installed) |

Owner preference: **one stage at a time**.

---

*Replace this file when plan-revision is accepted (or when next-stage work changes).*
