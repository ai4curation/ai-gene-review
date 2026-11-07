#!/usr/bin/env python3
"""Query official UniProt shell signatures; retain raw API output in the supplied cache directory."""
import argparse
import hashlib
import json
from pathlib import Path
import urllib.parse
import urllib.request


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cache-dir', type=Path, required=True)
    args = parser.parse_args()
    args.cache_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for proteome in ['UP000002438', 'UP000000625']:
        for signature in ['pfam-PF00936', 'pfam-PF03319', 'interpro-IPR000249', 'interpro-IPR004992']:
            query = f'proteome:{proteome} AND xref:{signature}'
            url = 'https://rest.uniprot.org/uniprotkb/search?' + urllib.parse.urlencode({
                'query': query, 'format': 'tsv', 'fields': 'accession,gene_names,protein_name,xref_pfam,xref_interpro', 'size': 500})
            with urllib.request.urlopen(url, timeout=60) as response:
                data = response.read()
                total = int(response.headers['X-Total-Results'])
            lines = data.decode().strip().splitlines()[1:]
            assert len(lines) == total, 'Pagination needed; refuse incomplete inventory'
            filename = f'{proteome}-{signature}.tsv'
            (args.cache_dir / filename).write_bytes(data)
            records.append({'proteome': proteome, 'signature': signature, 'url': url,
                            'total': total, 'accessions': [line.split('\t')[0] for line in lines],
                            'raw_file': filename, 'sha256': hashlib.sha256(data).hexdigest()})
    print(json.dumps(records, indent=2))


if __name__ == '__main__':
    main()
