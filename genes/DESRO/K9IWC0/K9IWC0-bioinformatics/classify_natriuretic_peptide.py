#!/usr/bin/env python3
"""Decide which natriuretic peptide paralogue K9IWC0 (Desmodus rotundus) is.

UniProt/ARBA names K9IWC0 "Natriuretic peptides B" (BNP/NPPB), but the PANTHER
subfamily assignment in the same record is PTHR12167:SF2 "C-TYPE NATRIURETIC
PEPTIDE". This script settles the question from sequence alone by aligning the
K9IWC0 precursor against the three human natriuretic peptide precursors
(NPPA/ANP, NPPB/BNP, NPPC/CNP) and reporting global percent identity plus the
17-residue disulfide ring that defines the mature hormone.

Nothing is hardcoded: all four sequences are fetched from the UniProt REST API
and the alignment is computed at run time. Run with:

    uv run python classify_natriuretic_peptide.py
"""

from __future__ import annotations

import json
import sys
import urllib.request

from Bio import Align

UNIPROT_FASTA = "https://rest.uniprot.org/uniprotkb/{acc}.fasta"

QUERY = ("K9IWC0", "Desmodus rotundus natriuretic peptide (query)")
HUMAN_PARALOGUES = [
    ("P01160", "human NPPA / ANP"),
    ("P16860", "human NPPB / BNP"),
    ("P23582", "human NPPC / CNP"),
]


def fetch(acc: str) -> str:
    """Return the bare amino-acid sequence for a UniProt accession."""
    with urllib.request.urlopen(UNIPROT_FASTA.format(acc=acc), timeout=60) as fh:
        lines = fh.read().decode().splitlines()
    return "".join(line.strip() for line in lines if not line.startswith(">"))


def ring(seq: str) -> str | None:
    """Return the C-terminal cysteine ring (Cys..Cys inclusive), if present.

    In every natriuretic peptide the mature hormone is closed by a 17-residue
    disulfide loop between the last two cysteines of the precursor.
    """
    positions = [i for i, aa in enumerate(seq) if aa == "C"]
    if len(positions) < 2:
        return None
    return seq[positions[-2] : positions[-1] + 1]


def percent_identity(a: str, b: str) -> float:
    aligner = Align.PairwiseAligner(scoring="blastp", mode="global")
    aln = aligner.align(a, b)[0]
    matches = sum(
        x == y
        for x, y in zip(aln[0], aln[1])
        if x != "-" and y != "-"
    )
    return 100.0 * matches / min(len(a), len(b))


def main() -> int:
    query_seq = fetch(QUERY[0])
    query_ring = ring(query_seq)

    results = []
    for acc, label in HUMAN_PARALOGUES:
        seq = fetch(acc)
        results.append(
            {
                "accession": acc,
                "label": label,
                "length": len(seq),
                "percent_identity_to_query": round(percent_identity(query_seq, seq), 1),
                "c_terminal_ring": ring(seq),
                "residues_after_ring": len(seq) - seq.rfind("C") - 1,
            }
        )

    report = {
        "query": {
            "accession": QUERY[0],
            "description": QUERY[1],
            "length": len(query_seq),
            "c_terminal_ring": query_ring,
            "residues_after_ring": len(query_seq) - query_seq.rfind("C") - 1,
        },
        "human_paralogues": results,
        "best_match": max(results, key=lambda r: r["percent_identity_to_query"])["label"],
    }

    json.dump(report, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
