"""Locate the S1-peptidase catalytic-triad motifs in CLIPA8 (A0A1S4H5S2).

Reads the sequence from the UniProt flat file in the gene folder and reports
the residues at the canonical His (TAAHC-like), Asp (D[IVL]AL[LI]) and Ser
(GDSGGP) motif positions. Run: uv run python catalytic_triad_check.py
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
UNIPROT = HERE.parent / "CLIPA8-uniprot.txt"


def read_sequence(path: Path) -> str:
    """Extract the SQ block sequence from a UniProt flat file."""
    lines = path.read_text().splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith("SQ "))
    seq = []
    for line in lines[start + 1 :]:
        if line.startswith("//"):
            break
        seq.append(line.replace(" ", ""))
    return "".join(seq)


def main() -> None:
    seq = read_sequence(UNIPROT)
    print(f"length {len(seq)}")
    motifs = {
        "His57 region (TAAH[CI])": r"[TS]AAH[CI]",
        "Asp102 region (ND[IV]AL)": r"ND[IV]AL",
        "Ser195 canonical (GDSGGP)": r"GDSGG",
        "Ser195 region, permissive (C.GD.G, canonical C.GDSGGP)": r"C.GD.G",
    }
    for name, pat in motifs.items():
        hits = [(m.start() + 1, m.group()) for m in re.finditer(pat, seq)]
        print(f"{name}: {hits if hits else 'no match'}")
        for pos, motif in hits:
            if "Ser195 region" in name:
                # position of the residue aligned to the catalytic Ser (third after the Cys..G)
                ser_pos = pos + 4
                print(f"  residue at catalytic-Ser position {ser_pos}: {seq[ser_pos - 1]}")


if __name__ == "__main__":
    main()
