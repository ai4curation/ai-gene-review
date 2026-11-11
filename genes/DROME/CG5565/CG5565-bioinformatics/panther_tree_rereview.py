"""Place gene leaves in a PANTHER family tree and report which PAINT IBD nodes they descend from.

Usage: python panther_tree_rereview.py FAMILY PAINT_TSV OUT_DIR GENE_ID [GENE_ID ...]

Fetches the PANTHER tree (pantherdb.org treeinfo service), saves it raw,
then for each requested leaf (matched on the tree's gene_id field) prints the
root-to-leaf path and the PAINT IBD rows (from the repo PAINT export) whose
node lies on that path.
"""
import csv
import json
import sys
import urllib.request
from pathlib import Path

family, paint_tsv, out_dir, *gene_ids = sys.argv[1:]
out = Path(out_dir)
out.mkdir(exist_ok=True)
url = f"https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family={family}"
request = urllib.request.Request(url, headers={"User-Agent": "curl/8.0"})
raw = urllib.request.urlopen(request, timeout=180).read()
(out / f"{family}-tree.json").write_bytes(raw)
tree = json.loads(raw)

leaves = []


def walk(node, path):
    if isinstance(node, list):
        for child in node:
            walk(child, path)
        return
    step = {
        "node": node.get("persistent_id", ""),
        "event": node.get("event_type", ""),
        "taxon": node.get("species", ""),
        "subfamily": node.get("sf_id", node.get("prop_sf_id", "")),
    }
    here = path + [step]
    children = node.get("children")
    if children:
        walk(children["annotation_node"], here)
    else:
        leaves.append({"gene_id": node.get("gene_id", ""), "symbol": str(node.get("gene_symbol", "")),
                       "organism": node.get("organism", ""), "path": here})


walk(tree["search"]["tree_topology"]["annotation_node"], [])
paint = list(csv.DictReader(open(paint_tsv), delimiter="\t"))

report = {"family": family, "panther_version": tree["search"]["product"]["version"],
          "n_leaves": len(leaves), "leaves": []}
for gid in gene_ids:
    hits = [leaf for leaf in leaves if leaf["gene_id"] == gid]
    for leaf in hits:
        nodes = {s["node"] for s in leaf["path"]}
        ibd = [r for r in paint if r["node"] in nodes]
        leaf["inherited_paint_ibd"] = ibd
        report["leaves"].append(leaf)
        print(f"== {gid} {leaf['symbol']} ({leaf['organism']}) leaf subfamily {leaf['path'][-1]['subfamily']}")
        print("   " + " > ".join(f"{s['node']}[{s['event'][:3]}|{s['taxon']}|{s['subfamily']}]" for s in leaf["path"]))
        for r in ibd:
            print(f"   inherits IBD {r['go_id']} at {r['node']} seeds={r['seeds']}")
    if not hits:
        print(f"== {gid}: not found in tree")
(out / "results.json").write_text(json.dumps(report, indent=2))
