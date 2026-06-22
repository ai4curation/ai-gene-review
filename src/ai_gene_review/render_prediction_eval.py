"""Render prediction review YAMLs into an HTML evaluation table.

Collects ``*-predictions-review.yaml`` files matching a glob pattern,
aggregates assessment counts, and renders a single interactive HTML table
with filtering, sorting, and a stacked assessment distribution bar.

Usage::

    # Render all ProtNLM prediction reviews
    python -m ai_gene_review.render_prediction_eval \\
        'genes/*/*-protnlm-predictions-review.yaml' \\
        -o pages/protnlm-eval.html \\
        --title 'ARGO-ProtNLM-50 Prediction Evaluation'

    # Render DeepECTF reviews from a specific project
    python -m ai_gene_review.render_prediction_eval \\
        'projects/BIOREASON_COMPARISON/**/genes/*/*-det-predictions-review.yaml' \\
        -o pages/deepectf-eval.html

    # Default: all *-predictions-review.yaml under genes/
    python -m ai_gene_review.render_prediction_eval
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader

CS_MAP = {"COR": 2, "CNN": 2, "LSP": 2, "UNC": 1, "PLI": 0, "NPI": 0, "REP": 0}
ASSESSMENT_ORDER = ["COR", "CNN", "LSP", "UNC", "PLI", "NPI", "REP"]


def load_prediction_review(path: Path) -> dict[str, Any]:
    """Load a single prediction review YAML.

    >>> from pathlib import Path
    >>> import tempfile, os
    >>> content = 'id: TEST\\ngene_symbol: TST\\ntaxon:\\n  id: NCBITaxon:1\\n  label: test\\npredictions: []\\n'
    >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
    ...     _ = f.write(content)
    ...     p = Path(f.name)
    >>> d = load_prediction_review(p)
    >>> d['id'], d['predictions']
    ('TEST', [])
    >>> os.unlink(p)
    """
    with open(path) as f:
        data = yaml.safe_load(f) or {}
    data.setdefault("predictions", [])
    data["_source_path"] = str(path)
    return data


def find_review_link(yaml_path: Path) -> str | None:
    """Derive relative link to the gene's HTML review page, if it exists."""
    gene_dir = yaml_path.parent
    gene_symbol = gene_dir.name
    html_path = gene_dir / f"{gene_symbol}-ai-review.html"
    if html_path.exists():
        return str(html_path)
    return None


def collect_predictions(
    pattern: str, root: Path | None = None,
) -> list[dict[str, Any]]:
    """Collect prediction review data from YAML files matching *pattern*.

    >>> collect_predictions('nonexistent-pattern-*.yaml')
    []
    """
    root = root or Path(".")
    paths = sorted(root.glob(pattern))
    results = []
    for p in paths:
        data = load_prediction_review(p)
        data["review_link"] = find_review_link(p)
        results.append(data)
    return results


def compute_stats(proteins: list[dict[str, Any]]) -> dict[str, Any]:
    """Compute aggregate statistics across all predictions.

    >>> stats = compute_stats([{'predictions': [
    ...     {'review': {'assessment': 'COR', 'confidence_score': 2}},
    ...     {'review': {'assessment': 'NPI', 'confidence_score': 0}},
    ... ]}])
    >>> stats['total_predictions'], stats['counts']['COR'], stats['counts']['NPI']
    (2, 1, 1)
    >>> stats['mean_cs']
    1.0
    """
    counts: dict[str, int] = {code: 0 for code in ASSESSMENT_ORDER}
    total = 0
    cs_sum = 0.0
    term_types: set[str] = set()

    for protein in proteins:
        for pred in protein.get("predictions", []):
            review = pred.get("review", {})
            assessment = review.get("assessment", "UNC")
            counts[assessment] = counts.get(assessment, 0) + 1
            cs_sum += CS_MAP.get(assessment, 0)
            total += 1
            tt = pred.get("predicted_term_type", "")
            if tt:
                term_types.add(tt)

    return {
        "total_predictions": total,
        "counts": counts,
        "mean_cs": cs_sum / total if total else 0.0,
        "term_types": sorted(term_types),
    }


def render_prediction_eval(
    proteins: list[dict[str, Any]],
    title: str = "Prediction Evaluation",
    subtitle: str = "",
    template_path: Path | None = None,
) -> str:
    """Render the evaluation HTML from collected protein data.

    Returns the HTML string.
    """
    if template_path is None:
        template_path = Path(__file__).parent / "templates" / "prediction_eval.html.j2"

    stats = compute_stats(proteins)

    env = Environment(
        loader=FileSystemLoader(str(template_path.parent)),
        autoescape=True,
    )
    template = env.get_template(template_path.name)
    return template.render(
        title=title,
        subtitle=subtitle,
        proteins=proteins,
        **stats,
    )


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Render prediction review YAMLs as an HTML evaluation table",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "pattern",
        nargs="?",
        default="genes/*/*-predictions-review.yaml",
        help="Glob pattern for prediction review YAMLs (default: genes/*/*-predictions-review.yaml)",
    )
    parser.add_argument(
        "-o", "--output",
        default=None,
        help="Output HTML path (default: stdout)",
    )
    parser.add_argument(
        "--title",
        default="Prediction Evaluation",
        help="Page title",
    )
    parser.add_argument(
        "--subtitle",
        default="",
        help="Subtitle text",
    )
    parser.add_argument(
        "--template",
        default=None,
        help="Custom Jinja2 template path",
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Root directory for glob resolution (default: .)",
    )
    args = parser.parse_args()

    proteins = collect_predictions(args.pattern, root=Path(args.root))
    if not proteins:
        print(f"No files found matching '{args.pattern}' under {args.root}", file=sys.stderr)
        sys.exit(1)

    template_path = Path(args.template) if args.template else None
    html = render_prediction_eval(
        proteins,
        title=args.title,
        subtitle=args.subtitle,
        template_path=template_path,
    )

    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html)
        print(f"Wrote {out} ({len(proteins)} proteins, "
              f"{compute_stats(proteins)['total_predictions']} predictions)")
    else:
        sys.stdout.write(html)


if __name__ == "__main__":
    main()
