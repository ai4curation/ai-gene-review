# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Align donkey SLC16A11 (A0A8C4PS96) to human MCT11 (Q8NCK7) from the repo's cached UniProt flat files.

Usage (from repo root):
    uv run --script genes/EQUAS/SLC16A11__A0A8C4PS96/SLC16A11__A0A8C4PS96-bioinformatics/align_to_human.py
Writes results.json next to this script and prints a summary.
"""
import json
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
DONKEY = REPO / "genes/EQUAS/SLC16A11__A0A8C4PS96/SLC16A11__A0A8C4PS96-uniprot.txt"
HUMAN = REPO / "genes/human/SLC16A11/SLC16A11-uniprot.txt"


def read_uniprot(path: Path) -> tuple[str, list[tuple[int, int]]]:
    seq, in_sq, tms = [], False, []
    for line in path.read_text().splitlines():
        if line.startswith("SQ "):
            in_sq = True
            continue
        if line.startswith("//"):
            break
        if in_sq:
            seq.append(line.replace(" ", ""))
        elif line.startswith("FT   TRANSMEM"):
            a, b = line.split()[2].split("..")
            tms.append((int(a), int(b)))
    return "".join(seq), tms


d_seq, d_tm = read_uniprot(DONKEY)
h_seq, h_tm = read_uniprot(HUMAN)

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.end_insertion_score = 0
aligner.end_deletion_score = 0
aln = aligner.align(d_seq, h_seq)[0]

# map human position (1-based) -> donkey position (1-based)
h2d: dict[int, int] = {}
for (ds, de), (hs, he) in zip(*aln.aligned):
    for i in range(he - hs):
        h2d[int(hs + i + 1)] = int(ds + i + 1)

pairs = list(h2d.items())
ident = sum(1 for h, d in pairs if h_seq[h - 1] == d_seq[d - 1])

tm_ident = []
for a, b in h_tm:
    pos = range(a, b + 1)
    same = sum(1 for p in pos if p in h2d and h_seq[p - 1] == d_seq[h2d[p] - 1])
    tm_ident.append({"human_tm": f"{a}-{b}", "identical_fraction": round(same / len(pos), 2)})

res = {
    "donkey_length": len(d_seq),
    "human_length": len(h_seq),
    "human_residues_aligned": len(pairs),
    "identity_over_aligned_pct": round(100 * ident / len(pairs), 1),
    "donkey_position_of_human_met1": h2d.get(1),
    "donkey_residue_at_that_position": d_seq[h2d[1] - 1] if 1 in h2d else None,
    "donkey_n_terminal_extension_length": (h2d[1] - 1) if 1 in h2d else None,
    "donkey_predicted_tm_helices": len(d_tm),
    "human_predicted_tm_helices": len(h_tm),
    "human_tm_identity": tm_ident,
}
(HERE / "results.json").write_text(json.dumps(res, indent=2) + "\n")
print(json.dumps(res, indent=2))
print(aln)
