#!/usr/bin/env python3
"""Download the public snapshots and verify exact bytes; no credentials required."""
import argparse,json,urllib.request,hashlib
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--manifest',type=Path,default=Path(__file__).with_name('source-manifest.json'));p.add_argument('--output-dir',type=Path,required=True);a=p.parse_args();a.output_dir.mkdir(parents=True,exist_ok=True)
for item in json.loads(a.manifest.read_text())['inputs'].values():
 data=urllib.request.urlopen(item['url'],timeout=120).read()
 if hashlib.sha256(data).hexdigest()!=item['sha256']:raise SystemExit('Upstream bytes changed: '+item['filename'])
 (a.output_dir/item['filename']).write_bytes(data)
 print(item['filename'],len(data),'SHA-256 verified')
