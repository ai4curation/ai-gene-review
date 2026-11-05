"""Summarise the PANTHER tree under a PAINT node that carries a PseudoCAP-seeded IBD.

Fetches the PANTHER (v19 API) tree for a family and reports, for the node:
its leaf count and leaf taxa, its immediate children, the path from the
family root through the node down to the target gene, every leaf with its
PANTHER definition, and which other IBD nodes of the family (from the local
PAINT table) are ancestors or descendants of the node.

Usage:
  python -I panther_node_composition.py FAMILY NODE TARGET [cached_tree.json] [paint.tsv]
TARGET is any string identifying the target leaf (UniProt accession or locus tag).
If no tree file is given the tree is downloaded from pantherdb.org.
"""

import collections
import csv
import json
import sys
import urllib.request


def load_tree(family: str, path: str | None) -> dict:
    """Return the root annotation_node of the PANTHER tree."""
    if path:
        with open(path) as fh:
            data = json.load(fh)
    else:
        url = f"https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family={family}"
        with urllib.request.urlopen(url, timeout=300) as resp:
            data = json.load(resp)
    return data["search"]["tree_topology"]["annotation_node"]


def kids(node: dict) -> list[dict]:
    c = node.get("children", {}).get("annotation_node", [])
    return c if isinstance(c, list) else [c]


def leaves(node: dict) -> list[dict]:
    k = kids(node)
    return [node] if not k else [x for c in k for x in leaves(c)]


def path_to(node: dict, pred, acc=None):
    """Path of nodes from node to the first node satisfying pred."""
    acc = (acc or []) + [node]
    if pred(node):
        return acc
    for c in kids(node):
        p = path_to(c, pred, acc)
        if p:
            return p
    return None


def desc(n: dict) -> str:
    return (
        f"{n.get('persistent_id')} event={n.get('event_type')} "
        f"species={n.get('species') or n.get('organism')} leaves={len(leaves(n))} "
        f"symbol={n.get('gene_symbol', '')} sf={n.get('sf_id', '')}"
    )


def main() -> None:
    family, node_id, target = sys.argv[1:4]
    tree_file = sys.argv[4] if len(sys.argv) > 4 else None
    paint_file = sys.argv[5] if len(sys.argv) > 5 else None
    root = load_tree(family, tree_file)
    root_path = path_to(root, lambda n: n.get("persistent_id") == node_id)
    if not root_path:
        print(f"{node_id} not found in {family} tree")
        return
    node = root_path[-1]
    print(f"# {node_id} in {family}")
    print(f"family root: {root.get('persistent_id')} total leaves: {len(leaves(root))}")
    print(f"is_family_root: {node is root}")
    print(f"node: {desc(node)}")
    lv = leaves(node)
    orgs = collections.Counter(x.get("organism", "?") for x in lv)
    print(f"leaves: {len(lv)}; distinct organisms: {len(orgs)}")
    print("\n## Path from family root to node")
    for n in root_path:
        print(f"- {desc(n)}")
    print("\n## Immediate children of node")
    for c in kids(node):
        print(f"- {desc(c)}")
    print("\n## Path from node to target")
    p = path_to(node, lambda n: not kids(n) and target in json.dumps(n))
    for n in p or []:
        print(f"- {desc(n)}")
    print("\n## Leaves under node (organism | symbol | gene_id | definition)")
    for x in lv:
        print(f"- {x.get('organism')} | {x.get('gene_symbol', '')} | {x.get('gene_id', '')} | {x.get('definition', '')}")
    if paint_file:
        anc_ids = {n.get("persistent_id") for n in root_path[:-1]}
        def ids(n):
            out = {n.get("persistent_id")}
            for c in kids(n):
                out |= ids(c)
            return out
        below = ids(node) - {node_id}
        print("\n## Other IBDs of the family relative to node")
        with open(paint_file) as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                rel = (
                    "SELF" if row["node"] == node_id else
                    "ANCESTOR" if row["node"] in anc_ids else
                    "DESCENDANT" if row["node"] in below else None
                )
                if rel:
                    nseeds = len(row["seeds"].split("|"))
                    print(f"- {rel} {row['node']} {row['go_id']} {row['aspect']} negated={row['negated']} n_seeds={nseeds}")


if __name__ == "__main__":
    main()
