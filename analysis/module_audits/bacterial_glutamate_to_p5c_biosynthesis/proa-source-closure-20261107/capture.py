"""Additive current curated-evidence closure, excluding provider bibliography expansion."""
import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
A = OUT.parent
SHARED = {'pages/projects/MODULE_TAXON_AUDIT.html', 'pages/projects/MODULE_TAXON_AUDIT/inventory.json',
          'pages/projects/index.html', 'projects/MODULE_TAXON_AUDIT.md', 'projects/MODULE_TAXON_AUDIT/inventory.json'}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def put(name, value):
    p = OUT / name
    tmp = p.with_suffix(p.suffix + '.tmp')
    tmp.write_bytes(value if isinstance(value, bytes) else (json.dumps(value, indent=2, sort_keys=True) + '\n').encode())
    tmp.replace(p)


def main():
    assert not (OUT / 'handoff.json').exists(), 'Already frozen'
    prior = ROOT / '.cache/module-audit-logs/glutamate-p5c-20261107/approved-main-1356/publication-manifest-sha256.json'
    put('prior-publication-manifest.json', prior.read_bytes())
    prior_map = json.loads(prior.read_text())
    hpath = A / 'proa-localization-followup-20261107/handoff.json'
    handoff = json.loads(hpath.read_text())
    inputs = {}
    successors = {}
    allowed = {'genes/BACSU/proA/proA-ai-review.yaml',
               'genes/BACSU/proA/proA-notes.md',
               'genes/BACSU/proA/proA-ai-review.html'}
    for path, expected in prior_map.items():
        if path in SHARED:
            continue
        actual = sha(ROOT / path)
        if actual != expected:
            assert path in allowed, path
            successors[path] = {'before_sha256': expected, 'after_sha256': actual,
                                'reason': 'Evidence-backed ProA cytosol refinement, notes and rendered review.'}
        inputs[path] = actual
    assert len(inputs) == 180
    assert set(successors) == allowed
    for field in ('files', 'source_dependencies'):
        for path, expected in handoff.get(field, {}).items():
            assert sha(ROOT / path) == expected, path
            inputs[path] = expected
    sealpath = ROOT / handoff['stage_path_hashes']
    for path, expected in json.loads(sealpath.read_text()).items():
        assert sha(ROOT / path) == expected, path
        inputs[path] = expected
    inputs[str(sealpath.relative_to(ROOT))] = sha(sealpath)
    inputs[str(hpath.relative_to(ROOT))] = sha(hpath)
    roots = sorted(p for p in prior_map if p.endswith('-ai-review.yaml'))
    assert len(roots) == 11  # nine bacterial members and two existing eukaryotic comparators
    module = 'modules/bacterial_glutamate_to_p5c_biosynthesis.yaml'
    roots.extend([module, module.replace('.yaml', '-notes.md')])
    for family in ('PTHR11063', 'PTHR43654'):
        folder = ROOT / 'interpro/panther' / family
        for p in folder.iterdir():
            if p.is_file():
                inputs[str(p.relative_to(ROOT))] = sha(p)
        roots.append(str((folder / f'{family}-review.yaml').relative_to(ROOT)))
    for review in list(roots):
        if review.endswith('-ai-review.yaml'):
            folder = (ROOT / review).parent
            for p in folder.iterdir():
                if p.is_file() and p.suffix in {'.txt', '.tsv'}:
                    inputs[str(p.relative_to(ROOT))] = sha(p)
            notes = review.replace('-ai-review.yaml', '-notes.md')
            if (ROOT / notes).exists():
                roots.append(notes)
    queue = sorted(set(roots))
    scanned = set()
    edges = []
    provider_boundary = {}
    missing = []

    def resolve(value, owner):
        value = value.rstrip('.,;')
        for path in (ROOT / value, ROOT / 'genes' / value, (ROOT / owner).parent / value):
            if path.is_file() and path.resolve().is_relative_to(ROOT):
                return str(path.resolve().relative_to(ROOT))
        return None

    def edge(value, owner, kind):
        target = resolve(value, owner)
        if target is None:
            missing.append({'source': owner, 'citation': value, 'kind': kind})
            return
        assert not target.startswith('.cache/'), target
        inputs[target] = sha(ROOT / target)
        edges.append({'source': owner, 'target': target, 'citation': value, 'kind': kind})
        if target.endswith(('.md', '-review.yaml')) and not target.startswith(('publications/', 'reactome/')):
            queue.append(target)

    while queue:
        path = queue.pop(0)
        if path in scanned:
            continue
        if not (ROOT / path).exists():
            # A module may have no standalone notes; explicit citations cannot use this exception.
            assert path == module.replace('.yaml', '-notes.md')
            continue
        scanned.add(path)
        inputs[path] = sha(ROOT / path)
        text = (ROOT / path).read_text()
        pmids = sorted({a or b for a, b in re.findall(r'PMID[:_\s]*(\d{6,9})|pubmed\.ncbi\.nlm\.nih\.gov/(\d{6,9})', text)})
        if 'deep-research' in path:
            provider_boundary[path] = {'PMIDs_not_followed': pmids, 'reason': 'Unadopted provider bibliography; report bytes preserved, no recursive literature expansion.'}
            continue
        for pmid in pmids:
            edge(f'publications/PMID_{pmid}.md', path, 'PMID')
        for value in sorted(set(re.findall(r'file:([^\s\]\[<>\)\(\"\'`,]+)', text))):
            edge(value, path, 'file')
        for rid in sorted(set(re.findall(r'Reactome:(R-[A-Z]+-\d+)', text))):
            edge(f'reactome/{rid}.md', path, 'Reactome')
        for value in sorted(set(re.findall(r'\]\(([^)\s]+)\)', text))):
            if not re.match(r'[a-z]+://|#', value) and resolve(value.split('#')[0], path):
                edge(value.split('#')[0], path, 'Markdown link')
    assert not missing, missing
    publications = {}
    for path in sorted(inputs):
        if path.startswith('publications/'):
            text = (ROOT / path).read_text()
            header = yaml.safe_load(text.split('---', 2)[1]) if text.startswith('---') else {}
            publications[path] = {k: header.get(k) for k in ('title', 'full_text_available')}
    put('inputs.json', dict(sorted(inputs.items())))
    put('citation-graph.json', {'roots': sorted(set(roots)), 'scanned': sorted(scanned), 'edges': sorted(edges, key=lambda x: (x['source'], x['kind'], x['target'], x['citation'])), 'missing': missing})
    put('provider-boundaries.json', provider_boundary)
    put('publication-access.json', publications)
    put('prior-and-supersession.json', {'prior_original_path': str(prior.relative_to(ROOT)), 'prior_manifest_sha256': sha(prior), 'prior_count': 185, 'prior_nonshared_verified': 180, 'prior_nonshared_unchanged': 177, 'excluded_shared_paths': sorted(SHARED), 'authorized_ProA_successors': successors, 'new_handoff': str(hpath.relative_to(ROOT)), 'new_handoff_sha256': sha(hpath)})
    print(json.dumps({'inputs': len(inputs), 'publications': len(publications), 'edges': len(edges), 'provider_boundaries': len(provider_boundary)}))


if __name__ == '__main__':
    main()
