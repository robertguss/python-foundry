# Chief Architect Synthesis Prompt — python-foundry

- **Artifact ID:** PROMPT-04-chief-architect-synthesis
- **Program:** python-foundry
- **Stage:** `synthesis` — Definitive Specification Synthesis
- **Stage kind:** chief-architect-synthesis
- **Required inputs:**
  - `docs/00-program-blueprint.md` (Accepted)
  - `docs/01-research-charter.md` (Accepted)
  - `docs/reports/01-modern-python-ecosystem.md` (Accepted **v0.2** — **full report**)
  - `docs/reports/02-ai-native-agent-workflow.md` (Accepted **v0.2** — **full report**)
  - `docs/reports/03-foundry-architecture.md` (Accepted **v0.1.1** — **full report**)
  - This prompt
  - `docs/handoffs/synthesis-attachment-manifest.md`
  - `AGENTS.md` (operating rules)
  - `program/contracts/synthesis.md`
  - `program/contracts/definitive-specification.md`
  - `program/templates/requirement.md`
  - `program/contracts/authority-and-precedence.md`
  - `program/contracts/identifiers.md` (as needed for REQ/RSK/OQ discipline)
- **Required output:** `docs/specifications/01-definitive-specification.md`
- **Requirement range:** REQ-001..REQ-299
- **Risk range (spec register):** prefer new RSK only if synthesis introduces material
  risks not already carried from reports; otherwise **carry and restate** upstream
  RSK-001..007, RSK-050..056, RSK-100..106 with stable IDs (do not renumber).
- **Open questions:** carry unresolved OQs with stable IDs; resolve in-spec where
  Chief Architect judgment + evidence suffice; mark owner-blocking OQs explicitly.
- **Depends on (must be accepted):** `research-foundry-architecture` (and transitively
  both G1 reports, Charter, Blueprint)
- **Synthesis date:** use the actual calendar date when synthesis is executed

> Contracts: `program/contracts/synthesis.md`,
> `program/contracts/definitive-specification.md`.
> Skeleton outline: `docs/specifications/01-definitive-specification.md` (replace
> placeholder content entirely).

## Role

Act as **Chief Architect** for python-foundry. Synthesis is **decision-making**,
not summarization or re-research.

You:

- Produce **one coherent proposed definitive specification** that is standalone
  and implementation-ready
- **Disposition every substantive `REC-###`** from all three accepted reports
- Preserve **locked decisions** and User decisions (ty, fnox+age, no dotenv
  secrets, AGENTS.md-only, no Claude adapters)
- Resolve contradictions; reject weak machinery; normalize terminology
- Convert accepted decisions into normative **`REQ-###`** requirements
- Leave **no foundational decision** to implementers without an explicit
  bounded spike or owner-blocking open question
- Do **not** invent new product scope, reopen non-goals, or start adversarial
  review / implementation planning in this session

## Mission

Answer:

> What is the **single coherent product specification** for python-foundry that
> synthesis can hand to adversarial review — covering hybrid generation
> (validate → plan → generate), Generated Project Core/profiles, AI-native
> surfaces, and foundry CLI architecture — with every upstream REC dispositioned
> and load-bearing choices expressed as `REQ-###`?

Produce `docs/specifications/01-definitive-specification.md` as a **complete
standalone** proposed definitive specification. Downstream agents must not need
chat history or the three research reports to implement, though reports remain
evidence authority until the revised spec is accepted as implementation
authority.

## Authority and Precedence

Apply exactly (highest first):

1. Accepted `DEC-###` records that explicitly supersede earlier authority (none
   expected unless present under `decisions/` at launch).
2. Locked decisions in `docs/00-program-blueprint.md`.
3. Normative methodology in `docs/01-research-charter.md` (evidence vocabulary,
   quality bar, anti-patterns).
4. **This commissioning prompt**.
5. Accepted revised definitive specification — **not yet applicable** (this
   stage *proposes* the first definitive specification).
6. Accepted focused research reports (evidence + recommendations):
   - `docs/reports/01-modern-python-ecosystem.md` (v0.2)
   - `docs/reports/02-ai-native-agent-workflow.md` (v0.2)
   - `docs/reports/03-foundry-architecture.md` (v0.1.1)
7. Adversarial reviews — N/A (downstream of this stage).
8. Implementation plans — N/A.
9. `research-program.toml` as operational index only.
10. go-foundry prior art (lower; already dispositioned in architecture REC-210).
11. Model preference (lowest; never load-bearing alone).

