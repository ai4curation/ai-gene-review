"""Recover pinned inputs to a separate directory; reject changed remote bytes."""
import argparse, hashlib, json
from pathlib import Path
from urllib.request import urlopen

p = argparse.ArgumentParser()
p.add_argument('--manifest', type=Path, required=True)
p.add_argument('--output-dir', type=Path, required=True)
a = p.parse_args()
for item in json.loads(a.manifest.read_text())['inputs']:
    target = a.output_dir / item['path']
    if target.exists():
        data = target.read_bytes()
    else:
        with urlopen(item['retrieval']['url'], timeout=90) as response:
            data = response.read()
    actual = hashlib.sha256(data).hexdigest()
    if actual != item['sha256']:
        raise ValueError(f"Remote/existing bytes changed: {item['path']} {actual}")
    if not target.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    print(f"Verified {item['path']} {actual}")
