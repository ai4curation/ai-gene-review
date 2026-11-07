"""Map configured reference positions across global protein alignments; no inferred assay outcomes."""
import argparse
from hashlib import sha256
from pathlib import Path
import re

import Bio
from Bio.Align import PairwiseAligner, substitution_matrices
import yaml


def read_record(path):
    text = path.read_text()
    sequence = ''.join(re.findall('[A-Z]+', text.split('SQ   SEQUENCE', 1)[1].split('\n', 1)[1].split('//')[0]))
    accession = re.search(r'^AC   ([^;]+)', text, re.M).group(1)
    declared = int(re.search(r'^ID.*?([0-9]+) AA\.', text, re.M).group(1))
    assert len(sequence) == declared, path
    return accession, sequence


def analyze(config, root):
    method = config['method']
    aligner = PairwiseAligner(mode=method['alignment'])
    aligner.substitution_matrix = substitution_matrices.load(method['substitution_matrix'])
    aligner.open_gap_score = method['open_gap_score']
    aligner.extend_gap_score = method['extend_gap_score']
    results = []
    inputs = {}
    for pair in config['pairs']:
        for key in ['reference', 'target']:
            path = root / pair[key]
            inputs[pair[key]] = sha256(path.read_bytes()).hexdigest()
        refacc, reference = read_record(root / pair['reference'])
        targetacc, target = read_record(root / pair['target'])
        alignment = aligner.align(reference, target)[0]
        mappings = {}
        for refblock, targetblock in zip(*alignment.aligned):
            for a, b in zip(range(*refblock), range(*targetblock)):
                mappings[a + 1] = b + 1
        sites = []
        for position in pair['reference_sites']:
            assert 0 < position <= len(reference)
            mapped = mappings.get(position)
            sites.append({'reference_position': position, 'reference_residue': reference[position - 1],
                          'target_position': mapped, 'target_residue': target[mapped - 1] if mapped else None,
                          'identical': bool(mapped and reference[position - 1] == target[mapped - 1])})
        identical = sum(reference[a - 1] == target[b - 1] for a, b in mappings.items())
        results.append({'name': pair['name'], 'reference_accession': refacc, 'target_accession': targetacc,
                        'reference_length': len(reference), 'target_length': len(target),
                        'aligned_nongap_pairs': len(mappings), 'identical_pairs': identical,
                        'identity_percent_nongap_pairs': round(100 * identical / len(mappings), 2),
                        'score': float(alignment.score), 'sites': sites, 'alignment': str(alignment)})
    return {'biopython_version': Bio.__version__, 'method': method, 'inputs_sha256': inputs, 'pairs': results}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('config', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    args = parser.parse_args()
    args.output.write_text(yaml.safe_dump(analyze(yaml.safe_load(args.config.read_text()), args.root), sort_keys=False))
