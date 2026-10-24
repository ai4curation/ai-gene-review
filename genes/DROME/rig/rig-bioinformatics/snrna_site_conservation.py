# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Check whether Drosophila rig (Q86BY9) retains the human GEMIN5 (Q8TEQ6)
WD40 Sm-site / m7G-cap contact residues reported by Xu et al. 2016 (PMID:27881600).

Sequences are parsed from the cached UniProt flat files in this repository.
A global Needleman-Wunsch alignment (BLOSUM62, open -10, extend -0.5) maps each
human residue position to the aligned fly residue. Output is printed as a table
and written to snrna_site_conservation.json.

Run from the repository root:
    uv run genes/DROME/rig/rig-bioinformatics/snrna_site_conservation.py
"""

import json
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
HUMAN = ROOT / "genes/human/GEMIN5/GEMIN5-uniprot.txt"
FLY = ROOT / "genes/DROME/rig/rig-uniprot.txt"
OUT = Path(__file__).with_name("snrna_site_conservation.json")

# Human GEMIN5 residues named as RNA contacts in PMID:27881600 (expected residue, position).
SITES = [
    ("N", 13), ("W", 14), ("Y", 15), ("R", 33), ("R", 335), ("M", 357),
    ("R", 359), ("F", 381), ("Y", 383), ("M", 403), ("W", 422), ("Y", 474),
    ("L", 580), ("N", 582), ("N", 605), ("K", 641),
]


def read_seq(path: Path) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("SQ "))
    seq = []
    for line in lines[start + 1 :]:
        if line.startswith("//"):
            break
        seq.append(line.replace(" ", ""))
    return "".join(seq)


def main() -> None:
    human = read_seq(HUMAN)
    fly = read_seq(FLY)
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(human, fly)[0]

    # map human index -> fly index (0-based) using aligned blocks
    hmap: dict[int, int] = {}
    for (hs, he), (fs, fe) in zip(*aln.aligned):
        for k in range(int(he - hs)):
            hmap[int(hs) + k] = int(fs) + k

    # global identity over aligned columns
    ident = sum(1 for h, f in hmap.items() if human[h] == fly[f])
    rows = []
    for expected, pos in SITES:
        h_res = human[pos - 1]
        f_idx = hmap.get(pos - 1)
        f_res = fly[f_idx] if f_idx is not None else "-"
        rows.append(
            {
                "human_pos": pos,
                "human_res_expected": expected,
                "human_res_observed": h_res,
                "fly_pos": (f_idx + 1) if f_idx is not None else None,
                "fly_res": f_res,
                "identical": h_res == f_res,
            }
        )
    result = {
        "human_length": len(human),
        "fly_length": len(fly),
        "aligned_pairs": len(hmap),
        "identical_pairs": ident,
        "identity_over_aligned_pairs": round(ident / len(hmap), 3),
        "sites": rows,
    }
    OUT.write_text(json.dumps(result, indent=2))
    print(f"human {len(human)} aa, fly {len(fly)} aa; aligned pairs {len(hmap)}; "
          f"identity over aligned pairs {result['identity_over_aligned_pairs']}")
    print("human\texp\tobs\tfly_pos\tfly_res\tidentical")
    for r in rows:
        print(f"{r['human_pos']}\t{r['human_res_expected']}\t{r['human_res_observed']}\t"
              f"{r['fly_pos']}\t{r['fly_res']}\t{r['identical']}")


if __name__ == "__main__":
    main()
