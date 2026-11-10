"""Check the published ImuABC closure and a notes-only round2 family fix."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
AUDIT = Path(__file__).resolve().parent
CHANGED = 'interpro/panther/PTHR33516/PTHR33516-review.yaml'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    baseline = json.loads((AUDIT / 'baseline.json').read_text())
    rows = 0
    historical_new = 0
    retired = 0
    for name, expected in baseline['reviews'].items():
        current = yaml.safe_load((ROOT / name).read_text())
        annotations = current.get('existing_annotations', [])
        payloads = [{key: value for key, value in row.items() if key != 'review'}
                    for row in annotations]
        assert payloads == expected['payloads'], name
        assert [row['review']['action'] for row in annotations] == expected['actions'], name
        assert digest(ROOT / name) == expected['sha256'], name
        rows += len(annotations)
        historical_new += sum(row['review']['action'] == 'NEW' for row in annotations)
        retired += sum(bool(row.get('retired')) for row in annotations)
    for name, before in baseline['family_documents'].items():
        after = yaml.safe_load((ROOT / name).read_text())
        if name == CHANGED:
            assert {k: v for k, v in before.items() if k != 'notes'} == {
                k: v for k, v in after.items() if k != 'notes'
            }
            assert before['notes'] != after['notes']
            assert 'wrong for a narrow-regulon paralog' not in after['notes']
            assert 'narrower regulon is not a counterexample' in after['notes']
        else:
            assert before == after, name
    for name, expected in baseline['protected_sources_sha256'].items():
        assert digest(ROOT / name) == expected, name
    for name, expected in baseline['published_closure_sha256'].items():
        if name != CHANGED:
            assert digest(ROOT / name) == expected, name
    result = {
        'result': 'PASS', 'head_baseline': baseline['head'],
        'gene_reviews_unchanged': len(baseline['reviews']), 'ordered_rows': rows,
        'historical_active_NEW_unchanged': historical_new,
        'retired_rows_unchanged': retired, 'new_rows': 0, 'deleted_rows': 0,
        'protected_sources_unchanged': len(baseline['protected_sources_sha256']),
        'published_closure_unchanged_except_family_notes': len(baseline['published_closure_sha256']),
        'family_documents': len(baseline['family_documents']),
        'all_node_and_term_assessments_unchanged': True,
    }
    (AUDIT / 'preservation.json').write_text(json.dumps(result, indent=2) + '\n')
    print(result)


if __name__ == '__main__':
    main()
