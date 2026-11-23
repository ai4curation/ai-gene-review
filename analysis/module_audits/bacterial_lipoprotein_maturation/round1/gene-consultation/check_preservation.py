"""Verify PR6184 gene follow-up with one exact, authorized authored-row exception."""
import copy
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
AUDIT = Path(__file__).resolve().parent
BASELINE = AUDIT.parent / 'baseline.json'
CHANGED = {
    'genes/ECOLI/lgt/lgt-ai-review.yaml',
    'genes/PSEPK/lspA/lspA-ai-review.yaml',
    'genes/ECOLI/lspA/lspA-ai-review.yaml',
    'genes/BACSU/lspA/lspA-ai-review.yaml',
    'genes/BACFN/BF9343_0945/BF9343_0945-ai-review.yaml',
    'genes/BACTN/BT_4364/BT_4364-ai-review.yaml',
    'genes/BACCR/BC_1526/BC_1526-ai-review.yaml',
    'genes/STAA8/SAOUHSC_00822/SAOUHSC_00822-ai-review.yaml',
    'genes/STAA8/SAOUHSC_02761/SAOUHSC_02761-ai-review.yaml',
}
LIT = 'genes/BACCR/BC_1526/BC_1526-ai-review.yaml'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def differences(a, b, prefix=''):
    if isinstance(a, dict) and isinstance(b, dict):
        result = []
        for key in sorted(a.keys() | b.keys()):
            p = f'{prefix}.{key}' if prefix else key
            if key not in a or key not in b:
                result.append({'path': p, 'before': a.get(key), 'after': b.get(key)})
            else:
                result.extend(differences(a[key], b[key], p))
        return result
    if isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        result = []
        for i, (old, new) in enumerate(zip(a, b, strict=True)):
            result.extend(differences(old, new, f'{prefix}[{i}]'))
        return result
    return [] if a == b else [{'path': prefix, 'before': a, 'after': b}]


def main():
    baseline = json.loads(BASELINE.read_text())
    rows = new_rows = retired_rows = 0
    semantic_changes = {}
    action_changes = []
    source_hashes = {}
    for name, old in baseline['reviews'].items():
        current = yaml.safe_load((ROOT / name).read_text())
        previous = old['document']
        assert current['id'] == previous['id']
        assert current['taxon'] == previous['taxon']
        original_rows = previous['existing_annotations']
        current_rows = current['existing_annotations']
        assert len(original_rows) == len(current_rows), name
        for i, (before, after) in enumerate(zip(original_rows, current_rows, strict=True)):
            a = {k: v for k, v in before.items() if k != 'review'}
            b = {k: v for k, v in after.items() if k != 'review'}
            if name == LIT and i == 2:
                assert a['term'] == {'id': 'GO:0005886', 'label': 'plasma membrane'}
                assert a['original_reference_id'] == 'PMID:34253723'
                assert before['review']['action'] == after['review']['action'] == 'NEW'
                assert a['evidence_type'] == 'IDA' and b['evidence_type'] == 'IC'
                a = copy.deepcopy(a)
                a['evidence_type'] = 'IC'
            assert a == b, (name, i, 'source payload or lifecycle drift')
            if before['review']['action'] != after['review']['action']:
                action_changes.append((name, i, before['review']['action'], after['review']['action']))
            if before['review']['action'] == 'NEW':
                assert after['review']['action'] == 'NEW'
                new_rows += 1
                retired_rows += int(bool(after.get('retired')))
            rows += 1
        delta = differences(previous, current)
        if name not in CHANGED:
            assert not delta, (name, 'unowned review changed')
            assert digest(ROOT / name) == old['sha256']
        else:
            semantic_changes[name] = delta
            gene = Path(name).parts[2]
            organism = Path(name).parts[1]
            allowed = set()
            if gene == 'lgt':
                allowed = {
                    'existing_annotations[12].review.' + field
                    for field in ['action', 'reason', 'summary',
                                  'supported_by[0].reference_id',
                                  'supported_by[0].supporting_text',
                                  'supported_by[1].reference_id',
                                  'supported_by[1].supporting_text']
                } | {'references[3].findings[0].statement'}
            elif gene == 'lspA' and organism == 'PSEPK':
                allowed = {
                    'existing_annotations[2].review.' + field
                    for field in ['action', 'reason', 'summary', 'proposed_replacement_terms']
                } | {'core_functions[0].supported_by[2].record_section',
                     'existing_annotations[0].review.supported_by[2].record_section'}
            elif gene == 'lspA':
                allowed = {'proposed_new_terms[0].' + field
                           for field in ['justification', 'proposed_parent.id',
                                         'proposed_parent.label']}
            elif gene in {'BF9343_0945', 'BT_4364'}:
                allowed = {'core_functions[0].' + field
                           for field in ['description', 'locations[0].id',
                                         'locations[0].label', 'supported_by']}
                allowed.add('proposed_new_terms')
                assert current['core_functions'][0]['supported_by'][:-1] == previous['core_functions'][0]['supported_by']
                assert current['core_functions'][0]['locations'] == [
                    {'id': 'GO:0005886', 'label': 'plasma membrane'}]
            elif name == LIT:
                allowed = {'existing_annotations[2].evidence_type',
                           'existing_annotations[2].review.reason', 'proposed_new_terms',
                           'references[3].findings[0].record_section'}
            else:
                allowed = {'proposed_new_terms'}
            assert {entry['path'] for entry in delta} <= allowed, (name, delta)
    assert action_changes == [
        ('genes/ECOLI/lgt/lgt-ai-review.yaml', 12, 'KEEP_AS_NON_CORE', 'UNDECIDED'),
        ('genes/PSEPK/lspA/lspA-ai-review.yaml', 2, 'ACCEPT', 'MODIFY'),
    ], action_changes
    for name, expected in baseline['protected_sources_sha256'].items():
        actual = digest(ROOT / name)
        assert actual == expected, (name, 'protected source changed')
        source_hashes[name] = actual
    historical_receipts = {}
    for name, expected in baseline['published_closure_sha256'].items():
        if name.startswith(('history/', 'analysis/module_audits/')):
            actual = digest(ROOT / name)
            assert actual == expected, (name, 'published history or audit receipt changed')
            historical_receipts[name] = actual
    result = {
        'status': 'PASS', 'baseline_sha256': digest(BASELINE),
        'review_count': len(baseline['reviews']), 'ordered_rows': rows,
        'historical_new': new_rows, 'active_new': new_rows - retired_rows,
        'retired_new': retired_rows, 'new_rows_added': 0,
        'source_payload_exception': {
            'path': LIT, 'row_index': 2, 'term': 'GO:0005886',
            'reference': 'PMID:34253723', 'action': 'NEW',
            'field': 'evidence_type', 'before': 'IDA', 'after': 'IC',
            'authorization': 'Explicit parent instruction: correct authored inference code; preserve every other payload and lifecycle field.',
            'reason': 'Native plasma-membrane compartment inferred from four-helix structure plus pathway; no direct native Bacillus localization assay.',
        },
        'action_changes': action_changes,
        'protected_sources_sha256': source_hashes,
        'unchanged_published_histories_and_receipts_sha256': historical_receipts,
        'semantic_changes': semantic_changes,
    }
    (AUDIT / 'preservation.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({k: result[k] for k in ['status', 'review_count', 'ordered_rows', 'historical_new', 'active_new', 'retired_new', 'new_rows_added']}))
    print(f'Protected sources: {len(source_hashes)}; unchanged historical histories/receipts: {len(historical_receipts)}')


if __name__ == '__main__':
    main()
