# Deep Research Prompt — Modern Python Ecosystem & Project Standards

- **Artifact ID:** PROMPT-01-modern-python-ecosystem
- **Program:** python-foundry
- **Stage:** `research-python-ecosystem` — Modern Python Ecosystem & Project Standards
- **Stage kind:** foundational focused research
- **Required inputs:**
  - `docs/00-program-blueprint.md` (Accepted)
  - `docs/01-research-charter.md` (Accepted)
  - This prompt
  - `AGENTS.md` (operating rules)
  - `program/contracts/focused-research-report.md`
  - `program/templates/recommendation.md`
  - Optional prior art (reference only, not authority): public go-foundry research/CLI docs if useful for *contrast*, not for Python tool choice
- **Required output:** `docs/reports/01-modern-python-ecosystem.md`
- **Recommendation range:** REC-001..REC-099
- **Risk range:** RSK-001..RSK-049
- **Open-question range:** OQ-001..OQ-049
- **Evidence spike IDs (if used):** SPK-001..SPK-049
- **Evidence IDs (within report):** EVD-001..EVD-099 (report-local unless promoted)
- **Parallel group:** G1 (do not wait on AI-native track; do not write that track’s report)
- **Research date:** use the actual calendar date when research is executed

## Role

Act as a **principal Python platform engineer** and **skeptical maintainer** who:

- Prefers closed, justified Core sets over fashion and framework zoos
- Resists unsupported complexity
- Designs for **macOS + Linux**, **uv-managed** projects, and **AI coding agents as primary implementers**
- Distinguishes verified fact, official claim, experiment, inference, judgment, and user preference

## Mission

Answer:

> What tooling, libraries, layouts, testing, and CI practices should define
> **Core** (and optional **profiles**) for CLI, scripts, and data/ETL Python
> projects in **2026** on **macOS/Linux** with **uv**?

Produce `docs/reports/01-modern-python-ecosystem.md` as a complete standalone
focused research report that architecture and synthesis can consume without
chat history.

## Authority and Precedence

Apply exactly (highest first):

1. Accepted `DEC-###` records that explicitly supersede earlier authority (none expected at this stage unless present under `decisions/`).
2. Locked decisions in `docs/00-program-blueprint.md`.
3. Normative methodology in `docs/01-research-charter.md`.
4. **This commissioning prompt**.
5. Accepted revised definitive specification — **not yet applicable**.
6. Accepted focused research reports — **none yet** for this program.
7. Adversarial reviews — N/A.
8. Implementation plans — N/A.
9. `research-program.toml` as operational index only.
10. Community convention.
11. Model preference (lowest; never load-bearing alone).

**go-foundry research/CLI is prior art only** — transferable design inspiration;
never sole proof that a Python tool or layout is correct.

Chat history, model memory, and uncommitted notes are **not** authority.

## Locked Context

Inherit all Blueprint locks, especially:

| ID | Constraint |
| -- | ---------- |
| L1 | Hybrid foundry (generator + strong default + template surface) — *this stage designs Core content, not the generator engine* |
| L2 | Foundry itself will be Python/`uv` (dogfood implications for recommended Core) |
| L3 | macOS + Linux only; never Windows |
| L4 | Prefer latest practical Python; pin exact floor/default with evidence |
| L5 | Toolchain **candidates** (confirm/refine/reject with evidence): `uv`, `ruff`, `ty`, `pytest`, `hk`, `fnox`; `httpx` when networking |
| L6 | Archetypes: CLI + scripts; data/ETL in scope; **no notebooks** |
| L7 | GitHub Actions in Core |
| L8 | Packaging: uv project + console scripts for v1 |
| L9 | AI-native first — *agent instruction/MCP/LSP catalog is the other G1 track; this stage only covers tooling/layout implications for agent operability* |
| L10–L14 | Prior art adapt-not-copy; personal+agents; standard rigor; quality over speed; research repo ≠ product implementation |

**Success criteria (from Blueprint):** fast path to runnable projects; agent can extend without oral tradition; consistent Core; reduced decision fatigue.

