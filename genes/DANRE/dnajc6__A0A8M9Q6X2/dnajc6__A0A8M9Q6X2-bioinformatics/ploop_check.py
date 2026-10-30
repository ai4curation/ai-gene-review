"""Inspect the PTP/PTEN P-loop (HCxxGxxR) region of zebrafish dnajc6 and compare to human auxilin.

Reads the UniProt flat files in the repo, extracts sequences, aligns the
phosphatase-like region pairwise (Biopython PairwiseAligner, BLOSUM62) and
prints the window around the annotated catalytic-cysteine position.

Run: uv run --with biopython python ploop_check.py
"""
from pathlib import Path
import re

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]


def read_uniprot_seq(path: Path) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith("SQ "))
    seq = []
    for l in lines[start + 1 :]:
        if l.startswith("//"):
            break
        seq.append(l.replace(" ", ""))
    return "".join(seq)


zf = read_uniprot_seq(ROOT / "genes/DANRE/dnajc6__A0A8M9Q6X2/dnajc6__A0A8M9Q6X2-uniprot.txt")
hs = read_uniprot_seq(ROOT / "genes/human/DNAJC6/DNAJC6-uniprot.txt")
print(f"zebrafish dnajc6 A0A8M9Q6X2 length: {len(zf)}")
print(f"human DNAJC6 O75061 length: {len(hs)}")

zf_cys = 223  # UniProt FT ACT_SITE (PROSITE-ProRule PRU00590)
print(f"zebrafish residues 215-235: {zf[214:235]} (C{zf_cys} = {zf[zf_cys-1]})")
window = zf[zf_cys - 2 : zf_cys + 7]
print(f"zebrafish HCxxGxxR-equivalent window ({zf_cys-1}..{zf_cys+7}): {window}")
canon = re.fullmatch(r"HC..G..R", window[:8])
print(f"matches canonical HCxxGxxR (P-loop with final Arg): {bool(canon)}")
print(f"residue at the canonical Arg position ({zf_cys+6}): {zf[zf_cys+5]}")

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"
aln = aligner.align(zf, hs)[0]
# identity over aligned columns
ident = sum(1 for a, b in zip(aln[0], aln[1]) if a == b and a != "-")
cols = sum(1 for a, b in zip(aln[0], aln[1]) if a != "-" and b != "-")
print(f"global identity zebrafish vs human over aligned columns: {ident}/{cols} = {ident/cols:.3f}")

# map zebrafish C223 to human position
zi = hi = 0
for a, b in zip(aln[0], aln[1]):
    if a != "-":
        zi += 1
    if b != "-":
        hi += 1
    if a != "-" and zi == zf_cys:
        print(f"zebrafish C{zf_cys} aligns to human position {hi if b != '-' else 'gap'} ({b})")
        print(f"human window {hi-1}..{hi+7}: {hs[hi-2:hi+7]}")
        break

# J-domain HPD motif
for m in re.finditer("HPD", zf):
    print(f"HPD motif in zebrafish at {m.start()+1}-{m.start()+3}")
for m in re.finditer("HPD", hs):
    print(f"HPD motif in human at {m.start()+1}-{m.start()+3}")
