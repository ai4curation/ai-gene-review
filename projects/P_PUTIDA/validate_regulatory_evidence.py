#!/usr/bin/env python3
"""Check sidecar structure, source quotations and accession/locus/taxon joins.

This does not verify experimental interpretation or remotely re-fetch articles.
Run after manual curation, alongside the standard gene-review validator.
"""
import argparse
import csv
from pathlib import Path

import yaml

from ai_gene_review.validation.quote_check import Outcome, check_document

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / 'projects/P_PUTIDA/tf_census/regulatory-evidence.schema.yaml'
METADATA = ROOT / 'projects/P_PUTIDA/data/psepk_uniprot_metadata.tsv'


def make_validator():
    """Use LinkML's standard backend, generated solely from the LinkML schema."""
    # This project validation tool requires the development dependency group.
    from linkml.validator import Validator
    from linkml.validator.plugins import JsonschemaValidationPlugin

    return Validator(SCHEMA, validation_plugins=[JsonschemaValidationPlugin(closed=True)])


def check_structure(data, validator, target_class='RegulatoryEvidence'):
    """Validate a complete record or a snippet against its LinkML class."""
    report = validator.validate(data, target_class)
    if report.results:
        raise ValueError('\n'.join(result.message for result in report.results))


def check_record(data, review, metadata, validator):
    check_structure(data, validator)
    regulator = data['regulator']
    accession = regulator['accession']
    if accession != review['id'].removeprefix('UniProtKB:') or regulator['taxon'] != review['taxon']['id']:
        raise ValueError('Sidecar regulator does not match gene-review accession/taxon')
    protein = metadata.get(accession)
    if not protein or regulator['locus'] not in protein['Gene Names'].split() or regulator['taxon'] != 'NCBITaxon:' + protein['Organism (ID)']:
        raise ValueError('Regulator accession/locus/taxon does not match reference metadata')
    loci = {n for row in metadata.values() for n in row['Gene Names'].split() if n.startswith('PP_')}
    reference_ids = {r['id'] for r in review.get('references', [])}
    ids = set()
    for assertion in data['relationships']:
        if assertion['id'] in ids:
            raise ValueError(f'Duplicate relationship ID: {assertion["id"]}')
        ids.add(assertion['id'])
        if assertion['target'].get('locus') and assertion['target']['locus'] not in loci:
            raise ValueError(f'Target locus absent from reference metadata: {assertion["target"]["locus"]}')
    for assertion in [*data['relationships'], *data.get('pathway_context', [])]:
        for evidence in assertion['evidence']:
            if evidence['reference_id'] not in reference_ids:
                raise ValueError(f'Undeclared gene-review reference: {evidence["reference_id"]}')
    check_quotes(data)
    return ids


def check_quotes(data):
    """Require every quotation to match a readable source, without a baseline waiver."""
    failures = [result for result in check_document(data, project_root=ROOT, baseline={})
                if result.outcome != Outcome.VERIFIED]
    if failures:
        raise ValueError('\n'.join(
            f'{result.quote.path} [{result.quote.reference_id}]: {result.detail}'
            for result in failures
        ))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files', type=Path, nargs='+')
    args = parser.parse_args()
    validator = make_validator()
    with METADATA.open() as handle:
        metadata = {r['Entry']: r for r in csv.DictReader(handle, delimiter='\t')}
    seen = set()
    for path in args.files:
        data = yaml.safe_load(path.read_text())
        review_path = path.with_name(path.name.replace('-regulatory-evidence.yaml', '-ai-review.yaml'))
        review = yaml.safe_load(review_path.read_text())
        ids = check_record(data, review, metadata, validator)
        if ids & seen:
            raise ValueError(f'Duplicate IDs across files: {sorted(ids & seen)}')
        seen.update(ids)
        for reference in review.get('references', []):
            if reference['id'].startswith('PMID:'):
                cache = ROOT / 'publications' / (reference['id'].replace(':', '_') + '.md')
                if not cache.exists():
                    raise ValueError(f'Uncached PMID: {reference["id"]}')
        print(f'PASS {path}: {len(ids)} relationships; structure, identity, reference links and quotes checked')
    print('Experimental support and pathway interpretation require manual review; not certified by this validator.')


if __name__ == '__main__':
    main()
