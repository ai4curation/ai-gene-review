#!/usr/bin/env python3
"""Optional acquisition of the declared live sources. Never replace differing inputs.
The bundled archive is the authoritative historical snapshot for offline replay.
"""
import argparse,hashlib,json,urllib.request
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--manifest',type=Path,default=Path('input-manifest.json'));p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
for r in json.loads(a.manifest.read_text()):
    dest=a.output/r['name']
    data=dest.read_bytes()if dest.exists()else urllib.request.urlopen(urllib.request.Request(r['url'],headers={'User-Agent':'DZIP1L-evidence-replay/1.0'}),timeout=90).read()
    actual=hashlib.sha256(data).hexdigest()
    if actual!=r['sha256']:raise SystemExit('Source version differs: '+r['name']+'; expected '+r['sha256']+' observed '+actual+'. Use the bundled historical snapshot; no replacement written.')
    if not dest.exists():dest.write_bytes(data)
    print(r['name'],actual)
