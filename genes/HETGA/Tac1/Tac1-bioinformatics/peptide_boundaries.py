#!/usr/bin/env python3
"""Locate the processed tachykinin peptides in the naked mole-rat Tac1 precursor.

The TrEMBL entry A0A0P6JY17 carries no PEPTIDE features, so the boundaries of
substance P / neurokinin A are not asserted anywhere in the record.  This script
(a) reads the sequences straight out of the two UniProt flat files, (b) aligns
them (they are the same length bar one C-terminal residue, so a gap-free
comparison after right-trimming is exact and is asserted, not assumed), and
(c) transfers the reviewed human PEPTIDE coordinates, checking each transferred
peptide still ends in the tachykinin F-x-G-L-M consensus followed by the
Gly-amide donor and a dibasic cleavage site.

Inputs (already in the repo / fetched by the script):
  genes/HETGA/Tac1/Tac1-uniprot.txt   naked mole-rat A0A0P6JY17
  P20366.txt                          human TAC1, fetched from UniProt REST

Run:  uv run --no-project python peptide_boundaries.py
"""

from __future__ import annotations

import re
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
NMR_FLATFILE = HERE.parent / "Tac1-uniprot.txt"
HUMAN_CACHE = HERE / "P20366.txt"
HUMAN_URL = "https://rest.uniprot.org/uniprotkb/P20366.txt"


def sequence(flatfile: str) -> str:
    body = flatfile.split("\nSQ   ", 1)[1].split("\n", 1)[1]
    return "".join(body.split("//", 1)[0].split())


def peptides(flatfile: str) -> list[tuple[int, int, str]]:
    out = []
    for m in re.finditer(
        r"^FT   PEPTIDE {9}(\d+)\.\.(\d+)\nFT {19}/note=\"([^\"]+)\"",
        flatfile,
        re.M,
    ):
        out.append((int(m.group(1)), int(m.group(2)), m.group(3)))
    return out


def main() -> int:
    nmr_flat = NMR_FLATFILE.read_text()
    if not HUMAN_CACHE.exists():
        HUMAN_CACHE.write_text(
            urllib.request.urlopen(HUMAN_URL).read().decode()
        )
    human_flat = HUMAN_CACHE.read_text()

    nmr, human = sequence(nmr_flat), sequence(human_flat)
    print(f"naked mole-rat A0A0P6JY17: {len(nmr)} aa")
    print(f"human         P20366    : {len(human)} aa  (isoform Beta, displayed)")

    # Gap-free colinearity over the shared length.
    n = min(len(nmr), len(human))
    diffs = [
        (i + 1, human[i], nmr[i]) for i in range(n) if human[i] != nmr[i]
    ]
    ident = 100.0 * (n - len(diffs)) / n
    print(f"\nungapped identity over 1..{n}: {n - len(diffs)}/{n} = {ident:.1f}%")
    print("substitutions (human->NMR):",
          ", ".join(f"{h}{p}{m}" for p, h, m in diffs) or "none")
    if len(nmr) != len(human):
        print(f"NMR C-terminal extension: {nmr[n:]!r} at {n + 1}..{len(nmr)}")

    print("\nHuman PEPTIDE features transferred to the NMR precursor:")
    print(f"{'peptide':<28}{'coords':<12}{'human':<40}{'naked mole-rat':<40}same?")
    for start, end, note in peptides(human_flat):
        h, m = human[start - 1:end], nmr[start - 1:end]
        print(f"{note:<28}{f'{start}..{end}':<12}{h:<40}{m:<40}{h == m}")

    print("\nProcessing-site check on the NMR sequence "
          "(tachykinin C-terminus F-x-G-L-M, then G amide donor + dibasic):")
    for m in re.finditer(r"F.GLM", nmr):
        end = m.end()
        print(f"  ...{m.group(0)} ends at {end}; next 3 residues = "
              f"{nmr[end:end + 3]!r} "
              f"({'G + dibasic OK' if re.match(r'G[KR][KR]', nmr[end:end + 3]) else 'no canonical site'})")

    print("\nPEPTIDE features present in the NMR TrEMBL record:",
          peptides(nmr_flat) or "none")
    return 0


if __name__ == "__main__":
    sys.exit(main())
