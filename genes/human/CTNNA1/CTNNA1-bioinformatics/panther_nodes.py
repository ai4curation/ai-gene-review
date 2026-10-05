"""Report the taxonomic range of PANTHER root nodes for the alpha-catenin
(PTHR18914) and vinculin (PTHR46180) families, and where human CTNNA1 (P35221),
human VCL (P18206) and Dictyostelium ctnnA (Q54MH2 / DDB_G0285939) sit.

Uses the public PANTHER tree API (pantherdb.org/services/oai). No results are
hardcoded; run with `python3 panther_nodes.py`.
"""
import collections
import json
import urllib.request

API = "https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family={}"
QUERY = {"P35221": "human CTNNA1", "P18206": "human VCL",
         "Q54MH2": "Dictyostelium ctnnA", "DDB_G0285939": "Dictyostelium ctnnA"}


def walk(node, path, out):
    kids = node.get("children", {}).get("annotation_node", [])
    if isinstance(kids, dict):
        kids = [kids]
    here = path + [(node.get("persistent_id"), node.get("species"))]
    out.append((node, here))
    for k in kids:
        walk(k, here, out)
    return out


for fam in ["PTHR18914", "PTHR46180"]:
    req = urllib.request.Request(API.format(fam), headers={"User-Agent": "curl/8"})
    with urllib.request.urlopen(req, timeout=120) as r:
        root = json.load(r)["search"]["tree_topology"]["annotation_node"]
    nodes = walk(root, [], [])
    leaves = [n for n, _ in nodes if not n.get("children")]
    orgs = collections.Counter(n.get("organism") for n in leaves)
    print(f"== {fam}: root {root.get('persistent_id')} "
          f"taxon={root.get('species')} leaves={len(leaves)}")
    print("   organisms:", ", ".join(sorted(o for o in orgs if o)))
    for n, path in nodes:
        gid = f"{n.get('gene_id') or ''} {n.get('node_name') or ''}"
        for acc, label in QUERY.items():
            if acc in gid:
                lineage = " > ".join(f"{p}({s})" for p, s in path[:-1] if s)
                print(f"   {label} {gid}: {lineage}")
