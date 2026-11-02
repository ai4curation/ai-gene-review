"""Global alignment of Drosophila TyrRS (Q9VV60) with human YARS1 (P54577).

Reports overall identity and the fly residues aligned to human motif positions
(class-I HIGH-like and KMSSS signatures, the mini-TyrRS ELR tripeptide, and the
lysine-rich region reported as the nuclear-localization element).
Motif positions are located on the human sequence by string search, never hardcoded
as fly results.

Run: uv run --with biopython python compare_motifs.py
"""

from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent
fly = str(next(SeqIO.parse(HERE / "Q9VV60.fasta", "fasta")).seq)
hum = str(next(SeqIO.parse(HERE / "P54577.fasta", "fasta")).seq)

aligner = PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"
aln = aligner.align(hum, fly)[0]

# map human index -> fly index
h2f: dict[int, int] = {}
for (hs, he), (fs, fe) in zip(*aln.aligned):
    for k in range(he - hs):
        h2f[hs + k] = fs + k

pairs = sum(he - hs for hs, he in aln.aligned[0])
ident = sum(
    1
    for (hs, he), (fs, fe) in zip(*aln.aligned)
    for k in range(he - hs)
    if hum[hs + k] == fly[fs + k]
)
print(f"human length {len(hum)}, fly length {len(fly)}")
print(f"aligned pairs {pairs}, identical {ident}, identity over aligned {ident / pairs:.3f}")

motifs = {
    "HIGH-like (class I signature region)": "PHVAYF",
    "KMSSS (class I signature)": "KMSSS",
    "ELR tripeptide (mini-TyrRS cytokine motif)": "LELR",
    "lysine-rich region (reported NLS)": "KKKLKKA",
}
for name, m in motifs.items():
    i = hum.find(m)
    if i < 0:
        print(f"{name}: motif {m} not found in human")
        continue
    fly_res = "".join(fly[h2f[j]] if j in h2f else "-" for j in range(i, i + len(m)))
    fstart = h2f.get(i)
    print(
        f"{name}: human {m} at {i + 1}-{i + len(m)}; fly {fly_res}"
        f" at {fstart + 1 if fstart is not None else 'NA'}"
    )
