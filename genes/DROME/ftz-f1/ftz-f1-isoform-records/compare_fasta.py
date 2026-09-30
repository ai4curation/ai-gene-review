#!/usr/bin/env python3
"""Compare two single-record FASTA files without alignment (Python 3 standard library)."""
import argparse
import hashlib
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('first', type=Path)
parser.add_argument('second', type=Path)
args = parser.parse_args()
def read(path):
    lines = path.read_text().splitlines()
    if not lines or not lines[0].startswith('>') or any(x.startswith('>') for x in lines[1:]):
        raise ValueError(f'Expected one FASTA record: {path}')
    sequence = ''.join(lines[1:]).replace(' ', '').upper()
    return {'file': str(path), 'header': lines[0][1:], 'length': len(sequence),
            'sequence_sha256': hashlib.sha256(sequence.encode()).hexdigest()}, sequence
first, a = read(args.first)
second, b = read(args.second)
print(json.dumps({'first': first, 'second': second, 'identical': a == b}, indent=2))
