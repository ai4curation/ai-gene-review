"""Align the N-terminal pseudokinase region of human VPS15 (PIK3R4, Q99570) with
C. elegans VPS-15 (Q23669) and report the worm residue at the position of the
human GTP-specificity gatekeeper Arg103 (PMID:39913640).

Run from the repository root:  uv run python genes/worm/vps-15/vps-15-bioinformatics/gatekeeper_check.py
"""
import io
import urllib.request

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as r:
        return str(next(SeqIO.parse(io.StringIO(r.read().decode()), "fasta")).seq)


human, worm = fetch("Q99570"), fetch("Q23669")
al = PairwiseAligner()
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score, al.extend_gap_score, al.mode = -10, -0.5, "global"
aln = al.align(human[:400], worm[:420])[0]
pos = {}
for (hs, he), (ws, _) in zip(*aln.aligned):
    for k in range(he - hs):
        pos[hs + k + 1] = ws + k + 1
for p, name in [(103, "gatekeeper (GTP specificity)")]:
    wp = pos.get(p)
    print(f"human {human[p-1]}{p} [{name}] -> worm", f"{worm[wp-1]}{wp}" if wp else "gap")
ident = sum(1 for (hs, he), (ws, _) in zip(*aln.aligned) for k in range(he - hs) if human[hs + k] == worm[ws + k])
print(f"identical aligned positions in N-terminal 400 aa: {ident}")
print(aln)
