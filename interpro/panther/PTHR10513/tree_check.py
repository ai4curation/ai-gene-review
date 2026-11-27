"""Map PTHR10513 PAINT assertions and proposed targets onto the PANTHER tree.

Run from the repository root:

    python interpro/panther/PTHR10513/tree_check.py

The compact PANTHER 19.0 tree is loaded through
``ai_gene_review.etl.panther_trees.load_family``. PAINT rows are read from
``PTHR10513-paint.tsv``, proposed target nodes from ``PTHR10513-review.yaml``,
and reviewed family members from ``PTHR10513-entries.csv``. The report is
written to ``PTHR10513-tree-check.txt``.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import yaml

from ai_gene_review.etl.panther_trees import leaves_below, load_family

HERE = Path(__file__).resolve().parent
FAMILY = HERE.name


def _sf_summary(tree: dict, nodes: list[str]) -> str:
    """Return a stable subfamily=count summary for ``nodes``."""
    counts = Counter(tree["leaves"][node]["subfamily"] for node in nodes)
    return ", ".join(f"{sf}={count}" for sf, count in sorted(counts.items()))


def _append_node(out: list[str], tree: dict, prefix: str, node: str) -> None:
    """Append a node summary and all human leaves below that node."""
    below = leaves_below(tree, node)
    out.append(
        f"{prefix} {node}: leaves {len(below)}; leaf subfamilies {_sf_summary(tree, below)}"
    )
    for leaf in below:
        info = tree["leaves"][leaf]
        if info["organism"] == "Homo sapiens":
            out.append(
                f"  human leaf of {node}: {leaf} UniProtKB:{info['uniprot']} "
                f"{info['symbol']} {info['subfamily']}"
            )


def main() -> None:
    tree = load_family(FAMILY)
    if tree is None:
        raise SystemExit(f"no PANTHER tree available for {FAMILY}")

    out = [
        f"tree {FAMILY} leaves {len(tree['leaves'])} internal nodes {len(tree['under'])}"
    ]

    with (HERE / f"{FAMILY}-paint.tsv").open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            node = row["node"]
            _append_node(
                out,
                tree,
                f"{row['evidence']} {node} {row['go_id']} {row['aspect']} "
                f"negated={row['negated']}",
                node,
            )

    review = yaml.safe_load((HERE / f"{FAMILY}-review.yaml").read_text())
    for assessment in review.get("node_assessments", []):
        proposal = assessment.get("proposed_action") or {}
        target = (proposal.get("target_node_id") or "").removeprefix("PANTHER:")
        if not target:
            continue
        source = assessment["node_id"].removeprefix("PANTHER:")
        term = assessment["asserted_term"]["id"]
        action = proposal["paint_action"]
        _append_node(
            out,
            tree,
            f"proposal {action} target for {source} {term}",
            target,
        )

    tree_accs = {info["uniprot"] for info in tree["leaves"].values()}
    with (HERE / f"{FAMILY}-entries.csv").open() as fh:
        members = list(csv.DictReader(fh))
    out.append(
        f"reviewed members {len(members)}; tree leaves among them "
        f"{sum(member['id'] in tree_accs for member in members)}"
    )
    for member in members:
        status = "TREE_LEAF" if member["id"] in tree_accs else "NOT_IN_TREE"
        out.append(
            f"member {member['id']} {member['gene'] or '-'} "
            f"{member['subfamily'] or '-'} length {member['length']} "
            f"{status}: {member['name']}"
        )

    (HERE / f"{FAMILY}-tree-check.txt").write_text("\n".join(out) + "\n")
    print(f"wrote {FAMILY}-tree-check.txt ({len(out)} lines)")


if __name__ == "__main__":
    main()
