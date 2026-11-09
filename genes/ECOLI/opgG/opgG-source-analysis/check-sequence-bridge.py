"""Verify frozen K-12 sequences against cached authoritative BL21 precursors.

Run from the repository root. Input FASTAs are acquired, unedited NCBI efetch
records in the ignored ecoli-review audit cache; URLs and hashes are in
sequence-bridge.md. No network calls or source changes are made here.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re

parser = argparse.ArgumentParser()
parser.add_argument('--cache-dir', default='.cache/module-audit-logs/opg-20261106/ecoli-review')
args = parser.parse_args()
expected = {'opgG': ('CAQ31569.1', 'cbbcc022f216c39bf19230f0eae4ed9dd084819305af26faf660e258d0c2c193'),
            'opgD': ('CAQ31910.2', 'ab2f6eb74e47d18fc94a2c0b4b2b5d137f964678f0f206e5e8057690a3077c23')}
results = {}
for gene, (accession, digest) in expected.items():
    fasta = Path(args.cache_dir) / f'{accession}.fasta'
    assert hashlib.sha256(fasta.read_bytes()).hexdigest() == digest
    assay = ''.join(fasta.read_text().splitlines()[1:])
    record = Path(f'genes/ECOLI/{gene}/{gene}-uniprot.txt').read_text()
    target = ''.join(re.findall('[A-Z]+', record.split('SQ   SEQUENCE')[1].split('\n', 1)[1].split('//')[0]))
    assert target == assay, gene
    results[gene] = {'assay_precursor': accession, 'length': len(target), 'identical': True}
print(json.dumps(results, indent=2))
