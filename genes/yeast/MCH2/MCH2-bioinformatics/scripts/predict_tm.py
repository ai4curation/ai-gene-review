#!/usr/bin/env python3
"""Predict transmembrane (TM) helices from a hydropathy profile.

Uses the Kyte-Doolittle hydropathy scale with a sliding window and a
peak-calling heuristic to estimate the number of TM segments. This is a
lightweight, reproducible approximation (NOT a substitute for TMHMM/Phobius/
DeepTMHMM); it is used to independently corroborate the UniProt-annotated
topology, and its limitations are documented in RESULTS.md.

Runs on ANY FASTA (no hardcoded sequence). Outputs a per-protein TSV with the
predicted TM count and the segment boundaries.

Usage:
    python predict_tm.py --fasta data/panel.fasta --out results/tm_predictions.tsv \
        --window 19 --threshold 1.6
"""
import argparse
from pathlib import Path

# Kyte & Doolittle (1982) hydropathy values
KD = {
    "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5,
    "Q": -3.5, "E": -3.5, "G": -0.4, "H": -3.2, "I": 4.5,
    "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8, "P": -1.6,
    "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2,
}


def read_fasta(path: Path) -> list[tuple[str, str]]:
    records = []
    name = None
    seq_parts: list[str] = []
    for line in path.read_text().splitlines():
        if line.startswith(">"):
            if name is not None:
                records.append((name, "".join(seq_parts)))
            name = line[1:].strip()
            seq_parts = []
        else:
            seq_parts.append(line.strip())
    if name is not None:
        records.append((name, "".join(seq_parts)))
    return records


def hydropathy_profile(seq: str, window: int) -> list[float]:
    """Return the windowed mean hydropathy centered at each residue."""
    half = window // 2
    n = len(seq)
    profile = []
    for i in range(n):
        lo = max(0, i - half)
        hi = min(n, i + half + 1)
        vals = [KD.get(seq[j], 0.0) for j in range(lo, hi)]
        profile.append(sum(vals) / len(vals))
    return profile


def call_tm_segments(
    profile: list[float], threshold: float, min_len: int, merge_gap: int
) -> list[tuple[int, int]]:
    """Call contiguous runs above threshold as TM candidates.

    Segments shorter than min_len are dropped; segments separated by <= merge_gap
    residues are merged (handles brief dips within a single helix window).
    """
    raw = []
    start = None
    for i, v in enumerate(profile):
        if v >= threshold and start is None:
            start = i
        elif v < threshold and start is not None:
            raw.append((start, i - 1))
            start = None
    if start is not None:
        raw.append((start, len(profile) - 1))

    # merge close segments
    merged: list[list[int]] = []
    for s, e in raw:
        if merged and s - merged[-1][1] - 1 <= merge_gap:
            merged[-1][1] = e
        else:
            merged.append([s, e])

    return [(s, e) for s, e in merged if (e - s + 1) >= min_len]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fasta", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--window", type=int, default=19)
    ap.add_argument("--threshold", type=float, default=1.6)
    ap.add_argument("--min-len", type=int, default=15)
    ap.add_argument("--merge-gap", type=int, default=3)
    args = ap.parse_args()

    records = read_fasta(args.fasta)
    args.out.parent.mkdir(parents=True, exist_ok=True)

    with args.out.open("w") as fh:
        fh.write("protein\tlength\tn_tm_predicted\tsegments\n")
        for name, seq in records:
            prof = hydropathy_profile(seq, args.window)
            segs = call_tm_segments(prof, args.threshold, args.min_len, args.merge_gap)
            seg_str = ";".join(f"{s + 1}-{e + 1}" for s, e in segs)
            fh.write(f"{name}\t{len(seq)}\t{len(segs)}\t{seg_str}\n")
            print(f"{name}: {len(segs)} TM segments")
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
