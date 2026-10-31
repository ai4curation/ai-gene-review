"""Resolve the leaf proteins under every IRD node, from the PANTHER family trees.

An IRD row says only "function lost/diverged at node X". To ask whether the genes
below X really lack the function, we need X's descendants. ``IBD.gaf`` has no
tree, so this script fetches each family's tree from the PANTHER API
(``treeinfo``), caches a compact copy under ``.cache/panther_trees/`` (git-ignored),
and lists the leaves under each IRD node.

Input:   ird_nodes.tsv (from fetch_paint_ird.py)
Output:  ird_clade_members.tsv.gz  one row per (IRD node, GO term, leaf protein)

Usage:
    uv run python projects/IRD_EVIDENCE/fetch_ird_clades.py
"""

from __future__ import annotations

import csv
import gzip
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from ai_gene_review.etl.panther_trees import load_family

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
NODES = HERE / "ird_nodes.tsv"
OUT = HERE / "ird_clade_members.tsv.gz"


def main() -> int:
    with NODES.open() as fh:
        ird = list(csv.DictReader(fh, delimiter="\t"))
    families = sorted({r["family"] for r in ird if r["family"]})
    with ThreadPoolExecutor(max_workers=6) as pool:
        trees = dict(zip(families, pool.map(lambda f: load_family(f, ROOT / ".cache" / "panther_trees"), families)))
    missing = [f for f, t in trees.items() if t is None]
    n_rows = 0
    with gzip.open(OUT, "wt", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["family", "ird_node", "go_id", "leaf_node", "uniprot", "organism", "symbol", "subfamily"])
        for r in ird:
            t = trees.get(r["family"])
            if t is None:
                continue
            node = r["ird_node"]
            leaf_ids = [node] if node in t["leaves"] else t["under"].get(node, [])
            for lid in leaf_ids:
                info = t["leaves"][lid]
                w.writerow([r["family"], node, r["go_id"], lid, info["uniprot"], info["organism"], info["symbol"], info["subfamily"]])
                n_rows += 1
    print(f"{len(families)} families, {len(missing)} without a tree: {missing[:20]}", file=sys.stderr)
    print(f"wrote {n_rows} clade-member rows to {OUT}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
