#!/usr/bin/env python3
"""Compare GO-GPT predictions with GOA and current AIGR review layers."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
GENERIC_TERMS = {
    "GO:0003674",
    "GO:0008150",
    "GO:0005575",
    "GO:0005488",
    "GO:0009987",
    "GO:0008152",
    "GO:0044237",
    "GO:0071704",
    "GO:0044238",
    "GO:0006807",
    "GO:0044260",
    "GO:0043170",
    "GO:0097159",
    "GO:1901363",
}
RETAINED_ACTIONS = {"", "ACCEPT", "KEEP_AS_NON_CORE", "UNDECIDED", "PENDING"}
CORE_SINGLE_TERM_SLOTS = (
    "molecular_function",
    "contributes_to_molecular_function",
    "in_complex",
)
CORE_MULTI_TERM_SLOTS = ("directly_involved_in", "locations")


def go_id(term: Any) -> str:
    """Return a GO identifier from a term mapping, or an empty string."""
    if not isinstance(term, dict):
        return ""
    identifier = str(term.get("id") or "")
    return identifier if identifier.startswith("GO:") else ""


def ids(terms: Iterable[Any]) -> set[str]:
    """Return all GO identifiers from term mappings."""
    return {identifier for term in terms if (identifier := go_id(term))}


def get_goa_terms(goa_file: Path) -> set[str]:
    """Level 1: exact terms from the committed GOA snapshot."""
    if not goa_file.exists():
        return set()
    with goa_file.open(newline="", encoding="utf-8") as handle:
        return {
            identifier
            for row in csv.DictReader(handle, delimiter="\t")
            if (identifier := str(row.get("GO TERM") or "")).startswith("GO:")
        }


def get_core_terms_from_document(review: dict[str, Any]) -> set[str]:
    """Return every GO-valued slot authored in ``core_functions``."""
    terms: set[str] = set()
    for core_function in review.get("core_functions", []) or []:
        for slot in CORE_SINGLE_TERM_SLOTS:
            if identifier := go_id(core_function.get(slot)):
                terms.add(identifier)
        for slot in CORE_MULTI_TERM_SLOTS:
            terms.update(ids(core_function.get(slot, []) or []))
    return terms


def get_core_terms(review_file: Path) -> set[str]:
    """Level 3: all GO-valued terms in current AIGR core functions."""
    review = yaml.safe_load(review_file.read_text(encoding="utf-8")) or {}
    return get_core_terms_from_document(review)


def get_post_review_terms(review_file: Path) -> set[str]:
    """Level 2: retained/replacement annotations plus AIGR core-function terms."""
    review = yaml.safe_load(review_file.read_text(encoding="utf-8")) or {}
    terms: set[str] = set()

    for annotation in review.get("existing_annotations", []) or []:
        if annotation.get("negated") is True:
            continue
        annotation_review = annotation.get("review") or {}
        action = str(annotation_review.get("action") or "")
        if action == "MODIFY":
            terms.update(ids(annotation_review.get("proposed_replacement_terms", []) or []))
        elif action in RETAINED_ACTIONS:
            if identifier := go_id(annotation.get("term")):
                terms.add(identifier)

    terms.update(get_core_terms_from_document(review))
    return terms


def prediction_sets(batch_file: Path) -> dict[tuple[str, str], set[str]]:
    """Recover emitted predictions independent of the batch file's old reference columns."""
    records = json.loads(batch_file.read_text(encoding="utf-8"))
    predictions: dict[tuple[str, str], set[str]] = defaultdict(set)
    for record in records:
        key = (record["organism"], record["gene"])
        predictions[key].update(record.get("pred_only", []))
        predictions[key].update(record.get("overlap_terms", []))
    return predictions


