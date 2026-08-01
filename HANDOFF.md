# HANDOFF — python-foundry

**Purpose:** Resume packet for a **fresh session**. Git artifacts are authority;
this file only says what to do next and what not to re-open.

| Field | Value |
| ----- | ----- |
| **As of** | 2026-08-01 |
| **Branch** | `main` |
| **Verify** | `git log -1 --oneline` · `research-program.toml` |
| **Program** | `active` · rigor `standard` |
| **Done** | discovery … architecture (**accepted**); **synthesis accepted**; **spec-review packaged** (`prompt-ready`) |
| **Next** | **`spec-review` substantive session** — write the adversarial review (prefer **fresh chat**) |

---

## Do next (this is the only work)

### Stage: `spec-review` — Specification Adversarial Review

| | |
| - | - |
| **Kind** | adversarial-review |
| **Status** | `prompt-ready` |
| **Prompt** | `docs/prompts/05-specification-adversarial-review-prompt.md` |
| **Output** | `docs/reviews/01-specification-adversarial-review.md` |
| **IDs** | FND-001..FND-199 |
| **Depends on** | synthesis — **accepted** |
| **Manifest** | `docs/handoffs/spec-review-attachment-manifest.md` |
| **Launch** | `docs/handoffs/spec-review-launch-message.md` |
| **Validate** | `docs/handoffs/spec-review-validation-task.md` |

### Research session (prefer fresh chat)

1. Open a **new** agent session.
2. Paste the launch message from
   `docs/handoffs/spec-review-launch-message.md` (content below the horizontal
   rule).
3. Attach (or ensure workspace read access to) every path in
   `docs/handoffs/spec-review-attachment-manifest.md`.
4. Agent writes the review → run `research-validate` using
   `docs/handoffs/spec-review-validation-task.md` → human accept → commit.
5. **Do not** mark stages `accepted` without human approval + commit hash.
6. **Do not** start `spec-revision` until `spec-review` is accepted.

### Attach for spec-review (full artifacts, not digests alone)

| Path | Why |
| ---- | --- |
| `docs/00-program-blueprint.md` | Locks, non-goals, success criteria |
| `docs/01-research-charter.md` | Evidence / review methodology |
| `docs/prompts/05-specification-adversarial-review-prompt.md` | Sole mission for the session |
| `docs/specifications/01-definitive-specification.md` | **Accepted proposed** spec under attack |
| `docs/reports/01-modern-python-ecosystem.md` | Provenance / lock checks |
| `docs/reports/02-ai-native-agent-workflow.md` | Provenance / lock checks |
| `docs/reports/03-foundry-architecture.md` | Provenance / lock checks |
| `program/contracts/adversarial-review.md` | Required review shape |
| `program/templates/finding.md` | Finding template |
| `program/contracts/authority-and-precedence.md` | Precedence ladder |
| `program/contracts/definitive-specification.md` | Spec shape checks |
| `AGENTS.md` | Operating rules |
| `docs/handoffs/spec-review-attachment-manifest.md` | This stage’s attachment list |

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

## Paste into a fresh research session

Use the full launch message in:

`docs/handoffs/spec-review-launch-message.md`

(Copy everything **below** the horizontal rule in that file.)

Short pointer if needed:

```text
Resume python-foundry from HANDOFF.md only as a pointer; Git is authority.

Next: spec-review substantive session only (one stage). Packaging is done;
synthesis is accepted.

1. Read AGENTS.md and docs/handoffs/spec-review-attachment-manifest.md.
2. Execute docs/prompts/05-specification-adversarial-review-prompt.md.
3. Write docs/reviews/01-specification-adversarial-review.md only.
4. Do not revise the specification or start plan stages.
5. Do not mark stages accepted without my approval.
```

---

## Do not

- Treat this handoff as higher authority than Blueprint / Charter / accepted artifacts
- Start **spec-revision** or implementation planning before spec-review is accepted
- Reopen Windows, dotenv secrets, Claude adapters, or demote ty/fnox without a DEC
- Invent acceptance without human + `accepted_commit` in the manifest
- Write the adversarial review in a packaging-only session unless the human
  explicitly overrides fresh-session policy

---

*Replace this file when spec-review is accepted (or when the next next-stage changes).*
