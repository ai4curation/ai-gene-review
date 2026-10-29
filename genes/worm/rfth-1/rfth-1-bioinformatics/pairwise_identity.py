"""Global pairwise identity of C. elegans RFTH-1 (Q23444) to human RFT1 (Q96AA3)
and yeast Rft1 (P38206).

Sequences are read from the local UniProt flat files where present
(genes/worm/rfth-1/rfth-1-uniprot.txt, genes/human/RFT1/RFT1-uniprot.txt);
the yeast sequence is fetched from the UniProt REST API.
Run from the repository root:  uv run python genes/worm/rfth-1/rfth-1-bioinformatics/pairwise_identity.py
"""
import io
import urllib.request

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices


def from_flatfile(path):
    return str(next(SeqIO.parse(path, "swiss")).seq)


def from_uniprot(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url, timeout=60) as r:
        return str(next(SeqIO.parse(io.StringIO(r.read().decode()), "fasta")).seq)


def identity(a, b):
    al = PairwiseAligner()
    al.mode = "global"
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    aln = al.align(a, b)[0]
    ident = aligned = 0
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            aligned += 1
            ident += a[i] == b[j]
    return ident, aligned


worm = from_flatfile("genes/worm/rfth-1/rfth-1-uniprot.txt")
targets = {
    "human RFT1 Q96AA3": from_flatfile("genes/human/RFT1/RFT1-uniprot.txt"),
    "yeast Rft1 P38206": from_uniprot("P38206"),
}
print(f"worm RFTH-1 Q23444 length {len(worm)}")
for name, seq in targets.items():
    ident, aligned = identity(worm, seq)
    print(
        f"{name}: length {len(seq)}; identical {ident}/{aligned} aligned positions "
        f"= {100*ident/aligned:.1f}%; identity over worm length = {100*ident/len(worm):.1f}%"
    )
