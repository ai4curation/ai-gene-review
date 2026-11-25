"""Align ARL9 (and its paralog ARL10) to ARF1 and report the residues at ARF1's
G-domain positions that bind or hydrolyse GTP.

ARF1 reference positions (UniProt P84077 numbering):
  G1 P-loop K30, T31 (nucleotide phosphate binding / Mg2+)
  switch I T48 (Mg2+ / gamma-phosphate)
  G3 Q71 (catalytic glutamine for GTP hydrolysis)
  G4 N126, K127, D129 (guanine base specificity)

Sequences are fetched from UniProt at run time.
"""
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

REF = "P84077"  # ARF1_HUMAN
TARGETS = {"ARL9": "Q6T311", "ARL10": "Q8N8L6"}
SITES = {"G1 K30": 30, "G1 T31": 31, "switch I T48": 48, "G3 Q71": 71,
         "G4 N126": 126, "G4 K127": 127, "G4 D129": 129}


def fetch(acc: str) -> str:
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta") as r:
        lines = r.read().decode().splitlines()
    return "".join(lines[1:])


def mapping(ref: str, tgt: str) -> dict[int, tuple[int, str] | None]:
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score = -10, -0.5
    al.mode = "global"
    best = al.align(ref, tgt)[0]
    m: dict[int, tuple[int, str] | None] = {i + 1: None for i in range(len(ref))}
    for (rs, re_), (ts, _) in zip(*best.aligned):
        for k in range(re_ - rs):
            m[rs + k + 1] = (ts + k + 1, tgt[ts + k])
    return m


def main() -> None:
    ref = fetch(REF)
    for name, site in SITES.items():
        assert ref[site - 1] == name.split()[-1][0], (name, ref[site - 1])
    for gene, acc in TARGETS.items():
        m = mapping(ref, fetch(acc))
        print(f"## {gene} ({acc}) vs ARF1 ({REF})")
        for name, site in SITES.items():
            hit = m[site]
            got = f"{hit[1]}{hit[0]}" if hit else "gap"
            print(f"{name:14s} -> {got}{'' if hit and hit[1] == ref[site - 1] else '  (differs)'}")
        print()


if __name__ == "__main__":
    main()
