"""Verify released consultations and record the exact module evidence input closure."""
import hashlib
import json
from pathlib import Path

import yaml

from ai_gene_review.module_logic import compile_node, count_routes, iter_atoms

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
AUDIT = HERE.parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def main():
    inputs = {}
    released_files = {}
    for name in ['ecoli', 'psepk', 'family', 'aciad', 'cross-lineage', 'flaj1-lola']:
        manifest = AUDIT / f'{name}-consultation/handoff.json'
        document = json.loads(manifest.read_text())
        files = document.get('files', document.get('files_sha256'))
        for filename, expected in files.items():
            actual = digest(ROOT / filename)
            assert actual == expected, filename
            released_files[filename] = actual
        inputs[str(manifest.relative_to(ROOT))] = digest(manifest)
    module_path = ROOT / 'modules/bacterial_lol_lipoprotein_trafficking.yaml'
    module = yaml.safe_load(module_path.read_text())
    accessions = {
        x['id'].split(':', 1)[1] for x in walk(module['module'])
        if x.get('id', '').startswith('UniProtKB:')
    }
    reviews = {}
    for filename in released_files:
        if filename.endswith('-ai-review.yaml'):
            data = yaml.safe_load((ROOT / filename).read_text())
            if data['id'] in accessions:
                assert data['status'] == 'COMPLETE', filename
                reviews[data['id']] = {
                    'path': filename, 'sha256': digest(ROOT / filename),
                    'description': data['description'],
                    'core_functions': data.get('core_functions', []),
                }
                inputs[filename] = digest(ROOT / filename)
        if filename.endswith('-review.yaml') and filename.startswith('interpro/'):
            inputs[filename] = digest(ROOT / filename)
    assert set(reviews) == accessions, sorted(accessions - set(reviews))
    assert len(reviews) == 17
    sources = json.loads((HERE / 'baseline.json').read_text())['protected_source_sha256'].copy()
    for item in walk(module):
        ref = item.get('source_id', item.get('reference_id', item.get('id', '')))
        if ref.startswith('PMID:'):
            path = ROOT / f'publications/PMID_{ref.split(":")[1]}.md'
        elif ref.startswith('file:'):
            name = ref[5:]
            path = ROOT / name
            if not path.exists():
                path = ROOT / 'genes' / name
        else:
            continue
        assert path.is_file(), ref
        sources[str(path.relative_to(ROOT))] = digest(path)
    for name, expected in sources.items():
        assert digest(ROOT / name) == expected, name
    inputs.update(sources)
    result = {
        'status': 'PASS', 'representative_count': len(reviews),
        'released_file_count_verified': len(released_files),
        'inputs_sha256': dict(sorted(inputs.items())),
        'source_closure_sha256': dict(sorted(sources.items())),
        'reviews': dict(sorted(reviews.items())),
        'scope': 'Exact input integrity and core-function inventory; not independent assay validation.',
    }
    (HERE / 'input-closure.json').write_text(json.dumps(result, indent=2) + '\n')
    circuit = compile_node(module['module'])
    result = {'status': 'FINAL', 'structural_route_combinations': count_routes(circuit),
              'atoms': [{'node_id': a.node_id, 'function_ids': list(a.function_ids),
                         'family_ids': list(a.family_ids), 'uniprots': list(a.uniprots)}
                        for a in iter_atoms(circuit)],
              'limitation': 'Complex active units, matched interfaces and same-protein bifunctionality require biological gates; six formal combinations are not six established routes.'}
    (HERE / 'final-logic.json').write_text(json.dumps(result, indent=2) + '\n')
    print(f'PASS: {len(reviews)} representatives; {len(released_files)} released files; {len(sources)} module source files.')


if __name__ == '__main__':
    main()
