# Attachment Manifest — research-foundry-architecture

## Stage

| Field | Value |
| ----- | ----- |
| Stage ID | `research-foundry-architecture` |
| Name | Foundry Architecture |
| Prompt | `docs/prompts/03-foundry-architecture-prompt.md` |
| Output | `docs/reports/03-foundry-architecture.md` |
| Status at package time | `prompt-ready` (after prompt install) |

## Required Full Artifacts

1. `docs/00-program-blueprint.md` — locked scope, graph, architecture stage mission, non-goals, go-foundry prior-art posture
2. `docs/01-research-charter.md` — evidence rules, REC format, confidence, anti-patterns
3. `docs/prompts/03-foundry-architecture-prompt.md` — commissioning prompt (sole stage mission)
4. `docs/reports/01-modern-python-ecosystem.md` — **Accepted v0.2 full report** (Core/profiles, layouts, CI, REC-013/014, ty/fnox locks)
5. `docs/reports/02-ai-native-agent-workflow.md` — **Accepted v0.2 full report** (AGENTS.md + `.agents/` only; MCP none; no Claude; emit contracts)
6. `AGENTS.md` — repository operating rules for agents
7. `program/contracts/focused-research-report.md` — required report sections
8. `program/templates/recommendation.md` — REC write-up shape
9. `program/contracts/evidence-model.md` — claim classes and ledger fields
10. `program/contracts/evidence-spike.md` — when/how to spike

## Required Decision Records

- None at package time (only `decisions/README.md` exists). If any `decisions/DEC-*.md` is accepted before launch, attach it in full.

## Required Handoff Digests

- None required separately: **full** G1 reports are attached (preferred over digest-only). Each report’s Handoff Digest (§17) must be read:
  - Ecosystem §17 — architecture needs Core/profile catalog, layouts, CI with ty, generator emits uv+fnox+ty
  - AI-native §17 — architecture emits `AGENTS.md` + `.agents/skills` only; no Claude adapters; no default MCP; command/DoD in templates

## Explicitly Excluded Artifacts

| Path | Why excluded |
| ---- | ------------ |
| `docs/prompts/01-modern-python-ecosystem-prompt.md` | Already executed; ecosystem **report** is authority for Core locks |
| `docs/prompts/02-ai-native-agent-workflow-prompt.md` | Already executed; AI-native **report** is authority for agent surface |
| Spine prompts (`NN-*.md`) | Not yet commissioned; synthesis is downstream |
| `docs/specifications/*`, `docs/plans/*`, `docs/reviews/*` | Placeholders / not accepted authority |
| Full go-foundry repositories as mandatory attach | Optional external prior art; fetch if needed for Adopt/Adapt/Reject analysis; not governing |
| Entire `program/reference/*` | Available in-repo if needed; not required attachments |
| Raw Exa dumps under `scripts/exa-output/` | Prior-stage evidence only; not architecture authority |
| `HANDOFF.md` | Resume aid only; not higher authority than Blueprint/Charter/reports |

## Authority Notes

1. Blueprint locks beat Charter specialization beats this prompt beats convention.
2. Accepted ecosystem report **v0.2** locks Core toolchain and profiles: **ty**, **fnox+age**, **no `.env` secrets**, REC-013 command surface, REC-014 Core/profile membership. Architecture **emits** these; does not re-select them.
3. Accepted AI-native report **v0.2** locks agent surface: **`AGENTS.md` + `.agents/` only**, no Claude adapters, MCP default none. Architecture **emits** these; does not re-litigate product support.
4. Research reports are recommendations, not commandments—until synthesis/spec acceptance. G1 locks that are **User decisions** (ty, fnox+age, no dotenv, no Claude) must still be treated as hard emit constraints unless a DEC supersedes them.
5. go-foundry is **prior art only** — transferable patterns; never sole proof.
6. Do not use chat history from the packaging session as authority.
7. Owner preference: **one stage at a time** — do not chain synthesis in the same substantive session.

## Expected Output

`docs/reports/03-foundry-architecture.md`

Optional: `docs/evidence/SPK-10*-*.md` if spikes are run.

## Identifier Ranges

| Kind | Range | Notes |
| ---- | ----- | ----- |
| REC | REC-200..REC-299 | Stage allocation |
| RSK | RSK-100..RSK-149 | Avoids ecosystem RSK-001..007 and AI-native RSK-050..056 |
| OQ | OQ-100..OQ-149 | Avoids ecosystem OQ-001..006 and AI-native OQ-050..055 |
| SPK | SPK-100..SPK-149 | Avoids ecosystem SPK-001..003 and AI-native SPK-050..052 |
| EVD | EVD-200..EVD-299 | Report-local unless promoted |

## Fresh-session policy

Execute this stage in a **new session** with only the attachments above (plus
in-repo retrieval of contracts if the agent can read the workspace). Do not chain
synthesis, adversarial review, or plan stages in the same substantive session.
