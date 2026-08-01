# HANDOFF — python-foundry

**Purpose:** Resume packet for a **fresh session**. Git artifacts are authority;
this file only says what to do next and what not to re-open.

| Field | Value |
| ----- | ----- |
| **As of** | 2026-08-01 |
| **Branch** | `main` |
| **Verify** | `git log -1 --oneline` · `research-program.toml` |
| **Program** | `active` · rigor `standard` |
| **Done** | discovery, charter, ecosystem, AI-native, architecture (all **accepted**); **synthesis packaging** (`prompt-ready`) |
| **Next** | **`synthesis` research session** — write the definitive specification |

---

## Do next (this is the only work)

### Stage: `synthesis` — Definitive Specification Synthesis

| | |
| - | - |
| **Kind** | chief-architect-synthesis |
| **Status** | `prompt-ready` |
| **Prompt** | `docs/prompts/04-chief-architect-synthesis-prompt.md` |
| **Output** | `docs/specifications/01-definitive-specification.md` |
| **IDs** | REQ-001..REQ-299 |
| **Depends on** | all three research reports — **accepted** |
| **Launch** | `docs/handoffs/synthesis-launch-message.md` |
| **Manifest** | `docs/handoffs/synthesis-attachment-manifest.md` |
| **Validate after** | `docs/handoffs/synthesis-validation-task.md` |

### Research session (prefer fresh chat)

1. Open a **new** agent session.
2. Paste the body of `docs/handoffs/synthesis-launch-message.md` (below the line).
3. Attach the full artifacts listed in the attachment manifest (not digests alone).
4. Agent writes `docs/specifications/01-definitive-specification.md`.
5. Run `research-validate` per the validation task.
6. Human accept → commit → record `accepted_commit` in `research-program.toml`.

**Do not** start `spec-review` until synthesis is accepted.

### Attach for synthesis (full artifacts, not digests alone)

| Path | Why |
| ---- | --- |
| `docs/00-program-blueprint.md` | Locks, scope, success criteria |
| `docs/01-research-charter.md` | Evidence / REQ methodology |
| `docs/reports/01-modern-python-ecosystem.md` | Accepted Core/profiles (v0.2) |
| `docs/reports/02-ai-native-agent-workflow.md` | Accepted agent surface (v0.2) |
| `docs/reports/03-foundry-architecture.md` | Accepted generator architecture (v0.1.1) |
| `docs/prompts/04-chief-architect-synthesis-prompt.md` | Sole mission for the session |
| `docs/handoffs/synthesis-attachment-manifest.md` | Attachment authority list |
| `program/contracts/synthesis.md` | Synthesis behavior |
| `program/contracts/definitive-specification.md` | Spec shape |
| `program/templates/requirement.md` | REQ template |
| `program/contracts/authority-and-precedence.md` | Precedence |
| `AGENTS.md` | Operating rules |

Owner preference: **one stage at a time**.

---

## Load-bearing locks (do not silently undo)

Point to full reports for detail. Synthesis **traces** these into REQs; it does
not re-litigate them without a DEC.

**Ecosystem Core** (`docs/reports/01-…` v0.2): Python ≥3.12 / default 3.13; **uv**
+ lockfile; **src/**; Ruff; **ty** Required; pytest; pre-commit Default; **fnox**
+ **age**; **no `.env` secrets**; GHA; Typer default CLI; profiles `http`,
`hooks-hk`, `data-etl`; command surface REC-013.

**AI-native** (`docs/reports/02-…` v0.2): root **`AGENTS.md` only**; skills under
**`.agents/skills/` only**; MCP default **none**; no Claude adapters; amplify
REC-013; fnox exec secrets.

**Architecture** (`docs/reports/03-…` v0.1.1): planner-led CLI `validate` →
`plan` → `generate`; TOML spec; plan-as-contract; stage → verify → exclusive
place; closed catalog; custom engine (not Copier runtime); GitHub template =
generated snapshot; emit Core + agent surface as invariants.

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

## Paste into a fresh synthesis research session

Use the full launch message in `docs/handoffs/synthesis-launch-message.md`.
Short form if needed:

```text
Resume python-foundry from HANDOFF.md only as a pointer; Git is authority.

Next: synthesis research only (one stage). Package is prompt-ready.

1. Read AGENTS.md, research-program.toml, the synthesis prompt, Blueprint,
   Charter, and accepted reports 01, 02, 03 in full.
2. Follow docs/handoffs/synthesis-launch-message.md and the attachment manifest.
3. Write docs/specifications/01-definitive-specification.md (replace placeholder).
4. Disposition every REC-001..014, 100..112, 200..212 into REQs as needed.
5. Do not start spec-review or mark accepted without my approval.
```

---

## Do not

- Treat this handoff as higher authority than Blueprint / Charter / accepted reports
- Start **spec-review** or implementation planning before synthesis is accepted
- Reopen Windows, dotenv secrets, Claude adapters, or demote ty/fnox without a DEC
- Invent acceptance without human + `accepted_commit` in the manifest
- Write the specification in a packaging-only session unless the human overrides
  fresh-session policy

---

*Replace this file when synthesis is accepted (or when the next next-stage changes).*
