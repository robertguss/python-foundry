# Fresh-Session Launch Message — research-foundry-architecture

Copy everything below the line into a **new** agent session.

---

You are executing **Foundry Architecture**
(`research-foundry-architecture`) of the **python-foundry** research program.

The attached files correspond to these authoritative repository artifacts:

1. `docs/00-program-blueprint.md` — Accepted Program Blueprint (locked constraints and graph)
2. `docs/01-research-charter.md` — Accepted Research Charter (evidence and methodology)
3. `docs/prompts/03-foundry-architecture-prompt.md` — commissioning prompt for this stage
4. `docs/reports/01-modern-python-ecosystem.md` — **Accepted** ecosystem report v0.2 (Core/profile locks)
5. `docs/reports/02-ai-native-agent-workflow.md` — **Accepted** AI-native report v0.2 (agent surface locks)
6. `AGENTS.md` — agent operating rules
7. `program/contracts/focused-research-report.md` — required report structure
8. `program/templates/recommendation.md` — recommendation template
9. `program/contracts/evidence-model.md` — evidence classes and ledger
10. `program/contracts/evidence-spike.md` — spike protocol
11. `docs/handoffs/research-foundry-architecture-attachment-manifest.md` — attachment manifest

Read every attached artifact completely before beginning. Apply their authority
and precedence rules exactly.

- The **Blueprint** locks product shape (hybrid generator + Core + template
  surface), non-goals, OS/Python posture, and success criteria. Do not reopen
  non-goals. Address Blueprint uncertainties on spec format, generation engine,
  and go-foundry transfer.
- The **Charter** governs evidence, citations, confidence, REC/RSK/OQ format,
  spikes, and anti-patterns.
- The **accepted ecosystem report (v0.2)** locks Generated Project Core tooling
  and profiles. Inherit especially:
  - **ty** Required Core type checker
  - **fnox** Required Core secrets with provider **age**
  - **no `.env` / dotenv secret storage**
  - REC-013 command surface; REC-014 Core/profile membership
  - Do **not** re-select uv/ruff/ty/pytest/fnox or reintroduce dotenv secrets.
  Architecture **emits** these locks.
- The **accepted AI-native report (v0.2)** locks agent surfaces. Inherit especially:
  - Root **`AGENTS.md` only**; skills under **`.agents/skills/` only**
  - **No** `CLAUDE.md` / `.claude/` Core emit
  - MCP default **none**
  - Amplify REC-013; fnox exec secrets protocol
  Architecture **emits** these locks.
- **go-foundry** is prior art only (adapt, do not copy blindly).
- The **commissioning prompt** is your sole mission document for this stage.
- Synthesis, adversarial review, and implementation planning are **out of scope**.

Execute the complete task commissioned by
`docs/prompts/03-foundry-architecture-prompt.md`.

If this session does not have write access to the local Git repository, do not
treat that as a blocker. Produce the complete standalone Markdown contents
intended for:

`docs/reports/03-foundry-architecture.md`

(and optional `docs/evidence/SPK-10*-*.md` if you run spikes).

Do not ask clarifying questions unless a true blocker exists under the
commissioning prompt.

Do not begin a downstream stage (including synthesis, spec review, or
implementation planning).

At the end provide:

1. The complete artifact (written to the output path or full Markdown for it).
2. A brief execution summary outside the artifact.
3. Any unmet requirement and why.
4. Any remaining blocker.
