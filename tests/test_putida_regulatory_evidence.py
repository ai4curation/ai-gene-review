"""Reject machine-readable regulatory records that misidentify or overstate evidence."""
import copy
import importlib.util
from pathlib import Path

import jsonschema
import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('regulatory_check', ROOT / 'projects/P_PUTIDA/validate_regulatory_evidence.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


@pytest.fixture
def case():
    data = yaml.safe_load((ROOT / 'genes/PSEPK/BenR/BenR-regulatory-evidence.yaml').read_text())
    review = yaml.safe_load((ROOT / 'genes/PSEPK/BenR/BenR-ai-review.yaml').read_text())
    schema = yaml.safe_load(checker.SCHEMA.read_text())
    metadata = {'Q88I42': {'Gene Names': 'benR PP_3159', 'Organism (ID)': '160488'},
                'target': {'Gene Names': 'benA PP_3161', 'Organism (ID)': '160488'}}
    return data, review, metadata, schema


def test_valid_record_retains_unknown_directness(case):
    data, review, metadata, schema = case
    assert checker.check_record(data, review, metadata, schema)
    assert data['relationships'][0]['directness'] == 'unresolved'


@pytest.mark.parametrize('error', ['wrong_locus', 'wrong_taxon', 'undeclared_reference', 'duplicate_id', 'missing_assay', 'pathway_execution'])
def test_reject_bad_evidence_record(case, error):
    data, review, metadata, schema = copy.deepcopy(case)
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
    with pytest.raises((ValueError, jsonschema.ValidationError)):
        checker.check_record(data, review, metadata, schema)
