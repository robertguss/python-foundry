# Attachment Manifest — research-ai-native

## Stage

| Field | Value |
| ----- | ----- |
| Stage ID | `research-ai-native` |
| Name | AI-Native Repository & Agent Workflow |
| Prompt | `docs/prompts/02-ai-native-agent-workflow-prompt.md` |
| Output | `docs/reports/02-ai-native-agent-workflow.md` |
| Status at package time | `prompt-ready` (after prompt install) |

## Required Full Artifacts

1. `docs/00-program-blueprint.md` — locked scope, graph, AI-native stage mission, non-goals
2. `docs/01-research-charter.md` — evidence rules, REC format, confidence, anti-patterns
3. `docs/prompts/02-ai-native-agent-workflow-prompt.md` — commissioning prompt (sole stage mission)
4. `docs/reports/01-modern-python-ecosystem.md` — **Accepted v0.2 full report** (Core locks: uv/ruff/ty/pytest/fnox+age, no dotenv secrets, REC-013 command surface)
5. `AGENTS.md` — repository operating rules for agents
6. `program/contracts/focused-research-report.md` — required report sections
7. `program/templates/recommendation.md` — REC write-up shape
8. `program/contracts/evidence-model.md` — claim classes and ledger fields
9. `program/contracts/evidence-spike.md` — when/how to spike

## Required Decision Records

- None at package time (only `decisions/README.md` exists). If any `decisions/DEC-*.md` is accepted before launch, attach it in full.

## Required Handoff Digests

- None required separately: the **full** ecosystem report is attached (preferred over digest-only). The ecosystem Handoff Digest (§17) is inside that report and must be read; it explicitly names AI-native handoff needs (ty LSP, fnox skills, forbid dotenv secrets, REC-013).

## Explicitly Excluded Artifacts

| Path | Why excluded |
| ---- | ------------ |
| `docs/prompts/01-modern-python-ecosystem-prompt.md` | Already executed; ecosystem **report** is the authority for Core locks |
| `docs/reports/03-*` / architecture prompts | Downstream; must not pre-decide generator engine |
| Spine prompts (`NN-*.md`) | Not yet commissioned |
| `docs/specifications/*`, `docs/plans/*`, `docs/reviews/*` | Placeholders / not accepted authority |
| Full go-foundry repositories | Optional external prior art only; not governing; fetch if needed for contrast |
| Entire `program/reference/*` | Available in-repo if needed; not required attachments |
| Raw Exa dumps under `scripts/exa-output/` | Ecosystem evidence only; not AI-native authority |

## Authority Notes

1. Blueprint locks beat Charter specialization beats this prompt beats convention.
2. Accepted ecosystem report **v0.2** locks Core toolchain for agent docs/skills: **ty**, **fnox+age**, **no `.env` secrets**, REC-013 command surface. Do not silently undo.
3. Research reports are recommendations, not commandments—until synthesis/spec acceptance.
4. Do not use chat history from the packaging session as authority.
5. Blueprint allowed G1 parallel start after charter; ecosystem is already accepted, so this session **inherits** it rather than pretending tool selection is open.
6. Owner preference: **one stage at a time** — do not chain architecture in the same substantive session.

## Expected Output

`docs/reports/02-ai-native-agent-workflow.md`

Optional: `docs/evidence/SPK-05*-*.md` if spikes are run.

## Identifier Ranges

| Kind | Range | Notes |
| ---- | ----- | ----- |
| REC | REC-100..REC-199 | Stage allocation |
| RSK | RSK-050..RSK-099 | Avoids ecosystem RSK-001..007 |
| OQ | OQ-050..OQ-099 | Avoids ecosystem OQ-001..006 |
| SPK | SPK-050..SPK-099 | Avoids ecosystem SPK-001..003 (planned) |
| EVD | EVD-100..EVD-199 | Report-local unless promoted |

## Fresh-session policy

Execute this stage in a **new session** with only the attachments above (plus in-repo retrieval of contracts if the agent can read the workspace). Do not chain architecture, synthesis, or plan stages in the same substantive session.
