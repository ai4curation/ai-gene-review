"""Verify the frozen two-gene inputs without refreshing any source."""
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[4]
BASELINE = ROOT / 'analysis/module_audits/bacterial_heptaprenylglyceryl_ether_lipid/baseline.json'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    baseline = json.loads(BASELINE.read_text())
    result = {'base_head': baseline['base_head'], 'baseline_sha256': digest(BASELINE),
              'reviews': {}, 'protected_sources': {}, 'historical_rows': 0,
              'inherited_new': 0, 'added_rows': 0}
    for rel, frozen in baseline['reviews'].items():
        path = ROOT / rel
        current = yaml.safe_load(path.read_text())
        original = yaml.safe_load(subprocess.check_output(
            ['git', 'show', f"{baseline['base_head']}:{rel}"], cwd=ROOT, text=True))
        rows = current['existing_annotations']
        payloads = [{k: v for k, v in row.items() if k != 'review'} for row in rows]
        assert payloads == frozen['ordered_payloads'], f'Payload/order changed: {rel}'
        old_actions = [row['review']['action'] for row in original['existing_annotations']]
        new_actions = [row['review']['action'] for row in rows]
        inherited = [i for i, action in enumerate(old_actions) if action == 'NEW']
        assert all(new_actions[i] == 'NEW' for i in inherited), rel
        notes = rel.replace('-ai-review.yaml', '-notes.md')
        old_notes = subprocess.check_output(
            ['git', 'show', f"{baseline['base_head']}:{notes}"], cwd=ROOT)
        assert (ROOT / notes).read_bytes().startswith(old_notes), f'Notes not append-only: {notes}'
        assert current['status'] == 'COMPLETE', rel
        result['reviews'][rel] = {
            'sha256': digest(path), 'original_rows': len(rows),
            'ordered_non_review_payloads_unchanged': True,
            'inherited_new_indices': inherited, 'notes_append_only': True,
            'actions': dict(Counter(new_actions)),
            'action_changes': [{'index': i, 'term': rows[i]['term']['id'],
                                'before': old, 'after': new}
                               for i, (old, new) in enumerate(zip(old_actions, new_actions))
                               if old != new]}
        result['historical_rows'] += len(rows)
        result['inherited_new'] += len(inherited)
    for rel, expected in baseline['protected_sources'].items():
        actual = digest(ROOT / rel)
        assert actual == expected, f'Protected source changed: {rel}'
        result['protected_sources'][rel] = actual
    result['protected_source_count'] = len(result['protected_sources'])
    result['result'] = 'PASS'
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
