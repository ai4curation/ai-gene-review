"""Check conservation of MCM AAA+ catalytic motifs in C. elegans MCM-4 (Q95XQ8).

Reads the sequence and FT MOTIF coordinates from ../mcm-4-uniprot.txt and reports the
residues at the Walker A, Walker B and arginine-finger (SRF) positions. Run with:

    python3 motif_check_rereview.py
"""

import re
from pathlib import Path

UNIPROT = Path(__file__).resolve().parent.parent / "mcm-4-uniprot.txt"


def read_record(path: Path) -> tuple[str, dict[str, tuple[int, int]]]:
    text = path.read_text()
    seq_block = text.split("\nSQ ", 1)[1].split("\n", 1)[1]
    seq = "".join(seq_block.replace("//", "").split())
    motifs = {}
    for m in re.finditer(r"FT   MOTIF\s+(\d+)\.\.(\d+)\nFT\s+/note=\"([^\"]+)\"", text):
        motifs[m.group(3)] = (int(m.group(1)), int(m.group(2)))
    return seq, motifs


def main() -> None:
    seq, motifs = read_record(UNIPROT)
    print(f"sequence_length\t{len(seq)}")
    for name, (start, end) in motifs.items():
        print(f"{name}\t{start}-{end}\t{seq[start - 1:end]}")
    walker_a = seq[motifs["Walker A"][0] - 1 : motifs["Walker A"][1]]
    print(f"walker_a_matches_MCM_GxxGxxK[ST]\t{bool(re.fullmatch(r'G..G..K[ST]', walker_a))}")
    srf = [(m.start() + 1, seq[m.start():m.start() + 3]) for m in re.finditer("SRF", seq)]
    print(f"SRF_occurrences\t{srf}")


if __name__ == "__main__":
    main()
