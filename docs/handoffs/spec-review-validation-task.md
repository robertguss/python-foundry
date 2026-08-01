# Validate Specification Adversarial Review (spec-review)

## When

After `docs/reviews/01-specification-adversarial-review.md` exists
(non-placeholder) and before human acceptance.

## Read

1. `README.md`
2. `AGENTS.md`
3. `research-program.toml`
4. `docs/00-program-blueprint.md`
5. `docs/01-research-charter.md`
6. `docs/prompts/05-specification-adversarial-review-prompt.md`
7. `docs/handoffs/spec-review-attachment-manifest.md`
8. `docs/specifications/01-definitive-specification.md` (subject)
9. `docs/reports/01-modern-python-ecosystem.md` (lock provenance as needed)
10. `docs/reports/02-ai-native-agent-workflow.md` (lock provenance as needed)
11. `docs/reports/03-foundry-architecture.md` (lock provenance as needed)
12. `program/contracts/adversarial-review.md`
13. `program/templates/finding.md`
14. `docs/reviews/01-specification-adversarial-review.md`

Use the `research-validate` skill if available.

## Validate

- Required review sections present (metadata, scope/method, executive assessment,
  findings, cross-cutting issues, gate recommendation, additional-round note,
  finding index, completion checklist)
- Artifact metadata and **actual review date**
- Status is **not** `Placeholder — not accepted`
- Identifier uniqueness and ranges:
  - FND-001..FND-199 only for new findings
  - No use of plan-review range FND-200..FND-399
  - No silent ID reuse
- Each finding has template-critical fields: severity, confidence, problem,
  evidence, failure scenario, impact, required correction (at minimum)
- Severity values only: Critical | High | Medium | Low
- Implementation gate present: Open | Conditional | Blocked, with rationale
  consistent with Critical/High findings
- Additional review round recommendation present (yes/no + conditions)
- Finding index table covers all findings
- No feature ideation disguised as defects (spot-check)
- Locks not silently reversed as “required correction” that undoes ty/fnox/
  AGENTS-only/no-Claude/exclusive-place/custom-engine without framing as DEC
  path (report if correction demands scope reversal without residual-risk
  framing)
- Specification file **unchanged** by the review stage (diff should not rewrite
  the proposed specification)
- Allowed file scope (primary write is the review path)
- Portable citations / section-REQ references where claims need them
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

Prompt install / packaging (this package — if not already committed):

```text
docs: add specification adversarial review prompt
```

After review accepted by human:

```text
docs: add specification adversarial review
```

Record `accepted_commit` on stage `spec-review` in `research-program.toml` only
after human acceptance.
