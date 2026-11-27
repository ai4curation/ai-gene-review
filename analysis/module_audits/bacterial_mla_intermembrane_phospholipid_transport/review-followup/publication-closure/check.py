"""Publication closure; bytecode is neither required nor read."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent


def digest(path):
    assert '__pycache__' not in path.parts and path.suffix != '.pyc', path
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def expected_union():
    evidence = load(OUT / 'exclusions.json')
    excluded = evidence['excluded_generated_noninputs']
    union = {}
    sources = evidence['source_manifests']
    for path, expected in sources.items():
        assert digest(ROOT / path) == expected, path
        handoff = load(ROOT / path)
        union[path] = expected
        for field in ('files', 'source_dependencies'):
            for member, h in handoff[field].items():
                assert member not in union or union[member] == h, member
                union[member] = h
    stage = evidence['stage_path_hashes']
    assert digest(ROOT / stage['path']) == stage['sha256']
    union[stage['path']] = stage['sha256']
    for path, expected in load(ROOT / stage['path']).items():
        assert path not in union or union[path] == expected, path
        union[path] = expected
    assert len(excluded) == 3
    for path, item in excluded.items():
        assert union.pop(path) == item['old_sha256'], path
        assert union[item['replacement_source']] == item['source_sha256']
    # No broad pattern-based deletion: any further generated path is an error.
    assert not [p for p in union if '__pycache__' in Path(p).parts or p.endswith('.pyc')]
    return dict(sorted(union.items()))


def main():
    inputs = load(OUT / 'inputs.json')
    assert inputs == expected_union()
    for path, expected in inputs.items():
        assert digest(ROOT / path) == expected, path
    graph_path = 'analysis/module_audits/bacterial_mla_intermembrane_phospholipid_transport/review-followup/source-closure/citation-graph.json'
    graph = load(ROOT / graph_path)
    assert not graph['missing']
    for edge in graph['edges']:
        assert edge['source'] in inputs and edge['target'] in inputs
    handoff = OUT / 'handoff.json'
    if handoff.exists():
        seal = load(handoff)
        for path, expected in seal['files'].items():
            assert digest(ROOT / path) == expected, path
        assert seal['source_dependencies'] == inputs
    print(json.dumps({'status': 'PASS', 'publication_inputs': len(inputs),
                      'exact_generated_exclusions': 3, 'scientific_sources_excluded': 0,
                      'resolved_citation_edges': len(graph['edges']),
                      'bytecode_reads': 0, 'old_seals_preserved': True,
                      'fresh_checkout_requires_generated_bytecode': False}, indent=2))


if __name__ == '__main__':
    main()
