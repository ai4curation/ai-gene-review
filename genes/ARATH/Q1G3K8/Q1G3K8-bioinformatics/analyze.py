"""Compare supplied sequences and map the longest exact 3-prime primer suffix.

No mismatches or gaps are allowed. Forward primers match the supplied strand;
reverse primers match by reverse complement. All positions are 1-based inclusive.
The input tables, not this code, specify genes, primer sequences, and comparisons.
"""

import argparse
import csv
import json
from pathlib import Path

from Bio import SeqIO
from Bio.Seq import Seq


def primer_hits(sequence: str, primer: str, direction: str, minimum: int) -> list[dict]:
    if direction not in {"forward", "reverse"}:
        raise ValueError(f"Invalid direction: {direction}")
    for trim in range(len(primer) - minimum + 1):
        query = primer[trim:]
        if direction == "reverse":
            query = str(Seq(query).reverse_complement())
        positions = []
        start = sequence.find(query)
        while start >= 0:
            positions.append({"start": start + 1, "end": start + len(query),
                              "matched_bases": len(query), "five_prime_trim": trim})
            start = sequence.find(query, start + 1)
        if positions:
            return positions
    return []


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sequences", type=Path, required=True)
    parser.add_argument("--primers", type=Path, required=True)
    parser.add_argument("--comparisons", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--minimum", type=int, default=14)
    args = parser.parse_args()
    if args.minimum < 1:
        parser.error("--minimum must be positive")
    sequences = {k: str(v.seq).upper() for k, v in SeqIO.to_dict(
        SeqIO.parse(args.sequences, "fasta")).items()}
    primer_results = []
    with args.primers.open() as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            primer = row["sequence"].upper()
            if set(primer) - set("ACGT"):
                raise ValueError(f"Non-ACGT primer: {row['primer']}")
            for target in row["targets"].split(","):
                sequence = sequences[target]
                if set(sequence) - set("ACGT"):
                    raise ValueError(f"Non-ACGT target: {target}")
                primer_results.append({"primer": row["primer"], "target": target,
                                       "direction": row["direction"],
                                       "hits": primer_hits(sequence, primer, row["direction"], args.minimum)})
    comparisons = []
    with args.comparisons.open() as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            left, right = sequences[row["left"]], sequences[row["right"]]
            comparisons.append({**row, "left_length": len(left), "right_length": len(right),
                                "identical": left == right})
    args.output.write_text(json.dumps({"minimum_exact_three_prime_match": args.minimum,
                                      "comparisons": comparisons, "primer_matches": primer_results}, indent=2) + "\n")


if __name__ == "__main__":
    main()
