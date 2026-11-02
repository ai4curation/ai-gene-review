"""Scan CG6830 (Q9VGJ8) for the APH/CHK-type Brenner catalytic-loop motif HxDxxxxN.

Reads the sequence from ../CG6830-uniprot.txt and reports each motif hit and the
SMART CHK domain it falls in. Run: python motif_scan_rereview.py
"""
import re
from pathlib import Path

DOMAINS = {"CHK domain 1": (174, 369), "CHK domain 2": (605, 797)}


def read_sequence(path: Path) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("SQ"))
    seq_lines = []
    for line in lines[start + 1 :]:
        if line.startswith("//"):
            break
        seq_lines.append(line.replace(" ", ""))
    return "".join(seq_lines)


def main() -> None:
    seq = read_sequence(Path(__file__).parent.parent / "CG6830-uniprot.txt")
    print(f"length={len(seq)}")
    for m in re.finditer(r"(?=(H.D....N))", seq):
        pos = m.start() + 1
        dom = [n for n, (a, b) in DOMAINS.items() if a <= pos <= b]
        print(f"HxDxxxxN at {pos}-{pos + 7}: {m.group(1)} in {dom or 'no CHK domain'}")


if __name__ == "__main__":
    main()
