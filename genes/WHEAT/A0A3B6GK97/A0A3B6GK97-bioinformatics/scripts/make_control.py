#!/usr/bin/env python3
"""Build a control FASTA to confirm the pipeline is input-driven (not hardcoded).

Takes the fetched sequences, DROPS the real query, and relabels an active,
experimentally-grounded reference (potato patatin P15478) as the QUERY. Running
analyze.py on this control should recover intact catalytic motifs (GTSTG + DGGG)
and a pPLAII/patatin placement — demonstrating the real query's 'motifs absent'
result is a property of that sequence, not a pipeline artifact.

Usage: uv run python scripts/make_control.py
"""
from __future__ import annotations

from pathlib import Path

SRC = Path("data/sequences.fasta")
DST = Path("data/test_control.fasta")
CONTROL_LABEL_PREFIX = "St_patatin_T5"  # active, structurally characterized patatin


def main() -> int:
    out = []
    for rec in SRC.read_text().split(">"):
        if not rec.strip():
            continue
        header, _, body = rec.partition("\n")
        if header.startswith("QUERY"):
            continue  # drop the real query
        if header.startswith(CONTROL_LABEL_PREFIX):
            acc = header.split("|", 1)[1].split()[0]
            header = f"QUERY_CONTROL_patatin|{acc} (relabelled {CONTROL_LABEL_PREFIX})"
        out.append(">" + header + "\n" + body.rstrip("\n"))
    DST.write_text("\n".join(out) + "\n")
    print(f"Wrote control FASTA -> {DST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
