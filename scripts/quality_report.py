#!/usr/bin/env python3
"""Generate per-organism quality dashboards for gene reviews.

Scans all gene review YAML files and produces a summary report with:
- Annotation counts and action distribution
- Deep research and core function coverage
- Review completeness metrics

Usage:
    python scripts/quality_report.py                    # all organisms
    python scripts/quality_report.py --organism human   # single organism
    python scripts/quality_report.py --tsv reports/quality.tsv  # TSV output
"""

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml


def load_review(path: Path) -> dict | None:
    """Load a gene review YAML file, returning None on failure."""
    with open(path) as f:
        return yaml.safe_load(f)


def analyze_gene(gene_dir: Path, review: dict) -> dict:
    """Analyze a single gene's review quality."""
    gene = gene_dir.name
    annotations = review.get("existing_annotations") or []
    actions: Counter[str] = Counter()
    for ann in annotations:
        r = ann.get("review") or {}
        action = r.get("action", "PENDING")
        actions[action] += 1

    core_functions = review.get("core_functions") or []
    has_deep_research = any(gene_dir.glob("*-deep-research-*.md"))
    has_description = bool(review.get("description"))
    references = review.get("references") or []
    status = review.get("status", "unknown")

    reviewed_count = sum(
        1 for ann in annotations
        if (ann.get("review") or {}).get("action", "PENDING") != "PENDING"
    )

    return {
        "gene": gene,
        "status": status,
        "total_annotations": len(annotations),
        "reviewed_annotations": reviewed_count,
        "actions": dict(actions),
        "has_core_functions": len(core_functions) > 0,
        "core_function_count": len(core_functions),
        "has_deep_research": has_deep_research,
        "has_description": has_description,
        "reference_count": len(references),
    }


def print_organism_report(organism: str, gene_stats: list[dict]) -> None:
    """Print a formatted report for one organism."""
    n = len(gene_stats)
    if n == 0:
        return

    total_ann = sum(g["total_annotations"] for g in gene_stats)
    reviewed_ann = sum(g["reviewed_annotations"] for g in gene_stats)
    all_actions: Counter[str] = Counter()
    for g in gene_stats:
        all_actions.update(g["actions"])

    with_core = sum(1 for g in gene_stats if g["has_core_functions"])
    with_research = sum(1 for g in gene_stats if g["has_deep_research"])
    with_desc = sum(1 for g in gene_stats if g["has_description"])
    fully_reviewed = sum(
        1 for g in gene_stats
        if g["reviewed_annotations"] == g["total_annotations"] and g["total_annotations"] > 0
    )

    print(f"\n{'='*60}")
    print(f" {organism}  ({n} genes)")
    print(f"{'='*60}")
    print(f"  Annotations:      {total_ann} total, {reviewed_ann} reviewed ({_pct(reviewed_ann, total_ann)})")
    print(f"  Fully reviewed:   {fully_reviewed}/{n} genes ({_pct(fully_reviewed, n)})")
    print(f"  Core functions:   {with_core}/{n} genes ({_pct(with_core, n)})")
    print(f"  Deep research:    {with_research}/{n} genes ({_pct(with_research, n)})")
    print(f"  Has description:  {with_desc}/{n} genes ({_pct(with_desc, n)})")

    if all_actions:
        print("\n  Action distribution:")
        for action in sorted(all_actions, key=lambda a: -all_actions[a]):
            count = all_actions[action]
            print(f"    {action:<25s} {count:>5d}  ({_pct(count, total_ann)})")

    # Flag genes needing attention
    incomplete = [
        g for g in gene_stats
        if g["reviewed_annotations"] < g["total_annotations"]
    ]
    if incomplete:
        print(f"\n  Genes with unreviewed annotations ({len(incomplete)}):")
        for g in sorted(incomplete, key=lambda x: x["reviewed_annotations"] / max(x["total_annotations"], 1)):
            pending = g["total_annotations"] - g["reviewed_annotations"]
            print(f"    {g['gene']:<20s} {pending} pending of {g['total_annotations']}")


