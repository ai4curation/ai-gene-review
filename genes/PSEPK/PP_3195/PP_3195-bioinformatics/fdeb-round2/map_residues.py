"""Map supplied residue positions by global sequence alignment (not a structure assay)."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import Bio
from Bio.Align import PairwiseAligner, substitution_matrices
import yaml


def read_sequence(path):
    text = path.read_text()
    if path.suffix == '.json':
        data = json.loads(text)
        data = data.get('response', data)
        return data['sequence']['value']
    body = text.split('\nSQ   SEQUENCE', 1)[1].split('\n', 1)[1].split('//')[0]
    return ''.join(re.findall('[A-Z]+', body))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--query', type=Path, required=True)
    parser.add_argument('--positions', type=int, nargs='+', required=True)
    parser.add_argument('--target', action='append', required=True, help='label=UniProt-flatfile-or-JSON')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    query = read_sequence(args.query)
    if not all(1 <= p <= len(query) for p in args.positions):
        parser.error('Position outside query sequence')
    aligner = PairwiseAligner(mode='global')
    aligner.substitution_matrix = substitution_matrices.load('BLOSUM62')
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    records = []
    for spec in args.target:
        label, path = spec.split('=', 1)
        path = Path(path)
        target = read_sequence(path)
        alignment = aligner.align(query, target)[0]
        mapping = {int(q): int(t) for q, t in zip(*alignment.indices) if q >= 0 and t >= 0}
        sites = []
        for pos in args.positions:
            mapped = mapping.get(pos - 1)
            sites.append(dict(query_position=pos, query_residue=query[pos - 1],
                              target_position=mapped + 1 if mapped is not None else None,
                              target_residue=target[mapped] if mapped is not None else None,
                              target_window=target[max(0, mapped - 7):mapped + 8] if mapped is not None else None))
        qtext = '/'.join(f'{s["query_residue"]}{s["query_position"]}' for s in sites)
        ttext = '/'.join(f'{s["target_residue"]}{s["target_position"]}' if s['target_position'] else 'gap' for s in sites)
        records.append(dict(label=label, target=str(path), target_length=len(target),
                            target_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                            identical_pairs=sum(query[q] == target[t] for q, t in mapping.items()),
                            aligned_pairs=len(mapping), sites=sites,
                            statement=f'{label}: query {qtext} maps to {ttext}.'))
    result = dict(query=str(args.query), query_sha256=hashlib.sha256(args.query.read_bytes()).hexdigest(),
                  biopython_version=Bio.__version__, method='Global BLOSUM62; gap-open -10; gap-extension -0.5; 1-based positions; first optimal alignment.', results=records)
    args.output.write_text(yaml.safe_dump(result, sort_keys=False))
    for record in records:
        print(record['statement'])


if __name__ == '__main__':
    main()
