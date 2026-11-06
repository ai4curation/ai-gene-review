"""Capture official UniParc cross-references without changing gene source records.

Run from the repository root with a new output directory as the sole argument.
Existing snapshots are immutable: the command refuses to reuse an output directory.
"""
from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from pathlib import Path
import sys

import requests
import yaml

RECORDS = (
    ('ligN', 'C0SUK1', 'UPI00019B2644'),
    ('ligP', 'E1CJ68', 'UPI0001DD3D33'),
    ('ligQ', 'G2IKM4', 'UPI0002276658'),
)


def main() -> None:
    output = Path(sys.argv[1])
    output.mkdir(parents=True, exist_ok=False)
    provenance = {'retrieved_at': datetime.now(timezone.utc).isoformat(), 'records': []}
    for gene, accession, upi in RECORDS:
        requests_made = []

        def capture(url: str, filename: str) -> tuple[dict, requests.Response]:
            response = requests.get(url, timeout=90)
            response.raise_for_status()
            (output / filename).write_bytes(response.content)
            requests_made.append({
                'url': url, 'retrieved_at': datetime.now(timezone.utc).isoformat(),
                'response_file': filename, 'http_status': response.status_code,
                'sha256': hashlib.sha256(response.content).hexdigest(),
                'response_headers': dict(response.headers),
            })
            return response.json(), response

        entry, _ = capture(f'https://rest.uniprot.org/uniparc/{upi}.json', f'{upi}.json')
        refs = []
        page = 1
        url = f'https://rest.uniprot.org/uniparc/{upi}/databases?size=500'
        total = None
        while url:
            data, response = capture(url, f'{upi}-databases-{page}.json')
            refs.extend(data['results'])
            if page == 1:
                total = int(response.headers['x-total-results'])
            url = response.links.get('next', {}).get('url')
            page += 1
        assert total == len(refs), (upi, total, len(refs))
        current, _ = capture(f'https://rest.uniprot.org/uniprotkb/{accession}.json', f'{accession}-current.json')
        raw_path = Path(f'genes/SPHSK/{gene}/{gene}-uniprot.txt')
        raw_bytes = raw_path.read_bytes()
        raw = raw_bytes.decode()
        sequence = ''.join(raw.split('\nSQ   ', 1)[1].split('\n', 1)[1].split('//', 1)[0].split())
        uniprot_refs = [r for r in refs if r['database'].startswith('UniProtKB/')]
        live = [r for r in uniprot_refs if r['active']]
        # If a future run finds candidates, capture each current record rather than
        # assuming that the UniParc active flag establishes its identity/taxon.
        for candidate in live:
            capture(f"https://rest.uniprot.org/uniprotkb/{candidate['id']}.json", f"{candidate['id']}-candidate.json")
        record = {
            'gene': gene, 'accession': accession, 'uniparc_id': upi,
            'requests': requests_made,
            'cross_reference_count': len(refs), 'all_cross_reference_pages_retrieved': True,
            'uniprotkb_cross_references': uniprot_refs,
            'active_uniprotkb_cross_references': live,
            'cross_reference_taxa': sorted({r['organism']['taxonId'] for r in refs if 'organism' in r}),
            'archival_sequence_file': str(raw_path),
            'archival_file_sha256': hashlib.sha256(raw_bytes).hexdigest(),
            'sequence_length': len(sequence),
            'sequence_sha256': hashlib.sha256(sequence.encode()).hexdigest(),
            'archive_equals_uniparc_sequence': sequence == entry['sequence']['value'],
            'current_record_status': current,
        }
        assert record['archive_equals_uniparc_sequence'], gene
        provenance['records'].append(record)
    (output / 'provenance.yaml').write_text(yaml.safe_dump(provenance, sort_keys=False))


if __name__ == '__main__':
    main()
