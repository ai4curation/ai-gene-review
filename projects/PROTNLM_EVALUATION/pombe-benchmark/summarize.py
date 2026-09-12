"""Regenerate the pombe census from frozen inputs; no biological adjudication.

Usage: uv run python projects/PROTNLM_EVALUATION/pombe-benchmark/summarize.py
"""
from collections import Counter
import argparse
import csv
import gzip
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

NS = '{http://uniprot.org/uniprot}'
ET.register_namespace('', NS[1:-1])


def table(path):
    with path.open() as stream:
        return list(csv.DictReader(stream, delimiter='\t'))


def save(root, name, rows):
    if not rows:
        raise ValueError(f'Empty output: {name}')
    with (root / name).open('w') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def summarize(root):
    source = root / 'snapshot'
    manifest = json.loads((root / 'manifest.json').read_text())
    for name, checksum in manifest['checksums'].items():
        assert hashlib.sha256((source / name).read_bytes()).hexdigest() == checksum, name
    index = {row['Entry']: row for row in table(source / 'uniprot-pombe-index.tsv')}
    identifiers = {row['external_id']: row for row in table(source / 'pombase-identifiers.tsv')}
    published = table(source / 'published-accessions.tsv')
    public_ids = {row['Entry'] for row in published}
    records = {r['primaryAccession']: r for r in map(json.loads, gzip.open(source / 'uniprot.jsonl.gz', 'rt'))}
    api = {r['accession']: r for r in map(json.loads, gzip.open(source / 'api-availability.jsonl.gz', 'rt'))}
    inventory, statements, provenance, all_statements, comparisons = [], [], [], [], []
    elements = ET.parse(source / 'predictions.xml').getroot().findall(NS + 'entry')
    assert len(elements) == len(records) == len(api)
    for entry in elements:
        accession = entry.findtext(NS + 'accession')
        metadata, pom = index[accession], identifiers[accession]
        gene = pom['gene_name'] or pom['gene_systematic_id']
        gos = entry.findall(NS + "dbReference[@type='GO']")
        functions = [text for comment in entry.findall(NS + "comment[@type='function']") for text in comment.findall(NS + 'text')]
        evidence = {e.get('key'): ET.tostring(e, encoding='unicode') for e in entry.findall(NS + 'evidence')}
        inventory.append(dict(accession=accession, gene_symbol=gene, pombase_id=pom['gene_systematic_id'],
                              uniprot_gene_names=metadata['Gene Names'], current_length=metadata['Length'],
                              reviewed=metadata['Reviewed'], go_count=len(gos), function_count=len(functions),
                              in_public_pilot=accession in public_ids))
        claims = [('GO', g.get('id'), g.find(NS + "property[@type='term']").get('value'), g.get('evidence', '')) for g in gos]
        claims += [('function', '', f.text or '', f.get('evidence', '')) for f in functions]
        for kind, identifier, text, keys in claims:
            assert all(k in evidence for k in keys.split()), (accession, keys)
            row = dict(accession=accession, gene_symbol=gene, type=kind, id=identifier, text=text, evidence_keys=keys)
            statements.append(row)
            all_statements.append(row)
            provenance.append({**row, 'evidence_xml': json.dumps([evidence[k] for k in keys.split()])})
        for loc in entry.findall(NS + "comment[@type='subcellular location']/" + NS + 'subcellularLocation/' + NS + 'location'):
            all_statements.append(dict(accession=accession, gene_symbol=gene, type='location', id=loc.get('id', ''), text=loc.text or '', evidence_keys=loc.get('evidence', '')))
        for keyword in entry.findall(NS + 'keyword'):
            all_statements.append(dict(accession=accession, gene_symbol=gene, type='keyword', id=keyword.get('id', ''), text=keyword.text or '', evidence_keys=keyword.get('evidence', '')))
        response = api[accession]
        live = response['response']
        if response['status'] == 200:
            assert live['primaryAccession'] == accession
            api_go = [(g['id'], next(p['value'] for p in g['properties'] if p['key'] == 'GoTerm')) for g in live.get('uniProtKBCrossReferences', []) if g['database'] == 'GO']
            api_functions = [t['value'] for c in live.get('comments', []) if c['commentType'] == 'FUNCTION' for t in c.get('texts', [])]
            comparisons.append(dict(accession=accession, status=200,
                                    go_id_labels_match=Counter(api_go) == Counter((i,t) for k,i,t,e in claims if k == 'GO'),
                                    function_paragraphs_match=Counter(api_functions) == Counter(f.text or '' for f in functions),
                                    function_text_matches_ignoring_final_period=Counter(t.removesuffix('.') for t in api_functions) == Counter((f.text or '').removesuffix('.') for f in functions)))
        else:
            comparisons.append(dict(accession=accession, status=response['status'], go_id_labels_match=None, function_paragraphs_match=None, function_text_matches_ignoring_final_period=None))
    save(root, 'inventory.csv', inventory)
    save(root, 'functional-cohort.csv', [r for r in inventory if r['go_count'] or r['function_count']])
    save(root, 'functional-predictions.csv', statements)
    save(root, 'claim-provenance.csv', provenance)
    save(root, 'prediction-statements.csv', all_statements)
    save(root, 'api-source-comparison.csv', comparisons)
    with (root / 'sequences.fasta').open('w') as stream:
        for row in inventory:
            stream.write(f">{row['accession']} {row['gene_symbol']} {row['pombase_id']}\n{records[row['accession']]['sequence']['value']}\n")
    counts = Counter(r['type'] for r in all_statements)
    summary = dict(original_pombe_records=len(inventory), functional_cohort_records=sum(bool(r['go_count'] or r['function_count']) for r in inventory),
                   genes_with_go=sum(bool(r['go_count']) for r in inventory), genes_with_function=sum(bool(r['function_count']) for r in inventory),
                   statement_counts=dict(counts), published_list_records=len(published),
                   published_pombe_records=sum(r['Organism (ID)'] in {'4896','284812'} or r['Organism'].startswith('Schizosaccharomyces pombe') for r in published),
                   matched_cohort_in_public_list=sum(r['in_public_pilot'] for r in inventory),
                   api_status_counts=dict(Counter(str(r['status']) for r in comparisons)),
                   api_go_mismatches=[r['accession'] for r in comparisons if r['go_id_labels_match'] is False],
                   api_function_exact_mismatches=[r['accession'] for r in comparisons if r['function_paragraphs_match'] is False],
                   api_function_substantive_mismatches=[r['accession'] for r in comparisons if r['function_text_matches_ignoring_final_period'] is False],
                   caveat='Primary-accession join identifies this cohort; it is not an exhaustive census of all current API-served pombe accessions or a search through historical secondary accessions. Current sequences do not establish prediction-time inputs.')
    (root / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parent)
    summarize(parser.parse_args().root)