Chat history, model memory, and uncommitted notes are **not** authority.
Handoff digests **never** replace full reports.

## Locked Context

### Blueprint locks (must preserve)

| ID | Constraint |
| -- | ---------- |
| L1 | Product shape: **hybrid** (generator CLI + strong default Core + GitHub template surface) |
| L2 | Foundry itself is **Python/`uv`** (dogfood) |
| L3 | macOS + Linux only; **never Windows** |
| L4 | Prefer latest practical Python; floor/default from accepted ecosystem |
| L6 | Archetypes: CLI + scripts; data/ETL in scope; **no notebooks** |
| L7 | GitHub Actions in Generated Project Core |
| L8 | Packaging: uv project + console scripts for v1 |
| L9 | AI-native first — closed agent surfaces |
| L10 | go-foundry **adapt, do not copy blindly** |
| L11–L14 | Personal + agents; standard rigor; quality over speed; research repo ≠ product implementation |

**Success criteria:** fast empty→runnable path; agent-operable repos; consistent
Core; reduced decision fatigue; program completion via revised spec + plan later.

**Non-goals (do not reopen):** marketplace; framework zoo; notebooks/GUI/mobile;
Windows; unlimited MCP/skill catalog; new package manager; coding backlog as
program output; full product implementation in this research repo.

### Inherited ecosystem Core locks (Accepted v0.2 — do not silently undo)

