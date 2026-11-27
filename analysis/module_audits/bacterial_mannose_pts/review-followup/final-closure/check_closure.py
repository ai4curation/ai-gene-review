"""Additive PR6193 closure: retain historical inputs and explicit supersession edges."""
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

from ai_gene_review.validation.local_source_text import quote_matches, resolve_local_source
from ai_gene_review.validation.supporting_text import build_supporting_text_validator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
AUDIT = HERE.parent.parent
sys.dont_write_bytecode = True
PROJECT = {'projects/MODULE_TAXON_AUDIT.md', 'projects/MODULE_TAXON_AUDIT/inventory.json',
           'pages/projects/MODULE_TAXON_AUDIT.html', 'pages/projects/MODULE_TAXON_AUDIT/inventory.json'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def imported(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for v in value.values():
            yield from strings(v)
    elif isinstance(value, list):
        for v in value:
            yield from strings(v)


def main():
    followup = HERE.parent
    baseline = read(followup / 'baseline.json')
    prior = AUDIT / 'capacity-consultation'
    prior_inputs = read(prior / 'inputs.json')['sha256']
    publication = ROOT / '.cache/module-audit-logs/mannose-20261107/publication-manifest-sha256.json'
    publication_inputs = read(publication)
    current_edges = read(followup / 'supersession.json')['paths']
    old_edges = read(AUDIT / 'ecoli-consultation/core-contribution-followup/preservation.json')['authorized_superseded_paths']
    edges = {p: [(v['before_sha256'], v['after_sha256'])] for p, v in current_edges.items()}
    assert len(edges) == 9
    for p, v in old_edges.items():
        edges.setdefault(p, []).append((v['before'], v['after']))
    inputs, transitions = {}, []

    def capture(path, expected=None, origin='current dependency'):
        path = Path(path)
        path = path if path.is_absolute() else ROOT / path
        name = str(path.relative_to(ROOT))
        actual = sha(path)
        if expected and expected != actual:
            assert (expected, actual) in edges.get(name, []), (name, expected, actual, origin)
            transitions.append({'path': name, 'before': expected, 'after': actual, 'origin': origin})
        record = inputs.setdefault(name, {'sha256': actual, 'origins': []})
        assert record['sha256'] == actual, name
        if origin not in record['origins']:
            record['origins'].append(origin)
        return path

    # Shared project metadata is historical provenance, not a scientific mutation allowance.
    metadata = []
    metadata_receipt = HERE / 'project-metadata-provenance.json'
    for name in sorted(PROJECT):
        published = subprocess.check_output(['git', 'show', baseline['head'] + ':' + name], cwd=ROOT)
        published_sha = hashlib.sha256(published).hexdigest()
        if not metadata_receipt.exists():
            assert sha(ROOT / name) == published_sha, name
            assert subprocess.check_output(['git', 'show', 'HEAD:' + name], cwd=ROOT) == published
        metadata.append({'path': name, 'original_full_run_sha256': publication_inputs[name],
                         'published_pr_head_sha256': published_sha, 'head': baseline['head'],
                         'scope': 'Pre-existing post-full-run metadata; excluded from immutable scientific inputs.'})
    for path, digest in publication_inputs.items():
        if path not in PROJECT:
            capture(path, digest, 'original 375-file publication manifest')
    capture(publication, origin='original publication manifest itself')
    for path, digest in prior_inputs.items():
        capture(path, digest, 'published capacity input closure')
    for path, digest in baseline['protected'].items():
        capture(path, digest, 'frozen source-preservation pool')
    for path, digest in baseline['old_audit_and_family_files'].items():
        capture(path, digest, 'old audit/family bytes')
    manifests = []
    for path in sorted(AUDIT.rglob('handoff.json')):
        if HERE in path.parents:
            continue
        manifest = read(capture(path, origin='released handoff'))
        files = manifest.get('files', {})
        assert isinstance(files, dict), path
        for name, digest in files.items():
            capture(name, digest, 'manifest ' + str(path.relative_to(ROOT)))
        manifests.append({'path': str(path.relative_to(ROOT)), 'sha256': sha(path), 'files': len(files)})
    for path in sorted(prior.rglob('*')):
        if path.is_file() and '__pycache__' not in path.parts:
            capture(path, origin='all old capacity receipts')
    # Retain exact separately acquired source inputs and their quote checks.
    for path in [AUDIT / 'literature-consultation/source-sha256.json',
                 AUDIT / 'ecoli-consultation/additional-protected.json']:
        source_map = read(capture(path, origin='source dependency map'))
        for name, digest in source_map.get('files', source_map).items():
            capture(name, digest, 'source dependency map ' + str(path.relative_to(ROOT)))
    panel = read(followup / 'published-panel-baseline.json')
    docs = {}
    row_count = historical_new = retired = 0
    for name, seed in panel.items():
        doc = yaml.safe_load(capture(name, origin='current panel').read_text())
        old, new = seed['document']['existing_annotations'], doc['existing_annotations']
        assert len(old) == len(new)
        for a, b in zip(old, new, strict=True):
            assert {k: v for k, v in a.items() if k != 'review'} == {k: v for k, v in b.items() if k != 'review'}
            assert (a['review']['action'] == 'NEW') == (b['review']['action'] == 'NEW')
            historical_new += b['review']['action'] == 'NEW'
            retired += b.get('retired', False)
        row_count += len(new)
        docs[name] = doc
    assert (len(docs), row_count, historical_new, retired) == (9, 93, 2, 0)
    for name in ['modules/bacterial_mannose_pts.yaml',
                 'interpro/panther/PTHR33799/PTHR33799-review.yaml',
                 'interpro/panther/PTHR32502/PTHR32502-review.yaml']:
        docs[name] = yaml.safe_load(capture(name, origin='current family/module').read_text())
    old_closure = imported('old_closure', prior / 'check_closure.py')
    validator, _ = build_supporting_text_validator(ROOT / 'publications')
    quotes, references = [], []
    for name, doc in docs.items():
        for ref, text in sorted(set(old_closure.quotes(doc))):
            if ref.startswith('file:'):
                source = resolve_local_source(ref, ROOT)
                assert source and quote_matches(text, source), (name, ref, text)
            else:
                assert ref.startswith('PMID:'), (name, ref)
                result = validator.validate(text, ref)
                assert result.is_valid and not result.skipped, (name, ref, result.message)
                source = ROOT / 'publications' / (ref.replace(':', '_') + '.md')
            capture(source, origin='current quoted source')
            quotes.append({'document': name, 'reference': ref, 'quote': text,
                           'source': str(source.relative_to(ROOT)), 'sha256': sha(source)})
        refs = set()
        for text in strings(doc):
            refs.update(re.findall(r'PMID:\d+', text))
            if text.startswith('file:'):
                refs.add(text)
        for ref in sorted(refs):
            if ref.startswith('PMID:'):
                source = ROOT / 'publications' / (ref.replace(':', '_') + '.md')
            else:
                source = resolve_local_source(ref, ROOT)
                assert source, (name, ref)
            capture(source, origin='current reference anywhere in document')
            references.append({'document': name, 'reference': ref, 'source': str(source.relative_to(ROOT))})
    ledger = yaml.safe_load((AUDIT / 'literature-consultation/evidence-ledger.yaml').read_text())
    for item in ledger:
        source = capture(item['consulted_source'], origin='full externally acquired primary/review')
        text = source.read_text()
        if source.suffix == '.html':
            text = BeautifulSoup(text, 'html.parser').get_text(' ', strip=True)
        assert item['supporting_text'] in re.sub(r'\s+', ' ', text).strip(), item['id']
    cap = imported('old_capacity', prior / 'check_capacity.py')
    cap.HERE = HERE / 'capacity-rerun'
    cap.HERE.mkdir(exist_ok=True)
    cap.main()
    now = read(cap.HERE / 'results.json')
    then = read(prior / 'results.json')
    followup_results = read(followup / 'capacity-rerun/results.json')
    for field in ['cases', 'case_count', 'mutations', 'mutation_count', 'sensitivities', 'sensitivity_count',
                  'compiled_atoms', 'core_atoms', 'bare_boolean_all_atoms_true_false_positives']:
        assert now[field] == then[field] == followup_results[field], field
    assert (now['case_count'], now['mutation_count'], now['sensitivity_count']) == (60, 13, 9)
    assert set(prior_inputs) <= set(inputs)
    assert set(publication_inputs) - PROJECT <= set(inputs)
    actual_deviations = {p for p, v in publication_inputs.items() if p not in PROJECT and sha(ROOT / p) != v}
    assert actual_deviations == set(current_edges)
    result = {'status': 'PASS', 'input_count': len(inputs), 'prior_capacity_inputs_retained': len(prior_inputs),
              'prior_publication_paths_retained': len(publication_inputs), 'metadata_provenance_only': len(PROJECT),
              'science_superseded_paths': sorted(current_edges), 'whole_panel_rows': row_count,
              'historical_NEW': historical_new, 'active_NEW': historical_new, 'retired': retired,
              'quote_count': len(quotes), 'external_quote_count': len(ledger), 'references': len(references),
              'capacity_exact_prior_expectations': True, 'capacity_cases': 60, 'model_mutations': 13, 'sensitivities': 9,
              'handoffs': manifests, 'full_corpus_status': 'NOT_RUN_FOR_CURRENT_FOLLOWUP',
              'old_full_proof': str((AUDIT / 'full-validation-proof.json').relative_to(ROOT))}
    outputs = {'input-map.json': inputs, 'supersession-chain.json': transitions,
               'project-metadata-provenance.json': metadata, 'quotes.json': quotes,
               'references.json': references, 'results.json': result,
               'required-ignored-source-paths.json': {p: v for p, v in inputs.items()
                                                     if p.startswith('.cache/') and 'frozen source-preservation pool' not in v['origins']}}
    for name, data in outputs.items():
        path = HERE / name
        if path.exists():
            assert read(path) == data, ('Frozen closure mismatch', name)
        else:
            path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({k: v for k, v in result.items() if not isinstance(v, (dict, list))}))


if __name__ == '__main__':
    main()
