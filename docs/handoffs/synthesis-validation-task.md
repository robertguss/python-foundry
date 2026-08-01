# Validate Definitive Specification (synthesis)

## When

After `docs/specifications/01-definitive-specification.md` exists (non-placeholder)
and before human acceptance.

## Read

1. `README.md`
2. `AGENTS.md`
3. `research-program.toml`
4. `docs/00-program-blueprint.md`
5. `docs/01-research-charter.md`
6. `docs/prompts/04-chief-architect-synthesis-prompt.md`
7. `docs/handoffs/synthesis-attachment-manifest.md`
8. `docs/reports/01-modern-python-ecosystem.md` (accepted Core locks)
9. `docs/reports/02-ai-native-agent-workflow.md` (accepted AI-native locks)
10. `docs/reports/03-foundry-architecture.md` (accepted architecture locks)
11. `program/contracts/synthesis.md`
12. `program/contracts/definitive-specification.md`
13. `program/templates/requirement.md`
14. `docs/specifications/01-definitive-specification.md`

Use the `research-validate` skill if available.

## Validate

- Required specification sections present (metadata through handoff to review)
- Artifact metadata and **actual synthesis date**
- Status is **Proposed — pending adversarial review** (not Accepted; not Placeholder)
- Identifier uniqueness and ranges:
  - REQ-001..REQ-299 only for new requirements
  - No reuse of REC IDs as REQs; no minting new RECs in synthesis
- **Recommendation Disposition Ledger complete** for:
  - REC-001..REC-014
  - REC-100..REC-112
  - REC-200..REC-212
  - Each row has exactly one allowed disposition
- Requirement completeness (template fields for Must REQs; verification paths)
- Traceability matrix covers normative REQs
- Risk register and open questions present; upstream RSK/OQ not silently dropped
- Deferred Work and Rejected Work present where dispositions require them
- High-level phases present; **no** granular coding backlog as primary content
- Portable citations where claims need them (no ephemeral-only authority)
- Completion checklist truthfulness
- **Inherited ecosystem Core locks respected:** ty Required; fnox+age Required;
  no dotenv secrets; REC-013/014 not contradicted
- **Inherited AI-native locks respected:** AGENTS.md + `.agents/` only; no Claude
  adapters as Default emit; MCP default none
- **Inherited architecture locks respected:** validate → plan → generate; TOML
  spec; plan-as-contract; exclusive place; closed catalog; custom engine; GitHub
  template = generated snapshot; Core + AI-native emit as invariants
- Blueprint non-goals preserved (Windows, notebooks, marketplace, framework zoo)
- Standalone character: specification is implementation-oriented without requiring
  chat history
- Allowed file scope (no Blueprint/Charter/report/prompt/manifest edits by the
  synthesis agent)
- Manifest status transition readiness (`awaiting-validation` → human accept)
- Git diff limited to the specification (and any explicitly allowed paths)

## Rules

- Do not fabricate missing research content or invent dispositions for unread RECs.
- Fix **mechanical** defects only (headings, metadata, broken ID formatting,
  checklist typos, missing section labels).
- Report substantive defects; set stage to `requires-revision` if needed.
- Do not mark `accepted` without human approval and commit hash.

## Recommended commit messages

Prompt install (this package — if not already committed):

```text
docs: add chief architect synthesis prompt
```

After specification accepted by human:

```text
docs: add definitive specification
```

Record `accepted_commit` on stage `synthesis` in `research-program.toml` only
after human acceptance.
