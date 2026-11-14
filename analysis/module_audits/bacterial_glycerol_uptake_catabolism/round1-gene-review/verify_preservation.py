"""Verify ordered annotation payloads, allowed action changes and protected sources."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    baseline = json.loads((HERE / 'frozen-inputs.json').read_text())
    rows = inherited_new = 0
    changes = []
    reviews = []
    for relative, original in baseline['reviews'].items():
        current = yaml.safe_load((ROOT / relative).read_text())
        annotations = current['existing_annotations']
        assert [{k: v for k, v in a.items() if k != 'review'} for a in annotations] == original['payloads'], relative
        assert current['status'] == original['status'], relative
        for index, (annotation, before) in enumerate(zip(annotations, original['actions'])):
            after = annotation['review']['action']
            if before == 'NEW':
                assert after == before, relative
                inherited_new += 1
            if before != after:
                changes.append({'path': relative, 'index': index, 'term': annotation['term']['id'], 'before': before, 'after': after})
        rows += len(annotations)
        reviews.append({'path': relative, 'rows': len(annotations), 'sha256': sha(ROOT / relative)})
    assert changes == baseline['allowed_action_changes'], changes
    for relative, expected in baseline['protected_sha256'].items():
        assert sha(ROOT / relative) == expected, relative
    for relative, original in baseline['notes'].items():
        data = (ROOT / relative).read_bytes()
        assert hashlib.sha256(data[:original['bytes']]).hexdigest() == original['sha256'], relative
    result = {'status': 'PASS', 'baseline_head': baseline['head'], 'reviews': reviews,
              'ordered_original_rows': rows, 'historical_NEW_preserved': inherited_new,
              'added_NEW': 0, 'action_changes': changes,
              'protected_sources_unchanged': len(baseline['protected_sha256']),
              'notes_original_prefixes_preserved': True}
    (HERE / 'preservation.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
