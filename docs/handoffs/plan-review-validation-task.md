# Validate Implementation Plan Adversarial Review (plan-review)

## When

After `docs/reviews/02-implementation-plan-adversarial-review.md` exists
(non-placeholder) and before human acceptance.

## Read

1. `README.md`
2. `AGENTS.md`
3. `research-program.toml`
4. `docs/00-program-blueprint.md`
5. `docs/01-research-charter.md`
6. `docs/prompts/08-implementation-plan-review-prompt.md`
7. `docs/handoffs/plan-review-attachment-manifest.md`
8. `docs/plans/01-implementation-plan.md` (subject)
9. `docs/specifications/02-definitive-specification-revised.md` (implementation authority)
10. `program/contracts/adversarial-review.md`
11. `program/templates/finding.md`
12. `program/contracts/implementation-plan.md`
13. `docs/reviews/02-implementation-plan-adversarial-review.md`

Use the `research-validate` skill if available.

## Validate

- Required review sections present (metadata, scope/method, executive assessment,
  findings, sequencing/integration issues, gate recommendation, additional-round
  note, finding index, completion checklist)
- Artifact metadata and **actual review date**
- Status is **not** `Placeholder — not accepted`
- Identifier uniqueness and ranges:
  - FND-200..FND-399 only for new findings
  - No use of specification-review range FND-001..FND-199 for new plan findings
  - No silent ID reuse
- Each finding has template-critical fields: severity, confidence, problem,
  evidence, failure scenario, impact, required correction (at minimum)
- Severity values only: Critical | High | Medium | Low
- Implementation gate present: Open | Conditional | Blocked, with rationale
  consistent with Critical/High findings
- Additional review round recommendation present (yes/no + conditions)
- Finding index table covers all findings
- No feature ideation disguised as defects (spot-check)
- Product locks not silently reversed as “required correction” that undoes
  ty/fnox/AGENTS-only/no-Claude/exclusive-place/custom-engine without DEC path
- Review attacks **sequencing** more than product redesign (spot-check)
- Plan file and revised specification **unchanged** by the review stage
- Allowed file scope (primary write is the review path)
- No coding backlog introduced in the review
- Portable citations / section-PHASE-MS-REQ references where claims need them
- Completion checklist truthfulness
- Manifest status transition readiness (`awaiting-validation` → human accept)
- Git diff limited to the review (and any explicitly allowed paths such as a
  validation report)

## Rules

- Do not fabricate missing findings or invent severities for unread content.
- Fix **mechanical** defects only (headings, metadata, broken ID formatting,
  checklist typos, missing section labels).
- Report substantive defects; set stage to `requires-revision` if needed.
- Do not mark `accepted` without human approval and commit hash.

## Recommended commit messages

Prompt install / packaging (this package):

```text
docs: add implementation plan review prompt
```

After review accepted by human:

```text
docs: add implementation plan adversarial review
```

Record `accepted_commit` on stage `plan-review` in `research-program.toml` only
after human acceptance.
