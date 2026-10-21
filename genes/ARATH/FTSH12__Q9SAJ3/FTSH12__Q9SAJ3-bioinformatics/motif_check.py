# /// script
# requires-python = ">=3.10"
# ///
"""Report AAA+ and M41 catalytic motifs in Q9SAJ3 (FTSH12) from the cached UniProt record.

Positions are 1-based UniProt coordinates. Run with:
    uv run --script motif_check.py
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
UNIPROT = HERE.parent / "FTSH12__Q9SAJ3-uniprot.txt"


def read_sequence(path: Path) -> str:
    text = path.read_text()
    seq_block = text.split("\nSQ   ", 1)[1].split("\n", 1)[1].split("//", 1)[0]
    return "".join(seq_block.split())


def main() -> None:
    seq = read_sequence(UNIPROT)
    print(f"length\t{len(seq)}")
    checks = {
        "Walker A (GxxxxGK[TS])": r"G....GK[TS]",
        "Walker B (hhhhDE)": r"[ILVMF]{4}DE",
        "M41 zinc motif (HExxH)": r"HE..H",
    }
    for name, pattern in checks.items():
        hits = [(m.start() + 1, m.group()) for m in re.finditer(pattern, seq)]
        print(f"{name}\t{hits}")
    for pos in (769, 770, 773, 849):
        print(f"residue {pos}\t{seq[pos - 1]}")


if __name__ == "__main__":
    main()
