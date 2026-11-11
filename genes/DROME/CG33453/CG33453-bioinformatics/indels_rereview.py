"""Locate the indels distinguishing two isoform sequences (re-review analysis).

Reads two UniProt JSON records, aligns them globally (BLOSUM62, open -10,
extend -0.5) and reports each gap block with its position in both sequences,
plus the UniProt SignalP-predicted signal peptide of each record, so that one can
see whether a length difference falls within the signal peptide or the mature chain.

Usage: python indels_rereview.py TARGET.json REFERENCE.json OUT.json
"""

import json
import sys
from pathlib import Path

from Bio.Align import PairwiseAligner, substitution_matrices


def signal_peptide(record: dict) -> list:
    return [
        [f["location"]["start"]["value"], f["location"]["end"]["value"]]
        for f in record.get("features", [])
        if f["type"] == "Signal"
    ]


def gap_blocks(aligned_ref: str, aligned_tgt: str) -> list:
    """Return gap blocks as dicts; positions are 1-based residue numbers.

    >>> gap_blocks("ABCD", "A--D")
    [{'missing_in': 'target', 'residues': 'BC', 'reference_start': 2, 'target_after': 1}]
    """
    blocks = []
    ri = ti = 0
    current = None
    for a, b in zip(aligned_ref, aligned_tgt):
        if a != "-":
            ri += 1
        if b != "-":
            ti += 1
        if b == "-" or a == "-":
            kind = "target" if b == "-" else "reference"
            res = a if b == "-" else b
            if current and current["missing_in"] == kind:
                current["residues"] += res
            else:
                current = {"missing_in": kind, "residues": res}
                if kind == "target":
                    current.update(reference_start=ri, target_after=ti)
                else:
                    current.update(target_start=ti, reference_after=ri)
                blocks.append(current)
        else:
            current = None
    return blocks


def main() -> None:
    tgt = json.loads(Path(sys.argv[1]).read_text())
    ref = json.loads(Path(sys.argv[2]).read_text())
    s, q = tgt["sequence"]["value"], ref["sequence"]["value"]
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(q, s)[0]
    aligned_ref, aligned_tgt = aln[0], aln[1]
    out = {
        "target": tgt["primaryAccession"],
        "reference": ref["primaryAccession"],
        "target_length": len(s),
        "reference_length": len(q),
        "target_signal_peptide": signal_peptide(tgt),
        "reference_signal_peptide": signal_peptide(ref),
        "gap_blocks": gap_blocks(aligned_ref, aligned_tgt),
        "mismatches_in_aligned_columns": sum(
            1 for a, b in zip(aligned_ref, aligned_tgt) if a != "-" and b != "-" and a != b
        ),
    }
    Path(sys.argv[3]).write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
