"""Locate Q18287 (C28G1.2) in the PANTHER PTHR11461 (serpin) tree.

Fetches the PANTHER tree for PTHR11461 from the PANTHER web service, finds the
leaf for Q18287, and reports:

* the chain of ancestral nodes (PTN persistent id, subfamily, event type,
  species label) from the leaf to the root;
* for the first few ancestors, the leaves in that clade (so the nearest
  relatives by tree topology, not by BLAST score, can be read off);
* whether each PAINT node in the local PTHR11461-paint.tsv is an ancestor of
  the Q18287 leaf.

Run: python3 panther_tree_placement.py > panther_tree_placement.txt
(stdlib only).
"""

import csv
import json
import urllib.request
from pathlib import Path

TREE_URL = "https://pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR11461"
TARGET = "UniProtKB=Q18287"
PAINT = (
    Path(__file__).resolve().parents[4]
    / "interpro/panther/PTHR11461/PTHR11461-paint.tsv"
)


def children(node):
    c = node.get("children")
    if not c:
        return []
    kids = c["annotation_node"]
    return kids if isinstance(kids, list) else [kids]


def find_path(node, path):
    path = path + [node]
    if TARGET in node.get("gene_id", "") or TARGET in node.get("node_name", ""):
        return path
    for k in children(node):
        p = find_path(k, path)
        if p:
            return p
    return None


def leaves(node):
    ks = children(node)
    if not ks:
        return [node]
    out = []
    for k in ks:
        out.extend(leaves(k))
    return out


def label(n):
    return n.get("gene_id") or n.get("node_name") or ""


def newick(n):
    ks = children(n)
    if not ks:
        return label(n).split(":")[-1]
    inner = ",".join(newick(k) for k in ks)
    return "(%s)%s[%s;bl=%s]" % (
        inner,
        n.get("persistent_id"),
        n.get("event_type"),
        n.get("branch_length"),
    )


def main():
    req = urllib.request.Request(TREE_URL, headers={"User-Agent": "curl/8"})
    with urllib.request.urlopen(req, timeout=180) as r:
        data = json.load(r)
    root = data["search"]["tree_topology"]["annotation_node"]
    path = find_path(root, [])
    if path is None:
        print("Q18287 not found in PTHR11461 tree")
        return
    leaf = path[-1]
    print("Target leaf:", label(leaf))
    print("Leaf subfamily:", leaf.get("sf_id"), leaf.get("sf_name"))
    print()
    print("Ancestors (nearest first):")
    ancestors = list(reversed(path[:-1]))
    for a in ancestors:
        print(
            " ",
            a.get("persistent_id"),
            a.get("sf_id"),
            a.get("sf_name"),
            a.get("event_type"),
            a.get("species"),
            "n_leaves=%d" % len(leaves(a)),
        )
    print()
    for depth, a in enumerate(ancestors[:4], start=1):
        ls = leaves(a)
        print(
            "Clade at ancestor %d (%s, %s), %d leaves:"
            % (depth, a.get("persistent_id"), a.get("species"), len(ls))
        )
        for lf in ls[:60]:
            print("   ", label(lf), lf.get("sf_id"), lf.get("definition", ""))
        print()
    print("Topology of the C. elegans duplication clade (ancestor 2):")
    print(newick(ancestors[1]))
    print()
    anc_ids = {a.get("persistent_id") for a in ancestors}
    print("PAINT nodes (local PTHR11461-paint.tsv) vs Q18287 ancestry:")
    with open(PAINT) as f:
        for row in csv.DictReader(f, delimiter="\t"):
            print(
                " ",
                row["node"],
                row["go_id"],
                row["evidence"],
                "NOT" if row["negated"] == "true" else "",
                "ANCESTOR" if row["node"] in anc_ids else "not ancestor",
            )


if __name__ == "__main__":
    main()
