# Fresh-Session Launch Message — research-ai-native

Copy everything below the line into a **new** agent session.

---

You are executing **AI-Native Repository & Agent Workflow**
(`research-ai-native`) of the **python-foundry** research program.

The attached files correspond to these authoritative repository artifacts:

1. `docs/00-program-blueprint.md` — Accepted Program Blueprint (locked constraints and graph)
2. `docs/01-research-charter.md` — Accepted Research Charter (evidence and methodology)
3. `docs/prompts/02-ai-native-agent-workflow-prompt.md` — commissioning prompt for this stage
4. `docs/reports/01-modern-python-ecosystem.md` — **Accepted** ecosystem report v0.2 (Core locks)
5. `AGENTS.md` — agent operating rules
6. `program/contracts/focused-research-report.md` — required report structure
7. `program/templates/recommendation.md` — recommendation template
8. `program/contracts/evidence-model.md` — evidence classes and ledger
9. `program/contracts/evidence-spike.md` — spike protocol
10. `docs/handoffs/research-ai-native-attachment-manifest.md` — attachment manifest

Read every attached artifact completely before beginning. Apply their authority
and precedence rules exactly.

- The **Blueprint** locks product scope, non-goals (including **closed, curated**
  agent tooling — no unlimited MCP/skill catalogs), OS/Python posture, and
  success criteria. Do not reopen non-goals.
- The **Charter** governs evidence, citations, confidence, REC/RSK/OQ format,
  spikes, and anti-patterns.
- The **accepted ecosystem report (v0.2)** locks Generated Project Core tooling
  and the agent-facing command surface. Inherit especially:
  - **ty** Required Core type checker
  - **fnox** Required Core secrets with provider **age**
  - **no `.env` / dotenv secret storage**
  - REC-013: `uv sync` / `uv run …` / `fnox exec -- …`
  - Do **not** re-select uv/ruff/ty/pytest/fnox or reintroduce dotenv secrets.
- The **commissioning prompt** is your sole mission document for this stage.
- Architecture, synthesis, and implementation planning are **out of scope**.

Execute the complete task commissioned by
`docs/prompts/02-ai-native-agent-workflow-prompt.md`.

If this session does not have write access to the local Git repository, do not
treat that as a blocker. Produce the complete standalone Markdown contents
intended for:

`docs/reports/02-ai-native-agent-workflow.md`

(and optional `docs/evidence/SPK-05*-*.md` if you run spikes).

Do not ask clarifying questions unless a true blocker exists under the
commissioning prompt.

Do not begin a downstream stage (including foundry architecture, synthesis,
spec review, or implementation).

At the end provide:

1. The complete artifact (written to the output path or full Markdown for it).
2. A brief execution summary outside the artifact.
3. Any unmet requirement and why.
4. Any remaining blocker.
