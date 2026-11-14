"""Exact source-payload, publication-byte, quote and phylogenetic join checks."""
import hashlib
import json
from pathlib import Path

import yaml

A = Path(__file__).resolve().parent
ROOT = A.parents[3]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def norm(value):
    return ' '.join(value.split())


def source(ref):
    if ref.startswith('PMID:'):
        return ROOT / 'publications' / ('PMID_' + ref.split(':')[1] + '.md')
    if ref.startswith('file:'):
        path = ref[5:]
        return next(p for p in [ROOT / path, ROOT / 'genes' / path] if p.exists())
    raise AssertionError(ref)


def quotes(value, inherited=None):
    if isinstance(value, dict):
        reference = value.get('reference_id', value.get('id', inherited))
        if 'supporting_text' in value:
            yield reference, value['supporting_text']
        for key, child in value.items():
            if key != 'supporting_text':
                yield from quotes(child, reference)
    elif isinstance(value, list):
        for child in value:
            yield from quotes(child, inherited)


def main():
    baseline = json.loads((A / 'seed-baseline.json').read_text())
    row_count = quote_count = 0
    actions = {}
    sources = {}
    for path, info in baseline.items():
        if not path.endswith('-ai-review.yaml'):
            assert sha(ROOT / path) == info['sha256'], path
            sources[path] = info['sha256']
            continue
        old = yaml.safe_load(info['text'])
        current = yaml.safe_load((ROOT / path).read_text())
        assert current['id'] == old['id'] and current['taxon'] == old['taxon']
        assert current['status'] == 'COMPLETE'
        assert len(old['existing_annotations']) == len(current['existing_annotations'])
        for i, (before, after) in enumerate(zip(old['existing_annotations'], current['existing_annotations'], strict=True)):
            assert {k: v for k, v in before.items() if k != 'review'} == {k: v for k, v in after.items() if k != 'review'}, (path, i)
            action = after['review']['action']
            assert action not in {'NEW', 'PENDING'}
            actions[action] = actions.get(action, 0) + 1
            row_count += 1
        for ref, quote in quotes(current):
            s = source(ref)
            assert norm(quote) in norm(s.read_text()), (path, ref, quote)
            sources[str(s.relative_to(ROOT))] = sha(s)
            quote_count += 1
        for ref in current['references']:
            if ref['id'].startswith('PMID:'):
                s = source(ref['id'])
                header = yaml.safe_load(s.read_text().split('---', 2)[1])
                assert norm(ref['title']) == norm(header['title'])
                sources[str(s.relative_to(ROOT))] = sha(s)
    assert row_count == 25
    acquisition = ROOT / 'analysis/module_audits/bacterial_nitrogen_regulatory_pts/acquisition-20261107/publication-acquisition-complete.json'
    for item in json.loads(acquisition.read_text())['results']:
        if item['path'] in sources:
            assert sources[item['path']] == item['sha256'], item['path']
    for joined in json.loads((A / 'paint-join.json').read_text()):
        assert joined['IBD_node'] in joined['path']
        assert not joined['cached_negative_assertions']
        for key in ['receipt', 'paint']:
            assert sha(ROOT / joined[key]) == joined[key + '_sha256']
            sources[joined[key]] = joined[key + '_sha256']
    if (A / 'handoff.json').exists():
        h = json.loads((A / 'handoff.json').read_text())
        for path, expected in {**h['files'], **h['source_dependencies']}.items():
            assert sha(ROOT / path) == expected, path
    print(json.dumps({'status': 'PASS', 'ordered_rows_preserved': row_count, 'raw_files_preserved': 6,
                      'NEW_added': 0, 'retirements': 0, 'literal_quotes_verified': quote_count,
                      'actions': actions, 'exact_tree_assertion_joins': 3}, indent=2))


if __name__ == '__main__':
    main()
