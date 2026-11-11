"""Report translated primer/protein exact peptide matches, without assigning gene identity.

All input/output paths are arguments. Evaluate all six translations and report the
longest contiguous exact peptide match for each primer/protein pair. Cloning tails
need not be manually removed; unmatched tails are ignored by the local exact match.
Short matches alone are not evidence of gene identity. Protein positions are 1-based.
"""
import argparse
import csv
from difflib import SequenceMatcher
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from zipfile import ZipFile
from Bio import SeqIO
from Bio.Seq import Seq


def primers(path):
    ns = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    with ZipFile(path) as archive:
        strings = [''.join(si.itertext()) for si in ET.fromstring(archive.read('xl/sharedStrings.xml')).findall('m:si', ns)]
        for name in sorted(archive.namelist()):
            if not (name.startswith('xl/worksheets/sheet') and name.endswith('.xml')):
                continue
            for row in ET.fromstring(archive.read(name)).findall('.//m:row', ns):
                values = []
                for cell in row.findall('m:c', ns):
                    value = cell.find('m:v', ns)
                    if value is not None:
                        values.append(strings[int(value.text)] if cell.get('t') == 's' else value.text)
                if len(values) >= 2 and re.fullmatch('[ACGTacgt]{12,}', values[-1]):
                    yield values[-2], values[-1].upper()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--primers', type=Path, required=True)
    parser.add_argument('--protein-record', type=Path, action='append', required=True)
    parser.add_argument('--embl-record', type=Path, action='append', default=[])
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--minimum', type=int, default=5)
    args = parser.parse_args()
    proteins = []
    for path in args.protein_record:
        proteins.extend((record.id, str(record.seq)) for record in SeqIO.parse(path, 'swiss'))
    for path in args.embl_record:
        for record in SeqIO.parse(path, 'embl'):
            for feature in record.features:
                if feature.type == 'CDS' and feature.qualifiers.get('translation'):
                    proteins.append((feature.qualifiers['protein_id'][0], feature.qualifiers['translation'][0]))
    if not proteins:
        raise ValueError('No proteins found')
    if args.minimum < 1:
        raise ValueError('Minimum match length must be positive')
    rows = []
    for name, nucleotide in primers(args.primers):
        for accession, protein in proteins:
            best = None
            for strand, dna in [('+', Seq(nucleotide)), ('-', Seq(nucleotide).reverse_complement())]:
                for frame in range(3):
                    coding = dna[frame:frame + ((len(dna)-frame)//3)*3]
                    peptide = str(coding.translate())
                    match = SequenceMatcher(None, peptide, protein, autojunk=False).find_longest_match()
                    if best is None or match.size > best[0]:
                        best = (match.size, strand, frame, peptide[match.a:match.a+match.size], match.b+1, match.b+match.size)
            if best[0] >= args.minimum:
                rows.append([name, nucleotide, accession, *best])
    with args.output.open('w') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(['primer', 'sequence', 'protein', 'match_aa', 'strand', 'frame_offset', 'matched_peptide', 'protein_start', 'protein_end'])
        writer.writerows(rows)
    print(f'{len(rows)} matches across {len(proteins)} proteins, minimum {args.minimum} aa; {args.output}')


if __name__ == '__main__':
    main()
