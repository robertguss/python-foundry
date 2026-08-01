# Fresh-Session Launch Message — synthesis

Copy everything below the line into a **new** agent session.

---

You are executing **Definitive Specification Synthesis** (`synthesis`) of the
**python-foundry** research program.

The attached files correspond to these authoritative repository artifacts:

1. `docs/00-program-blueprint.md` — Accepted Program Blueprint (locked constraints and graph)
2. `docs/01-research-charter.md` — Accepted Research Charter (evidence and methodology)
3. `docs/prompts/04-chief-architect-synthesis-prompt.md` — commissioning prompt for this stage
4. `docs/reports/01-modern-python-ecosystem.md` — **Accepted** ecosystem report v0.2 (Core/profile locks)
5. `docs/reports/02-ai-native-agent-workflow.md` — **Accepted** AI-native report v0.2 (agent surface locks)
6. `docs/reports/03-foundry-architecture.md` — **Accepted** architecture report v0.1.1 (generator locks)
7. `AGENTS.md` — agent operating rules
8. `program/contracts/synthesis.md` — synthesis contract (decision-making, REC dispositions)
9. `program/contracts/definitive-specification.md` — required specification structure
10. `program/templates/requirement.md` — requirement template
11. `program/contracts/authority-and-precedence.md` — precedence ladder
12. `docs/handoffs/synthesis-attachment-manifest.md` — attachment manifest

Read every attached artifact completely before beginning. Apply their authority
and precedence rules exactly.

- The **Blueprint** locks product shape (hybrid generator + Core + template
  surface), non-goals, OS/Python posture, and success criteria. Do not reopen
  non-goals (Windows, notebooks, marketplace, framework zoo, coding backlog as
  program output).
- The **Charter** governs evidence vocabulary, quality bar, and anti-patterns.
  Synthesis decides; it does not invent fake citations.
- The **accepted ecosystem report (v0.2)** locks Generated Project Core tooling
  and profiles. Inherit especially:
  - **ty** Required Core type checker
  - **fnox** Required Core secrets with provider **age**
  - **no `.env` / dotenv secret storage**
  - REC-013 command surface; REC-014 Core/profile membership
  - Do **not** demote ty/fnox or reintroduce dotenv secrets.
- The **accepted AI-native report (v0.2)** locks agent surfaces. Inherit especially:
  - Root **`AGENTS.md` only**; skills under **`.agents/skills/` only**
  - **No** `CLAUDE.md` / `.claude/` Core emit
  - MCP default **none**
  - Amplify REC-013; fnox exec secrets protocol
- The **accepted architecture report (v0.1.1)** locks generator architecture.
  Inherit especially:
  - Planner-led CLI: **`validate` → `plan` → `generate`**
  - **TOML** Project Spec; **plan-as-contract**
  - Stage → verify → **exclusive place**; closed catalog; **custom engine**
    (not Copier runtime)
  - GitHub template = **generated snapshot** from catalog SoT
  - Emit Core + AI-native surfaces as **invariants**
  - go-foundry is prior art (Adopt/Adapt/Reject already in REC-210)
- The **commissioning prompt** is your sole mission document for this stage.
- Synthesis is **decision-making**: disposition **every** REC-001..014,
  REC-100..112, REC-200..212; allocate **REQ-001..REQ-299** as needed; produce a
  **standalone** proposed definitive specification.
- Artifact status must be: **Proposed — pending adversarial review**.
- Adversarial review, specification revision, and implementation planning are
  **out of scope** for this session.

Execute the complete task commissioned by
`docs/prompts/04-chief-architect-synthesis-prompt.md`.

If this session does not have write access to the local Git repository, do not
treat that as a blocker. Produce the complete standalone Markdown contents
intended for:

`docs/specifications/01-definitive-specification.md`

Do not ask clarifying questions unless a true blocker exists under the
commissioning prompt.

Do not begin a downstream stage (including specification adversarial review,
revision, or implementation planning).

At the end provide:

1. The complete artifact (written to the output path or full Markdown for it).
2. A brief execution summary outside the artifact.
3. Any unmet requirement and why.
4. Any remaining blocker.
