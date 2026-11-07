"""Verify the bounded class-I source bridge and earlier immutable releases."""
import hashlib
import json
from pathlib import Path

from Bio import SeqIO

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    frozen = {
        'literature-consultation': '630f9b317c16e4505acf959e6fd9c4e585b2198dcdcd14b9a63fc925c3da2cd7',
        'gpo1-consultation': '98817183109b13aff66d02b2e11666cba9c35e0d1b9055ef9d6a6ec0c59a846d',
    }
    count = 0
    for directory, expected in frozen.items():
        manifest = HERE.parent / directory / 'handoff.json'
        assert sha(manifest) == expected
        for path, digest in json.loads(manifest.read_text())['files'].items():
            assert sha(ROOT / path) == digest, path
            count += 1
    uni = json.loads((HERE / 'P23608-uniprot.json').read_text())
    sequence = uni['sequence']['value']
    record = SeqIO.read(HERE / 'J05003.embl', 'embl')
    exact = [f for f in record.features if f.type == 'CDS'
             and f.qualifiers.get('translation', [''])[0] == sequence]
    assert len(exact) == 1 and len(sequence) == 589
    quotes = {
        '10612741': 'These data strongly suggested\nthat R. eutropha PHA synthase accepts',
        '35341893': 'without any synthase modification',
    }
    for pmid, quote in quotes.items():
        source = (ROOT / f'publications/PMID_{pmid}.md').read_text()
        assert ' '.join(quote.split()) in ' '.join(source.split())
    out = {'status': 'PASS', 'frozen_files_preserved': count,
           'frozen_handoffs_preserved': frozen, 'exact_sequence_length': 589,
           'exact_archive_protein': exact[0].qualifiers['protein_id'][0],
           'checked_primary_quotes': 2,
           'assay_construct_equality': 'NOT_ESTABLISHED',
           'source_scope': 'Two primary abstracts; no claimed full-text access',
           'new_gene_created': False}
    (HERE / 'results.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out))


if __name__ == '__main__':
    main()
