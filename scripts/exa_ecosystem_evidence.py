#!/usr/bin/env python3
"""Gather Exa Deep evidence for research-python-ecosystem decision areas.

Not the focused research report. Outputs raw JSON + a human-readable index
for later assembly into docs/reports/01-modern-python-ecosystem.md.

Requires:
  export EXA_API_KEY=...

Usage:
  python3 scripts/exa_ecosystem_evidence.py
  python3 scripts/exa_ecosystem_evidence.py --type deep-reasoning
  python3 scripts/exa_ecosystem_evidence.py --only python-version,uv-packaging
  python3 scripts/exa_ecosystem_evidence.py --list

Docs: https://exa.ai/docs/reference/search-api-guide
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

# Exa limits: max nesting depth 2, max ~10 properties total.
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
            "description": "Clear decision for python-foundry Core or profiles.",
        },
        "classification": {
            "type": "string",
            "description": "One of: Required, Default, Optional, Rejected, Watchlist, Exception.",
        },
        "rationale": {
            "type": "string",
            "description": "Evidence-based rationale; prefer official docs.",
        },
        "alternatives": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Credible alternatives considered.",
        },
        "caveats": {
            "type": "string",
            "description": "Risks, maturity issues, when not to apply.",
        },
        "confidence": {
            "type": "string",
            "description": "high, medium, or low based on source quality.",
        },
        "suggested_core_or_profile": {
            "type": "string",
            "description": "core | profile:<name> | none",
        },
    },
}

BASE_SYSTEM = """You are gathering evidence for a personal AI-native Python project foundry (python-foundry).

