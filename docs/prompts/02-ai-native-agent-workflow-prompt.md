# Deep Research Prompt — AI-Native Repository & Agent Workflow

- **Artifact ID:** PROMPT-02-ai-native-agent-workflow
- **Program:** python-foundry
- **Stage:** `research-ai-native` — AI-Native Repository & Agent Workflow
- **Stage kind:** independent focused research (G1; ecosystem already accepted — inherit Core locks)
- **Required inputs:**
  - `docs/00-program-blueprint.md` (Accepted)
  - `docs/01-research-charter.md` (Accepted)
  - `docs/reports/01-modern-python-ecosystem.md` (Accepted v0.2 — **full report**)
  - This prompt
  - `AGENTS.md` (operating rules)
  - `program/contracts/focused-research-report.md`
  - `program/templates/recommendation.md`
  - `program/contracts/evidence-model.md`
  - `program/contracts/evidence-spike.md`
  - Optional prior art (reference only, not authority): public go-foundry research/CLI docs if useful for *agent-surface contrast*, not as sole proof
- **Required output:** `docs/reports/02-ai-native-agent-workflow.md`
- **Recommendation range:** REC-100..REC-199
- **Risk range:** RSK-050..RSK-099
- **Open-question range:** OQ-050..OQ-099
- **Evidence spike IDs (if used):** SPK-050..SPK-099
- **Evidence IDs (within report):** EVD-100..EVD-199 (report-local unless promoted)
- **Parallel group:** G1 (ecosystem is already accepted; do not reopen tool selection; do not write architecture or synthesis)
- **Research date:** use the actual calendar date when research is executed

## Role

Act as a **principal AI-coding-agent platform engineer** and **skeptical maintainer** who:

- Designs for **AI coding agents as primary implementers** (Grok, Claude Code, and similar) with a human owner
- Prefers **closed, curated** agent toolchains over kitchen-sink skill/MCP catalogs
- Resists unsupported complexity, oral tradition, and dual competing instruction surfaces
- Distinguishes verified fact, official claim, experiment, inference, judgment, and user preference
- Treats agent product docs as Tier 1 for *that product’s* behavior and does not overgeneralize across agents without evidence

## Mission

Answer:

> How should the **foundry** and **Generated Projects** be structured, documented,
> and instrumented so AI coding agents work optimally (skills, MCP, LSP,
> instructions, checks)?

Produce `docs/reports/02-ai-native-agent-workflow.md` as a complete standalone
focused research report that architecture and synthesis can consume without
chat history.

## Authority and Precedence

Apply exactly (highest first):

1. Accepted `DEC-###` records that explicitly supersede earlier authority (none expected unless present under `decisions/`).
2. Locked decisions in `docs/00-program-blueprint.md`.
3. Normative methodology in `docs/01-research-charter.md`.
4. **This commissioning prompt**.
5. Accepted revised definitive specification — **not yet applicable**.
6. Accepted focused research reports — **`docs/reports/01-modern-python-ecosystem.md` (v0.2)** is accepted; inherit its Core locks for command surface, ty, fnox+age, and secrets policy. Do not re-litigate Core tool *selection* here.
7. Adversarial reviews — N/A.
8. Implementation plans — N/A.
9. `research-program.toml` as operational index only.
10. Community convention / agent “best practices” posts (lower tier).
11. Model preference (lowest; never load-bearing alone).

**go-foundry research/CLI is prior art only** — transferable design inspiration
for agent surfaces; never sole proof that a Python agent layout or MCP set is
correct.

Chat history, model memory, and uncommitted notes are **not** authority.

## Locked Context

Inherit all Blueprint locks, especially:

| ID | Constraint |
| -- | ---------- |
| L1 | Hybrid foundry (generator + strong default + template surface) — *this stage designs agent operability of foundry + Generated Projects, not the generator engine* |
| L2 | Foundry itself will be Python/`uv` (dogfood agent surface on the foundry repo too) |
| L3 | macOS + Linux only; never Windows |
| L6 | Archetypes: CLI + scripts; data/ETL in scope; **no notebooks** |
| L9 | **AI-native first** — portable skills; curated MCP/LSP/agent config; agent-operable layout and docs |
| L10–L14 | Prior art adapt-not-copy; personal+agents; standard rigor; quality over speed; research repo ≠ product implementation |

