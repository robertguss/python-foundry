# Attachment Manifest — research-python-ecosystem

## Stage

| Field | Value |
| ----- | ----- |
| Stage ID | `research-python-ecosystem` |
| Name | Modern Python Ecosystem & Project Standards |
| Prompt | `docs/prompts/01-modern-python-ecosystem-prompt.md` |
| Output | `docs/reports/01-modern-python-ecosystem.md` |
| Status at package time | `prompt-ready` (after prompt install) |

## Required Full Artifacts

1. `docs/00-program-blueprint.md` — locked scope, graph, constraints, success criteria
2. `docs/01-research-charter.md` — evidence rules, REC format, confidence, anti-patterns
3. `docs/prompts/01-modern-python-ecosystem-prompt.md` — commissioning prompt (sole stage mission)
4. `AGENTS.md` — repository operating rules for agents
5. `program/contracts/focused-research-report.md` — required report sections
6. `program/templates/recommendation.md` — REC write-up shape
7. `program/contracts/evidence-model.md` — claim classes and ledger fields
8. `program/contracts/evidence-spike.md` — when/how to spike

## Required Decision Records

- None at package time (only `decisions/README.md` exists). If any `decisions/DEC-*.md` is accepted before launch, attach it in full.

## Required Handoff Digests

- None (no upstream focused reports).

## Explicitly Excluded Artifacts

| Path | Why excluded |
| ---- | ------------ |
| `docs/prompts/02-*.md` / AI-native report | Parallel G1; not a dependency |
| `docs/reports/03-*` / architecture | Downstream; must not pre-decide generator engine |
| Spine prompts (`NN-*.md`) | Not yet commissioned |
| `docs/specifications/*`, `docs/plans/*`, `docs/reviews/*` | Placeholders / not accepted authority |
| Full go-foundry repositories | Optional external prior art only; not governing; fetch if needed for contrast, do not treat as inputs that override Blueprint/Charter |
| Entire `program/reference/*` | Available in-repo if needed; not required attachments |

## Authority Notes

1. Blueprint locks beat Charter specialization beats this prompt beats convention.
2. Research reports are recommendations, not commandments—until synthesis/spec acceptance.
3. Do not use chat history from the packaging session as authority.
4. Owner toolchain candidates (uv, ruff, ty, pytest, hk, fnox, httpx) are **candidates** until dispositioned with evidence.

## Expected Output

`docs/reports/01-modern-python-ecosystem.md`

## Identifier Ranges

| Kind | Range |
| ---- | ----- |
| REC | REC-001..REC-099 |
| RSK | RSK-001..RSK-049 |
| OQ | OQ-001..OQ-049 |
| SPK | SPK-001..SPK-049 |

## Fresh-session policy

Execute this stage in a **new session** with only the attachments above (plus in-repo retrieval of contracts if the agent can read the workspace). Do not chain AI-native research in the same substantive session.
