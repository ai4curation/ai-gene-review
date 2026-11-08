"""Map published promoter segments to an annotated genome, without functional inference.

Uses Biopython 1.85. Coordinates in JSON are one-based inclusive.
"""

import argparse
import hashlib
import json
from pathlib import Path

from Bio import SeqIO, SwissProt
from Bio.Seq import Seq


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--genome", type=Path, required=True)
    parser.add_argument("--queries", type=Path, required=True)
    parser.add_argument("--uniprot", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    genome = SeqIO.read(args.genome, "embl")
    with args.uniprot.open() as handle:
        protein = SwissProt.read(handle)
    sequence = str(genome.seq).upper()
    results = []
    for query in json.loads(args.queries.read_text()):
        motif = query["sequence"].upper()
        if not motif or set(motif) - set("ACGT"):
            raise ValueError("Queries must contain unambiguous DNA")
        hits = []
        for strand, probe in [(1, motif), (-1, str(Seq(motif).reverse_complement()))]:
            offset = 0
            while (position := sequence.find(probe, offset)) >= 0:
                hits.append(
                    {
                        "start": position + 1,
                        "end": position + len(probe),
                        "strand": strand,
                    }
                )
                offset = position + 1
        features = [
            feature
            for feature in genome.features
            if feature.type == "CDS"
            and query["candidate_locus"] in feature.qualifiers.get("locus_tag", [])
        ]
        candidates = []
        for feature in features:
            start, end = int(feature.location.start) + 1, int(feature.location.end)
            strand = feature.location.strand
            candidates.append(
                {
                    "locus": feature.qualifiers["locus_tag"],
                    "protein_id": feature.qualifiers.get("protein_id"),
                    "start": start,
                    "end": end,
                    "strand": strand,
                    "translation_length": len(feature.qualifiers["translation"][0]),
                    "translation_equals_uniprot": feature.qualifiers["translation"][0]
                    == protein.sequence,
                    "upstream_distances": [
                        (
                            start - hit["end"] - 1
                            if strand == 1
                            else hit["start"] - end - 1
                        )
                        if strand == hit["strand"]
                        else None
                        for hit in hits
                    ],
                }
            )
        results.append({"query": query, "hits": hits, "candidate_cds": candidates})
    report = {
        "genome": genome.id,
        "genome_length": len(sequence),
        "uniprot_accessions": protein.accessions,
        "input_sha256": {
            str(path): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in [args.genome, args.queries, args.uniprot]
        },
        "results": results,
    }
    args.output.write_text(json.dumps(report, indent=2) + "\n")


if __name__ == "__main__":
    main()
