"""Capture additive Gallate source closure; never modify an existing seal."""
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
A = ROOT / 'analysis/module_audits/bacterial_gallate_catabolism'
R = A / 'review-20261107'
PUBLISHED = 'f852d88b3b0cfe9f4658d879171b446a90dd6f1c'
EXCLUDED = {
    'pages/projects/MODULE_TAXON_AUDIT.html',
    'pages/projects/MODULE_TAXON_AUDIT/inventory.json',
    'pages/projects/index.html',
    'projects/MODULE_TAXON_AUDIT.md',
    'projects/MODULE_TAXON_AUDIT/inventory.json',
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path):
    return str(path.relative_to(ROOT))


def put(name, data):
    assert shutil.disk_usage(ROOT).free > 256 * 1024**2
    p = OUT / name
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + '.tmp')
    tmp.write_bytes(data if isinstance(data, bytes) else (json.dumps(data, indent=2, sort_keys=True) + '\n').encode())
    tmp.replace(p)


def load(path):
    return json.loads(path.read_text())


def main():
    assert not (OUT / 'handoff.json').exists(), 'Frozen: do not regenerate'
    aliases = {}
    for move in load(A / 'ci-provenance-relocation.json')['moves']:
        aliases[move['old']] = {'path': move['new'], 'sha256': move['sha256'], 'kind': 'previous byte-identical relocation'}
    for locus in ('C7569', 'C7570', 'C7572'):
        old = f'.cache/module-audit-logs/gallate-20261106/BURL3-{locus}-falcon.log'
        dest = f'provider-attempts/BURL3-{locus}-falcon.log'
        put(dest, (ROOT / old).read_bytes())
        aliases[old] = {'path': rel(OUT / dest), 'sha256': sha(ROOT / old), 'kind': 'byte-identical failed-provider log'}
    manifests = {}
    for name, old in (
        ('published-full-manifest.json', '.cache/module-audit-logs/gallate-20261107/round1/publication-manifest-sha256.json'),
        ('published-current-manifest.json', '.cache/module-audit-logs/gallate-20261107/post-hepg-main/publication-manifest-sha256.json'),
    ):
        put(name, (ROOT / old).read_bytes())
        manifests[name] = {'original_path': old, 'sha256': sha(ROOT / old)}
    fetch = ROOT / '.cache/module-audit-logs/gallate-20261107/review-20261107/provider-lead-fetch/results.json'
    put('provider-lead-fetch.json', fetch.read_bytes())
    supers = load(R / 'science-consultation/supersessions.json')
    supers.update(load(R / 'render-completion/handoff.json')['html_supersessions'])
    dependencies = {}
    claims = []

    def consume(mapping, origin):
        for old, expected in sorted(mapping.items()):
            if old in EXCLUDED:
                claims.append({'origin': origin, 'path': old, 'expected': expected, 'disposition': 'root-owned shared metadata excluded explicitly'})
                continue
            path = aliases.get(old, {}).get('path', old)
            actual = sha(ROOT / path)
            disposition = 'unchanged' if actual == expected else 'authorized successor'
            if actual != expected:
                s = supers.get(path, {})
                assert s.get('before_sha256') == expected and s.get('after_sha256') == actual, (origin, path, expected, actual)
            dependencies[path] = actual
            claims.append({'origin': origin, 'original_path': old, 'path': path, 'expected': expected, 'current': actual, 'disposition': disposition})

    for name in manifests:
        consume(load(OUT / name), name)
    published = load(OUT / 'published-current-manifest.json')
    for path, expected in published.items():
        if path not in EXCLUDED:
            blob = subprocess.check_output(['git', 'show', f'{PUBLISHED}:{path}'], cwd=ROOT)
            assert hashlib.sha256(blob).hexdigest() == expected, path
    for name in ('science-consultation', 'coverage-successor', 'render-completion'):
        p = R / name / 'handoff.json'
        dependencies[rel(p)] = sha(p)
        h = load(p)
        for field in ('files', 'source_dependencies'):
            consume(h[field], rel(p) + '#' + field)
    proteins = yaml.safe_load((A / 'coverage-evidence.yaml').read_text())['proteins']
    seeds = [p['review_path'] for p in proteins]
    seeds += ['modules/bacterial_gallate_catabolism.yaml', 'modules/bacterial_gallate_catabolism-notes.md']
    for family in ('PTHR12993', 'PTHR21240', 'PTHR33254', 'PTHR34596', 'PTHR43709'):
        for p in (ROOT / 'interpro/panther' / family).iterdir():
            dependencies[rel(p)] = sha(p)
        seeds.append(f'interpro/panther/{family}/{family}-review.yaml')
    # Notes and provider files already in the approved publication union are citation roots.
    seeds += [p for p in dependencies if p.endswith('.md') and p.startswith(('genes/', 'modules/'))]
    queue = sorted(set(seeds))
    scanned = set()
    edges = []
    missing = []

    def resolve(value, owner):
        value = value.rstrip('.,;')
        if value in aliases:
            return aliases[value]['path']
        choices = [ROOT / value, ROOT / 'genes' / value, (ROOT / owner).parent / value]
        return next((rel(p.resolve()) for p in choices if p.is_file() and p.resolve().is_relative_to(ROOT)), None)

    def add(value, owner, kind):
        path = resolve(value, owner)
        if path is None:
            missing.append({'source': owner, 'citation': value, 'kind': kind})
            return
        dependencies[path] = sha(ROOT / path)
        edges.append({'source': owner, 'citation': value, 'target': path, 'kind': kind})
        if (path.endswith('-ai-review.yaml') or path.endswith('.md')) and not path.startswith(('publications/', 'reactome/')):
            queue.append(path)
        if path.endswith('-ai-review.yaml'):
            notes = path.replace('-ai-review.yaml', '-notes.md')
            if (ROOT / notes).exists():
                queue.append(notes)

    while queue:
        path = queue.pop(0)
        if path in scanned:
            continue
        assert (ROOT / path).is_file(), path
        scanned.add(path)
        dependencies[path] = sha(ROOT / path)
        text = (ROOT / path).read_text()
        for pmid in sorted(set(re.findall(r'PMID[:_\s]*(\d{6,9})|pubmed\.ncbi\.nlm\.nih\.gov/(\d{6,9})', text))):
            number = pmid[0] or pmid[1]
            add(f'publications/PMID_{number}.md', path, 'PMID citation')
        for value in sorted(set(re.findall(r'file:([^\s\]\[<>\)\(\"\'`,]+)', text))):
            add(value, path, 'file citation')
        for reactome in sorted(set(re.findall(r'Reactome:(R-[A-Z]+-\d+)', text))):
            add(f'reactome/{reactome}.md', path, 'Reactome citation')
        for value in sorted(set(re.findall(r'\]\(([^)\s]+)\)', text))):
            if not re.match(r'[a-z]+://|#', value) and resolve(value.split('#')[0], path):
                add(value.split('#')[0], path, 'local Markdown link')
        for value in sorted(set(re.findall(r'\.cache/[^\s`\]\)\"\',]+', text))):
            if value.rstrip('.') in aliases:
                add(value.rstrip('.'), path, 'private log alias')
    assert all('deep-research' in item['source'] for item in missing), missing
    put('unresolved-provider-leads.json', {'status': 'UNADOPTED_EXTERNAL_BIBLIOGRAPHY', 'entries': missing, 'limitation': 'These citations occur only in transitive comparator/module provider reports. Their source report bytes are preserved; missing publication text is not claimed acquired or validated. No Gallate curated evidence depends on these leads.'})
    pubs = {}
    for p in sorted(dependencies):
        if p.startswith('publications/'):
            text = (ROOT / p).read_text()
            front = yaml.safe_load(text.split('---', 2)[1]) if text.startswith('---') else {}
            pubs[p] = {key: front.get(key) for key in ('title', 'full_text_available')}
            pubs[p]['citation_sources'] = sorted({e['source'] for e in edges if e['target'] == p})
            pubs[p]['role'] = 'provider bibliography only; claims not adopted' if p in {f'publications/PMID_{x}.md' for x in ('26867578', '21063756', '36724292', '41024182')} else 'curated/notes/family citation or preserved published source; access is cache-specific'
    put('aliases.json', aliases)
    put('manifest-provenance.json', {'published_head': PUBLISHED, 'manifests': manifests, 'excluded_shared_paths': sorted(EXCLUDED), 'claims': claims, 'supersessions': supers})
    put('citation-graph.json', {'roots': sorted(set(seeds)), 'scanned': sorted(scanned), 'edges': sorted(edges, key=lambda e: (e['source'], e['kind'], e['target'], e['citation'])), 'missing': missing, 'scope': 'Recursive explicit citations in reviews, notes, scoped analysis and provider reports. Publication/UniProt/PAINT data are terminal sources; their bibliographies are not new curation claims. Historical receipt contents remain frozen metadata, not new citation roots.'})
    put('publication-access.json', pubs)
    put('inputs.json', dict(sorted(dependencies.items())))
    put('members.json', [{'review_path': p['review_path'], 'accession': p['accession'], 'role': 'member or retained boundary comparator'} for p in proteins])
    print(json.dumps({'inputs': len(dependencies), 'publications': len(pubs), 'scanned': len(scanned), 'edges': len(edges), 'historical_claims': len(claims)}))


if __name__ == '__main__':
    main()
