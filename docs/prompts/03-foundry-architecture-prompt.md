# Deep Research Prompt — Foundry Architecture

- **Artifact ID:** PROMPT-03-foundry-architecture
- **Program:** python-foundry
- **Stage:** `research-foundry-architecture` — Foundry Architecture
- **Stage kind:** dependent focused research (requires both G1 tracks accepted)
- **Required inputs:**
  - `docs/00-program-blueprint.md` (Accepted)
  - `docs/01-research-charter.md` (Accepted)
  - `docs/reports/01-modern-python-ecosystem.md` (Accepted v0.2 — **full report**)
  - `docs/reports/02-ai-native-agent-workflow.md` (Accepted v0.2 — **full report**)
  - This prompt
  - `AGENTS.md` (operating rules)
  - `program/contracts/focused-research-report.md`
  - `program/templates/recommendation.md`
  - `program/contracts/evidence-model.md`
  - `program/contracts/evidence-spike.md`
  - Optional prior art (reference only, not authority):
    - https://github.com/robertguss/go-foundry-research
    - https://github.com/robertguss/go-foundry-cli
    — transferable patterns (spec → plan → generate, Core/profiles, closed catalogs);
    never sole proof that a Python/uv design is correct
- **Required output:** `docs/reports/03-foundry-architecture.md`
- **Recommendation range:** REC-200..REC-299
- **Risk range:** RSK-100..RSK-149
- **Open-question range:** OQ-100..OQ-149
- **Evidence spike IDs (if used):** SPK-100..SPK-149
- **Evidence IDs (within report):** EVD-200..EVD-299 (report-local unless promoted)
- **Depends on (must be accepted):** `charter`, `research-python-ecosystem`, `research-ai-native`
- **Research date:** use the actual calendar date when research is executed

## Role

Act as a **principal systems architect for developer tooling** and a **skeptical
maintainer** who:

- Designs hybrid project generators that are correct under dry-run and fail closed
- Prefers closed catalogs and small CLIs over unbounded plugin ecosystems
- Resists unsupported complexity, dual generation paths, and silent partial writes
- Designs for **macOS + Linux**, a **Python/`uv` foundry CLI**, and **AI coding
  agents as primary implementers** of Generated Projects
- Distinguishes verified fact, official claim, experiment, inference, judgment,
  user preference, and **prior-art parity hypothesis** (go-foundry)
- Treats accepted G1 reports as **inherited constraints**, not open re-research

## Mission

Answer:

> What architecture implements **hybrid generation** (spec → plan → generate),
> **Core / profiles / catalog**, and **AI-native surfaces** for a Python/`uv`
> foundry CLI, adapting go-foundry where appropriate?

Produce `docs/reports/03-foundry-architecture.md` as a complete standalone
focused research report that **synthesis** can consume without chat history.

## Authority and Precedence

Apply exactly (highest first):

1. Accepted `DEC-###` records that explicitly supersede earlier authority (none
   expected unless present under `decisions/`).
2. Locked decisions in `docs/00-program-blueprint.md`.
3. Normative methodology in `docs/01-research-charter.md`.
4. **This commissioning prompt**.
5. Accepted revised definitive specification — **not yet applicable**.
6. Accepted focused research reports:
   - `docs/reports/01-modern-python-ecosystem.md` (v0.2) — Core/profile locks
   - `docs/reports/02-ai-native-agent-workflow.md` (v0.2) — agent surface locks
   Do **not** re-litigate tool selection or agent standards here; **wire and emit** them.
7. Adversarial reviews — N/A.
8. Implementation plans — N/A.
9. `research-program.toml` as operational index only.
10. go-foundry prior art and community generator patterns (lower; adapt with evidence).
11. Model preference (lowest; never load-bearing alone).

**go-foundry research/CLI is prior art only** — strong transferable reference
for generation model, catalogs, and plan/transaction ideas; **never** sole proof
that a Python/`uv` architecture is correct. Mark go-foundry-derived claims as
**parity hypotheses** until justified for this program.

