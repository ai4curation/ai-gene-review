"""Summarise the PANTHER tree under the PAINT node that carries the pqsH-seeded IBD.

Fetches the PANTHER (v19 API) tree for PTHR45934 and reports, for the node
PTN008173107 (GO:0004497 IBD seeded only by PqsH), its leaf count, the taxa of
its leaves, the path from the node to PqsH (Q9I0Q0 / PA2587), and the event
types (speciation, horizontal transfer) on the way.

Usage: python -I panther_node_composition.py [cached_tree.json]
If no file is given the tree is downloaded from pantherdb.org.
"""

import collections
import json
import sys
import urllib.request

FAMILY = "PTHR45934"
NODE = "PTN008173107"
URL = f"https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family={FAMILY}"


def load_tree(path: str | None) -> dict:
    """Return the root annotation_node of the PANTHER tree."""
    if path:
        with open(path) as fh:
            data = json.load(fh)
    else:
        with urllib.request.urlopen(URL, timeout=180) as resp:
            data = json.load(resp)
    return data["search"]["tree_topology"]["annotation_node"]


def kids(node: dict) -> list[dict]:
    """Children of a tree node as a list."""
    c = node.get("children", {}).get("annotation_node", [])
    return c if isinstance(c, list) else [c]


def leaves(node: dict) -> list[dict]:
    """All leaf nodes below (or equal to) node."""
    k = kids(node)
    return [node] if not k else [x for c in k for x in leaves(c)]


def find(node: dict, pid: str) -> dict | None:
    """Find a node by persistent id."""
    if node.get("persistent_id") == pid:
        return node
    for c in kids(node):
        hit = find(c, pid)
        if hit:
            return hit
    return None


def path_to(node: dict, pred, acc=None):
    """Path of nodes from node to the first leaf satisfying pred."""
    acc = (acc or []) + [node]
    if not kids(node) and pred(node):
        return acc
    for c in kids(node):
        p = path_to(c, pred, acc)
        if p:
            return p
    return None


def main() -> None:
    root = load_tree(sys.argv[1] if len(sys.argv) > 1 else None)
    node = find(root, NODE)
    if node is None:
        print(f"{NODE} not found in {FAMILY} tree")
        return
    print(f"# {NODE} in {FAMILY}")
    print(f"is_family_root: {node is root}")
    print(f"node species label: {node.get('species')}, event: {node.get('event_type')}")
    lv = leaves(node)
    print(f"leaves: {len(lv)}")
    genera = collections.Counter(x.get("organism", "?").split()[0] for x in lv)
    print(f"distinct genera: {len(genera)}")
    print("leaf genera:", ", ".join(f"{g}={n}" for g, n in genera.most_common()))
    print("\n## Immediate children")
    for c in kids(node):
        print(
            f"- {c.get('persistent_id')} event={c.get('event_type')} "
            f"species={c.get('species') or c.get('organism')} leaves={len(leaves(c))}"
        )
    print("\n## Path to PqsH")
    p = path_to(node, lambda n: "PA2587" in json.dumps(n) or "Q9I0Q0" in json.dumps(n))
    for n in p or []:
        print(
            f"- {n.get('persistent_id')} event={n.get('event_type')} "
            f"species={n.get('species') or n.get('organism')} leaves={len(leaves(n))} "
            f"symbol={n.get('gene_symbol', '')}"
        )
    print("\n## Children of the horizontal-transfer node and root-level leaves")
    hgt = [n for n in (p or []) if n.get("event_type") == "HORIZ_TRANSFER"]
    if hgt:
        for c in kids(hgt[0]):
            print(
                f"- HGT child {c.get('persistent_id')} species={c.get('species') or c.get('organism')} "
                f"leaves={len(leaves(c))} symbol={c.get('gene_symbol', '')}"
            )
    for c in kids(node):
        if not kids(c):
            print(f"- root-level leaf {c.get('organism')} {c.get('gene_symbol')} {c.get('definition')}")
    ath = [x for x in lv if x.get("organism", "").startswith("Arabidopsis")]
    print("\n## Arabidopsis leaves")
    for x in ath:
        print(f"- {x.get('gene_symbol')} {x.get('gene_id')} {x.get('definition')}")


if __name__ == "__main__":
    main()
