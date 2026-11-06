"""Verify frozen original-panel payloads, explicit proposal refinement and raw sources."""
from collections import Counter
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / 'analysis/module_audits/bacterial_chemotaxis_signal_transduction'


def payload(row):
    return {key: value for key, value in row.items() if key != 'review'}


def signature(row):
    return json.dumps(row, sort_keys=True, ensure_ascii=False)


def main():
    baseline = json.loads((AUDIT / 'original-members-baseline.json').read_text())
    replacement = yaml.safe_load((AUDIT / 'PP_4332-authored-proposal-refinement.yaml').read_text())
    rows = raw_files = 0
    actions = Counter()
    for member in baseline['members']:
        document = yaml.safe_load((ROOT / member['review_path']).read_text())
        assert document['id'] == member['accession'], member['review_path']
        assert document['taxon'] == member['taxon'], member['review_path']
        assert document['status'] == 'COMPLETE', member['review_path']
        expected = Counter(signature(row['payload']) for row in member['annotations'])
        actual = Counter(signature(payload(row)) for row in document['existing_annotations'])
        if f"{member['organism']}/{member['gene']}" == replacement['gene']:
            assert replacement['original_row']['review']['action'] == 'NEW'
            old = signature(payload(replacement['original_row']))
            new = signature(payload(replacement['replacement_row']))
            assert expected[old] == 1
            expected.subtract({old: 1})
            expected.update({new: 1})
        assert +actual == +expected, member['review_path']
        for path, expected_hash in member['raw_sha256'].items():
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected_hash, path
            raw_files += 1
        rows += len(document['existing_annotations'])
        actions.update(row['review']['action'] for row in document['existing_annotations'])
    print(json.dumps({'reviews': len(baseline['members']), 'historical_rows': rows,
                      'machine_payloads_preserved': True, 'archived_authored_refinements': 1,
                      'raw_sources_preserved': raw_files, 'actions': dict(actions)}, indent=2))


if __name__ == '__main__':
    main()
