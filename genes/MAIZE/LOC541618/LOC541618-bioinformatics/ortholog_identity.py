"""Pairwise identity of maize K7VAM9 (ZmMPK5) to characterized plant MAPKs,
plus motif positions. Run from repo root:
  uv run python genes/MAIZE/LOC541618/LOC541618-bioinformatics/ortholog_identity.py
Fetches sequences from the UniProt REST API."""
import re, urllib.request
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = ["K7VAM9", "Q39026", "Q39023", "Q39024", "Q336X9", "Q5Z859"]

def fetch(acc):
    txt = urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta").read().decode()
    head, *seq = txt.strip().split("\n")
    return head, "".join(seq)

seqs = {a: fetch(a) for a in ACCS}
q = seqs["K7VAM9"][1]
al = Align.PairwiseAligner(mode="global", open_gap_score=-10, extend_gap_score=-0.5)
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
print(f"query K7VAM9 length {len(q)}")
for m, pat in [("ATP-binding VAIK", "VAIKK"), ("HRD catalytic loop", "HRDLKP"), ("TEY activation loop", "TEY"), ("C-terminal peptide used for anti-ZmMPK5 antibody", "EEQMKDLIYQEALAFNPDYQ")]:
    i = q.find(pat)
    print(f"{m}: {pat} at {i+1 if i>=0 else 'not found'}")
for a in ACCS[1:]:
    head, s = seqs[a]
    aln = al.align(q, s)[0]
    ident = sum(1 for x, y in zip(*aln) if x == y and x != "-")
    cols = sum(1 for x, y in zip(*aln) if x != "-" and y != "-")
    print(f"{head.split()[0]}\tlen={len(s)}\tidentity_over_aligned={ident/cols:.3f}\tidentity_over_query={ident/len(q):.3f}")
