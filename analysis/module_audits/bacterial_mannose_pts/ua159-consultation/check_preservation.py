"""Check seeded payloads, source immutability, released evidence and UA159 review coverage."""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

A = Path(__file__).resolve().parent
ROOT = A.parents[3]
C = ROOT / '.cache/module-audit-logs/mannose-pts-20261107/ua159-consultation'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(rows):
    return [{k: v for k, v in row.items() if k != 'review'} for row in rows]


def main():
    baseline = json.loads((A.parent / 'ua159-seed-baseline.json').read_text())
    original = json.loads((A.parent / 'baseline.json').read_text())
    protected = original['protected_files_sha256'] | baseline['protected_files_sha256']
    for path, digest in protected.items():
        assert sha(ROOT / path) == digest, path
    release = A.parent / 'literature-consultation/handoff.json'
    literature = json.loads(release.read_text())
    for path, digest in literature['files'].items():
        assert sha(ROOT / path) == digest, path
    full = ROOT / '.cache/module-audit-logs/mannose-20261107/literature-consultation/2014-mutans.txt'
    assert 'almost no detectable PTS-dependent uptake of GlcNAc' in re.sub(r'\s+', ' ', full.read_text())
    actions = Counter()
    genes = []
    logs = {}
    source_closure = dict(protected)
    source_closure[str(release.relative_to(ROOT))] = sha(release)
    for path, seed in baseline['genes'].items():
        d = yaml.safe_load((ROOT / path).read_text())
        before = seed['document']['existing_annotations']
        after = d['existing_annotations']
        assert payload(before) == payload(after), path
        assert d['status'] == 'COMPLETE'
        assert d['id'] == seed['document']['id']
        for row in after:
            assert row['review']['action'] in {'ACCEPT', 'MODIFY'}
            assert row['review']['supported_by']
            actions[row['review']['action']] += 1
            if row['term']['id'] in {'GO:0008982', 'GO:0051119'}:
                assert {t['id'] for t in row['review']['proposed_replacement_terms']} == {'GO:0022870', 'GO:0022855', 'GO:0022880'}
        core = d['core_functions'][0]
        assert core['contributes_to_molecular_function']['id'] == 'GO:0022870'
        assert 'molecular_function' not in core
        gene = d['gene_symbol']
        report = (C / f'{gene}-validate.log').read_text()
        assert 'All validations passed' in report
        falcon = (C / f'{gene}-falcon.log').read_text()
        assert '403 Failed to authenticate' in falcon
        assert not list((ROOT / path).parent.glob('*deep-research-falcon.md'))
        losses = (C / f'{gene}-paint-losses.log').read_text()
        assert 'not a leaf of this tree; losses not checked' in losses
        rendered = (ROOT / path).with_suffix('.html')
        text = BeautifulSoup(rendered.read_text(), 'html.parser').get_text(' ', strip=True)
        assert d['id'] in text and 'TODO:' not in text and 'PENDING' not in text
        genes.append(dict(gene=gene, accession=d['id'], rows=len(after),
                          actions=dict(Counter(r['review']['action'] for r in after)),
                          new=0, retired=0, paint_lineage='NOT_CHECKED_TARGET_ABSENT',
                          core='contributes_to GO:0022870', render='PASS',
                          validation='PASS_WITH_COVERAGE_ADVISORIES', provider='FALCON_403'))
    for path in C.glob('*.log'):
        logs[str(path.relative_to(ROOT))] = sha(path)
    source_closure.update(logs)
    ontology = json.loads((A / 'transporter-ancestry.json').read_text())
    ancestors = ontology['response']['results'][0]['ancestors']
    assert 'GO:0008982' in ancestors and 'GO:0051119' in ancestors
    receipt = dict(result='PASS', genes=genes, ordered_payload_count=sum(g['rows'] for g in genes),
                   action_counts=dict(actions), new_rows=0, retired_rows=0,
                   source_files_unchanged=len(protected), frozen_literature_files_unchanged=len(literature['files']),
                   source_sha256=source_closure,
                   limitations=['PAINT lineages cannot be checked because exact targets are absent from cached trees.',
                                'One core-coverage advisory for ManL; two each for ManM and ManN. No rows added to silence warnings.',
                                'Core activity and location combine native-system assays with target-domain and comparative mechanism inference; not independent target-subunit reconstitution.'])
    (A / 'preservation.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'source_sha256'}, indent=2))


if __name__ == '__main__':
    main()
