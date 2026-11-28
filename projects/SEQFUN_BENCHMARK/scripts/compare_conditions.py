"""Compare benchmark conditions and predictors target by target.

Reads generic Prediction files (the same inputs as ``benchmark score``) and
writes a Markdown report: a summary table (targets yes, NOT targets yes, decoys
yes per condition and predictor), targets split by whether the baseline GOA
input already entails them (any evidence code: the agent-review condition is
handed these rows and scores yes by keeping one), the same split by GO aspect,
and one row per target with each run's verdict.

    uv run python projects/SEQFUN_BENCHMARK/scripts/compare_conditions.py \\
        benchmarks/human-goa-2025-06/human-goa-2025-06.yaml \\
        -p benchmarks/human-goa-2025-06/predictions/blind-peptalk-claude-opus-5-5.jsonl ... \\
        -p benchmarks/human-goa-2025-06/predictions/agent-review-ai-gene-review-claude-opus-5-5.jsonl \\
        --baseline-dir benchmarks/human-goa-2025-06/run-inputs/baseline-goa \\
        -o projects/SEQFUN_BENCHMARK/human-goa-2025-06-comparison.md
"""

import csv
from collections import Counter
from pathlib import Path

import typer
import yaml

from ai_gene_review.benchmark.build import load_context
from ai_gene_review.benchmark.predictions import (
    queries,
    read_prediction_set,
    verdicts as prediction_verdicts,
)
from ai_gene_review.benchmark.sources import DEFAULT_CACHE

ABBREV = {"yes": "Y", "no": "n", "uncertain": "?", "missing": "-"}

app = typer.Typer()


def tally(counts: Counter, n: int) -> str:
    """'yes/n' with uncertain and missing noted.

    >>> tally(Counter({"yes": 3, "no": 1, "uncertain": 1}), 5)
    '3/5 (1 uncertain)'
    """
    extra = [f"{counts[k]} {k}" for k in ("uncertain", "missing") if counts[k]]
    return f"{counts['yes']}/{n}" + (f" ({', '.join(extra)})" if extra else "")


def baseline_terms(goa: Path) -> set[str]:
    r"""Non-negated GO terms in a baseline GOA TSV exported by ``benchmark export``.

    >>> import tempfile
    >>> p = Path(tempfile.mkdtemp()) / "x-goa.tsv"
    >>> rows = ["QUALIFIER\tGO TERM", "enables\tGO:1", "NOT|enables\tGO:2"]
    >>> _ = p.write_text("\n".join(rows) + "\n")
    >>> sorted(baseline_terms(p))
    ['GO:1']
    """
    with goa.open(newline="") as fh:
        return {
            row["GO TERM"]
            for row in csv.DictReader(fh, delimiter="\t")
            if not row["QUALIFIER"].startswith("NOT")
        }


@app.command()
def main(
    benchmark_file: Path,
    predictions: list[Path] = typer.Option(
        ..., "--predictions", "-p", help="Prediction files (.jsonl or .yaml)."
    ),
    baseline_dir: Path = typer.Option(..., help="run-inputs/baseline-goa folder."),
    output: Path = typer.Option(..., "--output", "-o"),
) -> None:
    benchmark = yaml.safe_load(benchmark_file.read_text())
    ctx, _ = load_context(benchmark["spec"], DEFAULT_CACHE)
    verdicts: dict[tuple[str, str, str, str], str] = {}
    for path in predictions:
        verdicts.update(
            prediction_verdicts(benchmark, read_prediction_set(path)["predictions"])
        )
    runs = sorted({(c, p) for c, p, _, _ in verdicts})
    names = [f"{c} {p}" for c, p in runs]

    rows = []
    for item in benchmark["items"]:
        aspects = {t["term"]["id"]: t["aspect"] for t in item["target_annotations"]}
        acc = item["protein"].split(":", 1)[1]
        given = baseline_terms(baseline_dir / f"{acc}-goa.tsv")
        for term, label, role in queries(item):
            rows.append(
                {
                    "gene": item["gene_symbol"],
                    "term": term,
                    "label": label,
                    "role": role,
                    "aspect": aspects.get(term, ""),
                    "in_baseline": any(
                        term in ctx.ontology.ancestors(ctx.ontology.resolve(g))
                        for g in given
                    ),
                    "verdicts": [
                        verdicts.get((c, p, item["id"], term), "missing")
                        for c, p in runs
                    ],
                }
            )

    lines = [f"# Condition comparison: {benchmark['id']}", ""]
    lines += [
        "| condition and predictor | targets yes | NOT targets yes | decoys yes |",
        "|---|---|---|---|",
    ]
    for i, name in enumerate(names):
        cells = []
        for role in ("TARGET", "NEGATED_TARGET", "DECOY"):
            sel = [r["verdicts"][i] for r in rows if r["role"] == role]
            counts = Counter(sel)
            if role == "DECOY" and counts["missing"] == len(sel):
                cells.append("not asked")
            else:
                cells.append(tally(counts, len(sel)))
        lines.append(f"| {name} | " + " | ".join(cells) + " |")

    targets = [r for r in rows if r["role"] == "TARGET"]
    n_in = sum(r["in_baseline"] for r in targets)
    lines += [
        "",
        "## Targets yes, split by whether the baseline input already entails them",
        "",
        f"{n_in} of {len(targets)} targets are entailed by a term (any evidence code) in "
        "the baseline GOA file that the agent-review condition was given. A review "
        "scores yes on these by keeping a row it was handed; the blind and organism "
        "conditions never see that file.",
        "",
        f"| condition and predictor | in baseline input (n={n_in}) | not in baseline input "
        f"(n={len(targets) - n_in}) |",
        "|---|---|---|",
    ]
    for i, name in enumerate(names):
        cells = [
            tally(
                Counter(r["verdicts"][i] for r in targets if r["in_baseline"] == flag),
                sum(r["in_baseline"] == flag for r in targets),
            )
            for flag in (True, False)
        ]
        lines.append(f"| {name} | " + " | ".join(cells) + " |")

    lines += ["", "## Targets yes, by GO aspect", ""]
    aspects = sorted({r["aspect"] for r in rows if r["role"] == "TARGET"})
    lines += [
        "| condition and predictor | " + " | ".join(aspects) + " |",
        "|---" * (len(aspects) + 1) + "|",
    ]
    for i, name in enumerate(names):
        cells = []
        for aspect in aspects:
            sel = [
                r["verdicts"][i]
                for r in rows
                if r["role"] == "TARGET" and r["aspect"] == aspect
            ]
            cells.append(tally(Counter(sel), len(sel)))
        lines.append(f"| {name} | " + " | ".join(cells) + " |")

    lines += [
        "",
        "## Per target",
        "",
        "Y yes, n no, ? uncertain, - missing. Columns: "
        + "; ".join(f"{j + 1} = {name}" for j, name in enumerate(names))
        + ".",
        "",
        "| gene | term | role | aspect | in baseline input | "
        + " | ".join(str(j + 1) for j in range(len(names)))
        + " |",
        "|---" * (5 + len(names)) + "|",
    ]
    for r in rows:
        if r["role"] == "DECOY":
            continue
        lines.append(
            f"| {r['gene']} | {r['term']} {r['label']} | {r['role']} | {r['aspect']} | "
            + ("yes" if r["in_baseline"] else "")
            + " | "
            + " | ".join(ABBREV[v] for v in r["verdicts"])
            + " |"
        )
    output.write_text("\n".join(lines) + "\n")
    typer.echo("\n".join(lines[:24]))


if __name__ == "__main__":
    app()
