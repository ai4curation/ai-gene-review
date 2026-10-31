"""Place human SPINK5 (Q9NQ38) in the PANTHER 19 PTHR10913 tree.

Usage: uv run --with requests python panther_tree.py

Fetches the PANTHER tree (treeinfo service) and prints:
- the root-to-leaf path of Q9NQ38 (PTN node, taxonomic range, event type, subfamily),
- the leaves under the PAINT IBD node PTN000099251 (serine-type endopeptidase
  inhibitor activity), so the taxonomic scope of that propagation can be read,
- the last common ancestor of Q9NQ38 with selected comparators.
Nothing is hardcoded beyond the accessions and node id queried.
"""

import re

import requests

TARGET = "Q9NQ38"
IBD_NODE = "PTN000099251"
COMPARATORS = {
    "Q9VSK1": "CG32354 (fly)",
    "Q86NV3": "Fs (fly)",
    "Q9UIK5": "TMEFF2 (human)",
    "P19883": "FST (human)",
    "Q148R4": "Spink5 (mouse)",
}


def children(node):
    kids = node.get("children", {}).get("annotation_node", [])
    return [kids] if isinstance(kids, dict) else kids


def leaves(node):
    kids = children(node)
    if not kids:
        return [node]
    out = []
    for k in kids:
        out.extend(leaves(k))
    return out


def leaf_paths(root):
    paths = {}

    def walk(node, path):
        here = path + [node]
        kids = children(node)
        for kid in kids:
            walk(kid, here)
        if not kids:
            m = re.search(r"UniProtKB=(\w+)", node.get("node_name", ""))
            if m:
                paths[m.group(1)] = here

    walk(root, [])
    return paths


def find(node, pid):
    if node.get("persistent_id") == pid:
        return node
    for k in children(node):
        hit = find(k, pid)
        if hit:
            return hit
    return None


def main():
    tree = requests.get(
        "https://www.pantherdb.org/services/oai/pantherdb/treeinfo",
        params={"family": "PTHR10913"},
        timeout=300,
    ).json()
    root = tree["search"]["tree_topology"]["annotation_node"]
    paths = leaf_paths(root)
    if TARGET not in paths:
        print(f"{TARGET} not found in PTHR10913 tree")
        return
    target_path = paths[TARGET]
    print(f"## Root-to-leaf path of {TARGET}")
    for n in target_path:
        print(
            n.get("persistent_id"),
            n.get("taxonomic_range"),
            n.get("event_type"),
            n.get("subfamily_id", ""),
            n.get("node_name", "") if not children(n) else "",
        )
    on_path = any(n.get("persistent_id") == IBD_NODE for n in target_path)
    print(f"\n{IBD_NODE} on {TARGET} path: {on_path}")

    ibd = find(root, IBD_NODE)
    if ibd:
        lv = leaves(ibd)
        print(f"\n## {IBD_NODE} ({ibd.get('taxonomic_range')}, {ibd.get('event_type')}): {len(lv)} leaves")
        for leaf in lv:
            print(leaf.get("node_name"), leaf.get("organism", ""))

    print(f"\n## LCA of {TARGET} with comparators")
    for acc, name in COMPARATORS.items():
        if acc not in paths:
            print(acc, name, "not in tree")
            continue
        p = paths[acc]
        i = 0
        while i < min(len(p), len(target_path)) and p[i] is target_path[i]:
            i += 1
        lca = target_path[i - 1]
        print(acc, name, lca.get("persistent_id"), lca.get("taxonomic_range"), lca.get("event_type"))


if __name__ == "__main__":
    main()
