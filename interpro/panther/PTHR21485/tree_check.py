"""Map this family's PAINT node assertions onto the PANTHER tree leaves.

Run from the repository root, e.g.:

    uv run python interpro/panther/PTHR21485/tree_check.py

The family is the name of the folder holding this script. The tree is loaded with
``ai_gene_review.etl.panther_trees.load_family`` (the cached compact tree under
``.cache/panther_trees/`` or, if absent, the PANTHER treeinfo service). PAINT rows are
read from ``<FAMILY>-paint.tsv`` and the reviewed family members from
``<FAMILY>-entries.csv``. For every PAINT row the script lists the leaves under the
node with their UniProt accession, organism, gene symbol and subfamily, then reports
which reviewed (Swiss-Prot) family members are, or are not, leaves of the tree.
Nothing about the result is hard-coded. Output: ``<FAMILY>-tree-check.txt``.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from ai_gene_review.etl.panther_trees import leaves_below, load_family

HERE = Path(__file__).resolve().parent
FAMILY = HERE.name


def main() -> None:
    """Write the tree check report for FAMILY."""
    tree = load_family(FAMILY)
    if tree is None:
        raise SystemExit(f"no PANTHER tree available for {FAMILY}")
    leaves = tree["leaves"]
    out: list[str] = [f"tree {FAMILY} leaves {len(leaves)} internal nodes {len(tree['under'])}"]
    paint = HERE / f"{FAMILY}-paint.tsv"
    if paint.exists():
        with paint.open() as fh:
            for row in csv.reader(fh, delimiter="\t"):
                if len(row) < 6 or not row[1].startswith("PTN"):
                    continue
                node, term, aspect, evidence, negated = row[1], row[2], row[3], row[4], row[5]
                below = leaves_below(tree, node)
                sf = Counter(leaves[x]["subfamily"] for x in below)
                sf_txt = ", ".join(f"{k}={v}" for k, v in sorted(sf.items()))
                out.append(
                    f"{evidence} {node} {term} {aspect} negated={negated}: "
                    f"leaves {len(below)}; leaf subfamilies {sf_txt}"
                )
                for leaf in below:
                    info = leaves[leaf]
                    out.append(
                        f"  leaf of {node}: {leaf} UniProtKB:{info['uniprot']} "
                        f"{info['symbol'] or '-'} {info['organism']} {info['subfamily']}"
                    )
    tree_accs = {info["uniprot"] for info in leaves.values()}
    with (HERE / f"{FAMILY}-entries.csv").open() as fh:
        members = list(csv.DictReader(fh))
    out.append(f"reviewed members {len(members)}; tree leaves among them "
               f"{sum(m['id'] in tree_accs for m in members)}")
    for m in members:
        status = "TREE_LEAF" if m["id"] in tree_accs else "NOT_IN_TREE"
        out.append(
            f"member {m['id']} {m['gene'] or '-'} {m['subfamily'] or '-'} "
            f"length {m['length']} {status}: {m['name']}"
        )
    (HERE / f"{FAMILY}-tree-check.txt").write_text("\n".join(out) + "\n")
    print(f"wrote {FAMILY}-tree-check.txt ({len(out)} lines)")


if __name__ == "__main__":
    main()
