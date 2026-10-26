# /// script
# requires-python = ">=3.12"
# dependencies = ["biopython==1.85"]
# ///
"""Globally align two supplied UniProt flat-file sequences and record provenance."""

import argparse
import hashlib
import json
from pathlib import Path

from Bio import Align, SeqIO

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("first", type=Path)
parser.add_argument("second", type=Path)
parser.add_argument("output", type=Path)
args = parser.parse_args()
records = [SeqIO.read(p, "swiss") for p in (args.first, args.second)]
aligner = Align.PairwiseAligner(
    mode="global",
    match_score=2,
    mismatch_score=-1,
    open_gap_score=-10,
    extend_gap_score=-0.5,
)
alignment = aligner.align(records[0].seq, records[1].seq)[0]
counts = alignment.counts()
result = {
    "inputs": [
        {
            "path": str(p),
            "accession": r.id,
            "length": len(r.seq),
            "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
        }
        for p, r in zip((args.first, args.second), records)
    ],
    "method": "global PairwiseAligner; match 2, mismatch -1, gap open -10, extend -0.5",
    "alignment_columns": alignment.shape[1],
    "identities": counts.identities,
    "mismatches": counts.mismatches,
    "gaps": counts.gaps,
    "identity_fraction": counts.identities / alignment.shape[1],
    "alignment": str(alignment),
}
args.output.write_text(json.dumps(result, indent=2) + "\n")
