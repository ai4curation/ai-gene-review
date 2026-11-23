"""Verify additive PR6193 curation and rerun the unchanged capacity expectations."""
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.dont_write_bytecode = True


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(rows):
    return [{k: v for k, v in row.items() if k != 'review'} for row in rows]


def main():
    before = json.loads((HERE / 'baseline.json').read_text())
    for path, digest in before['protected'].items():
        assert sha(ROOT / path) == digest, path
    for path, digest in before['old_audit_and_family_files'].items():
        assert sha(ROOT / path) == digest, path
    assert sha(ROOT / 'modules/bacterial_mannose_pts.yaml') == before['module_sha256']
    changed = []
    total = 0
    for path, original in before['genes'].items():
        current = yaml.safe_load((ROOT / path).read_text())
        old = original['document']['existing_annotations']
        new = current['existing_annotations']
        assert payload(old) == payload(new), path
        assert current['status'] == 'COMPLETE'
        assert [r.get('retired', False) for r in old] == [r.get('retired', False) for r in new]
        total += len(new)
        for index, (a, b) in enumerate(zip(old, new, strict=True)):
            if a['review']['action'] != b['review']['action']:
                assert current['gene_symbol'] == 'manL'
                assert b['term']['id'] in {'GO:0005886', 'GO:0016020'}
                assert b['review']['action'] == 'UNDECIDED'
                changed.append({'path': path, 'index': index, 'term': b['term']['id'],
                                'before': a['review']['action'], 'after': b['review']['action']})
        assert current['core_functions'][0]['contributes_to_molecular_function']['id'] == 'GO:0022870'
        if current['gene_symbol'] == 'manL':
            assert {x['id'] for x in current['core_functions'][0]['locations']} == {'GO:0005829'}
        assert 'grew more slowly than the wild-type strain in glucose but grew faster in mannose' not in json.dumps(current)
    assert total == 15 and len(changed) == 2
    panel = json.loads((HERE / 'published-panel-baseline.json').read_text())
    panel_rows = historical_new = 0
    for path, original in panel.items():
        current = yaml.safe_load((ROOT / path).read_text())
        old = original['document']['existing_annotations']
        new = current['existing_annotations']
        assert payload(old) == payload(new), path
        assert [(r['review']['action'] == 'NEW', r.get('retired', False)) for r in old] == [
            (r['review']['action'] == 'NEW', r.get('retired', False)) for r in new]
        panel_rows += len(new)
        historical_new += sum(r['review']['action'] == 'NEW' for r in new)
        if path not in before['genes']:
            assert sha(ROOT / path) == original['sha256'], path
    assert panel_rows == 93 and historical_new == 2
    source = ROOT / 'analysis/module_audits/bacterial_mannose_pts/capacity-consultation/check_capacity.py'
    spec = importlib.util.spec_from_file_location('published_capacity', source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.HERE = HERE / 'capacity-rerun'
    module.HERE.mkdir(exist_ok=True)
    module.main()
    result = json.loads((module.HERE / 'results.json').read_text())
    assert (result['case_count'], result['mutation_count'], result['sensitivity_count']) == (60, 13, 9)
    output = {
        'status': 'PASS', 'original_ordered_rows': total, 'payload_changes': 0,
        'whole_panel_original_rows': panel_rows, 'historical_new_preserved': historical_new,
        'new_rows': 0, 'retired_rows_changed': 0, 'review_action_changes': changed,
        'protected_source_count': len(before['protected']),
        'prior_audit_family_files_unchanged': len(before['old_audit_and_family_files']),
        'module_sha256_unchanged': before['module_sha256'],
        'published_capacity_checker_sha256': sha(source),
        'capacity': {k: result[k] for k in ['case_count', 'mutation_count', 'sensitivity_count']},
        'supersession': {path: {'published_sha256': data['sha256'], 'current_sha256': sha(ROOT / path)}
                        for path, data in before['genes'].items()},
        'limitations': ['Focused validation only; no full corpus result claimed.',
                       'Preserved review payloads do not prove lossless raw GOA multiplicity.',
                       'Family and domain constraints require the evidence-aware oracle; naked boolean atoms are insufficient.'],
    }
    (HERE / 'preservation.json').write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps({k: output[k] for k in ['status', 'original_ordered_rows', 'payload_changes', 'capacity']}))


if __name__ == '__main__':
    main()
