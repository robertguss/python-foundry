# Validate Final Revised Implementation Plan (plan-revision)

## When

After `docs/plans/02-implementation-plan-revised.md` exists (non-placeholder)
and before human acceptance.

## Read

1. `README.md`
2. `AGENTS.md`
3. `research-program.toml`
4. `docs/00-program-blueprint.md`
5. `docs/01-research-charter.md`
6. `docs/prompts/09-implementation-plan-revision-prompt.md`
7. `docs/handoffs/plan-revision-attachment-manifest.md`
8. `docs/plans/01-implementation-plan.md` (base)
9. `docs/reviews/02-implementation-plan-adversarial-review.md` (FND-200..205)
10. `docs/specifications/02-definitive-specification-revised.md` (implementation authority)
11. `program/contracts/implementation-plan.md`
12. `program/templates/phase.md`
13. `program/templates/milestone.md`
14. `program/operator/completion-criteria.md`
15. `docs/plans/02-implementation-plan-revised.md`

Use the `research-validate` skill if available.

## Validate

- Required sections present (revision front matter + full plan body + final
  implementation handoff + checklist)
- Artifact metadata and **actual revision date**
- Status is **not** Placeholder; status is exactly one of:
  - `Accepted — delivery authority`, or
  - `Proposed — delivery blocked` (blockers explicit)
- **Finding Disposition Ledger complete** for FND-200..FND-205
  - Each row exactly one allowed disposition
  - No silent FND loss
- Accepted corrections appear **integrated in body** (spot-check High findings
  FND-200..201 against phases/milestones/dogfood/hybrid — not ledger-only)
- Plan remains **subordinate** to revised-spec v0.2 (no REQ/architecture rewrite)
- Product locks preserved (ty, fnox+age, no dotenv secrets, AGENTS-only, no Claude,
  exclusive place, custom engine, closed catalog, generate-time lock, verify
  precedence, optional `--plan` bind)
- Blueprint non-goals preserved
- Phases/milestones only — **no** coding backlog or task packets
- Executable entry/exit criteria; no circular depends_on; no post-exit freeze fiction
- Early thin E2E path present or honestly restructured with rationale
- Spikes as gates; dogfood/hybrid sequencing consistent with dispositions
- Residual / residual-accept policy honest if residual language remains
- Testing, security, ops by phase
- Rollback/reconsideration triggers present
- Must REQ traceability present
- Final Implementation Handoff complete per completion-criteria (authoritative
  artifacts; whether implementation may begin; first phase; spikes; vertical
  slice; dogfood; evidence; risks; reversible decisions; blockers; read set)
- Standalone character
- Proposed plan (`01-…`) and review files **unchanged** by this stage
- Revised specification **unchanged** by this stage
- Allowed file scope (primary write is revised plan path)
- Completion checklist truthfulness
- Manifest status transition readiness (`awaiting-validation` → human accept)
- Git diff limited to the revised plan (and any explicitly allowed paths such as
  a validation report)

## Rules

- Do not fabricate missing dispositions or invent research.
- Fix **mechanical** defects only (headings, metadata, broken ID formatting,
  checklist typos, missing section labels).
- Report substantive defects; set stage to `requires-revision` if needed.
- Do not mark `accepted` without human approval and commit hash.

## Recommended commit messages

Prompt install / packaging (this package):

```text
docs: add implementation plan revision prompt
```

After revised plan accepted by human:

```text
docs: publish final revised implementation plan
```

Record `accepted_commit` on stage `plan-revision` in `research-program.toml`
only after human acceptance.
