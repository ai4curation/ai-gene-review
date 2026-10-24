# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython==1.85"]
# ///
"""Reproduce domain alignments and transfer verified reference active-site coordinates."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from Bio import SeqIO

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--target',type=Path,required=True)
p.add_argument('--references',type=Path,nargs='+',required=True)
p.add_argument('--output',type=Path,required=True)
a=p.parse_args();a.output.mkdir(exist_ok=True,parents=True)
docs=[json.loads(a.target.read_text())]+[json.loads(x.read_text()) for x in a.references]
domains=[]
for d in docs:
 seq=d['sequence']['value'];ac=d['primaryAccession']
 for f in d['features']:
  if f['type']=='Domain' and f['description'].startswith('Peptidase S1'):
   start,end=f['location']['start']['value'],f['location']['end']['value']
   # For the selected short target include every remaining residue, even beyond the domain call.
   if d is docs[0]:end=len(seq)
   domains.append({'id':f'{ac}_{start}_{end}','accession':ac,'start':start,'end':end,'sequence':seq[start-1:end],'active_sites':[x['location']['start']['value'] for x in d['features'] if x['type']=='Active site' and start<=x['location']['start']['value']<=end]})
(a.output/'domains.json').write_text(json.dumps(domains,indent=2)+'\n')
fa=a.output/'domains.fasta';fa.write_text(''.join('>'+d['id']+'\n'+d['sequence']+'\n' for d in domains))
results={'mafft_version':subprocess.run(['mafft','--version'],capture_output=True,text=True,check=True).stderr.strip(),'records':[{'accession':d['primaryAccession'],'length':len(d['sequence']['value']),'sha256':hashlib.sha256(d['sequence']['value'].encode()).hexdigest()} for d in docs],'modes':{}}
for mode in ['localpair','globalpair']:
 alnpath=a.output/f'{mode}-aligned.fasta'
 with alnpath.open('w') as out,(a.output/f'{mode}-mafft.txt').open('w') as err:
  subprocess.run(['mafft','--'+mode,'--maxiterate','1000',str(fa)],stdout=out,stderr=err,check=True)
 aln={r.id:str(r.seq) for r in SeqIO.parse(alnpath,'fasta')};positions={}
 for d in domains:
  idx=d['start']-1;m={}
  for col,aa in enumerate(aln[d['id']]):
   if aa!='-':idx+=1;m[col]=idx
  assert ''.join(aln[d['id']].split('-'))==d['sequence']
  positions[d['id']]=m
 mapped=[]
 for d in domains:
  for site in d['active_sites']:
   col=next(col for col,pos in positions[d['id']].items() if pos==site)
   mapped.append({'reference':d['id'],'reference_position':site,'reference_residue':aln[d['id']][col],'column_1based':col+1,'mapping':{k:{'position':positions[k].get(col),'residue':aln[k][col]} for k in aln}})
 results['modes'][mode]={'alignment':alnpath.name,'active_site_mapping':mapped}
# Full sequence prefix identity is independent of the alignment algorithms.
tseq=docs[0]['sequence']['value'];results['target_comparisons']=[]
for d in docs[1:]:
 s=d['sequence']['value'];prefix=0
 for x,y in zip(tseq,s):
  if x!=y:break
  prefix+=1
 results['target_comparisons'].append({'accession':d['primaryAccession'],'identical_prefix_length':prefix,'target_remaining_length':len(tseq)-prefix,'reference_remaining_length':len(s)-prefix})
(a.output/'results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
