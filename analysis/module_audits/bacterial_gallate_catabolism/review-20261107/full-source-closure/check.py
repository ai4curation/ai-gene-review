"""Read-only verification; does not rewrite seals or regenerate source material."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent


def load(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    inputs = load(OUT / 'inputs.json')
    for path, expected in inputs.items():
        assert not path.startswith('.cache/'), path
        assert sha(ROOT / path) == expected, path
    provenance = load(OUT / 'manifest-provenance.json')
    for name, item in provenance['manifests'].items():
        assert sha(OUT / name) == item['sha256'], name
    for item in provenance['claims']:
        if item['disposition'].startswith('root-owned'):
            assert item['path'] in provenance['excluded_shared_paths']
            continue
        assert inputs[item['path']] == item['current']
        if item['disposition'] == 'authorized successor':
            correction = provenance['supersessions'][item['path']]
            assert correction['before_sha256'] == item['expected']
            assert correction['after_sha256'] == item['current']
        else:
            assert item['expected'] == item['current']
    aliases = load(OUT / 'aliases.json')
    for item in aliases.values():
        assert sha(ROOT / item['path']) == item['sha256']
    graph = load(OUT / 'citation-graph.json')
    for edge in graph['edges']:
        assert edge['source'] in inputs and edge['target'] in inputs, edge
    # Deliberately do not pretend that transitive provider bibliography is closed.
    missing = graph['missing']
    assert missing == load(OUT / 'unresolved-provider-leads.json')['entries']
    assert all('deep-research' in item['source'] for item in missing)
    baseline = load(OUT.parent / 'science-consultation/baseline.json')
    members = load(OUT / 'members.json')
    assert len(members) == 12
    row_count = new_count = retired_count = 0
    for member in members:
        path = member['review_path']
        old = yaml.safe_load(baseline['documents'][path]['text'])
        current = yaml.safe_load((ROOT / path).read_text())
        assert old['id'] == current['id'] == member['accession'], path
        before = old['existing_annotations']
        after = current['existing_annotations']
        assert len(before) == len(after)
        for left, right in zip(before, after, strict=True):
            assert {k: v for k, v in left.items() if k != 'review'} == {k: v for k, v in right.items() if k != 'review'}, path
            assert (left['review']['action'] == 'NEW') == (right['review']['action'] == 'NEW'), path
            row_count += 1
            new_count += right['review']['action'] == 'NEW'
            retired_count += bool(right.get('retired'))
    assert row_count == 60 and new_count == 9
    handoff = OUT / 'handoff.json'
    if handoff.exists():
        for path, expected in load(handoff)['files'].items():
            assert sha(ROOT / path) == expected, path
        assert load(handoff)['source_dependencies'] == inputs
    print(json.dumps({
        'status': 'PASS', 'current_inputs': len(inputs),
        'published_claims_checked': len(provenance['claims']),
        'member_comparator_reviews': len(members), 'ordered_rows': row_count,
        'historical_NEW': new_count, 'retired_rows': retired_count,
        'resolved_citation_edges': len(graph['edges']),
        'Reactome_edges': sum(e['kind'] == 'Reactome citation' for e in graph['edges']),
        'unadopted_external_provider_citation_occurrences': len(missing),
        'unadopted_external_provider_PMIDs': len({e['citation'] for e in missing}),
        'private_cache_required': False,
        'claim_limit': 'Current scoped evidence closure PASS; transitive external provider bibliography is explicitly incomplete.',
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
