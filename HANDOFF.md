# HANDOFF — python-foundry

**Purpose:** Self-contained resume packet for a **fresh session**. Git-tracked
artifacts are authority; this file tells the next agent **exactly what to do**
and what not to re-open. Prefer reading the full attached paths below over chat
history.

| Field | Value |
| ----- | ----- |
| **As of** | 2026-08-01 |
| **Branch** | `main` |
| **HEAD (acceptance record)** | see `git log -1` after acceptance commit |
| **Verify** | `git log -1 --oneline` · `research-program.toml` · `just check` |
| **Program** | `active` · rigor `standard` · **research stages complete** |
| **Done** | discovery … **plan-revision accepted** (delivery authority `8543c13`) |
| **Next** | **Product implementation** under revised-spec + revised plan — **not** another research stage unless risk-triggered |

---

## Mission (current position)

The **research program** through `plan-revision` is **accepted**. Delivery
sequence authority and product law are frozen:

| Authority | Artifact | Commit |
| --------- | -------- | ------ |
| **Product law** | `docs/specifications/02-definitive-specification-revised.md` v0.2 | `faffbdc` |
| **Delivery sequence** | `docs/plans/02-implementation-plan-revised.md` v0.2 | `8543c13` |

### What to do next (product work)

1. Read **required set** before coding:
   - `docs/plans/02-implementation-plan-revised.md` (delivery authority)
   - `docs/specifications/02-definitive-specification-revised.md` (product law)
   - `docs/00-program-blueprint.md` (locks / non-goals)
   - `docs/01-research-charter.md` (methodology)
   - `AGENTS.md`
2. Start at **PHASE-01** (pure pipeline) unless owner directs otherwise.
3. Honor phase entry/exit criteria, spike gates (SPK-*), progressive milestones
   (MS-003a → MS-DF0 → MS-003b; MS-005 → MS-004), and residual policy (§16 of
   the revised plan).
4. Do **not** reverse product locks (ty, fnox+age, no dotenv secrets,
   AGENTS-only, no Claude adapters, exclusive place, custom engine, closed
   catalog, generate-time lock, verify CLI > TOML > default, optional `--plan`).

### Research program

No further research stages are queued. Second plan-review only if risk-triggered
(phase split/merge, new machinery, or product-law change without DEC). Formal
`DEC-###` for lock changes only.

---

## Authority and precedence (highest first)

1. Accepted `DEC-###` (none under `decisions/` unless present).
2. `docs/00-program-blueprint.md` locks and non-goals.
3. `docs/01-research-charter.md` methodology.
4. **Revised specification v0.2** — product law.
5. **Revised implementation plan v0.2** — delivery sequence authority.
6. Proposed plan / reviews / reports — provenance only.
7. `research-program.toml` — index only.
8. Model preference — lowest.

---

## Stage index (all accepted)

| Stage | Status | Commit |
| ----- | ------ | ------ |
| discovery … spec-revision | accepted | revised-spec v0.2 = product law (`faffbdc`) |
| `implementation-plan` | accepted | proposed plan `ab72895` (not delivery authority) |
| `plan-review` | accepted | review `7032972` · FND-200..205 disposed |
| `plan-revision` | **accepted** | revised plan **`8543c13`** · delivery authority |

---

## Do not

- Re-open plan-revision or invent a new coding backlog as research output
- Treat proposed plan `01-` as delivery authority
- Demote ty/fnox, add dotenv secrets, Claude adapters, Windows, marketplace,
  Copier-as-engine without DEC / Blueprint amendment
- Use chat history as authority over Git-tracked artifacts

---

## Paste-ready short kickoff (product implementation)

```text
Resume python-foundry from HANDOFF.md. Git is authority.

Research stages complete. Product implementation may begin.

1. Read docs/plans/02-implementation-plan-revised.md (delivery authority).
2. Read docs/specifications/02-definitive-specification-revised.md (product law).
3. Read Blueprint, Charter, AGENTS.md.
4. Start PHASE-01 pure pipeline per the revised plan.
5. Do not reverse locks; honor spikes and progressive milestones.
```

---

*Replace this file when product phase gates change the resume position or when
a risk-triggered research amendment is commissioned.*