def _pct(num: int, denom: int) -> str:
    if denom == 0:
        return "N/A"
    return f"{100 * num / denom:.0f}%"


def write_tsv(all_stats: dict[str, list[dict]], output_path: Path) -> None:
    """Write detailed per-gene TSV report."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    header = [
        "organism", "gene", "status", "total_annotations", "reviewed_annotations",
        "pct_reviewed", "has_core_functions", "core_function_count",
        "has_deep_research", "has_description", "reference_count",
        "ACCEPT", "MODIFY", "REMOVE", "KEEP_AS_NON_CORE",
        "MARK_AS_OVER_ANNOTATED", "UNDECIDED", "NEW", "PENDING",
    ]
    with open(output_path, "w") as f:
        f.write("\t".join(header) + "\n")
        for organism in sorted(all_stats):
            for g in sorted(all_stats[organism], key=lambda x: x["gene"]):
                pct = (
                    f"{100 * g['reviewed_annotations'] / g['total_annotations']:.0f}"
                    if g["total_annotations"] > 0 else "N/A"
                )
                row = [
                    organism, g["gene"], g["status"],
                    str(g["total_annotations"]), str(g["reviewed_annotations"]),
                    pct,
                    str(g["has_core_functions"]), str(g["core_function_count"]),
                    str(g["has_deep_research"]), str(g["has_description"]),
                    str(g["reference_count"]),
                ]
                for action in ["ACCEPT", "MODIFY", "REMOVE", "KEEP_AS_NON_CORE",
                               "MARK_AS_OVER_ANNOTATED", "UNDECIDED", "NEW", "PENDING"]:
                    row.append(str(g["actions"].get(action, 0)))
                f.write("\t".join(row) + "\n")
    print(f"\nTSV report written to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate per-organism quality dashboards")
    parser.add_argument("--organism", help="Restrict to a single organism")
    parser.add_argument("--tsv", metavar="PATH", help="Write detailed TSV report to PATH")
    args = parser.parse_args()

    genes_root = Path("genes")
    if not genes_root.is_dir():
        print("Error: genes/ directory not found", file=sys.stderr)
        return 1

    all_stats: dict[str, list[dict]] = defaultdict(list)

    if args.organism:
        org_dirs = [genes_root / args.organism]
    else:
        org_dirs = sorted(p for p in genes_root.iterdir() if p.is_dir())

    for org_dir in org_dirs:
        if not org_dir.is_dir():
            continue
        organism = org_dir.name

        for gene_dir in sorted(org_dir.iterdir()):
            if not gene_dir.is_dir():
                continue
            review_path = gene_dir / f"{gene_dir.name}-ai-review.yaml"
            if not review_path.exists():
                continue

            review = load_review(review_path)
            if review is None:
                continue

            stats = analyze_gene(gene_dir, review)
            all_stats[organism].append(stats)

    if not all_stats:
        print("No gene reviews found", file=sys.stderr)
        return 1

    for organism in sorted(all_stats):
        print_organism_report(organism, all_stats[organism])

    # Grand total
    total_genes = sum(len(v) for v in all_stats.values())
    total_ann = sum(g["total_annotations"] for gs in all_stats.values() for g in gs)
    reviewed_ann = sum(g["reviewed_annotations"] for gs in all_stats.values() for g in gs)
    print(f"\n{'='*60}")
    print(f" GRAND TOTAL: {total_genes} genes across {len(all_stats)} organisms")
    print(f" Annotations: {total_ann} total, {reviewed_ann} reviewed ({_pct(reviewed_ann, total_ann)})")
    print(f"{'='*60}")

    if args.tsv:
        write_tsv(all_stats, Path(args.tsv))

    return 0


if __name__ == "__main__":
    sys.exit(main())
