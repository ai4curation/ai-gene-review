#!/usr/bin/env python3
"""Compute pairwise percent identity from a multiple sequence alignment.

Percent identity is computed over aligned columns where BOTH sequences have a
residue (i.e. gaps in either sequence are excluded from the denominator).
Produces a full matrix TSV and, for a focal accession, a ranked list of its
closest relatives.

Runs on any aligned FASTA. Usage:
    python pairwise_identity.py --aln results/panel_aln.fasta \
        --focal P36032 --matrix results/identity_matrix.tsv \
        --ranked results/mch2_closest.tsv
"""
import argparse
from itertools import combinations
from pathlib import Path


def read_fasta(path: Path) -> list[tuple[str, str]]:
    records = []
    name = None
    parts: list[str] = []
    for line in path.read_text().splitlines():
        if line.startswith(">"):
            if name is not None:
                records.append((name, "".join(parts)))
            name = line[1:].strip()
            parts = []
        else:
            parts.append(line.strip())
    if name is not None:
        records.append((name, "".join(parts)))
    return records


def pct_identity(a: str, b: str) -> tuple[float, int]:
    """Return (percent identity, number of compared columns)."""
    same = 0
    compared = 0
    for ca, cb in zip(a, b):
        if ca == "-" or cb == "-":
            continue
        compared += 1
        if ca == cb:
            same += 1
    if compared == 0:
        return 0.0, 0
    return 100.0 * same / compared, compared


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--aln", required=True, type=Path)
    ap.add_argument("--focal", required=True)
    ap.add_argument("--matrix", required=True, type=Path)
    ap.add_argument("--ranked", required=True, type=Path)
    args = ap.parse_args()

    records = read_fasta(args.aln)
    names = [n for n, _ in records]
    seqs = dict(records)

    ident: dict[tuple[str, str], float] = {}
    for a, b in combinations(names, 2):
        pid, _ = pct_identity(seqs[a], seqs[b])
        ident[(a, b)] = pid
        ident[(b, a)] = pid
    for n in names:
        ident[(n, n)] = 100.0

    args.matrix.parent.mkdir(parents=True, exist_ok=True)
    with args.matrix.open("w") as fh:
        short = [n.split("|")[-1] for n in names]
        fh.write("protein\t" + "\t".join(short) + "\n")
        for i, ni in enumerate(names):
            row = [f"{ident[(ni, nj)]:.1f}" for nj in names]
            fh.write(short[i] + "\t" + "\t".join(row) + "\n")

    focal_full = None
    for n in names:
        if n.split("|")[0] == args.focal:
            focal_full = n
            break
    if focal_full is None:
        raise SystemExit(f"Focal {args.focal} not in alignment")

    ranked = sorted(
        [(n, ident[(focal_full, n)]) for n in names if n != focal_full],
        key=lambda x: x[1],
        reverse=True,
    )
    with args.ranked.open("w") as fh:
        fh.write("rank\tprotein\tpercent_identity_to_focal\n")
        for r, (n, pid) in enumerate(ranked, 1):
            fh.write(f"{r}\t{n.split('|')[-1]}\t{pid:.1f}\n")

    print(f"Focal: {focal_full.split('|')[-1]}")
    print("Closest relatives:")
    for n, pid in ranked[:6]:
        print(f"  {n.split('|')[-1]}: {pid:.1f}%")
    print(f"Wrote {args.matrix} and {args.ranked}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
