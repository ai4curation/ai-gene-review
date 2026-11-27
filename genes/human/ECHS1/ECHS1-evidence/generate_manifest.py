#!/usr/bin/env python3
"""Generate source metadata from saved inputs and captured HTTP receipts (stdlib)."""
import argparse
import hashlib
import json
from pathlib import Path

def sha(data):
    return hashlib.sha256(data).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inputs', type=Path, required=True)
    parser.add_argument('--receipts', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    receipts = json.loads(args.receipts.read_text())
    files = {'intact': 'intact-P30084.tsv', 'mint': 'mint-P30084.tsv',
             'mitocop': '34800366-mmc2.xlsx'}
    result = {'format': 'MITAB 2.7 records and original supplementary XLSX',
              'producer': 'generate_manifest.py; hashes computed from supplied input bytes, source URLs from captured HTTP receipts',
              'sources': {}}
    for name, filename in files.items():
        receipt_key = 'mitocop_archive' if name == 'mitocop' else name
        record = receipts[receipt_key]
        receipt = record['receipt']
        if receipt['status'] != 200:
            raise ValueError('Acquisition was not successful: ' + name)
        body = (args.inputs / filename).read_bytes()
        expected = receipts['workbook_extraction'] if name == 'mitocop' else receipt
        if sha(body) != expected['sha256'] or len(body) != expected['bytes']:
            raise ValueError('Input bytes differ from captured source: ' + name)
        entry = {'url': receipt['url'], 'sha256': sha(body), 'bytes': len(body),
                 'input_filename': filename,
                 'receipt_sha256': record['original_receipt_sha256']}
        if name == 'mitocop':
            if expected['archive_sha256'] != receipt['sha256']:
                raise ValueError('Workbook and archive provenance disagree')
            entry.update(archive_sha256=receipt['sha256'],
                         archive_member=expected['archive_member'],
                         note='The URL supplies the supplemental archive; the exact authenticated workbook member is bundled separately.')
        result['sources'][name] = entry
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'sources': len(result['sources']), 'verified_input_bytes': sum(s['bytes'] for s in result['sources'].values())}))

if __name__ == '__main__':
    main()
