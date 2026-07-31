#!/usr/bin/env python3
"""Gather Exa Deep evidence for research-ai-native decision areas.

Not the focused research report. Outputs raw JSON + INDEX.md for assembly into
docs/reports/02-ai-native-agent-workflow.md.

Requires:
  export EXA_API_KEY=...

Usage:
  python3 scripts/exa_ai_native_evidence.py --type deep-reasoning
  python3 scripts/exa_ai_native_evidence.py --only skills,mcp
  python3 scripts/exa_ai_native_evidence.py --list
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

API_URL = "https://api.exa.ai/search"
ROOT = Path(__file__).resolve().parents[1]

COMMON_SCHEMA: dict[str, Any] = {
    "type": "object",
    "required": [
        "recommendation",
        "classification",
        "rationale",
        "alternatives",
        "caveats",
        "confidence",
    ],
    "properties": {
        "recommendation": {
            "type": "string",
            "description": "Clear decision for python-foundry agent surface (foundry and/or Generated Projects).",
        },
        "classification": {
            "type": "string",
            "description": "One of: Required, Default, Optional, Rejected, Watchlist, Exception, Experimental.",
        },
        "rationale": {
            "type": "string",
            "description": "Evidence-based rationale; prefer official agent product docs and standards.",
        },
        "alternatives": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Credible alternatives considered.",
        },
        "caveats": {
            "type": "string",
            "description": "Risks, multi-agent gaps, when not to apply.",
        },
        "confidence": {
            "type": "string",
            "description": "high, medium, or low based on source quality.",
        },
        "applies_to": {
            "type": "string",
            "description": "generated-projects | foundry-repo | both",
        },
    },
}

BASE_SYSTEM = """You are gathering evidence for python-foundry AI-native agent workflow research.

Hard constraints:
- Targets: macOS and Linux only (never Windows).
- Primary implementers: AI coding agents (Grok, Claude Code, Cursor, similar).
- Prefer closed, curated agent tooling — no unlimited skill/MCP kitchen sinks.
- Inherited Core (do not re-litigate): uv, ruff, ty Required, pytest, fnox+age secrets,
  no .env/dotenv secret storage, command surface uv sync / uv run … / fnox exec -- ….
