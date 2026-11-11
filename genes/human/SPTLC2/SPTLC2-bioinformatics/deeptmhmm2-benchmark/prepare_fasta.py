"""Extract canonical sequences from supplied cached UniProt flat files."""
import argparse
from pathlib import Path
from Bio import SeqIO

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("output", type=Path)
parser.add_argument("inputs", nargs="+", type=Path)
args = parser.parse_args()
records = []
for path in args.inputs:
    record = SeqIO.read(path, "swiss")
    record.description = path.name
    records.append(record)
SeqIO.write(records, args.output, "fasta")
for record in records:
    print(record.id, len(record.seq))
