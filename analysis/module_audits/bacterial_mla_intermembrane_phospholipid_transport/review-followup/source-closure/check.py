"""Read-only source closure with exact authorized scientific successors."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
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
    p = load('prior-and-supersession.json')
    assert sha(OUT / 'prior-publication-manifest.json') == p['prior_manifest_sha256']
    prior = load('prior-publication-manifest.json')
    assert len(prior) == 573
    retained = {path: h for path, h in prior.items() if path not in p['excluded_shared_paths']}
    assert len(retained) == 569
    successors = p['authorized_gene_successors']
    allowed = {f'genes/{org}/{gene}/{gene}{suffix}'
               for org, gene in [('BORPE', 'BP3757'), ('BORPE', 'BP3758'), ('BORPE', 'BP3759'),
                                 ('BORPE', 'BP3760'), ('BORPE', 'BP3761'), ('PSEAE', 'ttg2D')]
               for suffix in ('-ai-review.yaml', '-notes.md', '-ai-review.html')}
    assert set(successors) <= allowed
    h = json.loads((ROOT / p['new_handoff']).read_text())
    assert sha(ROOT / p['new_handoff']) == p['new_handoff_sha256']
    declared = json.loads((ROOT / h['supersession_map']).read_text())
    for path, item in successors.items():
        assert declared[path]['published_before_sha256'] == item['before_sha256']
        assert declared[path]['after_sha256'] == item['after_sha256']
    for path, expected in retained.items():
        if path in successors:
            assert successors[path]['before_sha256'] == expected
            assert successors[path]['after_sha256'] == inputs[path] == h['files'][path]
        else:
            assert inputs[path] == expected, path
    for field in ('files', 'source_dependencies'):
        for path, expected in h.get(field, {}).items():
            assert inputs[path] == expected, path
    graph = load('citation-graph.json')
    assert not graph['missing']
    for edge in graph['edges']:
        assert edge['source'] in inputs and edge['target'] in inputs
    reviews = [path for path in graph['roots'] if path.startswith('genes/') and path.endswith('-ai-review.yaml')]
    assert len(reviews) == 18
    rows = historical = retired = 0
    for path in reviews:
        d = yaml.safe_load((ROOT / path).read_text())
        rows += len(d['existing_annotations'])
        for row in d['existing_annotations']:
            if row['review']['action'] == 'NEW':
                historical += 1
                retired += bool(row.get('retired'))
    assert rows == h['counts']['current_rows']
    assert historical == h['counts']['historical_new'] + h['counts']['authored_new']
    assert historical - retired == h['counts']['active_new']
    if (OUT / 'handoff.json').exists():
        seal = load('handoff.json')
        for path, expected in seal['files'].items():
            assert sha(ROOT / path) == expected, path
        assert seal['source_dependencies'] == inputs
    print(json.dumps({'status': 'PASS', 'current_inputs': len(inputs),
                      'prior_nonshared': len(retained), 'prior_unchanged': len(retained) - len(successors),
                      'authorized_successors': len(successors), 'reviews': len(reviews),
                      'ordered_rows': rows, 'historical_NEW_preserved': h['counts']['historical_new'],
                      'authored_NEW': h['counts']['authored_new'], 'total_NEW_rows': historical,
                      'active_NEW': historical - retired, 'retired_NEW': retired,
                      'resolved_citation_edges': len(graph['edges']),
                      'Reactome_edges': sum(e['kind'] == 'Reactome' for e in graph['edges']),
                      'provider_bibliographies_not_expanded': len(load('provider-boundaries.json')),
                      'private_cache_required': False}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
