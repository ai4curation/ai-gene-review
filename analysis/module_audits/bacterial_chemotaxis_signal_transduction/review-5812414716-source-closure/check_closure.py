"""Scoped publication union and recursive citation closure; no science writes."""
import hashlib
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
AUDIT = HERE.parent
ROOT = HERE.parents[3]
MODULE = ROOT / 'modules/bacterial_chemotaxis_signal_transduction.yaml'
PUBLISHED = '462ff344a425348aa3e9518cf3a55598cb1e69d1'
SHARED = {'projects/MODULE_TAXON_AUDIT.md', 'projects/MODULE_TAXON_AUDIT/inventory.json',
          'pages/projects/MODULE_TAXON_AUDIT.html', 'pages/projects/MODULE_TAXON_AUDIT/inventory.json'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path):
    return str(path.relative_to(ROOT))


def load(path):
    return yaml.safe_load(path.read_text())


def strings(value):
    if isinstance(value, dict):
        return [s for v in value.values() for s in strings(v)]
    if isinstance(value, list):
        return [s for v in value for s in strings(v)]
    return [value] if isinstance(value, str) else []


def main():
    inputs = {}
    missing = []
    metadata = []
    historical_manifest_entries = []
    private = defaultdict(set)
    references = []

    def add(path, reason):
        if not path.is_file():
            missing.append({'path': rel(path), 'reason': reason})
            return
        name = rel(path)
        if name in SHARED:
            if name not in {x['path'] for x in metadata}:
                metadata.append({'path': name, 'sha256_observed': sha(path),
                                 'scope': 'Shared mutable metadata; not immutable scientific input'})
            return
        item = inputs.setdefault(name, {'sha256': sha(path), 'reasons': []})
        if reason not in item['reasons']:
            item['reasons'].append(reason)

    # Union every explicit published path manifest, not a global unrelated pool.
    for path in sorted(AUDIT.glob('*.json')):
        doc = load(path)
        add(path, 'Prior committed audit receipt')
        for key in ['approved_manifest', 'validated_manifest', 'preserved_files_sha256', 'unchanged_files_sha256']:
            for name, value in doc.get(key, {}).items():
                expected = value.get('sha256') if isinstance(value, dict) else value
                target = ROOT / name
                add(target, 'Published manifest union: ' + rel(path) + '#' + key)
                historical_manifest_entries.append({'manifest': rel(path), 'path': name,
                    'historical_sha256': expected, 'current_sha256': sha(target) if target.is_file() else None})
    for path in AUDIT.glob('*.yaml'):
        add(path, 'Prior committed audit receipt')
    for dirname in ['review-5812414716-followup', 'review-5812414716-validation']:
        path = AUDIT / dirname / 'handoff.json'
        doc = load(path)
        add(path, 'Sealed current follow-up handoff')
        for name, digest in doc['files'].items():
            assert sha(ROOT / name) == digest, name
            add(ROOT / name, 'Sealed follow-up artifact: ' + rel(path))
    members = load(AUDIT / 'seed-baseline.yaml')['members']
    panel = [ROOT / m['review_path'] for m in members]
    assert len(panel) == 46
    raw_inputs = {}
    for member in members:
        for name, digest in member['raw_sha256'].items():
            assert sha(ROOT / name) == digest, name
            raw_inputs[name] = digest
            add(ROOT / name, 'Original frozen seed raw source')
    provider_inputs = load(AUDIT / 'provider-source-preservation.yaml')['sha256']
    for name, digest in provider_inputs.items():
        assert sha(ROOT / name) == digest, name
        add(ROOT / name, 'Original frozen provider source')
    families = sorted(set(re.findall(r'PTHR\d+', MODULE.read_text())))
    family_reviews = []
    family_limits = []
    for family in families:
        path = ROOT / f'interpro/panther/{family}/{family}-review.yaml'
        if path.is_file():
            family_reviews.append(path)
        else:
            family_limits.append({'family': family, 'scope': 'Mentioned identifier has no family-review file; no fabricated review or grant'})
    # Family reviews from older publication manifests remain in scope too.
    for name in inputs:
        if name.startswith('interpro/panther/') and name.endswith('-review.yaml'):
            path = ROOT / name
            if path not in family_reviews:
                family_reviews.append(path)
    notes = []
    for path in panel:
        note = path.with_name(path.name.replace('-ai-review.yaml', '-notes.md'))
        if note.is_file():
            notes.append(note)
        for source in path.parent.iterdir():
            if source.is_file() and source.suffix != '.html':
                add(source, 'Current panel gene folder; raw/provider/source analyses preserved')
    for path in family_reviews:
        for source in path.parent.iterdir():
            if source.is_file():
                add(source, 'Relevant family raw/assertion/source inventory')
    queue = panel + notes + family_reviews + [MODULE]
    scanned = set()
    pmids = re.compile(r'PMID\s*:?\s*(\d{5,9})')
    files = re.compile(r'file:([^\s`\]\)<>"\'}]+)')
    reactomes = re.compile(r'Reactome:(R-[A-Z]+-\d+)')
    private_pattern = re.compile(r'(?:\.cache/|/Users/|/tmp/)[^\s`\]\)<>"\']+')
    while queue:
        path = queue.pop()
        if path in scanned or not path.is_file():
            continue
        scanned.add(path)
        add(path, 'Current document or recursively cited local evidence')
        text = path.read_text(errors='replace')
        values = strings(load(path)) if path.suffix in {'.yaml', '.yml'} else [text]
        found = set()
        for text in values:
            found.update('PMID:' + x for x in pmids.findall(text))
            for group in re.findall(r'PMID\s*:?\s*\d{5,9}(?:\s*[,;/]\s*\d{5,9})+', text):
                found.update('PMID:' + x for x in re.findall(r'\d{5,9}', group))
            found.update('file:' + x.rstrip('.,;:') for x in files.findall(text))
            found.update('Reactome:' + x for x in reactomes.findall(text))
            for item in private_pattern.findall(text):
                private[item.rstrip('.,;:')].add(rel(path))
        for citation in sorted(found):
            if citation.startswith('PMID:'):
                target = ROOT / ('publications/PMID_' + citation[5:] + '.md')
            elif citation.startswith('Reactome:'):
                target = ROOT / 'reactome' / (citation[9:] + '.md')
            else:
                name = citation[5:].split('#')[0]
                target = ROOT / 'genes' / name
                if not target.is_file():
                    target = ROOT / name
            references.append({'document': rel(path), 'citation': citation, 'path': rel(target),
                               'exists': target.is_file()})
            add(target, citation + ' referenced by ' + rel(path))
            if (citation.startswith('file:') and target.is_file()
                    and target.suffix in {'.md', '.yaml', '.yml'}
                    and 'deep-research' not in target.name and 'publications' not in target.parts):
                queue.append(target)
    # Full ordered row payloads and lifecycle remain identical to the published head.
    panel_proof = {}
    row_total = 0
    active_new = 0
    retired_new = 0
    for path in panel:
        old_text = subprocess.check_output(['git', 'show', PUBLISHED + ':' + rel(path)], cwd=ROOT)
        old = yaml.safe_load(old_text)
        current = load(path)
        a = old['existing_annotations']
        b = current['existing_annotations']
        assert len(a) == len(b), rel(path)
        for x, y in zip(a, b, strict=True):
            assert {k: v for k, v in x.items() if k != 'review'} == {k: v for k, v in y.items() if k != 'review'}, rel(path)
            assert x['review']['action'] == y['review']['action'], rel(path)
            if y['review']['action'] == 'NEW':
                if y.get('retired', False):
                    retired_new += 1
                else:
                    active_new += 1
        row_total += len(b)
        panel_proof[rel(path)] = {'sha256': sha(path), 'ordered_rows': len(b),
                                  'full_review_published_identical': hashlib.sha256(old_text).hexdigest() == sha(path)}
    cher2 = 'genes/PSEPK/cheR2/cheR2-ai-review.yaml'
    assert panel_proof[cher2]['full_review_published_identical']
    # Match private scientific/provenance artifacts by bytes, not a similar name.
    aliases = {x['private_path']: x for x in load(HERE / 'private-alias-map.json')['files']}
    add(HERE / 'private-alias-map.json', 'Exact private-to-durable acquisition mapping')
    tracked = []
    if any(name not in aliases and (ROOT / name).is_file() for name in private):
        tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
    size_index = defaultdict(list)
    for name in tracked:
        path = ROOT / name
        if path.is_file() and path.suffix in {'.json', '.yaml', '.yml', '.log', '.txt', '.md', '.xml'}:
            size_index[path.stat().st_size].append(path)
    private_map = []
    for name, origins in sorted(private.items()):
        path = ROOT / name if not name.startswith('/') else Path(name)
        entry = {'private_path': name, 'cited_by': sorted(origins), 'exists': path.exists()}
        if name in aliases:
            alias = aliases[name]
            target = ROOT / alias['durable_path']
            assert sha(target) == alias['sha256']
            if path.is_file():
                assert sha(path) == alias['sha256']
            add(target, 'Byte-identical packaged alias of ' + name)
            entry.update({'sha256': alias['sha256'], 'durable_byte_identical_equivalents': [rel(target)],
                          'status': 'DURABLE_EQUIVALENT', 'role': alias['role']})
        elif path.is_file():
            digest = sha(path)
            matches = [f for f in size_index[path.stat().st_size] if sha(f) == digest]
            entry.update({'sha256': digest, 'durable_byte_identical_equivalents': [rel(f) for f in matches]})
            for target in matches:
                add(target, 'Byte-identical durable equivalent of ' + name)
            entry['status'] = 'DURABLE_EQUIVALENT' if matches else 'PRIVATE_FILE_NO_DURABLE_EQUIVALENT'
        elif path.is_dir():
            entry['status'] = 'HISTORICAL_DIRECTORY_REFERENCE'
            entry['scope'] = 'Notes describe historical validation provenance; this is not an individual scientific evidence citation.'
        else:
            entry['status'] = 'PRIVATE_PATH_MISSING'
        private_map.append(entry)
    # Distinguish older historical subjects from the current follow-up successors.
    latest = load(AUDIT / 'main9-integration.json')['preserved_files_sha256']
    approved_files = set(load(AUDIT / 'review-5812414716-followup/handoff.json')['files'])
    approved_files.update(load(AUDIT / 'review-5812414716-validation/handoff.json')['files'])
    root_metadata = {rel(AUDIT / 'README.md'), rel(AUDIT / 'audit-progress.yaml')}
    supersessions = []
    for name, digest in latest.items():
        current = sha(ROOT / name)
        if current != digest:
            assert name in approved_files or name in root_metadata, name
            at_published = hashlib.sha256(subprocess.check_output(
                ['git', 'show', PUBLISHED + ':' + name], cwd=ROOT)).hexdigest()
            supersessions.append({'path': name, 'old_manifest_sha256': digest,
                                  'published_head_sha256': at_published, 'current_sha256': current,
                                  'authority': 'Two sealed follow-up handoffs' if name in approved_files
                                  else 'Root-owned audit metadata committed at b05ebf8a63b180882c7251efe0d549b62fa91c2d'})
    result = {'status': 'CLOSURE_REQUIRES_PRIVATE_SOURCE_RECONCILIATION' if missing or any(
        x['status'] in {'PRIVATE_PATH_MISSING', 'PRIVATE_FILE_NO_DURABLE_EQUIVALENT'} for x in private_map) else 'PASS',
        'captured_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'panel_reviews': len(panel), 'family_reviews': len(family_reviews), 'family_limits': family_limits,
        'ordered_rows_preserved': row_total, 'active_NEW': active_new, 'retired_NEW': retired_new,
        'original_raw_sources_unchanged': len(raw_inputs), 'original_provider_sources_unchanged': len(provider_inputs),
        'historical_proposal_archive': rel(AUDIT / 'retired-inherited-proposals.yaml'),
        'historical_proposal_archive_sha256': sha(AUDIT / 'retired-inherited-proposals.yaml'),
        'panel': panel_proof, 'explicit_cheR2_full_review_unchanged': True,
        'input_count': len(inputs), 'inputs': dict(sorted(inputs.items())),
        'reference_edges': references, 'missing_sources': missing,
        'historical_manifest_entries': historical_manifest_entries, 'private_source_map': private_map,
        'latest_manifest_authorized_successors': supersessions,
        'shared_metadata_observations': metadata,
        'limits': ['No historical receipt rewritten; historical hashes describe their own snapshots.',
                   'Private source gaps remain explicit; no full paper copied or source downloaded.',
                   'No fresh capacity or full-corpus validation claim.']}
    (HERE / 'source-closure.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['status', 'panel_reviews', 'family_reviews', 'ordered_rows_preserved', 'active_NEW', 'retired_NEW', 'input_count']}))
    print('missing', len(missing), 'private', len(private_map), 'reference_edges', len(references))


if __name__ == '__main__':
    main()
