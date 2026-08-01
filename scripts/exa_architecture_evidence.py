#!/usr/bin/env python3
"""Gather Exa Deep evidence for research-foundry-architecture decision areas.

Not the focused research report. Outputs raw JSON + INDEX.md for assembly into
docs/reports/03-foundry-architecture.md.

Requires:
  export EXA_API_KEY=...

Usage:
  python3 scripts/exa_architecture_evidence.py --type deep-reasoning
  python3 scripts/exa_architecture_evidence.py --only cli-lifecycle,spec-format
  python3 scripts/exa_architecture_evidence.py --list
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
            "description": "Clear architectural decision for python-foundry generator.",
        },
        "classification": {
            "type": "string",
            "description": "One of: Required, Default, Optional, Rejected, Watchlist, Exception, Experimental.",
        },
        "rationale": {
            "type": "string",
            "description": "Evidence-based rationale; prefer official docs and proven generators.",
        },
        "alternatives": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Credible alternatives considered.",
        },
        "caveats": {
            "type": "string",
            "description": "Risks, dual-path drift, when not to apply.",
        },
        "confidence": {
            "type": "string",
            "description": "high, medium, or low based on source quality.",
        },
        "go_foundry_transfer": {
            "type": "string",
            "description": "Adopt | Adapt | Reject | N/A for related go-foundry patterns.",
        },
    },
}

BASE_SYSTEM = """You are gathering evidence for python-foundry FOUNDATION ARCHITECTURE research.

Hard constraints (do NOT re-litigate; design emit/wire only):
- Product: hybrid Python/uv foundry CLI + strong default Core + optional GitHub template surface.
- Targets: macOS and Linux only (never Windows).
- Archetypes: CLI apps, scripts, data/ETL (no notebooks, no web framework zoo).
- Inherited Generated Project Core: Python floor 3.12 / default 3.13; uv + uv.lock; src/ layout;
  Ruff; ty Required; pytest; pre-commit Default; fnox+age Required; no .env/dotenv secrets;
  GitHub Actions with setup-uv + ruff + ty + pytest; Typer default for CLI archetype.
- Profiles: http (httpx), hooks-hk (hk), data-etl (polars+pyarrow).
- Command surface: uv sync / uv run … / fnox exec -- ….
- AI-native emit: root AGENTS.md only; skills under .agents/skills/ only; no CLAUDE.md/.claude/;
  MCP default none; no Claude Code as design target.
