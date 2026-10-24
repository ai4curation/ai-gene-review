"""Align horse GEMIN5 F6WDM0 to human Q8TEQ6 and check conservation of
experimentally characterised RNA- and cap-contact residues.

Sequences are read from the UniProt flat files already in the repo.
Run: uv run --with biopython python compare_to_human.py
"""
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
GENES = HERE.parents[2]
HORSE = GENES / "HORSE/GEMIN5__F6WDM0/GEMIN5__F6WDM0-uniprot.txt"
HUMAN = GENES / "human/GEMIN5/GEMIN5-uniprot.txt"

# Human residues with experimental contact/mutation data.
# PMID:27881601 (snRNA Sm-site contacts, mutated) and m7G stacking residue Y474;
# PMID:19750007 (cap-binding W286, F338).
RESIDUES = {
    "PMID:27881601 snRNA contact": ["N13", "W14", "Y15", "R33", "R335", "M357",
                                    "R359", "F381", "Y383", "M403", "W422", "Y474"],
    "PMID:27881601 m7G contact": ["Y474", "L580", "N582"],
    "PMID:19750007 cap binding": ["W286", "F338"],
}


def read_seq(path: Path) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, ln in enumerate(lines) if ln.startswith("SQ "))
    seq = []
    for ln in lines[start + 1:]:
        if ln.startswith("//"):
            break
        seq.append(ln.replace(" ", ""))
    return "".join(seq)


def main() -> None:
    horse, human = read_seq(HORSE), read_seq(HUMAN)
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(human, horse)[0]
    # map human index -> horse index
    hmap: dict[int, int] = {}
    ident = aligned = 0
    gaps_human = gaps_horse = 0
    for (hs, he), (qs, qe) in zip(*aln.aligned):
        for k in range(he - hs):
            hmap[hs + k] = qs + k
            aligned += 1
            ident += human[hs + k] == horse[qs + k]
    print(f"human Q8TEQ6 length: {len(human)}")
    print(f"horse F6WDM0 length: {len(horse)}")
    print(f"aligned positions: {aligned}")
    print(f"identical positions: {ident}")
    print(f"identity over aligned: {100 * ident / aligned:.1f}%")
    print(f"identity over human length: {100 * ident / len(human):.1f}%")
    blocks = aln.aligned
    for i in range(1, len(blocks[0])):
        dh = blocks[0][i][0] - blocks[0][i - 1][1]
        dq = blocks[1][i][0] - blocks[1][i - 1][1]
        if dh or dq:
            print(f"gap between blocks: human {blocks[0][i-1][1]+1}-{blocks[0][i][0]} "
                  f"({dh} aa) / horse {blocks[1][i-1][1]+1}-{blocks[1][i][0]} ({dq} aa)")
    for label, res in RESIDUES.items():
        for r in res:
            aa, pos = r[0], int(r[1:])
            assert human[pos - 1] == aa, f"human residue mismatch {r}: {human[pos-1]}"
            q = hmap.get(pos - 1)
            hres = horse[q] if q is not None else "-"
            status = "identical" if hres == aa else "DIFFERENT"
            qpos = q + 1 if q is not None else None
            print(f"{label}\t{r}\thorse {hres}{qpos}\t{status}")


if __name__ == "__main__":
    main()
