"""Reproduce the NasN accession reconciliation from immutable downloaded records.

Run with the repository environment:
  uv run python modules/bacterial_assimilatory_nitrate_reduction-source-analysis/check_nasN_identity.py

Use --fetch to acquire missing versioned ENA inputs into the ignored cache.
The protein comparator is the committed, unedited UniProt flat-file record.
No curated files are changed; the computed proof is printed to stdout.
"""
from pathlib import Path
import argparse
import difflib
import hashlib
import json
import urllib.request

from Bio import SeqIO

CACHE = Path('.cache/module-audit-logs/nitrate-foundation')
SOURCE_URLS = {
    'reference': 'https://www.ebi.ac.uk/ena/browser/api/embl/CP000480.1',
    'corrected': 'https://www.ebi.ac.uk/ena/browser/api/embl/DQ866862.1',
}
PROTEIN_RECORD = Path('genes/MYCS2/nasN/nasN-uniprot.txt')


def sha(sequence):
    return hashlib.sha256(str(sequence).encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fetch', action='store_true')
    parser.add_argument('--cache-dir', type=Path, default=CACHE)
    args = parser.parse_args()
    for key, filename in [('reference', 'CP000480.embl'), ('corrected', 'DQ866862.embl')]:
        destination = args.cache_dir / filename
        if not destination.exists():
            if not args.fetch:
                parser.error(f'Missing {destination}; rerun with --fetch.')
            destination.parent.mkdir(parents=True, exist_ok=True)
            with urllib.request.urlopen(SOURCE_URLS[key], timeout=120) as response:
                destination.write_bytes(response.read())
    reference = SeqIO.read(args.cache_dir / 'CP000480.embl', 'embl')
    corrected = SeqIO.read(args.cache_dir / 'DQ866862.embl', 'embl')
    assert reference.id == 'CP000480.1'
    assert corrected.id == 'DQ866862.1'
    features = [f for f in reference.features if f.type == 'gene'
                and f.qualifiers.get('locus_tag') == ['MSMEG_4206']]
    assert len(features) == 1
    feature = features[0]
    old = str(feature.extract(reference.seq))
    new = str(corrected.seq)
    protein = str(corrected.seq.translate(to_stop=True))
    uniprot = SeqIO.read(PROTEIN_RECORD, 'swiss')
    edits = [dict(tag=tag, old_start=old_start, old_end=old_end,
                  corrected_start=new_start, corrected_end=new_end,
                  old_bases=old[old_start:old_end], corrected_bases=new[new_start:new_end])
             for tag, old_start, old_end, new_start, new_end
             in difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes()
             if tag != 'equal']
    assert edits == [dict(tag='insert', old_start=1849, old_end=1849,
                          corrected_start=1849, corrected_end=1850,
                          old_bases='', corrected_bases='G')]
    assert protein == str(uniprot.seq)
    result = dict(source_urls=SOURCE_URLS, reference_accession=reference.id,
                  reference_locus='MSMEG_4206', reference_pseudo='pseudo' in feature.qualifiers,
                  reference_length=len(old), corrected_accession=corrected.id,
                  corrected_locus='MSMEG4211', corrected_length=len(new),
                  edits_reference_to_corrected=edits, translated_length=len(protein),
                  uniprot_accession=uniprot.id,
                  protein_record=str(PROTEIN_RECORD),
                  protein_record_sha256=hashlib.sha256(PROTEIN_RECORD.read_bytes()).hexdigest(),
                  translation_exactly_matches_uniprot=True,
                  nucleotide_reference_sha256=sha(old), nucleotide_corrected_sha256=sha(new),
                  protein_sha256=sha(protein))
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
