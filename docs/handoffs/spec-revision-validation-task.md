# Validate Revised Definitive Specification (spec-revision)

## When

After `docs/specifications/02-definitive-specification-revised.md` exists
(non-placeholder) and before human acceptance.

## Read

1. `README.md`
2. `AGENTS.md`
3. `research-program.toml`
4. `docs/00-program-blueprint.md`
5. `docs/01-research-charter.md`
6. `docs/prompts/06-specification-revision-prompt.md`
7. `docs/handoffs/spec-revision-attachment-manifest.md`
8. `docs/specifications/01-definitive-specification.md` (base)
9. `docs/reviews/01-specification-adversarial-review.md` (FND-001..012)
10. `docs/reports/01-modern-python-ecosystem.md` (locks as needed)
11. `docs/reports/02-ai-native-agent-workflow.md` (locks as needed)
12. `docs/reports/03-foundry-architecture.md` (locks as needed)
13. `program/contracts/definitive-specification.md`
14. `program/templates/requirement.md`
15. `docs/specifications/02-definitive-specification-revised.md`

Use the `research-validate` skill if available.

## Validate

- Required sections present (revision front matter + full software-first body +
  handoff + checklist)
- Artifact metadata and **actual revision date**
- Status is **not** Placeholder; status is exactly one of:
  - `Accepted — implementation authority`, or
  - `Proposed — implementation blocked` (blockers explicit)
- **Finding Disposition Ledger complete** for FND-001..FND-012
  - Each row exactly one allowed disposition
  - No silent FND loss
- Integrated Correction Ledger present
- Preserved Strengths present
- Accepted corrections appear **integrated in body** (spot-check High findings
  FND-001..004 against architecture/REQ sections — not ledger-only)
- REQ identifier discipline:
  - Range REQ-001..REQ-299
  - Stable IDs retained where subject unchanged (no silent renumber of old REQs)
  - New IDs only from previously unused numbers
- Must REQs have verification paths
- Traceability updated for normative REQs
- REC disposition ledger carried (or honest deltas noted)
- Risk register / open questions / deferred / rejected updated for residuals
- Blueprint non-goals preserved
- Ecosystem Core locks respected (ty, fnox+age, no dotenv secrets, REC-013/014)
- AI-native locks respected (AGENTS.md + `.agents/` only; MCP none; no Claude)
- Architecture locks respected (validate/plan/generate; TOML; plan-as-contract
  honesty; exclusive place; closed catalog; custom engine; template snapshot)
- High-level phases present; **no** granular coding backlog
- Standalone character
- Updated implementation handoff present
- Proposed spec (`01-…`) and review files **unchanged** by this stage
- Allowed file scope (primary write is revised specification path)
- Completion checklist truthfulness
- Manifest status transition readiness (`awaiting-validation` → human accept)
- Git diff limited to the revised specification (and any explicitly allowed paths
  such as a validation report)

## Rules

- Do not fabricate missing dispositions or invent research.
- Fix **mechanical** defects only (headings, metadata, broken ID formatting,
  checklist typos, missing section labels).
- Report substantive defects; set stage to `requires-revision` if needed.
- Do not mark `accepted` without human approval and commit hash.

## Recommended commit messages

Prompt install / packaging (this package — if not already committed):

```text
docs: add specification revision prompt
```

After revised specification accepted by human:

```text
docs: publish revised definitive specification
```

Record `accepted_commit` on stage `spec-revision` in `research-program.toml`
only after human acceptance.
