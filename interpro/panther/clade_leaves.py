"""List the reference-proteome leaves below chosen PANTHER tree nodes.

Run from the repository root:
    python3 interpro/panther/clade_leaves.py PTHR43651 PTN002450373 [PTN... ...]
Prints, for each node, its taxon, event and subfamily, then every leaf below it
with organism, UniProt accession, PANTHER definition and the path from the node.
Uses the PANTHER treeinfo service (current release); a node that is not found is
reported as not found.
"""
import json
import sys
import urllib.request

TREEINFO = "https://pantherdb.org/services/oai/pantherdb/treeinfo?family={f}"
family, nodes = sys.argv[1], sys.argv[2:]
req = urllib.request.Request(TREEINFO.format(f=family), headers={"User-Agent": "ai-gene-review"})
with urllib.request.urlopen(req, timeout=120) as r:
    data = json.loads(r.read().decode())
version = data["search"]["product"]["version"]
root = data["search"]["tree_topology"]["annotation_node"]


def kids(n):
    c = n.get("children", {}).get("annotation_node", [])
    return [c] if isinstance(c, dict) else c


def find(n, pid):
    if n.get("persistent_id") == pid:
        return n
    for c in kids(n):
        hit = find(c, pid)
        if hit is not None:
            return hit
    return None


def leaves(n, path):
    k = kids(n)
    if not k:
        yield n, path
    for c in k:
        yield from leaves(c, path + [c.get("persistent_id")])


print(f"tree {family} PANTHER version {version} root {root.get('persistent_id')}")
for pid in nodes:
    node = find(root, pid)
    if node is None:
        print(f"node {pid} not found in {family}")
        continue
    lv = list(leaves(node, []))
    print(f"node {pid}; taxon {node.get('species')}; event {node.get('event_type')}; "
          f"subfamily {node.get('sf_id')}; leaves {len(lv)}")
    for leaf, path in lv:
        acc = leaf.get("node_name", "").split("UniProtKB=")[-1]
        print(f"  leaf of {pid}: {leaf.get('persistent_id')} {leaf.get('organism')} "
              f"UniProtKB:{acc} | {leaf.get('definition')} | via {' > '.join(path[:-1]) or '-'}")
