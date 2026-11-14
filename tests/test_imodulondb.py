"""Guard the biological distinctions and source-integrity failures of the importer."""
import copy
import json
from pathlib import Path

import pytest

from ai_gene_review.imodulondb import (
    IModulonDBClient, ImportErrorDetail, SourceCache, check_matrix, csv_rows,
    digest, optional_number, parse_members, parse_module_table, regulator_tokens,
    resolve_identity,
)

ROOT = Path(__file__).resolve().parents[1]


def test_absent_measurements_are_not_zero_or_rank_weights():
    assert optional_number('') is None
    assert optional_number('NaN') is None
    assert optional_number('0') == 0
    members = parse_members(b'locus,gene_name,gene_product\nPP_0001,x,enzyme\n')
    assert members[0]['weight'] is None
    modules = parse_module_table(b'k,name,regulator_readable,n_genes,precision,recall\n9,unknown,,0,,0\n')
    assert modules['9']['source_reference_regulon_metrics']['precision'] is None
    assert modules['9']['source_reference_regulon_metrics']['recall'] == 0
    assert modules['9']['regulator_expression'] is None


@pytest.mark.parametrize('value', ['inf', '-inf', 'Infinity', 'not-a-number'])
def test_nonfinite_measurements_fail(value):
    with pytest.raises(ImportErrorDetail):
        optional_number(value)


def matrix_fixture():
    return {
        '2': {'source_member_count': 1, 'members': [{'locus': 'PP_0001', 'weight': -.2}]},
        '7': {'source_member_count': 1, 'members': [{'locus': 'PP_0002', 'weight': .3}]},
    }


def test_matrix_joins_named_columns_and_checks_source_thresholds():
    modules = matrix_fixture()
    checks = check_matrix(b',7,2\nPP_0001,0.05,-0.2\nPP_0002,0.3,0.01\n', modules, {'2': .1, '7': .2})
    assert checks['module_count'] == 2
    assert all(m['threshold_check'] == 'passed' for m in modules.values())


@pytest.mark.parametrize('matrix,thresholds', [
    (b',7,7\nPP_0001,.2,.2\n', {'2': .1, '7': .2}),
    (b',2,7\nPP_0001,-.2,.05\nPP_0001,.01,.3\n', {'2': .1, '7': .2}),
    (b',2,7\nPP_0001,-.2,.05\nPP_0002,.01,.3\n', {'2': .1}),
    (b',2,7\nPP_0001,-.2,.05\nPP_0002,.01,.3\n', {'2': .3, '7': .2}),
    (b',2,7\nPP_0001,-.21,.05\nPP_0002,.01,.3\n', {'2': .1, '7': .2}),
    (b',2,7\nPP_0001,-.2,.05\n', {'2': .1, '7': .2}),
])
def test_incompatible_source_data_fail(matrix, thresholds):
    with pytest.raises(ImportErrorDetail):
        check_matrix(matrix, matrix_fixture(), thresholds)


def test_csv_duplicate_headers_and_members_fail():
    with pytest.raises(ImportErrorDetail):
        csv_rows(b'locus,locus\nx,x\n', {'locus'})
    with pytest.raises(ImportErrorDetail):
        parse_members(b'locus,gene_name,gene_product\nx,a,p\nx,b,q\n')


def test_cache_fails_offline_and_on_tampering(tmp_path):
    cache = SourceCache(tmp_path, offline=True)
    url = 'https://example.org/versioned.csv'
    with pytest.raises(ImportErrorDetail, match='Not cached'):
        cache.get(url)
    path = tmp_path / digest(url.encode())
    path.write_bytes(b'correct')
    path.with_suffix('.json').write_text(json.dumps({'url': url, 'sha256': digest(b'correct')}))
    assert cache.get(url) == b'correct'
    path.write_bytes(b'tampered')
    with pytest.raises(ImportErrorDetail, match='integrity'):
        cache.get(url)


