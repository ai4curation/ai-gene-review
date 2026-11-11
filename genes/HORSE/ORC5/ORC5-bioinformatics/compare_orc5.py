# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython>=1.83"]
# ///
"""Align horse ORC5 (A0A3Q2KSP7) to human ORC5 (O43913) and mouse Orc5 (Q9WUV0).

Reports global identity/coverage and the residues at the horse positions
equivalent to human sites described for HsORC5 in the structure paper
PMID:28112645 (Walker A P-loop GHTASGKT 37-44, Walker B DKAE 125-128, tether R104,
P139, arginine finger R143, Y182, R226).

Run: uv run --script compare_orc5.py
"""

from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).parent


def read_fasta(path: Path) -> str:
    lines = path.read_text().splitlines()
    return "".join(line.strip() for line in lines if not line.startswith(">"))


def read_uniprot_seq(path: Path) -> str:
    seq = []
    in_sq = False
    for line in path.read_text().splitlines():
        if line.startswith("SQ"):
            in_sq = True
            continue
        if line.startswith("//"):
            break
        if in_sq:
            seq.append(line.replace(" ", ""))
    return "".join(seq)


def mapping(aln) -> dict[int, int]:
    """Map 1-based target (reference) positions to 1-based query positions."""
    m = {}
    for (t0, t1), (q0, q1) in zip(*aln.aligned):
        for i in range(t1 - t0):
            m[t0 + i + 1] = q0 + i + 1
    return m


def main() -> None:
    horse = read_uniprot_seq(HERE.parent / "ORC5-uniprot.txt")
    refs = {
        "human O43913": read_fasta(HERE / "human_O43913.fasta"),
        "mouse Q9WUV0": read_fasta(HERE / "mouse_Q9WUV0.fasta"),
    }
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    print(f"horse A0A3Q2KSP7 length: {len(horse)}")
    for name, ref in refs.items():
        aln = aligner.align(ref, horse)[0]
        m = mapping(aln)
        ident = sum(1 for r, h in m.items() if ref[r - 1] == horse[h - 1])
        print(f"\n## {name} (length {len(ref)})")
        print(f"paired positions: {len(m)}; identical: {ident} "
              f"({100 * ident / len(m):.2f}% of paired); "
              f"coverage of reference: {100 * len(m) / len(ref):.2f}%; "
              f"coverage of horse: {100 * len(m) / len(horse):.2f}%")
        if name.startswith("human"):
            sites = {
                "Walker A P-loop 37-44": range(37, 45),
                "tether R104": [104],
                "Walker B DKAE 125-128": range(125, 129),
                "P139": [139],
                "arginine finger R143": [143],
                "Y182": [182],
                "R226": [226],
            }
            for label, positions in sites.items():
                h_res = "".join(ref[p - 1] for p in positions)
                q_pos = [int(m[p]) if p in m else None for p in positions]
                q_res = "".join(horse[q - 1] if q else "-" for q in q_pos)
                print(f"  {label}: human {h_res} -> horse {q_res} at {q_pos}")


if __name__ == "__main__":
    main()
