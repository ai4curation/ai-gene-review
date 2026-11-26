"""Verify module integration preserves original source bytes and evidence identities."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
MODULE = ROOT / 'modules/bacterial_lol_lipoprotein_trafficking.yaml'


def main():
    before = json.loads((HERE / 'baseline.json').read_text())
    current = yaml.safe_load(MODULE.read_text())
    sources_before = {e['source_id'] for e in before['module']['evidence']}
    sources_now = {e['source_id'] for e in current['evidence']}
    assert sources_before <= sources_now
    for name, expected in before['protected_source_sha256'].items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected, name
    refs = current['references']
    reviews = [r['id'] for r in refs if r.get('publication_type') == 'REVIEW']
    assert set(reviews) == {'PMID:30900542', 'PMID:42023066', 'PMID:40536045'}
    assert all(r['id'] not in {'PMID:25583975', 'PMID:39421643'} for r in refs)
    assert all('reference_review' in r for r in refs)
    required = current['module']['parts']
    assert len(required) == 2 and all(not p.get('optional') for p in required)
    assert {p['node']['id'] for p in required} == {'lipoprotein_extraction', 'lipoprotein_delivery'}
    result = {'status': 'PASS', 'original_evidence_sources_retained': len(sources_before),
              'protected_original_sources': len(before['protected_source_sha256']),
              'manual_references': len(refs), 'review_articles': reviews,
              'new_family_or_gene_edits_by_this_consultation': False,
              'scope': 'Module/source integrity check, not an independent biological capacity oracle'}
    (HERE / 'preservation.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
