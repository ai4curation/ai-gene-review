"""Summarise where the cached PAINT nodes sit in the PANTHER 19 family trees.

For each family, download the PANTHER treeinfo JSON (not retained), then for
every PTN node in the committed ``<FAM>-paint.tsv`` report whether the node is
in that family's tree, its tree_node_type, taxonomic range, event type, leaf
count, and the subfamilies and named example leaves beneath it.  Also report,
for chosen target accessions, the chain of annotated ancestors.

Usage:
    python paint_node_placement.py PTHR11070 PTHR30591 PTHR43788 \
        --targets P08394 Q88DZ5 P07648 Q88DZ4 P04993 Q88DZ6
Writes nothing; prints markdown to stdout.
"""

from __future__ import annotations

import argparse
import collections
import csv
import json
import sys
import urllib.request
from pathlib import Path

TREEINFO = "https://pantherdb.org/services/oai/pantherdb/treeinfo?family={fam}"
REPO = Path(__file__).resolve().parents[3]


def children(node):
    c = node.get("children")
    if not c:
        return []
    an = c["annotation_node"]
    return an if isinstance(an, list) else [an]


def walk(node, parent_chain, index, leaves_under):
    pid = node.get("persistent_id")
    chain = parent_chain + [node]
    if pid:
        index[pid] = (node, parent_chain)
    kids = children(node)
    if not kids:
        acc = None
        name = node.get("node_name", "")
        if "UniProtKB=" in name:
            acc = name.split("UniProtKB=")[-1]
        leaf = {
            "acc": acc,
            "sf": node.get("prop_sf_id") or node.get("sf_id"),
            "sym": node.get("gene_symbol"),
            "org": node.get("organism"),
            "chain": [n.get("persistent_id") for n in chain],
        }
        for n in chain:
            if n.get("persistent_id"):
                leaves_under[n["persistent_id"]].append(leaf)
        return [leaf]
    out = []
    for k in kids:
        out.extend(walk(k, chain, index, leaves_under))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("families", nargs="+")
    ap.add_argument("--targets", nargs="*", default=[])
    ap.add_argument("--show-sf", nargs="*", default=[],
                    help="list the leaves of these subfamilies (e.g. PTHR11070:SF49)")
    args = ap.parse_args(argv)
    for fam in args.families:
        req = urllib.request.Request(
            TREEINFO.format(fam=fam), headers={"User-Agent": "ai-gene-review-analysis/1.0"}
        )
        with urllib.request.urlopen(req, timeout=300) as r:
            data = json.load(r)
        root = data["search"]["tree_topology"]["annotation_node"]
        index, leaves_under = {}, collections.defaultdict(list)
        leaves = walk(root, [], index, leaves_under)
        print(f"## {fam}\n")
        print(f"- root node: {root.get('persistent_id')} "
              f"(taxonomic_range {root.get('taxonomic_range')}); leaves: {len(leaves)}\n")
        paint = REPO / "interpro" / "panther" / fam / f"{fam}-paint.tsv"
        rows = list(csv.DictReader(open(paint), delimiter="\t"))
        seen = []
        for row in rows:
            if row["node"] not in seen:
                seen.append(row["node"])
        print("| node | in tree | type | event | taxonomic range | leaves | subfamilies (leaf count) | terms |")
        print("|---|---|---|---|---|---|---|---|")
        for ptn in seen:
            terms = ",".join(r["go_id"] for r in rows if r["node"] == ptn)
            if ptn not in index:
                print(f"| {ptn} | no | | | | | | {terms} |")
                continue
            node, _ = index[ptn]
            lv = leaves_under[ptn]
            sfc = collections.Counter(tree_leaf["sf"] for tree_leaf in lv)
            sfs = "; ".join(f"{k} ({v})" for k, v in sfc.most_common())
            print(f"| {ptn} | yes | {node.get('tree_node_type','INTERNAL')} | "
                  f"{node.get('event_type','')} | {node.get('taxonomic_range','')} | "
                  f"{len(lv)} | {sfs} | {terms} |")
        print()
        for t in args.targets:
            hit = [tree_leaf for tree_leaf in leaves if tree_leaf["acc"] == t]
            if not hit:
                continue
            tree_leaf = hit[0]
            annotated = [p for p in tree_leaf["chain"] if p in seen]
            print(f"- target {t} ({tree_leaf['sym']}, {tree_leaf['org']}, {tree_leaf['sf']}): annotated ancestors "
                  f"{', '.join(annotated) if annotated else 'none'}")
        print()
        for sf in args.show_sf:
            if not sf.startswith(fam + ":"):
                continue
            print(f"- leaves of {sf}: " + "; ".join(
                f"{tree_leaf['acc']} {tree_leaf['sym']} ({tree_leaf['org']})" for tree_leaf in leaves if tree_leaf["sf"] == sf))
        print()


if __name__ == "__main__":
    sys.exit(main())
