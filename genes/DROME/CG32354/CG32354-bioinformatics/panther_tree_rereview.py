"""Place Q9VSK1 (CG32354) in the PANTHER 19 PTHR10913 tree and list Kazal reactive-site residues.

Usage: uv run --with requests python panther_tree_rereview.py

Fetches the PANTHER tree (treeinfo service) and the UniProt record, then prints:
- the root-to-leaf path of Q9VSK1 (PTN node, taxonomic range, event type),
- the last common ancestor (LCA) of Q9VSK1 with selected characterised members,
- the predicted P1-P1' residues at each PROSITE PRU00798 "Reactive bond" site.
Nothing is hardcoded: all output comes from the live services.
"""

import re

import requests

TARGET = "Q9VSK1"
COMPARATORS = {
    "Q86NV3": "Fs (fly follistatin)",
    "Q9VYH7": "CG12716 (fly)",
    "Q9VNL6": "anon-f (fly)",
    "Q3S1M5": "ZK813.6 (worm)",
    "Q9NQ38": "SPINK5 (human)",
    "Q9UIK5": "TMEFF2 (human)",
    "P19883": "FST (human)",
    "O95633": "FSTL3 (human)",
}


def children(node):
    kids = node.get("children", {}).get("annotation_node", [])
    return [kids] if isinstance(kids, dict) else kids


def leaf_paths(root):
    paths = {}

    def walk(node, path):
        here = path + [node]
        kids = children(node)
        for kid in kids:
            walk(kid, here)
        if not kids:
            m = re.search(r"UniProtKB=(\w+)", node.get("node_name", ""))
            if m:
                paths[m.group(1)] = here

    walk(root, [])
    return paths


def main():
    tree = requests.get(
        "https://www.pantherdb.org/services/oai/pantherdb/treeinfo",
        params={"family": "PTHR10913"},
        timeout=300,
    ).json()
    root = tree["search"]["tree_topology"]["annotation_node"]
    paths = leaf_paths(root)
    target_path = paths[TARGET]
    print(f"## Root-to-leaf path of {TARGET}")
    for n in target_path[:-1]:
        print(n.get("persistent_id"), n.get("taxonomic_range"), n.get("event_type"))
    print(f"\n## LCA of {TARGET} with comparators")
    for acc, name in COMPARATORS.items():
        if acc not in paths:
            print(acc, name, "not in tree")
            continue
        p = paths[acc]
        i = 0
        while i < min(len(p), len(target_path)) and p[i] is target_path[i]:
            i += 1
        lca = target_path[i - 1]
        print(acc, name, lca.get("persistent_id"), lca.get("taxonomic_range"), lca.get("event_type"))

    txt = requests.get(f"https://rest.uniprot.org/uniprotkb/{TARGET}.txt", timeout=60).text
    seq = "".join(txt.split("\nSQ ")[1].split("\n", 1)[1].replace("//", "").split())
    print(f"\n## Reactive-bond sites (length {len(seq)})")
    for m in re.finditer(r"FT   SITE\s+(\d+)\.\.(\d+)\nFT\s+/note=\"Reactive bond\"", txt):
        a = int(m.group(1))
        print(f"{a}-{a + 1}: P1={seq[a - 1]} P1'={seq[a]} context={seq[a - 6:a + 5]}")


if __name__ == "__main__":
    main()