Chat history, model memory, and uncommitted notes are **not** authority.

## Locked Context

### Blueprint locks (selected)

| ID | Constraint |
| -- | ---------- |
| L1 | Product shape: **hybrid** (generator CLI + strong default Core + GitHub template surface) |
| L2 | Foundry itself is **Python/`uv`** (dogfood) |
| L3 | macOS + Linux only; **never Windows** |
| L4 | Prefer latest practical Python for foundry and Generated Projects (inherit ecosystem floor/default) |
| L6 | Archetypes: CLI + scripts; data/ETL in scope; **no notebooks** |
| L7 | GitHub Actions in Generated Project Core (inherit ecosystem CI) |
| L8 | Packaging: uv project + console scripts for v1 |
| L9 | AI-native first — emit closed agent surfaces from accepted AI-native report |
| L10 | Prior art: go-foundry **adapt, do not copy blindly** |
| L11–L14 | Personal + agents; standard rigor; quality over speed; research repo ≠ product implementation |

**Success criteria (from Blueprint):** fast empty→runnable path; agent-operable
repos; consistent Core; reduced decision fatigue; architecture that synthesis can
turn into REQs.

**Non-goals (from Blueprint):** marketplace; framework zoo; notebooks/GUI/mobile;
Windows; unlimited MCP/skill catalog; new package manager; coding backlog as
program output; full implementation of the product in this stage.

### Inherited ecosystem Core locks (Accepted v0.2 — do not silently undo)

