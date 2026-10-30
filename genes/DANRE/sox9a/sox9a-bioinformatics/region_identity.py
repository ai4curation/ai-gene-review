"""Region-wise identity of zebrafish Sox9a, Sox9b and human SOX9.

Reads sequences and HMG-box coordinates from the cached UniProt flat files
(genes/DANRE/sox9a, genes/DANRE/sox9b, genes/human/SOX9), aligns each pair
globally (BLOSUM62, gap -10/-0.5, same settings as
projects/DANRE_DUPLICATION/scripts/compare_pair.py) and reports percent
identity over: the whole protein, the HMG box (coordinates of the first
sequence), the N-terminal region before the HMG box, and the C-terminal region
after it. Also reports the C-terminal end of each protein. Nothing is
hard-coded except file paths.

Run from the repository root:
    uv run python genes/DANRE/sox9a/sox9a-bioinformatics/region_identity.py
"""
import re
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]
FILES = {
    "sox9a": ROOT / "genes/DANRE/sox9a/sox9a-uniprot.txt",
    "sox9b": ROOT / "genes/DANRE/sox9b/sox9b-uniprot.txt",
    "SOX9": ROOT / "genes/human/SOX9/SOX9-uniprot.txt",
}


def parse(path):
    text = path.read_text()
    seq = "".join(re.search(r"^SQ.*?\n(.*?)^//", text, re.S | re.M).group(1).split())
    m = re.search(r"^FT   (?:DOMAIN|DNA_BIND)\s+(\d+)\.\.(\d+)\s*\nFT\s+/note=\"HMG box\"", text, re.M)
    hmg = (int(m.group(1)), int(m.group(2))) if m else None
    return seq, hmg


def align(a, b):
    al = Align.PairwiseAligner(mode="global")
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    return al.align(a, b)[0]


def region_identity(aln, a_len, start, end):
    """Identity over alignment columns whose seqA position lies in [start,end] (1-based)."""
    ident = cols = 0
    sa, sb = aln[0], aln[1]
    pos = 0
    for ca, cb in zip(sa, sb):
        if ca != "-":
            pos += 1
            inside = start <= pos <= end
        else:
            inside = start <= pos + 1 <= end and pos >= start
        if inside:
            cols += 1
            if ca == cb and ca != "-":
                ident += 1
    return 100.0 * ident / cols if cols else float("nan"), cols


def main():
    data = {k: parse(v) for k, v in FILES.items()}
    for k, (s, h) in data.items():
        print(f"{k}: length {len(s)}, HMG box {h}, C-terminal 10 aa {s[-10:]}")
    print()
    pairs = [("sox9a", "sox9b"), ("sox9a", "SOX9"), ("sox9b", "SOX9")]
    print("| Pair | Whole protein | N-term (before HMG) | HMG box | C-term (after HMG) |")
    print("|---|---|---|---|---|")
    for a, b in pairs:
        sa, ha = data[a]
        sb, _ = data[b]
        aln = align(sa, sb)
        whole = region_identity(aln, len(sa), 1, len(sa))
        nterm = region_identity(aln, len(sa), 1, ha[0] - 1)
        hmg = region_identity(aln, len(sa), ha[0], ha[1])
        cterm = region_identity(aln, len(sa), ha[1] + 1, len(sa))
        fmt = lambda x: f"{x[0]:.1f}% ({x[1]} cols)"
        print(f"| {a} vs {b} | {fmt(whole)} | {fmt(nterm)} | {fmt(hmg)} | {fmt(cterm)} |")


if __name__ == "__main__":
    main()
