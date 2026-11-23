# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests>=2.31"]
# ///
"""Map the GacS HATPase G1 (DxGxG) and G2 (GxGxG) box residues onto aligned
positions in RetS and the other GacS, by BLOSUM62 global pairwise alignment
of each protein against KT2440 GacS (Q88MC3). Also prints each sequence's
UniProt sequence version. Sequences are fetched live from UniProt REST.
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ANCHOR = "Q88MC3"
OTHERS = ["G3XD98", "Q88DK1", "Q9HUV7"]
# Box positions on the anchor, as found by hatpase_motifs.py (G1 444 DTGIG, G2 474 GTGLG).
BOXES = {"G1": [444, 446, 448], "G2": [474, 476, 478]}


def fetch(acc):
    j = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60).json()
    return j["sequence"]["value"], j["entryAudit"]["sequenceVersion"]


def main():
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score, al.mode = -10, -0.5, "global"
    a_seq, a_ver = fetch(ANCHOR)
    print(f"anchor\t{ANCHOR}\tsequence_version={a_ver}")
    for box, ps in BOXES.items():
        print(f"anchor\t{ANCHOR}\t{box}\t" + ",".join(f"{a_seq[p-1]}{p}" for p in ps))
    for acc in OTHERS:
        seq, ver = fetch(acc)
        aln = al.align(a_seq, seq)[0]
        amap = {}
        for (s1, e1), (s2, e2) in zip(*aln.aligned):
            for i, j in zip(range(s1, e1), range(s2, e2)):
                amap[i + 1] = j + 1
        for box, ps in BOXES.items():
            cells = []
            for p in ps:
                q = amap.get(p)
                cells.append(f"{seq[q-1]}{q}" if q else "gap")
            print(f"{acc}\tsequence_version={ver}\t{box}\t" + ",".join(cells))


if __name__ == "__main__":
    main()
