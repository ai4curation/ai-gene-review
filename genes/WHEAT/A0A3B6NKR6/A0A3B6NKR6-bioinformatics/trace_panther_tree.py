"""Trace root-to-leaf paths in the PANTHER PTHR38710 tree (panther_tree_PTHR38710.json,
downloaded from https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR38710)
for the wheat target and characterised relatives, and report where PAINT IBD nodes sit."""
import json
import sys

TARGETS = ["A0A3B6NKR6", "Q93ZC9", "Q9LY82"]
PAINT_NODES = ["PTN000048555", "PTN001475528", "PTN008680403", "PTN008673760"]

tree = json.load(open("panther_tree_PTHR38710.json"))["search"]["tree_topology"]["annotation_node"]


def children(node):
    ch = node.get("children", {}).get("annotation_node", [])
    return ch if isinstance(ch, list) else [ch]


paths = {}
node_seen = set()


def walk(node, path):
    label = f"{node.get('persistent_id')}[{node.get('species', '')}|{node.get('event_type', 'LEAF')}|{node.get('prop_sf_id', '')}]"
    node_seen.add(node.get("persistent_id"))
    gene = node.get("gene_id") or node.get("sequence_id") or ""
    newpath = path + [label]
    for t in TARGETS:
        if t in json.dumps({k: v for k, v in node.items() if k != "children"}):
            paths[t] = newpath + [str(gene)]
    for c in children(node):
        walk(c, newpath)


walk(tree, [])
leaves = json.dumps(tree).count('"gene_id"')
print(f"leaf records with gene_id: {leaves}")
for t in TARGETS:
    print(f"\n== {t}")
    for step in paths.get(t, ["NOT FOUND IN TREE"]):
        print("  ", step)
print()
for n in PAINT_NODES:
    print(n, "present in PTHR38710 tree:", n in node_seen)
common = None
if all(t in paths for t in TARGETS[:2]):
    a, b = paths[TARGETS[0]], paths[TARGETS[1]]
    i = 0
    while i < min(len(a), len(b)) and a[i] == b[i]:
        i += 1
    print("\nLast common ancestor of wheat target and AtGLCAK1:", a[i - 1])
sys.exit(0)
