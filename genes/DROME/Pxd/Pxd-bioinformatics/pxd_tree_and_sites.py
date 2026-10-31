"""Active-site check and PANTHER tree / PAINT node placement for Drosophila Pxd (Q01603).

1. Reports the residues of Q01603 at the UniProt PROSITE-ProRule PRU00298 positions
   (distal His, transition-state Arg, proximal heme-iron His) read from the local
   UniProt flat file.
2. Fetches the unfiltered PANTHER PTHR11475 tree, lists the ancestors of the Pxd leaf
   with their taxonomic range, and reports which PAINT IBD nodes from the local
   PTHR11475-paint.tsv are Pxd ancestors (i.e. which IBD assertions Pxd inherits) and
   which are not. (The species-filtered tree prunes deep nodes such as PTN000158755,
   so it is not used for this step.)
3. Prints the PTN007509807 subtree from the tree filtered to fly, human, mouse, worm
   and zebrafish, showing the fly paralogs closest to Pxd.

Run from repo root:  python3 genes/DROME/Pxd/Pxd-bioinformatics/pxd_tree_and_sites.py
Standard library only; fetches from pantherdb.org.
"""

import csv
import json
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
REPO = HERE.parents[3]
LOCAL_UNIPROT = HERE.parent / "Pxd-uniprot.txt"
PAINT = REPO / "interpro/panther/PTHR11475/PTHR11475-paint.tsv"
ACC = "Q01603"


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read().decode()


def seq_from_flat(txt: str) -> str:
    body = txt.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0]
    return "".join(body.split())


def kids(n: dict) -> list:
    c = n.get("children", {}).get("annotation_node", [])
    return c if isinstance(c, list) else [c]


def leaves(n: dict) -> list:
    k = kids(n)
    if not k:
        return [n]
    return [x for c in k for x in leaves(c)]


def newick(n: dict) -> str:
    k = kids(n)
    if not k:
        return f"{n.get('gene_symbol', '?')}[{n.get('prop_sf_id', '')}]"
    return "(" + ",".join(newick(c) for c in k) + f"){n.get('persistent_id', '')}:{n.get('event_type')}"


def path_to(n: dict, acc: str, path: list) -> list:
    path = path + [n]
    if acc in n.get("node_name", ""):
        return path
    for c in kids(n):
        r = path_to(c, acc, path)
        if r:
            return r
    return []


def main() -> None:
    seq = seq_from_flat(LOCAL_UNIPROT.read_text())
    print(f"Q01603 length {len(seq)}")
    positions = {185: "distal His, proton acceptor", 331: "transition-state Arg",
                 437: "proximal His, heme Fe axial ligand"}
    print("Residues at UniProt PROSITE-ProRule positions in Q01603:")
    for p, role in sorted(positions.items()):
        print(f"  {p}\t{seq[p - 1]}\t{role}\t{seq[p - 6:p + 5]}")

    full = json.loads(fetch("https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR11475"))
    p = path_to(full["search"]["tree_topology"]["annotation_node"], ACC, [])
    ancestor_ids = [n.get("persistent_id") for n in p]
    print("PANTHER ancestors of the Pxd leaf in the unfiltered tree (root first, nearest last):")
    for n in p:
        print(f"  {n.get('persistent_id')}\t{n.get('event_type')}\t{n.get('prop_sf_id')}\t"
              f"{n.get('taxonomic_range', '')}\tleaves={len(leaves(n))}")

    print("PAINT IBD nodes in PTHR11475 and whether Pxd descends from them:")
    with PAINT.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            inherited = row["node"] in ancestor_ids
            print(f"  {row['node']}\t{row['go_id']}\t{row['aspect']}\tPxd_inherits={inherited}")

    filt = json.loads(fetch("https://www.pantherdb.org/services/oai/pantherdb/treeinfo"
                            "?family=PTHR11475&taxonFltr=7227,9606,10090,6239,7955"))
    fp = path_to(filt["search"]["tree_topology"]["annotation_node"], ACC, [])
    target = next(n for n in fp if n.get("persistent_id") == "PTN007509807")
    print("Subtree of PTN007509807 in the tree filtered to fly, human, mouse, worm, zebrafish:")
    print("  " + newick(target))

if __name__ == "__main__":
    main()
