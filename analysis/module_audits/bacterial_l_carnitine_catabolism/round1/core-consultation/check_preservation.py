"""Check permitted lifecycle/core changes against the published round-one baseline."""
import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]


def payload(row):
    return {key: value for key, value in row.items() if key not in {'review', 'retired'}}


def main():
    before = json.loads((HERE / 'before.json').read_text())
    allowed = {(x['path'], x['term']) for x in before['allowed_retirement_only']}
    lifecycle = []
    actions = []
    counts = {'rows': 0, 'historical_NEW': 0, 'retired_before': 0, 'retired_after': 0}
    for name, record in before['reviews'].items():
        old = record['document']
        current = yaml.safe_load((ROOT / name).read_text())
        old_rows = old['existing_annotations']
        rows = current['existing_annotations']
        assert list(map(payload, old_rows)) == list(map(payload, rows)), name
        assert len(old_rows) == len(rows)
        for i, (prior, row) in enumerate(zip(old_rows, rows, strict=True)):
            term = row['term']['id']
            counts['rows'] += 1
            counts['historical_NEW'] += prior['review']['action'] == 'NEW'
            counts['retired_before'] += bool(prior.get('retired'))
            counts['retired_after'] += bool(row.get('retired'))
            if prior.get('retired', False) != row.get('retired', False):
                assert (name, term) in allowed
                assert row['retired'] is True
                assert prior['review']['action'] == row['review']['action'] == 'NEW'
                lifecycle.append({'path': name, 'index': i, 'term': term,
                                  'before': False, 'after': True,
                                  'reason': 'Curator retirement of redundant proposal; activity retained.'})
            if prior['review']['action'] != row['review']['action']:
                assert name.endswith('bcoE-bcoF-ai-review.yaml') and term == 'GO:0070403'
                assert (prior['review']['action'], row['review']['action']) == ('KEEP_AS_NON_CORE', 'ACCEPT')
                actions.append({'path': name, 'index': i, 'term': term,
                                'before': prior['review']['action'], 'after': row['review']['action']})
        if name.endswith('PP_0303-ai-review.yaml'):
            core = current['core_functions'][0]
            assert 'molecular_function' not in core
            assert core['proposed_molecular_function'] == current['proposed_new_terms'][0]['proposed_name']
            assert core['supported_by'] == old['core_functions'][0]['supported_by']
            assert current['existing_annotations'] == old_rows
            assert rows[0]['review']['action'] == 'UNDECIDED'
        else:
            assert current['core_functions'] == old['core_functions']
        for key in old.keys() - {'existing_annotations', 'core_functions'}:
            assert current[key] == old[key], (name, key)
    assert len(lifecycle) == 2 and len(actions) == 1
    for name, expected in before['protected_sources_sha256'].items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected, name
    result = {'status': 'PASS', **counts, 'rows_added': 0, 'rows_deleted': 0,
              'payload_changes': 0, 'ordered_payloads_exact': True,
              'protected_sources': len(before['protected_sources_sha256']),
              'lifecycle_changes': lifecycle, 'action_changes': actions,
              'core_change': 'PP_0303 exact existing proposed MF; no new annotation assertion',
              'active_NEW_after': counts['historical_NEW'] - counts['retired_after']}
    (HERE / 'preservation.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
