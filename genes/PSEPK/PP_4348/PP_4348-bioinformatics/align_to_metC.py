"""Global alignment of PP_4348 (Q88EV4) with E. coli MetC (P06721).

Reports percent identity and the PP_4348 residue aligned to MetC Lys210, the
PLP Schiff-base lysine (PMID:8831789). Reads the cached UniProt flat files.
Run from the repository root:
    python genes/PSEPK/PP_4348/PP_4348-bioinformatics/align_to_metC.py
"""
from pathlib import Path
from Bio import Align
from Bio.Align import substitution_matrices


def seq(path: Path) -> str:
    text = path.read_text().split("\nSQ")[1].split("\n", 1)[1]
    return "".join(c for c in text if c.isalpha())


ecoli = seq(Path("genes/ECOLI/metC/metC-uniprot.txt"))
putida = seq(Path("genes/PSEPK/PP_4348/PP_4348-uniprot.txt"))
aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aln = aligner.align(ecoli, putida)[0]
pos = {}
for (s1, e1), (s2, _e2) in zip(*aln.aligned):
    for k in range(e1 - s1):
        pos[s1 + k + 1] = s2 + k + 1
ident = sum(1 for i, j in pos.items() if ecoli[i - 1] == putida[j - 1])
print(f"MetC length {len(ecoli)}, PP_4348 length {len(putida)}")
print(f"aligned pairs {len(pos)}, identical {ident} ({100 * ident / len(pos):.1f}% of aligned)")
j = pos.get(210)
print(f"MetC K210 aligns to PP_4348 position {j}: {putida[j - 1] if j else '-'}")
