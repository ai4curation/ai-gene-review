"""Verify the bounded source catalogue against immutable local source bytes."""
from pathlib import Path
import hashlib
import yaml
ROOT = Path(__file__).resolve().parents[4]
DATA = yaml.safe_load(Path(__file__).with_name('evidence.yaml').read_text())
for row in DATA['evidence']:
    source = ROOT / row['source_path']
    assert hashlib.sha256(source.read_bytes()).hexdigest() == row['sha256'], source
    assert ' '.join(row['supporting_text'].split()) in ' '.join(source.read_text().split()), row['reference_id']
for row in DATA['members']:
    source = ROOT / row['review'].replace('-ai-review.yaml', '-uniprot.txt')
    assert hashlib.sha256(source.read_bytes()).hexdigest() == row['raw_uniprot_sha256'], source
print(f"PASS: {len(DATA['evidence'])} verbatim quotations/source hashes and {len(DATA['members'])} frozen protein identities")