| Layer | Lock |
| ----- | ---- |
| Python | Floor **3.12**, default pin **3.13** |
| Project tool | **uv** + committed `uv.lock` (apps; see OQ-104 for library nuance) |
| Layout | **src/** packages; scripts via **PEP 723** + `uv run` |
| Lint/format | **Ruff** (check + format) |
| Types | **ty** Required Core (User decision; residual RSK-002) |
| Tests | **pytest** Required; pytest-cov Default |
| Hooks | **pre-commit** Default; **hk** optional profile `hooks-hk` only |
| Secrets | **fnox** Required Core; provider **`age`**; **no `.env` / dotenv secrets** |
| CI | GitHub Actions + setup-uv + ruff + ty + pytest (Linux required; macOS optional) |
| CLI framework | **Typer** Default for CLI archetype |
| Profiles | `http` (httpx), `hooks-hk` (hk), `data-etl` (polars+pyarrow default; extras) |
| Command surface (**REC-013**) | `uv sync` / `uv run …` / `fnox exec -- …` |

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
| Core skill purposes (Generated Projects) | Closed set: `quality-gates`, `secrets-fnox`, `add-cli-command` (CLI), `add-script` (scripts) |

### Inherited architecture locks (Accepted v0.1.1 — do not silently undo)

| Layer | Lock |
| ----- | ---- |
| CLI lifecycle | Planner-led: **`validate` → `plan` → `generate`** (+ catalog list/show, version as justified) |
| Spec | **TOML** Project Spec (`schema = 1`); non-interactive first; explicit `--spec` |
| Plan | **Plan-as-contract** — same pure pipeline for validate/plan; generate executes that plan |
| Writes | Sibling **stage → verify (tiered) → exclusive place**; fail if dest exists/non-empty; no merge |
| Catalog | **Closed** core + archetypes + profiles + versions; no remote/plugin marketplace |
| Engine | **Custom** planner-led renderer (**not** Copier/Cookiecutter as runtime engine) |
| Emit | Core toolchain + AI-native surfaces as **invariants**, not optional extras |
| GitHub template | **Generated snapshot** from catalog SoT (not dual-edited) |
| go-foundry | Follow architecture **Adopt/Adapt/Reject** (REC-210); prior art only |

## Stage Boundary

### Included

1. One **proposed definitive specification** at the required output path.
2. Full structure per `program/contracts/definitive-specification.md` and the
   skeleton section list (metadata through handoff to adversarial review).
3. **Normative requirements** `REQ-001..REQ-299` (use only what is needed; leave
   unused IDs unallocated — never invent padding REQs).
4. **Recommendation Disposition Ledger** covering **every** substantive REC:
   - Ecosystem: REC-001..REC-014
   - AI-native: REC-100..REC-112
   - Architecture: REC-200..REC-212
5. **Traceability** matrix: REQ → sources (REC/DEC/judgment) → phase.
6. **Risk register** and **open questions** (carry + resolve where possible).
7. **Deferred / rejected work** sections so nothing disappears silently.
8. **High-level** first implementation strategy and **phase boundaries**
   (PHASE-##) sufficient for adversarial review and later planning — **not** a
   granular coding backlog or task packet list.
9. Explicit Chief Architect resolutions for synthesis-facing OQs where evidence
   and locks allow (see Methodology).
10. Definition of Done for the **product** as specified (and for this artifact).

### Excluded

1. New focused research tracks or re-running ecosystem/AI-native tool selection.
2. Reopening Windows, notebooks, marketplace, framework zoo, dotenv secrets,
   Claude adapters, demoting ty/fnox, or Copier-as-engine without a DEC path.
3. Adversarial review of the specification (downstream stage `spec-review`).
4. Implementation plan detail beyond high-level phases/milestones.
5. Product implementation, shipping binaries, or coding task packets.
6. Editing Blueprint, Charter, accepted reports, or this prompt’s authority.
7. Marking this stage `accepted` or inventing DEC records without human process.
8. Starting `spec-review`, `spec-revision`, or any plan stage in this session.

## Recommendation Disposition Rules

Every substantive inherited `REC-###` receives **exactly one** disposition in
the Disposition Ledger:

| Disposition | Meaning |
| ----------- | ------- |
| **Accepted** | Adopt as specified; map to REQ(s) |
| **Accepted with modification** | Adopt with explicit deltas; map to REQ(s); note what changed |
| **Merged** | Combined into another REC’s REQ(s); name the surviving subject |
| **Deferred** | Not in v1 normative scope; must appear under Deferred Work with reason |
| **Rejected** | Not adopted; must appear under Rejected Work with reason |
| **Superseded** | Replaced by a later REC or Chief Architect decision; name successor |
| **Not applicable** | Does not apply to the product as locked; short reason |

**Silent disappearance of any REC is a defect.** Merged/superseded items still
appear in the ledger.

User decisions and report locks that are load-bearing (ty Required, fnox+age,
no dotenv secrets, AGENTS.md-only, no Claude, plan-as-contract, exclusive place,
closed catalog, custom engine) default to **Accepted** unless a contradiction
forces **Accepted with modification** with explicit rationale — not silent demotion.

## Requirement Allocation Rules

- Allocate **REQ-001..REQ-299** only; never reuse IDs.
- Use `program/templates/requirement.md` fields for each REQ.
- Prefer stable, implementable subjects: lifecycle, formats, emit invariants,
  security, verification, non-goals as MUST NOT, phase membership.
- Each Must-priority REQ needs verification path (test, command, inspection,
  generated fixture, dogfooding, or explicit spike gate).
- Group REQs by theme in §22 but keep global ID uniqueness.
- Trace every Must REQ to at least one source (REC, DEC, Blueprint lock, or
  labeled Chief Architect judgment).

## Open Questions and Spikes

### Prefer resolve in synthesis (Chief Architect judgment)

Where research already recommends a default and only owner branding / polish
remains, **pick the research default**, document as judgment, and list residual
risk:

| ID | Topic | Research lean (do not re-research) |
| -- | ----- | ---------------------------------- |
| OQ-001 | ty CLI/config defaults in templates | Reasonable defaults + residual RSK-002; freeze at template level |
| OQ-101 | Default verify mode | Architecture recommends **`default`** tier before place |
| OQ-104 | Library vs app lockfile | Apps commit lock; libraries follow ecosystem guidance — make explicit |
| OQ-100 | Exact TOML field set | Freeze a **minimum normative field set** + extension policy; examples OK |

### May remain owner-blocking (explicit in Open Questions)

| ID | Topic | Notes |
| -- | ----- | ----- |
| OQ-003 | Force hk into Core | Only if owner rejects pre-commit Default — default keep REC-007 |
| OQ-004 | data-etl engine default | polars+pyarrow recommended; owner may DEC later |
| OQ-005 | macOS CI matrix | Optional cost preference — non-blocking for architecture REQs |
| OQ-105 | CLI binary name | Branding (`foundry` vs `python-foundry` vs `pyfoundry`) — pick a **provisional** default for REQs and mark owner-confirm |
| OQ-102 | JSON plan on disk | Optional; decide Default vs Optional |
| OQ-103 | data-etl skill set | Closed admission; may defer non-Core skills |
| OQ-052..055 | AI-native residuals | Resolve or defer with phase |

### Spikes

Do **not** run new multi-hour research programs. You may:

- **Schedule** residual SPK IDs from reports into phases (SPK-001..003,
  SPK-050/052, SPK-100..103) as implementation gates
- Mark REQ verification as “blocked on SPK-###” where load-bearing

Do not invent unbounded new spike programs.

## Methodology

1. Read **all required inputs completely** — full Blueprint, Charter, three
   reports, contracts, this prompt, attachment manifest. Digests alone are
   insufficient.
2. Inventory all RECs (001–014, 100–112, 200–212) before writing REQs.
3. Draft the **coherent product model** (stack, architecture, emit contracts,
   lifecycle) first; then allocate REQs; then complete disposition ledger and
   traceability (iterate until no orphan REC and no untraced Must REQ).
4. Resolve conflicts in favor of: Blueprint locks → User decisions → later
   architecture emit contracts that **wire** G1 (not re-select) → simpler closed
   sets over dual paths.
5. Normalize terminology across the three reports (one glossary of product terms:
   Project Spec, Generation Plan, Core, profile, archetype, catalog, stage/place,
   Generated Project, foundry CLI).
6. Write the specification as **standalone**: an implementer with only this file
   + ability to read locked tool docs should know what to build.
7. Status of the artifact: **`Proposed — pending adversarial review`**.
8. Do not mark the stage accepted; do not edit upstream accepted artifacts.

## Required Output Structure

Replace the placeholder skeleton entirely. Include at least:

1. Artifact Metadata  
2. Executive Decision Summary  
3. Authority and Intended Use  
4. Problem and Product Definition  
5. Goals and Non-Goals  
6. Locked Decisions and Invariants  
7. Final Technology Stack  
8. System Context  
9. Architecture  
10. Components and Boundaries  
11. Data Model (Project Spec, Plan, catalog entities)  
12. Interfaces and Integrations (CLI, GHA, agent surfaces)  
13. User Workflows  
14. Security and Privacy (fnox/age; no dotenv secrets; write safety)  
15. Reliability and Operations  
16. Testing and Verification  
17. CI and Release  
18. Migration (N/A or explicit greenfield)  
19. Performance Expectations  
20. Internal Contracts  
21. Dependency Bill of Materials  
22. Normative Requirements (`REQ-###`)  
23. Traceability  
24. Risk Register  
25. Open Questions  
26. Deferred Work  
27. Rejected Work  
28. Recommendation Disposition Ledger (all RECs)  
29. Definition of Done  
30. Handoff to Adversarial Review  

Plus high-level **phases** (PHASE-##) either in Architecture/Implementation
strategy sections or as a dedicated subsection before DoD — sufficient for
later implementation planning, not a task backlog.

Follow `program/contracts/definitive-specification.md` and
`program/templates/requirement.md`.

## Completion Checklist

- [ ] All required specification sections present and non-placeholder
- [ ] Status: **Proposed — pending adversarial review**
- [ ] Actual synthesis date recorded in metadata
- [ ] Every REC-001..014, REC-100..112, REC-200..212 dispositioned (ledger)
- [ ] REQ-001..REQ-299 used correctly; no out-of-range IDs; no silent ID reuse
- [ ] Must REQs have verification paths
- [ ] Traceability matrix complete for normative REQs
- [ ] Blueprint locks and non-goals preserved
- [ ] Ecosystem Core locks preserved (ty, fnox+age, no dotenv secrets, REC-013/014)
- [ ] AI-native locks preserved (AGENTS.md + `.agents/` only; MCP none; no Claude)
- [ ] Architecture locks preserved (validate/plan/generate; TOML; plan-as-contract;
      exclusive place; closed catalog; custom engine; template = generated snapshot)
- [ ] Risks and open questions carried or resolved honestly
- [ ] Deferred and Rejected work sections prevent silent loss
- [ ] High-level phases present; **no** granular coding backlog
- [ ] Standalone: implementable without chat history
- [ ] Allowed file scope only (specification path; optional notes only if already
      in scope — do not edit Blueprint/Charter/reports/prompt/manifest)
- [ ] No downstream stage started (no adversarial review content as the main work)
- [ ] Handoff to adversarial review section complete

## Allowed File Scope

| Path | Action |
| ---- | ------ |
| `docs/specifications/01-definitive-specification.md` | **Write** (primary output; replace placeholder) |
| Other paths | **Read only** |

Do not modify `research-program.toml`, Blueprint, Charter, reports, prompts, or
handoff package files in the substantive synthesis session (validators/humans
own status transitions after validation).
