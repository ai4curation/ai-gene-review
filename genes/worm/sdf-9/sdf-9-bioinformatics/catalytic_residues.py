"""Map PTP1B (PTPN1, P18031) catalytic/invariant residues onto C. elegans SDF-9 (G5EGA9).

Reads the SDF-9 sequence from the local UniProt flat file (sdf-9-uniprot.txt), fetches
PTP1B from the UniProt REST API, performs a BLOSUM62 local alignment restricted to the
PTP domain region, and prints the SDF-9 residue aligned to each PTP1B landmark position.
Run from repo root:  uv run python genes/worm/sdf-9/sdf-9-bioinformatics/catalytic_residues.py
"""
import re
import sys
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
UNIPROT_TXT = HERE.parent / "sdf-9-uniprot.txt"

# PTP1B landmark residues (1-based, UniProt P18031 numbering) and their roles
LANDMARKS = {
    46: "Y46 pTyr recognition loop (KNRY motif)",
    48: "D48 pTyr recognition loop",
    181: "D181 WPD-loop general acid",
    214: "H214 P-loop (lowers Cys pKa)",
    215: "C215 catalytic nucleophile",
    216: "S216 P-loop",
    220: "G220 P-loop",
    221: "R221 P-loop phosphate binding",
    222: "S222 P-loop (Cys-SH stabilisation)",
    262: "Q262 Q-loop (water positioning)",
}


def read_uniprot_seq(path: Path) -> str:
    text = path.read_text()
    sq = text.split("\nSQ ", 1)[1].split("\n", 1)[1]
    return re.sub(r"[^A-Z]", "", sq.split("//")[0])


def fetch_fasta(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url, timeout=60) as fh:
        lines = fh.read().decode().splitlines()
    return "".join(l.strip() for l in lines if not l.startswith(">"))


def main() -> int:
    sdf9 = read_uniprot_seq(UNIPROT_TXT)
    ptp1b = fetch_fasta("P18031")
    print(f"SDF-9 length {len(sdf9)}; PTP1B length {len(ptp1b)}")
    aligner = Align.PairwiseAligner()
    aligner.mode = "local"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    # restrict PTP1B to catalytic domain (approx. residues 1-300)
    ptp_dom = ptp1b[:300]
    aln = aligner.align(ptp_dom, sdf9)[0]
    print(f"Alignment score: {aln.score}")
    print(aln)
    # build position map PTP1B -> SDF-9
    mapping = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for i in range(a1 - a0):
            mapping[a0 + i + 1] = b0 + i + 1
    print("PTP1B_pos\tPTP1B_res\tSDF9_pos\tSDF9_res\trole")
    for pos, role in LANDMARKS.items():
        s_pos = mapping.get(pos)
        s_res = sdf9[s_pos - 1] if s_pos else "-"
        print(f"{pos}\t{ptp1b[pos-1]}\t{s_pos or '-'}\t{s_res}\t{role}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
