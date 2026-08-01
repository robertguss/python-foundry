# Fresh-Session Launch Message — implementation-plan

Copy everything below the line into a **new** agent session.

---

You are executing **Implementation Plan** (`implementation-plan`) of the
**python-foundry** research program.

The attached files correspond to these authoritative repository artifacts:

1. `docs/00-program-blueprint.md` — Accepted Program Blueprint
2. `docs/01-research-charter.md` — Accepted Research Charter
3. `docs/prompts/07-implementation-plan-prompt.md` — commissioning prompt for this stage
4. `docs/specifications/02-definitive-specification-revised.md` — **Accepted** revised definitive specification v0.2 (**implementation authority**)
5. `docs/reviews/01-specification-adversarial-review.md` — Accepted adversarial review (context only)
6. `AGENTS.md` — agent operating rules
7. `program/contracts/implementation-plan.md` — plan contract (boundaries, required content)
8. `program/templates/phase.md` — phase template
9. `program/templates/milestone.md` — milestone template
10. `program/contracts/authority-and-precedence.md` — precedence ladder
11. `docs/handoffs/implementation-plan-attachment-manifest.md` — attachment manifest

Read every attached artifact completely before beginning. Apply their authority
and precedence rules exactly.

- The **revised definitive specification** is **implementation authority**. Your
  plan is subordinate: sequence delivery; **do not** change architecture or REQs.
- Use revised-spec **PHASE-01..06** and handoff §30 as the starting phase model;
  refine with executable entry/exit criteria.
- Stay at **phases and milestones only** — **no** coding backlog, sprint tickets,
  or agent task packets.
- Produce thin end-to-end capability early; integrate continuously; dogfood
  before broad expansion; schedule spikes (SPK-*) as gates.
- Preserve locks: ty, fnox+age, no dotenv secrets, AGENTS.md-only, no Claude,
  exclusive place, closed catalog, custom engine, generate-time uv.lock, verify
  precedence CLI > TOML > default, optional `generate --plan` bind.
- Residual risks to sequence: ty maturity, fnox/dotenv relapse, lock network cost,
  agents skipping `--plan`, provisional CLI name.
- Plan artifact status: **Proposed — pending plan adversarial review** (not
  delivery authority yet).
- **Do not** start plan-review or product implementation in this session.

Execute the complete task commissioned by
`docs/prompts/07-implementation-plan-prompt.md`.

If this session does not have write access to the local Git repository, do not
treat that as a blocker. Produce the complete standalone Markdown contents
intended for:

`docs/plans/01-implementation-plan.md`

Do not ask clarifying questions unless a true blocker exists under the
commissioning prompt.

Do not begin a downstream stage (including plan adversarial review).

At the end provide:

1. The complete artifact (written to the output path or full Markdown for it).
2. A brief execution summary outside the artifact.
3. Any unmet requirement and why.
4. Any remaining blocker.
