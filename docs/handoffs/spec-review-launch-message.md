# Fresh-Session Launch Message — spec-review

Copy everything below the line into a **new** agent session.

---

You are executing **Specification Adversarial Review** (`spec-review`) of the
**python-foundry** research program.

The attached files correspond to these authoritative repository artifacts:

1. `docs/00-program-blueprint.md` — Accepted Program Blueprint (locked constraints and graph)
2. `docs/01-research-charter.md` — Accepted Research Charter (evidence and methodology)
3. `docs/prompts/05-specification-adversarial-review-prompt.md` — commissioning prompt for this stage
4. `docs/specifications/01-definitive-specification.md` — **Accepted proposed** definitive specification (subject under attack)
5. `docs/reports/01-modern-python-ecosystem.md` — **Accepted** ecosystem report v0.2 (Core locks / provenance)
6. `docs/reports/02-ai-native-agent-workflow.md` — **Accepted** AI-native report v0.2 (agent surface locks / provenance)
7. `docs/reports/03-foundry-architecture.md` — **Accepted** architecture report v0.1.1 (generator locks / provenance)
8. `AGENTS.md` — agent operating rules
9. `program/contracts/adversarial-review.md` — adversarial review contract (posture, severity)
10. `program/templates/finding.md` — finding template
11. `program/contracts/authority-and-precedence.md` — precedence ladder
12. `program/contracts/definitive-specification.md` — specification shape for consistency checks
13. `docs/handoffs/spec-review-attachment-manifest.md` — attachment manifest

Read every attached artifact completely before beginning. Apply their authority
and precedence rules exactly.

- The **Blueprint** locks product shape, non-goals, OS/Python posture, and success
  criteria. Do not reopen non-goals (Windows, notebooks, marketplace, framework
  zoo, coding backlog as program output) as product scope.
- The **Charter** governs evidence vocabulary, quality bar, and anti-patterns.
- The **proposed definitive specification** is your **attack surface**. Synthesis
  is accepted as a proposed artifact; it is **not** yet implementation authority.
  Attack contradictions, missing REQs, weak verification, unsafe semantics,
  non-total workflows, over-engineering, and silent expansion paths.
- The **accepted reports** are for **provenance and lock checks** — confirm the
  specification correctly traces locks; do not re-run tool selection research.
- Inherit especially (locks are not defects by preference):
  - **ty** Required; **fnox** + **age** Required; **no** dotenv secrets
  - Root **`AGENTS.md` only**; skills under **`.agents/skills/` only**; MCP none;
    no Claude adapters
  - **`validate` → `plan` → `generate`**; TOML spec; plan-as-contract; exclusive
    place; closed catalog; custom engine; template = generated snapshot
- The **commissioning prompt** is your sole mission document for this stage.
- Produce findings **FND-001..FND-199** as justified (strong few, not a quota).
  Use the finding template. Prefer concrete failure scenarios and required
  corrections.
- **Do not** revise the specification, write an implementation plan, or add
  features disguised as findings.
- **Do not** treat preference as defect.
- Artifact status for the review should be complete pending validation/acceptance
  (not Placeholder).

Execute the complete task commissioned by
`docs/prompts/05-specification-adversarial-review-prompt.md`.

If this session does not have write access to the local Git repository, do not
treat that as a blocker. Produce the complete standalone Markdown contents
intended for:

`docs/reviews/01-specification-adversarial-review.md`

Do not ask clarifying questions unless a true blocker exists under the
commissioning prompt.

Do not begin a downstream stage (including specification revision or
implementation planning).

At the end provide:

1. The complete artifact (written to the output path or full Markdown for it).
2. A brief execution summary outside the artifact.
3. Any unmet requirement and why.
4. Any remaining blocker.