| Layer | Lock |
| ----- | ---- |
| Python | Floor **3.12**, default pin **3.13** |
| Project tool | **uv** + committed `uv.lock` |
| Layout | **src/** packages; scripts via **PEP 723** + `uv run` |
| Lint/format | **Ruff** (check + format) |
| Types | **ty** Required Core (User decision; residual **RSK-002**) |
| Tests | **pytest** Required; pytest-cov Default |
| Hooks | **pre-commit** Default; **hk** optional profile `hooks-hk` only |
| Secrets | **fnox** Required Core; provider **`age`**; **no `.env` / dotenv secrets** |
| CI | GitHub Actions + setup-uv + ruff + ty + pytest (Linux required; macOS optional) |
| CLI framework | **Typer** Default for CLI archetype |
| Profiles | `http` (httpx), `hooks-hk` (hk), `data-etl` (polars+pyarrow default; extras) |
| Command surface (**REC-013**) | `uv sync` / `uv run …` / `fnox exec -- …` |

Generator **must emit** these locks into Generated Projects. Do not demote **ty**
or **fnox**, reintroduce dotenv secrets, or invent alternate Core toolchains
without a labeled DEC path (default: keep locks).

### Inherited AI-native locks (Accepted v0.2 — do not silently undo)

| Layer | Lock |
| ----- | ---- |
| Instructions | Root **`AGENTS.md` only** — **no** `CLAUDE.md` / `.claude/` Core emit |
| Skills | **`.agents/skills/<name>/SKILL.md` only** under **`.agents/`** |
| MCP | Default **none**; kitchen-sink catalogs **Rejected** |
| Diagnostics | Ruff + ty LSP for editors; **CLI gates** for agent definition-of-done |
| Commands | Amplify **REC-013** in templates/skills/docs |
| Secrets protocol | `fnox exec` + age; forbid dotenv secrets in agent docs/skills |
| Targets | Grok / Cursor / Codex / similar — **not** Claude Code as design target |
| Core skill purposes (Generated Projects) | Closed set: `quality-gates`, `secrets-fnox`, `add-cli-command` (CLI), `add-script` (scripts) — architecture designs **emit**, not unbounded new catalogs |

### Blueprint uncertainties this stage must address

1. Spec format and generation engine design (go-foundry parity vs Python-idiomatic).
2. How much of go-foundry’s catalog / plan / transaction model transfers to Python/uv.
3. How architecture **emits** the accepted Core/profile split and AI-native surfaces
   without dual paths or oral tradition.

## Stage Boundary

### Included

1. **CLI surface for the foundry product** — command model for at least:
   validate → plan (dry-run) → generate; any init/status/list-catalog helpers
   justified for v1; flags and exit semantics at architecture level (not full UX copy).
2. **Project specification format** — human- and agent-writable inputs that
   declare archetype, profiles, metadata, and options; versioning and validation
   rules; relation to `pyproject`/template params.
3. **Generation plan model** — dry-run artifact: planned file writes, deps,
   profile expansion, conflicts; what must be true before generate is allowed.
4. **Filesystem / write semantics** — transactional or fail-closed behavior;
   overwrite policy; partial-write recovery; non-goals for v1 if any.
5. **Catalog model** — closed catalog of templates, fragments, profiles, skills
   bodies, CI workflows; versioning; how Core vs profile membership is expressed
   (inherit ecosystem REC-014 and AI-native skill catalog).
6. **Archetype and profile model** — how CLI / scripts / data-ETL archetypes and
   opt-in profiles compose; conflicts and mutual exclusion; expansion algorithm.
7. **Module / package layout of the foundry itself** — recommended Python/`uv`
   module boundaries (CLI, domain, catalog, render, plan, validate) suitable for
   dogfooding Core.
8. **Evidence / quality gates for generation** — what the generator checks before
   and after generate (spec validity, Core invariants, optional post-gen
   `uv sync` / ruff / ty smoke policy).
9. **AI-native emit contract** — how generate produces `AGENTS.md`,
   `.agents/skills/…`, command/DoD docs, fnox.toml, and **does not** emit Claude
   adapters or default MCP kitchen sinks.
10. **GitHub template surface** — how hybrid “template repo” relates to generator
    path (parity requirements, single source of truth vs dual maintenance risk).
11. **go-foundry transfer analysis** — which patterns are Adopt / Adapt / Reject
    with rationale (not blind copy).
12. **Extension points for v1** — what is intentionally closed vs later-open
    (profiles, catalog entries) without marketplace design.
13. **Handoff to synthesis** — stable architecture claims that become REQs
    (interfaces, invariants, lifecycle), not a coding backlog.

### Excluded

1. Re-selecting Core packages (uv, ruff, ty, pytest, fnox, etc.) — accepted
   ecosystem report.
2. Reopening AI-native standards (`AGENTS.md` + `.agents/` only; MCP none;
   no Claude adapters) — accepted AI-native report.
3. Full product implementation; shipping the CLI binary.
4. Granular coding backlog / task packets / sprint plan.
5. Unlimited profiles, plugins, or MCP/skill marketplaces.
6. Web frameworks, GUI, mobile, notebooks, **Windows**.
7. Multi-tenant org template marketplaces.
8. Inventing a new package manager.
9. Full security threat model program (light notes only if load-bearing for
   secrets emit / write safety).
10. Writing synthesis, adversarial review, or implementation plan.
11. Reintroducing `.env` secrets or Claude Code adapters “for convenience.”
12. Marking this stage accepted or editing Blueprint/Charter/G1 reports.

## Primary Research Question

What **evidence-backed architecture** should python-foundry use for hybrid
generation (spec → plan → generate), closed Core/profile/catalog composition,
filesystem semantics, and AI-native surface emission under accepted G1 locks —
and which go-foundry patterns should be adopted, adapted, or rejected?

## Subsidiary Questions

Answer each with recommendation(s) or an explicit OQ:

1. What is the **v1 CLI command set** and lifecycle (validate / plan / generate
   and any others)? What are hard fail conditions?
2. What is the **project spec format** (file format(s), schema shape, versioning,
   agent-editability)? Why not pure flags-only or pure interactive-only?
3. How does **plan (dry-run)** represent intended changes, and how does it bind
   generate (plan-as-contract vs plan-as-preview)?
4. What are **write / overwrite / conflict** semantics? Atomic enough for v1?
5. How is the **closed catalog** structured (templates, fragments, profiles,
   skills, workflows)? How are versions and Core membership declared?
6. How do **archetypes and profiles** compose and expand into concrete file and
   dependency sets (algorithm + conflict rules)?
7. How does the architecture **guarantee emit** of ecosystem Core (uv, ruff, ty,
   pytest, fnox+age, GHA, REC-013) and AI-native surface (AGENTS.md, skills,
   no Claude, no default MCP)?
8. What is the recommended **foundry product module layout** (Python packages)
   for maintainability and dogfooding?
9. How should the **GitHub template surface** stay coherent with the generator
   without dual-source drift (single SoT, generate-from-catalog, or other)?
10. Which go-foundry patterns transfer (**Adopt / Adapt / Reject** table)?
11. What **post-generate verification** is Required vs Optional (e.g. run quality
    gates in-generator vs document for agents only)?
12. What risks (partial writes, catalog drift, agent-invented specs, plan/generate
    skew, dual template/generator paths) are material for v1?
13. Which load-bearing claims need **bounded spikes** (SPK-10x) before or during
    early implementation?

## Inheritance Contract

- Do not reopen Blueprint non-goals (Windows, notebooks, framework zoo, unlimited
  catalogs, etc.).
- Do not demote **ty** or **fnox** from Core or reintroduce **dotenv/`.env`
  secret storage** without a labeled DEC path — default is **keep locks**.
- Do not reintroduce **Claude Code adapters** (`CLAUDE.md`, `.claude/`) or a
  default MCP kitchen sink without a DEC path — default is **keep AI-native locks**.
- Do not reallocate ecosystem REC-001..014 or AI-native REC-100..112; **cite them**
  as inherited constraints where architecture emits or depends on them.
- Allocate REC/RSK/OQ/SPK only from this stage’s ranges; never reuse IDs.
- Synthesis will turn architecture + G1 into REQs; this report must still produce
  **stable, implementable** architectural decisions (interfaces, invariants,
  lifecycle, catalogs), not vague aspirations.

## Required Research Domains

1. Project generator / cookiecutter / copier / scaffolding architecture patterns
   (2026-relevant; Python-first)
2. Spec → plan → apply / dry-run / transactional write patterns in developer tools
3. Closed catalog / template composition and versioning
4. CLI design for multi-step generators (validate / plan / apply)
5. go-foundry research and CLI public artifacts as **prior art** (parity analysis)
6. uv-based project layout for the foundry product itself (dogfood Core)
7. Emitting agent instruction/skills trees from generators without dual paths
8. GitHub template repo vs generator dual-maintenance failure modes
9. Failure modes: partial generation, drift between plan and write, catalog sprawl,
   agent-invented non-Core tools in generated trees

## Methodology

1. Read **all required inputs completely** before researching — including both
   **full** accepted G1 reports (not digests alone).
2. Conduct **current** source-backed research; inspect go-foundry prior art for
   transfer analysis with explicit Adopt/Adapt/Reject.
3. Prefer **Tier 1–2** sources per Charter; mark go-foundry claims as parity
   hypotheses until justified.
4. Compare **credible alternatives** for each major decision area (at least:
   spec format approach; plan binding model; write semantics; catalog structure;
   template vs generator SoT).
5. Make **one primary recommendation per decision area** (plus Optional/Rejected
   as needed).
6. Run **bounded evidence spikes** when documentary evidence is weak or a
   load-bearing claim is economically testable (e.g. plan-as-contract prototype;
   catalog expand dry-run; emit tree smoke). Record as SPK-10x under
   `docs/evidence/` if committing spike reports; summarize in the main report.
   Blueprint expects spikes when generation/plan semantics are uncertain.
7. Record contradictory evidence and uncertainty honestly.
8. Score alternatives with the Charter evaluation rubric (hard gates = Blueprint
   locks + accepted G1 locks).

## Evidence and Citation Rules

Inherit Charter §§4–6 and §8:

- Portable Markdown links / source ledger with **access dates**
- No ephemeral-only citations
- Classify claims (verified fact, official claim, experiment, inference, judgment,
  user decision, hypothesis, **parity hypothesis**)
- Popularity/stars are not sufficient for architectural Required choices
- Mark go-foundry references as prior art / parity hypothesis when used
- Do not treat Exa/raw dumps or chat as authority; they may seed evidence only

## Evidence-Spike Policy

Spikes **expected** when:

- Plan/generate binding semantics are load-bearing and contested
- Catalog expansion or profile composition rules are complex enough to mis-specify
- Write/overwrite safety claims are load-bearing for “fail closed”
- Emit tree for Core + AI-native surface needs a smoke structure check

Spikes must be bounded, reproducible where practical, environment-documented
(OS, Python, tool versions), and not promoted to product architecture by inertia.

**Do not** re-run ecosystem tool-selection spikes or AI-native product-support
spikes as if open; may **reference** planned SPK-001..003, SPK-050, SPK-052 as
residual work synthesis/implementation should schedule.

## Comparison and Scoring Requirements

For each major decision area, include a short comparison table or equivalent
prose covering: fit to locks, agent operability, simplicity/closed-set discipline,
evidence quality, maintenance burden (including dual-path risk), go-foundry
transfer fit, and recommendation classification (Required / Default / Optional /
Rejected / Watchlist / Experimental).

## Required Recommendation Identifiers

- Allocate from **REC-200..REC-299** only.
- Use `program/templates/recommendation.md` fields for each REC.
- Cover at minimum (merge only if truly identical decision):

  - Foundry CLI lifecycle (validate / plan / generate)
  - Project specification format and validation
  - Plan (dry-run) model and binding to generate
  - Filesystem write / conflict / fail-closed semantics
  - Closed catalog model (structure, versioning, Core membership)
  - Archetype + profile composition rules
  - Core/profile **emit** contract (maps ecosystem REC-014 into generator)
  - AI-native **emit** contract (maps REC-100..112 into generator)
  - Foundry product module/package layout (Python/uv)
  - GitHub template surface vs generator coherence
  - go-foundry transfer disposition (may be one REC with Adopt/Adapt/Reject table)
  - Post-generate verification policy
  - Extension / closed-set discipline for v1 (anti-marketplace)

- Explicitly **cite** inherited ecosystem and AI-native RECs where architecture
  emits or depends on them (especially REC-003, REC-008, REC-012, REC-013,
  REC-014, REC-100..107, REC-110).

## Required Risk and Open-Question Ranges

- **RSK-100..RSK-149** — e.g. partial writes, plan/generate skew, catalog drift,
  dual template/generator maintenance, agent-invented non-Core tools, emit of
  forbidden surfaces (dotenv, Claude adapters)
- **OQ-100..OQ-149** — unknowns synthesis or owner must resolve
- **Do not reuse** RSK-001..007, RSK-050..056, OQ-001..006, OQ-050..055,
  SPK-001..003, SPK-050..052 for **new** subjects; you may **reference** them
- Blocking OQs for synthesis must be labeled clearly

## Exact Report Structure

Produce `docs/reports/03-foundry-architecture.md` with **exactly these sections**
(you may add subsections):

1. Artifact metadata (type, program, stage, status, version, created, last updated,
   **actual research date**, depends-on)
2. Executive answer
3. Scope and exclusions
4. Inherited constraints (Blueprint + accepted ecosystem + accepted AI-native)
5. Methodology
6. Source quality and limitations
7. Evidence spikes (or “None” with justification)
8. Comparative analysis (by decision area)
9. Recommendations (full REC write-ups, REC-200+)
10. Evidence Ledger
11. Recommendation ledger (index table of all REC-2##)
12. Risks (RSK-10x+)
13. Weak evidence
14. Conflicting evidence
15. Assumptions
16. Open questions (OQ-10x+)
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
- Required downstream decisions (for **synthesis** primarily)
- Relevant identifiers
- Full-report sections that must be read before deciding

## Required Tables

Include at least:

1. **CLI lifecycle** — command → inputs → outputs → fail conditions
2. **Spec model** — fields / dimensions → required vs optional → validation rules
3. **Plan model** — plan elements → binding strength → human/agent visibility
4. **Write semantics** — scenario → behavior (create/skip/fail/overwrite)
5. **Catalog inventory (v1 closed set)** — entry kind → id → emits what → Core/profile
6. **Archetype × profile composition** — allowed combinations / conflicts
7. **Emit contract** — inherited REC → generated paths/content invariants
8. **Foundry module map** — package/module → responsibility
9. **go-foundry transfer** — pattern → Adopt / Adapt / Reject → rationale
10. **Anti-patterns** — pattern → why rejected → mitigation REC

## Anti-Patterns (do not)

- Windows support creep
- Notebook or web framework zoo
- Unlimited profile/plugin/MCP/skill catalogs or marketplace design
- Stars/popularity as sole architectural proof
- Blind copy of go-foundry without Python/uv justification
- Reopening ecosystem Core tool selection or AI-native standards as if undecided
- Reintroducing **`.env` / dotenv secrets** or **Claude adapters** as Default emit
- Dual competing generators without a single SoT strategy
- Silent partial writes presented as success
- Silent REC loss or ID reuse (including G1 IDs)
- Placeholder sections or “TBD” standing in for recommendations
- Writing a granular coding backlog instead of architecture
- Beginning synthesis, review, or implementation plan stages
- Modifying Blueprint, Charter, G1 reports, or other stages’ outputs

## Completion Checklist

- [ ] All required report sections present
- [ ] Actual research date recorded
- [ ] Primary and subsidiary questions answered or explicitly OQ’d
- [ ] REC-200..REC-299 used correctly; no out-of-range IDs
- [ ] RSK/OQ/SPK within assigned ranges; no reuse of G1 IDs for new subjects
- [ ] Inherited ecosystem Core locks respected (ty, fnox+age, no dotenv, REC-013/014)
- [ ] Inherited AI-native locks respected (AGENTS.md + `.agents/` only; no Claude;
      MCP default none)
- [ ] go-foundry transfer table present (Adopt/Adapt/Reject)
- [ ] Evidence Ledger complete for load-bearing claims
- [ ] Source ledger with URLs and access dates
- [ ] Required tables complete
- [ ] Credible alternatives compared for major decision areas
- [ ] Handoff Digest complete (synthesis-oriented)
- [ ] Allowed file scope respected
- [ ] No downstream stages started

## Allowed File Scope

**May create/modify:**

- `docs/reports/03-foundry-architecture.md` (**primary required output**)
- `docs/evidence/SPK-10N-*.md` (only if spikes are run and documented)
- Optional spike scratch **outside** the repo if policy prefers; if so, still
  summarize in the report

**Must not modify:**

- `docs/00-program-blueprint.md`
- `docs/01-research-charter.md`
- `docs/reports/01-modern-python-ecosystem.md`
- `docs/reports/02-ai-native-agent-workflow.md`
- `research-program.toml` (human/architect updates status on acceptance)
- Other prompts, reports, specs, plans, reviews
- `program/` methodology library
- Product implementation code (none expected in this research repo)

## Final Response Requirements

1. Write the complete report to `docs/reports/03-foundry-architecture.md` (or
   provide the full Markdown if the session cannot write the repo—still treat it
   as that path’s contents).
2. Provide a brief execution summary **outside** the artifact.
3. List any unmet requirement and why.
4. List any remaining blocker.
5. Do **not** ask clarifying questions unless a true blocker exists under this prompt.
6. Do **not** begin a downstream stage (synthesis, review, or plan).
