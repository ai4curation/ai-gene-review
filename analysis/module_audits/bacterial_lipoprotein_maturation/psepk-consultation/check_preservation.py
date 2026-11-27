"""Check ordered machine payloads, inherited proposals, and frozen raw/source files."""
from collections import Counter
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import json

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def payloads(document):
    return [{k: v for k, v in row.items() if k != 'review'}
            for row in document['existing_annotations']]


def check_rows(before, document):
    assert payloads(document) == before['ordered_payloads'], 'ordered source payload changed'
    for old, current in zip(before['actions'], document['existing_annotations']):
        if old == 'NEW':
            assert current['review']['action'] == 'NEW', 'inherited active proposal changed'


def main():
    baseline = yaml.safe_load((HERE / 'baseline.yaml').read_text())
    root_baseline = json.loads((HERE.parent / 'baseline.json').read_text())
    protected = root_baseline['protected_files_sha256'] | baseline['protected_sha256']
    for name, expected in protected.items():
        assert digest(ROOT / name) == expected, name
    actions = Counter()
    changes = []
    total = 0
    new = 0
    documents = {}
    for name, before in baseline['reviews'].items():
        document = yaml.safe_load((ROOT / name).read_text())
        documents[name] = document
        check_rows(before, document)
        for index, (old, row) in enumerate(zip(before['actions'], document['existing_annotations'])):
            action = row['review']['action']
            actions[action] += 1
            total += 1
            new += old == 'NEW'
            if old != action:
                changes.append({'path': name, 'index': index, 'term': row['term'],
                                'before': old, 'after': action})
    # These tests alter only independent in-memory copies, never source files.
    first = next(iter(documents))
    fault_cases = {}
    fault = deepcopy(documents[first])
    fault['existing_annotations'].reverse()
    fault_cases['reordered_original_rows'] = (first, fault)
    fault = deepcopy(documents[first])
    fault['existing_annotations'][0]['term']['id'] = 'in-memory-corruption'
    fault_cases['changed_original_payload'] = (first, fault)
    name = next(n for n, b in baseline['reviews'].items() if 'NEW' in b['actions'])
    fault = deepcopy(documents[name])
    fault['existing_annotations'].pop(baseline['reviews'][name]['actions'].index('NEW'))
    fault_cases['deleted_inherited_proposal'] = (name, fault)
    detected = []
    for label, (name, fault) in fault_cases.items():
        try:
            check_rows(baseline['reviews'][name], fault)
        except AssertionError:
            detected.append(label)
        else:
            raise AssertionError('Undetected fault: ' + label)
    result = {'status': 'PASS', 'ordered_rows': total, 'historical_NEW_preserved': new,
              'new_rows_added': 0, 'retirements_added': 0, 'actions': dict(actions),
              'action_changes': changes, 'protected_files_verified': len(protected),
              'protected_sha256': protected, 'faults_detected': detected,
              'new_publications_sha256': {f'publications/PMID_{p}.md': digest(ROOT / f'publications/PMID_{p}.md')
                                         for p in ['26912896', '17416655']},
              'paint_scope': 'All three target leaves absent from cached trees; lineage loss checks unavailable.'}
    (HERE / 'preservation-results.yaml').write_text(yaml.safe_dump(result, sort_keys=False))
    print({k: result[k] for k in ['status', 'ordered_rows', 'historical_NEW_preserved', 'protected_files_verified', 'actions']})


if __name__ == '__main__':
    main()
