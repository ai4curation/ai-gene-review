"""Extract one CDS translation from EMBL or one official UniProt JSON sequence."""
import argparse,json
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from pathlib import Path
ap=argparse.ArgumentParser()
ap.add_argument('input',type=Path)
ap.add_argument('format',choices=['embl','uniprot-json'])
ap.add_argument('output',type=Path)
a=ap.parse_args()
if a.format=='embl':
    r=SeqIO.read(a.input,'embl')
    cds=[f for f in r.features if f.type=='CDS' and 'translation' in f.qualifiers]
    assert len(cds)==1,'Ambiguous CDS selection'
    f=cds[0]
    record=SeqRecord(Seq(f.qualifiers['translation'][0]),id=f.qualifiers['protein_id'][0],
                     description=r.description+'; '+r.id)
else:
    r=json.loads(a.input.read_text())
    record=SeqRecord(Seq(r['sequence']['value']),id=r['primaryAccession'],
                     description=r['organism']['scientificName'])
a.output.parent.mkdir(parents=True,exist_ok=True)
SeqIO.write([record],a.output,'fasta')
