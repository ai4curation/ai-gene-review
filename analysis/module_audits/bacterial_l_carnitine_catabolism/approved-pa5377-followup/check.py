"""Read-only exact preservation check for the PA5377 COS follow-up."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
AUDIT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    baseline = json.loads((AUDIT / 'baseline.json').read_text())
    review = 'genes/PSEAE/PA5377/PA5377-ai-review.yaml'
    notes = 'genes/PSEAE/PA5377/PA5377-notes.md'
    html = 'genes/PSEAE/PA5377/PA5377-ai-review.html'
    old = yaml.safe_load(baseline['review_text'])
    new = yaml.safe_load((ROOT / review).read_text())
    expected_changes = {'existing_annotations', 'references', 'suggested_questions', 'suggested_experiments'}
    assert {key for key in old.keys() | new.keys() if old.get(key) != new.get(key)} == expected_changes
    assert len(old['existing_annotations']) == len(new['existing_annotations'])
    for i, (before, after) in enumerate(zip(old['existing_annotations'], new['existing_annotations'], strict=True)):
        assert {k: v for k, v in before.items() if k != 'review'} == {k: v for k, v in after.items() if k != 'review'}
        if i != 21:
            assert before == after
    row = new['existing_annotations'][21]
    assert row['term']['id'] == 'GO:1901682'
    assert row['original_reference_id'] == 'PMID:23763788'
    assert row['review']['action'] == 'KEEP_AS_NON_CORE'
    donor = yaml.safe_load((ROOT / 'genes/PSEAE/cbcW/cbcW-ai-review.yaml').read_text())
    assert row == donor['existing_annotations'][21]
    old_refs = {r['id']: r for r in old['references']}
    new_refs = {r['id']: r for r in new['references']}
    for key in old_refs.keys() - {'PMID:23763788'}:
        assert old_refs[key] == new_refs[key]
    assert len(new_refs) == len(old_refs) + 1
    for path, expected in baseline['files'].items():
        if path not in {review, notes, html}:
            assert sha(ROOT / path) == expected, path
    prior = json.loads((AUDIT / 'adjudication-receipt.json').read_text())
    for path, expected in prior['inputs'].items():
        if path != review:
            assert sha(ROOT / path) == expected, path
    assert (ROOT / notes).read_text().startswith(baseline['notes_text'] or '')
    assert 'CosX-dependent COS entry' in (ROOT / html).read_text()
    if (AUDIT / 'handoff.json').exists():
        handoff = json.loads((AUDIT / 'handoff.json').read_text())
        for path, expected in handoff['files'].items():
            assert sha(ROOT / path) == expected, path
    print(json.dumps({'status': 'PASS', 'ordered_rows': len(new['existing_annotations']),
                      'historical_NEW': sum(r['review']['action'] == 'NEW' for r in new['existing_annotations']),
                      'only_changed_annotation_index': 21,
                      'all_payloads_qualifiers_lifecycle_preserved': True,
                      'core_and_other_decisions_unchanged': True}, indent=2))


if __name__ == '__main__':
    main()
