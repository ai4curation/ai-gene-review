"""Re-review sequence scan for SCO2678 (Q9L243).

Parses the cached UniProt flat file, reports candidate HAD-superfamily motif
residues by regex, and a Kyte-Doolittle hydropathy scan of the N-terminus
(signal-peptide check). Usage: uv run --no-project python motif_scan_rereview.py
"""
import re
from pathlib import Path

HERE = Path(__file__).parent
UNIPROT = HERE.parent / "Q9L243-uniprot.txt"

KD = dict(A=1.8, R=-4.5, N=-3.5, D=-3.5, C=2.5, Q=-3.5, E=-3.5, G=-0.4, H=-3.2, I=4.5,
          L=3.8, K=-3.9, M=1.9, F=2.8, P=-1.6, S=-0.8, T=-0.7, W=-0.9, Y=-1.3, V=4.2)


def read_seq(path: Path) -> str:
    lines = path.read_text().splitlines()
    i = next(n for n, line in enumerate(lines) if line.startswith("SQ"))
    seq = []
    for line in lines[i + 1:]:
        if line.startswith("//"):
            break
        seq.append(line.replace(" ", ""))
    return "".join(seq)


def main() -> None:
    seq = read_seq(UNIPROT)
    print(f"length={len(seq)}")
    motifs = {
        "motif I (hhDxD)": r"[ILVMF]{2,}D.D",
        "motif II (hhhh[ST])": r"[ILVMFWA]{3}[ST]",
        "motif III (K)": r"K",
        "motif IV (hhhDD / hhhGD)": r"[ILVMFW]{2,}[ILVMFW]?[DG]D",
    }
    for name, pat in motifs.items():
        hits = [(m.start() + 1, m.group()) for m in re.finditer(pat, seq)]
        print(name, hits)
    win = 15
    maxh = max((sum(KD[a] for a in seq[i:i + win]) / win, i + 1) for i in range(0, 40))
    print(f"max KD hydropathy over residues 1-55 (window {win}): {maxh[0]:.2f} at start {maxh[1]}")
    print("(signal-peptide h-regions typically give window means > ~1.6)")
    print("N-terminal 30 aa:", seq[:30])


if __name__ == "__main__":
    main()
