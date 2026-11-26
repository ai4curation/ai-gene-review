"""Compare benchmark conditions target by target (peptalk runs and agent-review).

Writes a Markdown report: a summary table (targets yes, NOT targets yes, decoys
yes per condition), targets split by whether the baseline GOA input already
entails them (any evidence code: the agent-review condition is handed these
rows and scores yes by keeping one), the same split by GO aspect, and one row
per target with each condition's verdict.

    uv run python projects/SEQFUN_BENCHMARK/scripts/compare_conditions.py \\
        benchmarks/human-goa-2025-06/human-goa-2025-06.yaml \\
        --peptalk benchmarks/human-goa-2025-06/runs/blind-claude-opus-5-5.jsonl ... \\
        --reviews-dir benchmarks/human-goa-2025-06/runs/agent-review/genes \\
        --baseline-dir benchmarks/human-goa-2025-06/run-inputs/baseline-goa \\
        -o projects/SEQFUN_BENCHMARK/human-goa-2025-06-comparison.md
"""

from collections import Counter
from pathlib import Path

import typer
import yaml

from ai_gene_review.benchmark.build import load_context
from ai_gene_review.benchmark.run import (
    peptalk_verdicts,
    queries,
    read_jsonl,
    review_verdicts,
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
    >>> rows = ["h", "\t".join(["U", "A", "S", "enables", "GO:1"]),
    ...         "\t".join(["U", "A", "S", "NOT|enables", "GO:2"])]
    >>> _ = p.write_text("\n".join(rows) + "\n")
    >>> sorted(baseline_terms(p))
    ['GO:1']
    """
    terms = set()
    for line in goa.read_text().splitlines()[1:]:
        cols = line.split("\t")
        if not cols[3].startswith("NOT"):
            terms.add(cols[4])
    return terms


@app.command()
def main(
    benchmark_file: Path,
    peptalk: list[Path] = typer.Option(...),
    reviews_dir: Path = typer.Option(...),
    baseline_dir: Path = typer.Option(..., help="run-inputs/baseline-goa folder."),
    review_label: str = typer.Option("agent-review"),
    output: Path = typer.Option(..., "--output", "-o"),
) -> None:
    benchmark = yaml.safe_load(benchmark_file.read_text())
    ctx, _ = load_context(benchmark["spec"], DEFAULT_CACHE)
    verdicts = peptalk_verdicts(benchmark, read_jsonl(peptalk))
    verdicts.update(review_verdicts(benchmark, ctx, reviews_dir, review_label))
    runs = sorted({(c, m) for c, m, _, _ in verdicts})
    names = [f"{c} {m}".strip() for c, m in runs]

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
                        verdicts.get((c, m, item["id"], term), "missing")
                        for c, m in runs
                    ],
                }
            )

    lines = [f"# Condition comparison: {benchmark['id']}", ""]
    lines += [
        "| condition | targets yes | NOT targets yes | decoys yes |",
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
        "scores yes on these by keeping a row it was handed; the peptalk conditions "
        "never see that file.",
        "",
        f"| condition | in baseline input (n={n_in}) | not in baseline input "
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
        "| condition | " + " | ".join(aspects) + " |",
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
