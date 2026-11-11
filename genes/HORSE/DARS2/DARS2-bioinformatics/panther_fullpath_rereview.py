"""Re-review: fetch the unpruned PANTHER 19 tree for PTHR22594 and print the full ancestral
path (persistent ids, event type, subfamily) of the horse and human DARS2 leaves.
Run: python3 panther_fullpath_rereview.py > panther_fullpath_rereview.out"""
import json
import urllib.request

URL = "https://pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR22594"
req = urllib.request.Request(URL, headers={"User-Agent": "curl/8"})
tree = json.load(urllib.request.urlopen(req))["search"]["tree_topology"]["annotation_node"]

def kids(n):
    c = n.get("children", {}).get("annotation_node", [])
    return c if isinstance(c, list) else [c]

def walk(n, path):
    p = path + [f"{n.get('persistent_id')}({n.get('event_type')}{','+n['sf_id'] if n.get('sf_id') else ''})"]
    if not kids(n) and n.get("organism") in ("Equus caballus", "Homo sapiens") and n.get("gene_symbol") == "DARS2":
        print(n.get("organism"), n.get("gene_id"))
        print("  " + " > ".join(p))
    for k in kids(n):
        walk(k, p)

walk(tree, [])