- Prefer primary/official product docs over blogs and marketing.
- Be concrete about file paths, discovery rules, and defaults when known.
- If evidence is weak or contradictory across agents, say so and lower confidence.
- Do not invent Windows support or multi-tenant requirements.
"""


@dataclass(frozen=True)
class QuerySpec:
    id: str
    title: str
    query: str
    include_domains: tuple[str, ...] = ()
    num_results: int = 8
    system_extra: str = ""


QUERIES: list[QuerySpec] = [
    QuerySpec(
        id="instruction-files",
        title="Agent instruction files (AGENTS.md vs product adapters)",
        query=(
            "For multi-agent coding projects in 2026 (Claude Code, Cursor, Grok Build, Codex), "
            "what instruction files should a Python project generator emit? Cover AGENTS.md "
            "as portable source of truth, CLAUDE.md adapters (@AGENTS.md import or symlink), "
            ".cursor/rules vs AGENTS.md, and whether product-only trees are Required or Optional. "
            "Prefer official docs: agents.md, code.claude.com/docs, cursor.com/docs, docs.x.ai."
        ),
        include_domains=(
            "agents.md",
            "code.claude.com",
            "docs.anthropic.com",
            "cursor.com",
            "docs.x.ai",
            "github.com",
        ),
    ),
    QuerySpec(
        id="skills-layout",
        title="Portable skills layout and closed catalogs",
        query=(
            "What is the portable Agent Skills layout for multi-product coding agents in 2026? "
            "Cover .agents/skills/<name>/SKILL.md, product-specific paths (.claude/skills, "
            ".cursor/skills), SKILL.md frontmatter requirements, progressive disclosure, and "
            "whether generators should dual-emit skills. Prefer agentskills.io and official "
            "Claude Code, Cursor, Codex, VS Code agent skills docs."
        ),
        include_domains=(
            "agentskills.io",
            "code.claude.com",
            "cursor.com",
            "developers.openai.com",
            "code.visualstudio.com",
            "docs.x.ai",
        ),
    ),
    QuerySpec(
        id="mcp-curation",
        title="Curated MCP defaults vs none",
        query=(
            "For personal local Python CLI/script projects on macOS/Linux in 2026, should a "
            "project generator commit a default MCP server set, a minimal curated set, or none? "
            "Cover context cost of connected MCP tools, .mcp.json project scope, Claude Code MCP "
            "docs, Cursor/VS Code/Grok MCP config paths, and kitchen-sink failure modes. Prefer "
            "official MCP and agent product docs."
        ),
        include_domains=(
            "modelcontextprotocol.io",
            "code.claude.com",
            "cursor.com",
            "code.visualstudio.com",
            "docs.github.com",
            "docs.x.ai",
        ),
    ),
    QuerySpec(
        id="lsp-diagnostics",
        title="LSP and diagnostics for ruff and ty",
        query=(
            "How should AI coding agents and editors get lint and type diagnostics for Python "
            "projects using Ruff and Astral ty in 2026? Cover official Ruff LSP/editor setup, "
            "ty language server or check CLI, VS Code/Cursor extensions, and agent-facing "
            "command surface (uv run ruff, uv run ty). Prefer docs.astral.sh for ruff and ty."
        ),
        include_domains=(
            "docs.astral.sh",
            "github.com",
            "marketplace.visualstudio.com",
        ),
    ),
    QuerySpec(
        id="secrets-agents-fnox",
        title="Agent secrets protocol with fnox and age",
        query=(
            "How should AI coding agents run commands that need secrets using fnox with age "
            "provider, without teaching agents to use .env or python-dotenv for secret storage? "
            "Cover fnox exec patterns, fnox.toml, age keys, and common agent failure modes. "
            "Prefer official fnox docs (fnox.jdx.dev) and age documentation."
        ),
        include_domains=(
            "fnox.jdx.dev",
            "github.com",
            "age-encryption.org",
        ),
    ),
    QuerySpec(
        id="command-surface-agents",
        title="Agent verification command surface",
        query=(
            "For uv-based Python projects with ruff, ty, pytest, pre-commit, and fnox in 2026, "
            "what minimal command surface should AGENTS.md and skills document so coding agents "
            "lint, typecheck, test, and run secrets-aware entrypoints consistently? Prefer "
            "official uv, ruff, ty, pytest, pre-commit, and fnox docs."
        ),
        include_domains=(
            "docs.astral.sh",
            "docs.pytest.org",
            "pre-commit.com",
            "fnox.jdx.dev",
        ),
    ),
    QuerySpec(
        id="multi-agent-adapters",
        title="Multi-agent product strategy without unbounded forks",
        query=(
            "What is the best strategy in 2026 for supporting Claude Code, Cursor, Grok Build, "
            "and similar coding agents without maintaining unbounded per-product instruction "
            "and skill forks? Cover portable-first AGENTS.md + thin adapters, symlink patterns, "
            "and when product-specific trees are justified. Prefer official multi-product docs "
            "and agents.md / agentskills standards."
        ),
        include_domains=(
            "agents.md",
            "agentskills.io",
            "code.claude.com",
            "cursor.com",
            "docs.x.ai",
        ),
    ),
    QuerySpec(
        id="definition-of-done",
        title="Agent definition of done and verification hooks",
        query=(
            "What definition-of-done checks should AI coding agents run before claiming work "
            "complete on a Python CLI/script repo with uv, ruff, ty, pytest, and optional "
            "pre-commit? Cover CI parity, local gates, and anti-patterns (empty tests, skipped "
            "typecheck, inventing dotenv). Prefer official tool docs and practical agent-ops guides."
        ),
        include_domains=(
            "docs.astral.sh",
            "docs.pytest.org",
            "pre-commit.com",
            "docs.github.com",
        ),
    ),
]


def post_search(api_key: str, payload: dict[str, Any], timeout_s: float) -> dict[str, Any]:
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        API_URL,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
            "User-Agent": "python-foundry-exa-ai-native-evidence/0.1",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout_s) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code}: {err_body}") from e


def run_one(
    api_key: str,
    spec: QuerySpec,
    *,
    search_type: str,
    timeout_s: float,
) -> dict[str, Any]:
    system = BASE_SYSTEM
    if spec.system_extra:
        system = system + "\n" + spec.system_extra

    payload: dict[str, Any] = {
        "query": spec.query,
        "type": search_type,
        "numResults": spec.num_results,
        "systemPrompt": system,
        "outputSchema": COMMON_SCHEMA,
        "contents": {"highlights": True},
    }
    if spec.include_domains:
        payload["includeDomains"] = list(spec.include_domains)

    t0 = time.perf_counter()
    data = post_search(api_key, payload, timeout_s=timeout_s)
    elapsed = time.perf_counter() - t0

    return {
        "query_id": spec.id,
        "title": spec.title,
        "search_type": search_type,
        "elapsed_seconds": round(elapsed, 2),
        "request_payload": {
            "query": spec.query,
            "type": search_type,
            "includeDomains": list(spec.include_domains) if spec.include_domains else None,
            "numResults": spec.num_results,
        },
        "response": data,
        "cost_dollars": (data.get("costDollars") or {}).get("total"),
        "output_content": (data.get("output") or {}).get("content"),
        "grounding": (data.get("output") or {}).get("grounding"),
        "result_urls": [
            {"title": r.get("title"), "url": r.get("url")} for r in (data.get("results") or [])
        ],
    }


def write_index_md(run_dir: Path, records: list[dict[str, Any]], meta: dict[str, Any]) -> None:
    lines: list[str] = [
        "# Exa AI-native evidence run",
        "",
        f"- **Started (UTC):** {meta['started_utc']}",
        f"- **Finished (UTC):** {meta['finished_utc']}",
        f"- **Search type:** `{meta['search_type']}`",
        f"- **Queries:** {meta['query_count']}",
        f"- **Total cost (USD):** {meta.get('total_cost')}",
        f"- **Total elapsed (s):** {meta.get('total_elapsed')}",
        "",
        "This is **raw evidence**, not an accepted research report.",
        "Assemble into `docs/reports/02-ai-native-agent-workflow.md` with Charter rules.",
        "",
        "## Per-query summaries",
        "",
    ]
    for rec in records:
        lines.append(f"### `{rec['query_id']}` — {rec['title']}")
        lines.append("")
        lines.append(f"- File: `{rec['query_id']}.json`")
        lines.append(f"- Elapsed: {rec.get('elapsed_seconds')}s")
        lines.append(f"- Cost: {rec.get('cost_dollars')}")
        content = rec.get("output_content")
        if isinstance(content, dict):
            lines.append(f"- **Classification:** {content.get('classification', '—')}")
            lines.append(f"- **Confidence:** {content.get('confidence', '—')}")
            lines.append(f"- **Applies to:** {content.get('applies_to', '—')}")
            lines.append(f"- **Recommendation:** {content.get('recommendation', '—')}")
            lines.append("")
            lines.append(f"**Rationale:** {content.get('rationale', '—')}")
            lines.append("")
            alts = content.get("alternatives") or []
            if alts:
                lines.append("**Alternatives:**")
                for a in alts:
                    lines.append(f"- {a}")
                lines.append("")
            if content.get("caveats"):
                lines.append(f"**Caveats:** {content['caveats']}")
                lines.append("")
        elif content:
            lines.append(f"- Output: {content}")
            lines.append("")
        else:
            lines.append("- Output: _(missing)_")
            lines.append("")

        urls = rec.get("result_urls") or []
        if urls:
            lines.append("**Top results:**")
            for u in urls[:8]:
                lines.append(f"- [{u.get('title') or u.get('url')}]({u.get('url')})")
            lines.append("")

    (run_dir / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Exa Deep evidence for AI-native research")
    parser.add_argument(
        "--type",
        default="deep-reasoning",
        choices=["deep-lite", "deep", "deep-reasoning"],
    )
    parser.add_argument("--only", default="", help="Comma-separated query ids")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--timeout", type=float, default=180.0)
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument("--sleep", type=float, default=0.5)
    args = parser.parse_args()

    if args.list:
        for q in QUERIES:
            print(f"{q.id:28} {q.title}")
        return 0

    api_key = os.environ.get("EXA_API_KEY", "").strip()
    if not api_key:
        print("EXA_API_KEY is not set", file=sys.stderr)
        return 2

    only = {x.strip() for x in args.only.split(",") if x.strip()}
    selected = [q for q in QUERIES if not only or q.id in only]
    if only:
        missing = only - {q.id for q in selected}
        if missing:
            print(f"Unknown query ids: {sorted(missing)}", file=sys.stderr)
            return 2
    if not selected:
        print("No queries selected", file=sys.stderr)
        return 2

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = args.out_dir or (ROOT / "scripts" / "exa-output" / f"ai-native-{stamp}")
    run_dir.mkdir(parents=True, exist_ok=True)

    started = datetime.now(timezone.utc).isoformat()
    records: list[dict[str, Any]] = []
    total_cost = 0.0
    total_elapsed = 0.0

    for i, spec in enumerate(selected):
        print(f"[{i+1}/{len(selected)}] {spec.id} …", file=sys.stderr, flush=True)
        try:
            rec = run_one(api_key, spec, search_type=args.type, timeout_s=args.timeout)
            records.append(rec)
            (run_dir / f"{spec.id}.json").write_text(
                json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
            )
            c = rec.get("cost_dollars")
            if isinstance(c, (int, float)):
                total_cost += float(c)
            total_elapsed += float(rec.get("elapsed_seconds") or 0)
            content = rec.get("output_content") or {}
            rec_line = content.get("recommendation", "") if isinstance(content, dict) else ""
            print(
                f"  ok {rec.get('elapsed_seconds')}s cost={c} rec={str(rec_line)[:100]}",
                file=sys.stderr,
                flush=True,
            )
        except Exception as e:
            err = {"query_id": spec.id, "title": spec.title, "error": str(e)}
            records.append(err)
            (run_dir / f"{spec.id}.json").write_text(
                json.dumps(err, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
            )
            print(f"  FAIL: {e}", file=sys.stderr, flush=True)
        if i + 1 < len(selected) and args.sleep > 0:
            time.sleep(args.sleep)

    finished = datetime.now(timezone.utc).isoformat()
    meta = {
        "started_utc": started,
        "finished_utc": finished,
        "search_type": args.type,
        "query_count": len(selected),
        "total_cost": round(total_cost, 4),
        "total_elapsed": round(total_elapsed, 2),
    }
    (run_dir / "meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    write_index_md(run_dir, records, meta)
    print(f"INDEX → {run_dir / 'INDEX.md'}", file=sys.stderr)
    print(f"total cost≈${total_cost:.4f} elapsed≈{total_elapsed:.1f}s", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
