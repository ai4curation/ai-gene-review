#!/usr/bin/env python3
"""Locate the diagnostic catalytic/functional motifs of an m-AAA protease in the
C. elegans ppgn-1 (Y38F2AR.7, UniProt G5EDB6) sequence.

The point of this script is to test one specific, falsifiable question: does the
ppgn-1 protein sequence *itself* retain the residues required for (a) ATP
binding/hydrolysis by the AAA+ module and (b) zinc-dependent proteolysis by the
M41 peptidase module? A catalytically dead paralog (pseudo-protease/pseudo-ATPase)
would have lost one or more of these. Motif positions are reported, not asserted;
if a motif is absent the script says so.

Sequence is parsed directly from the sibling UniProt flat file so nothing is
hard-coded. Run:  uv run python analyze_motifs.py
"""
from __future__ import annotations

import re
from pathlib import Path

UNIPROT = Path(__file__).resolve().parent.parent / "ppgn-1-uniprot.txt"


def read_sequence(path: Path) -> str:
    """Extract the amino-acid sequence from a UniProt .txt (SQ ... //) record."""
    lines = path.read_text().splitlines()
    seq_chars: list[str] = []
    in_seq = False
    for line in lines:
        if line.startswith("SQ "):
            in_seq = True
            continue
        if in_seq:
            if line.startswith("//"):
                break
            seq_chars.append(line.replace(" ", "").strip())
    return "".join(seq_chars)


def find(pattern: str, seq: str) -> list[tuple[int, str]]:
    """Return 1-based start position and matched text for each regex hit."""
    return [(m.start() + 1, m.group(0)) for m in re.finditer(pattern, seq)]


def main() -> None:
    seq = read_sequence(UNIPROT)
    print("# ppgn-1 (G5EDB6) motif scan")
    print(f"length: {len(seq)} aa\n")

    # AAA+ ATPase Walker A / P-loop: G-x(4)-G-K-[S/T]
    walker_a = find(r"G.{4}GK[ST]", seq)
    # AAA+ Walker B: hydrophobic run then D-E (canonical hhhhDE core). The
    # hydrophobic class includes aromatics (Y/F/W) as is standard for Walker B.
    walker_b = find(r"[ILVFMYWAC]{3,4}DE", seq)
    # Second region of homology (SRH) arginine finger neighbourhood is family
    # specific; we only report Walker A/B here.
    # M41 / FtsH zinc metalloprotease active site: HExxH (two Zn-coordinating His
    # plus catalytic Glu). Also report the downstream third ligand context.
    hexxh = find(r"H E[A-Z][A-Z]H".replace(" ", ""), seq)

    def report(name: str, hits: list[tuple[int, str]]) -> None:
        if hits:
            for pos, txt in hits:
                print(f"{name}: FOUND at {pos} -> {txt}")
        else:
            print(f"{name}: NOT FOUND")

    report("Walker A (P-loop, ATP binding)", walker_a)
    report("Walker B (Mg-ATP hydrolysis)", walker_b)
    report("HExxH (M41 zinc-binding catalytic motif)", hexxh)

    # Context window around the HExxH for manual inspection of the third ligand.
    for pos, _ in hexxh:
        window = seq[pos - 1 : pos + 34]
        print(f"\nHExxH context [{pos}..{pos + len(window) - 1}]: {window}")


if __name__ == "__main__":
    main()
