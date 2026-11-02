# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython", "requests"]
# ///
"""Global alignment of horse DUSP5 (F7ALT2) vs human DUSP5 (Q16690).

Reports identity, and conservation at the catalytic Cys (human C263),
the HCxxGxxRS P-loop, the KIM region (human ~R53/R54 region) and the NLS
(human 53-74, UniProt MOTIF).
"""
import io
import requests
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return str(next(SeqIO.parse(io.StringIO(r.text), "fasta")).seq)


human = fetch("Q16690")
horse = fetch("F7ALT2")
al = PairwiseAligner(mode="global", open_gap_score=-10, extend_gap_score=-0.5)
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
aln = al.align(human, horse)[0]
hmap = {}
ident = paired = 0
for (hs, he), (qs, qe) in zip(*aln.aligned):
    for i, j in zip(range(hs, he), range(qs, qe)):
        hmap[i + 1] = j + 1
        paired += 1
        ident += human[i] == horse[j]
print(f"human Q16690 length {len(human)}; horse F7ALT2 length {len(horse)}")
print(f"identity {ident}/{paired} paired residues = {100*ident/paired:.2f}%")
for name, (s, e) in {"NLS (human 53-74)": (53, 74), "P-loop HCxxGxxRS (human 262-270)": (262, 270)}.items():
    hs = human[s - 1:e]
    qs = "".join(horse[hmap[p] - 1] if p in hmap else "-" for p in range(s, e + 1))
    same = sum(a == b for a, b in zip(hs, qs))
    print(f"{name}: human {hs} horse {qs} ({same}/{len(hs)} identical)")
c = hmap.get(263)
print(f"catalytic Cys: human [263] {human[262]} -> horse [{c}] {horse[c-1] if c else '-'}")
