"""Reject machine-readable regulatory records that misidentify or overstate evidence."""
import copy
import importlib.util
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('regulatory_check', ROOT / 'projects/P_PUTIDA/validate_regulatory_evidence.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


@pytest.fixture(scope="module")
def validator():
    return checker.make_validator()


@pytest.fixture
def case():
    data = yaml.safe_load((ROOT / 'genes/PSEPK/BenR/BenR-regulatory-evidence.yaml').read_text())
    review = yaml.safe_load((ROOT / 'genes/PSEPK/BenR/BenR-ai-review.yaml').read_text())
    metadata = {'Q88I42': {'Gene Names': 'benR PP_3159', 'Organism (ID)': '160488'},
                'target': {'Gene Names': 'benA PP_3161', 'Organism (ID)': '160488'}}
    return data, review, metadata


def test_valid_record_retains_unknown_directness(case, validator):
    data, review, metadata = case
    assert checker.check_record(data, review, metadata, validator)
    assert data['relationships'][0]['directness'] == 'unresolved'


@pytest.mark.parametrize('error', ['wrong_locus', 'wrong_taxon', 'undeclared_reference', 'duplicate_id', 'missing_assay', 'pathway_execution'])
def test_reject_bad_evidence_record(case, validator, error):
    data, review, metadata = copy.deepcopy(case)
    if error == 'wrong_locus':
        data['regulator']['locus'] = 'PP_3161'
    elif error == 'wrong_taxon':
        data['regulator']['taxon'] = 'NCBITaxon:303'
    elif error == 'undeclared_reference':
        data['relationships'][0]['evidence'][0]['reference_id'] = 'PMID:999999999'
    elif error == 'duplicate_id':
        data['relationships'].append(copy.deepcopy(data['relationships'][0]))
    elif error == 'missing_assay':
        del data['relationships'][0]['evidence'][0]['assay']
    elif error == 'pathway_execution':
        data['pathway_context'][0]['relationship'] = 'involved_in'
    with pytest.raises(ValueError):
        checker.check_record(data, review, metadata, validator)


@pytest.mark.parametrize('target_class,select', [
    ('RegulatorIdentity', lambda d: d['regulator']),
    ('RegulatoryRelationship', lambda d: d['relationships'][0]),
    ('RegulatoryTarget', lambda d: d['relationships'][0]['target']),
    ('RegulatoryEvidenceItem', lambda d: d['relationships'][0]['evidence'][0]),
    ('PathwayContext', lambda d: d['pathway_context'][0]),
    ('RegulatoryProcessTerm', lambda d: d['pathway_context'][0]['process']),
])
def test_validate_standalone_snippet(case, validator, target_class, select):
    snippet = copy.deepcopy(select(case[0]))
    checker.check_structure(snippet, validator, target_class)
    with pytest.raises(ValueError):
        checker.check_structure({}, validator, target_class)


@pytest.mark.parametrize('error', ['blank_assay', 'empty_evidence', 'empty_limitations',
                                 'unknown_field', 'invalid_effect', 'bad_reference'])
def test_relationship_snippet_constraints(case, validator, error):
    snippet = copy.deepcopy(case[0]['relationships'][0])
    if error == 'blank_assay':
        snippet['evidence'][0]['assay'] = '   '
    elif error == 'empty_evidence':
        snippet['evidence'] = []
    elif error == 'empty_limitations':
        snippet['limitations'] = []
    elif error == 'unknown_field':
        snippet['unrecognized'] = True
    elif error == 'invalid_effect':
        snippet['effect'] = 'catalyzes'
    elif error == 'bad_reference':
        snippet['evidence'][0]['reference_id'] = 'unsupported:123'
    with pytest.raises(ValueError):
        checker.check_structure(snippet, validator, 'RegulatoryRelationship')