Hard constraints:
- Targets: macOS and Linux only (never Windows).
- Archetypes: CLI apps, scripts, and data/ETL (no notebooks, no web framework zoo).
- Packaging baseline candidate: uv.
- Primary implementers are AI coding agents; prefer simple, documented, closed defaults.
- Prefer primary/official documentation over blogs and marketing.
- Be concrete about versions, defaults, and config when known.
- If evidence is weak or contradictory, say so and lower confidence.
- Do not invent Windows support or multi-tenant product requirements.
"""


@dataclass(frozen=True)
class QuerySpec:
    id: str
    title: str
    query: str
    include_domains: tuple[str, ...] = ()
    num_results: int = 8
    # Extra system prompt fragment
    system_extra: str = ""


QUERIES: list[QuerySpec] = [
    QuerySpec(
        id="python-version",
        title="Python version floor and default",
        query=(
            "For new personal Python CLI and script projects in 2026 on macOS and Linux, "
            "what should the minimum and default Python versions be? Consider CPython EOL "
            "dates, security support, library compatibility, and uv Tier 1 supported versions. "
            "Prefer docs.python.org, PEPs, endoflife data, and docs.astral.sh/uv."
        ),
        include_domains=(
            "docs.astral.sh",
            "docs.python.org",
            "peps.python.org",
            "devguide.python.org",
        ),
    ),
    QuerySpec(
        id="uv-packaging",
        title="uv as project and package manager",
        query=(
            "Should uv be the default project and package manager for new Python CLI/script "
            "projects in 2026 instead of Poetry, PDM, Hatch, or pip+venv+pip-tools? "
            "Cover pyproject.toml workflow, lockfiles (uv.lock), dependency groups, "
            "console scripts, and publishing. Prefer official Astral uv docs and "
            "packaging.python.org."
        ),
        include_domains=("docs.astral.sh", "packaging.python.org", "github.com"),
    ),
    QuerySpec(
        id="project-layout",
        title="Project layout for CLI, scripts, data/ETL",
        query=(
            "What project directory layouts are recommended in 2026 for (1) installable CLI "
            "packages with console entry points, (2) simple scripts, and (3) data/ETL tools "
            "using uv and pyproject.toml? Discuss src layout vs flat layout, package naming, "
            "and where tests live. Prefer packaging.python.org, Hatchling/setuptools docs, "
            "and Astral uv project guides."
        ),
        include_domains=(
            "packaging.python.org",
            "docs.astral.sh",
            "setuptools.pypa.io",
            "hatch.pypa.io",
        ),
    ),
    QuerySpec(
        id="ruff-lint-format",
        title="Ruff for lint and format",
        query=(
            "Should Ruff be the default linter and formatter for new Python projects in 2026 "
            "instead of flake8+isort+black or ruff+black combinations? What baseline config "
            "is recommended for CLI/script repos used by AI coding agents? Prefer official "
            "docs.astral.sh/ruff documentation."
        ),
        include_domains=("docs.astral.sh", "github.com"),
    ),
    QuerySpec(
        id="type-checking-ty",
        title="Type checking: ty vs alternatives",
        query=(
            "For new Python projects in 2026, should Astral ty be the default static type "
            "checker versus mypy or Pyright/BasedPyright? Maturity, speed, IDE/LSP fit, "
            "CI usage, and risks of adopting ty as Core. Prefer official ty/mypy/pyright "
            "docs and recent maintainer statements."
        ),
        include_domains=(
            "docs.astral.sh",
            "mypy.readthedocs.io",
            "microsoft.github.io",
            "github.com",
        ),
    ),
    QuerySpec(
        id="pytest-testing",
        title="pytest and test layout",
        query=(
            "Should pytest be Required Core for personal Python CLI and script projects in "
            "2026? Which plugins and settings are worth Default vs Optional (pytest-cov, "
            "pytest-xdist, etc.)? Recommended test directory layout with uv. Prefer "
            "docs.pytest.org and packaging guidance."
        ),
        include_domains=("docs.pytest.org", "docs.astral.sh", "packaging.python.org"),
    ),
    QuerySpec(
        id="hooks-hk",
        title="Git hooks with hk",
        query=(
            "Evaluate jdx hk (https://github.com/jdx/hk) as the default git hooks / local "
            "quality gate tool for Python projects in 2026 versus pre-commit. Installation, "
            "config model, CI parity, maturity, and whether it should be Core for a personal "
            "foundry that also uses uv, ruff, and pytest. Prefer official hk docs and "
            "pre-commit docs for comparison."
        ),
        include_domains=("github.com", "hk.jdx.dev", "pre-commit.com", "docs.astral.sh"),
    ),
    QuerySpec(
        id="secrets-fnox",
        title="Secrets with fnox",
        query=(
            "Evaluate fnox (https://fnox.jdx.dev/) for secrets management in personal Python "
            "CLI/script projects in 2026. Should it be Required Core, Optional profile, or "
            "out of Core? Compare lightly to dotenv, direnv, and 1Password/CLI patterns. "
            "How should templates avoid committing secrets? Prefer official fnox docs."
        ),
        include_domains=("fnox.jdx.dev", "github.com", "direnv.net"),
    ),
    QuerySpec(
        id="httpx-http",
        title="HTTP client: httpx",
        query=(
            "For Python CLI and script projects that need HTTP in 2026, should httpx be the "
            "default client versus requests or urllib? Sync vs async defaults for CLI tools, "
            "and whether httpx belongs in every project Core or only an optional http profile. "
            "Prefer official httpx and requests documentation."
        ),
        include_domains=("www.python-httpx.org", "requests.readthedocs.io", "docs.python.org"),
    ),
    QuerySpec(
        id="cli-framework",
        title="CLI framework default",
        query=(
            "For new Python CLI applications in 2026, what should the default CLI framework "
            "be among Typer, Click, argparse, and cyclopts/rich-click? Consider typing, "
            "agent-friendliness, dependency weight, and official docs. Prefer library docs."
        ),
        include_domains=(
            "typer.tiangolo.com",
            "click.palletsprojects.com",
            "docs.python.org",
            "github.com",
        ),
    ),
    QuerySpec(
        id="data-etl-profile",
        title="Data/ETL profile (DuckDB, pandas, peers)",
        query=(
            "For a Python foundry supporting data/ETL pipelines without notebooks in 2026, "
            "what libraries should be in an optional data-etl profile versus never in Core? "
            "Consider DuckDB, pandas, polars, and pyarrow. Prefer official project docs and "
            "current maintenance status."
        ),
        include_domains=(
            "duckdb.org",
            "pandas.pydata.org",
            "pola.rs",
            "arrow.apache.org",
            "github.com",
        ),
    ),
    QuerySpec(
        id="github-actions-ci",
        title="GitHub Actions CI with uv",
        query=(
            "What is the recommended GitHub Actions workflow shape in 2026 for a Python "
            "project using uv, ruff, type checking, and pytest on Linux (and optionally "
            "macOS)? Include setup-uv or official Astral actions, caching, Python matrix, "
            "and permissions hygiene. Prefer docs.astral.sh/uv and GitHub Actions docs."
        ),
        include_domains=(
            "docs.astral.sh",
            "docs.github.com",
            "github.com",
        ),
    ),
    QuerySpec(
        id="command-surface",
        title="Developer/agent command surface",
        query=(
            "For uv-based Python projects in 2026, what minimal command set should docs "
            "promise so humans and AI coding agents can lint, typecheck, test, and run "
            "hooks consistently? Prefer uv run patterns, just/make optional wrappers, and "
            "official Astral guidance."
        ),
        include_domains=("docs.astral.sh", "just.systems", "github.com"),
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
            "User-Agent": "python-foundry-exa-ecosystem-evidence/0.1",
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
        f"# Exa ecosystem evidence run",
        "",
        f"- **Started (UTC):** {meta['started_utc']}",
        f"- **Finished (UTC):** {meta['finished_utc']}",
        f"- **Search type:** `{meta['search_type']}`",
        f"- **Queries:** {meta['query_count']}",
        f"- **Total cost (USD):** {meta.get('total_cost')}",
        f"- **Total elapsed (s):** {meta.get('total_elapsed')}",
        "",
        "This is **raw evidence**, not an accepted research report.",
        "Assemble into `docs/reports/01-modern-python-ecosystem.md` with Charter rules.",
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
            lines.append(f"- **Core/profile:** {content.get('suggested_core_or_profile', '—')}")
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
            for u in urls[:6]:
                lines.append(f"- [{u.get('title') or u.get('url')}]({u.get('url')})")
            lines.append("")

        grounding = rec.get("grounding") or []
        if grounding:
            lines.append("**Grounding (sample):**")
            for g in grounding[:6]:
                conf = g.get("confidence", "?")
                field = g.get("field", "?")
                cites = g.get("citations") or []
                cite_s = "; ".join(
                    f"[{c.get('title') or 'src'}]({c.get('url')})" for c in cites[:3] if c.get("url")
                )
                lines.append(f"- `{field}` [{conf}]: {cite_s}")
            lines.append("")

    (run_dir / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Exa Deep evidence for ecosystem research")
    parser.add_argument(
        "--type",
        default="deep-reasoning",
        choices=["deep-lite", "deep", "deep-reasoning"],
        help="Default: deep-reasoning for load-bearing decisions",
    )
    parser.add_argument(
        "--only",
        default="",
        help="Comma-separated query ids (default: all)",
    )
    parser.add_argument("--list", action="store_true", help="List query ids and exit")
    parser.add_argument("--timeout", type=float, default=120.0)
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Output directory (default: scripts/exa-output/ecosystem-<timestamp>)",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=0.5,
        help="Seconds between requests",
    )
    args = parser.parse_args()

    if args.list:
        for q in QUERIES:
            print(f"{q.id:24} {q.title}")
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
    run_dir = args.out_dir or (ROOT / "scripts" / "exa-output" / f"ecosystem-{stamp}")
    run_dir.mkdir(parents=True, exist_ok=True)

    started = datetime.now(timezone.utc)
    records: list[dict[str, Any]] = []
    failures: list[str] = []
    total_cost = 0.0
    total_elapsed = 0.0

    print(f"Run directory: {run_dir}", file=sys.stderr)
    print(f"type={args.type} queries={len(selected)}", file=sys.stderr)

    for i, spec in enumerate(selected, 1):
        print(f"[{i}/{len(selected)}] {spec.id} …", file=sys.stderr, flush=True)
        try:
            rec = run_one(api_key, spec, search_type=args.type, timeout_s=args.timeout)
            path = run_dir / f"{spec.id}.json"
            path.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            records.append(rec)
            c = rec.get("cost_dollars")
            if isinstance(c, (int, float)):
                total_cost += float(c)
            total_elapsed += float(rec.get("elapsed_seconds") or 0)
            cls = ""
            if isinstance(rec.get("output_content"), dict):
                cls = rec["output_content"].get("classification", "")
            print(
                f"  ok {rec.get('elapsed_seconds')}s cost={rec.get('cost_dollars')} {cls}",
                file=sys.stderr,
                flush=True,
            )
        except Exception as e:
            failures.append(f"{spec.id}: {e}")
            print(f"  FAIL {e}", file=sys.stderr, flush=True)
            err_path = run_dir / f"{spec.id}.error.txt"
            err_path.write_text(str(e) + "\n", encoding="utf-8")
        if i < len(selected) and args.sleep > 0:
            time.sleep(args.sleep)

    finished = datetime.now(timezone.utc)
    meta = {
        "started_utc": started.isoformat(),
        "finished_utc": finished.isoformat(),
        "search_type": args.type,
        "query_count": len(selected),
        "success_count": len(records),
        "failure_count": len(failures),
        "failures": failures,
        "total_cost": round(total_cost, 6),
        "total_elapsed": round(total_elapsed, 2),
        "query_ids": [q.id for q in selected],
    }
    (run_dir / "run-meta.json").write_text(
        json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    write_index_md(run_dir, records, meta)

    print(file=sys.stderr)
    print(f"Done. success={len(records)} fail={len(failures)}", file=sys.stderr)
    print(f"total_cost_usd≈{total_cost:.4f} total_elapsed_s≈{total_elapsed:.1f}", file=sys.stderr)
    print(f"INDEX: {run_dir / 'INDEX.md'}", file=sys.stderr)

    return 1 if failures and not records else (1 if failures else 0)


if __name__ == "__main__":
    raise SystemExit(main())
