#!/usr/bin/env python3
"""Recompute sequence/taxon ROGIDs for supplied PSI-MI TAB interaction records.

No gene, protein length, expected match or biological conclusion is hardcoded.
The FASTA supplies database reference sequences and taxid= annotations. Matches
authenticate the references named in MITAB, not the experimentally cloned inserts.
"""
import argparse
import base64
import collections
import hashlib
import json
import re
from pathlib import Path


def read_fasta(path):
    sequences = {}
    accession = None
    for line in path.read_text().splitlines():
        if line.startswith('>'):
            fields = line[1:].split()
            accession = fields[0]
            match = re.search(r'\btaxid=(\d+)\b', line)
            if not match or accession in sequences:
                raise ValueError('FASTA needs unique accessions and taxid= annotations')
            sequences[accession] = {'taxon': int(match.group(1)), 'sequence': ''}
        elif line.strip():
            if accession is None or not re.fullmatch('[A-Za-z]+', line.strip()):
                raise ValueError('Invalid sequence or missing FASTA header')
            sequences[accession]['sequence'] += line.strip().upper()
    if not sequences or any(not s['sequence'] for s in sequences.values()):
        raise ValueError('Empty FASTA sequence set')
    return sequences


def reference_check(identifier, taxon_field, checksum_field, sequences):
    accession = identifier.split(':', 1)[-1]
    if accession not in sequences:
        return {'accession': accession, 'status': 'REFERENCE_NOT_SUPPLIED'}
    record = sequences[accession]
    taxon = record['taxon']
    sequence = record['sequence']
    digest = base64.b64encode(hashlib.sha1(sequence.encode()).digest()).decode().rstrip('=')
    rogid = digest + str(taxon)
    declared_taxa = [int(x) for x in re.findall(r'taxid:(\d+)', taxon_field)]
    match = 'rogid:' + rogid in checksum_field.split('|') and taxon in declared_taxa
    return {'accession': accession, 'taxon': taxon, 'length': len(sequence),
            'sequence_sha256': hashlib.sha256(sequence.encode()).hexdigest(),
            'calculated_rogid': rogid, 'literal_checksums': checksum_field,
            'status': 'MATCH' if match else 'MISMATCH'}


def analyze(mitab, fasta, target):
    sequences = read_fasta(fasta)
    records = []
    for line_index, line in enumerate(mitab.read_text().splitlines()):
        if not line or line.startswith('#'):
            continue
        fields = line.split('\t')
        if len(fields) < 38:
            raise ValueError(f'Line {line_index}: expected MITAB with features/checksums')
        if target and target not in [x.split(':', 1)[-1] for x in fields[:2]]:
            continue
        sides = [reference_check(fields[i], fields[9+i], fields[32+i], sequences)
                 for i in range(2)]
        records.append({'line_zero_based': line_index, 'id_a': fields[0], 'id_b': fields[1],
                        'method': fields[6], 'publication': fields[8],
                        'interaction_type': fields[11], 'identifiers': fields[13],
                        'expansion': fields[15], 'negative': fields[35],
                        'feature_a': fields[36], 'feature_b': fields[37],
                        'reference_checks': sides})
    counts = collections.Counter(s['status'] for r in records for s in r['reference_checks'])
    return {'target': target, 'record_count': len(records), 'reference_check_counts': dict(counts),
            'inputs': {str(p.name): hashlib.sha256(p.read_bytes()).hexdigest() for p in [mitab, fasta]},
            'limit': 'ROGID identifies the database reference sequence. It does not establish the experimental insert, native interaction, affinity, or directness of a co-complex association.',
            'records': records}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mitab', type=Path, required=True)
    parser.add_argument('--fasta', type=Path, required=True)
    parser.add_argument('--target', help='Optional unprefixed accession; omit to examine every row')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = analyze(args.mitab, args.fasta, args.target)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['target','record_count','reference_check_counts']}))
    if not result['records'] or result['reference_check_counts'].get('MISMATCH'):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
