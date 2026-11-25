#!/usr/bin/env python3
"""Recompute source-context/sequence joins from saved QuickGO, MITAB and UniProt bytes.
Python 3.9+, standard library only. No network or curation decisions.
"""
import argparse,base64,collections,hashlib,json,re
from pathlib import Path

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rogid(u):
 return 'rogid:'+base64.b64encode(hashlib.sha1(u['sequence']['value'].encode()).digest()).decode().rstrip('=')+str(u['organism']['taxonId'])
def identifier(s):return s.removeprefix('uniprotkb:')
def compute(root,target,all_incident):
 manifest=json.loads((root/'source-manifest.json').read_text())
 for p in manifest['sources']:assert sha(root/p['path'])==p['sha256'],p['path']
 identities={p.stem:json.loads(p.read_text()) for p in sorted((root/'inputs/identities').glob('*.json'))}
 raw=json.loads((root/'inputs/quickgo.json').read_text())
 assert len(raw['results'])==raw['numberOfHits'],'incomplete QuickGO response'
 contexts=[]
 if not all_incident:
  for i,s in enumerate(raw['results']):
   if s['geneProductId']!='UniProtKB:'+target or s['goEvidence']!='IPI':continue
   partners=[r['id'] for group in s['withFrom'] or [] for r in group['connectedXrefs'] if r['db']=='UniProtKB']
   for partner in partners:contexts.append({'quickgo_index':i,'annotation_id':s['id'],'reference':s['reference'],'partner':partner})
 keys={(x['reference'].replace('PMID:','pubmed:'),x['partner']) for x in contexts}
 all_records=[];selected=[]
 for n,line in enumerate((root/'inputs/intact.tsv').read_text().split('\n'),1):
  if not line or line.startswith('#'):continue
  f=line.split('\t');assert len(f)==42,(n,len(f))
  if 'uniprotkb:'+target not in f[:2]:continue
  t=f[:2].index('uniprotkb:'+target);p=1-t;partner=identifier(f[p]);refs=f[8].split('|')
  entry={'line_1based':n,'target_side':t,'partner':partner,'reference':f[8],'method':f[6],'target_role':f[18+t],'partner_role':f[18+p],'target_features':f[36+t],'partner_features':f[36+p],'host':f[28],'negative':f[35],'identifiers':f[13],'fields':f}
  entry['sequence_checks']={}
  for name,side,acc in [('target',t,target),('partner',p,partner)]:
   u=identities.get(acc)
   entry['sequence_checks'][name]={'accession':acc,'record_checksum':f[32+side],'sequence_length':len(u['sequence']['value']) if u else None,'calculated_checksum':rogid(u) if u else None,'match':rogid(u)==f[32+side] if u else None}
  all_records.append(entry)
  if all_incident or any((ref,partner) in keys for ref in refs):selected.append(entry)
 for c in contexts:
  c['matched_lines_1based']=[x['line_1based'] for x in selected if c['partner']==x['partner'] and c['reference'].replace('PMID:','pubmed:') in x['reference'].split('|')]
  assert c['matched_lines_1based'],c
 by_ref={}
 for ref in sorted({ref for x in selected for ref in x['reference'].split('|') if ref.startswith('pubmed:')}):
  rows=[x for x in selected if ref in x['reference'].split('|')]
  by_ref[ref]={'records':len(rows),'partners':sorted({x['partner'] for x in rows}),'validated_two_hybrid':sum('MI:1356' in x['method'] for x in rows)}
 summary={'target':target,'mode':'all_incident' if all_incident else 'complete_IPI_contexts','quickgo_total':len(raw['results']),'IPI_contexts':len(contexts),'incident_records':len(all_records),'selected_records':len(selected),'partners':len({x['partner'] for x in selected}),'negative_records':sum(x['negative']=='true' for x in selected),'sequence_checks':dict(collections.Counter(str(s['match']) for x in selected for s in x['sequence_checks'].values())),'by_publication':by_ref}
 return {'summary.json':summary,'contexts.json':contexts,'records.json':selected}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent);ap.add_argument('--target',required=True);ap.add_argument('--all-incident',action='store_true');ap.add_argument('--output',type=Path,required=True);ap.add_argument('--check',action='store_true');a=ap.parse_args()
 out=a.output if a.output.is_absolute() else a.root/a.output
 computed=compute(a.root,a.target,a.all_incident)
 if not a.check:out.mkdir(parents=True,exist_ok=True)
 for name,data in computed.items():
  content=json.dumps(data,indent=2,ensure_ascii=False)+'\n'
  if a.check:assert (out/name).read_text()==content,name
  else:(out/name).write_text(content)
 print(json.dumps({'result':'PASS','check':a.check,**computed['summary.json']}))
if __name__=='__main__':main()
