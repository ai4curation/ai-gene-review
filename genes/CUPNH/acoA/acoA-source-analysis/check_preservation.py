"""Check captured seed payloads without reading GOA as biological evidence."""
from pathlib import Path
import hashlib,json,yaml
root=Path(__file__).resolve().parents[4]
original=json.loads(Path(__file__).with_name('original-annotation-payloads.json').read_text())
report={'reviews':{},'original_rows':0,'final_rows':0,'raw_files':0,'passed':True}
for rel,b in original.items():
 d=yaml.safe_load((root/rel).read_text());n=len(b['annotations']);rows=d.get('existing_annotations',[])
 same=[{k:v for k,v in a.items() if k!='review'} for a in rows[:n]]==b['annotations']
 ids=all(d[k]==b[k] for k in ['id','gene_symbol','taxon'])
 raw=all(hashlib.sha256((root/q).read_bytes()).hexdigest()==h for q,h in b['raw_sha256'].items())
 additions=rows[n:];new_ok=all(a['term']['id']=='GO:0016624' and a.get('qualifier')=='contributes_to' and a['review']['action']=='NEW' and d['gene_symbol']=='acoB' for a in additions)
 ok=same and ids and raw and new_ok
 report['reviews'][rel]={'original_rows':n,'final_rows':len(rows),'payloads_identical':same,'identity_preserved':ids,'raw_hashes_identical':raw,'new_proposals':len(additions),'passed':ok}
 report['original_rows']+=n;report['final_rows']+=len(rows);report['raw_files']+=len(b['raw_sha256']);report['passed'] &=ok
print(json.dumps(report,indent=2));raise SystemExit(0 if report['passed'] else 1)
