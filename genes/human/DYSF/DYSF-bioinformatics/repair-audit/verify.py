"""Recompute ontology/comparator facts from genuine saved QuickGO records."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--gocam-index', type=Path)
parser.add_argument('--check', action='store_true')
args = parser.parse_args()
manifest = json.loads((HERE / 'sources.json').read_text())
archive = (HERE / 'input-records.json.gz').read_bytes()
assert hashlib.sha256(archive).hexdigest() == manifest['archive_sha256']
raw = json.loads(gzip.decompress(archive))
records = {}
for source in manifest['records']:
    text = raw[source['name']]
    assert hashlib.sha256(text.encode()).hexdigest() == source['sha256']
    records[source['name']] = json.loads(text)
terms = {t['id']: t for t in records['terms']['results']}
repair = records['repair-human']
assert repair['numberOfHits'] == len(repair['results'])
assert all(r['goId'] == 'GO:0001778' and r['taxonId'] == 9606 for r in repair['results'])
target = records['dysf-current']
assert target['numberOfHits'] == len(target['results'])
assert all(r['geneProductId'] == 'UniProtKB:O75923' for r in target['results'])
selected = {'UniProtKB:O43581', 'UniProtKB:Q9NZM1', 'UniProtKB:Q75V66', 'UniProtKB:Q9Y3E7'}
result = {
    'terms': {k: {'name': v['name'], 'aspect': v['aspect'], 'obsolete': v['isObsolete']} for k, v in terms.items()},
    'titin_ancestors': records['titin-ancestors']['results'][0]['ancestors'],
    'repair_ancestors': records['repair-ancestors']['results'][0]['ancestors'],
    'complete_human_repair_rows': len(repair['results']),
    'comparator_rows': [{k: r[k] for k in ['geneProductId', 'symbol', 'goEvidence', 'reference', 'qualifier', 'withFrom']} for r in repair['results'] if r['geneProductId'] in selected],
    'target_source_rows': len(target['results']),
    'target_repair_rows': [r for r in target['results'] if r['goId'] == 'GO:0001778'],
    'target_process_terms': sorted({r['goId'] for r in target['results'] if r['goAspect'] == 'biological_process'}),
}
if args.check:
    assert result == json.loads((HERE / 'RESULTS.json').read_text())
if args.gocam_index:
    source = args.gocam_index.read_bytes()
    assert hashlib.sha256(source).hexdigest() == manifest['gocam_index_sha256'], 'GO-CAM index version differs'
    matches = [line for line in source.decode().splitlines() if 'O75923' in line or 'DYSF' in line]
    assert not matches, matches
    print('PASS: captured GO-CAM index has no DYSF target matches')
if args.check:
    print('PASS: exact source hashes, complete query coverage, ontology and comparator results')
else:
    print(json.dumps(result, indent=2))
