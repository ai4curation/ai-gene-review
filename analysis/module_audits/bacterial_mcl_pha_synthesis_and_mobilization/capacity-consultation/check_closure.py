"""Read-only verification of released sources, ordered rows and quoted evidence.

Only this consultation's output is written. Earlier scripts are not invoked because
some regenerate their frozen receipts. --capture records final inputs once all
seven consultations are released; subsequent invocations verify that snapshot.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
AUDIT = HERE.parent
MODULE = ROOT / 'modules/bacterial_mcl_pha_synthesis_and_mobilization.yaml'
RELEASES = ['literature', 'gpo1', 'class-i', 'psepk', 'pseae', 'cupnh', 'family']


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(row):
    return {k: v for k, v in row.items() if k not in {'review', 'retired'}}


def nodes(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from nodes(child)
    elif isinstance(value, list):
        for child in value:
            yield from nodes(child)


def resolve(ref):
    if ref.startswith('PMID:'):
        return ROOT / 'publications' / (ref.replace(':', '_') + '.md')
    if ref.startswith('file:'):
        rel = ref[5:]
        for candidate in [ROOT / 'genes' / rel, ROOT / rel]:
            if candidate.is_file():
                return candidate
        raise AssertionError(f'Unresolved local source {ref}')
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--capture', action='store_true')
    args = parser.parse_args()
    snapshot = HERE / 'input-closure.json'
    hashes = {}

    def record(path):
        rel = str(path.relative_to(ROOT))
        hashes[rel] = sha(path)
        return rel

    manifests = {}
    for name in RELEASES:
        path = AUDIT / f'{name}-consultation/handoff.json'
        assert path.exists(), f'Awaiting frozen release: {path}'
        data = json.loads(path.read_text())
        manifests[record(path)] = sha(path)
        receipt = AUDIT / f'root-{name}-handoff-receipt.json'
        receipt_data = json.loads(receipt.read_text())
        assert receipt_data['sha256'] == sha(path), receipt
        record(receipt)
        for rel, expected in data['files'].items():
            assert sha(ROOT / rel) == expected, f'Released file changed: {rel}'
            record(ROOT / rel)

    baselines = ['baseline.json', 'additional-seed-baseline.json', 'cupnh-seed-baseline.json']
    ordered = historical = new_count = 0
    lifecycle = []
    reviews = {}
    protected = {}
    for filename in baselines:
        baseline_path = AUDIT / filename
        baseline = json.loads(baseline_path.read_text())
        record(baseline_path)
        for rel, expected in baseline['protected_files_sha256'].items():
            assert sha(ROOT / rel) == expected, rel
            protected[record(ROOT / rel)] = expected
        for rel, prior in baseline.get('reviews', baseline.get('genes', {})).items():
            old = prior['document']['existing_annotations']
            current = yaml.safe_load((ROOT / rel).read_text())
            assert current['status'] == 'COMPLETE', rel
            rows = current['existing_annotations']
            assert [payload(r) for r in rows[:len(old)]] == [payload(r) for r in old], rel
            ordered += len(old)
            for index, (before, after) in enumerate(zip(old, rows, strict=False)):
                if before['review']['action'] == 'NEW':
                    historical += 1
                    assert after['review']['action'] == 'NEW'
                if before.get('retired', False) != after.get('retired', False):
                    assert rel == 'genes/PSEPK/phaZ/phaZ-ai-review.yaml' and index == 2
                    assert after.get('retired') is True
                    lifecycle.append({'path': rel, 'index': index, 'retired': True,
                                      'action_preserved': 'NEW'})
            added = rows[len(old):]
            if added:
                assert rel == 'genes/PSEAE/phaG/phaG-ai-review.yaml' and len(added) == 1
                assert added[0]['term']['id'] == 'GO:0016747'
                assert added[0]['evidence_type'] == 'IC' and added[0]['review']['action'] == 'NEW'
            new_count += len(added)
            reviews[rel] = {'original_rows': len(old), 'added_rows': len(added),
                            'actions': dict(Counter(r['review']['action'] for r in rows)),
                            'retired_rows': sum(bool(r.get('retired')) for r in rows)}
            record(ROOT / rel)
    assert ordered == 23 and historical == 5 and new_count == 1 and len(lifecycle) == 1

    # Hash every primary in the independent fixture, even if absent from a core
    # activity's own citations. This prevents role-list-only provenance omissions.
    fixtures = yaml.safe_load((HERE / 'fixtures.yaml').read_text())
    for member in fixtures['members'].values():
        for ref in member['sources']:
            record(resolve(ref))
    record(MODULE)
    assert yaml.safe_load(MODULE.read_text())['status'] == 'COMPLETE'
    record(ROOT / 'pages/modules/bacterial_mcl_pha_synthesis_and_mobilization.html')
    for name in ['module-semantic-final.log', 'module-render-final.log', 'module-history.log']:
        record(ROOT / '.cache/module-audit-logs/mcl-pha-20261107' / name)
    record(ROOT / 'src/ai_gene_review/module_logic.py')
    for path in (ROOT / 'history/modules/bacterial_mcl_pha_synthesis_and_mobilization').glob('*.yaml'):
        record(path)

    # Follow local/PMID references from the module and released curated YAML.
    queue = [MODULE] + [ROOT / p for p in hashes if p.endswith('-review.yaml')]
    visited = set()
    while queue:
        path = queue.pop()
        if path in visited:
            continue
        visited.add(path)
        data = yaml.safe_load(path.read_text())
        for node in nodes(data):
            for key in ['id', 'source_id', 'reference_id']:
                ref = node.get(key)
                if not isinstance(ref, str):
                    continue
                source = resolve(ref)
                if source:
                    record(source)
                    if source.suffix == '.yaml' and source not in visited:
                        queue.append(source)

    # Independently recheck the frozen literature excerpts, including external
    # full-text artifacts. Hash receipts are not a substitute for substring checks.
    quotes = []
    ledger_path = AUDIT / 'literature-consultation/reference-ledger.yaml'
    for entry in yaml.safe_load(ledger_path.read_text()):
        path = ROOT / entry['source_path']
        assert sha(path) == entry['source_sha256']
        record(path)
        text = ' '.join(path.read_text().split())
        for finding in entry['findings']:
            assert ' '.join(finding['supporting_text'].split()) in text, entry['id']
            quotes.append({'reference': entry['id'], 'source': entry['source_path'], 'matched': True})
    for pmid, quote in [('10612741', 'These data strongly suggested that R. eutropha PHA synthase accepts'),
                        ('35341893', 'without any synthase modification')]:
        path = resolve(f'PMID:{pmid}')
        assert quote in ' '.join(path.read_text().split())
        quotes.append({'reference': f'PMID:{pmid}', 'source': record(path), 'matched': True})
    # Verify acquisition bytes closed by previous consultations, without treating
    # failed downloads as successfully accessed publications.
    for dirname in ['literature', 'class-i']:
        path = AUDIT / f'{dirname}-consultation/source-closure.json'
        for rel, expected in json.loads(path.read_text()).items():
            assert sha(ROOT / rel) == expected, rel
            record(ROOT / rel)

    closure = {'manifests': manifests, 'files': dict(sorted(hashes.items()))}
    if args.capture:
        assert not snapshot.exists(), 'Refuse to overwrite frozen input snapshot'
        snapshot.write_text(json.dumps(closure, indent=2, sort_keys=True) + '\n')
    else:
        assert json.loads(snapshot.read_text()) == closure, 'Input closure changed'
    result = {'status': 'PASS', 'input_closure_sha256': sha(snapshot),
              'verified_releases': len(manifests), 'input_files': len(hashes),
              'protected_sources': len(protected), 'original_ordered_rows': ordered,
              'historical_new': historical, 'added_new': new_count,
              'authorized_lifecycle_changes': lifecycle, 'reviews': reviews,
              'independently_rechecked_quotes': quotes,
              'limitations': 'Source integrity and exact quotation do not prove biological interpretation. Access scopes and strain/construct limitations remain those recorded in the source ledgers.'}
    (HERE / 'closure-results.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ['reviews', 'independently_rechecked_quotes']}))


if __name__ == '__main__':
    main()
