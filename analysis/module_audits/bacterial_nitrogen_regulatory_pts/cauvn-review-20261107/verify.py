"""Check original payloads, lifecycle, immutable sources, and literal quotations."""
import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
AUDIT = Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def normalized(text):
    return re.sub(r'\s+', ' ', text).strip()

def payload(row):
    return {key: val for key, val in row.items() if key != 'review'}

def source(reference):
    if reference.startswith('PMID:'):
        return ROOT / ('publications/PMID_' + reference.split(':')[1] + '.md')
    if reference.startswith('file:'):
        rel = reference[5:]
        return next(path for path in (ROOT / 'genes' / rel, ROOT / rel) if path.exists())
    raise ValueError(reference)

def walk(value, reference=None):
    if isinstance(value, dict):
        reference = value.get('reference_id', reference)
        if 'findings' in value:
            reference = value['id']
        if value.get('supporting_text'):
            yield reference, value['supporting_text']
        for child in value.values():
            yield from walk(child, reference)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child, reference)

def main():
    baseline = json.loads((AUDIT / 'baseline.json').read_text())
    protected = {p: sha for p, sha in baseline['files'].items() if not p.endswith('-ai-review.yaml')}
    protected.update(baseline['publication_snapshot'])
    for path, sha in protected.items():
        assert digest(ROOT / path) == sha, path
    result = {'ordered_rows': 0, 'original_new': 0, 'current_new': 0, 'retired': 0,
              'quotes_verified': 0, 'protected_input_count': len(protected),
              'protected_inputs': protected, 'source_dependencies': {}, 'genes': {}}
    for gene in ('ptsP', 'ptsH', 'ptsN'):
        path = ROOT / f'genes/CAUVN/{gene}/{gene}-ai-review.yaml'
        current = yaml.safe_load(path.read_text())
        seed = AUDIT / f'seed-copies/{gene}-ai-review.yaml'
        assert digest(seed) == baseline['files'][str(path.relative_to(ROOT))]
        original = yaml.safe_load(seed.read_text())
        oldrows = original['existing_annotations']
        rows = current['existing_annotations']
        assert [payload(row) for row in oldrows] == [payload(row) for row in rows], gene
        assert current['status'] == 'COMPLETE'
        assert all(row['review']['action'] != 'PENDING' for row in rows)
        assert all(line == line.rstrip() for line in path.read_text().splitlines())
        result['ordered_rows'] += len(rows)
        result['original_new'] += sum(row['review']['action'] == 'NEW' for row in oldrows)
        result['current_new'] += sum(row['review']['action'] == 'NEW' for row in rows)
        result['retired'] += sum(bool(row.get('retired')) for row in rows)
        for ref, quote in walk(current):
            src = source(ref)
            assert normalized(quote) in normalized(src.read_text()), (gene, ref, quote)
            result['quotes_verified'] += 1
            result['source_dependencies'][str(src.relative_to(ROOT))] = digest(src)
        result['genes'][gene] = {'rows': len(rows), 'review_sha256': digest(path),
                                'actions': [row['review']['action'] for row in rows]}
    assert (result['ordered_rows'], result['original_new'], result['current_new'], result['retired']) == (15, 0, 0, 0)
    for pmid in ('27109061', '26489861'):
        path = ROOT / f'publications/PMID_{pmid}.md'
        result['source_dependencies'][str(path.relative_to(ROOT))] = digest(path)
    result['new_publication_note'] = '26489861 was normally fetched by root after this consultation baseline; full canonical text, no existing cache replacement.'
    result['status'] = 'PASS'
    (AUDIT / 'preservation.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('protected_inputs', 'source_dependencies', 'genes')}, indent=2))

if __name__ == '__main__':
    main()