**Blueprint non-goal L6 for agents:** Unlimited MCP/skill catalog — **closed, curated** agent tooling only for v1.

### Inherited ecosystem Core locks (Accepted report v0.2 — do not silently undo)

These are **constraints for agent docs/skills/checks**, not open re-research of package managers or type checkers:

| Layer | Lock |
| ----- | ---- |
| Python | Floor **3.12**, default pin **3.13** |
| Project tool | **uv** + committed `uv.lock` |
| Layout | **src/** packages; scripts via **PEP 723** + `uv run` |
| Lint/format | **Ruff** (check + format) |
| Types | **ty** Required Core (**User decision**; residual RSK-002) |
| Tests | **pytest** Required; pytest-cov Default |
| Hooks | **pre-commit** Default; **hk** optional profile only |
| Secrets | **fnox** Required Core; provider **`age`**; **no `.env` / dotenv secrets** |
| CI | GitHub Actions + setup-uv + ruff + ty + pytest (Linux required; macOS optional) |
| CLI framework | **Typer** Default for CLI archetype |
| Command surface (REC-013) | `uv sync` / `uv run ruff …` / `uv run ty check` / `uv run pytest` / `uv run pre-commit …` / `fnox exec -- …` |

**Explicit handoff from ecosystem to this track:** document **ty** LSP/agent diagnostics; **fnox** skills and age key hygiene; **forbid dotenv secret patterns** in agent instructions; amplify the REC-013 command surface in skills/docs.

**Success criteria (from Blueprint):** agent can extend projects without oral tradition; closed agent toolchain; consistent Core; reduced decision fatigue.

**Non-goals (from Blueprint):** marketplace; framework zoo; notebooks/GUI/mobile; Windows; unlimited catalogs; new package managers; coding backlog as research output; multi-agent orchestration product; model training; building every MCP server.

## Stage Boundary

### Included

1. **Agent instruction surfaces** — `AGENTS.md`, `CLAUDE.md`, `.cursorrules` / Cursor rules, Copilot instructions, and similar: which files for **foundry** vs **Generated Projects**; precedence when multiple exist; minimal vs comprehensive content.
2. **Portable skills** — skill layout conventions (e.g. `.agents/skills/`, product-specific skill dirs); what skills ship in Core vs optional profiles; skill authoring standards (when to use a skill vs docs).
3. **MCP** — curated default MCP set for foundry work and for Generated Projects; what is Required vs Optional vs Rejected; how templates declare MCP config without kitchen-sink sprawl.
4. **LSP / editor diagnostics** — defaults that match Core tools (especially **ty**, Ruff); editor-agnostic recommendations; agent use of diagnostics.
5. **Repo layout for agent operability** — directory conventions that reduce search cost; where docs, skills, evidence, and contracts live; boundaries agents must not cross without a stage/DEC.
6. **Verification hooks agents can run** — map REC-013 command surface into agent workflows; pre-commit vs CI parity; “definition of done” for agent PRs.
7. **Secrets operability for agents** — how agents use **fnox + age** safely; patterns that prevent reintroducing `.env`/dotenv; CI/dev key handling at a light level (not full threat model).
8. **Foundry-product agent surface vs Generated Project surface** — what differs (generator CLI skills, research-program skills vs ordinary app skills).
9. **Multi-agent product coverage** — design for Grok, Claude Code, and similar without maintaining unbounded per-product forks; portable-first with thin product adapters if needed.
10. **Context packaging / handoffs** — how generated projects should present attachable context (README, AGENTS.md, skill indexes) so fresh agent sessions succeed.
11. **Anti-patterns** — oral tradition, contradictory instruction files, dual command surfaces, dotenv “quick starts,” uncurated MCP lists.
12. **Closed catalog model** — how architecture will later emit skills/MCP/LSP as part of generate (requirements shape only; not generator engine design).

### Excluded

1. Foundry **generator engine** design (spec format, plan transactions, catalog engine, write semantics) — architecture track.
2. Re-selecting Core packages (uv, ruff, ty, pytest, fnox, etc.) — already dispositioned in ecosystem report; may only document *agent usage* of those tools.
3. Web frameworks, GUI, mobile, notebooks, Windows.
4. Multi-tenant org template marketplaces.
5. Building or implementing every MCP server; multi-agent orchestration product; model training.
6. Unlimited skill/MCP catalogs.
7. Granular implementation backlog / task packets.
8. Implementing the Foundry product (beyond optional **bounded** spikes).
9. Writing architecture, synthesis, or other stages’ reports.
10. Reopening dotenv secrets “for agent simplicity” without a DEC path (must not recommend as Default).

## Primary Research Question

How should **python-foundry** and its **Generated Projects** be structured,
documented, and instrumented so AI coding agents operate optimally under the
locked Core toolchain — with a **closed, curated** set of skills, MCP, LSP,
instructions, and checks?

## Subsidiary Questions

Answer each with recommendation(s) or an explicit OQ:

1. What **instruction file set** should Core emit for Generated Projects (`AGENTS.md` and peers)? What is Required vs optional product-specific adapters?
2. How should **portable skills** be laid out and versioned? What is the closed Core skill set (names/purposes) vs profile skills?
3. What **curated MCP servers** (if any) belong in Core for Generated Projects vs only for the foundry development environment?
4. What **LSP / diagnostics** defaults should Core document for **ty** and **Ruff** (and anything else justified)?
5. How should agents discover and run the **REC-013 command surface** (docs, skills, just recipes wrappers)?
6. How should **fnox + age** be taught to agents so they do **not** invent `.env` workflows?
7. What differs between **foundry-repo agent surface** and **Generated Project agent surface**?
8. How should **context handoffs** work for fresh sessions on Generated Projects (attach lists, digests vs full files)?
9. What **verification / definition-of-done** checklist should agents follow before claiming work complete?
10. How should multi-tool agent products (Grok, Claude Code, Cursor, etc.) be supported without an unbounded matrix?
11. Which go-foundry agent patterns (if any) are **parity hypotheses** worth adapting vs rejecting for Python?
12. What risks (agent instruction conflict, skill drift, MCP supply chain, ty diagnostic noise) are material for v1?

## Inheritance Contract

- Do not reopen Blueprint non-goals (Windows, notebooks, framework zoo, unlimited catalogs, etc.).
- Do not demote **ty** or **fnox** from Core or reintroduce **dotenv/`.env` secret storage** without labeling a proposed DEC path and residual risk — default is **keep locks**.
- Do not reallocate ecosystem REC-001..014; **cite them** as inherited constraints where relevant.
- Allocate REC/RSK/OQ/SPK only from this stage’s ranges; never reuse IDs.
- Downstream architecture will design generation; this report must still produce **stable, implementable** agent-surface definitions (file paths, catalog membership, command contracts, skill purposes).

## Required Research Domains

1. Agent instruction file conventions across major coding agents (2026)
2. Portable skill formats and repository layouts (including `.agents/skills/` and product-specific variants)
3. MCP protocol capabilities and practical curated-server selection for personal Python repos
4. LSP / editor integration for Ruff and **ty** (and how agents consume diagnostics)
5. Agent-operable verification patterns (uv run, pre-commit, CI parity)
6. Secrets workflows for agents with **fnox** and **age** (official docs + failure modes)
7. Context-window / attachment strategies for multi-file agent sessions
8. go-foundry AI-native patterns as prior art only (if publicly available)
9. Known failure modes: conflicting CLAUDE.md vs AGENTS.md, skill bloat, MCP sprawl, agents inventing dotenv

## Methodology

1. Read all required inputs completely before researching — **including the full accepted ecosystem report**.
2. Conduct **current** source-backed research; verify agent product docs, skill formats, MCP specs, and tool integrations as of the research date.
3. Prefer **Tier 1–2** sources per Charter; use lower tiers for failure modes (“what agents struggle with”) with appropriate confidence.
4. Compare **credible alternatives** for each major decision area (instruction file strategy; skill layout; MCP Core set vs none; multi-agent adapter strategy).
5. Make **one primary recommendation per decision area** (plus Optional/Rejected as needed).
6. Run **bounded evidence spikes** when documentary evidence is weak or a load-bearing claim is testable (e.g. sample Generated Project tree + agent instruction set; ty diagnostics path; fnox exec smoke without dotenv). Record as SPK-05x under `docs/evidence/` if committing spike reports; summarize in the main report.
7. Record contradictory evidence and uncertainty honestly.
8. Score alternatives with the Charter evaluation rubric (hard gates = Blueprint locks + accepted ecosystem Core locks).

## Evidence and Citation Rules

Inherit Charter §§4–6 and §8:

- Portable Markdown links / source ledger with **access dates**
- No ephemeral-only citations
- Classify claims (verified fact, official claim, experiment, inference, judgment, user decision, hypothesis)
- Popularity/stars/“everyone uses X agent” are not sufficient for Core
- Mark go-foundry references as prior art / parity hypothesis when used
- Agent product docs are Tier 1 for that product only — label overgeneralization risk

## Evidence-Spike Policy

Spikes **optional but preferred** when:

- Instruction file precedence is contested and testable on a sample tree
- ty diagnostics or `uv run ty` integration is load-bearing for agent “definition of done”
- fnox+age vs agent-invented dotenv is a documented failure mode worth a smoke test
- A proposed Core MCP server’s install/auth cost is load-bearing

Spikes must be bounded, reproducible where practical, environment-documented (OS, agent product if any, tool versions), and not promoted to product architecture by inertia.

**Do not** re-run ecosystem tool selection spikes; may reference planned ecosystem SPK-001..003 as open residual work.

## Comparison and Scoring Requirements

For each major decision area, include a short comparison table or equivalent prose covering: fit to locks, agent operability, simplicity/closed-set discipline, evidence quality, maintenance burden (multi-agent products), and recommendation classification (Required / Default / Optional / Rejected / Watchlist / Experimental).

## Required Recommendation Identifiers

- Allocate from **REC-100..REC-199** only.
- Use `program/templates/recommendation.md` fields for each REC.
- Cover at minimum (merge only if truly identical decision):

  - Generated Project instruction file standard (`AGENTS.md` and peers)
  - Foundry-repo agent instruction standard (may differ)
  - Portable skills layout and Core skill catalog (closed set)
  - Profile/optional skills policy
  - Curated MCP Core vs Optional vs Rejected
  - LSP / diagnostics defaults (ty, Ruff, others if justified)
  - Agent command surface / verification workflow (inherit and amplify REC-013)
  - Secrets agent protocol (fnox + age; forbid dotenv secrets)
  - Multi-agent product strategy (portable-first vs per-product forks)
  - Fresh-session / context attachment guidance for Generated Projects
  - Definition of done for agent implementers
  - Explicit anti-catalog / anti-oral-tradition rules

- Explicitly **cite** inherited ecosystem RECs (especially REC-005, REC-008, REC-013, REC-014) where agent recommendations depend on them.

## Required Risk and Open-Question Ranges

- **RSK-050..RSK-099** — e.g. instruction conflict, skill drift, MCP supply chain, agent dotenv relapse, ty diagnostic noise for agents, overfit to one agent product
- **OQ-050..OQ-099** — unknowns architecture or owner must resolve
- **Do not reuse** RSK-001..007 / OQ-001..006 / SPK-001..003 (ecosystem); you may **reference** them
- Blocking OQs for architecture must be labeled clearly

## Exact Report Structure

Produce `docs/reports/02-ai-native-agent-workflow.md` with **exactly these sections** (you may add subsections):

1. Artifact metadata (type, program, stage, status, version, created, last updated, **actual research date**, depends-on)
2. Executive answer
3. Scope and exclusions
4. Inherited constraints (Blueprint + accepted ecosystem Core locks)
5. Methodology
6. Source quality and limitations
7. Evidence spikes (or “None” with justification)
8. Comparative analysis (by decision area)
9. Recommendations (full REC write-ups, REC-100+)
10. Evidence Ledger
11. Recommendation ledger (index table of all REC-1##)
12. Risks (RSK-05x+)
13. Weak evidence
14. Conflicting evidence
15. Assumptions
16. Open questions (OQ-05x+)
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
- Required downstream decisions (for architecture / synthesis)
- Relevant identifiers
- Full-report sections that must be read before deciding

## Required Tables

Include at least:

1. **Agent instruction surface** — file → audience (foundry vs generated) → Required/Default/Optional → purpose
2. **Core skill catalog** — skill id/name → purpose → when applied → status
3. **MCP catalog** — server → purpose → Required/Optional/Rejected → auth/secrets notes
4. **LSP / diagnostics map** — tool → agent/editor path → Core?
5. **Command surface for agents** — maps to REC-013 + any wrappers
6. **Foundry vs Generated Project** differences (agent surface only)
7. **Anti-patterns** — pattern → why rejected → mitigation REC

## Anti-Patterns (do not)

- Windows support creep
- Notebook or web framework zoo
- Unlimited skill/MCP catalogs
- Stars/popularity or “Twitter best practice” as sole proof
- Reopening ecosystem Core tool selection (uv/ruff/ty/pytest/fnox) as if undecided
- Reintroducing **`.env` / dotenv secrets** as Default “for agents”
- Designing the Foundry generator engine here
- Dual competing command surfaces that contradict REC-013
- Silent REC loss or ID reuse (including ecosystem IDs)
- Placeholder sections or “TBD” standing in for recommendations
- Beginning architecture or synthesis stages
- Modifying Blueprint, Charter, ecosystem report, or other stages’ outputs

## Completion Checklist

- [ ] All required report sections present
- [ ] Actual research date recorded
- [ ] Primary and subsidiary questions answered or explicitly OQ’d
- [ ] REC-100..REC-199 used correctly; no out-of-range IDs
- [ ] RSK/OQ/SPK within assigned ranges; no reuse of ecosystem RSK/OQ/SPK IDs for new subjects
- [ ] Inherited ecosystem Core locks respected (ty, fnox+age, no dotenv secrets, REC-013 surface)
- [ ] Evidence Ledger complete for load-bearing claims
- [ ] Source ledger with URLs and access dates
- [ ] Required tables complete
- [ ] Credible alternatives compared for major decision areas
- [ ] Handoff Digest complete
- [ ] Allowed file scope respected
- [ ] No downstream stages started

## Allowed File Scope

**May create/modify:**

- `docs/reports/02-ai-native-agent-workflow.md` (**primary required output**)
- `docs/evidence/SPK-05N-*.md` (only if spikes are run and documented)
- Optional spike scratch **outside** the repo if policy prefers; if so, still summarize in the report

**Must not modify:**

- `docs/00-program-blueprint.md`
- `docs/01-research-charter.md`
- `docs/reports/01-modern-python-ecosystem.md`
- `research-program.toml` (human/architect updates status on acceptance)
- Other prompts, reports, specs, plans, reviews
- `program/` methodology library
- Product implementation code (none expected in this research repo)

## Final Response Requirements

1. Write the complete report to `docs/reports/02-ai-native-agent-workflow.md` (or provide the full Markdown if the session cannot write the repo—still treat it as that path’s contents).
2. Provide a brief execution summary **outside** the artifact.
3. List any unmet requirement and why.
4. List any remaining blocker.
5. Do **not** ask clarifying questions unless a true blocker exists under this prompt.
6. Do **not** begin a downstream stage.
