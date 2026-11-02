"""Print the PANTHER 19 tree path (root -> leaf) for Q8P365 and E. coli BtuE (P06610)
in PTHR11592, and the leaves under their shared node.

Run: uv run --no-project --with requests python panther_tree_path_rereview.py
"""
import json

import requests

URL = "https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR11592"
TARGETS = ["Q8P365", "P06610"]


def kids(n):
    c = n.get("children")
    if not c:
        return []
    a = c["annotation_node"]
    return a if isinstance(a, list) else [a]


def paths(n, path, out):
    path = path + [n]
    own = json.dumps({k: v for k, v in n.items() if k != "children"})
    for t in TARGETS:
        if f"UniProtKB={t}" in own:
            out[t] = path
    for k in kids(n):
        paths(k, path, out)


def leaves(n):
    if not kids(n):
        return [n.get("node_name", "")]
    return [x for k in kids(n) for x in leaves(k)]


def main() -> None:
    d = requests.get(URL, timeout=300).json()
    root = d["search"]["tree_topology"]["annotation_node"]
    print("PANTHER version", d["search"]["product"]["version"])
    out: dict = {}
    paths(root, [], out)
    for t, p in out.items():
        print(f"\n{t} path:")
        for node in p:
            print(" ", node.get("persistent_id"), node.get("species"), node.get("event_type"),
                  node.get("sf_id"), node.get("node_name", ""))
    shared = [a for a, b in zip(out["Q8P365"], out["P06610"]) if a is b]
    lca = shared[-1]
    print(f"\nLowest shared node: {lca.get('persistent_id')} {lca.get('species')} {lca.get('sf_id')}")
    for leaf in leaves(lca):
        print("  ", leaf)


if __name__ == "__main__":
    main()
