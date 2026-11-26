"""Summarize AGENT_REVIEW sandbox runs: model, effort, cost and a leakage audit.

Reads each ``SANDBOX_ROOT/<GENE>/transcript.jsonl`` (headless Claude Code
stream-json) and writes one YAML record per gene: model, cost, turns, the
review's action counts, and every Bash command that touched the network or a
path outside the sandbox.

    uv run python projects/SEQFUN_BENCHMARK/scripts/summarize_agent_runs.py \\
        SANDBOX_ROOT --effort high -o projects/SEQFUN_BENCHMARK/agent-review-runs.yaml
"""

import json
import re
from collections import Counter
from pathlib import Path

import typer
import yaml

NETWORK = re.compile(
    r"curl|wget|https?://|requests\.|urllib|rest\.uniprot|ebi\.ac\.uk|ncbi"
)
OUTSIDE = re.compile(
    r"(?<![\w.])(/Users/|~/|/private/(?!tmp/claude)|\.\./\.\./\.\./\.\.)"
)

app = typer.Typer()


def flagged_commands(commands: list[str], pattern: re.Pattern) -> list[str]:
    """Commands matching ``pattern``, truncated.

    >>> flagged_commands(["ls", "curl https://x"], NETWORK)
    ['curl https://x']
    """
    return [c[:200] for c in commands if pattern.search(c)]


def tool_inputs(transcript: Path) -> tuple[list[str], list[str], dict]:
    commands, paths, result = [], [], {}
    for line in transcript.read_text().splitlines():
        rec = json.loads(line)
        if rec.get("type") == "result":
            result = rec
        if rec.get("type") != "assistant":
            continue
        for block in rec["message"].get("content") or []:
            if block.get("type") != "tool_use":
                continue
            inp = block.get("input") or {}
            if "command" in inp:
                commands.append(inp["command"])
            for key in ("file_path", "path"):
                if key in inp:
                    paths.append(inp[key])
    return commands, paths, result


@app.command()
def main(
    sandbox_root: Path,
    effort: str = typer.Option(..., help="Effort level the runs used."),
    output: Path = typer.Option(..., "--output", "-o"),
) -> None:
    records = []
    for transcript in sorted(sandbox_root.glob("*/transcript.jsonl")):
        box = transcript.parent
        gene = box.name
        commands, paths, result = tool_inputs(transcript)
        review = yaml.safe_load(
            (box / "genes" / "human" / gene / f"{gene}-ai-review.yaml").read_text()
        )
        actions = Counter(
            (row.get("review") or {}).get("action")
            for row in review.get("existing_annotations") or []
        )
        outside_paths = [
            p
            for p in paths
            if not str(p).startswith(str(box)) and str(p).startswith("/")
        ]
        records.append(
            {
                "gene": gene,
                "model": sorted(result.get("modelUsage", {}) or {"unknown": 0}),
                "effort": effort,
                "cost_usd": round(result.get("total_cost_usd", 0.0), 4),
                "num_turns": result.get("num_turns"),
                "outcome": result.get("subtype"),
                "actions": dict(sorted(actions.items(), key=lambda kv: str(kv[0]))),
                "core_functions": len(review.get("core_functions") or []),
                "network_commands": flagged_commands(commands, NETWORK),
                "outside_sandbox_commands": flagged_commands(commands, OUTSIDE),
                "outside_sandbox_paths": outside_paths,
            }
        )
    total = round(sum(r["cost_usd"] for r in records), 2)
    output.write_text(
        yaml.safe_dump(
            {"total_cost_usd": total, "runs": records}, sort_keys=False, width=100
        )
    )
    typer.echo(f"{len(records)} runs, total ${total}")


if __name__ == "__main__":
    app()
