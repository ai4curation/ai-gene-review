# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Independent re-check of the TM1 protonation-site residue (XylE Asp27 / GLUT1 Asn29)
in GLT-1 (Q1K4S3), its SF92 relative MstE (Q5B0S0) and Neurospora HGT-1/HGT-2.

Each protein is globally aligned (BLOSUM62) to E. coli XylE (P0AGF4); the residue aligned
to XylE position 27 is reported. Sequences are fetched live from UniProt.
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

REF = "P0AGF4"  # XylE, proton-coupled xylose symporter; Asp27 protonation site
REF_POS = 27
TARGETS = {
    "Q1K4S3": "GLT-1 (N. crassa, PTHR48022:SF92)",
    "Q5B0S0": "MstE (A. nidulans AN5860, PTHR48022:SF92)",
    "Q7S0I5": "HGT-1 (N. crassa)",
    "Q7S3Q4": "HGT-2 (N. crassa)",
    "P11166": "GLUT1 (human, uniporter; expect Asn29)",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def mapped_residue(ref: str, tgt: str, pos: int) -> tuple[int | None, str]:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    aln = aligner.align(ref, tgt)[0]
    for (rs, re_), (ts, te) in zip(*aln.aligned):
        if rs <= pos - 1 < re_:
            j = ts + (pos - 1 - rs)
            return j + 1, tgt[j]
    return None, "-"


def main() -> None:
    ref = fetch(REF)
    print(f"reference {REF} position {REF_POS} residue {ref[REF_POS - 1]}")
    print("accession\tlabel\tmapped_position\tresidue")
    for acc, label in TARGETS.items():
        p, aa = mapped_residue(ref, fetch(acc), REF_POS)
        print(f"{acc}\t{label}\t{p}\t{aa}")


if __name__ == "__main__":
    main()
