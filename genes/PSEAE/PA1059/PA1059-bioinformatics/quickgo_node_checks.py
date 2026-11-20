"""Count GOA IBAs propagated from a PAINT node and list annotations of chosen leaves.

Usage: python -I quickgo_node_checks.py GO_ID PTN_NODE ACC[,ACC...]
Also counts the node's IBA rows by assigning group (GO_Central vs TreeGrafter).
Queries the QuickGO annotation API (live; results depend on the GOA release).
"""

import json
import sys
import urllib.request

BASE = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"


def get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.load(resp)


def main() -> None:
    go_id, node, accs = sys.argv[1], sys.argv[2], sys.argv[3]
    d = get(f"{BASE}?goId={go_id}&goUsage=exact&withFrom={node}&limit=1")
    print(f"GOA annotations to {go_id} with with/from {node}: {d['numberOfHits']}")
    counts: dict[str, int] = {}
    page, pages = 1, 1
    while page <= pages and d["numberOfHits"]:
        dd = get(f"{BASE}?goId={go_id}&goUsage=exact&withFrom={node}&limit=200&page={page}")
        pages = dd["pageInfo"]["total"]
        for r in dd["results"]:
            counts[r["assignedBy"]] = counts.get(r["assignedBy"], 0) + 1
        page += 1
    print(f"  by assigning group: {counts}")
    d = get(f"{BASE}?geneProductId={accs}&limit=100")
    print("\n## Annotations of selected leaves (gene product, GO id, evidence, with/from, reference)")
    for r in d["results"]:
        wf = [x["id"] for w in (r.get("withFrom") or []) for x in w["connectedXrefs"]]
        print(f"- {r['geneProductId']} {r['goId']} {r['goEvidence']} {','.join(wf)} {r['reference']}")


if __name__ == "__main__":
    main()
