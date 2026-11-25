"""Compare the archived assayed SS1 TlpD sequence to the frozen 26695 seed.
Run from any working directory with Python 3; no network or third-party modules.
"""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
raw = HERE.parent / 'tlpD-uniprot.txt'
record = HERE / 'SS1-A0A1U9IUC7-record.json'
archive = HERE / 'UPI000980CA3C.json'
ss1_record = json.loads(record.read_text())
assert ss1_record['extraAttributes']['uniParcId'] == 'UPI000980CA3C'
ss1 = json.loads(archive.read_text())['sequence']['value']
target = ''.join(re.findall('[A-Z]+', raw.read_text().split('\nSQ   ', 1)[1].split('\n', 1)[1].split('//')[0]))
assert len(ss1) == len(target) == 433
changes = [{'position': i, 'SS1': a, '26695': b} for i, (a, b) in enumerate(zip(ss1, target), 1) if a != b]
result = {
    'method': 'Unaligned positional comparison of two colinear 433-residue TlpD sequences; all differences reported; no sequence identity assumption.',
    'target': 'UniProtKB:O25321; H. pylori 26695; frozen seeded flat file',
    'assayed_sequence': 'UniProtKB:A0A1U9IUC7; H. pylori SS1; PMID:31465435',
    'archive': 'UniParc:UPI000980CA3C; linked by inactive UniProt record',
    'length_each': 433,
    'identical_positions': 433 - len(changes),
    'identity_percent': round((433-len(changes))/433*100, 3),
    'differences': changes,
    'CZB_H315_C340_H368_H372': {str(i): {'SS1': ss1[i-1], '26695': target[i-1]} for i in (315,340,368,372)},
    'input_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (raw, record, archive)},
    'interpretation': 'Near-identical orthologs support explicit cross-strain inference, not a direct 26695 biochemical assay. The HOCl-reactive C340 and the three zinc-coordinating histidines are conserved.'
}
(HERE/'sequence-comparison.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