**Non-goals (from Blueprint):** marketplace, framework zoo, notebooks/GUI/mobile, Windows, unlimited catalogs, new package managers, coding backlog as research output.

## Stage Boundary

### Included

1. **Python version policy** — floor, default, how Generated Projects declare `requires-python`.
2. **Project/package management with uv** — layout of `pyproject.toml`, lockfiles, dependency groups (main/dev), workspaces if relevant to personal tools, build backend recommendations for installable packages vs scripts.
3. **Project layout conventions** — `src/` vs flat; package naming; CLI entry points / console scripts; script-oriented vs library-oriented layouts; multi-module defaults.
4. **Lint and format** — ruff (and any residual need for other formatters); config baselines suitable for agents.
5. **Type checking** — ty vs credible alternatives; strictness defaults; what belongs in Core CI.
6. **Testing** — pytest as candidate; plugins worth Core vs Optional; coverage policy; test layout.
7. **Hooks** — hk (and alternatives only if hk fails evidence); pre-commit-class workflows for local + CI parity.
8. **Secrets** — fnox (and alternatives only if needed); patterns safe for generated projects (no secret material in repo).
9. **HTTP clients** — httpx vs alternatives; when Core vs profile.
10. **CLI frameworks** — typer/click/argparse/etc. for **Generated Project** CLIs (not the Foundry product architecture deep-dive).
11. **Data/ETL profile** — DuckDB, pandas, and peer options; what is profile vs never-Core; no notebooks.
12. **Logging / structured output** — minimal Core recommendations for CLI/scripts.
13. **GitHub Actions CI** — matrix (Python versions, OS: linux required; macOS optional/cost note); jobs for lint, typecheck, test; caching with uv; permissions hygiene at a light level.
14. **Quality gates agents can run** — single documented command surface (e.g. `uv run …` / just recipes) implied by Core tools.
15. **Core vs capability profile split** — explicit tables: always-on Core vs optional profiles (e.g. `data-etl`, `http-client`, `cli-app`).
16. **Licensing note** — only as it affects Core dependency choices (prefer permissive, note copyleft risks); not a full legal opinion.

### Excluded

1. Foundry **generator engine** design (spec format, plan transactions, catalog engine) — architecture track.
2. Full **agent skills / MCP / LSP product catalog** — AI-native track (you may note *tooling* requirements those tracks will need, e.g. “LSP must understand this layout”).
3. Web frameworks, GUI, mobile, notebooks, Windows.
4. Multi-tenant org template marketplaces.
5. Inventing a new package manager.
6. Granular implementation backlog / task packets.
7. Implementing the Foundry product (beyond optional **bounded** spikes).
8. Consuming or writing the AI-native or architecture reports.

## Primary Research Question

What should the **evidence-backed Core toolchain and project standards** be for
python-foundry Generated Projects (CLI, scripts, data/ETL) in 2026 under the
locked constraints, and what should be **Optional profiles** vs **Rejected**?

## Subsidiary Questions

Answer each with recommendation(s) or an explicit OQ:

1. What **Python version floor and default** should Core use, and why?
2. How should Generated Projects be structured for **uv** (files, groups, lock policy)?
3. What is the default **directory/package layout** for CLI vs script vs data/ETL archetypes?
4. Should **ruff** be Required Core for lint+format? Any complementary tools?
5. Should **ty** be Required Core for types? Compare at least one serious alternative; state confidence.
6. Should **pytest** be Required Core? Which plugins/config are Default vs Optional?
7. Should **hk** be Required Core for hooks? Compare to pre-commit only if material.
8. Should **fnox** be Required or Optional for secrets? How should templates avoid leaking secrets?
9. When is **httpx** Core vs profile? Alternatives?
10. What **CLI framework** default (if any) for CLI archetype?
11. What belongs in a **data-etl** profile (DuckDB, pandas, others)? What is explicitly out?
12. What **GitHub Actions** workflow shape is Core (jobs, OS matrix, Python matrix, uv setup)?
13. What **one-command** (or minimal command set) should docs promise for check/test?
14. How should **dependency pinning/locking** work for apps vs libraries the owner publishes?
15. Which owner candidates are **confirmed**, **demoted**, or **rejected**, with evidence?

