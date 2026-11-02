# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
"""Place mec-14 (Q20127) in the PANTHER PTHR42686 tree (PANTHER treeinfo API)
and list the ancestral nodes from mec-14 to the root, with the leaves under each,
for C. elegans, D. melanogaster, S. cerevisiae, A. thaliana and human."""
import requests

TAXA = "6239,7227,559292,3702,9606"
URL = f"https://pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR42686&taxonFltr={TAXA}"
root = requests.get(URL, timeout=120).json()["search"]["tree_topology"]["annotation_node"]


def children(n):
    c = n.get("children", {}).get("annotation_node", [])
    return c if isinstance(c, list) else [c]


def leaves(n):
    if n.get("tree_node_type") == "LEAF":
        return [f"{n.get('gene_symbol')}|{n.get('node_name').split('|')[-1]}"]
    return [x for c in children(n) for x in leaves(c)]


def path_to(n, target):
    if target in (n.get("node_name") or ""):
        return [n]
    for c in children(n):
        p = path_to(c, target)
        if p:
            return [n] + p
    return None


print("Leaves in filtered tree:", leaves(root))
path = path_to(root, "UniProtKB=Q20127")
for n in reversed(path[:-1]):
    print(f"{n.get('persistent_id')} {n.get('event_type')} {n.get('species','')} sf={n.get('prop_sf_id')}: {leaves(n)}")
leaf = path[-1]
print("mec-14 leaf:", leaf.get("persistent_id"), leaf.get("prop_sf_id"), leaf.get("sf_name"))
