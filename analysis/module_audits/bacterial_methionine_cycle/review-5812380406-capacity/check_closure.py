"""Additive local input closure; never rewrites historical receipts or science."""
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
AUDIT = HERE.parent
ROOT = HERE.parents[3]
SEALED = AUDIT / 'review-5812380406-followup'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def relative(path):
    return str(path.relative_to(ROOT))


def main():
    assert shutil.disk_usage(ROOT).free > 256 * 1024 * 1024
    sealed = read(SEALED / 'handoff.json')
    assert sha(SEALED / 'handoff.json') == 'c574e47bfd3ace889917dc6416e517f9ab5aab25ef0fefa263aab0fa3643dbcd'
    successor = read(HERE / 'family-attachment-supersession.json')
    def verify_seal():
        for name, digest in sealed['files'].items():
            if name == successor['path']:
                assert digest == successor['prior_sha256']
                assert sha(ROOT / successor['prior_bytes_archive']) == digest
                assert sha(ROOT / name) == successor['current_sha256']
            else:
                assert sha(ROOT / name) == digest, name
    verify_seal()
    old_family = yaml.safe_load((ROOT / successor['prior_bytes_archive']).read_text())
    new_family = yaml.safe_load((ROOT / successor['path']).read_text())
    old_family.pop('notes')
    new_family.pop('notes')
    for section in ['node_assessments', 'term_assessments']:
        for entry in old_family[section]:
            entry['supported_by'] = [x for x in entry.get('supported_by', [])
                                     if 'supporting_text' in x]
    assert old_family == new_family
    copy_proof = read(HERE / 'copy-provenance.json')
    original_checker = ROOT / copy_proof['original_checker']
    assert sha(original_checker) == copy_proof['original_sha256']
    expected_copy = original_checker.read_text().replace(
        'ROOT = HERE.parents[2]', 'ROOT = HERE.parents[3]').replace(
        "HERE / 'capacity-results.json'", "HERE / 'prior-capacity-results.json'")
    assert (HERE / 'check_capacity.py').read_text() == expected_copy
    before = read(SEALED / 'before.json')
    preserved = read(SEALED / 'preservation.json')
    protected = dict(before['protected_sources'])
    protected.update({p: v['sha256'] for p, v in read(
        SEALED / 'classification-ontology-provenance.json').items()})
    assert len(protected) == 62  # panther.obo occurs in both provenance lists
    for name, digest in protected.items():
        assert sha(ROOT / name) == digest, name
    baseline = read(AUDIT / 'baseline.json')
    module_path = 'modules/bacterial_methionine_cycle.yaml'
    module_families = sorted(set(re.findall(r'PTHR\d+', (ROOT / module_path).read_text())))
    family_reviews = set(baseline['families'])
    family_assessment_gaps = []
    for family in module_families:
        name = f'interpro/panther/{family}/{family}-review.yaml'
        if (ROOT / name).is_file():
            family_reviews.add(name)
        else:
            family_assessment_gaps.append({'family': family, 'review': name,
                'limit': 'No family review exists; descriptor/member evidence is not a universal family grant.'})
    documents = list(preserved['panel']) + sorted(family_reviews) + [module_path]
    inputs = {}
    missing = []
    references = []

    def add(path, reason):
        path = path.resolve()
        if not path.is_relative_to(ROOT):
            missing.append({'path': str(path), 'reason': reason, 'kind': 'external_path'})
            return
        name = relative(path)
        if not path.is_file():
            missing.append({'path': name, 'reason': reason, 'kind': 'missing_file'})
            return
        entry = inputs.setdefault(name, {'sha256': sha(path), 'reasons': []})
        if reason not in entry['reasons']:
            entry['reasons'].append(reason)

    # Keep the complete earlier publication union, rather than a convenient subset.
    old_receipt = AUDIT / 'review-followup/full-validation-20261107-1238.json'
    old = read(old_receipt)['frozen_input_sha256']
    differences = []
    metadata = []
    for name, digest in old.items():
        path = ROOT / name
        current = sha(path) if path.is_file() else None
        if name in {'projects/MODULE_TAXON_AUDIT.md', 'projects/MODULE_TAXON_AUDIT/inventory.json',
                     'pages/projects/MODULE_TAXON_AUDIT.html', 'pages/projects/MODULE_TAXON_AUDIT/inventory.json'}:
            head = subprocess.check_output(['git', 'show', 'HEAD:' + name], cwd=ROOT)
            metadata.append({'path': name, 'historical_freeze_sha256': digest,
                             'current_sha256': current,
                             'current_HEAD_identical': hashlib.sha256(head).hexdigest() == current,
                             'scope': 'Shared project metadata observed, excluded from immutable science closure'})
            continue
        add(path, 'prior 854-input published full-validation freeze')
        if current != digest:
            assert name in sealed['files'], name
            assert current == (successor['current_sha256'] if name == successor['path']
                               else sealed['files'][name]), name
            differences.append({'path': name, 'prior_sha256': digest,
                                'current_sha256': current,
                                'authority': (relative(HERE / 'family-attachment-supersession.json')
                                              if name == successor['path'] else relative(SEALED / 'handoff.json'))})
    add(old_receipt, 'historical full-validation receipt remains historical')
    for path in AUDIT.rglob('*'):
        if not path.is_file() or HERE in path.parents:
            continue
        if path.name in {'handoff.json', 'receipt.json', 'ready.json', 'capacity-results.json',
                         'closure-results.json', 'check_capacity.py', 'check_closure.py'}:
            add(path, 'preserved earlier audit/checker/receipt')
    add(ROOT / 'src/ai_gene_review/module_logic.py', 'Production compiler and satisfaction implementation')
    # Released artifact lists can be repository-relative or bundle-relative.
    manifests = []
    for path in sorted(AUDIT.rglob('handoff.json')):
        if HERE in path.parents:
            continue
        doc = read(path)
        entries = doc.get('files', {})
        assert isinstance(entries, dict), str(path)
        manifest = {'path': relative(path), 'sha256': sha(path), 'entries': []}
        for name, original_digest in entries.items():
            target = ROOT / name
            if not target.exists():
                target = path.parent / name
            add(target, 'released artifact from ' + relative(path))
            manifest['entries'].append({
                'path': relative(target) if target.is_relative_to(ROOT) else str(target),
                'historical_sha256': original_digest,
                'current_sha256': sha(target) if target.is_file() else None})
        manifests.append(manifest)
    add(ROOT / 'history/other/PTHR23420/2026-11-07T132843Z-codex-893507.yaml', 'Authorized family attachment successor history')
    for name in protected:
        add(ROOT / name, '63 protected observations / 62 unique follow-up inputs')
    # Discover citations anywhere in the current documents and cited local analyses.
    queue = [ROOT / name for name in documents]
    visited = set()
    pmid_pattern = re.compile(r'PMID\s*:?\s*(\d{5,9})')
    file_pattern = re.compile(r'file:([^\s\]\)\}\"\'<>]+)')
    while queue:
        path = queue.pop()
        if path in visited or not path.is_file():
            continue
        visited.add(path)
        add(path, 'current scientific document or recursively cited local source')
        text = path.read_text(errors='replace')
        if path.suffix in {'.yaml', '.yml'}:
            strings = []

            def walk(value):
                if isinstance(value, dict):
                    for child in value.values():
                        walk(child)
                elif isinstance(value, list):
                    for child in value:
                        walk(child)
                elif isinstance(value, str):
                    strings.append(value)
            walk(yaml.safe_load(text))
        else:
            strings = [text]
        citations = set()
        for value in strings:
            citations.update('PMID:' + match for match in pmid_pattern.findall(value))
            citations.update('file:' + match.rstrip('.,;:') for match in file_pattern.findall(value))
        for citation in sorted(citations):
            if citation.startswith('PMID:'):
                target = ROOT / ('publications/PMID_' + citation[5:] + '.md')
            else:
                name = citation[5:]
                target = ROOT / 'genes' / name
                if not target.is_file():
                    target = ROOT / name
            references.append({'document': relative(path), 'reference': citation,
                               'source': relative(target) if target.is_relative_to(ROOT) else str(target),
                               'exists': target.is_file()})
            add(target, citation + ' cited by ' + relative(path))
            # Raw databases and entire articles are source leaves, not a demand for
            # every bibliography item or database cross-reference in those sources.
            if (citation.startswith('file:') and target.is_file()
                    and target.suffix in {'.md', '.yaml', '.yml'}
                    and 'deep-research' not in target.name
                    and 'publications' not in target.parts):
                queue.append(target)
    # Recheck full ordered source payloads and lifecycle against the published HEAD.
    row_total = 0
    new_total = 0
    payloads = {}
    for name in preserved['panel']:
        current = yaml.safe_load((ROOT / name).read_text())
        original = yaml.safe_load(subprocess.check_output(
            ['git', 'show', before['head'] + ':' + name], cwd=ROOT))
        old_rows = original['existing_annotations']
        rows = current['existing_annotations']
        assert len(rows) == len(old_rows), name
        for index, (old_row, row) in enumerate(zip(old_rows, rows, strict=True)):
            assert {k: v for k, v in row.items() if k != 'review'} == {
                k: v for k, v in old_row.items() if k != 'review'}, (name, index)
            if old_row.get('review', {}).get('action') == 'NEW':
                assert row['review']['action'] == 'NEW', (name, index)
                assert row.get('retired') == old_row.get('retired'), (name, index)
                new_total += 1
        row_total += len(rows)
        payloads[name] = {'sha256': sha(ROOT / name), 'ordered_rows': len(rows)}
    assert row_total == 192 and new_total == 4
    # No scientific old checker/receipt is rewritten by this supplement.
    verify_seal()
    result = {
        'status': 'PASS' if not missing else 'MISSING_SOURCES_REPORTED',
        'scope': {'members': 18, 'family_reviews': len(family_reviews), 'module': 1,
                  'sealed_followup_files': 28, 'protected_provenance_observations': 63, 'unique_protected_inputs': 62},
        'ordered_rows_preserved': row_total, 'historical_NEW_preserved': new_total,
        'added_deleted_retired_rows': 0, 'panel': payloads,
        'source_input_count': len(inputs), 'inputs': dict(sorted(inputs.items())),
        'reference_edges': references, 'missing_sources': missing,
        'prior_full_freeze_input_count': len(old), 'explicit_supersessions': differences,
        'shared_metadata_observations': metadata, 'released_manifest_observations': manifests,
        'family_assessment_gaps': family_assessment_gaps,
        'sealed_science_successor': successor,
        'sealed_hashes_unchanged': 27, 'sealed_hashes_explicitly_superseded': 1,
        'limits': ['Prior full validation describes its old input snapshot, not this follow-up.',
                   'Historical manifest entry hashes remain recorded even when a later release supersedes their subjects.',
                   'Source presence/hash closure is not a claim every cached article contains full text.',
                   'Shared project metadata is separately observed, not frozen scientific input.',
                   'No source downloaded, publication refreshed, or old receipt rewritten.']}
    (HERE / 'source-closure.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['status', 'scope', 'ordered_rows_preserved',
                     'historical_NEW_preserved', 'source_input_count']}))
    print('missing', len(missing), 'supersessions', len(differences), 'reference edges', len(references))


if __name__ == '__main__':
    main()
