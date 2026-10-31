"""Which PTHR15184 leaves inherit GO:0042776 (mitochondrial ATP synthesis) from PTN000390017?

PAINT places an IBD for GO:0042776 "proton motive force-driven mitochondrial ATP
synthesis" at PTN000390017 (Eukaryota) and an IRD (NOT) at the Synechocystis leaf
PTN002309672. This script fetches the live PTHR15184 tree, lists every leaf under
PTN000390017 with its organism, UniProt accession and definition, and flags plastid
(chloroplastic) and bacterial members, which make ATP in thylakoids or the plasma
membrane rather than in mitochondria.

Run: uv run --with requests python projects/CONSERVED_FUNCTION_RECOVERY/f_type_atp_synthase/mito_synthesis_node.py
Writes mito_synthesis_node.tsv and mito_synthesis_node_summary.json beside this script.
"""
import collections
import csv
import json
import pathlib

import requests

OUT = pathlib.Path(__file__).parent
TREE = "https://pantherdb.org/services/oai/pantherdb/treeinfo"
IBD, IRD = "PTN000390017", "PTN002309672"


def kids(n):
    ch = n.get("children", {}).get("annotation_node", [])
    return [ch] if isinstance(ch, dict) else ch


def main():
    root = requests.get(TREE, params={"family": "PTHR15184"}, timeout=300).json()
    root = root["search"]["tree_topology"]["annotation_node"]
    node, parent = {}, {}
    stack = [(root, None)]
    while stack:
        n, p = stack.pop()
        node[n["persistent_id"]] = n
        parent[n["persistent_id"]] = p
        stack += [(c, n["persistent_id"]) for c in kids(n)]

    def chain(pid):
        out = []
        while pid:
            out.append(pid)
            pid = parent[pid]
        return out

    def leaves(n):
        out, st = [], [n]
        while st:
            m = st.pop()
            c = kids(m)
            if not c:
                out.append(m)
            st += c
        return out

    rows = [("leaf", "organism", "uniprot", "gene_symbol", "definition", "subfamily", "class", "under_IRD_leaf")]
    counts = collections.Counter()
    for lf in sorted(leaves(node[IBD]), key=lambda m: m.get("organism", "")):
        name = lf.get("node_name", "")
        acc = next((x.split("=")[1] for x in name.split("|") if x.startswith("UniProtKB=")), "")
        defin = lf.get("definition", "")
        org = lf.get("organism", "")
        if "chloroplast" in defin.lower() or "plastid" in defin.lower():
            cls = "plastid"
        elif "mitochondri" in defin.lower():
            cls = "mitochondrial"
        else:
            cls = "unspecified"
        counts[cls] += 1
        rows.append((lf["persistent_id"], org, acc, lf.get("gene_symbol", ""), defin,
                     lf.get("prop_sf_id", ""), cls, IRD in chain(lf["persistent_id"])))
    # Ancestors of the IRD leaf up to the IBD node, with the class make-up of each clade,
    # and the two children of each, to find the lowest node holding the plastid clade.
    def make_up(n):
        c = collections.Counter()
        for m in leaves(n):
            d = m.get("definition", "").lower()
            c["plastid" if "chloroplast" in d else "mitochondrial" if "mitochondri" in d else "unspecified"] += 1
        sf = collections.Counter(m.get("prop_sf_id", "") for m in leaves(n))
        return {"leaves": len(leaves(n)), "classes": dict(c), "subfamilies": dict(sf)}

    walk = []
    pid = IRD
    while pid:
        n = node[pid]
        walk.append({"node": pid, "event_type": n.get("event_type"),
                     "species": n.get("species") or n.get("organism"), **make_up(n),
                     "children": [{"node": c["persistent_id"], "species": c.get("species") or c.get("organism"),
                                   **make_up(c)} for c in kids(n)]})
        if pid == IBD:
            break
        pid = parent[pid]

    # The duplication below the horizontal-transfer node separates plastid from plant
    # mitochondrial beta subunits; report both children.
    split = "PTN008558602"
    plastid_split = {"node": split, "event_type": node[split].get("event_type"),
                     "children": [{"node": c["persistent_id"], "species": c.get("species") or c.get("organism"),
                                   **make_up(c)} for c in kids(node[split])]}

    summary = {
        "ird_to_ibd_walk": walk,
        "plastid_vs_mitochondrial_split": plastid_split,
        "ibd_node": IBD, "ibd_species": node[IBD].get("species"),
        "ibd_parent": parent[IBD], "ird_leaf": IRD,
        "ird_leaf_organism": node[IRD].get("organism"), "ird_leaf_parent": parent[IRD],
        "ird_leaf_under_ibd": IBD in chain(IRD),
        "n_leaves_under_ibd": len(rows) - 1, "leaf_classes": dict(counts),
        "ibd_children": [(c["persistent_id"], c.get("species") or c.get("organism"), len(leaves(c)))
                         for c in kids(node[IBD])],
    }
    with open(OUT / "mito_synthesis_node.tsv", "w", newline="") as fh:
        csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(rows)
    (OUT / "mito_synthesis_node_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    for r in rows[1:]:
        if r[6] != "mitochondrial":
            print(*r, sep="\t")


if __name__ == "__main__":
    main()
