"""Compare original payloads while checking explicitly recorded source additions."""
from copy import deepcopy
import json


def original_payloads(root, audit, member, document):
    rows = [{k: deepcopy(v) for k, v in row.items() if k != 'review'}
            for row in document['existing_annotations']]
    proof = json.loads((audit / 'approved-main7-integration.json').read_text())
    entry = proof.get('upstream_qualifier_integration', {}).get(member['review_path'])
    if not entry:
        return rows
    original = [row['payload'] for row in member['annotations']]
    seen = set()
    for change in entry['qualifier_additions']:
        index = change['target_index']
        assert index not in seen, (member['review_path'], index)
        seen.add(index)
        assert rows[index]['qualifier'] == change['qualifier'], (member['review_path'], index)
        del rows[index]['qualifier']
        # Nothing besides this exact upstream qualifier may be discounted.
        assert rows[index] in original, (member['review_path'], index)
    return rows
