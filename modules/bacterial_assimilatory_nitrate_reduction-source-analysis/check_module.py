"""Validate the bounded native nitrate panel with the production module validator.

Run from the repository root with ``uv run python <this-file>``. Family membership
is read from unedited target UniProt records; names are checked by the validator
against the committed PANTHER ontology. No global family-index download is needed.
"""
import json
from pathlib import Path
import re

import yaml

from ai_gene_review.validation.module_validator import validate_module_file

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATA = ROOT / "analysis/module_audits/bacterial_assimilatory_nitrate_reduction"


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def main():
    panel = yaml.safe_load((DATA / 'members.yaml').read_text())
    members, reviews = {}, {}
    for member in panel:
        path = ROOT / member['path']
        doc = yaml.safe_load(path.read_text())
        accession = member['accession']
        assert doc['id'] == accession
        assert doc['taxon']['id'] == 'NCBITaxon:' + str(member['taxon_id'])
        raw = path.with_name(member['gene'] + '-uniprot.txt').read_text()
        assert re.search(r'^AC   ' + re.escape(accession) + r';', raw, re.M)
        assert re.search(r'NCBI_TaxID=' + str(member['taxon_id']) + r'(?:\s|;)', raw)
        families = re.findall(r'^DR   PANTHER; ([^;]+);', raw, re.M)
        if families:
            members[accession] = next((family for family in families if ':SF' in family), families[0])
        assert all(row['review']['action'] != 'PENDING' for row in doc['existing_annotations'])
        reviews[accession] = path
    path = ROOT / 'modules/bacterial_assimilatory_nitrate_reduction.yaml'
    doc = yaml.safe_load(path.read_text())
    used = {node['id'].split(':', 1)[1] for node in walk(doc['module'])
            if str(node.get('id', '')).startswith('UniProtKB:')}
    assert used == set(reviews), (used - set(reviews), set(reviews) - used)
    activities = [a for node in walk(doc['module']) for a in node.get('annotons', [])]
    connections = [c for node in walk(doc['module']) for c in node.get('connections', [])]
    assert all(a.get('evidence') for a in activities)
    assert all(c.get('evidence') for c in connections)
    assert not any(str(node.get('source_id', '')).endswith('-ai-review.yaml') for node in walk(doc))
    result = validate_module_file(path, member_index=members, gene_index=reviews)
    report = {'valid': result.is_valid, 'errors': result.errors, 'warnings': result.warnings,
              'members': len(panel), 'activities': len(activities), 'connections': len(connections),
              'references': len(doc.get('references', [])),
              'findings': sum(len(ref.get('findings', [])) for ref in doc.get('references', [])),
              'member_classifications': members}
    (DATA / 'validation-results.yaml').write_text(yaml.safe_dump(report, sort_keys=False, allow_unicode=True))
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if result.is_valid else 1)


if __name__ == '__main__':
    main()
