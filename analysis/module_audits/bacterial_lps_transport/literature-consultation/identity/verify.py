"""Verify exact H44/76 CDS-to-UniProt bridges without treating strains as interchangeable."""
import gzip
import hashlib
import io
import json
from pathlib import Path

from Bio import SeqIO

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SOURCE = ROOT / '.cache/module-audit-logs/lps-20261107/literature-consultation/AEQZ01.dat.gz'


def main():
    provenance = json.loads((HERE / 'H44-genome-provenance.json').read_text())
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == provenance['sha256']
    cds = []
    text = gzip.decompress(SOURCE.read_bytes()).decode()
    for record in SeqIO.parse(io.StringIO(text), 'embl'):
        for feature in record.features:
            if feature.type == 'CDS' and 'translation' in feature.qualifiers:
                cds.append((record.id, feature.qualifiers))
    mapping = {'Q9K0A7': ('lptE', 'NMH_2330', 'EFV62668.1', 159),
               'Q7DDQ9': ('lptH (carrier; UniProt gene name lptA)', 'NMH_1931', 'EFV63335.1', 176),
               'F0MIT7': ('lptD', 'NMH_1010', 'EFV64164.1', 802)}
    result = []
    for accession, (role, locus, protein, length) in mapping.items():
        target = json.loads((HERE / f'{accession}.json').read_text())
        sequence = target['sequence']['value']
        hits = [(contig, q) for contig, q in cds if q['translation'][0] == sequence]
        assert len(hits) == 1
        contig, qualifiers = hits[0]
        assert qualifiers['locus_tag'] == [locus]
        assert qualifiers['protein_id'] == [protein]
        assert len(sequence) == length
        result.append({'uniprot': accession, 'gene_role': role,
                       'target_taxon': target['organism']['taxonId'],
                       'target_species': target['organism']['scientificName'],
                       'H44_contig': contig, 'H44_locus': locus,
                       'H44_protein': protein, 'identity': f'{length}/{length}',
                       'sequence_sha256': hashlib.sha256(sequence.encode()).hexdigest()})
    output = {'status': 'PASS', 'bridges': result,
              'scope': 'Natural reference CDS translation identity, not complete expression-construct identity or transfer of native strain phenotype.',
              'source': provenance}
    (HERE / 'results.json').write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
