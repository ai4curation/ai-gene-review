"""Compare translated GenBank constructs with supplied UniProt flat files exactly."""
import argparse
import csv
from pathlib import Path
from Bio import SeqIO

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--genbank", type=Path, required=True)
parser.add_argument("--uniprot", type=Path, nargs="+", required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
constructs = []
for record in SeqIO.parse(args.genbank, "genbank"):
    for feature in record.features:
        if feature.type == "CDS" and "translation" in feature.qualifiers:
            constructs.append((record.id, feature.qualifiers["translation"][0],
                               "; ".join(feature.qualifiers.get("note", []))))
if not constructs:
    raise ValueError("No translated CDS records found")
with args.output.open("w") as handle:
    writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
    writer.writerow(["accession", "length", "exact_construct_matches", "construct_notes"])
    for path in args.uniprot:
        record = SeqIO.read(path, "swiss")
        matches = [(identifier, note) for identifier, seq, note in constructs
                   if seq == str(record.seq)]
        writer.writerow([record.id, len(record.seq),
                         ";".join(x[0] for x in matches),
                         ";".join(x[1] for x in matches)])
