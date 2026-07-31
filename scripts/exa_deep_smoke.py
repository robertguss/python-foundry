#!/usr/bin/env python3
"""Smoke-test Exa Deep Search API (not the Grok Exa MCP).

Requires:
  export EXA_API_KEY=...

Usage:
  python3 scripts/exa_deep_smoke.py
  python3 scripts/exa_deep_smoke.py --type deep-reasoning
  python3 scripts/exa_deep_smoke.py --query "..." --out /tmp/exa-deep-smoke.json

Docs: https://exa.ai/docs/reference/search-api-guide
      https://exa.ai/blog/exa-deep
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

API_URL = "https://api.exa.ai/search"

# Keep schema within Exa limits: max nesting depth 2, max ~10 properties.
DEFAULT_OUTPUT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "required": ["recommendation", "python_floor", "rationale", "alternatives"],
    "properties": {
        "recommendation": {
            "type": "string",
            "description": "One-sentence recommendation for default package manager.",
        },
        "python_floor": {
            "type": "string",
            "description": "Suggested minimum Python version for new projects, e.g. 3.12.",
        },
        "rationale": {
            "type": "string",
            "description": "Short rationale grounded in official docs where possible.",
        },
        "alternatives": {
            "type": "array",
            "description": "Other package managers considered.",
            "items": {"type": "string"},
        },
        "caveats": {
            "type": "string",
            "description": "Limitations, maturity risks, or when not to use the recommendation.",
        },
    },
}

DEFAULT_QUERY = (
    "For new personal Python CLI and script projects on macOS and Linux in 2026, "
    "should uv be the default project and package manager instead of poetry or pip+venv? "
    "Prefer official documentation (Astral uv, Python packaging guides). "
    "State a recommended minimum Python version for new projects."
)

DEFAULT_SYSTEM_PROMPT = (
    "Prefer primary/official documentation over blogs. "
    "Be concrete about versions and defaults. "
    "If evidence is weak, say so. "
    "Do not recommend Windows-specific tooling."
)


def build_payload(
    *,
    query: str,
    search_type: str,
    system_prompt: str,
    num_results: int,
) -> dict[str, Any]:
    return {
        "query": query,
        "type": search_type,
        "numResults": num_results,
        "systemPrompt": system_prompt,
        "outputSchema": DEFAULT_OUTPUT_SCHEMA,
        # Highlights help us see raw sources without dumping full pages.
        "contents": {"highlights": True},
    }


def post_search(api_key: str, payload: dict[str, Any], timeout_s: float) -> dict[str, Any]:
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        API_URL,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
            "User-Agent": "python-foundry-exa-deep-smoke/0.1",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout_s) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw)
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"HTTP {e.code}: {err_body}") from e
    except urllib.error.URLError as e:
        raise SystemExit(f"Request failed: {e}") from e


def summarize(data: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("=== Exa Deep smoke test — summary ===")
    lines.append(f"requestId:   {data.get('requestId', '—')}")
    lines.append(f"searchType:  {data.get('searchType', data.get('resolvedSearchType', '—'))}")
    cost = data.get("costDollars") or {}
    if cost:
        lines.append(f"costDollars: {cost.get('total', cost)}")

    output = data.get("output") or {}
    content = output.get("content")
    lines.append("")
    lines.append("--- output.content ---")
    if content is None:
        lines.append("(missing — Deep may have failed to synthesize)")
    elif isinstance(content, (dict, list)):
        lines.append(json.dumps(content, indent=2, ensure_ascii=False))
    else:
        lines.append(str(content))

    grounding = output.get("grounding") or []
    lines.append("")
    lines.append(f"--- output.grounding ({len(grounding)} fields) ---")
    for g in grounding[:20]:
        field = g.get("field", "?")
        conf = g.get("confidence", "?")
        cites = g.get("citations") or []
        lines.append(f"  [{conf}] {field}")
        for c in cites[:5]:
            title = c.get("title") or ""
            url = c.get("url") or ""
            lines.append(f"      - {title} {url}".rstrip())

    results = data.get("results") or []
    lines.append("")
    lines.append(f"--- results ({len(results)}) ---")
    for i, r in enumerate(results[:8], 1):
        lines.append(f"  {i}. {r.get('title', '')}")
        lines.append(f"     {r.get('url', '')}")
        hl = r.get("highlights") or []
        if hl:
            snippet = hl[0].replace("\n", " ")
            if len(snippet) > 160:
                snippet = snippet[:157] + "..."
            lines.append(f"     highlight: {snippet}")

    lines.append("")
    lines.append("=== end summary ===")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke-test Exa Deep Search API")
    parser.add_argument(
        "--type",
        default="deep",
        choices=["deep-lite", "deep", "deep-reasoning"],
        help="Exa search type (default: deep)",
    )
    parser.add_argument("--query", default=DEFAULT_QUERY, help="Search query")
    parser.add_argument(
        "--system-prompt",
        default=DEFAULT_SYSTEM_PROMPT,
        help="systemPrompt for planning/synthesis",
    )
    parser.add_argument("--num-results", type=int, default=6)
    parser.add_argument(
        "--timeout",
        type=float,
        default=120.0,
        help="HTTP timeout seconds (deep can take 4-50s+)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Write full JSON response to this path",
    )
    args = parser.parse_args()

    api_key = os.environ.get("EXA_API_KEY", "").strip()
    if not api_key:
        print("EXA_API_KEY is not set. export EXA_API_KEY=... and retry.", file=sys.stderr)
        return 2

    payload = build_payload(
        query=args.query,
        search_type=args.type,
        system_prompt=args.system_prompt,
        num_results=args.num_results,
    )

    print(f"POST {API_URL}", file=sys.stderr)
    print(f"type={args.type!r} numResults={args.num_results} timeout={args.timeout}s", file=sys.stderr)
    print(f"query={args.query[:120]}{'…' if len(args.query) > 120 else ''}", file=sys.stderr)
    print("waiting…", file=sys.stderr)

    t0 = time.perf_counter()
    data = post_search(api_key, payload, timeout_s=args.timeout)
    elapsed = time.perf_counter() - t0
    print(f"done in {elapsed:.1f}s", file=sys.stderr)

    out_path = args.out
    if out_path is None:
        out_path = Path(__file__).resolve().parent / "exa-deep-smoke-last.json"
    out_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"full JSON → {out_path}", file=sys.stderr)

    print(summarize(data))

    # Exit non-zero if smoke looks broken (no output / no results).
    if not data.get("output") and not data.get("results"):
        print("FAIL: empty response (no output and no results)", file=sys.stderr)
        return 1
    if data.get("output") is None:
        print("WARN: no synthesized output (results may still be useful)", file=sys.stderr)
        return 0
    print("PASS: received response with output and/or results", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
