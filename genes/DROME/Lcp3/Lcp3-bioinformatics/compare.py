"""Compare complete UniProt flat-file sequences; Python standard library only."""
import argparse
import hashlib
import json
from pathlib import Path


def read_record(path):
    text = path.read_text()
    sequence = ''.join(text.split('\nSQ   ', 1)[1].split('\n', 1)[1].split('//', 1)[0].split())
    if not sequence.isalpha() or not sequence.isupper():
        raise ValueError(f'Invalid protein sequence in {path}')
    return {'file': str(path), 'accession': next(l.split()[1].rstrip(';') for l in text.splitlines() if l.startswith('AC   ')), 'length': len(sequence), 'sha256': hashlib.sha256(sequence.encode()).hexdigest(), 'sequence': sequence}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('target', type=Path)
    parser.add_argument('reference', type=Path)
    args = parser.parse_args()
    target, reference = map(read_record, [args.target, args.reference])
    print(json.dumps({'target': target, 'reference': reference, 'sequences_identical': target['sequence'] == reference['sequence'], 'matching_positions_without_alignment': sum(a == b for a,b in zip(target['sequence'], reference['sequence']))}, indent=2))
