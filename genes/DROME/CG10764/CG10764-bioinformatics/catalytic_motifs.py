"""Scan the CG10764 (A1ZAT2) sequence for S1A catalytic-triad and S1-pocket motifs.

Reads the sequence from ../CG10764-uniprot.txt and reports, for each of the two
PROSITE PS50240 Peptidase S1 domain ranges in the record, whether the His (TAAHC-like),
Asp and Ser (GDSGGP) motifs are present, plus the residue at chymotrypsin position 189
(six residues before the catalytic Ser), which predicts P1 specificity.

Run: python catalytic_motifs.py
"""

import re
from pathlib import Path

HERE = Path(__file__).parent
UNIPROT = HERE.parent / "CG10764-uniprot.txt"


def read_sequence(path: Path) -> str:
    """Return the SQ block of a UniProt flat file as one string."""
    lines = path.read_text().splitlines()
    start = next(i for i, ln in enumerate(lines) if ln.startswith("SQ "))
    seq = []
    for ln in lines[start + 1 :]:
        if ln.startswith("//"):
            break
        seq.append(ln.replace(" ", ""))
    return "".join(seq)


def read_domains(path: Path) -> list[tuple[int, int]]:
    """Return (start, end) of every FT DOMAIN line."""
    out = []
    for ln in path.read_text().splitlines():
        m = re.match(r"FT\s+DOMAIN\s+(\d+)\.\.(\d+)", ln)
        if m:
            out.append((int(m.group(1)), int(m.group(2))))
    return out


def scan(seq: str, start: int, end: int) -> dict:
    """Report triad motif hits (1-based positions) within a domain."""
    sub = seq[start - 1 : end]
    res: dict = {"range": f"{start}-{end}"}
    his = re.search(r"[ST]A[AG]HC", sub)
    res["His_motif"] = (
        f"{his.group()} H{start + his.start() + 3}" if his else "absent"
    )
    ser = re.search(r"G[DE]SGG[PS]", sub)
    if ser:
        s_pos = start + ser.start() + 2
        res["Ser_motif"] = f"{ser.group()} S{s_pos}"
        res["pos189_equiv"] = f"{seq[s_pos - 1 - 6]}{s_pos - 6}"
    else:
        res["Ser_motif"] = "absent"
        res["pos189_equiv"] = "n/a"
    asp = re.search(r"[NR]D[IVL][AGSM][LIV][LIV]", sub)
    res["Asp_motif"] = (
        f"{asp.group()} D{start + asp.start() + 1}" if asp else "absent"
    )
    return res


def main() -> None:
    seq = read_sequence(UNIPROT)
    print(f"length={len(seq)}")
    for s, e in read_domains(UNIPROT):
        print(scan(seq, s, e))


if __name__ == "__main__":
    main()
