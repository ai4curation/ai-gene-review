#!/usr/bin/env python3
"""Pairwise identity of GATA DNA-binding domains (DBDs) across yeast GATA factors.

Approach (no hardcoded results):
1. Re-detect the GATA Cys4 zinc finger in each input sequence (same regex as
   find_gata_zinc_finger.py) and extract a DBD window = the zinc finger plus a
   fixed flank on each side (default 8 aa), clamped to sequence ends.
2. Align the extracted DBD windows with MAFFT.
3. Compute all pairwise percent identities over aligned columns where BOTH
   sequences have a residue (ignoring gap-gap and gap-residue columns).

Outputs a TSV identity matrix and the DBD FASTA + alignment.

Usage:
    python pairwise_dbd_identity.py <input.fasta> --outdir results [--flank 8]
"""

from __future__ import annotations

import argparse
import itertools
import re
import subprocess
import sys
from pathlib import Path

from Bio import SeqIO

GATA_ZF = re.compile(r"C.{2}C.{17,20}C.{2}C")


def extract_dbd(seq: str, flank: int) -> tuple[int, int, str] | None:
    """Return (start_1based, end_1based, dbd_seq) for the first GATA ZF window."""
    m = GATA_ZF.search(seq)
    if not m:
        return None
    start = max(0, m.start() - flank)
    end = min(len(seq), m.end() + flank)
    return start + 1, end, seq[start:end]


def pct_identity(a: str, b: str) -> tuple[float, int]:
    """Percent identity over columns where both have a (non-gap) residue."""
    assert len(a) == len(b), "aligned sequences must be equal length"
    ident = 0
    compared = 0
    for x, y in zip(a, b):
        if x == "-" or y == "-":
            continue
        compared += 1
        if x == y:
            ident += 1
    if compared == 0:
        return 0.0, 0
    return 100.0 * ident / compared, compared


def short_name(header: str) -> str:
    # sp|P40209|GAT2_YEAST -> GAT2
    parts = header.split("|")
    if len(parts) >= 3:
        return parts[2].split("_")[0]
    return header


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("fasta", type=Path)
    ap.add_argument("--outdir", type=Path, required=True)
    ap.add_argument("--flank", type=int, default=8)
    args = ap.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)

    dbd_records = []  # (name, dbd_seq)
    for rec in SeqIO.parse(str(args.fasta), "fasta"):
        seq = str(rec.seq)
        res = extract_dbd(seq, args.flank)
        name = short_name(rec.id)
        if res is None:
            print(f"WARNING: no GATA ZF found in {rec.id}; skipping", file=sys.stderr)
            continue
        start, end, dbd = res
        dbd_records.append((name, dbd))
        print(f"{name}: DBD window {start}-{end} (len {len(dbd)})")

    if len(dbd_records) < 2:
        print("ERROR: need >=2 DBDs to compare", file=sys.stderr)
        return 1

    dbd_fasta = args.outdir / "gata_dbd_windows.fasta"
    dbd_fasta.write_text(
        "".join(f">{n}\n{s}\n" for n, s in dbd_records)
    )

    # Align with MAFFT
    aln_path = args.outdir / "gata_dbd_alignment.fasta"
    proc = subprocess.run(
        ["mafft", "--auto", "--quiet", str(dbd_fasta)],
        capture_output=True, text=True, check=True,
    )
    aln_path.write_text(proc.stdout)

    aln = {short_name(r.id): str(r.seq) for r in SeqIO.parse(str(aln_path), "fasta")}
    names = list(aln.keys())

    # Pairwise identity matrix
    matrix = {n: {m: (100.0 if n == m else None) for m in names} for n in names}
    print("\nPairwise DBD % identity (aligned, gap columns excluded):")
    for a, b in itertools.combinations(names, 2):
        pid, ncol = pct_identity(aln[a], aln[b])
        matrix[a][b] = pid
        matrix[b][a] = pid
        print(f"  {a:6s} vs {b:6s}: {pid:5.1f}%  (over {ncol} columns)")

    # Write TSV
    tsv = args.outdir / "gata_dbd_identity_matrix.tsv"
    with tsv.open("w") as fh:
        fh.write("\t" + "\t".join(names) + "\n")
        for n in names:
            row = [f"{matrix[n][m]:.1f}" if matrix[n][m] is not None else "NA" for m in names]
            fh.write(n + "\t" + "\t".join(row) + "\n")
    print(f"\nWrote: {tsv}")
    print(f"Wrote: {aln_path}")

    # Report GAT2's ranked neighbors
    if "GAT2" in matrix:
        others = [(m, matrix["GAT2"][m]) for m in names if m != "GAT2"]
        others.sort(key=lambda x: x[1], reverse=True)
        print("\nGAT2 DBD identity ranking (closest first):")
        for m, v in others:
            print(f"  {m:6s}: {v:5.1f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
