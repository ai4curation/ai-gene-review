"""Place Q9VGC0 (CG17404/SP149) in the PANTHER PTHR24256 gene tree.

Downloads the PTHR24256 tree from the PANTHER API, walks from the Q9VGC0 leaf
to the family root, and lists for each ancestor its PTN id, event type,
taxonomic range, subfamily and leaves; then lists the human and Drosophila
leaves in each child clade of the node immediately above the Q9VGC0 subfamily
clade.
Usage: python3 panther_tree_rereview.py > panther_tree_rereview.txt
"""
import json
import urllib.request

URL = "https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR24256"
req = urllib.request.Request(URL, headers={"User-Agent": "curl/8.0"})
with urllib.request.urlopen(req, timeout=300) as fh:
    root = json.load(fh)["search"]["tree_topology"]["annotation_node"]


def kids(n):
    c = n.get("children")
    if not c:
        return []
    c = c["annotation_node"]
    return c if isinstance(c, list) else [c]


def leaves(n):
    k = kids(n)
    return [n] if not k else [x for c in k for x in leaves(c)]


def find(n, acc, path):
    path = path + [n]
    if acc in n.get("node_name", ""):
        return path
    for c in kids(n):
        r = find(c, acc, path)
        if r:
            return r
    return None


def label(leaf):
    acc = leaf.get("node_name", "").split("UniProtKB=")[-1]
    return f"{leaf.get('gene_symbol')}|{leaf.get('organism')}|{acc}"


path = find(root, "UniProtKB=Q9VGC0", [])
print("## Path from Q9VGC0 to the family root")
for n in path[::-1]:
    L = leaves(n)
    print(
        n.get("persistent_id"), n.get("event_type"), n.get("taxonomic_range"),
        n.get("sf_id") or n.get("prop_sf_id"), n.get("sf_name"), f"leaves={len(L)}",
    )
    if len(L) <= 12:
        for leaf in L:
            print("   ", label(leaf))

target_sf = path[-1].get("sf_id") or path[-1].get("prop_sf_id")
top = max(i for i, n in enumerate(path) if (n.get("sf_id") or n.get("prop_sf_id")) != target_sf)
fam_root = path[top]
print("\n## Child clades of", fam_root.get("persistent_id"), "(parent of the", target_sf, "clade)")
for c in kids(fam_root):
    L = leaves(c)
    print(c.get("persistent_id"), c.get("event_type"), c.get("taxonomic_range"),
          c.get("sf_id") or c.get("prop_sf_id"), f"leaves={len(L)}")
    for org in ("Homo sapiens", "Drosophila melanogaster"):
        sel = [label(x) for x in L if x.get("organism") == org]
        print(f"   {org}: {', '.join(sel) if sel else 'none'}")
