# Fresh-Session Launch Message — plan-revision

Copy everything below the line into a **new** agent session.

---

You are executing **Final Revised Implementation Plan** (`plan-revision`) of the
**python-foundry** research program.

The attached files correspond to these authoritative repository artifacts:

1. `docs/00-program-blueprint.md` — Accepted Program Blueprint
2. `docs/01-research-charter.md` — Accepted Research Charter
3. `docs/prompts/09-implementation-plan-revision-prompt.md` — commissioning prompt for this stage
4. `docs/plans/01-implementation-plan.md` — **Accepted stage** proposed plan v0.1 (**base text**; not delivery authority)
5. `docs/reviews/02-implementation-plan-adversarial-review.md` — **Accepted** plan adversarial review (FND-200..205)
6. `docs/specifications/02-definitive-specification-revised.md` — **Accepted** revised definitive specification v0.2 (**implementation authority**)
7. `AGENTS.md` — agent operating rules
8. `program/contracts/implementation-plan.md` — plan boundary + final revised plan rules
9. `program/templates/phase.md` — phase template
10. `program/templates/milestone.md` — milestone template
11. `program/operator/completion-criteria.md` — final implementation handoff contents
12. `program/contracts/authority-and-precedence.md` — precedence ladder
13. `docs/handoffs/plan-revision-attachment-manifest.md` — attachment manifest

Read every attached artifact completely before beginning. Apply their authority
and precedence rules exactly.

- The **Blueprint** locks product shape, non-goals, and success criteria. Do not
  reopen Windows, notebooks, marketplace, framework zoo, or coding backlog as
  program output.
- The **revised definitive specification** is **implementation authority**
  (product law). The plan is **subordinate** — do not reverse product locks or
  rewrite REQs via “plan fixes.”
- The **proposed implementation plan** is your **base text**. Correct it by
  integrating dispositions — do not leave contradictory old sequencing language.
- The **accepted plan adversarial review** is your **finding list**. Disposition
  **every** FND-200..205 (Accepted / Accepted with modification / Rejected /
  Deferred to bounded spike / Not applicable). Silent loss is a defect.
- Review gate was **Conditional**: resolve High findings **FND-200** and
  **FND-201** before claiming unblocked catalog freeze / hybrid readiness as
  delivery authority. Prefer resolution over deferral for High findings.
- Themes: freeze durability vs dogfood; progressive PHASE-04 integration; ty
  timing vs SPK-002; MS-004/005 order; MS-005 observable evidence; residual-accept
  policy honesty.
- **Prefer simplification** over new plan machinery. Preserve strengths: thin
  E2E at MS-002, linear phases, spike gates, Must REQ table, no coding backlog.
- Remain at **phase/milestone** granularity only.
- Artifact status must be honest: **`Accepted — delivery authority`** only if
  blockers are cleared; else **`Proposed — delivery blocked`** with blockers
  listed.
- Include a complete **Final Implementation Handoff** per completion-criteria.
- **Do not** edit the proposed `01-` plan, the review, or the revised
  specification. **Do not** start product implementation in this session.

Execute the complete task commissioned by
`docs/prompts/09-implementation-plan-revision-prompt.md`.

If this session does not have write access to the local Git repository, do not
treat that as a blocker. Produce the complete standalone Markdown contents
intended for:

`docs/plans/02-implementation-plan-revised.md`

Do not ask clarifying questions unless a true blocker exists under the
commissioning prompt.

Do not begin a downstream stage (including product implementation).

At the end provide:

1. The complete artifact (written to the output path or full Markdown for it).
2. A brief execution summary outside the artifact.
3. Any unmet requirement and why.
4. Any remaining blocker.
