"""Reproduce the source and identity scope checks used by the four AhpCF reviews."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
SOURCES = {
    'Salmonella primary full text (PMID10828978)': 'publications/url_https___citeseerx.ist.psu.edu_document_doi_9595b48acf5bd878f3f207ac05949130853a61be&repid_rep1&type_pdf.md',
    'Poole mechanistic review full text': 'publications/url_https___scb.wfu.edu_Poole-files_ABB-Poole-05.pdf.md',
    'Bacillus native operon primary abstract': 'publications/PMID_8932314.md',
    'Bacillus compensatory-defense primary abstract': 'publications/PMID_8932315.md',
    'Legacy partial-ORF assignment abstract': 'publications/PMID_8125345.md',
    'AhpF PAINT node scope': 'interpro/panther/PTHR48105/PTHR48105-paint.tsv',
    'AhpC PAINT node scope': 'interpro/panther/PTHR10681/PTHR10681-paint.tsv',
}
PASSAGES = {
    'Salmonella primary full text (PMID10828978)': [
        'Wild-type and C129,132S AhpF as well as AhpC from S.\ntyphimurium were expressed and purified',
        'TrR activity was not detected in either protein\nusing standard DTNB- and insulin-linked assays and E. coli\nTr.',
        'after 20 h about one-third of the Tr was reduced.',
        'Intact AhpF transferred electrons to Tr\nat half the rate of F[208-521]',
    ],
    'Bacillus native operon primary abstract': [
        'The ahp operon,\nencoding the two subunits AhpC and AhpF, was cloned and localized between the\ngntRKPZ operon and the bglA locus.',
        'more sensitive to cumene hydroperoxide (CHP) during\nexponential growth.',
    ],
    'AhpF PAINT node scope': ['PTN005133404\tGO:0004791', 'PTN000530716\tGO:0005829'],
    'AhpC PAINT node scope': ['PTN000073874\tGO:0008379'],
}


def main():
    result = {}
    for name, relpath in SOURCES.items():
        path = ROOT / relpath
        text = path.read_text()
        passages = PASSAGES.get(name, [])
        assert all(passage in text for passage in passages), name
        result[name] = {
            'path': relpath,
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'verified_literal_passages': passages,
        }
    for species in ['SALTY', 'BACSU']:
        for gene in ['ahpC', 'ahpF']:
            path = ROOT / f'genes/{species}/{gene}/{gene}-uniprot.txt'
            text = path.read_text()
            identity = text.splitlines()[:2]
            if gene == 'ahpF':
                assert 'TIGR03140; AhpF' in text
                assert 'IPR044141; AhpF_NTD_C' in text
                assert 'IPR044142; AhpF_NTD_N' in text
            result[f'{species}/{gene} exact target record'] = {
                'path': str(path.relative_to(ROOT)),
                'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                'identity_lines': identity,
                'native_kinetics': 'direct Salmonella biochemical evidence' if species == 'SALTY' else 'native operon/physiology plus orthology; no purified Bacillus-pair kinetics asserted',
            }
    (HERE / 'source-scope-proof.json').write_text(json.dumps(result, indent=2) + '\n')
    print(f'PASS: {len(result)} source/identity records; all inspected literal passages retained')


if __name__ == '__main__':
    main()
