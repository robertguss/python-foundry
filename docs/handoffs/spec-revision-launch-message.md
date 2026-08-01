# Fresh-Session Launch Message — spec-revision

Copy everything below the line into a **new** agent session.

---

You are executing **Revised Definitive Specification** (`spec-revision`) of the
**python-foundry** research program.

The attached files correspond to these authoritative repository artifacts:

1. `docs/00-program-blueprint.md` — Accepted Program Blueprint (locked constraints and graph)
2. `docs/01-research-charter.md` — Accepted Research Charter (evidence and methodology)
3. `docs/prompts/06-specification-revision-prompt.md` — commissioning prompt for this stage
4. `docs/specifications/01-definitive-specification.md` — **Accepted proposed** definitive specification (base text)
5. `docs/reviews/01-specification-adversarial-review.md` — **Accepted** adversarial review (FND-001..012)
6. `docs/reports/01-modern-python-ecosystem.md` — **Accepted** ecosystem report v0.2
7. `docs/reports/02-ai-native-agent-workflow.md` — **Accepted** AI-native report v0.2
8. `docs/reports/03-foundry-architecture.md` — **Accepted** architecture report v0.1.1
9. `AGENTS.md` — agent operating rules
10. `program/contracts/definitive-specification.md` — specification + revision contract
11. `program/templates/requirement.md` — requirement template
12. `program/contracts/authority-and-precedence.md` — precedence ladder
13. `docs/handoffs/spec-revision-attachment-manifest.md` — attachment manifest

Read every attached artifact completely before beginning. Apply their authority
and precedence rules exactly.

- The **Blueprint** locks product shape, non-goals, and success criteria. Do not
  reopen Windows, notebooks, marketplace, framework zoo, or coding backlog as
  program output.
- The **proposed specification** is your **base text**. Correct it by integrating
  dispositions — do not leave contradictory old language.
- The **accepted adversarial review** is your **finding list**. Disposition
  **every** FND-001..012 (Accepted / Accepted with modification / Rejected /
  Deferred to bounded spike / Not applicable). Silent loss is a defect.
- Review gate was **Conditional**: resolve High findings FND-001..004 before
  claiming unblocked generate/emit freeze. Prefer resolution over deferral for
  High findings.
- **Prefer simplification** over new machinery. Preserve strengths: closed Core,
  exclusive place, plan-as-contract honesty, REC ledger, hybrid single SoT.
- Inherit locks: **ty** Required; **fnox+age**; no dotenv secrets; AGENTS.md +
  `.agents/` only; MCP none; no Claude; `validate` → `plan` → `generate`;
  exclusive place; closed catalog; custom engine; template = generated snapshot.
- The **commissioning prompt** is your sole mission document for this stage.
- Output a **standalone** revised specification at the required path. Artifact
  status must be honest: **`Accepted — implementation authority`** only if
  blockers are cleared; else **`Proposed — implementation blocked`** with
  blockers listed.
- **Do not** edit the proposed `01-` spec, the review, or start implementation
  planning in this session.

Execute the complete task commissioned by
`docs/prompts/06-specification-revision-prompt.md`.

If this session does not have write access to the local Git repository, do not
treat that as a blocker. Produce the complete standalone Markdown contents
intended for:

`docs/specifications/02-definitive-specification-revised.md`

Do not ask clarifying questions unless a true blocker exists under the
commissioning prompt.

Do not begin a downstream stage (including implementation planning).

At the end provide:

1. The complete artifact (written to the output path or full Markdown for it).
2. A brief execution summary outside the artifact.
3. Any unmet requirement and why.
4. Any remaining blocker.
