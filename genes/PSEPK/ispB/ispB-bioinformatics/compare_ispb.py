"""Global alignment of P. putida KT2440 IspB (Q88Q11) with E. coli IspB (P0AD57).

Reads both sequences from the UniProt flat files in the repository, reports
percent identity over aligned columns, and prints the P. putida residues that
align with E. coli IspB residues reported to affect chain length or activity
(Y38, A79, R321; PMID:11108713) and with the first aspartate-rich motif.

Usage (from the repository root):
    python genes/PSEPK/ispB/ispB-bioinformatics/compare_ispb.py
"""
import re
import sys
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]


def read_uniprot_seq(path: Path) -> str:
    text = path.read_text().splitlines()
    seq, on = [], False
    for line in text:
        if line.startswith("SQ   "):
            on = True
            continue
        if on:
            if line.startswith("//"):
                break
            seq.append(re.sub(r"\s", "", line))
    return "".join(seq)


def main() -> int:
    ec = read_uniprot_seq(ROOT / "genes/ECOLI/ispB/ispB-uniprot.txt")
    pp = read_uniprot_seq(ROOT / "genes/PSEPK/ispB/ispB-uniprot.txt")
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(ec, pp)[0]
    # map E. coli position -> P. putida position
    ec_to_pp = {}
    ident = cols = 0
    for (es, ee), (ps, pe) in zip(*aln.aligned):
        for i, j in zip(range(es, ee), range(ps, pe)):
            ec_to_pp[i + 1] = j + 1
            cols += 1
            ident += ec[i] == pp[j]
    print(f"E. coli IspB P0AD57 length: {len(ec)}")
    print(f"P. putida IspB Q88Q11 length: {len(pp)}")
    print(f"Aligned (ungapped) columns: {cols}")
    print(f"Identical positions: {ident} ({100.0 * ident / cols:.1f}% of aligned columns)")
    for pos in (38, 79, 321):
        j = ec_to_pp.get(pos)
        ppres = f"{pp[j - 1]}{j}" if j else "gap"
        print(f"E. coli {ec[pos - 1]}{pos} aligns with P. putida {ppres}")
    m = re.search(r"DD..D", ec)
    if m:
        s = m.start() + 1
        j = ec_to_pp.get(s)
        print(f"E. coli first DDxxD motif {ec[m.start():m.end()]} at {s}; "
              f"P. putida aligned segment: {pp[j - 1:j + 4] if j else 'gap'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
