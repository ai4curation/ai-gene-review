"""Map human TRAF2 (Q12933) functional features onto horse F7BIV4.

Reads the two UniProt flat files in the gene folders, globally aligns the
canonical sequences (BLOSUM62, open -10, extend -0.5) and reports, for each
human feature position, the aligned horse residue. Also reports every gap
segment (insertions in horse relative to human) with human flanking positions.

Run from the repository root:
    uv run --with biopython python genes/HORSE/TRAF2/TRAF2-bioinformatics/compare_features_rereview.py
"""

from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
HUMAN = ROOT / "genes/human/TRAF2/TRAF2-uniprot.txt"
HORSE = ROOT / "genes/HORSE/TRAF2/TRAF2-uniprot.txt"

# Human Q12933 positions taken from its UniProt record (FT lines / literature):
# S11 phospho-site, RING 34-73, TRAF-type ZF1 124-180, ZF2 177-233,
# cIAP-binding residues I285/V288/E292 (PubMed:20385093), coiled coil 299-348,
# MATH 351-496.
FEATURES = {
    "S11 (phosphosite)": [11],
    "RING Cys/His ligands (C34..C73 window)": list(range(34, 74)),
    "cIAP-binding I285, V288, E292": [285, 288, 292],
    "coiled coil 299-348": list(range(299, 349)),
    "MATH 351-496": list(range(351, 497)),
}


def read_seq(path: Path) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, ln in enumerate(lines) if ln.startswith("SQ   "))
    seq = []
    for ln in lines[start + 1 :]:
        if ln.startswith("//"):
            break
        seq.append(ln.replace(" ", ""))
    return "".join(seq)


def main() -> None:
    human = read_seq(HUMAN)
    horse = read_seq(HORSE)
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    aln = aligner.align(human, horse)[0]
    # map human 1-based position -> horse 1-based position
    hmap: dict[int, int] = {}
    for (hs, he), (qs, qe) in zip(*aln.aligned):
        for k in range(he - hs):
            hmap[hs + k + 1] = qs + k + 1
    print(f"human length {len(human)}, horse length {len(horse)}")
    for name, positions in FEATURES.items():
        mapped = [p for p in positions if p in hmap]
        ident = sum(human[p - 1] == horse[hmap[p] - 1] for p in mapped)
        print(
            f"{name}: {len(mapped)}/{len(positions)} aligned, "
            f"{ident}/{len(mapped)} identical"
        )
        ch = [p for p in mapped if human[p - 1] in "CH"]
        ch_ident = sum(human[p - 1] == horse[hmap[p] - 1] for p in ch)
        print(f"  Cys/His positions: {ch_ident}/{len(ch)} identical")
        if len(positions) <= 3:
            for p in positions:
                hp = hmap.get(p)
                print(
                    f"  human {human[p - 1]}{p} -> horse "
                    + (f"{horse[hp - 1]}{hp}" if hp else "gap")
                )
    # horse-specific insertions: horse residues not aligned to human
    aligned_horse = set(hmap.values())
    run: list[int] = []
    runs = []
    for q in range(1, len(horse) + 1):
        if q not in aligned_horse:
            run.append(q)
        elif run:
            runs.append(run)
            run = []
    if run:
        runs.append(run)
    inv = {v: k for k, v in hmap.items()}
    for r in runs:
        before = inv.get(r[0] - 1)
        print(
            f"horse insertion {r[0]}-{r[-1]} ({len(r)} aa) "
            f"'{horse[r[0] - 1 : r[-1]]}' after human position {before}"
        )
    unaligned_human = [p for p in range(1, len(human) + 1) if p not in hmap]
    print(f"human residues without a horse partner: {len(unaligned_human)}")


if __name__ == "__main__":
    main()
