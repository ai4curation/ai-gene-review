"""Locate B8BAB0's japonica allele (OsBURP12, Os08g0380100) and characterised
PTHR31458 members in the PANTHER tree, and test whether they descend from the
PAINT IBD node PTN004827911 recorded in interpro/panther/PTHR31458/PTHR31458-paint.tsv.

B8BAB0 itself (indica TrEMBL) is not a PANTHER reference-proteome leaf, so its
japonica allele Q6ZA27 is used as its proxy (see RESULTS-rereview.md).
Run: uv run python panther_tree_placement_rereview.py
"""
import json
import urllib.request

FAMILY = "PTHR31458"
PAINT_NODE = "PTN004827911"
QUERY_UNIPROT = ["Q6ZA27", "Q7XES5", "Q40161", "O80760", "P92982", "P92990", "Q6K2M1"]


def leaves_with_paths(node, path, out):
    step = (node.get("persistent_id"), node.get("prop_sf_id"), node.get("species"), node.get("event_type"))
    path = path + [step]
    children = node.get("children", {}).get("annotation_node", [])
    if isinstance(children, dict):
        children = [children]
    if not children:
        out.append((node, path))
    for child in children:
        leaves_with_paths(child, path, out)
    return out


def main() -> None:
    url = f"https://pantherdb.org/services/oai/pantherdb/treeinfo?family={FAMILY}"
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.0"})
    data = json.load(urllib.request.urlopen(req))
    root = data["search"]["tree_topology"]["annotation_node"]
    leaves = leaves_with_paths(root, [], [])
    print(f"PANTHER version {data['search']['product']['version']}; {len(leaves)} leaves")
    by_acc = {}
    for node, path in leaves:
        name = node.get("node_name") or ""
        for acc in QUERY_UNIPROT:
            if f"UniProtKB={acc}" in name:
                by_acc[acc] = (node, path)
    for acc in QUERY_UNIPROT:
        if acc not in by_acc:
            print(f"{acc}\tNOT_IN_TREE")
            continue
        node, path = by_acc[acc]
        under = any(p[0] == PAINT_NODE for p in path)
        print(f"{acc}\t{node.get('gene_symbol')}\t{node.get('organism')}\t{node.get('prop_sf_id')}\tunder_{PAINT_NODE}={under}")
        for step in path:
            print("\t\t" + "\t".join(str(x) for x in step))
    # last common ancestor of OsBURP12 and each other member
    if "Q6ZA27" in by_acc:
        ref = [p[0] for p in by_acc["Q6ZA27"][1]]
        for acc, (node, path) in by_acc.items():
            if acc == "Q6ZA27":
                continue
            ids = [p[0] for p in path]
            lca = None
            for a, b in zip(ref, ids):
                if a != b:
                    break
                lca = a
            info = next(p for p in path if p[0] == lca)
            print(f"LCA(Q6ZA27,{acc})\t{lca}\t{info[2]}\t{info[3]}")


if __name__ == "__main__":
    main()
