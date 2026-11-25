"""Dump the PANTHER reference tree of PTHR40279 (one line per node, indented by depth).

PTHR40279 has no PAINT annotations, so tree_check.py (which starts from the PAINT slice)
cannot run on it. Run from the repository root:
    python3 interpro/panther/PTHR40279/tree_dump.py
Writes interpro/panther/PTHR40279/PTHR40279-tree-dump.txt from the PANTHER treeinfo service.
"""
import json
import urllib.request
from pathlib import Path

FAMILY = "PTHR40279"
URL = f"https://pantherdb.org/services/oai/pantherdb/treeinfo?family={FAMILY}"
req = urllib.request.Request(URL, headers={"User-Agent": "ai-gene-review"})
with urllib.request.urlopen(req, timeout=120) as r:
    data = json.loads(r.read().decode())
root = data["search"]["tree_topology"]["annotation_node"]
lines = [f"tree {FAMILY} PANTHER version {data['search']['product']['version']}"]


def walk(n, depth=0):
    kids = (n.get("children") or {}).get("annotation_node") or []
    kids = kids if isinstance(kids, list) else [kids]
    fields = [n.get("persistent_id"), n.get("sf_id") or "", n.get("event_type") or "",
              n.get("taxonomic_range") or "", n.get("gene_symbol") or "", n.get("sf_name") or ""]
    lines.append("  " * depth + " | ".join(str(f) for f in fields))
    for k in kids:
        walk(k, depth + 1)


walk(root)
out = Path(__file__).resolve().parent / f"{FAMILY}-tree-dump.txt"
out.write_text("\n".join(lines) + "\n")
print(out)
