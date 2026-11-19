#!/usr/bin/env python3
"""Reproduce DMGO accession/construct checks from authoritative source snapshots.

Run from the repository root with `uv run python
 genes/ARTGO/dmg/dmg-source-analysis/verify_identity.py`.
Use --fetch to acquire missing source responses into ignored audit cache only.
Frozen gene sources and publications are never changed. Hash differences stop
verification; they require an explicit source-version reassessment.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import urllib.request
import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--fetch', action='store_true')
args = parser.parse_args()
provenance = yaml.safe_load((HERE / 'identity-provenance.yaml').read_text())
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
for source in provenance['source_records']:
    path = ROOT / source['cached_path']
    if not path.exists() and args.fetch:
        path.parent.mkdir(parents=True, exist_ok=True)
        request = urllib.request.Request(source['url'], headers={'User-Agent': 'ai-gene-review identity audit'})
        with urllib.request.urlopen(request, timeout=90) as response:
            data = response.read()
        assert hashlib.sha256(data).hexdigest() == source['sha256'], f'Changed upstream source: {source["url"]}'
        path.write_bytes(data)
    assert path.exists(), f'Missing {path}; rerun with --fetch'
    assert sha(path) == source['sha256'], f'Hash mismatch: {path}'

raw = HERE.parent / 'dmg-uniprot.txt'
assert sha(raw) == provenance['uniprot_raw_sha256']
sequence = re.sub(r'[^A-Z]', '', raw.read_text().split('\nSQ   ', 1)[1].split('\n', 1)[1].split('//', 1)[0])
assert len(sequence) == 830
cache = ROOT / '.cache/module-audit-logs/dimethylglycine-20261106/artgo-dmg'
embl = (cache / 'AF329477.embl').read_text()
assert '/strain="NRRL B-2979"' in embl
block = next(b for b in re.split(r'\nFT   CDS\s+', embl) if '/protein_id="AAK16482.1"' in b)
assert block.startswith('1099..3591')
translation = re.search(r'/translation="([^"]+)"', block).group(1)
translation = re.sub(r'\s+', '', re.sub(r'\nFT\s+', '', translation))
assert translation == sequence
wildtype = json.loads((cache / '1PJ5-entity1.json').read_text())
mutant = json.loads((cache / '3GSI-entity1.json').read_text())
def polymer(d):
    return re.sub(r'\s+', '', d['entity_poly']['pdbx_seq_one_letter_code_can'])
assert polymer(wildtype) == sequence
assert len(polymer(mutant)) == 827
changes = [(i + 4, a, b) for i, (a, b) in enumerate(zip(sequence[3:], polymer(mutant))) if a != b]
assert changes == [(552, 'D', 'A')]
assert 'D552A' in json.dumps(mutant)
assert 'Q9AGP8' in json.dumps(wildtype)
paralog = next(b for b in re.split(r'\nFT   CDS\s+', embl) if '/protein_id="ABB73054.1"' in b)
assert paralog.startswith('14567..17074')
paralog_translation = re.sub(r'\s+', '', re.sub(r'\nFT\s+', '', re.search(r'/translation="([^"]+)"', paralog).group(1)))
assert paralog_translation != sequence
# This source quote is textually contiguous even in the original HTML.
quote = 'we could not easily discriminate between the linear and cyclic forms'
assert quote in (cache / 'PMC2719421.html').read_text()
print(json.dumps({'result': 'PASS', 'target': 'UniProtKB:Q9AGP8',
 'donor_strain': 'NRRL B-2979', 'length': 830,
 'AF329477.3_AAK16482.1': '830/830 exact', '1PJ5_entity1': '830/830 exact',
 '3GSI_entity1': {'target_range': '4-830', 'length': 827, 'substitution': 'D552A'},
 'distinct_dmg2': 'ABB73054.1, 14567..17074; not the assayed dmg construct',
 'source_snapshots_sha256': 'all four match', '2009_intermediate_quote': 'exact match',
 '2001_substrate_quote': 'manually checked publisher full text; source bytes unavailable'}, indent=2))
