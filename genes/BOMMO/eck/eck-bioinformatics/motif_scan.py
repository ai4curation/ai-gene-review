"""Locate the Brenner phosphotransferase motif (HxDhxxxN) and the
APH/CHK-type catalytic-loop context in BmEc22K (UniProt Q0PCR8).

Reads the sequence from the local UniProt flat file; no hardcoded results.
Run: python3 motif_scan.py
"""
import re
from pathlib import Path

UNIPROT = Path(__file__).resolve().parent.parent / "eck-uniprot.txt"


def read_sequence(path: Path) -> str:
    """Return the sequence from a UniProt flat file.

    >>> s = read_sequence(UNIPROT)
    >>> len(s) > 0
    True
    """
    lines = path.read_text().splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("SQ "))
    seq_lines = []
    for line in lines[start + 1 :]:
        if line.startswith("//"):
            break
        seq_lines.append(line)
    return re.sub(r"[^A-Z]", "", "".join(seq_lines))


def main() -> None:
    seq = read_sequence(UNIPROT)
    print(f"length: {len(seq)}")
    # Brenner's motif for phosphotransferases: H-x-D-[hydrophobic]-x-x-x-N
    for m in re.finditer(r"(?=(H.D[ILMVFYAC]...N))", seq):
        s = m.start()
        print(f"Brenner motif HxDhxxxN: {m.group(1)} at {s + 1}-{s + 8} "
              f"(H{s + 1}, D{s + 3}, N{s + 8})")
    # Looser form, as sometimes reported (HxDxxxxN)
    for m in re.finditer(r"(?=(H.D....N))", seq):
        s = m.start()
        print(f"Loose HxDxxxxN: {m.group(1)} at {s + 1}-{s + 8}")
    # D-[FY]-G-like magnesium-binding motif candidates downstream (DxxD / DFG / DY/DW)
    for m in re.finditer(r"(?=(VV?D[YFW]))", seq):
        s = m.start()
        print(f"candidate Mg-binding D in {m.group(1)} near {s + 1}")


if __name__ == "__main__":
    main()
