#!/usr/bin/env python3
"""Verify PR6160 gene follow-up against its frozen, ordered source inputs."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    baseline = json.loads((HERE / 'frozen-inputs.json').read_text())
    rows = inherited_new = 0
    results = []
    for relative, original in baseline['reviews'].items():
        current = yaml.safe_load((ROOT / relative).read_text())
        annotations = current['existing_annotations']
        payloads = [{k: v for k, v in row.items() if k != 'review'} for row in annotations]
        actions = [row['review']['action'] for row in annotations]
        assert payloads == original['payloads'], f'Ordered payload change: {relative}'
        assert actions == original['actions'], f'Action change: {relative}'
        assert current['status'] == original['status'], relative
        rows += len(annotations)
        inherited_new += actions.count('NEW')
        results.append({'path': relative, 'rows': len(annotations), 'sha256': sha(ROOT / relative)})
    for relative, expected in baseline['protected_sha256'].items():
        assert sha(ROOT / relative) == expected, f'Protected source changed: {relative}'
    for relative, original in baseline.get('notes', {}).items():
        contents = (ROOT / relative).read_bytes()
        assert hashlib.sha256(contents[:original['bytes']]).hexdigest() == original['sha256'], relative
    result = {
        'status': 'PASS', 'baseline_head': baseline['head'],
        'review_count': len(results), 'ordered_original_rows': rows,
        'historical_NEW_preserved': inherited_new, 'added_NEW': 0,
        'action_changes': 0, 'protected_source_count': len(baseline['protected_sha256']),
        'all_payloads_order_actions_sources_preserved': True,
        'notes_original_prefixes_preserved': True, 'reviews': results,
    }
    (HERE / 'preservation.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
