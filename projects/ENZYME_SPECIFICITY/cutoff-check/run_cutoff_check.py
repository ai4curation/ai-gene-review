"""Run the trusted-cutoff check over the electronic enzyme rows of selected reviews.

For each gene in ``genes.yaml``, every IEA/IBA molecular-function row whose GO term
cross-references a complete EC number (one reaction) is checked with
``ai_gene_review.validation.enzyme_family_cutoff``, and the verdict is set beside the
reviewer's action for that row. Nothing here is hand-entered: rows, actions and scores
are all read or computed at run time.

    uv run python projects/ENZYME_SPECIFICITY/cutoff-check/run_cutoff_check.py
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import yaml

from ai_gene_review.validation.enzyme_family_cutoff import (
    check,
    go_ec_xrefs,
    is_complete_ec,
)

HERE = Path(__file__).parent
ELECTRONIC = {"IEA", "IBA"}


def enzyme_rows(review_path: Path) -> list[dict]:
    """Electronic MF rows whose term maps to a complete EC number, de-duplicated by term."""
    review = yaml.safe_load(review_path.read_text())
    rows: dict[str, dict] = {}
    for ann in review.get("existing_annotations") or []:
        term = ann["term"]
        if ann.get("evidence_type") not in ELECTRONIC or term["id"] in rows:
            continue
        ecs = [ec for ec in go_ec_xrefs(term["id"]) if is_complete_ec(ec)]
        if not ecs:
            continue
        rows[term["id"]] = {
            "accession": review["id"],
            "gene": review["gene_symbol"],
            "go": term["id"],
            "label": term["label"],
            "ec": ecs,
            "action": ann["review"]["action"],
        }
    return list(rows.values())


def main() -> None:
    """Check every selected row and write results.yaml plus a verdict-by-action table."""
    selection = yaml.safe_load((HERE / "genes.yaml").read_text())
    results = []
    for gene in selection["genes"]:
        for row in enzyme_rows(Path(gene["review"])):
            report = check(row["accession"], [], [row["go"]], Path(".cache"))
            # Families differ in TC, so "best" is the largest margin over TC, not raw score.
            hits = [s for s in report.scores if s.is_target and s.seq_score is not None]
            best = max(hits, key=lambda s: s.seq_score - s.tc[0], default=None)
            results.append(
                {
                    **row,
                    "verdict": report.verdict,
                    "best_target_family": None
                    if best is None
                    else f"{best.accession} {best.product_name}",
                    "best_target_score": None if best is None else best.seq_score,
                    "best_target_tc": None if best is None else best.tc[0],
                    "better_fitting_families": report.better_fitting_families,
                    "ncbifam_release": report.ncbifam_release,
                }
            )
            print(f"{row['gene']:10} {row['go']} {row['action']:24} {report.verdict}")

    (HERE / "results.yaml").write_text(
        yaml.safe_dump(results, sort_keys=False, width=120)
    )
    table = Counter((r["verdict"], r["action"]) for r in results)
    actions = sorted({a for _, a in table})
    verdicts = sorted({v for v, _ in table})
    lines = [
        "| verdict | " + " | ".join(actions) + " |",
        "|---" * (len(actions) + 1) + "|",
    ]
    lines += [
        f"| {v} | " + " | ".join(str(table[(v, a)]) for a in actions) + " |"
        for v in verdicts
    ]
    (HERE / "verdict_by_action.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
