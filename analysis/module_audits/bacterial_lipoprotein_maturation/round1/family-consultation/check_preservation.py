"""Recheck scoped family edits, frozen sources, original assertions and quotations."""

import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
AUDIT = HERE.parent.parent
FAMILY = 'interpro/panther/PTHR38686/PTHR38686-review.yaml'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def norm(text):
    return ' '.join(re.sub(r'(?m)^(?:CC|FT|DE)\s+', '', text).split())


def quotes(value):
    if isinstance(value, dict):
        if 'reference_id' in value and 'supporting_text' in value:
            yield value
        for item in value.values():
            yield from quotes(item)
    elif isinstance(value, list):
        for item in value:
            yield from quotes(item)


def payload(row):
    return {k: v for k, v in row.items() if k not in {'assessment', 'assessment_reason', 'supported_by'}}


def main():
    published = json.loads((AUDIT / 'round1/baseline.json').read_text())
    original = json.loads((AUDIT / 'baseline.json').read_text())
    failures = []
    for path, digest in published['protected_sources_sha256'].items():
        if sha(ROOT / path) != digest:
            failures.append(f'Protected source changed: {path}')
    historical = {
        p: h for p, h in published['published_closure_sha256'].items()
        if p.startswith(('analysis/', 'history/'))
    }
    for path, digest in historical.items():
        if sha(ROOT / path) != digest:
            failures.append(f'Published historical artifact changed: {path}')
    assertions = 0
    for path, old in published['families'].items():
        doc = yaml.safe_load((ROOT / path).read_text())
        before = old['document'].get('node_assessments', [])
        after = doc.get('node_assessments', [])
        if [payload(x) for x in before] != [payload(x) for x in after]:
            failures.append(f'Ordered PAINT assertion changed: {path}')
        if [x['assessment'] for x in before] != [x['assessment'] for x in after]:
            failures.append(f'PAINT judgment enum changed: {path}')
        assertions += len(before)
        if path != FAMILY and sha(ROOT / path) != old['sha256']:
            failures.append(f'Unowned family changed: {path}')
    current = yaml.safe_load((ROOT / FAMILY).read_text())
    old = published['families'][FAMILY]['document']
    allowed = {'node_assessments', 'term_assessments', 'references', 'notes'}
    for key in old.keys() | current.keys():
        if key not in allowed and old.get(key) != current.get(key):
            failures.append(f'Unexpected top-level edit: {key}')
    if [x['scope'] for x in old['term_assessments']] != [x['scope'] for x in current['term_assessments']]:
        failures.append('Family term scopes changed')
    source_hashes = {}
    quote_count = 0
    for family in [FAMILY, 'interpro/panther/PTHR40042/PTHR40042-review.yaml']:
        for entry in quotes(yaml.safe_load((ROOT / family).read_text())):
            ref = entry['reference_id']
            if ref.startswith('file:'):
                path = ROOT / ref[5:]
                if not path.exists():
                    path = ROOT / 'genes' / ref[5:]
            elif ref.startswith('PMID:'):
                path = ROOT / 'publications' / f"{ref.replace(':', '_')}.md"
            else:
                failures.append(f'Unsupported quote reference: {ref}')
                continue
            source_hashes[str(path.relative_to(ROOT))] = sha(path)
            if norm(entry['supporting_text']) not in norm(path.read_text()):
                failures.append(f'Quote mismatch: {family} / {ref}')
            quote_count += 1
    ledger = {}
    for label, doc in [('original', original['families'][FAMILY]['document']), ('published', old), ('revised', current)]:
        ledger[label] = {
            'notes': doc['notes'],
            'nodes': [x for x in doc['node_assessments'] if x['node_id'] in {'PANTHER:PTN000557706', 'PANTHER:PTN000092528', 'PANTHER:PTN002459128'}],
            'term': next(x for x in doc['term_assessments'] if x['assessed_term']['id'] == 'GO:0050126'),
        }
    (HERE / 'judgment-ledger.json').write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + '\n')
    result = {
        'status': 'FAIL' if failures else 'PASS',
        'protected_sources': len(published['protected_sources_sha256']),
        'unchanged_published_historical_artifacts': len(historical),
        'preserved_ordered_paint_assertions': assertions,
        'family_scope_and_node_enums_unchanged': not failures,
        'changed_families': [FAMILY],
        'unmodified_families': 3,
        'quotes_checked': quote_count,
        'source_sha256': source_hashes,
        'limitations': ['Gene and module edits belong to parallel owners and are not asserted unchanged here.'],
        'failures': failures,
    }
    (HERE / 'preservation.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'source_sha256'}, indent=2))
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
