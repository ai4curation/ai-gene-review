#!/usr/bin/env python3
"""Measure Affinage's *retrieval* performance against finished AIGR gene reviews.

The other scripts in this project evaluate Affinage's **GO grounding** layer
(``compare_affinage.py``) — whether the terms it emits match the curated ones.
This one asks a different and more operational question:

    When Affinage is used as the deep-research provider for a real review,
    how much of the literature that the finished review actually relies on
    did Affinage supply?

That is a **recall** question, and it is the one Affinage's own trust gates do
*not* answer. ``gates_passed: True`` certifies that the citations in the report
are real, resolvable and correctly quoted — i.e. **precision**. A report can
pass every gate and still omit the single paper that decides the review.

Method
------
For each gene with a committed ``<GENE>-deep-research-affinage.md``:

1. ``affinage`` = PMIDs appearing in that report.
2. ``review``   = PMIDs cited anywhere in ``<GENE>-ai-review.yaml``.
3. ``goa``      = PMIDs already present in ``<GENE>-goa.tsv``.

The key refinement is (3). GOA-supplied PMIDs are **handed to the reviewer** by
the annotation file — no literature search is needed to find them, so counting
them in the denominator flatters or penalises the provider arbitrarily. The
honest denominator for a retrieval provider is the set the reviewer had to go
*find*:

    novel = review - goa          # references the review added beyond GOA
    hits  = novel ∩ affinage      # ... that Affinage actually supplied

We report both the naive recall (over all review PMIDs) and the novel-reference
recall, because the gap between them is itself informative.

We also report ``unused`` = affinage - review: returned references the finished
review never cited. That is the precision-side cost, and it is expected to be
non-zero for any literature sweep.

Nothing is hard-coded. Every number derives from files committed in the repo.
Genes with no Affinage report, or with an empty report, are reported as such —
an empty return is a real and important result, not an error to be skipped.

Usage
-----
    uv run python retrieval_recall.py --all
    uv run python retrieval_recall.py --genes-file campaign-genes.txt
    uv run python retrieval_recall.py AFF4 AGFG1 ACTG2

Writes results/paint-campaign/{per-gene.json,summary.csv,summary.md}
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

import typer

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
GENES = REPO / "genes" / "human"
OUTDIR = HERE / "results" / "paint-campaign"

# PMIDs are written as "PMID:12345678" in reviews and either that or a bare
# "PMID 12345678" / "[PMID:12345678]" in provider reports.
PMID_RE = re.compile(r"PMID:?\s*(\d{6,9})")

app = typer.Typer(add_completion=False, help=__doc__)


def pmids_in(path: Path) -> set[str]:
    """Return the set of PMIDs mentioned in a file, empty if the file is absent.

    >>> import tempfile, pathlib
    >>> d = pathlib.Path(tempfile.mkdtemp())
    >>> _ = (d / "x.md").write_text("see PMID:12345678 and PMID: 987654 again PMID:12345678")
    >>> sorted(pmids_in(d / "x.md"))
    ['12345678', '987654']
    >>> pmids_in(d / "missing.md")
    set()
    """
    if not path.is_file():
        return set()
    return set(PMID_RE.findall(path.read_text(encoding="utf-8", errors="replace")))


def goa_pmids(path: Path) -> set[str]:
    """PMIDs in the GOA reference column — references the reviewer is *given*.

    The GOA TSV reference column holds values like ``PMID:9560228`` or
    ``GO_REF:0000033``; only the former count here.

    >>> import tempfile, pathlib
    >>> d = pathlib.Path(tempfile.mkdtemp())
    >>> _ = (d / "g.tsv").write_text(
    ...     "GENE PRODUCT DB\\tREFERENCE\\n"
    ...     "UniProtKB\\tPMID:111111\\n"
    ...     "UniProtKB\\tGO_REF:0000033\\n")
    >>> sorted(goa_pmids(d / "g.tsv"))
    ['111111']
    """
    return pmids_in(path)


def analyse(symbol: str) -> dict:
    """Compute retrieval stats for one gene. Missing inputs are recorded, not raised."""
    folder = GENES / symbol
    report = folder / f"{symbol}-deep-research-affinage.md"
    review = folder / f"{symbol}-ai-review.yaml"
    goa = folder / f"{symbol}-goa.tsv"

    aff = pmids_in(report)
    rev = pmids_in(review)
    goa_set = goa_pmids(goa)

    novel = rev - goa_set
    hits = novel & aff
    unused = aff - rev

    return {
        "gene": symbol,
        "has_report": report.is_file(),
        "has_review": review.is_file(),
        "gates_passed": gates_flag(report),
        # Does the review reference the report as a `file:` source at all?
        "cites_report": review.is_file()
        and "deep-research-affinage" in review.read_text(errors="replace"),
        "n_affinage": len(aff),
        "n_review": len(rev),
        "n_goa": len(goa_set),
        "n_novel": len(novel),
        "n_hits": len(hits),
        "n_review_hits": len(rev & aff),  # incl. GOA-supplied refs; naive numerator
        "n_unused": len(unused),
        # naive recall counts GOA-supplied refs in the denominator; novel_recall
        # is the honest retrieval measure. Both None when undefined.
        "naive_recall": ratio(len(rev & aff), len(rev)),
        "novel_recall": ratio(len(hits), len(novel)),
        "used_fraction": ratio(len(aff & rev), len(aff)),
    }


def gates_flag(report: Path) -> str:
    """Read the ``gates_passed`` front-matter value, or 'absent' if the field is missing.

    >>> import tempfile, pathlib
    >>> d = pathlib.Path(tempfile.mkdtemp())
    >>> _ = (d / "a.md").write_text("---\\ngates_passed: True\\n---\\n")
    >>> gates_flag(d / "a.md")
    'True'
    >>> _ = (d / "b.md").write_text("---\\ntitle: x\\n---\\n")
    >>> gates_flag(d / "b.md")
    'absent'
    """
    if not report.is_file():
        return "no_report"
    for line in report.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.strip().lower().startswith("gates_passed"):
            return line.split(":", 1)[1].strip()
    return "absent"


def ratio(num: int, den: int) -> float | None:
    """Fraction, or None when the denominator is zero (undefined, not zero).

    >>> ratio(1, 4)
    0.25
    >>> ratio(3, 0) is None
    True
    """
    return None if den == 0 else round(num / den, 4)


def discover() -> list[str]:
    """Every human gene folder carrying a committed Affinage report."""
    return sorted(
        p.parent.name
        for p in GENES.glob("*/*-deep-research-affinage.md")
        if p.name == f"{p.parent.name}-deep-research-affinage.md"
    )


def aggregate(rows: list[dict]) -> dict:
    """Pool counts across genes. Pooled ratios weight genes by reference count."""
    scored = [r for r in rows if r["has_report"] and r["has_review"]]
    tot_aff = sum(r["n_affinage"] for r in scored)
    tot_rev = sum(r["n_review"] for r in scored)
    tot_novel = sum(r["n_novel"] for r in scored)
    tot_hits = sum(r["n_hits"] for r in scored)
    tot_used = sum(r["n_affinage"] - r["n_unused"] for r in scored)
    return {
        "n_genes_scored": len(scored),
        "n_genes_total": len(rows),
        "total_affinage_pmids": tot_aff,
        "total_review_pmids": tot_rev,
        "total_goa_pmids": sum(r["n_goa"] for r in scored),
        "total_novel_pmids": tot_novel,
        "total_hits": tot_hits,
        "pooled_novel_recall": ratio(tot_hits, tot_novel),
        # Naive recall scores the provider against GOA-supplied references it was
        # never asked to retrieve; reported only to show how much it understates.
        "pooled_naive_recall": ratio(sum(r["n_review_hits"] for r in scored), tot_rev),
        "pooled_used_fraction": ratio(tot_used, tot_aff),
        "n_reviews_citing_report": sum(1 for r in scored if r["cites_report"]),
        "empty_reports": sorted(r["gene"] for r in scored if r["n_affinage"] == 0),
        "gates": _tally(r["gates_passed"] for r in scored),
        "by_curation_depth": stratify(rows),
        "zero_recall_genes": sorted(
            r["gene"] for r in scored if r["n_novel"] > 0 and r["n_hits"] == 0
        ),
    }


def _tally(values) -> dict[str, int]:
    out: dict[str, int] = {}
    for v in values:
        out[v] = out.get(v, 0) + 1
    return dict(sorted(out.items()))


def band(n_goa: int) -> str:
    """How well-curated a gene already is, proxied by its count of GOA-supplied PMIDs.

    Used to test whether retrieval recall depends on how well-studied the gene is.

    >>> band(0), band(5), band(40)
    ('dark (0-2 GOA refs)', 'medium (3-9)', 'well-studied (10+)')
    """
    if n_goa <= 2:
        return "dark (0-2 GOA refs)"
    return "medium (3-9)" if n_goa <= 9 else "well-studied (10+)"


def stratify(rows: list[dict]) -> dict[str, dict]:
    """Pooled recall within each curation-depth band.

    Pooling (not averaging per-gene ratios) matters: a gene with one novel
    reference scores 0% or 100% and would otherwise dominate the mean.
    """
    out: dict[str, dict] = {}
    for r in rows:
        if not (r["has_report"] and r["has_review"]) or r["n_novel"] == 0:
            continue
        b = band(r["n_goa"])
        acc = out.setdefault(b, {"genes": 0, "novel": 0, "hits": 0})
        acc["genes"] += 1
        acc["novel"] += r["n_novel"]
        acc["hits"] += r["n_hits"]
    for acc in out.values():
        acc["recall"] = ratio(acc["hits"], acc["novel"])
    return out


def write_outputs(rows: list[dict], summary: dict) -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    (OUTDIR / "per-gene.json").write_text(
        json.dumps({"summary": summary, "genes": rows}, indent=2) + "\n"
    )

    fields = list(rows[0].keys())
    with (OUTDIR / "summary.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    scored = [r for r in rows if r["has_report"] and r["has_review"]]
    scored.sort(key=lambda r: (r["novel_recall"] is None, r["novel_recall"] or 0))
    lines = [
        f"# Affinage retrieval recall (n={summary['n_genes_scored']} scored)",
        "",
        "Generated by `retrieval_recall.py` — do not edit by hand.",
        "",
        f"- Affinage PMIDs returned: **{summary['total_affinage_pmids']}**",
        f"- PMIDs cited by finished reviews: **{summary['total_review_pmids']}**"
        f" (of which **{summary['total_goa_pmids']}** were already supplied by GOA)",
        f"- References the reviews had to *find*: **{summary['total_novel_pmids']}**",
        f"- ... supplied by Affinage: **{summary['total_hits']}**"
        f" (**pooled novel-reference recall = {_pct(summary['pooled_novel_recall'])}**)",
        f"- Fraction of Affinage's returned refs the reviews used:"
        f" **{_pct(summary['pooled_used_fraction'])}**",
        "",
        f"Trust gates across scored genes: `{summary['gates']}`",
        "",
        f"Reports returning **zero** PMIDs ({len(summary['empty_reports'])}):"
        f" {', '.join(summary['empty_reports']) or '_none_'}",
        "",
        f"Genes where Affinage supplied **none** of the novel references"
        f" ({len(summary['zero_recall_genes'])}):"
        f" {', '.join(summary['zero_recall_genes']) or '_none_'}",
        "",
        "## Does recall depend on how well-studied the gene is?",
        "",
        "| curation depth | genes | novel refs | supplied | recall |",
        "|----------------|------:|-----------:|---------:|-------:|",
    ]
    for b, acc in sorted(summary["by_curation_depth"].items()):
        lines.append(
            f"| {b} | {acc['genes']} | {acc['novel']} | {acc['hits']} "
            f"| {_pct(acc['recall'])} |"
        )
    lines += [
        "",
        "| gene | gates | aff | review | GOA | novel | hits | novel recall | used |",
        "|------|-------|----:|-------:|----:|------:|-----:|-------------:|-----:|",
    ]
    for r in scored:
        lines.append(
            f"| {r['gene']} | {r['gates_passed']} | {r['n_affinage']} | {r['n_review']} "
            f"| {r['n_goa']} | {r['n_novel']} | {r['n_hits']} "
            f"| {_pct(r['novel_recall'])} | {_pct(r['used_fraction'])} |"
        )
    (OUTDIR / "summary.md").write_text("\n".join(lines) + "\n")


def _pct(x: float | None) -> str:
    """Percent string, or 'n/a' for an undefined ratio.

    >>> _pct(0.3412)
    '34%'
    >>> _pct(None)
    'n/a'
    """
    return "n/a" if x is None else f"{round(100 * x):d}%"


@app.command()
def main(
    genes: list[str] = typer.Argument(None, help="Gene symbols; omit with --all."),
    all_genes: bool = typer.Option(
        False, "--all", help="Score every gene with a report."
    ),
    genes_file: Path = typer.Option(None, "--genes-file", help="One symbol per line."),
) -> None:
    """Score Affinage retrieval recall and write results/paint-campaign/."""
    symbols = list(genes or [])
    if genes_file:
        symbols += [
            ln.strip() for ln in genes_file.read_text().splitlines() if ln.strip()
        ]
    if all_genes:
        symbols += discover()
    if not symbols:
        raise typer.BadParameter("give gene symbols, --genes-file, or --all")

    rows = [analyse(s) for s in sorted(set(symbols))]
    summary = aggregate(rows)
    write_outputs(rows, summary)

    typer.echo(
        f"scored {summary['n_genes_scored']}/{summary['n_genes_total']} genes | "
        f"novel-reference recall {_pct(summary['pooled_novel_recall'])} | "
        f"used {_pct(summary['pooled_used_fraction'])} | "
        f"empty reports {len(summary['empty_reports'])}"
    )
    typer.echo(f"wrote {OUTDIR}/")


if __name__ == "__main__":
    app()
