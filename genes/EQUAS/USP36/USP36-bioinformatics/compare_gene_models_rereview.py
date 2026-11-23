# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython"]
# ///
"""Compare the donkey USP36 benchmark model A0A9L0JCH5 with the other donkey, horse and
human USP36 products, to ask whether its 33-residue USP-domain insertion (donkey 253-285)
is shared by other gene models of the same gene.

Usage: uv run --script compare_gene_models_rereview.py <donkey_uniprot.txt> <acc> [<acc> ...]
For each accession: fetches the UniProt flat file (REST), reports length, the Ensembl gene id(s),
global identity to A0A9L0JCH5, and whether the insertion segment is present (best local
alignment of the 33-mer, identity reported).
"""
import sys, urllib.request
from Bio import Align
from Bio.Align import substitution_matrices


def parse_flat(txt):
    seq, inseq, genes = [], False, []
    for line in txt.splitlines():
        if line.startswith("DR   Ensembl;"):
            genes.append(line.split(";")[3].strip().rstrip("."))
        if line.startswith("SQ"):
            inseq = True
            continue
        if line.startswith("//"):
            break
        if inseq:
            seq.append("".join(line.split()))
    return "".join(seq), sorted(set(genes))


def aligner(mode):
    a = Align.PairwiseAligner()
    a.mode = mode
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score, a.extend_gap_score = -10, -0.5
    return a


def identity(aln):
    ident = pairs = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            pairs += 1
            ident += aln.target[i] == aln.query[j]
    return ident, pairs


donkey_file, accs = sys.argv[1], sys.argv[2:]
dseq, dgenes = parse_flat(open(donkey_file).read())
ins = dseq[252:285]
print(f"benchmark A0A9L0JCH5 length {len(dseq)} Ensembl gene {dgenes}")
print(f"insertion segment (253-285): {ins}")
g, l = aligner("global"), aligner("local")
for acc in accs:
    txt = urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.txt").read().decode()
    seq, genes = parse_flat(txt)
    gi, gp = identity(g.align(dseq, seq)[0])
    la = l.align(ins, seq)[0]
    li, lp = identity(la)
    start = la.aligned[1][0][0] + 1 if lp else None
    print(f"{acc}\tlen {len(seq)}\tgene {genes}\tglobal identity to benchmark {gi}/{gp} ({100*gi/gp:.1f}%)"
          f"\tinsertion best local match {li}/{len(ins)} identical over {lp} aligned, starting at {start}")
