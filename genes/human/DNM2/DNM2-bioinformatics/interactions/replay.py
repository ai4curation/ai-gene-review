#!/usr/bin/env python3
"""Reproduce DNM2 interaction selection from frozen raw inputs; Python 3.9+, stdlib only."""
import argparse,csv,json
from pathlib import Path
from extract import compute,verified_inputs

def binding_projection(paths,selection):
 result=[]
 for item in selection:
  source=item['source'];pmid=source['original_reference_id'].split(':')[-1]
  partners=[x.split(':',1)[1]for x in source.get('supporting_entities',[])];matches=[]
  for service in ['intact','mint']:
   with paths[service].open(newline='')as stream:
    for line,fields in enumerate(csv.reader(stream,delimiter='\t'),1):
     if len(fields)<15 or 'pubmed:'+pmid not in fields[8].split('|'):continue
     for side in [0,1]:
      ids=fields[side].split('|')+fields[side+2].split('|')
      if not any(v.lower()in ['uniprotkb:p50570']+['uniprotkb:p50570-'+str(i)for i in range(1,6)]for v in ids):continue
      other=1-side;other_ids=fields[other].split('|')+fields[other+2].split('|')
      matched=[p for p in partners if 'uniprotkb:'+p in other_ids]
      if matched:matches.append({'service':service,'line':line,'target_side':side,'matched_partners':matched,'fields':fields})
  result.append({'index':item['index'],'source':source,'matches':matches})
 return result

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--inputs-dir',required=True,type=Path);p.add_argument('--check',action='store_true');args=p.parse_args()
 here=Path(__file__).resolve().parent;manifest=json.loads((here/'source-manifest.json').read_text());selection=json.loads((here/'selection.json').read_text())
 paths=verified_inputs(args.inputs_dir,manifest)
 dataset=compute(args.inputs_dir,manifest,selection)
 binding=binding_projection(paths,json.loads((here/'binding-selection.json').read_text()))
 # Only the two relevant raw digests are part of the graph/CSV output contract.
 dataset['input_sha256']={k:v for k,v in dataset['input_sha256'].items()if k in ['apms','opencell']}
 for name,value in [('dataset-results.json',dataset),('binding-results.json',binding)]:
  encoded=json.dumps(value,indent=2,ensure_ascii=False)+'\n';path=here/name
  if args.check:
   if path.read_text()!=encoded:raise SystemExit('FAIL: raw-derived mismatch in '+name)
  else:path.write_text(encoded)
 print(json.dumps({'status':'PASS'if args.check else'WRITTEN','source_binding_rows':len(binding),'rows_with_MITAB_records':sum(bool(x['matches'])for x in binding),'MITAB_records':sum(len(x['matches'])for x in binding),'APMS_incident':dataset['apms']['incident_count'],'APMS_selected':dataset['apms']['selected_count'],'OpenCell_incident':dataset['opencell']['incident_count'],'OpenCell_selected':dataset['opencell']['selected_count']}))
if __name__=='__main__':main()
