# Research Charter — python-foundry

- **Artifact type:** Research Charter
- **Program:** python-foundry
- **Status:** Accepted
- **Version:** 0.1
- **Created:** 2026-07-30
- **Last updated:** 2026-07-31
- **Depends on:** Accepted Program Blueprint (`docs/00-program-blueprint.md`)
- **Rigor tier:** standard (inherited from Blueprint)

> This Charter defines **how** research is conducted for python-foundry. It does
> not invent product conclusions. Accepted by human via Git commit recorded in
> `research-program.toml`.

## 1. Artifact Metadata

| Field | Value |
| ----- | ----- |
| Program ID | python-foundry |
| Owner | robertguss |
| Repository | https://github.com/robertguss/python-foundry |
| Governing Blueprint | `docs/00-program-blueprint.md` (Accepted) |
| Methodology library | `program/` (contracts, templates, reference) |
| Operational index | `research-program.toml` (not substantive authority) |

**Prior art (transferable reference, not governing unless adopted via REC/DEC):**

- https://github.com/robertguss/go-foundry-research
- https://github.com/robertguss/go-foundry-cli

## 2. Research Philosophy

1. **Artifacts carry context; chat does not.** Every substantive claim that
   matters later must live in a Git-tracked Markdown artifact with portable
   citations.
2. **Evidence before confidence.** Polished prose is not proof. Distinguish
   verified fact, official claim, corroboration, experiment, inference,
   architectural judgment, user decision, and hypothesis
   (`program/contracts/evidence-model.md`).
3. **Decide for the locked product, not for fashion.** Optimize for the
   Blueprint: personal hybrid foundry, AI-agent-primary implementation, macOS +
   Linux, CLI/scripts/data-ETL, uv-centric Python dogfooding.
4. **Challenge owner defaults with evidence; do not discard them casually.**
   Candidates such as uv, ruff, ty, pytest, hk, fnox, and httpx are **honest
   starting points**, not automatic Core. Confirm, refine, or replace with
   explicit REC + rationale.
5. **Adapt go-foundry; do not copy blindly.** Generation patterns
   (spec → plan → generate, Core vs profiles, closed catalogs, dry-run
   discipline) are transferable *hypotheses*. Python packaging, tooling, and
   agent surfaces must be re-researched.
6. **Closed sets over kitchen sinks.** Prefer a small, justified Core and a
   small curated agent toolchain over “support everything.”
7. **Standard rigor:** full evidence ledgers on focused reports; bounded spikes
   for load-bearing uncertainty; selective corroboration; full synthesis and
   adversarial reviews; risk-triggered extra rounds only.
8. **Time posture:** research quality over artificial calendar pressure (Blueprint L13).

## 3. Scope Discipline

### In scope for research stages

| Track | May research |
| ----- | ------------ |
| `research-python-ecosystem` | uv and packaging; lint/type/test; hooks/secrets; HTTP clients; data/ETL libraries (DuckDB, pandas, etc.); project layouts; GitHub Actions; Python version floor/default for macOS/Linux |
| `research-ai-native` | Agent instruction layouts; portable skills; curated MCP/LSP; editor/agent config; checks agents can run; operability of foundry + generated projects |
| `research-foundry-architecture` | Spec format; validate/plan/generate; catalog; Core/profiles/archetypes; Python CLI shape; filesystem/write semantics; transfer/adapt go-foundry patterns |

### Out of scope (all stages unless Blueprint amended)

- Windows support
- Notebooks, GUI, mobile
- Framework zoo / multi-tenant marketplace
- Unlimited MCP/skill catalogs
- New package managers
- Granular coding backlogs as research outputs
- Product implementation beyond **bounded evidence spikes**
- Treating chat, model memory, or uncited “common knowledge” as authority

### Stage boundary rules

- One primary research question per focused stage (see Blueprint §11).
- Do not absorb architecture into ecosystem, or agent workflow into packaging.
- Dependent stages must not start until prerequisite reports are **accepted**.
- JIT prompts are generated only when prerequisites allow (`research-stage` skill).

## 4. Source Hierarchy

Higher tiers outrank lower tiers for **load-bearing** recommendations. Lower
tiers may surface failure modes and questions.

1. **Tier 1 — Primary / official:** Language and tool specifications; official
   docs; source repositories; first-party release notes and version pins;
   PEPs that are accepted/final where relevant; GitHub Actions official docs;
   Astral/uv/ruff/ty official docs; pytest docs; hk/fnox official docs; MCP and
   major agent product docs from first parties.
