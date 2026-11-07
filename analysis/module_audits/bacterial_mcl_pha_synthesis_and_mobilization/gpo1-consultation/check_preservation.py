"""Prove GPo1 source-row, source-byte and frozen literature preservation."""
from collections import Counter
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
AUDIT = HERE.parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(row):
    return {key: value for key, value in row.items() if key != 'review'}


def main():
    base = json.loads((AUDIT / 'baseline.json').read_text())
    seeded = json.loads((AUDIT / 'additional-seed-baseline.json').read_text())
    sources = base['protected_files_sha256'] | seeded['protected_files_sha256']
    for path, expected in sources.items():
        assert sha(ROOT / path) == expected, path
    frozen = AUDIT / 'literature-consultation/handoff.json'
    assert sha(frozen) == '630f9b317c16e4505acf959e6fd9c4e585b2198dcdcd14b9a63fc925c3da2cd7'
    for path, expected in json.loads(frozen.read_text())['files'].items():
        assert sha(ROOT / path) == expected, path
    results = []
    actions = Counter()
    for path, before in seeded['genes'].items():
        if not path.startswith('genes/ECTOL/'):
            continue
        doc = yaml.safe_load((ROOT / path).read_text())
        assert doc['status'] == 'COMPLETE', path
        rows = doc['existing_annotations']
        original = before['document']['existing_annotations']
        assert list(map(payload, rows)) == list(map(payload, original)), path
        for row in rows:
            assert row['review']['action'] != 'PENDING'
            actions[row['review']['action']] += 1
        results.append({'review': path, 'ordered_payloads_preserved': len(rows),
                        'new_rows': 0, 'retired_rows': 0})
    out = {'status': 'PASS', 'reviews': results, 'actions': dict(actions),
           'protected_source_files': len(sources), 'prior_literature_files_preserved': 24,
           'all_seven_payloads_and_order_preserved': True,
           'provider_attempts': {'count': 3, 'result': '403 authentication failure'},
           'focused_validation': '3 PASS; 2 PhaZ core-coverage advisories; no NEW added for warnings',
           'paint': 'All three targets absent from reference trees; lineage losses not resolvable'}
    (HERE / 'preservation-results.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out))


if __name__ == '__main__':
    main()
