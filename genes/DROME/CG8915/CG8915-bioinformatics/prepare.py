"""Extract exact sequences from supplied UniProt JSON and Swiss-Prot records."""
import argparse,json
from pathlib import Path
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
p=argparse.ArgumentParser();p.add_argument('--json',nargs='*',default=[]);p.add_argument('--swiss',nargs='*',default=[]);p.add_argument('--output',required=True);a=p.parse_args()
rs=[]
for file in a.json:
 raw=json.loads(Path(file).read_text());rs.append(SeqRecord(Seq(raw['sequence']['value']),id=raw['primaryAccession'],description='source='+file))
for file in a.swiss:
 r=SeqIO.read(file,'swiss');r.id=r.annotations['accessions'][0];r.description='source='+file;rs.append(r)
assert rs and len({r.id for r in rs})==len(rs)
SeqIO.write(rs,a.output,'fasta')
