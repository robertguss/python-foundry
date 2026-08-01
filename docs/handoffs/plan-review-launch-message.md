# Fresh-Session Launch Message — plan-review

Copy everything below the line into a **new** agent session.

---

You are executing **Implementation Plan Adversarial Review** (`plan-review`) of
the **python-foundry** research program.

The attached files correspond to these authoritative repository artifacts:

1. `docs/00-program-blueprint.md` — Accepted Program Blueprint
2. `docs/01-research-charter.md` — Accepted Research Charter
3. `docs/prompts/08-implementation-plan-review-prompt.md` — commissioning prompt for this stage
4. `docs/plans/01-implementation-plan.md` — **Accepted stage** proposed plan v0.1 (**attack surface**; not delivery authority)
5. `docs/specifications/02-definitive-specification-revised.md` — **Accepted** revised definitive specification v0.2 (**implementation authority**)
6. `AGENTS.md` — agent operating rules
7. `program/contracts/adversarial-review.md` — review contract (posture, severity, plan-review attacks)
8. `program/templates/finding.md` — finding template
9. `program/contracts/implementation-plan.md` — plan shape and boundary
10. `program/contracts/authority-and-precedence.md` — precedence ladder
11. `docs/handoffs/plan-review-attachment-manifest.md` — attachment manifest

Read every attached artifact completely before beginning. Apply their authority
and precedence rules exactly.

- The **Blueprint** locks product shape, non-goals, and success criteria. Do not
  reopen Windows, notebooks, marketplace, framework zoo, or coding backlog as
  product scope.
- The **Charter** governs evidence vocabulary, quality bar, and anti-patterns.
- The **revised definitive specification** is **implementation authority**. The
  plan must remain subordinate; do not reverse product locks via “findings.”
- The **proposed implementation plan** is your **attack surface**. Attack
  sequencing: circular dependencies, missing prerequisites, unprovable exit
  criteria, late risk discovery, deferred integration/dogfooding, overlarge
  phases, milestones without integration evidence, and reinterpretation of
  architecture or REQs.
- Produce findings **FND-200..FND-399** as justified (strong few, not a quota).
  Use the finding template. Prefer concrete failure scenarios and required
  **plan** corrections (Proposed Plan Diff).
- **Do not** revise the plan, revise the specification, write a coding backlog,
  or start product implementation.
- **Do not** treat preference as defect.
- Artifact status for the review should be complete pending validation/acceptance
  (not Placeholder).

Execute the complete task commissioned by
`docs/prompts/08-implementation-plan-review-prompt.md`.

If this session does not have write access to the local Git repository, do not
treat that as a blocker. Produce the complete standalone Markdown contents
intended for:

`docs/reviews/02-implementation-plan-adversarial-review.md`

Do not ask clarifying questions unless a true blocker exists under the
commissioning prompt.

Do not begin a downstream stage (including plan-revision or product
implementation).

At the end provide:

1. The complete artifact (written to the output path or full Markdown for it).
2. A brief execution summary outside the artifact.
3. Any unmet requirement and why.
4. Any remaining blocker.
