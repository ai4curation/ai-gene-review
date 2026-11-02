"""Pairwise identity of maize C6F010 against reviewed Arabidopsis RBOH proteins.

Downloads sequences from the UniProt REST API, performs global alignment
(BLOSUM62, gap open -10, extend -0.5) and reports % identity over aligned
columns (identical / alignment length excluding terminal gaps of the shorter seq).
Also reports residues at the PIRSR heme-binding His positions of C6F010.
Usage: uv run python rboh_identity.py
"""
import io
import urllib.request

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

Q = "C6F010"
URL = ("https://rest.uniprot.org/uniprotkb/search?format=fasta&size=50&query="
       "organism_id:3702+AND+reviewed:true+AND+gene:RBOH*")


def fetch(url):
    with urllib.request.urlopen(url) as r:
        return list(SeqIO.parse(io.StringIO(r.read().decode()), "fasta"))


query = fetch(f"https://rest.uniprot.org/uniprotkb/{Q}.fasta")[0]
targets = fetch(URL)
al = PairwiseAligner()
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score = -10
al.extend_gap_score = -0.5
al.mode = "global"
rows = []
for t in targets:
    a = al.align(str(query.seq), str(t.seq))[0]
    ident = sum(1 for (qs, qe), (ts, te) in zip(*a.aligned)
                for i, j in zip(range(qs, qe), range(ts, te))
                if query.seq[i] == t.seq[j])
    aligned = sum(qe - qs for qs, qe in a.aligned[0])
    rows.append((100 * ident / aligned, 100 * ident / len(query.seq), t.id, len(t.seq)))
print("target\tlength\tpct_identity_aligned\tpct_identity_query_length")
for p, pq, tid, L in sorted(rows, reverse=True):
    print(f"{tid}\t{L}\t{p:.1f}\t{pq:.1f}")
print()
for pos in (461, 475, 564, 577):
    print(f"C6F010 residue {pos}: {query.seq[pos-1]}")
