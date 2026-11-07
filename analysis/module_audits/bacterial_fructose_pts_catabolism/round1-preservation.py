"""Verify unchanged source rows/actions and mechanism after review follow-up."""
from pathlib import Path
from copy import deepcopy
import hashlib
import json
import re
import subprocess
import yaml

ROOT = Path(__file__).resolve().parents[3]
AUDIT = Path(__file__).resolve().parent
HEAD = '6342c397981015f8463fd8c09a4c64d96d1a3ffc'
MODULE = 'modules/bacterial_fructose_pts_catabolism.yaml'


def git_bytes(path):
    return subprocess.check_output(['git', 'show', f'{HEAD}:{path}'], cwd=ROOT)


def payloads(review):
    return [{k: v for k, v in row.items() if k != 'review'}
            for row in review['existing_annotations']]


def representatives(value):
    if isinstance(value, dict):
        yield from value.get('representative_members', [])
        for v in value.values():
            yield from representatives(v)
    elif isinstance(value, list):
        for v in value:
            yield from representatives(v)


def main():
    prior = json.loads((AUDIT / 'final-panel-preservation.json').read_text())
    protected = set(prior['protected_files'])
    rows = {}; names = {}; refs = set()
    tracked = set(subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', HEAD],
                                        cwd=ROOT, text=True).splitlines())
    for path in prior['reviews']:
        old = yaml.safe_load(git_bytes(path)); new = yaml.safe_load((ROOT / path).read_text())
        assert payloads(old) == payloads(new), path
        assert [a['review']['action'] for a in old['existing_annotations']] == [a['review']['action'] for a in new['existing_annotations']], path
        assert [(r['id'], r['title']) for r in old['references']] == [(r['id'], r['title']) for r in new['references']], path
        rows[path] = dict(rows=len(payloads(new)), payload_order_actions_and_reference_ids_titles_preserved=True,
                         sha256=hashlib.sha256((ROOT / path).read_bytes()).hexdigest())
        folder = str(Path(path).parent) + '/'
        protected.update(p for p in tracked if p.startswith(folder) and
                         any(x in p for x in ['-uniprot.', '-goa.', '-deep-research', '-citations.']))
        refs.update(r['id'] for r in old['references'] if r['id'].startswith('PMID:'))
        up = Path(path).with_name(Path(path).name.replace('-ai-review.yaml', '-uniprot.txt'))
        names[old['id']] = re.search(r'^DE   (?:RecName|SubName): Full=(.*?)(?: \{|;)',
                                    (ROOT / up).read_text(), re.M).group(1)
    old = yaml.safe_load(git_bytes(MODULE)); new = yaml.safe_load((ROOT / MODULE).read_text())
    refs.update(r['id'] for r in old['references'] if r['id'].startswith('PMID:'))
    for ref in refs:
        p = 'publications/' + ref.replace(':', '_') + '.md'
        if p in tracked:
            protected.add(p)
    protected.update(p for p in tracked if p.startswith('modules/bacterial_fructose_pts_catabolism-deep-research'))
    source_hashes = {}
    for p in sorted(protected):
        data = (ROOT / p).read_bytes(); assert data == git_bytes(p), p
        source_hashes[p] = hashlib.sha256(data).hexdigest()
    old_reps = list(representatives(old)); new_reps = list(representatives(new))
    assert len(old_reps) == len(new_reps)
    changed_labels = 0
    for a, b in zip(old_reps, new_reps):
        assert a['term']['id'] == b['term']['id']
        acc = b['term']['id'].split(':')[1]
        assert b['term']['label'] == names[acc], b
        changed_labels += a['term']['label'] != b['term']['label']
    expected = deepcopy(old)
    for r in representatives(expected):
        r['term']['label'] = names[r['term']['id'].split(':')[1]]
    expected['notes'] = new['notes']
    removed = expected['module']['knowledge_gaps'].pop(0)
    assert removed['gap_kind'] == ['ONTOLOGY']
    assert removed['gap_statement'] in new['notes'] and removed['boundary'] in new['notes']
    assert expected == new, 'Unexpected module mechanism or metadata change'
    fixture_path = 'analysis/module_audits/bacterial_fructose_pts_catabolism/capacity-fixtures.yaml'
    original_fixture = yaml.safe_load(git_bytes(fixture_path))
    fixture = yaml.safe_load((ROOT / fixture_path).read_text())
    expected_fixture = deepcopy(original_fixture)
    refreshed = 0
    for protein in expected_fixture['proteins'].values():
        if 'review' in protein:
            sha = hashlib.sha256((ROOT / protein['review']).read_bytes()).hexdigest()
            refreshed += sha != protein['review_sha256']
            protein['review_sha256'] = sha
    assert expected_fixture == fixture, 'Unexpected activity/domain/system fixture change'
    assert refreshed == 5
    # No need to revise the current preferred DEIRA authored label.
    path = 'genes/DEIRA/DR_B0074/DR_B0074-ai-review.yaml'
    assert (ROOT / path).read_bytes() == git_bytes(path)
    snapshot = ROOT / '.cache/module-audit-logs/fructose-20261107/round1/before.json'
    if snapshot.exists():
        before = json.loads(snapshot.read_text())
        for path, sha in before['protected'].items():
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == sha, path
    result = dict(status='PASS', reviewed_head=HEAD, reviews=len(rows),
                  annotation_rows=sum(r['rows'] for r in rows.values()), added_rows=0, removed_rows=0,
                  changed_actions=0, original_payload_and_order_preserved=True,
                  reference_ids_and_titles_preserved=True,
                  module_mechanism_and_remaining_biological_gap_unchanged=True,
                  fixture_biological_claims_unchanged=True, refreshed_review_hashes=refreshed,
                  representative_occurrences_checked=len(new_reps), corrected_representative_occurrences=changed_labels,
                  deira_authored_label_and_review_unchanged=True,
                  protected_source_count=len(source_hashes), protected_sha256=source_hashes, reviews_sha256=rows,
                  module_sha256=hashlib.sha256((ROOT / MODULE).read_bytes()).hexdigest())
    (AUDIT / 'round1-preservation.yaml').write_text(yaml.safe_dump(result, sort_keys=False))
    print({k: v for k, v in result.items() if k not in ['protected_sha256', 'reviews_sha256']})


if __name__ == '__main__':
    main()
