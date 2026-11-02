"""Locate plant Q-type zinc-finger and EAR-like motifs in ZFP7 (Q39266).

Reads the sequence from the cached UniProt flat file; standard library only.
Run: python3 motifs.py
"""
import re
from pathlib import Path

UNIPROT = Path(__file__).resolve().parent.parent / "ZFP7-uniprot.txt"

MOTIFS = {
    "QALGGH (plant Q-type C2H2 finger)": r"QALGGH",
    "C2H2 zinc ligand spacing C-x2-C-x3-F-x5-L-x2-H-x3-H": r"C..C...F.....L..H...H",
    "LxLxL (EAR-like)": r"(?=(L.L.L))",
    "DLNxxP (EAR)": r"(?=(DLN..P))",
}


def read_sequence(path: Path) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("SQ "))
    seq = []
    for line in lines[start + 1:]:
        if line.startswith("//"):
            break
        seq.append(line.replace(" ", ""))
    return "".join(seq)


def main() -> None:
    seq = read_sequence(UNIPROT)
    print(f"length\t{len(seq)}")
    for name, pattern in MOTIFS.items():
        hits = [(m.start() + 1, m.group(1) if m.groups() else m.group(0)) for m in re.finditer(pattern, seq)]
        if not hits:
            print(f"{name}\tnone")
        for pos, s in hits:
            print(f"{name}\t{pos}-{pos + len(s) - 1}\t{s}")


if __name__ == "__main__":
    main()
