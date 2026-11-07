from pathlib import Path
import requests
import json
import gzip
import hashlib
import datetime
import concurrent.futures
from ai_gene_review.etl.panther_trees import (
    compact_tree,
    leaf_nodes_for,
    ancestors_of,
    TREE_URL,
)

w = Path("/private/tmp/aigr-nitrogen-pts-taxon-audit")
c = (
    w
    / "analysis/module_audits/bacterial_nitrogen_regulatory_pts/tree-evidence-20261107"
)
c.mkdir(exist_ok=True)
members = {
    "PTHR46244": ["P37177", "Q88CN5", "A0A0H3C823", "P08839"],
    "PTHR33705": ["P0A9N0", "Q88PA2", "A0A0H3C344", "P0AA04", "P08877"],
    "PTHR47738": ["P69829", "Q88PA0", "A0A0H3CDT8"],
}


def fetch(fam):
    try:
        r = requests.get(TREE_URL, params={"family": fam}, timeout=35)
        r.raise_for_status()
        raw = r.content
        tree = compact_tree(r.json())
        return fam, raw, tree, {"url": r.url, "status": r.status_code}
    except Exception as e:
        return fam, None, None, {"url": TREE_URL, "family": fam, "error": str(e)}


with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    rs = list(pool.map(fetch, members))
for fam, raw, tree, d in rs:
    d["observed_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    d["scope"] = (
        "Tree ancestry only; must join to PAINT assertion evidence before adjudicating node placement."
    )
    if tree:
        (c / f"{fam}-treeinfo.json.gz").write_bytes(gzip.compress(raw, mtime=0))
        (c / f"{fam}-compact.json").write_text(json.dumps(tree, sort_keys=True) + "\n")
        d["raw_sha256"] = hashlib.sha256(raw).hexdigest()
        d["leaf_count"] = len(tree["leaves"])
        d["members"] = {}
        for acc in members[fam]:
            leaves = leaf_nodes_for(tree, acc)
            d["members"][acc] = {
                "leaves": leaves,
                "paths": {leaf: sorted(ancestors_of(tree, leaf)) for leaf in leaves},
                "leaf_metadata": {leaf: tree["leaves"][leaf] for leaf in leaves},
            }
    (c / f"{fam}-receipt.json").write_text(json.dumps(d, indent=2) + "\n")
    print(
        fam,
        "success",
        tree is not None,
        "leaves",
        len(tree["leaves"]) if tree else 0,
        flush=True,
    )
