# HANDOFF — python-foundry

**Purpose:** Self-contained resume packet for a **fresh session**. Git-tracked
artifacts are authority; this file tells the next agent **exactly what to do**
and what not to re-open. Prefer reading the full attached paths below over chat
history.

| Field | Value |
| ----- | ----- |
| **As of** | 2026-08-01 |
| **Branch** | `main` |
| **HEAD (accept record)** | see `git log -1` after accept commits |
| **Verify** | `git log -1 --oneline` · `research-program.toml` · `just check` |
| **Program** | `active` · rigor `standard` |
| **Done** | discovery … **plan-review accepted** (`7032972`; FND-200..205; **Conditional** gate) |
| **Next** | **`plan-revision` packaging** — JIT package **not** written yet |

---

## Do next (this is the only work)

### Stage: `plan-revision` — Final Revised Implementation Plan

| | |
| - | - |
| **Kind** | artifact-revision |
| **Status** | `planned` (package first) |
| **Output** | `docs/plans/02-implementation-plan-revised.md` |
| **Depends on** | plan-review — **accepted** (`703297212c797f747de47448c91ce1d5aa5269de`) |
| **Skeleton prompt** | `docs/prompts/NN-final-plan-revision-prompt.md` (install with stable number) |
| **Subject inputs** | Proposed plan + accepted review (dispose **every** FND-200..205) |
| **Product law** | Revised-spec v0.2 (`faffbdc`) — plan remains subordinate |
| **Delivery status after accept** | `Accepted — delivery authority` on revised plan only |

### Packaging session (allowed now)

1. Read `AGENTS.md` and skill `.agents/skills/research-stage/SKILL.md`.
2. Produce the **five-item JIT package** for `plan-revision` only:
   - canonical stage prompt under `docs/prompts/` (stable number; replace `NN-`)
   - attachment manifest → `docs/handoffs/plan-revision-attachment-manifest.md`
   - launch message → `docs/handoffs/plan-revision-launch-message.md`
   - validation task → `docs/handoffs/plan-revision-validation-task.md`
   - set stage status → **`prompt-ready`** in `research-program.toml`
3. **Do not** write the revised plan in the packaging session unless the human
   explicitly overrides fresh-session policy.
4. **Do not** mark stages `accepted` without human approval + commit hash.

### Research session (after package; prefer fresh chat)

Paste the launch message. Agent produces `docs/plans/02-implementation-plan-revised.md`
with a **Finding Disposition Ledger** for FND-200..205 → `research-validate` →
human accept → commit. That file becomes **delivery authority**.

### Findings that revision must address

| Severity | IDs | Theme |
| -------- | --- | ----- |
| High | FND-200 | Catalog freeze exits before dogfood; rollback reopens PHASE-04 after exit |
| High | FND-201 | PHASE-04 overlarge; single MS-003 hides progressive integration |
| Medium | FND-202 | ty hardened at MS-002 default verify before SPK-002 config gate |
| Medium | FND-203 | MS-004 / MS-005 unordered; hybrid can freeze before dogfood |
| Medium | FND-204 | MS-005 owner attestation unprovable as sole acceptance evidence |
| Medium | FND-205 | Residual-accept of spikes can undercut Must REQ exit honesty |

Gate from review: **Conditional** — dispose High findings before treating catalog
freeze / hybrid readiness as delivery authority.

### Authority reminder

| Artifact | Role |
| -------- | ---- |
| Revised-spec v0.2 | **Implementation authority** (product law) |
| Plan `01-` v0.1 | **Proposed** only (stage accepted; **not** delivery authority) |
| Review `02-` | Findings for plan-revision; not product law |
| Plan `02-` (future) | **Delivery authority** only after plan-revision accept |

### Attach for plan-revision (when packaging)

| Path | Why |
| ---- | --- |
| `docs/00-program-blueprint.md` | Locks, non-goals, success criteria |
| `docs/01-research-charter.md` | Methodology |
| `docs/plans/01-implementation-plan.md` | Proposed plan being revised |
| `docs/reviews/02-implementation-plan-adversarial-review.md` | **Accepted** findings to dispose |
| `docs/specifications/02-definitive-specification-revised.md` | Product law; plan must stay subordinate |
| Stage prompt (once installed) | Sole mission |
| `program/contracts/implementation-plan.md` | Plan boundary + final revised plan rules |
| `program/contracts/adversarial-review.md` | Disposition / additional-round context |
| `program/contracts/authority-and-precedence.md` | Precedence ladder |
| `AGENTS.md` | Operating rules |

**Locks (do not reverse via plan “fixes”):** ty Required; fnox+age; no dotenv secrets;
AGENTS.md + `.agents/` only; MCP none; no Claude; validate→plan→generate (+ optional
`--plan` bind); exclusive place; closed catalog; custom engine; generate-time
`uv.lock`; verify CLI > TOML > default; frozen public template cell.

**Non-goals (do not reopen):** Windows; notebooks/GUI; marketplace; framework zoo;
coding backlog as program output.

---

## Program position (index only)

| Stage | Status | Commit / note |
| ----- | ------ | ------------- |
| … through `spec-revision` | accepted | revised-spec v0.2 = product law (`faffbdc`) |
| `implementation-plan` | accepted | proposed plan `ab72895` (not delivery authority) |
| `plan-review` | **accepted** | review `7032972` · FND-200..205 · Conditional |
| `plan-revision` | **planned** | package next; then substantive fresh session |

Owner preference: **one stage at a time**.

---

## Do not

- Start product implementation as a substitute for an accepted revised plan
- Treat proposed plan `01-` as delivery authority
- Mark stages `accepted` without human approval + commit hash
- Reverse product locks or Blueprint non-goals
- Chain plan-revision packaging and substantive revision unless human overrides
- Invent coding backlog / sprint tickets / agent task packets

---

## Paste-ready short kickoff (packaging)

```text
Resume python-foundry from HANDOFF.md. Git is authority.

Next: plan-revision packaging only (research-stage skill).
Do not write the revised plan in the packaging session.
Dispose FND-200..205 is for the later substantive session.
```

---

*Replace this file when plan-revision is packaged or accepted.*
