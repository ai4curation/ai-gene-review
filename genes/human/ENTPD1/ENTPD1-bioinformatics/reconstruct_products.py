"""Apply UniProt alternative-sequence records and compare with independent FASTA.

No biological verdicts or gene-specific coordinates. Features are coordinate
projections only; preserved sequence does not establish preserved function.
Python standard library only. Inputs/outputs supplied by CLI.
"""
import argparse,hashlib,json
from pathlib import Path

def require(v,m):
 if not v:raise ValueError(m)

def fasta_records(text):
 out={};key=None
 for line in text.splitlines():
  if line.startswith('>'):
   h=line[1:].split()[0];key=h.split('|')[1] if '|' in h else h
   require(key not in out,'Duplicate FASTA identifier');out[key]=''
  elif line.strip():require(key is not None,'Sequence before FASTA identifier');out[key]+=line.strip()
 return out

def reconstruct(record,fasta):
 seq=record['sequence']['value'];acc=record['primaryAccession'];require(len(seq)==record['sequence']['length'],'Displayed sequence length')
 require(fasta.get(acc)==seq,'Displayed sequence FASTA mismatch')
 variants={f['featureId']:f for f in record.get('features',[]) if f['type']=='Alternative sequence'}
 products=[i for c in record.get('comments',[]) if c['commentType']=='ALTERNATIVE PRODUCTS' for i in c['isoforms']]
 if not products:products=[{'name':{'value':'Displayed'},'isoformIds':[acc],'isoformSequenceStatus':'Displayed'}]
 results=[]
 for prod in products:
  edits=[]
  for v in prod.get('sequenceIds',[]):
   require(v in variants,'Missing variant '+v);f=variants[v];start=f['location']['start'];end=f['location']['end'];require(start['modifier']==end['modifier']=='EXACT','Uncertain variant coordinates')
   a,b=start['value'],end['value'];require(1<=a<=b<=len(seq),'Variant range')
   alt=f.get('alternativeSequence',{});original=alt.get('originalSequence');require(original is None or seq[a-1:b]==original,'Variant preimage mismatch')
   reps=alt.get('alternativeSequences',[]);require(len(reps)<=1,'Ambiguous alternatives');replacement=reps[0] if reps else ''
   edits.append({'id':v,'start':a,'end':b,'replacement':replacement,'source_segment':seq[a-1:b]})
  edits.sort(key=lambda e:e['start']);require(all(a['end']<b['start'] for a,b in zip(edits,edits[1:])),'Overlapping alternatives')
  chars=[];origins=[];cursor=1
  for e in edits:
   chars.extend(seq[cursor-1:e['start']-1]);origins.extend(range(cursor,e['start']))
   chars.extend(e['replacement']);origins.extend([None]*len(e['replacement']));cursor=e['end']+1
  chars.extend(seq[cursor-1:]);origins.extend(range(cursor,len(seq)+1));reconstructed=''.join(chars)
  identifier=prod['isoformIds'][0];fid=acc if prod['isoformSequenceStatus']=='Displayed' else identifier
  require(fid in fasta,'Missing FASTA '+fid);exact_match=reconstructed==fasta[fid];require(exact_match,'Reconstruction mismatch '+fid)
  mapping={old:new for new,old in enumerate(origins,1) if old is not None};features=[]
  for f in record.get('features',[]):
   if f['type'] not in {'Transmembrane','Active site','Binding site','Lipidation'}:continue
   a=f['location']['start']['value'];b=f['location']['end']['value'];positions=[mapping[x] for x in range(a,b+1) if x in mapping]
   features.append({'type':f['type'],'description':f.get('description',''),'canonical_start':a,'canonical_end':b,'original_segment':seq[a-1:b],'unchanged_residue_count':len(positions),'feature_length':b-a+1,'projected_unchanged_positions':positions,'source_evidences':f.get('evidences',[])})
  results.append({'id':identifier,'name':prod['name']['value'],'fasta_identifier':fid,'length':len(reconstructed),'sha256':hashlib.sha256(reconstructed.encode()).hexdigest(),'edits':edits,'sequence':reconstructed,'exact_independent_fasta_match':exact_match,'canonical_feature_projections':features})
 require(set(fasta)=={r['fasta_identifier'] for r in results},'Unexpected FASTA identifiers')
 return {'accession':acc,'taxon':record['organism']['taxonId'],'products':results}

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--uniprot',type=Path,required=True);p.add_argument('--fasta',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 result=reconstruct(json.loads(a.uniprot.read_text()),fasta_records(a.fasta.read_text()));a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'accession':result['accession'],'products':[(r['id'],r['length']) for r in result['products']],'all_exact':all(r['exact_independent_fasta_match'] for r in result['products'])}))