@pytest.fixture
def identity_dataset(tmp_path):
    (tmp_path / 'metadata.tsv').write_text(
        'Entry\tOrganism (ID)\tGene Names\tProtein names\n'
        'Q88I42\t160488\tfur PP_0001\tregulator\n'
        'Q88DX2\t160488\tfur PP_0002\tregulator\n')
    return {
        'organism': {'canonical_organism': 'PSEPK', 'metadata_path': 'metadata.tsv', 'taxon_id': 'NCBITaxon:160488'},
        'source_gene_identities': [],
        'source_regulator_identities': [{'name': 'Zur', 'locus': 'PP_0001'}],
        'modules': [], 'checks': {}, 'source_manifest': {}, 'importer_sha256': 'test',
    }


def test_alias_ambiguity_and_strong_identifier_precedence(identity_dataset, tmp_path):
    with pytest.raises(ImportErrorDetail, match='Ambiguous'):
        resolve_identity(identity_dataset, 'fur', tmp_path)
    identity, _, _, names = resolve_identity(identity_dataset, 'PP0001', tmp_path)
    assert identity['accession'] == 'Q88I42'
    assert identity['report_name'] == 'Q88I42'  # nonunique symbols cannot collide
    assert names == {'zur'}
    assert resolve_identity(identity_dataset, 'P06519', tmp_path)[0]['status'] == 'outside_reference_or_unresolved'


def test_multiple_assignments_are_separate_from_gene_membership(identity_dataset, tmp_path):
    expression = 'Zur and GltR-II'
    assert regulator_tokens(expression) == ['Zur', 'GltR-II']
    dataset = copy.deepcopy(identity_dataset)
    dataset['modules'] = [
        {'module_id': '1', 'name': 'Zur-1', 'regulator_expression': expression,
         'regulator_tokens': regulator_tokens(expression), 'members': []},
        {'module_id': '2', 'name': 'Zur-2', 'regulator_tokens': ['Zur'], 'members': []},
        {'module_id': '3', 'name': 'stress', 'regulator_tokens': [],
         'members': [{'locus': 'PP_0001', 'weight': -.4}]},
    ]
    client = IModulonDBClient(tmp_path / 'cache')
    client.loaded['PSEPK'] = dataset
    result = client.summarize('p_putida', 'Q88I42', repo_root=tmp_path)
    assert [m['module_id'] for m in result['assigned_modules']] == ['1', '2']
    assert result['assigned_modules'][0]['regulator_expression'] == expression
    assert [m['module_id'] for m in result['gene_memberships']] == ['3']
    assert result['target_comparison_status'] == 'not_performed_no_structured_curated_target_set'


def test_published_benr_membership_regression():
    dataset = json.loads((ROOT / 'projects/P_PUTIDA/tf_census/imodulon/dataset.json').read_text())
    benr = next(m for m in dataset['modules'] if m['name'] == 'BenR')
    assert len(dataset['modules']) == 84
    assert benr['module_id'] == '27'
    assert {m['locus'] for m in benr['members']} == {
        'PP_3161', 'PP_3162', 'PP_3163', 'PP_3164', 'PP_3165',
        'PP_3166', 'PP_3167', 'PP_3713', 'PP_3714', 'PP_3715',
    }
    assert benr['threshold'] == pytest.approx(.12821891758582343)
    assert all(m['threshold_check'] == 'passed' for m in dataset['modules'])


def test_legacy_alias_writes_canonical_review_directory(tmp_path):
    client = IModulonDBClient(tmp_path / 'cache', offline=True)
    client.loaded['PSEPK'] = json.loads((ROOT / 'projects/P_PUTIDA/tf_census/imodulon/dataset.json').read_text())
    result = client.compare_with_review('p_putida', 'PP_3159', tmp_path)
    assert result['identity']['accession'] == 'Q88I42'
    assert (tmp_path / 'genes/PSEPK/BenR/BenR-imodulondb-comparison.md').exists()
    assert not (tmp_path / 'genes/p_putida').exists()
