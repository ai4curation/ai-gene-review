"""Compare two equal-length protein FASTAs without assuming any expected differences.

Unequal lengths are reported as inconclusive: this is a positional comparison,
not an alignment algorithm. Python 3.12 standard library only.
"""
import argparse
import hashlib
import json
from pathlib import Path


def read_fasta(path):
    lines = path.read_text().splitlines()
    if not lines or not lines[0].startswith('>') or sum(x.startswith('>') for x in lines) != 1:
        raise ValueError(f'Expected one FASTA record: {path}')
    sequence = ''.join(x.strip() for x in lines[1:]).upper()
    if not sequence or set(sequence) - set('ABCDEFGHIJKLMNOPQRSTUVWXYZ*'):
        raise ValueError(f'Invalid protein sequence: {path}')
    return dict(header=lines[0][1:], sequence=sequence,
                file_sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def compare(first, second):
    a, b = read_fasta(first), read_fasta(second)
    result = dict(inputs=[dict(file=p.name, header=s['header'], length=len(s['sequence']),
                               file_sha256=s['file_sha256'])
                          for p, s in [(first, a), (second, b)]])
    if len(a['sequence']) != len(b['sequence']):
        return dict(result, status='INCONCLUSIVE_UNEQUAL_LENGTHS', differences=None)
    differences = [dict(position=i, first=x, second=y)
                   for i, (x, y) in enumerate(zip(a['sequence'], b['sequence']), 1) if x != y]
    return dict(result, status='COMPARED', differences=differences)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('first', type=Path)
    parser.add_argument('second', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    args.output.write_text(json.dumps(compare(args.first, args.second), indent=2) + '\n')
