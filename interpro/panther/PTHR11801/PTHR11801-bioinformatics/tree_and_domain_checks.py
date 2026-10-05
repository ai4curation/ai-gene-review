"""Reproducible checks behind the PTHR11801 (STAT) family review.

1. Places every PTHR11801 PAINT node in the PANTHER 19 tree (taxon, event, subfamily)
   and reports which PANTHER subfamilies descend from each IBD node.
2. Lists the organisms represented in the PANTHER JAK family (PTHR45807), to show which
   STAT-bearing lineages have no JAK.
3. Reports the InterPro domain cross-references of selected STAT-family members, to
   show which members carry a STAT DNA-binding domain.

Nothing is hardcoded except the query lists; run with `python3 tree_and_domain_checks.py`.
Network access to pantherdb.org and rest.uniprot.org is required.
"""
import collections
import csv
import json
import re
import urllib.request
from pathlib import Path

TREE = "https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family={}"
UNIPROT = "https://rest.uniprot.org/uniprotkb/{}?format=txt"
HERE = Path(__file__).resolve().parent
PAINT = HERE.parent / "PTHR11801-paint.tsv"
DOMAIN_QUERY = ["P40763", "P42224", "Q24151", "Q9NAD6", "Q20977", "O00910",
                "Q54BD4", "Q70GP4", "Q86I20", "B5X561", "Q56XZ1"]
DBD_IPR = {"IPR008967", "IPR013801", "IPR012345", "IPR037059"}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8"})
    with urllib.request.urlopen(req, timeout=180) as r:
        return r.read().decode()


def kids(n):
    k = n.get("children", {}).get("annotation_node", [])
    return [k] if isinstance(k, dict) else k


def index_tree(fam):
    root = json.loads(fetch(TREE.format(fam)))["search"]["tree_topology"]["annotation_node"]
    nodes = {}

    def walk(n, sf):
        sf = n.get("sf_id") or sf
        ch = kids(n)
        leaves = []
        for c in ch:
            leaves += walk(c, sf)
        if not ch:
            m = re.search(r"UniProtKB=(\w+)", n.get("node_name") or n.get("gene_id") or "")
            leaves = [(m.group(1) if m else None, n.get("organism"), n.get("gene_symbol"), sf)]
        nodes[n.get("persistent_id")] = (n.get("species"), n.get("event_type"), sf, leaves)
        return leaves

    walk(root, None)
    return root, nodes


def main():
    _, nodes = index_tree("PTHR11801")
    print("== PTHR11801 PAINT nodes in the PANTHER tree")
    seen = set()
    with open(PAINT) as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            node = row["node"]
            if node in seen:
                continue
            seen.add(node)
            species, event, sf, leaves = nodes.get(node, (None, None, None, []))
            sfs = collections.Counter(leaf[3] for leaf in leaves)
            orgs = sorted({leaf[1] for leaf in leaves if leaf[1]})
            print(f"{node}\ttaxon={species}\tevent={event}\tnode_SF={sf}\tleaves={len(leaves)}")
            print("   descendant SFs:", dict(sorted(sfs.items(), key=lambda x: str(x[0]))))
            print("   has Dictyostelium:", any("Dictyostelium" in o for o in orgs),
                  "| has Caenorhabditis:", any("Caenorhabditis" in o for o in orgs),
                  "| has plants (Arabidopsis):", any("Arabidopsis" in o for o in orgs))

    root, jak = index_tree("PTHR45807")
    print(f"\n== PTHR45807 (JAK) organisms represented; root {root.get('persistent_id')} "
          f"({root.get('species')})")
    orgs = collections.Counter()
    all_leaves = jak[root.get("persistent_id")][3]
    for leaf in all_leaves:
        orgs[leaf[1]] += 1
    for o, c in sorted(orgs.items(), key=lambda x: str(x[0])):
        print(f"   {c}\t{o}")
    for probe in ["Caenorhabditis elegans", "Caenorhabditis briggsae", "Pristionchus pacificus",
                  "Dictyostelium discoideum", "Arabidopsis thaliana", "Nematostella vectensis"]:
        print(f"   JAK members in {probe}: {orgs.get(probe, 0)}")

    print("\n== InterPro cross-references (STAT DNA-binding-domain entries marked *)")
    for acc in DOMAIN_QUERY:
        txt = fetch(UNIPROT.format(acc))
        gn = re.search(r"^GN   Name=([^;{ ]+)", txt, re.M)
        iprs = re.findall(r"^DR   InterPro; (IPR\d+); ([^.]+)\.", txt, re.M)
        has_dbd = any(i in DBD_IPR for i, _ in iprs)
        print(f"{acc}\t{gn.group(1) if gn else '?'}\tDNA-binding domain entry: {has_dbd}")
        print("   " + "; ".join(f"{i}{'*' if i in DBD_IPR else ''} {n}" for i, n in iprs))


if __name__ == "__main__":
    main()
