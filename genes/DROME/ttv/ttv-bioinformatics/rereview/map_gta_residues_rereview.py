"""Map human EXT1/EXT2 GT-A (GT64) domain residues onto Drosophila ttv-PC (D5SHU8).

Re-review analysis (2026-10-20). Independent of the earlier compare.py outputs,
which are left untouched.

Inputs (FASTA, downloaded from UniProt REST and retained in this folder):
  D5SHU8  ttv-PC, 299 aa
  Q9V730  Ttv full length (EXT1_DROME), 760 aa
  Q16394  human EXT1
  Q93063  human EXT2
  Q9Y169  Sotv (EXT2_DROME)

Residue lists come from Li et al. 2023 (PMID:36593275) text: human EXT1 GT-A
DxD motif D565/D567, R595, R701, and the positions where EXT1 differs from the
active EXT2 GT-A site (EXT1 V487 ~ EXT2 Y463, EXT1 P489 ~ EXT2 R465,
EXT1 Q677 ~ EXT2 K651). Each residue is mapped by pairwise global alignment
and the observed amino acid is printed; nothing is hardcoded about outcome.

Usage: uv run --no-project --with biopython==1.85 python map_gta_residues_rereview.py
"""

import json
import sys
from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent


def load(acc: str) -> str:
    return str(next(SeqIO.parse(HERE / f"{acc}.fasta", "fasta")).seq)


def aligner() -> PairwiseAligner:
    a = PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    return a


def position_map(seq_a: str, seq_b: str) -> dict[int, int]:
    """1-based map from positions in seq_a to aligned positions in seq_b.

    >>> position_map("ACDE", "ACDE")[3]
    3
    """
    aln = aligner().align(seq_a, seq_b)[0]
    mapping: dict[int, int] = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for i in range(int(a1 - a0)):
            mapping[int(a0) + i + 1] = int(b0) + i + 1
    return mapping


def identity(seq_a: str, seq_b: str, start: int, end: int) -> float:
    """Percent identity over seq_a[start..end] (1-based) to aligned seq_b."""
    m = position_map(seq_a, seq_b)
    pairs = [(i, m[i]) for i in range(start, end + 1) if i in m]
    same = sum(1 for i, j in pairs if seq_a[i - 1] == seq_b[j - 1])
    return round(100 * same / (end - start + 1), 1)


def main() -> None:
    target = load("D5SHU8")
    ttv = load("Q9V730")
    hext1 = load("Q16394")
    hext2 = load("Q93063")
    sotv = load("Q9Y169")

    ttv_to_target = position_map(ttv, target)
    hext1_to_ttv = position_map(hext1, ttv)
    hext2_to_hext1 = position_map(hext2, hext1)

    out: dict = {"lengths": {k: len(v) for k, v in
                             {"D5SHU8": target, "Q9V730": ttv, "Q16394": hext1,
                              "Q93063": hext2, "Q9Y169": sotv}.items()}}
    starts = [i for i, j in ttv_to_target.items() if j == 1]
    out["ttv_position_of_target_residue_1"] = starts[0] if starts else None
    out["target_vs_ttv_identity_pct_over_target"] = identity(target, ttv, 1, len(target))
    out["hEXT1_GTA_479_728_vs_ttv_identity_pct"] = identity(hext1, ttv, 479, 728)
    out["hEXT1_GTA_479_728_vs_sotv_identity_pct"] = identity(hext1, sotv, 479, 728)

    rows = []
    hext1_residues = {487: "V487 (EXT2 Y463 uridine stacking)",
                      489: "P489 (EXT2 R465 phosphate salt bridge)",
                      565: "D565 DxD", 567: "D567 DxD", 595: "R595",
                      677: "Q677 (EXT2 K651)", 701: "R701"}
    for pos, note in hext1_residues.items():
        t = hext1_to_ttv.get(pos)
        d = ttv_to_target.get(t) if t else None
        rows.append({"hEXT1_pos": pos, "note": note, "hEXT1_aa": hext1[pos - 1],
                     "ttv_pos": t, "ttv_aa": ttv[t - 1] if t else None,
                     "D5SHU8_pos": d, "D5SHU8_aa": target[d - 1] if d else None})
    hext2_residues = {463: "EXT2 Y463", 465: "EXT2 R465", 538: "EXT2 D538",
                      540: "EXT2 D540 Mn", 651: "EXT2 K651"}
    for pos, note in hext2_residues.items():
        h1 = hext2_to_hext1.get(pos)
        rows.append({"hEXT2_pos": pos, "note": note, "hEXT2_aa": hext2[pos - 1],
                     "aligned_hEXT1_pos": h1,
                     "aligned_hEXT1_aa": hext1[h1 - 1] if h1 else None})
    out["residues"] = rows
    json.dump(out, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
