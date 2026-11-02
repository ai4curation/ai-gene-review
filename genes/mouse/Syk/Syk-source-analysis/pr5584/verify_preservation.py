from pathlib import Path
import json,yaml,hashlib
root=Path(__file__).resolve().parents[5]
p=json.loads(Path(__file__).with_name('panel-preservation.json').read_text())
for f,b in p['reviews'].items():
 d=yaml.safe_load((root/f).read_text())
 rows=[{k:v for k,v in a.items() if k!='review'} for a in d['existing_annotations']]
 h=hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 assert h==b['original_payload_sha256'],f
for f,h in p['raw_sha256'].items():
 assert hashlib.sha256((root/f).read_bytes()).hexdigest()==h,f
print('PASS: 2645 ordered original payloads and 44 raw hashes preserved.')
