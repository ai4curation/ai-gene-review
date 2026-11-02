"""Map numbered sites through a supplied aligned FASTA; report residues, not biology."""
import argparse
import csv
from pathlib import Path


def read_fasta(path):
    sequences = {}
    name = None
    for line in path.read_text().splitlines():
        if line.startswith('>'):
            name = line[1:].split()[0]
            sequences[name] = ''
        elif name:
            sequences[name] += line.strip().upper()
    if not sequences or len({len(s) for s in sequences.values()}) != 1:
        raise ValueError('Expected a nonempty aligned FASTA with equal sequence lengths')
    return sequences


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('alignment', type=Path)
    parser.add_argument('reference')
    parser.add_argument('sites', nargs='+', type=int)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    sequences = read_fasta(args.alignment)
    reference = sequences[args.reference]
    columns = {}
    pos = 0
    for col, residue in enumerate(reference):
        if residue != '-':
            pos += 1
            if pos in args.sites:
                columns[pos] = col
    if set(columns) != set(args.sites):
        raise ValueError('Reference sites outside the supplied sequence')
    with args.output.open('w') as handle:
        writer = csv.writer(handle, delimiter='\t')
        writer.writerow(['sequence', 'reference_position', 'reference_residue', 'alignment_column', 'target_position', 'target_residue'])
        for name, sequence in sequences.items():
            for site, col in columns.items():
                residue = sequence[col]
                target = len(sequence[:col + 1].replace('-', '')) if residue != '-' else ''
                writer.writerow([name, site, reference[col], col + 1, target, residue])


if __name__ == '__main__':
    main()
