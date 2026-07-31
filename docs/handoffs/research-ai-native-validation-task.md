# Validate AI-Native Repository & Agent Workflow research report

## When

After `docs/reports/02-ai-native-agent-workflow.md` exists and before human
acceptance.

## Read

1. `README.md`
2. `AGENTS.md`
3. `research-program.toml`
4. `docs/00-program-blueprint.md`
5. `docs/01-research-charter.md`
6. `docs/prompts/02-ai-native-agent-workflow-prompt.md`
7. `docs/handoffs/research-ai-native-attachment-manifest.md`
8. `docs/reports/01-modern-python-ecosystem.md` (accepted Core locks)
9. `program/contracts/focused-research-report.md`
10. `docs/reports/02-ai-native-agent-workflow.md`
11. Any `docs/evidence/SPK-05*-*.md` referenced by the report

Use the `research-validate` skill if available.

## Validate

- Required report sections present (metadata through completion checklist)
- Artifact metadata and **actual research date**
- Identifier uniqueness and ranges:
  - REC-100..199
  - RSK-050..099 (no reuse of ecosystem RSK-001..007 for new subjects)
  - OQ-050..099 (no reuse of ecosystem OQ-001..006 for new subjects)
  - SPK-050..099 if used
- Recommendation completeness (template fields; closed catalog discipline)
- Citation portability and source ledger access dates
- Evidence Ledger for load-bearing claims
- Risks and open questions
- Handoff Digest completeness
- Completion checklist truthfulness
- **Inherited Core locks respected:** ty Required; fnox+age Required; no dotenv secrets as Default; REC-013 command surface not contradicted
- Allowed file scope (no Blueprint/Charter/ecosystem report/manifest edits by the research agent)
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
docs: add AI-native agent workflow research prompt
```

After report accepted by human:

```text
docs: add AI-native agent workflow research report
```

Record `accepted_commit` on stage `research-ai-native` in
`research-program.toml` only after human acceptance.
