"""Locate each PAINT node of PTHR21340-paint.tsv in the PANTHER tree(s) and list
the reference-proteome leaves that descend from it.

Run from this directory:  python3 tree_check.py
Writes PTHR21340-tree-check.txt. Uses the PANTHER treeinfo service (current
PANTHER release) for PTHR21340 and for any extra family given on the command
line (default: PTHR43736, the family PANTHER itself assigns E. coli nudB to).
Nothing is hard-coded about the result: a node that is not found is reported
as not found.
"""
import csv
import json
import sys
import urllib.request

TREEINFO = "https://pantherdb.org/services/oai/pantherdb/treeinfo?family={f}"
FAMILY = "PTHR21340"
EXTRA = sys.argv[1:] or ["PTHR43736"]


def get_tree(family):
    req = urllib.request.Request(TREEINFO.format(f=family), headers={"User-Agent": "ai-gene-review"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.loads(r.read().decode())
    return data["search"]["product"]["version"], data["search"]["tree_topology"]["annotation_node"]


def kids(node):
    c = node.get("children")
    if not c:
        return []
    a = c.get("annotation_node")
    return a if isinstance(a, list) else [a]


def leaves(node):
    k = kids(node)
    if not k:
        return [node]
    out = []
    for x in k:
        out += leaves(x)
    return out


def find(node, target, path=()):
    if node.get("persistent_id") == target:
        return node, path
    for k in kids(node):
        hit = find(k, target, path + (node,))
        if hit:
            return hit
    return None


def sf_of(node):
    return node.get("sf_id") or node.get("prop_sf_id") or "-"


def main():
    nodes = sorted({r["node"] for r in csv.DictReader(open(f"{FAMILY}-paint.tsv"), delimiter="\t")})
    trees = {}
    for fam in [FAMILY] + EXTRA:
        trees[fam] = get_tree(fam)
    lines = []
    for fam, (ver, root) in trees.items():
        lines.append(f"tree {fam} PANTHER version {ver} root {root.get('persistent_id')} "
                     f"taxon {root.get('species')} leaves {len(leaves(root))}")
    for n in nodes:
        found = False
        for fam, (ver, root) in trees.items():
            hit = find(root, n)
            if not hit:
                continue
            found = True
            node, path = hit
            ls = leaves(node)
            sfs = {}
            for leaf in ls:
                sfs[sf_of(leaf)] = sfs.get(sf_of(leaf), 0) + 1
            lines.append(f"node {n} found in {fam} tree; taxon {node.get('species')}; "
                         f"event {node.get('event_type')}; subfamily {sf_of(node)}; "
                         f"depth {len(path)}; leaves {len(ls)}; leaf subfamilies "
                         + ", ".join(f"{k}={v}" for k, v in sorted(sfs.items())))
            for leaf in ls:
                lines.append(f"  leaf of {n}: {leaf.get('persistent_id')} {leaf.get('gene_id')} "
                             f"{leaf.get('organism')} {sf_of(leaf)}")
        if not found:
            lines.append(f"node {n} not found in trees: {', '.join(trees)}")
    with open(f"{FAMILY}-tree-check.txt", "w") as out:
        out.write("\n".join(lines) + "\n")
    print(f"{len(lines)} lines written")


if __name__ == "__main__":
    main()
