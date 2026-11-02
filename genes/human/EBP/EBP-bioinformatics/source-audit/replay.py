#!/usr/bin/env python3
"""Recompute EBP source joins from bundled exact saved inputs; Python 3.9+ stdlib."""
import argparse,base64,csv,hashlib,io,json,re,tarfile
from pathlib import Path

def digest(b):return hashlib.sha256(b).hexdigest()
def replay(root):
 manifest=json.loads((root/'source-manifest.json').read_text())
 archive=root/'inputs.tar.gz';assert digest(archive.read_bytes())==manifest['archive_sha256']
 data={}
 with tarfile.open(archive,'r:gz')as tar:
  assert {m.name for m in tar.getmembers()}=={x['name']for x in manifest['inputs']}
  for item in manifest['inputs']:
   member=tar.getmember(item['name']);assert member.isfile()
   b=tar.extractfile(member).read();assert len(b)==item['bytes']and digest(b)==item['sha256']
   data[item['name']]=b
 J=lambda name:json.loads(data[name])
 sources=J('source-objects.json');raw=list(csv.reader(io.StringIO(data['intact-Q15125.tsv'].decode()),delimiter='\t'))
 selected=[(i+1,r)for i,r in enumerate(raw)if any('pubmed:'+p in r[8]for p in ['25910212','32296183'])]
 joins=[]
 for i,a in enumerate(sources):
  if a['original_reference_id']not in ['PMID:25910212','PMID:32296183']:continue
  partners=[p.split(':',1)[1]for p in a.get('supporting_entities',[])if p.startswith('UniProtKB:')]
  rows=[]
  for line,r in selected:
   ids=[x.split(':',1)[1]for x in r[:2]]
   if 'pubmed:'+a['original_reference_id'][5:]not in r[8]:continue
   match=(ids==['Q15125','Q15125'])if a['term']['id']=='GO:0042802'else all(p in ids for p in partners)
   if match:rows.append(line)
  assert rows
  joins.append({'review_index':i,'source_reference':a['original_reference_id'],'source_partners':partners,'physical_lines_1based':rows,'actual_partners':sorted({x.split(':',1)[1]for line,r in selected if line in rows for x in r[:2]if x!='uniprotkb:Q15125'})})
 official={name.removeprefix('UniProt-').removesuffix('.json'):J(name)for name in data if name.startswith('UniProt-')and name.endswith('.json')}
 sequences={k:v['sequence']['value']for k,v in official.items()if isinstance(v,dict)and 'sequence'in v}
 for acc,record in official.items():
  primary_sequence=record['sequence']['value'];features={f['featureId']:f for f in record.get('features',[])if f['type']=='Alternative sequence'}
  for comment in record.get('comments',[]):
   if comment['commentType']!='ALTERNATIVE PRODUCTS':continue
   for iso in comment['isoforms']:
    if iso['isoformSequenceStatus']not in ['Displayed','Described']:continue
    if any(v not in features for v in iso.get('sequenceIds',[])):continue
    sequence=primary_sequence;edits=[]
    for vid in iso.get('sequenceIds',[]):
     f=features[vid];a=f['location']['start']['value'];b=f['location']['end']['value'];change=f.get('alternativeSequence',{})
     if change.get('originalSequence'):assert sequence[a-1:b]==change['originalSequence']
     edits.append((a,b,change.get('alternativeSequences',[''])[0]))
    for a,b,replacement in sorted(edits,reverse=True):sequence=sequence[:a-1]+replacement+sequence[b:]
    for aid in iso['isoformIds']:sequences[aid]=sequence
 old=data['P08195-unisave253.txt'].decode();primary=''.join(re.findall('[A-Z]+',old.split('\nSQ   ',1)[1].split('\n',1)[1].split('//')[0]))
 block=re.search(r'FT   VAR_SEQ\s+98\n(.*?)(?=\nFT   \S)',old,re.S).group(1)
 note=' '.join(line.removeprefix('FT').strip()for line in block.splitlines())
 original,replacement=re.search(r'/note="([A-Z]+) -> ([A-Z]+) \(in isoform\s+4\)',note).groups()
 assert primary[97]==original
 historical=primary[:97]+replacement+primary[98:];sequences['P08195-4']=historical
 sequence_checks=[]
 for line,r in selected:
  for side in [0,1]:
   acc=r[side].split(':',1)[1];seq=sequences.get(acc);tax=re.search(r'taxid:(\d+)',r[9+side]).group(1)
   rogid=('rogid:'+base64.b64encode(hashlib.sha1(seq.encode()).digest()).decode().rstrip('=')+tax)if seq else None
   sequence_checks.append({'physical_line_1based':line,'side':'A'if side==0 else'B','accession':acc,'sequence_length':len(seq)if seq else None,'calculated_rogid':rogid,'record_rogid':r[32+side],'matches':rogid==r[32+side]if seq else None,'features':r[36+side],'method':r[6],'sequence_source':'archived UniSave253 reconstruction'if acc=='P08195-4'else'current official record'if seq else'unresolved IntAct-only clone'})
 nodes={};paths={}
 def visit(n,path):
  k=n['persistent_id'];nodes[k]=n;paths[k]=path+[k];children=n.get('children',{}).get('annotation_node',[])
  for c in([children]if isinstance(children,dict)else children):visit(c,paths[k])
 visit(J('PTHR14207-tree.json')['search']['tree_topology']['annotation_node'],[])
 target=[k for k,n in nodes.items()if n.get('node_name','').endswith('UniProtKB=Q15125')];assert len(target)==1;target=target[0]
 msa=J('PTHR14207-msa.json')['search']['MSA_list']['sequence_info'];aligned={x['persistent_id']:re.sub('[^A-Za-z]','',x['sequence']).upper()for x in msa}
 assert aligned[target]==sequences['Q15125']
 gaf=[]
 for line in data['PTHR14207-assertions.gaf'].decode().splitlines():
  if line.startswith('!'):continue
  f=line.split('\t');assert f[1]in nodes;gaf.append({'fields':f,'node_on_target_path':f[1]in paths[target]})
 entity=J('Reactome-195697-retry.json');cat=J('Reactome-195674.json')
 assert entity['referenceEntity']['identifier']=='Q15125'
 reactions=[]
 for rid in ['R-HSA-195690','R-HSA-6807052']:
  r=J('Reactome-'+rid+'.json');assert any(x['dbId']==195674 for x in r['catalystActivity'])
  reactions.append({k:r.get(k)for k in ['stId','displayName','input','output','crossReference','compartment']})
 terms=[]
 for name in sorted(data):
  if re.fullmatch(r'GO\d{7}\.json',name):
   for t in J(name).get('results',[]):terms.append({k:t.get(k)for k in ['id','name','definition','comment','aspect','isObsolete','children']})
 return {'all_intact_records':len(raw),'selected_intact_records':len(selected),'annotation_joins':joins,'selected_records':[{'physical_line_1based':n,'fields':r}for n,r in selected],'sequence_checks':sequence_checks,'sequence_summary':{'exact':sum(x['matches']is True for x in sequence_checks),'mismatch':sum(x['matches']is False for x in sequence_checks),'unresolved':sum(x['matches']is None for x in sequence_checks)},'historical_SLC3A2':{'entry_version':253,'canonical_length':len(primary),'product_length':len(historical),'assayed_133_661_equals_current_P08195_2':historical[132:661]==sequences['P08195-2']},'paint':{'tree_nodes':len(nodes),'msa_sequences':len(aligned),'target_node':target,'target_path':paths[target],'target_length':len(sequences['Q15125']),'family_assertions':gaf},'reactome':{'reactions':reactions,'catalyst':cat,'entity':{k:entity.get(k)for k in ['stId','displayName','speciesName','compartment','startCoordinate','endCoordinate','referenceEntity']}},'terms':terms}

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--inputs',type=Path,default=Path(__file__).resolve().parent);p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true');a=p.parse_args()
 result=replay(a.inputs)
 if a.check:assert result==json.loads((a.inputs/'results.json').read_text()),'Saved results differ from recomputed raw inputs'
 if a.output:a.output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'status':'PASS','all_records':result['all_intact_records'],'selected_records':result['selected_intact_records'],'source_joins':len(result['annotation_joins']),'sequence_summary':result['sequence_summary'],'paint_nodes':result['paint']['tree_nodes'],'target_length':result['paint']['target_length'],'check':a.check}))
if __name__=='__main__':main()
