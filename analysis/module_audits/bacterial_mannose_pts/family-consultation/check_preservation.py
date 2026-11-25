"""Verify exact source/PAINT preservation, identity, architecture and quoted evidence."""
import csv
import hashlib
import json
from pathlib import Path

import yaml

from ai_gene_review.etl.panther_trees import compact_tree
from ai_gene_review.validation.local_source_text import quote_matches, resolve_local_source
from ai_gene_review.validation.supporting_text import build_supporting_text_validator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def quotations(value, inherited=None):
    if isinstance(value, dict):
        reference = value.get('reference_id', inherited)
        if value.get('supporting_text'):
            yield reference, value['supporting_text']
        for key, child in value.items():
            if key != 'supporting_text':
                yield from quotations(child, reference)
    elif isinstance(value, list):
        for child in value:
            yield from quotations(child, inherited)


def main():
    baseline = json.loads((HERE / 'baseline.json').read_text())
    root_baseline = json.loads((HERE.parent / 'baseline.json').read_text())
    inputs = {}
    for name, expected in {**root_baseline['protected_files_sha256'], **baseline['protected_sources_sha256']}.items():
        assert sha(ROOT / name) == expected, name
        inputs[name] = expected
    for name in baseline['new_reviews_previously_absent']:
        assert name in ['PTHR33799', 'PTHR32502']
        assert root_baseline['families'][f'interpro/panther/{name}/{name}-review.yaml'] == {'existed': False}
    labels = json.loads((HERE / 'official-labels.json').read_text())
    trees = json.loads((HERE / 'trees-compact.json').read_text())
    validator, _ = build_supporting_text_validator(ROOT / 'publications')
    paint_ledger, quote_ledger, member_ledger = [], [], []
    for family in ['PTHR33799', 'PTHR32502']:
        path = ROOT / f'interpro/panther/{family}/{family}-review.yaml'
        doc = yaml.safe_load(path.read_text())
        assert doc['review_status'] == 'COMPLETE'
        assert doc['family_name'] == labels[doc['family_id']]
        assert not doc.get('residue_sites'), 'No invented universal residue discriminator'
        tree_source = HERE / f'{family}-tree.json'
        assert compact_tree(json.loads(tree_source.read_text())) == trees[family]
        inputs[str(tree_source.relative_to(ROOT))] = sha(tree_source)
        raw = list(csv.DictReader((path.parent / f'{family}-paint.tsv').open(), delimiter='\t'))
        assert len(raw) == len(doc['node_assessments'])
        for before, after in zip(raw, doc['node_assessments'], strict=True):
            assert after['node_id'] == 'PANTHER:' + before['node']
            assert after['asserted_term']['id'] == before['go_id']
            assert after['evidence'] == before['evidence']
            assert after['negated'] == (before['negated'] == 'true')
            assert after['paint_snapshot'] == before['date']
            assert [v['id'] for v in after['seeds']] == before['seeds'].split('|')
            expected_taxon = before['taxon'].replace('taxon:', 'NCBITaxon:') if before['taxon'] != 'taxon:' else None
            assert after.get('node_taxon', {}).get('id') == expected_taxon
            assert before['node'] in trees[family]['under']
            paint_ledger.append({'family': family, 'source_assertion': before,
                                 'assessment': after['assessment'], 'reason': after['assessment_reason'],
                                 'current_descendant_count': len(trees[family]['under'][before['node']])})
        entries = {r['id']: r for r in csv.DictReader((path.parent / f'{family}-entries.csv').open())}
        for subfamily in doc['subfamilies']:
            assert subfamily['label'] == labels[subfamily['subfamily_id']]
            for member in subfamily['representative_members']:
                accession = member['id'].split(':')[1]
                sf = subfamily['subfamily_id'].removeprefix('PANTHER:')
                if accession in entries:
                    assert entries[accession]['subfamily'] == sf
                    source = path.parent / f'{family}-entries.csv'
                else:
                    source = HERE / f'{accession}-uniprot.json'
                    record = json.loads(source.read_text())
                    assert any(r['database'] == 'PANTHER' and r['id'] == sf for r in record['uniProtKBCrossReferences'])
                inputs[str(source.relative_to(ROOT))] = sha(source)
                member_ledger.append({'member': accession, 'subfamily': sf, 'source': str(source.relative_to(ROOT))})
        for ref, text in sorted(set(quotations(doc))):
            if ref.startswith('file:'):
                source = resolve_local_source(ref, ROOT)
                assert source and quote_matches(text, source), (ref, text)
            else:
                assert ref.startswith('PMID:')
                result = validator.validate(text, ref)
                assert result.is_valid and not result.skipped, (ref, result.message)
                source = ROOT / 'publications' / (ref.replace(':', '_') + '.md')
            inputs[str(source.relative_to(ROOT))] = sha(source)
            quote_ledger.append({'family': family, 'reference': ref, 'supporting_text': text,
                                 'source_sha256': sha(source)})
        for scope in doc['term_assessments']:
            if scope['scope'] == 'FAMILY_WIDE':
                assert family == 'PTHR33799' and scope['assessed_term']['id'] == 'GO:0009401'
    for accession, sf in [('Q9CEX8', 'PTHR33799:SF1'), ('Q9CEX7', 'PTHR32502:SF25'),
                           ('Q9CEX6', 'PTHR32502:SF27'), ('Q8DSC4', 'PTHR33799:SF1'),
                           ('Q8DSC3', 'PTHR32502:SF25'), ('Q8DSC2', 'PTHR32502:SF27')]:
        path = HERE / f'{accession}-uniprot.json'
        record = json.loads(path.read_text())
        assert any(x['database'] == 'PANTHER' and x['id'] == sf for x in record['uniProtKBCrossReferences'])
        inputs[str(path.relative_to(ROOT))] = sha(path)
    for accession, length, domain in [('P26379', 146, 'PF03610'), ('P26380', 163, 'PF03830')]:
        path = HERE / f'{accession}-uniprot.json'
        record = json.loads(path.read_text())
        assert record['sequence']['length'] == length
        assert any(x['database'] == 'Pfam' and x['id'] == domain for x in record['uniProtKBCrossReferences'])
        if accession == 'P26380':
            assert not any(x['database'] == 'PANTHER' for x in record['uniProtKBCrossReferences'])
        inputs[str(path.relative_to(ROOT))] = sha(path)
    assert len(paint_ledger) == 8
    result = {'status': 'PASS', 'family_count': 2, 'ordered_PAINT_assertions_preserved': 8,
              'family_raw_sources_unchanged': 6, 'protected_original_source_count': len(root_baseline['protected_files_sha256']),
              'member_groundings': member_ledger, 'quote_count': len(quote_ledger),
              'new_publication': 'publications/PMID_11976750.md',
              'source_scope': 'All pre-existing protected sources unchanged. PMID11976750 was absent and normally fetched; its cache is abstract-only. Full experimental negatives were not inferred from titles or absence.',
              'paint_assessments': paint_ledger, 'quotes': quote_ledger,
              'inputs_sha256': dict(sorted(inputs.items()))}
    (HERE / 'preservation.json').write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n')
    print(json.dumps({k: result[k] for k in ['status', 'family_count', 'ordered_PAINT_assertions_preserved', 'family_raw_sources_unchanged', 'protected_original_source_count', 'quote_count']}))


if __name__ == '__main__':
    main()
