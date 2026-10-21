# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython"]
# ///
"""Align horse SHLD2 canonical model A0A9L0TUF0 against human SHLD2 long isoform Q86V20-2.

Human Q86V20-2 (904 aa) is the long form used in the biochemical and rescue
studies (PMID:29789392, PMID:30022168). It carries the 69-residue OB-fold-B
exon (inserted after iso-1 K654) that the UniProt displayed isoform lacks.

Reports overall identity and coverage, identity over functionally mapped
human regions, conservation of mutagenised / structural residues, and the
location of horse-specific insertions. Human iso-1 coordinates above 654
are converted to iso-2 by adding 69.

Run: uv run compare_to_human.py
"""

import json
import re
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
GENES = HERE.parents[2]


def read_uniprot_seq(path: Path) -> str:
    text = path.read_text()
    sq = text.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[^A-Z]", "", sq)


def read_fasta(path: Path) -> str:
    lines = path.read_text().splitlines()
    return "".join(line.strip() for line in lines if not line.startswith(">"))


def iso1_to_iso2(pos: int) -> int:
    """Convert a Q86V20-1 coordinate to Q86V20-2.

    >>> iso1_to_iso2(60)
    60
    >>> iso1_to_iso2(699)
    768
    """
    return pos if pos <= 654 else pos + 69


horse = read_uniprot_seq(HERE.parent / "SHLD2__A0A9L0TUF0-uniprot.txt")
human = read_fasta(GENES / "human" / "SHLD2" / "SHLD2-isoform2.fasta")

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"
aligner.end_gap_score = 0
aln = aligner.align(horse, human)[0]
a, b = aln[0], aln[1]

# map human position (1-based) -> horse position (1-based or None),
# and collect runs of horse residues aligned to human gaps
hum2horse: dict[int, int | None] = {}
horse_insertions: list[tuple[int, int, int]] = []  # (after human pos, horse start, length)
hpos = qpos = 0
run: list[int] = []
for x, y in zip(a, b):
    if x != "-":
        hpos += 1
    if y != "-":
        qpos += 1
        hum2horse[qpos] = hpos if x != "-" else None
    if y == "-" and x != "-":
        if not run:
            run = [qpos, hpos, 0]
        run[2] += 1
    elif run:
        horse_insertions.append((run[0], run[1], run[2]))
        run = []
if run:
    horse_insertions.append((run[0], run[1], run[2]))

pairs = [(x, y) for x, y in zip(a, b) if x != "-" and y != "-"]
ident = sum(1 for x, y in pairs if x == y)
covered = sum(1 for v in hum2horse.values() if v is not None)


def region_identity(start: int, end: int) -> dict:
    n = same = 0
    for p in range(start, end + 1):
        q = hum2horse.get(p)
        n += 1
        if q is not None and horse[q - 1] == human[p - 1]:
            same += 1
    return {
        "human_iso2": f"{start}-{end}",
        "horse": f"{hum2horse.get(start)}-{hum2horse.get(end)}",
        "identity": round(same / n, 3),
    }


regions = {
    "SHLD3/MAD2L2-binding N-terminus (iso-1 1-60)": region_identity(1, 60),
    "SHLD3/MAD2L2-binding minimal segment, residues mutated in 6-11 deletion": region_identity(6, 11),
    "ssDNA-binding SHLD2C construct (iso-2 421-904)": region_identity(421, 904),
    "OB-fold-B exon absent from short isoform (iso-2 655-723)": region_identity(655, 723),
    "SHLD1-interaction region (iso-1 652-822)": region_identity(652, iso1_to_iso2(822)),
}

cys = {}
for p1 in (699, 702, 717, 720):
    p2 = iso1_to_iso2(p1)
    q = hum2horse.get(p2)
    cys[f"iso-1 C{p1} / iso-2 {human[p2 - 1]}{p2}"] = (
        f"horse {horse[q - 1]}{q}" if q else "gap"
    )

big_insertions = [
    {"after_human_iso2": h, "horse_start": s, "length": n, "seq": horse[s - 1 : s - 1 + n]}
    for h, s, n in horse_insertions
    if n >= 5
]

result = {
    "horse_length": len(horse),
    "human_iso2_length": len(human),
    "aligned_pairs": len(pairs),
    "identity_over_aligned": round(ident / len(pairs), 3),
    "human_coverage": round(covered / len(human), 3),
    "horse_N_terminus": horse[:20],
    "human_N_terminus": human[:20],
    "regions": regions,
    "zinc_ribbon_cysteines": cys,
    "horse_insertions_ge5": big_insertions,
}
(HERE / "compare_to_human.json").write_text(json.dumps(result, indent=2))
print(json.dumps(result, indent=2))
