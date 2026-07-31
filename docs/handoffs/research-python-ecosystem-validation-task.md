# Validate Modern Python Ecosystem research report

## When

After `docs/reports/01-modern-python-ecosystem.md` exists and before human
acceptance.

## Read

1. `README.md`
2. `AGENTS.md`
3. `research-program.toml`
4. `docs/00-program-blueprint.md`
5. `docs/01-research-charter.md`
6. `docs/prompts/01-modern-python-ecosystem-prompt.md`
7. `docs/handoffs/research-python-ecosystem-attachment-manifest.md`
8. `program/contracts/focused-research-report.md`
9. `docs/reports/01-modern-python-ecosystem.md`
10. Any `docs/evidence/SPK-00*-*.md` referenced by the report

Use the `research-validate` skill if available.

## Validate

- Required report sections present (metadata through completion checklist)
- Artifact metadata and **actual research date**
- Identifier uniqueness and ranges: REC-001..099, RSK-001..049, OQ-001..049, SPK-001..049
- Recommendation completeness (template fields; L5 candidate disposition)
- Citation portability and source ledger access dates
- Evidence Ledger for load-bearing claims
- Risks and open questions
- Handoff Digest completeness
- Completion checklist truthfulness
- Allowed file scope (no Blueprint/Charter/manifest edits by the research agent)
- Manifest status transition readiness (`awaiting-validation` → human accept)
- Git diff limited to report (+ optional evidence spikes)

## Rules

- Do not fabricate missing research content.
- Fix **mechanical** defects only (headings, metadata, broken ID formatting, checklist typos).
- Report substantive defects; set stage to `requires-revision` if needed.
- Do not mark `accepted` without human approval and commit hash.

## Recommended commit messages

Prompt install (this package — if not already committed):

```text
docs: add modern python ecosystem research prompt
```

After report accepted by human:

```text
docs: add modern python ecosystem research report
```

Record `accepted_commit` on stage `research-python-ecosystem` in
`research-program.toml` only after human acceptance.
