"""Which Capsaspora T-box protein is Brachyury?

Sebe-Pedros et al. 2013 (PMID:24043797) studied Capsaspora Brachyury (CoBra)
and a second T-box gene (CoTbx3) but give no locus IDs. UniProt lists three
Capsaspora T-box proteins with automatic names. This script extracts each
protein's T-box domain (InterPro IPR001699 coordinates from UniProt features)
and scores it by global alignment (BLOSUM62) against the T-box domains of
human T-box factors from different classes. A clear best match to TBXT
supports, but does not prove, the Brachyury assignment (a phylogeny would be
needed for that). All sequences and coordinates are fetched live.

Usage: uv run python projects/ORIGINS_OF_MULTICELLULARITY/capsaspora-tbox/tbox_assign.py
"""
import json
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

CAPSASPORA = ["A0A0D2VZV8", "A0A0D2WSA5", "A0A0D2VUC6"]
HUMAN = {"TBXT": "O15178", "TBX6": "O95947", "TBX2": "Q13207", "TBX3": "O15119",
         "TBX4": "P57082", "TBX5": "Q99593", "TBX1": "O43435", "TBX19": "O60806",
         "TBR1": "Q16650", "EOMES": "O95936", "TBX20": "Q9UMR3", "MGA": "Q8IWI9"}


def fetch_json(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json"
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)


def tbox_domain(acc):
    d = fetch_json(acc)
    seq = d["sequence"]["value"]
    for f in d.get("features", []):
        if f["type"] == "DNA binding" or (f["type"] == "Domain" and "T-box" in f.get("description", "")):
            s = f["location"]["start"]["value"]; e = f["location"]["end"]["value"]
            return seq[s - 1:e], (s, e)
    return None, None


def main():
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    human = {}
    for name, acc in HUMAN.items():
        dom, loc = tbox_domain(acc)
        if dom:
            human[name] = dom
    print("human T-box domains found:", ", ".join(f"{k}({len(v)})" for k, v in human.items()))
    for acc in CAPSASPORA:
        dom, loc = tbox_domain(acc)
        if not dom:
            print(acc, "no T-box feature found")
            continue
        scores = sorted(((aligner.score(dom, h), n) for n, h in human.items()), reverse=True)
        print(f"\n{acc} T-box {loc} len {len(dom)}")
        for sc, n in scores[:5]:
            print(f"  {n:6s} {sc:7.1f}")


if __name__ == "__main__":
    main()


def residue_at_xbra149():
    """Report the residue aligned to Xenopus Brachyury (P24781) position 149.

    PMID:24043797 reports Lys149 in metazoan Brachyury, Asn at this position in
    other T-box classes, and Arg in Capsaspora Brachyury (CoBra).
    """
    xbra = fetch_json("P24781")["sequence"]["value"]
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "local"
    print(f"\nXenopus Bra residue 149 = {xbra[148]} (context {xbra[143:154]})")
    for acc in CAPSASPORA:
        seq = fetch_json(acc)["sequence"]["value"]
        aln = aligner.align(xbra, seq)[0]
        hit = None
        for (xs, xe), (ys, ye) in zip(*aln.aligned):
            if xs <= 148 < xe:
                hit = ys + (148 - xs)
        if hit is None:
            print(f"{acc}: position 149 not in an aligned block")
        else:
            print(f"{acc}: residue aligned to XBra149 = {seq[hit]} at {hit + 1} (context {seq[hit-5:hit+6]})")


if __name__ == "__main__":
    residue_at_xbra149()