def build_comparison(repo_root: Path) -> tuple[list[dict[str, Any]], dict[str, dict[str, int]]]:
    """Build deterministic per-gene records and aggregate counters."""
    batch_file = repo_root / "reports" / "gogpt-comparison.json"
    if not batch_file.exists():
        raise FileNotFoundError(f"Missing GO-GPT batch results: {batch_file}")

    stats = {
        level: {"overlap": 0, "total": 0, "pred": 0}
        for level in ("goa", "post_review", "core")
    }
    details: list[dict[str, Any]] = []

    for (organism, gene), predictions in sorted(prediction_sets(batch_file).items()):
        specific_predictions = predictions - GENERIC_TERMS
        if not specific_predictions:
            continue
        gene_dir = repo_root / "genes" / organism / gene
        review_file = gene_dir / f"{gene}-ai-review.yaml"
        if not review_file.exists():
            continue

        reference_sets = {
            "goa": get_goa_terms(gene_dir / f"{gene}-goa.tsv"),
            "post_review": get_post_review_terms(review_file),
            "core": get_core_terms(review_file),
        }
        overlaps = {
            level: specific_predictions & reference
            for level, reference in reference_sets.items()
        }
        for level, reference in reference_sets.items():
            stats[level]["overlap"] += len(overlaps[level])
            stats[level]["total"] += len(reference)
            stats[level]["pred"] += len(specific_predictions)

        details.append(
            {
                "organism": organism,
                "gene": gene,
                "preds": len(specific_predictions),
                "goa_terms": len(reference_sets["goa"]),
                "goa_overlap": len(overlaps["goa"]),
                "post_review_terms": len(reference_sets["post_review"]),
                "post_review_overlap": len(overlaps["post_review"]),
                "core_terms": len(reference_sets["core"]),
                "core_overlap": len(overlaps["core"]),
                "goa_overlap_terms": sorted(overlaps["goa"]),
                "post_review_overlap_terms": sorted(overlaps["post_review"]),
                "core_overlap_terms": sorted(overlaps["core"]),
            }
        )

    return details, stats


def write_figure(path: Path, stats: dict[str, dict[str, int]]) -> None:
    """Render the three-level overlap figure from the computed aggregates."""
    import matplotlib.pyplot as plt

    predicted = stats["goa"]["pred"]
    values = [
        predicted,
        stats["goa"]["overlap"],
        stats["post_review"]["overlap"],
        stats["core"]["overlap"],
    ]
    labels = [
        "GO-GPT predictions\nemitted",
        "Match raw GOA",
        "Match retained/replacement\nAIGR annotations",
        "Match agent-adjudicated\nAIGR core functions",
    ]
    colors = ["#d9e7f4", "#9ac7df", "#4f9dca", "#0b5fa5"]

    fig, axis = plt.subplots(figsize=(14, 8))
    bars = axis.barh(labels, values, color=colors)
    axis.invert_yaxis()
    axis.set_xlabel("Number of GO-GPT predictions (300 genes)", fontsize=17)
    axis.set_title(
        "GO-GPT prediction overlap narrows at each adjudication level",
        fontsize=20,
    )
    axis.tick_params(axis="both", labelsize=15)
    axis.set_xlim(0, max(values) * 1.24)
    for bar, value in zip(bars, values):
        percent = 100 * value / predicted if predicted else 0
        axis.text(
            value + max(values) * 0.012,
            bar.get_y() + bar.get_height() / 2,
            f"{value:,} ({percent:.1f}%)",
            va="center",
            fontsize=15,
        )
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=160)
    plt.close(fig)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument(
        "--output",
        type=Path,
        help="Per-gene JSON output (default: reports/gogpt-comparison-levels.json)",
    )
    parser.add_argument(
        "--figure",
        type=Path,
        help="Figure output (default: BIOREASON article figures directory)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    output = args.output or repo_root / "reports" / "gogpt-comparison-levels.json"
    figure = args.figure or (
        repo_root
        / "projects"
        / "BIOREASON_COMPARISON"
        / "article"
        / "figures"
        / "three_level_overlap.png"
    )
    details, stats = build_comparison(repo_root)

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(details, indent=2) + "\n", encoding="utf-8")
    write_figure(figure, stats)

    print(f"Genes analyzed: {len(details)}")
    print(f"{'Level':<24} {'Overlap':>8} {'Reference':>10} {'Recall':>8} {'Precision':>10}")
    labels = {
        "goa": "vs GOA",
        "post_review": "vs post-review AIGR",
        "core": "vs AIGR core functions",
    }
    for level in ("goa", "post_review", "core"):
        level_stats = stats[level]
        recall = 100 * level_stats["overlap"] / max(level_stats["total"], 1)
        precision = 100 * level_stats["overlap"] / max(level_stats["pred"], 1)
        print(
            f"{labels[level]:<24} {level_stats['overlap']:>8} "
            f"{level_stats['total']:>10} {recall:>7.1f}% {precision:>9.1f}%"
        )
    print(f"Wrote {output}")
    print(f"Wrote {figure}")


if __name__ == "__main__":
    main()
