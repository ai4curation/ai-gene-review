# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython>=1.83"]
# ///
"""Global alignment of horse GPC3 (A0A3Q2L6D3) to human GPC3 (P51654).

Reports identity, length and whether human functional residues (from the
P51654 UniProt feature table) are conserved at the aligned horse positions.
Run: uv run --script compare_sequences.py
"""

from pathlib import Path

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices

HERE = Path(__file__).parent

# Human P51654 positions taken from human-GPC3-P51654-uniprot.txt feature table
SITES = {
    "furin cleavage P1 (R358, SITE 358..359)": 358,
    "beta-chain start S359": 359,
    "N-glycosylation N124": 124,
    "N-glycosylation N241": 241,
    "N-glycosylation N418": 418,
    "HS attachment S495": 495,
    "HS attachment S509": 509,
    "GPI-anchor amidated N554": 554,
}


def main() -> None:
    horse = next(SeqIO.parse(HERE / "A0A3Q2L6D3.fasta", "fasta")).seq
    human = next(SeqIO.parse(HERE / "P51654.fasta", "fasta")).seq
    aligner = PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(human, horse)[0]

    # map human index -> horse index
    hmap: dict[int, int] = {}
    ident = paired = 0
    for (hs, he), (qs, qe) in zip(*aln.aligned):
        for i, j in zip(range(hs, he), range(qs, qe)):
            hmap[i] = j
            paired += 1
            ident += human[i] == horse[j]
    cys_h = [i for i, a in enumerate(human) if a == "C"]
    cys_cons = sum(1 for i in cys_h if i in hmap and horse[hmap[i]] == "C")

    print(f"human length {len(human)}; horse length {len(horse)}")
    print(f"paired residues {paired}; identical {ident} ({100 * ident / paired:.2f}%)")
    print(f"human cysteines {len(cys_h)}; conserved in horse {cys_cons}")
    for name, pos in SITES.items():
        i = pos - 1
        j = hmap.get(i)
        hres = human[i]
        qres = horse[j] if j is not None else "-"
        qpos = j + 1 if j is not None else "gap"
        print(f"{name}: human {hres}{pos} -> horse {qres}{qpos} "
              f"{'conserved' if hres == qres else 'NOT conserved'}")
    furin_h = str(human[354:358])
    j = hmap.get(354)
    furin_q = str(horse[j:j + 4]) if j is not None else "gap"
    print(f"furin motif human 355-358 {furin_h}; horse aligned {furin_q}")


if __name__ == "__main__":
    main()
