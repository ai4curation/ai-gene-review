# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Compare NCU11362 (A7UX10) with characterised METTL16 orthologs.

Fetches sequences from UniProt REST, runs global pairwise alignments
(BLOSUM62) and reports identity, coverage and conservation of the
catalytic NPPF motif (human METTL16 N184-P185-P186-F187) and the
C-terminal KA-1 region coverage.
"""
import json
import re
import sys

import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"A7UX10": "NCU11362 N. crassa", "O42662": "Mtl16 S. pombe", "Q86W50": "METTL16 human"}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


seqs = {a: fetch(a) for a in ACCS}
aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"

out = {"lengths": {a: len(s) for a, s in seqs.items()}, "nppf_positions": {}, "pairs": {}}
for a, s in seqs.items():
    out["nppf_positions"][a] = [m.start() + 1 for m in re.finditer("NPPF", s)]

q = seqs["A7UX10"]
for ref in ("O42662", "Q86W50"):
    aln = aligner.align(q, seqs[ref])[0]
    ident = aligned = 0
    qcov = set()
    rcov = set()
    for (qs, qe), (rs, re_) in zip(*aln.aligned):
        for i, j in zip(range(qs, qe), range(rs, re_)):
            aligned += 1
            qcov.add(i)
            rcov.add(j)
            if q[i] == seqs[ref][j]:
                ident += 1
    # map reference NPPF onto query
    mapped = {}
    for p in out["nppf_positions"][ref]:
        for (qs, qe), (rs, re_) in zip(*aln.aligned):
            if rs <= p - 1 < re_:
                qi = int(qs + (p - 1 - rs))
                mapped[p] = {"query_pos": int(qi) + 1, "query_motif": q[qi:qi + 4]}
    out["pairs"][ref] = {
        "identity_over_aligned": round(ident / aligned, 3),
        "aligned_columns": aligned,
        "query_coverage": round(len(qcov) / len(q), 3),
        "reference_coverage": round(len(rcov) / len(seqs[ref]), 3),
        "reference_last_quarter_coverage": round(
            len([j for j in rcov if j >= 0.75 * len(seqs[ref])]) / (len(seqs[ref]) - int(0.75 * len(seqs[ref]))), 3),
        "reference_NPPF_mapped_to_query": mapped,
    }

json.dump(out, sys.stdout, indent=2)
print()
