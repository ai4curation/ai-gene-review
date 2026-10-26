from pathlib import Path
import json,hashlib,yaml
root=Path(__file__).resolve().parents[4]
p=json.loads(Path(__file__).with_name('original-annotation-payloads.json').read_text())
for f,b in p['reviews'].items():
 d=yaml.safe_load((root/f).read_text())
 assert [{k:v for k,v in a.items() if k!='review'} for a in d['existing_annotations']]==b['original_payloads'],f
for f,h in p['raw_sha256'].items():
 assert hashlib.sha256((root/f).read_bytes()).hexdigest()==h,f
print('PASS: 24 original annotation payloads and four raw source hashes preserved; no new rows.')
