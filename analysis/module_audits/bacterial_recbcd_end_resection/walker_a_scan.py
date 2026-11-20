#!/usr/bin/env python3
"""Scan UniProt flat files for the Walker A (P-loop) ATP-binding motif.

Usage: python walker_a_scan.py FILE [FILE ...]

For each UniProt flat file, extract the SQ sequence and report every match to
the canonical Walker A consensus [AG]-x(4)-G-K-[ST] (PROSITE PS00017-like).
Also reports matches of a relaxed pattern G-x(4)-GK (without the S/T) so that
degenerate motifs are visible. No results are hard-coded; an empty list means
no match in that sequence.
"""
import re
import sys

STRICT = re.compile(r"(?=([AG].{4}GK[ST]))")
RELAXED = re.compile(r"(?=(G.{4}GK))")


def read_entry(path):
    acc, seq, in_sq = None, [], False
    with open(path) as fh:
        for line in fh:
            if line.startswith("AC   ") and acc is None:
                acc = line[5:].split(";")[0].strip()
            elif line.startswith("SQ   "):
                in_sq = True
            elif line.startswith("//"):
                break
            elif in_sq:
                seq.append("".join(line.split()))
    return acc, "".join(seq).upper()


def main(paths):
    for path in paths:
        acc, seq = read_entry(path)
        strict = [(m.start() + 1, m.group(1)) for m in STRICT.finditer(seq)]
        relaxed = [(m.start() + 1, m.group(1)) for m in RELAXED.finditer(seq)]
        print(f"{acc}\tlength={len(seq)}\tstrict_[AG]x4GK[ST]={strict}\trelaxed_Gx4GK={relaxed}\t{path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
