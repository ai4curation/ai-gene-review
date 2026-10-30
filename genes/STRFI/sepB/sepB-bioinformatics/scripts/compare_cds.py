# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython==1.85"]
# ///
"""Compare named annotated CDSs in any EMBL record with UniProt flat files."""
import argparse, csv, hashlib
from pathlib import Path
from Bio import SeqIO

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--embl', type=Path, required=True)
p.add_argument('--pair', action='append', required=True, help='CDS-gene=UniProt-flat-file')
p.add_argument('--output', type=Path, required=True)
a = p.parse_args()
record = SeqIO.read(a.embl, 'embl')
rows = []
for pair in a.pair:
    gene, path = pair.split('=', 1)
    matches = [f for f in record.features if f.type == 'CDS' and gene in f.qualifiers.get('gene', [])]
    if len(matches) != 1:
        raise ValueError(f'{gene}: expected one CDS, found {len(matches)}')
    f = matches[0]
    annotated = f.qualifiers['translation'][0]
    translated = str(f.extract(record.seq).translate(table=int(f.qualifiers.get('transl_table', ['11'])[0]), cds=True))
    protein = SeqIO.read(path, 'swiss')
    sequence = str(protein.seq)
    rows.append(dict(gene=gene, source_record=record.id, source_protein=f.qualifiers['protein_id'][0],
                     start_1based=int(f.location.start)+1, end_1based_inclusive=int(f.location.end),
                     strand=f.location.strand, accession=protein.annotations['accessions'][0],
                     source_length=len(annotated), uniprot_length=len(sequence),
                     genome_translation_matches_annotation=translated == annotated,
                     exact_sequence_match=sequence == annotated,
                     source_sha256=hashlib.sha256(annotated.encode()).hexdigest(),
                     uniprot_sha256=hashlib.sha256(sequence.encode()).hexdigest()))
a.output.parent.mkdir(parents=True, exist_ok=True)
with a.output.open('w') as out:
    writer = csv.DictWriter(out, fieldnames=list(rows[0]), delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
