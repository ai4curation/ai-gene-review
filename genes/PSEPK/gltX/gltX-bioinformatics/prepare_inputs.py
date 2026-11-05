"""Prepare a raw-record target and normally downloaded comparator FASTAs."""
import argparse
import hashlib
import json
from pathlib import Path

import requests


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target-record', type=Path, required=True)
    parser.add_argument('--target-id', required=True)
    parser.add_argument('--references', nargs='+', required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    provenance = []
    parts = []
    for accession in args.references:
        url = f'https://rest.uniprot.org/uniprotkb/{accession}.fasta'
        response = requests.get(url, timeout=40)
        response.raise_for_status()
        target = args.output_dir / f'{accession}.fasta'
        target.write_text(response.text)
        provenance.append({'url': url, 'file': target.name, 'sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
        parts.append(f'>{accession}\n' + ''.join(response.text.splitlines()[1:]) + '\n')
    raw = args.target_record.read_text()
    if not any(args.target_id in line for line in raw.splitlines() if line.startswith('AC   ')):
        raise ValueError('Target id does not occur in raw accession lines')
    sequence = ''.join(''.join(line.split()) for line in raw.split('SQ   SEQUENCE')[1].splitlines()[1:] if not line.startswith('//'))
    if not sequence or not sequence.isalpha():
        raise ValueError('Invalid raw sequence')
    target = args.output_dir / f'{args.target_id}.fasta'
    target.write_text(f'>{args.target_id}\n{sequence}\n')
    provenance.append({'source': str(args.target_record), 'file': target.name, 'sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
    parts.append(target.read_text())
    (args.output_dir / 'input.fasta').write_text(''.join(parts))
    (args.output_dir / 'provenance.json').write_text(json.dumps(provenance, indent=2) + '\n')


if __name__ == '__main__':
    main()
