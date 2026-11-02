"""Global pairwise identity of the wheat target vs the two Arabidopsis glucuronokinases
(sequences in seqs_rereview.fasta, fetched from rest.uniprot.org). BLOSUM62, gap open -10, extend -0.5."""
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

recs = {r.id.split("|")[1]: str(r.seq) for r in SeqIO.parse("seqs_rereview.fasta", "fasta")}
al = PairwiseAligner(mode="global", substitution_matrix=substitution_matrices.load("BLOSUM62"),
                     open_gap_score=-10, extend_gap_score=-0.5)
q = "A0A3B6NKR6"
for t in ["Q93ZC9", "Q9LY82"]:
    aln = al.align(recs[q], recs[t])[0]
    ident = sum(1 for a, b in zip(*aln) if a == b and a != "-")
    cols = sum(1 for a, b in zip(*aln) if a != "-" and b != "-")
    print(f"{q} ({len(recs[q])} aa) vs {t} ({len(recs[t])} aa): identical={ident} aligned={cols} "
          f"identity_over_aligned={ident/cols:.3f} identity_over_target_len={ident/len(recs[t]):.3f}")
aln = al.align(recs["Q93ZC9"], recs["Q9LY82"])[0]
ident = sum(1 for a, b in zip(*aln) if a == b and a != "-"); cols = sum(1 for a, b in zip(*aln) if a != "-" and b != "-")
print(f"Q93ZC9 vs Q9LY82: identity_over_aligned={ident/cols:.3f}")
# conserved GHMP motif II (glycine-rich PxGSGLGSSAA-like phosphate-binding loop)
import re
for k, s in recs.items():
    m = re.search(r"G[LS][SG]GSSA", s)
    print(k, "GHMP phosphate-binding loop match:", m.group(0) if m else None, m.start() + 1 if m else "")
