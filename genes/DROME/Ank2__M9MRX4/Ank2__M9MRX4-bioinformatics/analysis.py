"""Reproducible checks for the Ank2 giant isoform M9MRX4 (isoform U / Ank2-XL class).

1. PANTHER 19 placement: where does the Ank2 leaf sit relative to the bilaterian
   ankyrin PAINT node PTN002380879?
2. Isoform coverage: does M9MRX4 contain the Ank2-L (Q7KU92) C-terminal segment
   1682-2089 that Pielage et al. 2008 (PMID:18439405) showed binds microtubules in
   vitro, and the shared N-terminal ankyrin/ZU5/UPA/death-domain region?

Run: python3 analysis.py  (standard library only; needs network)
"""

import json
import urllib.request

PANTHER = "https://www.pantherdb.org/services/oai/pantherdb"


def get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.0"})
    with urllib.request.urlopen(req, timeout=180) as r:
        return r.read().decode()


def fasta(acc: str) -> str:
    txt = get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta")
    return "".join(txt.splitlines()[1:])


def walk(node, depth, out):
    kids = node.get("children", {}).get("annotation_node", [])
    if isinstance(kids, dict):
        kids = [kids]
    out.append(
        "  " * depth
        + " ".join(
            str(x)
            for x in (
                node.get("persistent_id"),
                node.get("event_type", ""),
                node.get("sf_id", ""),
                node.get("species", ""),
                node.get("gene_symbol", ""),
                node.get("organism", ""),
                node.get("gene_id", ""),
            )
            if x
        )
    )
    for k in kids:
        walk(k, depth + 1, out)


def panther_section():
    print("## PANTHER 19 gene classification")
    for gid, org in [
        ("FBgn0261788", 7227),
        ("FBgn0011747", 7227),
        ("ANK1", 9606),
        ("ANK2", 9606),
        ("ANK3", 9606),
    ]:
        d = json.loads(get(f"{PANTHER}/geneinfo?geneInputList={gid}&organism={org}"))
        g = d["search"]["mapped_genes"]["gene"]
        print(f"{gid}\t{g.get('family_id')}\t{g.get('sf_id')}")
    for fam in ("PTHR24123", "PTHR24133"):
        print(f"\n## PANTHER 19 tree {fam} (filtered to fly, human, mouse, worm)")
        d = json.loads(
            get(f"{PANTHER}/treeinfo?family={fam}&taxonFltr=7227,9606,10090,6239")
        )
        out: list[str] = []
        walk(d["search"]["tree_topology"]["annotation_node"], 0, out)
        print("\n".join(out))


def isoform_section():
    print("\n## Isoform coverage")
    u = fasta("M9MRX4")
    lg = fasta("Q7KU92")
    print(f"M9MRX4 length {len(u)}; Q7KU92 (Ank2-L) length {len(lg)}")
    mt = lg[1681:2089]
    print(f"Ank2-L 1682-2089 microtubule-binding segment ({len(mt)} aa) exact in M9MRX4: {mt in u}")
    if mt in u:
        s = u.index(mt) + 1
        print(f"  located at M9MRX4 {s}-{s + len(mt) - 1}")
    # longest shared prefix (N-terminal shared region)
    n = 0
    while n < min(len(u), len(lg)) and u[n] == lg[n]:
        n += 1
    print(f"identical N-terminal prefix shared by M9MRX4 and Ank2-L: {n} aa")
    # longest shared suffix
    c = 0
    while c < min(len(u), len(lg)) and u[-1 - c] == lg[-1 - c]:
        c += 1
    print(f"identical C-terminal suffix shared by M9MRX4 and Ank2-L: {c} aa")
    # 50-mer tiling: fraction of Ank2-L covered exactly by M9MRX4
    k = 50
    hits = sum(1 for i in range(0, len(lg) - k + 1, k) if lg[i : i + k] in u)
    print(f"Ank2-L 50-mer tiles found exactly in M9MRX4: {hits}/{len(range(0, len(lg) - k + 1, k))}")


def xl_section():
    print("\n## Comparison with the 11,634-aa giant isoform AA (X2JCM1)")
    u = fasta("M9MRX4")
    xl = fasta("X2JCM1")
    n = 0
    while n < min(len(u), len(xl)) and u[n] == xl[n]:
        n += 1
    print(f"identical N-terminal prefix shared by M9MRX4 and X2JCM1: {n} aa")
    k = 50
    tiles = range(0, len(xl) - k + 1, k)
    hits = sum(1 for i in tiles if xl[i : i + k] in u)
    print(f"X2JCM1 50-mer tiles found exactly in M9MRX4: {hits}/{len(tiles)}")
    tiles_u = range(0, len(u) - k + 1, k)
    in_xl = sum(1 for i in tiles_u if u[i : i + k] in xl)
    print(f"M9MRX4 50-mer tiles found exactly in X2JCM1: {in_xl}/{len(tiles_u)}")
    lg = fasta("Q7KU92")
    in_l = [i for i in tiles_u if u[i : i + k] in lg]
    print(f"M9MRX4 50-mer tiles found exactly in Ank2-L: {len(in_l)}/{len(tiles_u)}")
    neither = [i for i in tiles_u if u[i : i + k] not in lg and u[i : i + k] not in xl]
    print(f"M9MRX4 50-mer tiles in neither Ank2-L nor X2JCM1: {len(neither)}")
    if neither:
        print(f"  first/last such tile start (1-based): {neither[0] + 1}/{neither[-1] + 1}")


if __name__ == "__main__":
    panther_section()
    isoform_section()
    xl_section()
