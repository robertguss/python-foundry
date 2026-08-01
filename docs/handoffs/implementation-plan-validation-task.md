# Validate Implementation Plan (implementation-plan)

## When

After `docs/plans/01-implementation-plan.md` exists (non-placeholder) and before
human acceptance.

## Read

1. `README.md`
2. `AGENTS.md`
3. `research-program.toml`
4. `docs/00-program-blueprint.md`
5. `docs/01-research-charter.md`
6. `docs/prompts/07-implementation-plan-prompt.md`
7. `docs/handoffs/implementation-plan-attachment-manifest.md`
8. `docs/specifications/02-definitive-specification-revised.md` (authority)
9. `program/contracts/implementation-plan.md`
10. `program/templates/phase.md`
11. `program/templates/milestone.md`
12. `docs/plans/01-implementation-plan.md`

Use the `research-validate` skill if available.

## Validate

- Required plan sections present (metadata through definition of plan completion)
- Artifact metadata and **actual plan date**
- Status is **not** Placeholder; not premature `Accepted — delivery authority`
  (should be proposed pending plan review)
- Subordinate to revised specification (spot-check: no contradictory architecture
  or lock undos)
- Phases/milestones only — **no** granular coding backlog or task packets
- Each phase has executable entry and exit criteria (observable evidence)
- Dependency graph present; no circular phase depends_on
- Early thin end-to-end capability (not infrastructure-only forever)
- Spikes/dogfooding/hybrid template sequencing present
- Testing, security, ops addressed by phase
- Rollback/reconsideration triggers present
- Requirement-to-phase traceability covers Must REQs (or justified sampling with
  explicit completeness claim)
- Residual risks from revised spec sequenced (ty, fnox, lock, plan-bind)
- Blueprint non-goals preserved
- Allowed file scope (primary write is plan path)
- Revised specification **unchanged** by this stage
- Completion checklist truthfulness
- Manifest status transition readiness (`awaiting-validation` → human accept)

## Rules

- Do not invent missing phases or rewrite the specification.
- Fix **mechanical** defects only.
- Report substantive defects; set stage to `requires-revision` if needed.
- Do not mark `accepted` without human approval and commit hash.

## Recommended commit messages

Prompt install / packaging (this package):

```text
docs: add implementation plan prompt
```

After plan accepted by human:

```text
docs: add implementation plan
```

Record `accepted_commit` on stage `implementation-plan` only after human
acceptance.
