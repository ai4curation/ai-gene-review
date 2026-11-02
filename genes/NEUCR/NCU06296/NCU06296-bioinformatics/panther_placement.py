# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Fetch the PANTHER PTHR23023 tree and print the leaf-to-root path for Q7SAD4
with event type, taxon, subfamily and leaf counts."""
import json
import urllib.request

URL = "https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR23023"
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


path = find(root, "Q7SAD4", [])
for n in reversed(path):
    print(n.get("persistent_id"), n.get("event_type"), n.get("taxonomic_range") or n.get("species"),
          n.get("prop_sf_id"), len(leaves(n)))
