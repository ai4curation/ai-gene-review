"""Check conservation of synaptojanin catalytic motifs in fly Synj (Q5U0V7).

Fetches Q5U0V7 (fly Synj), O43426 (human SYNJ1) and G5ECL2 (worm UNC-26) from
UniProt, aligns fly and worm to human with a global pairwise alignment, and
reports the residues at positions aligned to:
  - the SAC domain catalytic CX5R(T/S) motif (located by regex in human SYNJ1)
  - human SYNJ1 R258 (Parkinsonism R258Q; fly R228 per PMID:28331029)
  - 5-phosphatase signature motifs located by regex in human SYNJ1
No results are hardcoded; output is printed for RESULTS.md.
"""

import re
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"fly_Synj": "Q5U0V7", "human_SYNJ1": "O43426", "worm_unc26": "G5ECL2"}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    text = urllib.request.urlopen(url).read().decode()
    return "".join(text.splitlines()[1:])


def mapping(ref: str, other: str) -> dict[int, int]:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    aln = aligner.align(ref, other)[0]
    m: dict[int, int] = {}
    for (rs, re_), (os_, oe) in zip(*aln.aligned):
        for i in range(re_ - rs):
            m[rs + i] = os_ + i
    return m


def main() -> None:
    seqs = {k: fetch(v) for k, v in ACCS.items()}
    for k, s in seqs.items():
        print(f"{k} {ACCS[k]} length={len(s)}")
    human = seqs["human_SYNJ1"]
    motifs = {
        "SAC CX5R(T/S)": r"C.{5}R[TS]",
        "5-ptase WxGDxNxR": r"W.GD.N.R",
        "5-ptase PxxxDR(I/V)": r"P[A-Z]{2}[A-Z]DR[IV]",
    }
    sites: dict[str, list[int]] = {}
    for name, pat in motifs.items():
        for mt in re.finditer(pat, human):
            sites[f"{name} @{mt.start()+1}"] = list(range(mt.start(), mt.end()))
    for other in ("fly_Synj", "worm_unc26"):
        m = mapping(human, seqs[other])
        print(f"\n== {other} vs human SYNJ1")
        for name, pos in sites.items():
            h = "".join(human[p] for p in pos)
            o = "".join(seqs[other][m[p]] if p in m else "-" for p in pos)
            ostart = m.get(pos[0])
            label = f"{other} pos {ostart+1}" if ostart is not None else "gap"
            print(f"{name:28s} human {h:12s} {other} {o:12s} ({label})")
    # Fly R228 (PMID:28331029 knock-in R228Q, equivalent of human R258Q in the
    # isoform numbering used there): report fly residue and aligned human residue.
    m = mapping(human, seqs["fly_Synj"])
    inv = {v: k for k, v in m.items()}
    f = 227
    hpos = inv.get(f)
    print(f"\nfly residue 228 = {seqs['fly_Synj'][f]} context {seqs['fly_Synj'][f-5:f+6]}")
    if hpos is not None:
        print(f"aligned human SYNJ1 (O43426 canonical) residue {hpos+1} = {human[hpos]} context {human[hpos-5:hpos+6]}")


if __name__ == "__main__":
    main()
