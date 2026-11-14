"""Lightweight additive checks; no validators, renders or source writes."""
import copy
import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def differences(old, new, path=''):
    if isinstance(old, dict) and isinstance(new, dict):
        out = []
        for key in sorted(set(old) | set(new)):
            where = path + '/' + key
            if key not in old or key not in new:
                out.append(where)
            else:
                out.extend(differences(old[key], new[key], where))
        return out
    if isinstance(old, list) and isinstance(new, list):
        if len(old) != len(new):
            return [path]
        return [item for i, (a, b) in enumerate(zip(old, new, strict=True))
                for item in differences(a, b, path + '/' + str(i))]
    return [] if old == new else [path]


def main():
    before = json.loads((HERE / 'before.json').read_text())
    result = {'status': 'PASS_LIGHTWEIGHT', 'baseline_head': before['head'],
              'documents': {}, 'ordered_rows': 0, 'historical_NEW': 0,
              'source_payload_or_lifecycle_changes': 0, 'new_supporting_quotes': 0}
    for name, snapshot in before['documents'].items():
        old = snapshot['document']
        new = yaml.safe_load((ROOT / name).read_text())
        changed = differences(old, new)
        def quotations(value):
            if isinstance(value, dict):
                found = [value['supporting_text']] if 'supporting_text' in value else []
                return found + [q for v in value.values() for q in quotations(v)]
            if isinstance(value, list):
                return [q for v in value for q in quotations(v)]
            return []
        assert set(quotations(new)).issubset(set(quotations(old)))
        if name.startswith('genes/'):
            old_rows = old['existing_annotations']
            rows = new['existing_annotations']
            assert len(rows) == len(old_rows)
            for old_row, row in zip(old_rows, rows, strict=True):
                assert {k: v for k, v in old_row.items() if k != 'review'} == {
                    k: v for k, v in row.items() if k != 'review'}
                a = copy.deepcopy(old_row['review'])
                b = copy.deepcopy(row['review'])
                a.pop('reason', None)
                b.pop('reason', None)
                assert a == b
                if old_row['review']['action'] == 'NEW':
                    result['historical_NEW'] += 1
            result['ordered_rows'] += len(rows)
            if '/cheW/' in name:
                assert len(changed) == 4 and all(p.endswith('/review/reason') for p in changed)
                assert 'GO:0060090' not in (ROOT / name).read_text()
            else:
                assert changed == ['/knowledge_gaps', '/suggested_experiments']
                assert new['suggested_experiments'][0]['experiment_type'] == 'Purified-protein phosphotransfer and phosphate-release kinetics'
        else:
            assert len(changed) == 4
            assert sum(p.endswith('/role_description') for p in changed) == 3
            assert '/notes' in changed
        result['documents'][name] = {'before_sha256': snapshot['sha256'],
                                    'after_sha256': sha(ROOT / name), 'changed_fields': changed}
    for name, record in before['notes'].items():
        assert (ROOT / name).read_text().startswith(record['text']), name
    for name, digest in before['protected_inputs'].items():
        assert sha(ROOT / name) == digest, name
    result['protected_inputs_unchanged'] = len(before['protected_inputs'])
    result['protected_inputs'] = before['protected_inputs']
    result['notes_append_only'] = True
    result['remaining_checks'] = ['Two focused gene validations', 'Module focused validation',
                                  'Three generated history validations', 'Gene and module renders',
                                  'Root decides whether a current capacity rerun is warranted']
    (HERE / 'preservation.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in {'documents', 'protected_inputs'}}))


if __name__ == '__main__':
    main()
