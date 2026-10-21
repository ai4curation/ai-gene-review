# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
"""Locate C28G1.2 (PANTHER leaf PTN007508271) in the PANTHER PTHR11461 tree and
list the leaves under each of its first four ancestors.
Run: uv run panther_placement.py"""
import requests

TARGET = "PTN007508271"
r = requests.get("https://pantherdb.org/services/oai/pantherdb/treeinfo",
                 params={"family": "PTHR11461"}, timeout=300)
r.raise_for_status()
root = r.json()["search"]["tree_topology"]["annotation_node"]
parent, nodes = {}, {}


def kids(n):
    k = n.get("children", {}).get("annotation_node", [])
    return [k] if isinstance(k, dict) else k


stack = [(root, None)]
while stack:
    n, p = stack.pop()
    nodes[n["persistent_id"]] = n
    parent[n["persistent_id"]] = p
    stack.extend((k, n["persistent_id"]) for k in kids(n))


def leaves(pid):
    n = nodes[pid]
    ks = kids(n)
    return [n] if not ks else [x for k in ks for x in leaves(k["persistent_id"])]


x = TARGET
for _ in range(4):
    p = parent[x]
    L = leaves(p)
    print(f"ANCESTOR {p} taxon_range={nodes[p].get('taxonomic_range', '')} n_leaves={len(L)}")
    if len(L) <= 40:
        for leaf in L:
            print(f"    {leaf['persistent_id']}\t{leaf.get('node_name')}\t{leaf.get('gene_symbol')}")
    x = p