2. **Tier 2 — Authoritative analysis:** Maintainer design docs/ADRs; official
   security advisories; peer-reviewed or standards-body material; high-quality
   institutional guides.
3. **Tier 3 — Independent technical:** Reproducible benchmarks; production
   case studies with methods; careful independent write-ups with dated claims.
4. **Tier 4 — Community:** Issues, discussions, forums, practitioner anecdotes
   (including “what agents struggle with” reports).
5. **Tier 5 — Marketing / unsourced:** Vendor landing pages, undated blogs
   without methods, social posts without primary backup.

**Special sources for this program:**

| Source | Treatment |
| ------ | --------- |
| go-foundry research/spec/CLI | **Prior art** — cite as transferable design input; never as sole proof that a Python choice is correct |
| Owner preferences (discovery) | **User decision** class — record as constraints/candidates; still test against Tier 1–3 where Core is claimed |
| Agent product docs (Claude Code, Grok, etc.) | Tier 1 for *that product’s* behavior; do not overgeneralize across agents without evidence |
| PyPI download counts / GitHub stars | **Not** sufficient for Core inclusion (anti-popularity) |

## 5. Citation Rules

1. Prefer **portable** citations: Markdown links, numbered footnotes, and/or a
   **Source Ledger** table with URL, title, publisher/owner, and **access date**.
2. Do **not** rely solely on ephemeral UI citation chips or chat-only footnotes.
3. Every load-bearing factual claim in a focused report must map to a ledger
   entry or spike ID.
4. Quote version numbers and retrieval dates for tools that move quickly (uv,
   ruff, ty, Python, GitHub Actions runners, agent CLIs).
5. When citing go-foundry artifacts, use stable paths/URLs and state whether the
   claim is **parity hypothesis** or **adopted decision**.
6. Unpublished local experiments belong under **SPK-###** with environment notes,
   not as bare “we tried it.”

## 6. Current-Information Rules

As of the **actual research execution date**, re-verify claims that change:

- Tool and language versions, deprecations, default behaviors
- Packaging and lockfile semantics (`uv`, `pyproject.toml` fields)
- Type checker / linter capabilities and config schemas
- GitHub Actions runner images and recommended actions
- MCP protocol/features and agent skill formats
- Licensing of dependencies proposed for Core
- Security advisories for proposed Core tools

Stale knowledge from training data is **hypothesis** until re-verified. Mark
access dates. If a critical source is unavailable, open an **OQ-###** and lower
confidence rather than inventing.

## 7. Evidence-Spike Protocol

Follow `program/contracts/evidence-spike.md` and
`program/templates/evidence-spike.md`.

### When spikes are expected in this program

| Situation | Example |
| --------- | ------- |
| Contested Core tool | “ty vs alternative type checker for agent-edited code” |
| Generation semantics | Dry-run plan fidelity; write/rollback behavior |
| Agent operability | Agent can add a CLI command from docs alone on a sample layout |
| Layout / packaging | src layout + console scripts + uv workspace edge cases |
| Hooks/secrets | hk + fnox integration smoke on Linux and macOS |

### Constraints

- Bounded, decision-oriented, disposable prototype code
- Spike **reports** may be committed under `docs/evidence/`; prototype trees
  should not silently become the product architecture
- Document OS (Linux/macOS), Python version, tool versions, and limitations
- Consuming reports must not overgeneralize from one OS or one agent product

## 8. Evidence Ledger Format

Every focused research report includes an **Evidence Ledger** with at least:

| Field | Meaning |
| ----- | ------- |
| Evidence ID | `EVD-###` within the report (or program-stable if allocated) |
| Claim | Proposition supported |
| Classification | Per `program/contracts/evidence-model.md` |
| Source or spike | Citation or `SPK-###` |
| Source tier | 1–5 per §4 |
| Date | Publication, release, or experiment date |
| Access or execution date | When verified |
| Confidence | High \| Medium \| Low |
| Limitations | What it does not prove |
| Contradictory evidence | If any |
| Downstream use | `REC-###`, `REQ-###`, `DEC-###`, RSK, OQ |
| Revalidation trigger | When to re-check |

**Major recommendations** require: problem solved; requirements/constraints;
credible alternatives; supporting evidence; tradeoffs; confidence; failure
modes; revisit triggers. **Popularity alone is never sufficient.**

## 9. Recommendation Format

Use `program/templates/recommendation.md`. Stable IDs:

| Track | Range |
| ----- | ----- |
| research-python-ecosystem | REC-001..REC-099 |
| research-ai-native | REC-100..REC-199 |
| research-foundry-architecture | REC-200..REC-299 |

### Classification vocabulary

`Default` | `Required` | `Optional` | `Exception` | `Experimental` | `Watchlist` | `Rejected`

### Program-specific guidance

- Prefer **Default/Required** only for true Core candidates with Tier 1–3 support
  or explicit **User decision** + residual risk recorded.
- Use **Optional** for capability profiles (e.g. data/ETL, HTTP client bundle).
- Use **Watchlist** for promising tools not ready for Core.
- **Rejected** items keep their IDs forever (no reuse).
- Owner toolchain candidates that survive research should be labeled clearly as
  confirmed Default/Required vs demoted Optional/Watchlist/Rejected.

## 10. Evaluation Rubric

When comparing alternatives (tools, layouts, generation designs, agent
surfaces), score and narrate against:

| Criterion | Weight guidance (standard) |
| --------- | -------------------------- |
| Fit to locked constraints (Blueprint L1–L14) | Hard gate — fail = out |
| Agent operability (discoverability, docs, checks) | High |
| Correctness / failure visibility (validate, plan, tests) | High |
| Simplicity and closed-set discipline | High |
| Evidence quality and recency | High |
| Maintenance burden for a single owner + agents | Medium-high |
| Ecosystem momentum *with* primary docs (not stars alone) | Medium |
| Transfer/learning from go-foundry (reduce design risk) | Medium |
| Extensibility via profiles without Core bloat | Medium |
| Security/secrets hygiene (esp. fnox/hooks) | Medium |
| Performance/scale | Low unless architecture-changing |

Document tradeoffs explicitly. A “winner” that fails a hard gate is not a winner.

## 11. Confidence Model

| Level | Meaning |
| ----- | ------- |
| **High** | Strong Tier 1–2 evidence and/or reproducible spike; alternatives considered; residual risks named and small for this program |
| **Medium** | Credible evidence with gaps, single-platform spike, or moderate inference; safe to recommend with revisit triggers |
| **Low** | Weak/contradictory evidence, heavy inference, or owner preference without corroboration; may not be load-bearing for Core |

**Rules:**

- Confidence must track evidence quality; never inflate for narrative smoothness.
- Load-bearing Core (“Required in every generated project”) should aim for
  **High** or **Medium** with explicit RSK/OQ if Medium.
- **Low** confidence items are Watchlist/Optional/OQ material unless the owner
  explicitly accepts as User decision (record DEC if locked early).

## 12. Risk and Open-Question Format

### Risks — `RSK-###`

| Field | Content |
| ----- | ------- |
| Description | What could go wrong |
| Likelihood | High \| Medium \| Low |
| Impact | High \| Medium \| Low |
| Mitigation | Concrete reduction |
| Residual risk | What remains |
| Owner | Default: program owner |
| Trigger | When to re-evaluate |
| Related | REC/REQ/DEC/OQ/SPK |

### Open questions — `OQ-###`

| Field | Content |
| ----- | ------- |
| Question | Precise unknown |
| Blocking? | Yes/No for which stage |
| Owner | Default: program owner or stage agent |
| Resolution path | Research, spike, user decision, later phase |
| Deadline | Stage gate or “before synthesis” / “before implementation” |

Allocate RSK/OQ from shared ranges in the Blueprint; never reuse IDs.

## 13. Replication and Reconciliation Protocol

Follow `program/contracts/replication-reconciliation.md`.

- Program default: replication **enabled**, **not required**.
- Consider replication when a report makes a **contested load-bearing** claim
  with weak or single-source evidence (e.g. mandating a Core tool).
- Replicated runs use the **same prompt** independently; results go to distinct
  outputs; **reconciliation** is required before synthesis consumes them.
- Do not fake consensus; document residual disagreement as OQ/RSK.

## 14. Synthesis Rules

Follow `program/contracts/synthesis.md`.

- Synthesis consumes **accepted** research reports (and reconciliations if any).
- **No silent recommendation loss:** every REC is accepted, rejected, deferred,
  or merged with explicit disposition and traceability to REQ/DEC where needed.
- Resolve conflicts using Charter hierarchy, Blueprint locks, and evidence—not
  novelty or verbosity.
- Output: definitive specification with `REQ-001..REQ-299` as needed; honest
  open questions rather than false precision.
- Do not introduce major new subsystems that research never supported (review
  will attack feature ideation disguised as synthesis).