## Inheritance Contract

- Do not reopen Blueprint non-goals (Windows, notebooks, framework zoo, etc.).
- Do not silently convert owner preferences into Required Core without evidence or explicit User-decision labeling.
- Do not allocate REC/RSK/OQ/SPK outside assigned ranges.
- Never reuse IDs.
- Downstream architecture will design generation; this report must still produce **stable, implementable** Core/profile definitions (names, purposes, representative dependencies, layout rules).

## Required Research Domains

1. uv project/packaging workflows (official docs + current behavior)
2. Ruff and formatting/lint ecosystem position in 2026
3. ty and type-checking landscape relevant to Astral stack
4. pytest practices for small CLIs and data scripts
5. hk and fnox official capabilities and fit
6. httpx and CLI frameworks commonly used with modern typing
7. DuckDB/pandas (and close peers) for non-notebook ETL
8. GitHub Actions + uv best practices
9. Layout conventions (`src` layout, scripts packages) with agent-editability in mind

## Methodology

1. Read all required inputs completely before researching.
2. Conduct **current** source-backed research; verify versions and defaults as of the research date.
3. Prefer **Tier 1–2** sources per Charter; use lower tiers only for failure modes or questions.
4. Compare **credible alternatives** for each major decision area (at least one alternative for type checker, hooks approach, CLI framework, HTTP client, data stack pieces).
5. Make **one primary recommendation per decision area** (plus Optional/Rejected as needed).
6. Run **bounded evidence spikes** when documentary evidence is weak or a load-bearing claim is economically testable (e.g. uv+ruff+ty+pytest smoke on Linux; lockfile behavior). Record as SPK-### under `docs/evidence/` if committing spike reports; summarize in the main report.
7. Record contradictory evidence and uncertainty honestly.
8. Score alternatives with the Charter evaluation rubric (hard gates = Blueprint locks).

## Evidence and Citation Rules

Inherit Charter §§4–6 and §8:

- Portable Markdown links / source ledger with **access dates**
- No ephemeral-only citations
- Classify claims (verified fact, official claim, experiment, inference, judgment, user decision, hypothesis)
- Popularity/stars are not sufficient for Core
- Mark go-foundry references as prior art / parity hypothesis when used

## Evidence-Spike Policy

Spikes **expected** when:

- Version pins or tool defaults are contested and testable
- Integration of uv + ruff + ty + pytest + hk is load-bearing for “Core works out of the box”
- Layout choice affects console script / import behavior

Spikes must be bounded, reproducible where practical, environment-documented (OS, Python, tool versions), and not promoted to production architecture by inertia.

## Comparison and Scoring Requirements

For each major decision area, include a short comparison table or equivalent prose covering: fit to locks, agent operability, simplicity, evidence quality, maintenance burden, and recommendation classification (Required / Default / Optional / Rejected / Watchlist).

## Required Recommendation Identifiers

- Allocate from **REC-001..REC-099** only.
- Use `program/templates/recommendation.md` fields for each REC.
- Cover at minimum (merge only if truly identical decision):

  - Python version policy
  - uv/project packaging standard
  - Layout standard(s) by archetype
  - Lint/format (ruff or alternative)
  - Type checking (ty or alternative)
  - Testing (pytest + plugins policy)
  - Hooks (hk or alternative)
  - Secrets (fnox or alternative)
  - HTTP client policy
  - CLI framework default for CLI archetype
  - Data/ETL profile contents
  - GitHub Actions Core workflow policy
  - Core vs profile membership table (may be one REC with structured table plus supporting RECs)
  - Developer command surface for quality gates

- Explicitly disposition each Blueprint L5 candidate: confirm, demote, or reject.

## Required Risk and Open-Question Ranges

