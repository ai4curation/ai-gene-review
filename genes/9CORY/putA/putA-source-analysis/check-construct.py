"""Verify the CfPutA deposit bridge from official cached RCSB responses.

Run from repository root with uv run python <this-file>. Downloads are preserved
in the ignored nonalpha-review cache, not embedded in the curated source folder.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
from Bio.PDB.MMCIF2Dict import MMCIF2Dict

parser = argparse.ArgumentParser()
parser.add_argument('--sources', type=Path, default=Path('.cache/module-audit-logs/puta-20261106/nonalpha-review'))
args = parser.parse_args()
proof = json.loads(Path(__file__).with_name('construct-bridge.json').read_text())
files = ['5ux5-entity.response', '5ux5-sifts.response', '5ux5-cif.response']
for filename, source in zip(files, proof['sources']):
    path = args.sources / filename
    assert hashlib.sha256(path.read_bytes()).hexdigest() == source['sha256'], filename
entity = json.loads((args.sources / files[0]).read_text())
cif = MMCIF2Dict(str(args.sources / files[2]))
sequence = entity['entity_poly']['pdbx_seq_one_letter_code_can']
raw = Path('genes/9CORY/putA/putA-uniprot.txt').read_text()
target = ''.join(re.findall('[A-Z]+', raw.split('SQ   SEQUENCE')[1].split('\n', 1)[1].split('//')[0]))
assert sequence == target
assert len(sequence) == 1076 and sequence.startswith('GHM')
assert hashlib.sha256(sequence.encode()).hexdigest() == proof['sequence_sha256']
assert cif['_pdbx_poly_seq_scheme.pdb_seq_num'][:3] == ['-1', '0', '1']
assert cif['_pdbx_poly_seq_scheme.pdb_seq_num'][1075] == '1074'
assert entity['rcsb_polymer_entity_container_identifiers']['uniprot_ids'] == ['A0A1X8XLF1']
print('PASS: complete 1076-aa match; GH precedes paper-numbered residues 1–1074.')
