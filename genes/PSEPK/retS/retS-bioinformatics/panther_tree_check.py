# /// script
# requires-python = ">=3.10"
# dependencies = ["requests>=2.31", "pyyaml>=6"]
# ///
"""Re-checkable extract of the PANTHER 19 PTHR45339 tree for the RetS review.

Fetches the family tree from the PANTHER treeinfo service and writes a compact
YAML (panther_tree_check.yaml) recording: the tree size and root; which PAINT
nodes from interpro/panther/PTHR45339/PTHR45339-paint.tsv are present; for the
node in RetS's TreeGrafter WITH field (PTN009177399) its ancestor path and
leaves; and the leaves of PTN000703787. Run from the repo root:

  uv run --no-project --script genes/PSEPK/retS/retS-bioinformatics/panther_tree_check.py
"""
import csv
from datetime import date
from pathlib import Path

import requests
import yaml

FAMILY = "PTHR45339"
URL = f"https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family={FAMILY}"
PAINT = Path(f"interpro/panther/{FAMILY}/{FAMILY}-paint.tsv")
OUT = Path(__file__).with_name("panther_tree_check.yaml")
FOCUS = ["PTN009177399", "PTN000703787"]


def children(n):
    c = (n.get("children") or {}).get("annotation_node", [])
    return [c] if isinstance(c, dict) else c


def index(root):
    idx = {}

    def walk(n, anc):
        idx[n["persistent_id"]] = (n, anc)
        for c in children(n):
            walk(c, anc + [n])

    walk(root, [])
    return idx


def leaves(n):
    return [n] if not children(n) else [x for c in children(n) for x in leaves(c)]


def main():
    data = requests.get(URL, timeout=120).json()
    search = data["search"]
    root = search["tree_topology"]["annotation_node"]
    idx = index(root)
    paint_nodes = sorted({r["node"] for r in csv.DictReader(PAINT.open(), delimiter="\t")})
    out = {
        "source": URL,
        "panther_version": search["product"]["version"],
        "fetched": date.today().isoformat(),
        "root": {"node": root["persistent_id"], "species": root.get("species")},
        "leaf_count": len(leaves(root)),
        "paint_nodes_in_tree": {p: p in idx for p in paint_nodes},
        "focus": {},
    }
    for p in FOCUS:
        if p not in idx:
            out["focus"][p] = "absent"
            continue
        n, anc = idx[p]
        out["focus"][p] = {
            "species": n.get("species"),
            "ancestors": [f"{a['persistent_id']} ({a.get('species')})" for a in anc],
            "leaves": [f"{l['node_name']} | {l.get('definition')}" for l in leaves(n)],
        }
    OUT.write_text(yaml.safe_dump(out, sort_keys=False, width=100))


if __name__ == "__main__":
    main()
