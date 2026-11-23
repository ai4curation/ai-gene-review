# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Re-review sequence comparison for CG32086 (M9NF85).

Fetches UniProt sequences, compares the CG32086 isoforms, scans for the
PROSITE PS00018 EF-hand calcium-binding loop pattern, and computes local
alignments of M9NF85 against human EFHB and fly PTHR12086 members.
Run: uv run compare_sequences_rereview.py
"""
import difflib
import re

import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "M9NF85": "CG32086 isoform (benchmark)",
    "Q8IQG0": "CG32086 isoform (PANTHER representative, carries IBA)",
    "Q8T4E3": "CG32086 cDNA AT02370p",
    "Q8N7U6": "human EFHB (PTHR12086:SF12)",
    "Q7KUG5": "fly CG6110 FBgn0053489 (PTHR12086:SF12)",
    "Q8MST3": "fly CG6110 FBgn0053490 (PTHR12086:SF12)",
    "Q9VXP5": "fly Efhc1.1 (PTHR12086:SF11)",
}
PS00018 = re.compile(
    r"(?=(D[^W][DNS][^ILVFYW][DENSTG][DNQGHRK][^GP][LIVMC][DENQSTAGC]..[DE]))"
)


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


seqs = {a: fetch(a) for a in ACCS}
print("## Lengths")
for a, d in ACCS.items():
    print(f"{a}\t{len(seqs[a])}\t{d}")

print("\n## Isoform differences relative to M9NF85")
for other in ["Q8IQG0", "Q8T4E3"]:
    sm = difflib.SequenceMatcher(None, seqs["M9NF85"], seqs[other], autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != "equal":
            print(f"{other}\t{tag}\tM9NF85 {i1+1}-{i2}\t{other} {j1+1}-{j2}\t"
                  f"{seqs['M9NF85'][i1:i2][:40]}|{seqs[other][j1:j2][:40]}")

print("\n## PS00018 EF-hand Ca-binding loop matches")
for a in ACCS:
    hits = [(m.start() + 1, m.group(1)) for m in PS00018.finditer(seqs[a])]
    print(f"{a}\t{hits}")

aligner = Align.PairwiseAligner()
aligner.mode = "local"
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -11
aligner.extend_gap_score = -1
print("\n## Local alignments of M9NF85 vs relatives")
q = seqs["M9NF85"]
for a in ["Q8N7U6", "Q7KUG5", "Q8MST3", "Q9VXP5"]:
    aln = aligner.align(q, seqs[a])[0]
    qb, tb = aln.aligned
    qcov = sum(e - s for s, e in qb)
    ident = sum(
        1 for (qs, qe), (ts, te) in zip(qb, tb) for k in range(qe - qs)
        if q[qs + k] == seqs[a][ts + k]
    )
    print(f"{a}\tscore={aln.score:.0f}\tM9NF85 {qb[0][0]+1}-{qb[-1][1]}\t"
          f"{a} {tb[0][0]+1}-{tb[-1][1]}\taligned={qcov}\tidentity={ident/qcov:.2f}")
