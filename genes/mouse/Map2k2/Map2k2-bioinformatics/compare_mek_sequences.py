"""Compare mouse Map2k2 (Q63932) with human MAP2K2 (P36507) and human MAP2K1 (Q02750).

Reads sequences from the repository's cached UniProt flat files, computes global
pairwise identity (Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5),
and reports residues at mouse positions of catalytic / regulatory features
annotated in Q63932 (ATP-binding K101, catalytic D194, activation-loop S222/S226)
plus the C-terminal tail.

Run from the repository root:
    uv run python genes/mouse/Map2k2/Map2k2-bioinformatics/compare_mek_sequences.py
"""
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
FILES = {
    "mouse_Map2k2_Q63932": ROOT / "genes/mouse/Map2k2/Map2k2-uniprot.txt",
    "human_MAP2K2_P36507": ROOT / "genes/human/MAP2K2/MAP2K2-uniprot.txt",
    "human_MAP2K1_Q02750": ROOT / "genes/human/MAP2K1/MAP2K1-uniprot.txt",
}
MOUSE_SITES = {101: "ATP-binding Lys", 194: "catalytic Asp (proton acceptor)",
               222: "activation-loop Ser (by RAF)", 226: "activation-loop Ser (by RAF)"}


def read_seq(path: Path) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, ln in enumerate(lines) if ln.startswith("SQ   "))
    seq = []
    for ln in lines[start + 1:]:
        if ln.startswith("//"):
            break
        seq.append(ln.replace(" ", ""))
    return "".join(seq)


def make_aligner() -> Align.PairwiseAligner:
    al = Align.PairwiseAligner()
    al.mode = "global"
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    return al


def mapping(aln) -> dict[int, int]:
    """Map 1-based positions in seq A to 1-based positions in seq B."""
    m = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for k in range(a1 - a0):
            m[a0 + k + 1] = b0 + k + 1
    return m


def main() -> None:
    seqs = {k: read_seq(v) for k, v in FILES.items()}
    for k, s in seqs.items():
        print(f"{k}\tlength={len(s)}")
    al = make_aligner()
    mouse = seqs["mouse_Map2k2_Q63932"]
    for other in ("human_MAP2K2_P36507", "human_MAP2K1_Q02750"):
        aln = al.align(mouse, seqs[other])[0]
        m = mapping(aln)
        ident = sum(1 for a, b in m.items() if mouse[a - 1] == seqs[other][b - 1])
        print(f"\nmouse_Map2k2 vs {other}: aligned_pairs={len(m)} identical={ident} "
              f"identity_over_aligned={ident / len(m):.4f} identity_over_mouse_length={ident / len(mouse):.4f}")
        for pos, desc in MOUSE_SITES.items():
            op = m.get(pos)
            ores = seqs[other][op - 1] if op else "-"
            print(f"  mouse {mouse[pos - 1]}{pos} ({desc}) -> {other} {ores}{op if op else ''}")
        print(f"  C-terminal 10 aa: mouse={mouse[-10:]} {other}={seqs[other][-10:]}")


if __name__ == "__main__":
    main()
