#!/usr/bin/env python3
"""Reproduce source-specific MITAB records and sequence checks; Python 3.9+, stdlib only."""
from pathlib import Path
import argparse,json,hashlib,base64,collections,re
COLS=['id_a','id_b','alt_a','alt_b','alias_a','alias_b','method','author','publication','taxid_a','taxid_b','type','source','interaction_id','confidence','expansion','bio_role_a','bio_role_b','exp_role_a','exp_role_b','interactor_type_a','interactor_type_b','xref_a','xref_b','xref_interaction','annotation_a','annotation_b','annotation_interaction','host','parameters','creation','update','checksum_a','checksum_b','checksum_interaction','negative','feature_a','feature_b','stoichiometry_a','stoichiometry_b','identification_a','identification_b']
def main():
 p=argparse.ArgumentParser();p.add_argument('--directory',type=Path,default=Path(__file__).resolve().parent);p.add_argument('--target');p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true');a=p.parse_args()
 root=a.directory;sel=json.loads((root/'selection.json').read_text());target=a.target or sel['target'];records=[];all_target=0
 for s in json.loads((root/'sources.json').read_text()):
  data=(root/s['path']).read_bytes();assert hashlib.sha256(data).hexdigest()==s['sha256'],s['path']
 for line,raw in enumerate((root/'inputs/intact-O60762.tsv').read_text().splitlines(),1):
  if raw.startswith('#'):continue
  f=raw.split('\t');assert len(f)==len(COLS)
  if not any('uniprotkb:'+target in f[x].split('|') for x in [0,1]):continue
  all_target+=1
  if not any('pubmed:'+pm in f[8].split('|') for pm in sel['publications']):continue
  records.append({'physical_line':line,'fields':dict(zip(COLS,f))})
 counts=collections.Counter(re.search(r'pubmed:(\d+)',r['fields']['publication']).group(1) for r in records)
 identities={};proof=[]
 for f in sorted((root/'inputs').glob('*.json')):
  j=json.loads(f.read_text());acc=j['primaryAccession'];seq=j['sequence']['value'];identities[acc]=j
  rogid=base64.b64encode(hashlib.sha1(seq.encode()).digest()).decode().rstrip('=')+str(j['organism']['taxonId'])
  participants=[r for r in records if 'uniprotkb:'+acc in [r['fields']['id_a'],r['fields']['id_b']]]
  proof.append({'accession':acc,'length':len(seq),'sequence_sha256':hashlib.sha256(seq.encode()).hexdigest(),'ROGID':rogid,'selected_records_with_accession':len(participants),'matching_checksum_records':sum(any(rogid in r['fields'][x] for x in ['checksum_a','checksum_b']) for r in participants)})
 c=identities[sel['clone']]['sequence']['value'];r=identities[sel['reference']]['sequence']['value'];deletions=[i+1 for i in range(len(r)) if r[:i]+r[i+1:]==c]
 outputs={'selected-records.json':{'target':target,'all_target_records_in_snapshot':all_target,'selected_record_count':len(records),'selected_publication_counts':dict(sorted(counts.items())),'records':records},'sequence-checks.json':{'identities':proof,'clone_comparison':{'clone':sel['clone'],'reference':sel['reference'],'clone_length':len(c),'reference_length':len(r),'single_deletion_possible_positions':deletions,'deleted_residues':[r[i-1] for i in deletions]}}}
 out=a.output or root/'outputs'
 if a.check:
  for name,j in outputs.items():assert json.loads((out/name).read_text())==j,name
 else:
  out.mkdir(parents=True,exist_ok=True)
  for name,j in outputs.items():(out/name).write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n')
 print(json.dumps({'target':target,'all_target_records_in_snapshot':all_target,'selected':len(records),'sources':dict(counts),'single_deletion_positions':deletions,'mode':'check' if a.check else 'write'},sort_keys=True))
if __name__=='__main__':main()
