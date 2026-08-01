# Validate Foundry Architecture research report

## When

After `docs/reports/03-foundry-architecture.md` exists and before human
acceptance.

## Read

1. `README.md`
2. `AGENTS.md`
3. `research-program.toml`
4. `docs/00-program-blueprint.md`
5. `docs/01-research-charter.md`
6. `docs/prompts/03-foundry-architecture-prompt.md`
7. `docs/handoffs/research-foundry-architecture-attachment-manifest.md`
8. `docs/reports/01-modern-python-ecosystem.md` (accepted Core locks)
9. `docs/reports/02-ai-native-agent-workflow.md` (accepted AI-native locks)
10. `program/contracts/focused-research-report.md`
11. `docs/reports/03-foundry-architecture.md`
12. Any `docs/evidence/SPK-10*-*.md` referenced by the report

Use the `research-validate` skill if available.

## Validate

- Required report sections present (metadata through completion checklist)
- Artifact metadata and **actual research date**
- Identifier uniqueness and ranges:
  - REC-200..299
  - RSK-100..149 (no reuse of RSK-001..007 or RSK-050..056 for new subjects)
  - OQ-100..149 (no reuse of OQ-001..006 or OQ-050..055 for new subjects)
  - SPK-100..149 if used
- Recommendation completeness (template fields; closed catalog discipline)
- Citation portability and source ledger access dates
- Evidence Ledger for load-bearing claims
- Risks and open questions
- Handoff Digest completeness (synthesis-oriented)
- Required tables present (CLI lifecycle, spec, plan, write semantics, catalog,
  composition, emit contract, module map, go-foundry transfer, anti-patterns)
- Completion checklist truthfulness
- **Inherited ecosystem Core locks respected:** ty Required; fnox+age Required;
  no dotenv secrets as Default; REC-013/014 not contradicted
- **Inherited AI-native locks respected:** AGENTS.md + `.agents/` only; no Claude
  adapters as Default emit; MCP default none
- go-foundry treated as prior art (Adopt/Adapt/Reject), not sole authority
- Allowed file scope (no Blueprint/Charter/G1 report/manifest edits by the
  research agent)
- Manifest status transition readiness (`awaiting-validation` → human accept)
- Git diff limited to report (+ optional evidence spikes)

## Rules

- Do not fabricate missing research content.
- Fix **mechanical** defects only (headings, metadata, broken ID formatting,
  checklist typos).
- Report substantive defects; set stage to `requires-revision` if needed.
- Do not mark `accepted` without human approval and commit hash.

## Recommended commit messages

Prompt install (this package — if not already committed):

```text
docs: add foundry architecture research prompt
```

After report accepted by human:

```text
docs: add foundry architecture research report
```

Record `accepted_commit` on stage `research-foundry-architecture` in
`research-program.toml` only after human acceptance.
