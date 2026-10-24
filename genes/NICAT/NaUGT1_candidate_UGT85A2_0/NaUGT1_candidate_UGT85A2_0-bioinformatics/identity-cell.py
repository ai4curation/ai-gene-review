# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython==1.85", "openpyxl==3.1.5"]
# ///
"""Compare supplemental primers with a GenBank CDS and infer primer-compatible starts.

All sequence/primer inputs are external; no biological results are hardcoded.
A reconstructed ORF retains the deposited splice junctions, changing only its
start to a consistent cloning-primer start. This is not a deposited construct.
"""
import argparse, hashlib, json
from pathlib import Path
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import CompoundLocation, FeatureLocation
import openpyxl

p=argparse.ArgumentParser()
p.add_argument('--supplement',type=Path,required=True)
p.add_argument('--genomic',type=Path,required=True)
p.add_argument('--target',type=Path,required=True)
p.add_argument('--uniprot',type=Path,required=True)
p.add_argument('--model-protein',required=True)
p.add_argument('--primer-label',required=True)
p.add_argument('--minimum-match',type=int,default=18)
p.add_argument('--output',type=Path,required=True)
a=p.parse_args()
reference=SeqIO.read(a.genomic,'genbank')
model=next(f for f in reference.features if f.type=='CDS' and a.model_protein in f.qualifiers.get('protein_id',[]))
short=SeqIO.read(a.target,'genbank')
short_cds=next(f for f in short.features if f.type=='CDS')
up=SeqIO.read(a.uniprot,'swiss')
sequence=str(reference.seq).upper()
model_dna=model.extract(reference.seq)
protein=str(model_dna.translate()).rstrip('*')
short_protein=str(short_cds.extract(short.seq).translate()).rstrip('*')

def matches(s):
 out=[]
 for strand,q in [(1,s),(-1,str(Seq(s).reverse_complement()))]:
  at=sequence.find(q)
  while at>=0:
   out.append({'strand':strand,'start_1based':at+1,'end_1based':at+len(q)})
   at=sequence.find(q,at+1)
 return out

rows=[];starts=set()
for row_number,values in enumerate(openpyxl.load_workbook(a.supplement,data_only=True).active.values,1):
 if values[0]!=a.primer_label:continue
 primer=str(values[1]).upper();entry={'table_row':row_number,'label':values[0],'primer':primer,'purpose':values[2]}
 for k in range(len(primer)-a.minimum_match+1):
  suffix=primer[k:];hits=matches(suffix)
  if hits:
   entry.update(longest_3prime_match=suffix,matches=hits)
   for hit in hits:
    if values[2] in ['Pathway Elucidation','Protein Expression','SLC','BiFC','Y2H'] and suffix.startswith('ATG') and hit['strand']==model.location.strand:
     start=hit['end_1based'] if hit['strand']==-1 else hit['start_1based']
     oldstart=int(model.location.parts[0].end) if hit['strand']==-1 else int(model.location.parts[0].start)+1
     if (hit['strand']==-1 and start>=oldstart) or (hit['strand']==1 and start<=oldstart):starts.add(start)
   break
 if 'matches' not in entry:entry['matches']=[]
 rows.append(entry)
inferred=[]
for start in sorted(starts):
 parts=list(model.location.parts);first=parts[0]
 if model.location.strand==-1:parts[0]=FeatureLocation(int(first.start),start,strand=-1)
 else:parts[0]=FeatureLocation(start-1,int(first.end),strand=1)
 loc=CompoundLocation(parts) if len(parts)>1 else parts[0]
 dna=loc.extract(reference.seq);pep=str(dna.translate()).rstrip('*')
 inferred.append({'genomic_start_1based':start,'location_0based':str(loc),'cds_length':len(dna),'protein_length':len(pep),'internal_stops':pep.count('*'),'target_exact_offset_0based':pep.find(str(up.seq)),'ends_with_complete_target':pep.endswith(str(up.seq)),'sequence':pep,'n_terminal_extension':pep[:-len(up)] if pep.endswith(str(up.seq)) else None})
result={'inputs':{str(x):{'sha256':hashlib.sha256(x.read_bytes()).hexdigest()} for x in [a.supplement,a.genomic,a.target,a.uniprot]},'genomic_accession':reference.id,'model_protein':a.model_protein,'model_location_0based':str(model.location),'model_gene':model.qualifiers.get('gene'),'model_locus':model.qualifiers.get('locus_tag'),'uniprot':up.id,'short_genomic_accession':short.id,'short_genomic_protein':short_cds.qualifiers.get('protein_id'),'model_length':len(protein),'target_length':len(up),'model_equals_target':protein==str(up.seq),'short_genomic_protein_equals_target':short_protein==str(up.seq),'primer_label':a.primer_label,'primer_count':len(rows),'primers_with_genomic_3prime_match':sum(bool(x['matches']) for x in rows),'primers':rows,'primer_compatible_orfs':inferred}
a.output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['inputs','primers','primer_compatible_orfs']},indent=2))