## 15. Adversarial-Review Rules

Follow `program/contracts/adversarial-review.md`.

- Review **attacks** the artifact: gaps, contradictions, weak evidence,
  scope creep, agent-operability failures, overfit to fashion, unsafe defaults.
- Findings use `FND-001..FND-199` (spec) and `FND-200..FND-399` (plan).
- Review is **not** a feature brainstorm; attractive extras without evidence are
  out of scope unless they expose a hole in stated requirements.
- Additional rounds only per **risk-triggered** policy (`research-program.toml`).
- Revision stages must disposition each finding: accept, accept-with-change,
  reject-with-rationale, or defer-with-OQ—no silent drops.

## 16. Validation Rules

Follow `program/contracts/validation.md` and the `research-validate` skill.

- Independent validation **before** human acceptance of substantive artifacts.
- Validators check structure, metadata, IDs, citations, ledgers, checklists,
  scope, authority, placeholders, and manifest consistency.
- Validators **fix mechanical defects only**; they do not invent research,
  citations, findings, or requirements.
- Placeholder status never counts as complete.

## 17. Handoff Rules

Follow `program/contracts/handoffs.md`.

- Fresh session per substantive stage; attachment manifests list only needed
  authority artifacts.
- Handoffs must be self-contained: goal, inputs, outputs, constraints, success
  criteria, and forbidden behaviors.
- Do not depend on “as discussed in chat.”
- Implementation handoff (end of program) points at **accepted revised
  specification** + **accepted revised plan** only.

## 18. Anti-Patterns

In addition to `program/reference/anti-patterns.md`, this program especially
forbids:

| Anti-pattern | Why it hurts here |
| ------------ | ----------------- |
| Chat-history authority | Breaks fresh-session research |
| Research by popularity | Stars ≠ Core fitness |
| Evidence-free confidence | Agents will encode false certainty into projects |
| Cargo-cult Core | Owner favorites without confirmation |
| Blind go-foundry copy | Wrong ecosystem assumptions |
| Framework zoo / MCP zoo | Reintroduces decision fatigue |
| Silent REC loss | Breaks synthesis integrity |
| Plan-as-backlog | Program stops at phases/milestones |
| Prototype capture | Spike code becomes accidental architecture |
| Windows “just in case” | Explicit non-goal |
| Placeholder completion | Unlocks work on empty files |

## 19. Completion Standards

### Focused research report

Complete only when:

1. Primary question answered within scope
2. Evidence Ledger present and load-bearing claims cited
3. REC-### items use the locked format and ID range
4. RSK/OQ allocated where needed
5. Confidence and limitations honest
6. Independent validation passes
7. Human accepts; manifest `accepted_commit` recorded

### Specification / plan / review / revision

Complete only when contract-required sections exist, IDs are valid, validation
passes, human accepts, and the manifest reflects acceptance.

### Program

Complete when revised definitive specification and revised implementation plan
are accepted as implementation and delivery authority
(`program/operator/completion-criteria.md`).

## 20. Canonical vocabulary (program-specific)

| Term | Meaning |
| ---- | ------- |
| **Foundry** | The python-foundry generator product being designed |
| **Generated Project** | Repository produced by the Foundry (or its default template surface) |
| **Core** | Files, tools, and behaviors included in every Generated Project |
| **Capability Profile** | Optional composed capability (not a second random template) |
| **Archetype** | Primary project shape (CLI, script, data/ETL, …) |
| **Project Specification** | Declarative input describing a project to generate |
| **Generation Plan** | Immutable plan produced before filesystem writes (dry-run) |
| **Agent surface** | Skills, MCP, LSP, instruction files, and checks for AI coding agents |
| **Prior art** | go-foundry research/CLI — reference only until adopted |

## 21. Inheritance

All later stages inherit this Charter. Conflicts with the Blueprint are
resolved by **Blueprint locks** unless a formal amendment or DEC supersedes.
Conflicts with methodology under `program/` are resolved by this Charter where
it specializes; otherwise by `program/contracts/`.

## Completion Checklist

- [x] All sections project-specialized where needed
- [x] Source hierarchy and citation rules explicit
- [x] Evidence Ledger and recommendation formats locked
- [x] Evaluation rubric and confidence model specialized
- [x] Spike, replication, synthesis, review, validation, handoff rules explicit
- [x] Anti-patterns and vocabulary specialized
- [x] Human accepts Charter
- [x] Manifest updated; accepting commit recorded
