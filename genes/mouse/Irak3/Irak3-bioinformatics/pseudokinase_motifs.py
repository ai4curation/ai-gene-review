"""Compare catalytic-motif positions of mouse Irak3 (Q8K4B2) with human IRAK3 (Q9Y616)
and the active kinases mouse IRAK4 / human IRAK1 equivalents are not needed: the
question is whether mouse Irak3 shares the human pseudokinase substitutions.

Reads sequences from the UniProt flat files in the repo, aligns them globally
(BLOSUM62, Biopython PairwiseAligner) and reports the residues aligned to the
human catalytic-loop (HRD -> CGS, 291-293) and Mg-binding loop (DFG -> DFA, 311-313)
positions, plus overall identity. Run: uv run --with biopython python pseudokinase_motifs.py
"""

import json
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]


def read_uniprot_seq(path: Path) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("SQ   "))
    seq = []
    for line in lines[start + 1 :]:
        if line.startswith("//"):
            break
        seq.append(line.replace(" ", ""))
    return "".join(seq)


mouse = read_uniprot_seq(ROOT / "genes/mouse/Irak3/Irak3-uniprot.txt")
human = read_uniprot_seq(ROOT / "genes/human/IRAK3/IRAK3-uniprot.txt")

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"
aln = aligner.align(human, mouse)[0]

# map human position (1-based) -> mouse position (1-based) or None
h2m: dict[int, int | None] = {}
for (hs, he), (ms, me) in zip(*aln.aligned):
    for k in range(he - hs):
        h2m[int(hs + k + 1)] = int(ms + k + 1)

identical = sum(
    1
    for (hs, he), (ms, me) in zip(*aln.aligned)
    for k in range(he - hs)
    if human[hs + k] == mouse[ms + k]
)
aligned_len = aln.shape[1]


def motif(hpos: list[int]) -> dict:
    return {
        "human_positions": hpos,
        "human_residues": "".join(human[p - 1] for p in hpos),
        "mouse_positions": [h2m.get(p) for p in hpos],
        "mouse_residues": "".join(
            mouse[h2m[p] - 1] if h2m.get(p) else "-" for p in hpos
        ),
    }


result = {
    "human_length": len(human),
    "mouse_length": len(mouse),
    "identical_positions": int(identical),
    "alignment_columns": int(aligned_len),
    "percent_identity_over_alignment": round(100 * identical / aligned_len, 1),
    "catalytic_loop_HRD_equivalent": motif([291, 292, 293]),
    "mg_binding_DFG_equivalent": motif([311, 312, 313]),
    "vaik_lys_equivalent": motif([192]),
    "death_domain_W74_equivalent": motif([74]),
    "pin1_site_S110_P111_equivalent": motif([110, 111]),
}
out = Path(__file__).with_name("pseudokinase_motifs.json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
