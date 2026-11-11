#!/usr/bin/env python3
"""Retrieve authenticated external inputs; do not replace differing existing files."""
import argparse, hashlib, json, urllib.request
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--manifest', type=Path, default=Path('input-manifest.json'))
parser.add_argument('--output', type=Path, required=True)
parser.add_argument('--all', action='store_true', help='Also retrieve the smaller inputs already bundled in the archive')
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
for item in json.loads(args.manifest.read_text()):
    if item.get('bundled', True) and not args.all:
        continue
    destination = args.output / item['name']
    if destination.exists():
        data = destination.read_bytes()
    else:
        request = urllib.request.Request(item['url'], headers={'User-Agent': 'EARS2-evidence-replay/1.0'})
        with urllib.request.urlopen(request, timeout=90) as response:
            data = response.read()
    actual = hashlib.sha256(data).hexdigest()
    if actual != item['sha256']:
        raise SystemExit('SHA-256 mismatch for '+item['name']+': expected '+item['sha256']+', observed '+actual+'. No file written.')
    if item.get('md5') and hashlib.md5(data).hexdigest() != item['md5']:
        raise SystemExit('Published MD5 mismatch for '+item['name']+'. No file written.')
    if not destination.exists():
        destination.write_bytes(data)
    print(item['name'], actual)
