# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Fetch the PANTHER PTHR48022 tree and report the leaf-to-root paths of
A. nidulans MstE (Q5B0S0) and N. crassa GLT-1 (Q1K4S3), the most recent common
ancestor of the two, and the leaves of the PTHR48022:SF92 subfamily root clade.

Also reports, for every PAINT IBD node in the local PTHR48022-paint.tsv, whether
MstE descends from that node.

Run: uv run --script panther_placement.py
"""
import csv
import json
import urllib.request
from pathlib import Path

URL = "https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR48022"
PAINT = Path(__file__).resolve().parents[4] / "interpro/panther/PTHR48022/PTHR48022-paint.tsv"
req = urllib.request.Request(URL, headers={"User-Agent": "curl/8"})
root = json.load(urllib.request.urlopen(req))["search"]["tree_topology"]["annotation_node"]


def kids(n):
    c = n.get("children", {}).get("annotation_node", [])
    return c if isinstance(c, list) else [c]


def leaves(n):
    return [n] if not kids(n) else [x for k in kids(n) for x in leaves(k)]


def find(n, acc, path):
    if acc in n.get("node_name", ""):
        return path + [n]
    for k in kids(n):
        r = find(k, acc, path + [n])
        if r:
            return r
    return None


def desc(n):
    return (f"{n.get('persistent_id')}\t{n.get('event_type')}\t"
            f"{n.get('taxonomic_range') or n.get('species')}\t{n.get('sf_id') or ''}\t"
            f"{n.get('prop_sf_id')}\t{len(leaves(n))}")


paths = {}
for acc in ("Q5B0S0", "Q1K4S3"):
    p = find(root, acc, [])
    paths[acc] = p
    print(f"## Leaf-to-root path for {acc} (leaf node_name: {p[-1].get('node_name')})")
    print("persistent_id\tevent\ttaxon\tsf_id\tprop_sf_id\tn_leaves")
    for n in reversed(p):
        print(desc(n))
    print()

ids_a = [n.get("persistent_id") for n in paths["Q5B0S0"]]
ids_b = [n.get("persistent_id") for n in paths["Q1K4S3"]]
mrca = None
for a, b in zip(paths["Q5B0S0"], paths["Q1K4S3"]):
    if a.get("persistent_id") == b.get("persistent_id"):
        mrca = a
print("## MRCA of MstE and GLT-1")
print(desc(mrca))
print()

sf92_roots = [n for n in paths["Q5B0S0"] if n.get("sf_id") == "PTHR48022:SF92"]
for n in sf92_roots:
    print(f"## Leaves under SF92 root {n.get('persistent_id')}")
    for lf in leaves(n):
        print(f"{lf.get('node_name')}\t{lf.get('species') or ''}\t{lf.get('gene_symbol') or ''}")
    print()

print("## PAINT IBD nodes in PTHR48022 and whether MstE descends from them")
with open(PAINT) as fh:
    for row in csv.DictReader(fh, delimiter="\t"):
        print(f"{row['node']}\t{row['go_id']}\t{row['aspect']}\tMstE_descends={row['node'] in ids_a}"
              f"\tGLT1_descends={row['node'] in ids_b}\tMstE_is_seed={'Q5B0S0' in row['seeds']}")
