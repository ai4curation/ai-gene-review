"""Map supplied reference coordinates through a global protein alignment.

Biological interpretations belong in RESULTS.md. Inputs, positions and output
paths are command-line arguments; the script contains no expected residues.
"""

import argparse
import hashlib
import json
from pathlib import Path

import Bio
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices


def read_protein(path, format):
    record = SeqIO.read(path, format)
    if not record.seq:
        raise ValueError(f"Empty sequence: {path}")
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference", type=Path, required=True)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--reference-format", default="fasta")
    parser.add_argument("--target-format", default="fasta")
    parser.add_argument("--positions", nargs="+", type=int, required=True)
    parser.add_argument("--matrix", default="BLOSUM62")
    parser.add_argument("--open-gap", type=float, default=-10.0)
    parser.add_argument("--extend-gap", type=float, default=-0.5)
    parser.add_argument("--flank", type=int, default=5)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--alignment", type=Path, required=True)
    args = parser.parse_args()
    reference = read_protein(args.reference, args.reference_format)
    target = read_protein(args.target, args.target_format)
    if args.flank < 0 or any(p < 1 or p > len(reference) for p in args.positions):
        parser.error("Positions must be within the reference and flank nonnegative")

    aligner = PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load(args.matrix)
    aligner.open_gap_score = args.open_gap
    aligner.extend_gap_score = args.extend_gap
    alignments = aligner.align(reference.seq, target.seq)
    alignment = alignments[0]
    mapping = {}
    for ref_span, target_span in zip(*alignment.aligned):
        for r, t in zip(range(*ref_span), range(*target_span)):
            mapping[r + 1] = t + 1

    rows = []
    for position in args.positions:
        target_position = mapping.get(position)
        row = {
            "reference_position": position,
            "reference_residue": str(reference.seq[position - 1]),
            "target_position": target_position,
            "target_residue": str(target.seq[target_position - 1]) if target_position else None,
            "reference_window": str(reference.seq[max(0, position - 1 - args.flank):position + args.flank]),
            "target_window": str(target.seq[max(0, target_position - 1 - args.flank):target_position + args.flank]) if target_position else None,
        }
        rows.append(row)

    def source(path, record):
        return {
            "path": str(path),
            "record_id": record.id,
            "description": record.description,
            "length": len(record),
            "file_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "sequence_sha256": hashlib.sha256(str(record.seq).encode()).hexdigest(),
        }

    result = {
        "biopython_version": Bio.__version__,
        "reference": source(args.reference, reference),
        "target": source(args.target, target),
        "parameters": {
            "mode": aligner.mode,
            "substitution_matrix": args.matrix,
            "open_gap_score": args.open_gap,
            "extend_gap_score": args.extend_gap,
            "flank": args.flank,
            "optimal_alignment_selection": "first alignment returned by Biopython",
        },
        "alignment_score": alignment.score,
        "positions": rows,
    }
    for path in [args.output, args.alignment]:
        path.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    args.alignment.write_text(str(alignment) + "\n")
    print("reference_position\treference_residue\ttarget_position\ttarget_residue")
    for row in rows:
        print("\t".join(str(row[k]) for k in ["reference_position", "reference_residue", "target_position", "target_residue"]))


if __name__ == "__main__":
    main()
