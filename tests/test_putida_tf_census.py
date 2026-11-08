"""Regression checks for identity reconciliation and biological scope boundaries."""
import importlib.util
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('putida_tf_census', ROOT / 'projects/P_PUTIDA/build_tf_census.py')
census = importlib.util.module_from_spec(spec)
spec.loader.exec_module(census)


@pytest.fixture
def classification_inputs():
    rules = yaml.safe_load((ROOT / 'projects/P_PUTIDA/tf_census/rules.yaml').read_text())
    # Only the ontology facts needed for these scope-boundary regressions.
    go = {'GO:0003700': {'ids': ['GO:0003700', 'GO:0016987']}, 'GO:0016987': {'ids': ['GO:0016987']}}
    return rules, go


def protein(name, pfam='', go=''):
    return {'Protein names': name, 'InterPro': '', 'Pfam': pfam, 'Gene Ontology IDs': go}


@pytest.mark.parametrize('row,expected', [
    (protein('Sigma-54 dependent transcriptional regulator', 'PF00158'), 'dbtf_candidate'),
    (protein('RNA polymerase subunit sigma-24', 'PF04542', 'GO:0016987'), 'sigma_factor_candidate'),
    (protein('Negative regulator of flagellin synthesis (Anti-sigma-28 factor)'), 'transcription_machinery_or_cofactor_candidate'),
    (protein('Response regulator for chemotactic signal transduction', 'PF00072'), 'other_signaling_candidate'),
    (protein('Response regulator', 'PF00072'), 'ambiguous_candidate'),
    (protein('Ribosomal RNA small subunit methyltransferase A'), 'nonregulatory_candidate'),
    (protein('RNA-binding protein Hfq', 'PF17209', 'GO:0003700'), 'post_transcriptional_regulator_candidate'),
    (protein('Fused DNA alkyltransferase-transcriptional activator'), 'dbtf_candidate'),
])
def test_role_boundaries(classification_inputs, row, expected):
    rules, go = classification_inputs
    assert census.classify(row, {}, go, rules)[0] == expected


def test_external_assignment_is_not_tf_identity(classification_inputs):
    rules, go = classification_inputs
    row = protein('Uncharacterized protein')
    assert census.classify(row, {}, go, rules, external=True)[0] == 'ambiguous_candidate'


def test_strong_identifiers_do_not_fall_back_to_symbols():
    index = census.IdentityIndex([
        {'Entry': 'Q1', 'Gene Names': 'fur PP_0119'},
        {'Entry': 'Q2', 'Gene Names': 'fur PP_4730'},
    ], [])
    assert index.resolve(name='Fur') == ('ambiguous', 'alias', {'Q1', 'Q2'})
    assert index.resolve(locus='PP0119', name='Fur') == ('mapped', 'locus', {'Q1'})
    assert index.resolve(accession='MISSING', locus='PP0119', name='Fur') == ('unmapped', 'accession', set())
    assert index.resolve(locus='PP9999', name='fur') == ('unmapped', 'locus', set())


def test_review_alias_must_have_matching_accession_and_taxon():
    rows = [{'Entry': 'Q1', 'Gene Names': 'uvrY PP_4099'}]
    reviews = [
        {'accession': 'Q1', 'gene_symbol': 'gacA', 'taxon_id': '160488'},
        {'accession': 'Q1', 'gene_symbol': 'wrong_species', 'taxon_id': '9606'},
        {'accession': 'Q2', 'gene_symbol': 'wrong_accession', 'taxon_id': '160488'},
    ]
    index = census.IdentityIndex(rows, reviews)
    assert index.resolve(name='GacA')[2] == {'Q1'}
    assert index.resolve(name='wrong_species')[0] == 'unmapped'
    assert index.resolve(name='wrong_accession')[0] == 'unmapped'


def test_module_assignments_keep_unassigned_and_multiple_modules():
    precise = {
        'regulators': [{'source_name': 'Zur', 'locus_tag': 'PP_0119', 'upstream_evidence': ['RegPrecise']}],
        'regulator_gene_records': [],
        'modules': [{'module_id': 'Zur-1', 'regulator': 'Zur'}, {'module_id': 'Zur-2', 'regulator': 'Zur'}, {'module_id': 'Unknown', 'regulator': None}],
    }
    rows = census.external_records([], precise)
    assignments = [r for r in rows if r['source'] == 'PRECISE321_MODULE']
    assert [r['module_id'] for r in assignments] == ['Zur-1', 'Zur-2', 'Unknown']
    assert assignments[0]['loci'] == ['PP_0119']
    assert not assignments[-1]['protein_record']


def test_regprecise_multiple_loci_are_not_a_composite_identifier():
    rows = census.external_records([{
        'source_id': '1', 'source_name': 'MetR', 'locus_tag': 'PP1063 , PP2696',
        'record_type': 'TF', 'url': 'https://example.org/regulon/1', 'family': 'LysR',
    }], {'regulators': [], 'regulator_gene_records': [], 'modules': []})
    assert rows[0]['loci'] == ['PP1063', 'PP2696']


def test_declared_complete_does_not_hide_pending_rows(tmp_path):
    folder = tmp_path / 'gene'
    folder.mkdir()
    (folder / 'gene-ai-review.yaml').write_text('''id: Q1
gene_symbol: gene
status: COMPLETE
taxon: {id: 'NCBITaxon:160488'}
existing_annotations:
- term: {id: 'GO:0003700'}
- term: {id: 'GO:0003677'}
  review: {action: null}
''')
    row = census.load_reviews(tmp_path)[0]
    assert row['declared_status'] == 'COMPLETE'
    assert row['pending_rows'] == 2
    assert row['has_core_functions'] is False
    assert row['validation_status'] == 'not_run'
