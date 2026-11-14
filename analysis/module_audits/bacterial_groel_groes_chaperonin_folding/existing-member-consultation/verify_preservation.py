"""Read-only preservation audit against the parent's pre-edit immutable snapshot.
Run from the repository root: uv run python <this script>
"""
from pathlib import Path
import collections
import hashlib
import json
import subprocess
import yaml

BASELINE = Path('analysis/module_audits/bacterial_groel_groes_chaperonin_folding/existing-members-baseline.json')
CACHE = Path('.cache/module-audit-logs/groel-20261107/existing-review')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def audit():
    baseline = json.loads(BASELINE.read_text())
    pre_edit = json.loads((CACHE / 'pre-edit.json').read_text()) if (CACHE / 'pre-edit.json').exists() else {}
    members = []
    for path, original in baseline['reviews'].items():
        old = yaml.safe_load(original['text'])
        current = yaml.safe_load(Path(path).read_text())
        rows = current['existing_annotations']
        before = old['existing_annotations']
        payloads = [{k: v for k, v in row.items() if k != 'review'} for row in rows]
        original_payloads = [{k: v for k, v in row.items() if k != 'review'} for row in before]
        assert payloads == original_payloads, f'Changed ordered annotation payload: {path}'
        assert current['id'] == old['id'] and current['taxon'] == old['taxon'], path
        inherited_new = [i for i, row in enumerate(before) if row['review']['action'] == 'NEW']
        assert all(rows[i]['review']['action'] == 'NEW' for i in inherited_new), path
        assert current['status'] == 'COMPLETE', path
        assert not any(line.rstrip() != line for line in Path(path).read_text().splitlines()), path
        notes_path = path.replace('-ai-review.yaml', '-notes.md')
        historical_notes = subprocess.run(['git', 'show', f"{baseline['head']}:{notes_path}"], capture_output=True, text=True)
        old_notes = pre_edit.get(path, {}).get('notes_text')
        if historical_notes.returncode == 0:
            assert old_notes is None or old_notes == historical_notes.stdout, notes_path
            old_notes = historical_notes.stdout
        if old_notes is not None:
            assert Path(notes_path).read_text().startswith(old_notes), path
        members.append({
            'path': path, 'review_sha256': sha(path), 'original_review_sha256': original['sha256'],
            'original_rows': len(before), 'current_rows': len(rows),
            'ordered_payload_sha256': hashlib.sha256(json.dumps(payloads, sort_keys=True).encode()).hexdigest(),
            'inherited_new_indexes': inherited_new, 'added_rows': 0,
            'actions': dict(sorted(collections.Counter(a['review']['action'] for a in rows).items())),
            'action_changes': [{'index': i, 'term': a['term']['id'], 'from': b['review']['action'], 'to': a['review']['action']}
                               for i, (a, b) in enumerate(zip(rows, before)) if a['review']['action'] != b['review']['action']],
        })
    protected = []
    for path, old_sha in baseline['protected_sources'].items():
        current_sha = sha(path)
        assert current_sha == old_sha, f'Protected source changed: {path}'
        protected.append({'path': path, 'original_sha256': old_sha, 'current_sha256': current_sha, 'unchanged': True})
    report = {'baseline': str(BASELINE), 'baseline_sha256': sha(BASELINE), 'baseline_head': baseline['head'],
              'reviews': members, 'historical_rows': sum(x['original_rows'] for x in members),
              'current_rows': sum(x['current_rows'] for x in members),
              'inherited_new': sum(len(x['inherited_new_indexes']) for x in members),
              'added_new': 0, 'protected_file_count': len(protected), 'protected_sources': protected,
              'result': 'PASS'}
    assert report['historical_rows'] == 121 and report['protected_file_count'] == 67
    return report


if __name__ == '__main__':
    print(json.dumps(audit(), indent=2))
