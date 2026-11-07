"""Offline checks of saved identity, quotes and source-preservation receipts."""
import hashlib
import json
from pathlib import Path

import yaml
from Bio import SeqIO

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    baseline = json.loads((HERE.parent / 'baseline.json').read_text())
    protected = baseline['protected_files_sha256']
    for path, expected in protected.items():
        assert sha(ROOT / path) == expected, path
    transfer = json.loads((HERE / 'preflight-transfer-receipt.json').read_text())
    assert sha(Path(transfer['original_handoff'])) == transfer['original_handoff_sha256']
    for source, rec in transfer['copies'].items():
        assert sha(Path(rec['source_root']) / source) == rec['sha256']
        assert sha(ROOT / rec['destination']) == rec['sha256']
    uniprot = json.loads((HERE / 'identity/uniprot-source.json').read_text())
    results = json.loads((HERE / 'identity/results.json').read_text())
    for row in results:
        record = SeqIO.read(HERE / 'identity' / f"{row['accession']}.embl", 'embl')
        sequence = uniprot[row['uniprot']]['response']['sequence']['value']
        exact = [f for f in record.features if f.type == 'CDS'
                 and f.qualifiers.get('translation', [''])[0] == sequence]
        assert len(exact) == 1, row['uniprot']
        assert len(sequence) == row['length']
        assert sha(HERE / 'identity' / f"{row['accession']}.embl") == row['archive_sha256']
    ledger = yaml.safe_load((HERE / 'reference-ledger.yaml').read_text())
    for row in ledger:
        path = ROOT / row['source_path']
        assert sha(path) == row['source_sha256'], path
        normalized = ' '.join(path.read_text().split())
        for finding in row['findings']:
            assert ' '.join(finding['supporting_text'].split()) in normalized
    result = {'protected_sources': len(protected), 'preflight_copies': len(transfer['copies']),
              'exact_protein_bridges': len(results), 'checked_findings': len(ledger),
              'full_manually_read_reviews': sum(r['publication_type'] == 'REVIEW'
                                               and r['access_scope'].startswith('FULL')
                                               for r in ledger), 'status': 'PASS'}
    (HERE / 'preservation-results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
