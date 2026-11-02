"""Compare the Takifugu gas7a gene models (all from ENSTRUG00000029588) with
human GAS7 (O60861) and mouse Gas7 (Q60780).

Reports pairwise global identity, the region of human GAS7 covered by each fugu
model, and simple motif scans for WW-domain tryptophan spacing and SH3 presence.
Inputs are UniProt FASTA files fetched from rest.uniprot.org (see RESULTS-rereview.md).
Run: uv run python compare_isoforms_rereview.py
"""
import re
from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

here = Path(__file__).parent
recs = {}
for f in ["fugu_gas7.fasta", "human.fasta", "mouse.fasta"]:
    for r in SeqIO.parse(here / f, "fasta"):
        recs[r.id.split("|")[1]] = str(r.seq)

aligner = PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"
aligner.end_gap_score = 0  # do not penalise terminal overhangs

refs = ["O60861", "Q60780"]
fugu = [k for k in recs if k.startswith("A0A674")]
for q in sorted(fugu):
    qs = recs[q]
    print(f"== {q} length {len(qs)}")
    for ref in refs:
        rs = recs[ref]
        aln = aligner.align(qs, rs)[0]
        ident = 0
        aligned = 0
        rpos = []
        for (qa, qb), (ra, rb) in zip(*aln.aligned):
            for i, j in zip(range(qa, qb), range(ra, rb)):
                aligned += 1
                rpos.append(j + 1)
                if qs[i] == rs[j]:
                    ident += 1
        print(
            f"  vs {ref} (len {len(rs)}): aligned {aligned}, identical {ident} "
            f"({100*ident/aligned:.1f}% of aligned), ref span {min(rpos)}-{max(rpos)}"
        )
    # WW domain: two Trp separated by 20-22 residues followed by xxP
    ww = [m.start() + 1 for m in re.finditer(r"(?=W.{20,22}W..P)", qs)]
    print(f"  WW-like W..W..P motif starts: {ww if ww else 'none'}")

for ref in refs:
    rs = recs[ref]
    ww = [m.start() + 1 for m in re.finditer(r"(?=W.{20,22}W..P)", rs)]
    print(f"== {ref} WW-like motif starts: {ww}")
