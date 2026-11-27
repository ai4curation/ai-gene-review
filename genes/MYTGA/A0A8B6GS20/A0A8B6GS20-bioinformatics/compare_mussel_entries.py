# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Compare A0A8B6GS20 (ORF MGAL_10B089004) with the other M. galloprovincialis
PTHR10807:SF73 entries (ORF MGAL_10B079678) and with human MTMR9, to ask whether the
mussel genome has a full-length MTMR9 gene model that this entry is a partial copy of."""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = ["A0A8B6GS20", "A0A8B6EPV9", "A0A8B6EME1", "A0A8B6ENJ7", "A0A8B6ELH7", "Q96QG7"]


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


seqs = {a: fetch(a) for a in ACCS}
aligner = Align.PairwiseAligner(mode="local")
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -11
aligner.extend_gap_score = -1
t = seqs["A0A8B6GS20"]
for other in ACCS[1:]:
    ref = seqs[other]
    aln = aligner.align(t, ref)[0]
    tb, rb = aln.aligned
    pairs = sum(e - s for s, e in tb)
    ident = sum(t[i] == ref[j] for (ts, te), (rs, re_) in zip(tb, rb) for i, j in zip(range(ts, te), range(rs, re_)))
    print(f"A0A8B6GS20 {tb[0][0] + 1}-{tb[-1][1]} vs {other} (len {len(ref)}) {rb[0][0] + 1}-{rb[-1][1]}: "
          f"{pairs} pairs, identity {ident / pairs:.1%}")
# full-length mussel model vs human MTMR9
for other in ["A0A8B6ENJ7", "A0A8B6EPV9"]:
    aln = aligner.align(seqs[other], seqs["Q96QG7"])[0]
    tb, rb = aln.aligned
    pairs = sum(e - s for s, e in tb)
    print(f"{other} {tb[0][0] + 1}-{tb[-1][1]} vs Q96QG7 {rb[0][0] + 1}-{rb[-1][1]}: "
          f"human coverage {pairs / len(seqs['Q96QG7']):.1%}")
