"""Check Lit source preservation and explicitly account for authored proposals."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
AUDIT = Path(__file__).resolve().parent
GENE = ROOT / 'genes/BACCR/BC_1526/BC_1526-ai-review.yaml'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    baseline = yaml.safe_load((AUDIT / 'seed-baseline.yaml').read_text())
    document = yaml.safe_load(GENE.read_text())
    original = baseline['review'].get('existing_annotations', [])
    assert original == [], 'The independent seed was not empty'
    rows = document['existing_annotations']
    assert len(rows) == 3
    assert [row['term']['id'] for row in rows] == [
        'GO:0016867', 'GO:0042160', 'GO:0005886'
    ]
    assert all(row['review']['action'] == 'NEW' for row in rows)
    assert not any(row.get('retired') for row in rows)
    protected = dict(json.loads((AUDIT.parent / 'baseline.json').read_text())[
        'protected_files_sha256'
    ])
    protected.update(baseline['protected_publication_sha256'])
    for name, digest in baseline['files_sha256'].items():
        if not name.endswith('-ai-review.yaml'):
            protected[name] = digest
    protected.update(yaml.safe_load((AUDIT / 'new-source-baseline.yaml').read_text()))
    for name, digest in protected.items():
        assert sha(ROOT / name) == digest, name
    primary = (ROOT / 'publications/PMID_34253723.md').read_text()
    assert 'B. cereus strain ATCC 14579 (Uniprot ID: Q813T3_BACCR)' in primary
    result = {
        'result': 'PASS', 'ordered_original_payloads': 0, 'authored_NEW': 3,
        'deleted_rows': 0, 'retired_rows': 0,
        'identity': 'Primary explicitly names exact accession and strain',
        'protected_file_count': len(protected), 'protected_sha256': protected,
        'NEW_accounting': [row['term'] for row in rows],
        'scope': 'Source/payload and explicit proposal accounting; not an independent assay',
    }
    (AUDIT / 'preservation.yaml').write_text(yaml.safe_dump(result, sort_keys=False))
    print(f'PASS: empty seed preserved; 3 explicit NEW rows; {len(protected)} protected files')


if __name__ == '__main__':
    main()