- Closed catalogs only — no marketplace, no unlimited plugins/MCP/skills.
- go-foundry (research + CLI) is PRIOR ART only: adapt, do not copy blindly.
- Prefer primary/official docs and well-known generator tools (copier, cookiecutter, cruft, etc.).
- Be concrete about CLI lifecycle, plan/dry-run, write semantics, catalog structure.
- If evidence is weak or contradictory, say so and lower confidence.
- Do not invent Windows support, multi-tenant marketplaces, or coding backlogs as architecture.
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
        id="cli-lifecycle",
        title="Generator CLI lifecycle (validate / plan / generate)",
        query=(
            "For a personal project generator CLI in 2026, what is a robust command lifecycle "
            "for validate, plan/dry-run, and generate/apply? Cover fail-closed validation, "
            "exit codes, dry-run vs apply separation, and patterns from copier, cookiecutter, "
            "and infrastructure tools (terraform plan/apply style). Prefer official docs."
        ),
        include_domains=(
            "copier.readthedocs.io",
            "cookiecutter.readthedocs.io",
            "developer.hashicorp.com",
            "github.com",
        ),
    ),
    QuerySpec(
        id="spec-format",
        title="Project specification format for generators",
        query=(
            "What input specification formats work best for project generators in 2026: "
            "YAML/TOML/JSON schema, CLI flags only, interactive prompts, or hybrid? "
            "Cover versioning, agent-editability, validation, and cookiecutter cookiecutter.json "
            "vs copier answers vs declarative project specs. Prefer official docs and design guides."
        ),
        include_domains=(
            "copier.readthedocs.io",
            "cookiecutter.readthedocs.io",
            "json-schema.org",
            "toml.io",
            "github.com",
        ),
    ),
    QuerySpec(
        id="plan-binding",
        title="Plan dry-run model and binding to generate",
        query=(
            "How should a generator dry-run plan bind to the actual generate step? Compare "
            "plan-as-preview (informative only) vs plan-as-contract (generate must match plan), "
            "plan files on disk, and failure modes when plan and write diverge. Examples from "
            "terraform plan, kubectl dry-run, copier/cookiecutter preview modes if any."
        ),
        include_domains=(
            "developer.hashicorp.com",
            "kubernetes.io",
            "copier.readthedocs.io",
            "github.com",
        ),
    ),
    QuerySpec(
        id="write-semantics",
        title="Filesystem write, overwrite, and fail-closed semantics",
        query=(
            "What filesystem write semantics should a project generator use on macOS/Linux for "
            "v1: atomic write, temp-dir then move, skip existing, fail on conflict, overwrite "
            "flags? Cover partial-write recovery, empty target directory requirements, and "
            "patterns from cookiecutter, copier, and scaffolding tools."
        ),
        include_domains=(
            "copier.readthedocs.io",
            "cookiecutter.readthedocs.io",
            "github.com",
        ),
    ),
    QuerySpec(
        id="catalog-model",
        title="Closed catalog model for templates and profiles",
        query=(
            "How should a closed catalog of project templates, fragments, profiles, and emitted "
            "agent skills be structured for a non-marketplace personal foundry? Cover versioning, "
            "Core vs optional profile membership, composition of template fragments, and "
            "anti-patterns of unbounded plugin catalogs. Prefer design docs and copier/cookiecutter "
            "template organization practices."
        ),
        include_domains=(
            "copier.readthedocs.io",
            "cookiecutter.readthedocs.io",
            "github.com",
        ),
    ),
    QuerySpec(
        id="archetype-profiles",
        title="Archetype and profile composition",
        query=(
            "How should project generators compose base archetypes (CLI app, scripts, data/ETL) "
            "with optional capability profiles (http client, hooks variant, data stack) without "
            "combinatorial explosion? Cover conflict rules, mutual exclusion, dependency expansion, "
            "and closed-set discipline for personal tooling generators."
        ),
        include_domains=(
            "copier.readthedocs.io",
            "cookiecutter.readthedocs.io",
            "github.com",
        ),
    ),
    QuerySpec(
        id="template-vs-generator",
        title="GitHub template surface vs generator single source of truth",
        query=(
            "How should a hybrid foundry keep a GitHub template repository coherent with a "
            "generator CLI without dual-source drift? Compare generate-from-catalog as SoT, "
            "template-as-SoT, dual-path with CI parity checks, and Use-this-template flows. "
            "Prefer GitHub template docs and generator maintainership lessons."
        ),
        include_domains=(
            "docs.github.com",
            "github.com",
            "copier.readthedocs.io",
        ),
    ),
    QuerySpec(
        id="emit-ai-native-core",
        title="Emitting Core toolchain and AI-native surfaces from generators",
        query=(
            "How should a Python project generator emit a locked Core (uv, ruff, ty, pytest, "
            "fnox, GitHub Actions, src layout) plus AI-native surfaces (AGENTS.md, .agents/skills) "
            "as invariants rather than optional extras? Cover template invariants, post-generate "
            "verification, and preventing agents from inventing alternate toolchains or dotenv."
        ),
        include_domains=(
            "docs.astral.sh",
            "agents.md",
            "agentskills.io",
            "docs.github.com",
            "github.com",
        ),
    ),
    QuerySpec(
        id="post-generate-verify",
        title="Post-generate verification policy",
        query=(
            "Should a project generator run quality gates (uv sync, ruff, typecheck, pytest) "
            "after generate, or only document commands for humans/agents? Cover tradeoffs of "
            "in-generator verification vs agent definition-of-done, CI bootstrap, and timeout/cost "
            "for personal CLIs on macOS/Linux."
        ),
        include_domains=(
            "docs.astral.sh",
            "docs.pytest.org",
            "docs.github.com",
            "github.com",
        ),
    ),
    QuerySpec(
        id="python-cli-module-layout",
        title="Python CLI product module layout for a foundry",
        query=(
            "What package/module layout suits a Python/uv CLI tool that validates specs, builds "
            "generation plans, and renders catalogs (e.g. cli/, domain/, catalog/, render/, plan/)? "
            "Prefer src layout, Typer/Click app structure, and maintainable boundaries for dogfooding."
        ),
        include_domains=(
            "docs.astral.sh",
            "typer.tiangolo.com",
            "packaging.python.org",
            "github.com",
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
            "User-Agent": "python-foundry-exa-architecture-evidence/0.1",
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
        "# Exa architecture evidence run",
        "",
        f"- **Started (UTC):** {meta['started_utc']}",
        f"- **Finished (UTC):** {meta['finished_utc']}",
        f"- **Search type:** `{meta['search_type']}`",
        f"- **Queries:** {meta['query_count']}",
        f"- **Total cost (USD):** {meta.get('total_cost')}",
        f"- **Total elapsed (s):** {meta.get('total_elapsed')}",
        "",
        "This is **raw evidence**, not an accepted research report.",
        "Assemble into `docs/reports/03-foundry-architecture.md` with Charter rules.",
        "",
        "## Per-query summaries",
        "",
    ]
    for rec in records:
        lines.append(f"### `{rec.get('query_id', '?')}` — {rec.get('title', '')}")
        lines.append("")
        if rec.get("error"):
            lines.append(f"- **ERROR:** {rec['error']}")
            lines.append("")
            continue
        lines.append(f"- File: `{rec['query_id']}.json`")
        lines.append(f"- Elapsed: {rec.get('elapsed_seconds')}s")
        lines.append(f"- Cost: {rec.get('cost_dollars')}")
        content = rec.get("output_content")
        if isinstance(content, dict):
            lines.append(f"- **Classification:** {content.get('classification', '—')}")
            lines.append(f"- **Confidence:** {content.get('confidence', '—')}")
            lines.append(f"- **go-foundry transfer:** {content.get('go_foundry_transfer', '—')}")
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
    parser = argparse.ArgumentParser(description="Exa Deep evidence for foundry architecture")
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
    run_dir = args.out_dir or (ROOT / "scripts" / "exa-output" / f"architecture-{stamp}")
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