- **RSK-001..RSK-049** — e.g. tool immaturity, lockfile drift, CI cost, secret mishandling templates
- **OQ-001..OQ-049** — unknowns that architecture or owner must resolve
- Blocking OQs for architecture must be labeled clearly

## Exact Report Structure

Produce `docs/reports/01-modern-python-ecosystem.md` with **exactly these sections** (you may add subsections):

1. Artifact metadata (type, program, stage, status, version, created, last updated, **actual research date**, depends-on)
2. Executive answer
3. Scope and exclusions
4. Inherited constraints
5. Methodology
6. Source quality and limitations
7. Evidence spikes (or “None” with justification)
8. Comparative analysis (by decision area)
9. Recommendations (full REC write-ups)
10. Evidence Ledger
11. Recommendation ledger (index table of all REC-###)
12. Risks (RSK-###)
13. Weak evidence
14. Conflicting evidence
15. Assumptions
16. Open questions (OQ-###)
17. Handoff Digest (required fields per focused-research-report contract)
18. Source ledger
19. Completion checklist

### Handoff Digest must include

- Decisions supported
- Recommendations accepted by the report (list REC IDs)
- Recommendations challenged (if any internal tension)
- Evidence strength summary
- Weak and conflicting evidence pointers
- Assumptions
- Risks
- Open questions
- Required downstream decisions (for architecture / AI-native / synthesis)
- Relevant identifiers
- Full-report sections that must be read before deciding

## Required Tables

Include at least:

1. **Core membership** — component → Required/Default/Optional/Rejected → rationale REC
2. **Profiles** — profile id → contents → when applied
3. **Archetype layout** — CLI / script / data-ETL → directory/entry conventions
4. **CI matrix** — OS × Python × jobs
5. **Command surface** — human/agent commands for lint, typecheck, test, hooks
6. **L5 candidate disposition** — uv, ruff, ty, pytest, hk, fnox, httpx

## Anti-Patterns (do not)

- Windows support creep
- Notebook or web framework zoo
- Stars/popularity as proof
- Silent conversion of owner taste into Required without evidence label
- Designing the Foundry generator engine here
- Writing AI-native skill/MCP catalogs here
- Silent REC loss or ID reuse
- Placeholder sections or “TBD” standing in for recommendations
- Beginning architecture or synthesis stages
- Modifying Blueprint, Charter, or other stages’ outputs

## Completion Checklist

- [ ] All required report sections present
- [ ] Actual research date recorded
- [ ] Primary and subsidiary questions answered or explicitly OQ’d
- [ ] REC-001..REC-099 used correctly; no out-of-range IDs
- [ ] RSK/OQ/SPK within assigned ranges
- [ ] Evidence Ledger complete for load-bearing claims
- [ ] Source ledger with URLs and access dates
- [ ] Core vs profile tables complete
- [ ] L5 candidates dispositioned
- [ ] Credible alternatives compared for major tools
- [ ] Handoff Digest complete
- [ ] Allowed file scope respected
- [ ] No downstream stages started

## Allowed File Scope

**May create/modify:**

- `docs/reports/01-modern-python-ecosystem.md` (**primary required output**)
- `docs/evidence/SPK-00N-*.md` (only if spikes are run and documented)
- Optional spike scratch **outside** the repo if policy prefers; if so, still summarize in the report

**Must not modify:**

- `docs/00-program-blueprint.md`
- `docs/01-research-charter.md`
- `research-program.toml` (human/architect updates status on acceptance)
- Other prompts, reports, specs, plans, reviews
- `program/` methodology library
- Product implementation code (none expected in this research repo)

## Final Response Requirements

1. Write the complete report to `docs/reports/01-modern-python-ecosystem.md` (or provide the full Markdown if the session cannot write the repo—still treat it as that path’s contents).
2. Provide a brief execution summary **outside** the artifact.
3. List any unmet requirement and why.
4. List any remaining blocker.
5. Do **not** ask clarifying questions unless a true blocker exists under this prompt.
6. Do **not** begin a downstream stage.
