"""Compare curated reviews to machine payloads and source hashes pinned at seeding."""
from collections import Counter
import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'analysis/module_audits/bacterial_beta_aryl_ether_dimer_cleavage'


def main():
    baseline = yaml.safe_load((DATA / 'seed-baseline.yaml').read_text())
    reports, raw_hashes = [], {}
    for item in baseline['reviews']:
        doc = yaml.safe_load((ROOT / item['path']).read_text())
        assert doc['id'] == item['id'] and doc['taxon'] == item['taxon']
        rows = doc.get('existing_annotations', [])
        assert [{k: v for k, v in a.items() if k != 'review'} for a in rows] == item['annotations']
        assert doc['status'] == 'COMPLETE'
        actions = Counter(a['review']['action'] for a in rows)
        assert not (set(actions) & {'NEW', 'PENDING'})
        for path, digest in item['raw_sha256'].items():
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, path
            raw_hashes[path] = digest
        reports.append({'path': item['path'], 'machine_rows': len(rows),
                        'machine_fields_and_order_preserved': True,
                        'identity_and_taxon_preserved': True, 'actions': dict(actions)})
    report = {'base_commit': baseline['base_commit'], 'reviews': len(reports),
              'machine_rows_preserved': sum(r['machine_rows'] for r in reports),
              'raw_files_unchanged': len(raw_hashes), 'new_annotations': 0,
              'gene_reviews': reports, 'raw_sha256': raw_hashes}
    assert (report['reviews'], report['machine_rows_preserved'], report['raw_files_unchanged']) == (16, 9, 32)
    (DATA / 'preservation-results.yaml').write_text(yaml.safe_dump(report, sort_keys=False))
    print('PASS: 16 identities, 9 machine annotation payloads, 32 raw files; zero NEW rows')


if __name__ == '__main__':
    main()
