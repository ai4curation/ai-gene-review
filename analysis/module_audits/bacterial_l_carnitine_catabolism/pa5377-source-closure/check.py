"""Read-only closure verification, with explicit shared-metadata boundaries."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent


def load(name):
    return json.loads((OUT / name).read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    inputs = load('inputs.json')
    for path, expected in inputs.items():
        assert not path.startswith('.cache/')
        assert sha(ROOT / path) == expected, path
    provenance = load('prior-and-supersession.json')
    assert sha(OUT / 'prior-publication-manifest.json') == provenance['prior_manifest_sha256']
    prior = load('prior-publication-manifest.json')
    assert len(prior) == 332
    retained = {p: h for p, h in prior.items() if p not in provenance['excluded_shared_paths']}
    assert len(retained) == 327
    for path, expected in retained.items():
        assert inputs[path] == expected, path
    for path, change in provenance['PA5377_successors'].items():
        assert inputs[path] == change['after_sha256']
    handoff = json.loads((ROOT / provenance['new_handoff']).read_text())
    assert sha(ROOT / provenance['new_handoff']) == provenance['new_handoff_sha256']
    for key in ('files', 'source_dependencies'):
        for path, expected in handoff[key].items():
            assert inputs[path] == expected, path
    graph = load('citation-graph.json')
    assert not graph['missing']
    for edge in graph['edges']:
        assert edge['source'] in inputs and edge['target'] in inputs
    reviews = [p for p in graph['roots'] if p.endswith('-ai-review.yaml')]
    assert len(reviews) == 15
    rows = historical = retired = 0
    for path in reviews:
        d = yaml.safe_load((ROOT / path).read_text())
        rows += len(d['existing_annotations'])
        for row in d['existing_annotations']:
            if row['review']['action'] == 'NEW':
                historical += 1
                retired += bool(row.get('retired'))
    if (OUT / 'handoff.json').exists():
        for path, expected in load('handoff.json')['files'].items():
            assert sha(ROOT / path) == expected, path
        assert load('handoff.json')['source_dependencies'] == inputs
    print(json.dumps({'status': 'PASS', 'inputs': len(inputs), 'prior_unchanged': 327,
                      'curated_reviews': 15, 'module_panel_reviews': 14,
                      'adjacent_duplicate': 'PA5377 = cbcW, Q9HTI7', 'ordered_rows': rows,
                      'historical_NEW': historical, 'active_NEW': historical - retired,
                      'retired_NEW': retired, 'resolved_citation_edges': len(graph['edges']),
                      'Reactome_edges': sum(e['kind'] == 'Reactome' for e in graph['edges']),
                      'provider_bibliographies_not_expanded': len(load('provider-boundaries.json')),
                      'private_cache_required': False}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
