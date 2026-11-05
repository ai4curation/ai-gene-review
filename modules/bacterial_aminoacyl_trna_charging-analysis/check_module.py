"""Validate the bounded 42-member module without building a global family index.

Run from the repository root: uv run python modules/bacterial_aminoacyl_trna_charging-analysis/check_module.py
Membership comes from unedited target UniProt records, not curated module labels.
"""
import json
from pathlib import Path
import re

import yaml
from ai_gene_review.validation.module_validator import validate_module_file

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def main():
    members = json.loads((HERE / 'members.json').read_text())
    mapping, gene_index = {}, {}
    for entry in members:
        path = ROOT / entry['path']
        review = yaml.safe_load(path.read_text())
        accession = entry['accession']
        assert review['id'] == accession, path
        raw = path.with_name(entry['gene'] + '-uniprot.txt').read_text()
        assert re.search(r'^AC   ' + re.escape(accession) + r';', raw, re.M), path
        assert review['taxon']['id'] == 'NCBITaxon:' + str(entry['taxon_id']), path
        assert re.search(r'NCBI_TaxID=' + str(entry['taxon_id']) + r'(?:\s|;)', raw), path
        families = re.findall(r'^DR   PANTHER; ([^;]+);', raw, re.M)
        if families:
            mapping[accession] = next((f for f in families if ':SF' in f), families[0])
        gene_index[accession] = path
    path = ROOT / 'modules/bacterial_aminoacyl_trna_charging.yaml'
    doc = yaml.safe_load(path.read_text())
    used = {x['id'].split(':', 1)[1] for x in walk(doc['module']) if str(x.get('id', '')).startswith('UniProtKB:')}
    assert used == set(gene_index), (used-set(gene_index), set(gene_index)-used)
    annotons = [a for x in walk(doc['module']) for a in x.get('annotons', [])]
    edges = [e for x in walk(doc['module']) for e in x.get('connections', [])]
    assert all(a.get('evidence') for a in annotons)
    assert all(e.get('evidence') for e in edges)
    result = validate_module_file(path, member_index=mapping, gene_index=gene_index)
    report = {'valid':result.is_valid,'errors':result.errors,'warnings':result.warnings,'members':len(members),'activities':len(annotons),'connections':len(edges),'references':len(doc['references']),'findings':sum(len(r.get('findings',[])) for r in doc['references']),'member_mapping':mapping}
    (HERE / 'validation-results.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    raise SystemExit(0 if result.is_valid else 1)


if __name__ == '__main__':
    main()
