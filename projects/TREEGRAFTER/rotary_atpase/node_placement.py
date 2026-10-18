"""Locate the PAINT node behind the ATP-synthase terms on FliI/SctN in the live PANTHER tree.

Fetches the PTHR15184 tree from the PANTHER API and reports, for the IBD node
PTN008558586 and each TreeGrafter graft node seen in the reviewed GOA files,
its parent chain and which subfamilies each child clade of PTN008558586 holds.

Run: uv run --with requests projects/TREEGRAFTER/rotary_atpase/node_placement.py
"""
import collections, csv, glob, pathlib, requests

OUT = pathlib.Path(__file__).parent
IBD = "PTN008558586"
TREE = "https://pantherdb.org/services/oai/pantherdb/treeinfo"


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

    def ancestors(pid):
        out = []
        while pid:
            out.append(pid)
            pid = parent[pid]
        return out

    def subfams(n):
        acc, stack = collections.Counter(), [n]
        while stack:
            m = stack.pop()
            if m.get("sf_id"):
                acc[f'{m["sf_id"]} {m.get("sf_name", "")}'] += 1
            stack += kids(m)
        return sorted(acc)

    rows = [("node", "role", "event_type", "species", "parent", "under_" + IBD, "subfamilies")]
    ibd = node[IBD]
    rows.append((IBD, "IBD node (GO:0046933, GO:0045259)", ibd.get("event_type"), ibd.get("species") or "",
                 parent[IBD], "self", ""))
    for c in kids(ibd):
        rows.append((c["persistent_id"], "child of IBD node", c.get("event_type"), c.get("species") or "",
                     IBD, "yes", "; ".join(subfams(c))))
    grafts = set()
    for f in glob.glob("genes/*/*/*-goa.tsv"):
        for r in csv.DictReader(open(f), delimiter="\t"):
            if r["REFERENCE"] == "GO_REF:0000118" and r["GO TERM"] == "GO:0046933" and "PTHR15184" not in r["WITH/FROM"]:
                grafts.update(x.split(":")[1] for x in r["WITH/FROM"].split("|") if x.startswith("PANTHER:PTN"))
    for g in sorted(grafts):
        if g in node:
            chain = ancestors(g)
            clade = next((c["persistent_id"] for c in kids(ibd) if c["persistent_id"] in chain), "")
            rows.append((g, f"TreeGrafter graft node (clade {clade})", node[g].get("event_type"),
                         node[g].get("species") or "", parent[g], "yes" if IBD in chain else "no",
                         "; ".join(subfams(node[g]))))
    with open(OUT / "node_placement.tsv", "w", newline="") as fh:
        csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(rows)
    for r in rows:
        print(*r[:6], sep="\t")


if __name__ == "__main__":
    main()
