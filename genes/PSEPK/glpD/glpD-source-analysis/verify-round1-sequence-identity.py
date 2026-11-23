"""Reproduce the frozen Q88NY0/P13035 bridge without fetching sources."""
import hashlib
import json
from pathlib import Path

from Bio import Align, SeqIO

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
expected = json.loads((HERE / 'round1-sequence-identity.json').read_text())
for relative, digest in expected['sources'].items():
    assert hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == digest
sequences = {
    species: str(SeqIO.read(ROOT / f'genes/{species}/glpD/glpD-uniprot.txt', 'swiss').seq)
    for species in ['ECOLI', 'PSEPK']
}
aligner = Align.PairwiseAligner(mode='global')
aligner.match_score = 2
aligner.mismatch_score = -1
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
alignment = aligner.align(sequences['ECOLI'], sequences['PSEPK'])[0]
pairs = list(zip(alignment[0], alignment[1]))
identical = sum(left == right and left != '-' for left, right in pairs)
aligned = sum(left != '-' and right != '-' for left, right in pairs)
assert identical == expected['identical_positions'] == 286
assert aligned == expected['aligned_residue_pairs'] == 500
assert len(pairs) == expected['alignment_columns'] == 515
print(f'PASS: {identical}/{aligned} aligned residue pairs; {identical}/{len(pairs)} total columns')
