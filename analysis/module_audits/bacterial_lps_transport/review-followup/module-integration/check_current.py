"""Additive LPS closure and production capacity checks; historical files are read-only."""
import gzip
import hashlib
import importlib.util
import io
import json
import sys
from pathlib import Path
from unittest.mock import patch

import yaml
from Bio import SeqIO

from ai_gene_review.validation.local_source_text import quote_matches, resolve_local_source
from ai_gene_review.validation.supporting_text import build_supporting_text_validator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
AUDIT = HERE.parents[1]
PACK = HERE.parent / 'source-packaging'
LEGACY = AUDIT / 'capacity-consultation'
MODULE = ROOT / 'modules/bacterial_lps_transport.yaml'
MODULE_HISTORY = 'history/modules/bacterial_lps_transport/2026-11-07T115529Z-codex-586af7.yaml'
NOTE = 'Lineages without a curated terminal profile have unknown coverage here, not demonstrated absence of LPS transport capacity.'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def write_json(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + '\n')


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main():
    inputs, consumed_replacements, superseded, manifests = {}, {}, {}, {}
    replacements = read_json(PACK / 'replacement-map.json')['replacements']
    changes = read_json(HERE.parent / 'implementation/supersession.json')['changes']
    deterministic = read_json(LEGACY / 'determinism-followup/receipt.json')
    for path, row in deterministic['changed_previously_frozen_files'].items():
        assert path not in changes
        changes[path] = {'before_sha256': row['old_expected_sha256'], 'after_sha256': row['new_sha256']}
    before_module = read_json(HERE / 'before.json')
    for path, expected in before_module['files_sha256'].items():
        changes[path] = {'before_sha256': expected, 'after_sha256': sha(ROOT / path)}

    def add(path, expected=None):
        full = Path(path)
        full = full if full.is_absolute() else ROOT / full
        relative = str(full.relative_to(ROOT))
        if relative in replacements:
            item = replacements[relative]
            assert expected is None or expected == item['original_sha256'], relative
            full = ROOT / item['replacement_path']
            assert sha(full) == item['replacement_sha256'], relative
            if item['mode'] == 'BYTE_IDENTICAL':
                assert sha(full) == item['original_sha256'], relative
            else:
                assert item['mode'] == 'SCOPED_EXCERPT' and not item['full_source_reconstructable']
                assert ' '.join(item['checked_quote'].split()) in ' '.join(full.read_text().split())
            consumed_replacements[relative] = item
            relative = item['replacement_path']
            expected = item['replacement_sha256']
        else:
            actual = sha(full)
            if expected is not None and actual != expected:
                allowed = changes.get(relative)
                assert allowed and expected == allowed['before_sha256'] and actual == allowed['after_sha256'], (relative, expected, actual)
                superseded[relative] = allowed
                expected = actual
        actual = sha(full)
        assert expected is None or actual == expected, relative
        assert not relative.startswith('.cache/'), relative
        assert relative not in inputs or inputs[relative] == actual
        inputs[relative] = actual
        return full

    # Every release, including its source_dependencies, is traversed. A narrow hash
    # chain authorizes exactly the documented scientific and deterministic updates.
    release_paths = sorted(AUDIT.glob('**/handoff*.json'))
    release_paths = [p for p in release_paths if HERE not in p.parents and PACK not in p.parents]
    dependency_fields = ('files', 'files_sha256', 'source_dependencies', 'protected_sources_sha256',
                         'previous_history_files_sha256')
    for release in release_paths:
        manifests[str(release.relative_to(ROOT))] = sha(add(release))
        data = read_json(release)
        for field in dependency_fields:
            for path, expected in data.get(field, {}).items():
                assert isinstance(expected, str) and len(expected) == 64, (release, field, path)
                add(path, expected)
        if isinstance(data.get('input_closure'), str):
            closure = add(data['input_closure'])
            for path, expected in read_json(closure)['inputs_sha256'].items():
                add(path, expected)

    historical = read_json(HERE / 'historical-artifacts.json')
    for path, expected in historical.items():
        assert sha(ROOT / path) == expected, ('historical artifact changed', path)
        add(path, expected)
    add(PACK / 'replacement-map.json')
    add(PACK / 'prepare.py')
    add(PACK / 'index-removal-paths.txt')
    add(HERE / 'before.json')
    add(ROOT / MODULE_HISTORY)
    add(ROOT / 'pages/modules/bacterial_lps_transport.html')
    add(Path(__file__))

    # The only module delta is a coverage note; topology, evidence and selectors
    # must compare exactly with the previously published document.
    current = yaml.safe_load(add(MODULE).read_text())
    comparison = yaml.safe_load(MODULE.read_text())
    variants = comparison['module']['parts'][2]['node']['variant_sets'][0]
    old_notes = before_module['module_document']['module']['parts'][2]['node']['variant_sets'][0]['notes']
    assert variants['id'] == 'terminal_lpt_profiles' and variants['notes'] == old_notes + ' ' + NOTE
    variants['notes'] = old_notes
    assert comparison == before_module['module_document'], 'unexpected module science delta'
    write_json('module-supersession.json', {'changes': {p: changes[p] for p in before_module['files_sha256']},
               'allowed_delta': 'module.parts[2].node.variant_sets[0].notes only', 'note': NOTE,
               'history': MODULE_HISTORY, 'status': 'PASS'})

    closure_lib = load('lps_historical_closure', LEGACY / 'check_closure.py')
    reviews, protected = {}, {}
    for name in ('baseline.json', 'additional-seed-baseline.json', 'accessory-seed-baseline.json'):
        baseline = read_json(add(AUDIT / name))
        reviews.update(baseline.get('reviews', baseline.get('genes')))
        for path, expected in baseline.get('protected_files_sha256', baseline.get('protected_sources', {})).items():
            protected[path] = sha(add(path, expected))
    assert len(reviews) == 19
    rows = historical_new = active_new = 0
    documents = {}
    for path, baseline in sorted(reviews.items()):
        doc = yaml.safe_load(add(path).read_text())
        old = baseline['document']
        assert doc['status'] == 'COMPLETE' and (doc['id'], doc['taxon']) == (old['id'], old['taxon'])
        assert len(old['existing_annotations']) == len(doc['existing_annotations'])
        for a, b in zip(old['existing_annotations'], doc['existing_annotations'], strict=True):
            assert {k: v for k, v in a.items() if k != 'review'} == {k: v for k, v in b.items() if k != 'review'}, path
            assert (a['review']['action'] == 'NEW') == (b['review']['action'] == 'NEW')
            rows += 1
            historical_new += b['review']['action'] == 'NEW'
            active_new += b['review']['action'] == 'NEW' and not b.get('retired', False)
        documents[path] = doc
    assert (rows, historical_new, active_new) == (214, 6, 6)
    documents[str(MODULE.relative_to(ROOT))] = current
    quoted = []
    validator, _ = build_supporting_text_validator(ROOT / 'publications')
    for path, doc in sorted(documents.items()):
        # Include references without quotations, not only the core's citations.
        for ref in doc.get('references', []):
            if ref['id'].startswith('PMID:'):
                add('publications/' + ref['id'].replace(':', '_') + '.md')
        for ref, text in sorted(set(closure_lib.quotes(doc))):
            if ref.startswith('file:'):
                source = resolve_local_source(ref, ROOT)
                assert source and quote_matches(text, source), (path, ref, text)
            else:
                assert ref.startswith('PMID:'), ref
                validation = validator.validate(text, ref)
                assert validation.is_valid and not validation.skipped, (path, ref, validation.message)
                source = ROOT / 'publications' / (ref.replace(':', '_') + '.md')
            source = add(source)
            quoted.append({'document': path, 'reference': ref, 'supporting_text': text,
                           'source': str(source.relative_to(ROOT)), 'source_sha256': sha(source)})
    ledger = yaml.safe_load(add(AUDIT / 'literature-consultation/ledger.yaml').read_text())
    for ref in ledger['references']:
        access = ref['access']
        add(access['publication_cache'])
        text = add(access['consulted_text'], access['consulted_text_sha256']).read_text()
        assert closure_lib.norm(ref['checked_quote']) in closure_lib.norm(text)
    for replacement in replacements.values():
        for path, expected in replacement.get('additional_scoped_evidence', {}).items():
            add(path, expected)

    identity_dir = AUDIT / 'literature-consultation/identity'
    identity = read_json(add(identity_dir / 'results.json'))
    archive = add('.cache/module-audit-logs/lps-20261107/literature-consultation/AEQZ01.dat.gz', identity['source']['sha256'])
    cds = [(r.id, f.qualifiers) for r in SeqIO.parse(io.StringIO(gzip.decompress(archive.read_bytes()).decode()), 'embl')
           for f in r.features if f.type == 'CDS' and 'translation' in f.qualifiers]
    assert len(cds) == 2423
    for bridge in identity['bridges']:
        target = read_json(add(identity_dir / (bridge['uniprot'] + '.json')))
        sequence = target['sequence']['value']
        assert hashlib.sha256(sequence.encode()).hexdigest() == bridge['sequence_sha256']
        hits = [(c, q) for c, q in cds if q['translation'][0] == sequence]
        assert len(hits) == 1
        contig, qualifiers = hits[0]
        assert (contig, qualifiers['locus_tag'], qualifiers['protein_id'], target['organism']['taxonId']) == (
            bridge['H44_contig'], [bridge['H44_locus']], [bridge['H44_protein']], bridge['target_taxon'])
    trees = read_json(add(AUDIT / 'family-consultation/tree-snapshot.json'))
    controls = {'Q9RS08': 'PTHR36504:SF1', 'Q9RSJ0': 'PTHR45772:SF10',
                'Q9RVF4': 'PTHR33529:SF2', 'Q9X257': 'PTHR30189:SF1'}
    for accession, subfamily in controls.items():
        tree = trees[subfamily.split(':')[0]]
        original = json.loads(gzip.decompress(add(tree['source'], tree['sha256']).read_bytes()))
        assert original['leaves'] == tree['leaves']
        assert any(x['uniprot'] == accession and x['subfamily'] == subfamily for x in original['leaves'].values())

    # Reuse the historical production-compiler oracle, redirecting only its outputs.
    capacity = load('lps_historical_capacity', add(LEGACY / 'check_capacity.py'))
    capacity.HERE = HERE
    capacity.main()
    for name in ('cases.json', 'results.json'):
        assert (HERE / name).read_bytes() == (LEGACY / name).read_bytes(), ('capacity regression', name)
    result = read_json(HERE / 'results.json')
    assert (result['case_count'], result['mutation_count'], result['gate_sensitivity_count']) == (56, 14, 7)
    for code in ('src/ai_gene_review/module_logic.py', 'src/ai_gene_review/module_gene_symbols.py',
                 'src/ai_gene_review/module_qc.py', 'src/ai_gene_review/render_modules.py',
                 'src/ai_gene_review/validation/local_source_text.py', 'src/ai_gene_review/validation/supporting_text.py'):
        add(code)
    assert len(consumed_replacements) == 9
    write_json('quotes.json', quoted)
    write_json('closure.json', {
        'status': 'PASS', 'review_count': 19, 'ordered_source_rows': rows,
        'historical_NEW': historical_new, 'active_NEW': active_new, 'retired_NEW': 0,
        'protected_seed_sources': len(protected), 'quote_count': len(quoted),
        'literature_quotes_checked': len(ledger['references']), 'identity_bridges_reverified': identity['bridges'],
        'family_controls': controls, 'module_sha256': sha(MODULE), 'manifests_sha256': manifests,
        'source_dependency_fields_unioned': list(dependency_fields), 'inputs_sha256': dict(sorted(inputs.items())),
        'authorized_supersessions_consumed': superseded, 'source_replacements_consumed': consumed_replacements,
        'historical_artifacts_byte_preserved': len(historical),
        'cache_inputs_opened': 0, 'complete_article_reconstruction_from_excerpts': False,
        'capacity': {'cases': 56, 'mutations': 14, 'sensitivities': 7, 'cases_and_results_byte_identical': True},
        'limitations': ['Full-text historical judgments beyond packaged excerpts are provenance-attested, not independently reproducible from excerpts.',
                       'Production Boolean compilation does not enforce substrate, ATP, interfaces, lineage or complex stoichiometry; the original independent role gates remain required.',
                       'EXACTLY_ONE is evaluated as OR; no missing-profile result proves absent biological capacity.']})
    print(json.dumps({'status': 'PASS', 'inputs': len(inputs), 'rows': rows, 'quotes': len(quoted), 'cache_reads': 0}))


if __name__ == '__main__':
    original_open = Path.open

    def no_original_cache(self, *args, **kwargs):
        """Prove current checks do not consume any of the nine original cache inputs."""
        resolved = self.resolve()
        assert (ROOT / '.cache/module-audit-logs/lps-20261107/literature-consultation') not in resolved.parents
        assert (ROOT / '.cache/panther_trees') not in resolved.parents
        return original_open(self, *args, **kwargs)

    with patch.object(Path, 'open', no_original_cache):
        main()
