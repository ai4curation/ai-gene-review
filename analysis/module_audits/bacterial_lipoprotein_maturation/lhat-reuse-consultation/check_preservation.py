"""Verify exact approved LhaT reuse without modifying source artifacts."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
AUDIT = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(row):
    return {key: value for key, value in row.items() if key != 'review'}


def main():
    proof = yaml.safe_load((AUDIT / 'reuse-provenance.yaml').read_text())
    for name, record in proof['files'].items():
        assert digest(ROOT / name) == record['sha256'], name
    provider = proof['prior_provider_attempt']
    assert digest(ROOT / provider['local_copy']) == provider['sha256']
    review = yaml.safe_load((ROOT / 'genes/BACSU/ypjA/ypjA-ai-review.yaml').read_text())
    rows = review['existing_annotations']
    assert len(rows) == 2
    assert [payload(rows[0])] == proof['fresh_seed_payloads']
    assert rows[0]['review']['action'] == 'ACCEPT'
    assert rows[1]['review']['action'] == 'NEW'
    assert rows[1]['term']['id'] == 'GO:0008080'
    assert not any(row.get('retired') for row in rows)
    baseline = json.loads((AUDIT.parent / 'baseline.json').read_text())
    for name, value in baseline['protected_files_sha256'].items():
        assert digest(ROOT / name) == value, name
    result = {
        'result': 'PASS', 'ordered_seed_rows': 1, 'approved_review_rows': 2,
        'historical_active_NEW': 1, 'newly_authored_proposals': 0,
        'retired_rows': 0, 'source_files_exact': len(proof['files']),
        'initial_module_sources_preserved': len(baseline['protected_files_sha256']),
        'science': 'Review and notes byte-identical to approved commit blobs',
    }
    (AUDIT / 'preservation.yaml').write_text(yaml.safe_dump(result, sort_keys=False))
    print(result)


if __name__ == '__main__':
    main()
