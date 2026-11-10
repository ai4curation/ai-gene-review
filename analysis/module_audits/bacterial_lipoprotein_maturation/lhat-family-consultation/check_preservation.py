"""Preserve raw inputs and validate local evidence of the new family review."""
import hashlib
import re
from pathlib import Path

import yaml
from Bio import SwissProt

ROOT = Path(__file__).resolve().parents[4]
AUDIT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    baseline = yaml.safe_load((AUDIT / 'baseline.yaml').read_text())
    for name, expected in baseline['protected_sha256'].items():
        assert sha(ROOT / name) == expected, name
    released = yaml.safe_load((AUDIT.parent / 'lhat-reuse-consultation/handoff.yaml').read_text())
    for name, expected in released['files'].items():
        assert sha(ROOT / name) == expected, name
    review = yaml.safe_load((ROOT / 'interpro/panther/PTHR40042/PTHR40042-review.yaml').read_text())
    assert review['term_assessments'][0]['scope'] == 'UNRESOLVED'
    assert review['node_assessments'] == []
    assert not review.get('residue_sites')
    assert not (ROOT / 'interpro/panther/PTHR40042/PTHR40042-paint.tsv').exists()
    with (ROOT / 'genes/BACSU/ypjA/ypjA-uniprot.txt').open() as stream:
        sequence = SwissProt.read(stream).sequence
    assert sequence[170:173] == 'YFL'
    assert hashlib.sha256(sequence.encode()).hexdigest() == baseline['anchor_sequence_sha256']
    checked = 0

    def visit(value):
        nonlocal checked
        if isinstance(value, list):
            for item in value:
                visit(item)
        if isinstance(value, dict):
            ref = value.get('reference_id', '')
            quote = value.get('supporting_text')
            if ref.startswith('file:') and quote:
                path = ROOT / ref.removeprefix('file:')
                def normalized(text):
                    return re.sub(r'\s+', ' ', text).strip()
                assert normalized(quote) in normalized(path.read_text()), ref
                checked += 1
            for item in value.values():
                visit(item)

    visit(review)
    result = {
        'result': 'PASS', 'protected_inputs': len(baseline['protected_sha256']),
        'released_gene_files_unchanged': len(released['files']),
        'local_quotes_checked': checked, 'sequence_context': 'P54392 version1 YFL171-173',
        'original_PAINT_assertions': 0, 'new_ancestral_assertions': 0,
        'residue_rule': 'omitted; no independent positive control established',
    }
    (AUDIT / 'preservation.yaml').write_text(yaml.safe_dump(result, sort_keys=False))
    print(result)


if __name__ == '__main__':
    main()
