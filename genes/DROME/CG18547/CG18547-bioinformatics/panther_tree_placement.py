# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
"""Fetch the PANTHER tree for PTHR42686 and report the root-to-leaf node path
for CG18547 (Q9VGF3) and the characterised members O81884 (LGALDH) and
Q04212 (ARA2), plus the leaves of the Ecdysozoa/Bilateria clades around CG18547."""
import requests

r = requests.get("https://www.pantherdb.org/services/oai/pantherdb/treeinfo",
                 params={"family": "PTHR42686"}, timeout=120)
r.raise_for_status()
root = r.json()["search"]["tree_topology"]["annotation_node"]
TARGETS = ["Q9VGF3", "O81884", "Q04212", "Q20127"]


def kids(n):
    ch = n.get("children", {}).get("annotation_node", [])
    return [ch] if isinstance(ch, dict) else ch


paths = {}


def walk(n, path):
    p = path + [n]
    for acc in TARGETS:
        if "UniProtKB=" + acc in n.get("node_name", ""):
            paths[acc] = p
    for c in kids(n):
        walk(c, p)


walk(root, [])


def label(n):
    return f"{n.get('persistent_id')}({n.get('species') or n.get('organism')},{n.get('event_type')})"


for acc, p in paths.items():
    print(acc, " > ".join(label(n) for n in p))
    print("   MF slim at leaf:", p[-1].get("PANTHER_GO_SLIM_MF"))


def leaves(n):
    if not kids(n):
        return [f"{n.get('node_name')} {n.get('gene_symbol')}"]
    return [x for c in kids(n) for x in leaves(c)]


fly = paths["Q9VGF3"]
for n in fly[-6:-1]:
    print("\nClade", label(n))
    for leaf in leaves(n):
        print("   ", leaf)
# LCA of fly with each characterised member
for acc in ["O81884", "Q04212", "Q20127"]:
    lca = None
    for a, b in zip(fly, paths[acc]):
        if a is b:
            lca = a
    print(f"LCA(Q9VGF3,{acc}) = {label(lca)}")
