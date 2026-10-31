"""Isoform comparison, catalytic-residue check and PANTHER tree placement for CG42331.

Compares the benchmark accession Q9VC41 (CG42331-PC) with Q9VC42 (CG42331-PB/PD),
checks residues at the UniProt PROSITE-ProRule catalytic/heme positions in Q9VC41,
and reports the PANTHER 19.0 tree neighbourhood of CG42331 (Q9VC42 leaf).

Run from repo root:  python3 genes/DROME/CG42331/CG42331-bioinformatics/isoform_and_tree_check.py
Uses only the Python standard library; fetches from rest.uniprot.org and pantherdb.org.
"""

import json
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
LOCAL_UNIPROT = HERE.parent / "CG42331-uniprot.txt"


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
    pc = seq_from_flat(LOCAL_UNIPROT.read_text())
    pb_txt = fetch("https://rest.uniprot.org/uniprotkb/Q9VC42.txt")
    pb = seq_from_flat(pb_txt)
    offset = pb.find(pc)
    print(f"Q9VC41 length {len(pc)}; Q9VC42 length {len(pb)}")
    print(f"Q9VC41 is an exact C-terminal suffix of Q9VC42: {pb.endswith(pc)}; starts at Q9VC42 residue {offset + 1}")
    print(f"Q9VC42 residues absent from Q9VC41 (1..{offset}): {pb[:offset]}")
    sig = [l for l in pb_txt.splitlines() if l.startswith("FT   SIGNAL")]
    print(f"Q9VC42 signal peptide feature: {sig}")
    print(f"Q9VC41 N-terminus: {pc[:40]}")
    positions = {85: "heme covalent (Asp)", 86: "distal His, proton acceptor", 214: "transition-state Arg",
                 217: "heme covalent (Glu)", 318: "proximal His, heme Fe axial ligand",
                 87: "Ca2+", 159: "Ca2+", 161: "Ca2+", 163: "Ca2+", 165: "Ca2+"}
    print("Residues at UniProt PROSITE-ProRule positions in Q9VC41:")
    for p, role in sorted(positions.items()):
        print(f"  {p}\t{pc[p - 1]}\t{role}\t{pc[p - 6:p + 5]}")
    tree = json.loads(fetch("https://www.pantherdb.org/services/oai/pantherdb/treeinfo"
                            "?family=PTHR11475&taxonFltr=7227,9606,10090,6239,7955"))
    root = tree["search"]["tree_topology"]["annotation_node"]
    p = path_to(root, "Q9VC42", [])
    print("PANTHER 19.0 ancestors of the CG42331 leaf (nearest last):")
    for n in p:
        print(f"  {n.get('persistent_id')}\t{n.get('event_type')}\t{n.get('prop_sf_id')}")
    print("Subtree of the third-from-leaf ancestor:")
    print("  " + newick(p[-3]))


if __name__ == "__main__":
    main()
