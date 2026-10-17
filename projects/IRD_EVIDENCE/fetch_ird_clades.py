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
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
CACHE = ROOT / ".cache" / "panther_trees"
NODES = HERE / "ird_nodes.tsv"
OUT = HERE / "ird_clade_members.tsv.gz"
TREE_URL = "https://pantherdb.org/services/oai/pantherdb/treeinfo"


def _children(node: dict) -> list[dict]:
    ch = node.get("children", {}).get("annotation_node", [])
    return [ch] if isinstance(ch, dict) else ch


def compact_tree(tree: dict) -> dict:
    """Reduce a treeinfo response to ``{"leaves": {ptn: info}, "under": {ptn: [leaf ptns]}}``.

    ``under`` lists, for every internal node, the leaf PTNs below it. A leaf's
    ``uniprot`` is parsed from ``node_name`` (``ORG|DB=id|UniProtKB=ACC``).
    """
    leaves: dict[str, dict] = {}
    under: dict[str, list[str]] = {}

    def walk(n: dict) -> list[str]:
        pid = n.get("persistent_id", "")
        kids = _children(n)
        if not kids:
            name = n.get("node_name", "")
            acc = ""
            for tok in name.split("|"):
                if tok.startswith("UniProtKB="):
                    acc = tok.split("=", 1)[1]
            leaves[pid] = {
                "uniprot": acc,
                "organism": n.get("organism", ""),
                "symbol": n.get("gene_symbol", ""),
                "subfamily": n.get("prop_sf_id", "") or n.get("sf_id", ""),
            }
            return [pid]
        below: list[str] = []
        for c in kids:
            below.extend(walk(c))
        under[pid] = below
        return below

    sys.setrecursionlimit(100000)
    walk(tree["search"]["tree_topology"]["annotation_node"])
    return {"leaves": leaves, "under": under}


def load_family(family: str) -> dict | None:
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"{family}.json.gz"
    if path.exists():
        with gzip.open(path, "rt") as fh:
            return json.load(fh)
    for attempt in range(4):
        try:
            r = requests.get(TREE_URL, params={"family": family}, timeout=300)
            if r.status_code == 200:
                data = compact_tree(r.json())
                with gzip.open(path, "wt") as fh:
                    json.dump(data, fh)
                return data
        except (requests.RequestException, ValueError, KeyError) as e:
            print(f"{family}: {e}", file=sys.stderr)
        time.sleep(5 * (attempt + 1))
    print(f"{family}: tree not fetched", file=sys.stderr)
    return None


def main() -> int:
    with NODES.open() as fh:
        ird = list(csv.DictReader(fh, delimiter="\t"))
    families = sorted({r["family"] for r in ird if r["family"]})
    with ThreadPoolExecutor(max_workers=6) as pool:
        trees = dict(zip(families, pool.map(load_family, families)))
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
