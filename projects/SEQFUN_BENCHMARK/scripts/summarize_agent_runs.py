"""Summarize AGENT_REVIEW sandbox runs: model, effort, cost and a leakage audit.

Reads each ``SANDBOX_ROOT/<GENE>/transcript.jsonl`` (headless Claude Code
stream-json) and writes one YAML record per gene: model, cost, turns, the
review's action counts, and every tool call (any tool, any argument) that
names the network, a path outside the sandbox, or the repository checkout
(``$AIGR_REPO``, which ``run_agent_review.sh`` exports so that
``tools/residues.sh`` can run the repository's residue checker).

It also writes the scoring input: per gene, the sha256 of the final review and
the terms ``review_claims`` reads from it (kept and contested), so that the
agent-review score can be recomputed and checked without the git-ignored
reviews.

    uv run python projects/SEQFUN_BENCHMARK/scripts/summarize_agent_runs.py \\
        SANDBOX_ROOT --effort high -o projects/SEQFUN_BENCHMARK/agent-review-runs.yaml \\
        --claims-output projects/SEQFUN_BENCHMARK/agent-review-claims.yaml
"""

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

import typer
import yaml

from ai_gene_review.benchmark.importers.reviews import review_claims

NETWORK = re.compile(
    r"curl|wget|https?://|requests\.|urllib|rest\.uniprot|ebi\.ac\.uk|ncbi"
)
OUTSIDE = re.compile(
    r"(?<![\w.])(/Users/|~/|/private/(?!tmp/claude)|\.\./\.\./\.\./\.\.)"
    r"|AIGR_REPO|repos/ai-gene-review|orca/workspaces"
)

app = typer.Typer()


def flagged_commands(commands: list[str], pattern: re.Pattern) -> list[str]:
    """Tool inputs matching ``pattern``, truncated.

    >>> flagged_commands(["ls", "curl https://x"], NETWORK)
    ['curl https://x']
    >>> flagged_commands(['{"command": "cat $AIGR_REPO/genes/x"}'], OUTSIDE)
    ['{"command": "cat $AIGR_REPO/genes/x"}']
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
            commands.append(json.dumps(inp))
            for key in ("file_path", "path"):
                if key in inp:
                    paths.append(inp[key])
    return commands, paths, result


@app.command()
def main(
    sandbox_root: Path,
    effort: str = typer.Option(..., help="Effort level the runs used."),
    output: Path = typer.Option(..., "--output", "-o"),
    claims_output: Path = typer.Option(...),
) -> None:
    records = []
    claims = []
    for transcript in sorted(sandbox_root.glob("*/transcript.jsonl")):
        box = transcript.parent
        gene = box.name
        commands, paths, result = tool_inputs(transcript)
        review_file = box / "genes" / "human" / gene / f"{gene}-ai-review.yaml"
        review = yaml.safe_load(review_file.read_text())
        kept, contested = review_claims(review)
        claims.append(
            {
                "gene": gene,
                "review_sha256": hashlib.sha256(review_file.read_bytes()).hexdigest(),
                "kept": sorted(kept),
                "contested": sorted(contested),
            }
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
                "network_tool_calls": flagged_commands(commands, NETWORK),
                "outside_sandbox_tool_calls": flagged_commands(commands, OUTSIDE),
                "outside_sandbox_paths": outside_paths,
            }
        )
    total = round(sum(r["cost_usd"] for r in records), 2)
    output.write_text(
        yaml.safe_dump(
            {"total_cost_usd": total, "runs": records}, sort_keys=False, width=100
        )
    )
    claims_output.write_text(yaml.safe_dump({"reviews": claims}, sort_keys=False))
    typer.echo(f"{len(records)} runs, total ${total}")


if __name__ == "__main__":
    app()
