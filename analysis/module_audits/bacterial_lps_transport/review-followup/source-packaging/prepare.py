"""One-time additive source packaging; never rewrites any original input."""
import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
AUDIT = HERE.parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_new(path, content):
    assert not path.exists(), path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)


def main():
    inventory_path = AUDIT / 'review-followup/triage/source-inventory.json'
    inventory = json.loads(inventory_path.read_text())
    ledger = yaml.safe_load((AUDIT / 'literature-consultation/ledger.yaml').read_text())
    references = {r['access']['consulted_text']: r for r in ledger['references']}
    licenses = {
        '2015-review-full.txt': 'FEMS 2015; all rights reserved, as stated in the consulted publisher text.',
        '2024-review.txt': 'The Author(s), under exclusive licence to Microbiological Society of Korea 2024, as stated in the consulted PDF.',
        '2026-regulation.txt': 'CC BY-NC-ND 4.0, as stated under Rights and permissions in the consulted Nature article; this receipt does not claim an unrestricted adaptation licence.',
        'Nm-LptE.txt': 'Copyright 2011 American Society for Biochemistry and Molecular Biology; no explicit Creative Commons licence located in the consulted PMC rendering.',
    }
    replacements = {}
    for old, expected in inventory['tracked_cache_files'].items():
        source = ROOT / old
        assert sha(source) == expected, old
        item = {'original_path': old, 'original_sha256': expected,
                'original_bytes': source.stat().st_size,
                'original_preserved_locally': True}
        if source.name.endswith('.gz'):
            new = HERE / 'data' / source.name
            write_new(new, source.read_bytes())
            item.update(mode='BYTE_IDENTICAL', replacement_scope='Complete public data snapshot; byte equality verified.',
                        full_source_reconstructable=True)
            if source.name == 'AEQZ01.dat.gz':
                item.update(url='https://ftp.ebi.ac.uk/pub/databases/ena/wgs/public/aeq/AEQZ01.dat.gz',
                            rights='INSDC/ENA public-data policy permits redistribution and use without restrictions or licensing fees.',
                            rights_url='https://ena-browser-docs.readthedocs.io/en/latest/about/policies.html',
                            provenance=str((AUDIT / 'literature-consultation/identity/H44-genome-provenance.json').relative_to(ROOT)))
            else:
                family = source.name.split('.')[0]
                item.update(url=f'https://pantherdb.org/services/oai/pantherdb/treeinfo?family={family}',
                            rights='Public PANTHER reference-tree data; a specific standalone data licence was not verified. No licence inferred from the PANTHER publication licence. Official download-page lookup returned HTTP403 on 2026-11-07.',
                            provenance=str((AUDIT / 'family-consultation/tree-snapshot.json').relative_to(ROOT)))
        else:
            ref = references[old]
            text = source.read_text()
            quote = ref['checked_quote']
            assert ' '.join(quote.split()) in ' '.join(text.split())
            new = HERE / 'excerpts' / (ref['id'].replace(':', '_') + '.md')
            lines = [f"# {ref['id']} bounded source excerpt", '', ref['title'], '',
                     f"Source: {ref['access']['url']}", f"Original consulted-text SHA256: {expected}",
                     'Original access: successful full-text acquisition recorded in the frozen literature consultation on 2026-11-07; no new full-text acquisition is claimed.',
                     f"Rights observed: {licenses[source.name]}", '', 'Verbatim excerpt checked against the original consulted text:', '', f'> {quote}', '',
                     'Scope: ' + ref['reference_review']['review_notes'], '',
                     'This excerpt replaces only the scoped verification dependency. It neither reconstructs the complete article nor independently reproduces every historical full-text judgment. The original local cache and its acquisition/hash records are retained.', '']
            write_new(new, '\n'.join(lines).encode())
            item.update(mode='SCOPED_EXCERPT', reference=ref['id'], title=ref['title'],
                        url=ref['access']['url'], rights=licenses[source.name], checked_quote=quote,
                        replacement_scope='The ledger quotation and its bounded claim. Historical full-text consultation remains attested by acquisition records and source hash, not reproducible from this excerpt alone.',
                        full_source_reconstructable=False,
                        publication_cache=ref['access']['publication_cache'],
                        acquisition_provenance=str((AUDIT / 'literature-consultation/acquisition.json').relative_to(ROOT)))
            if source.name == 'Nm-LptE.txt':
                primary = AUDIT / 'neisseria-consultation/primary-evidence.md'
                primary_quotes = [line[2:] for line in primary.read_text().splitlines() if line.startswith('> ')]
                assert all(' '.join(q.split()) in ' '.join(text.split()) for q in primary_quotes)
                item['additional_scoped_evidence'] = {str(primary.relative_to(ROOT)): sha(primary)}
                item['additional_quotes_verified_against_original'] = len(primary_quotes)
        item.update(replacement_path=str(new.relative_to(ROOT)), replacement_sha256=sha(new))
        replacements[old] = item
    result = {'status': 'CAPTURED', 'checked_at': '2026-11-07', 'original_inventory_sha256': sha(inventory_path),
              'original_inputs_unchanged': True, 'replacements': replacements,
              'rights_limit': 'Article excerpts are bounded scientific support, not republication of full reviews. Public tree snapshots carry attribution; no unverified blanket licence is asserted.'}
    write_new(HERE / 'replacement-map.json', (json.dumps(result, indent=2) + '\n').encode())
    write_new(HERE / 'index-removal-paths.txt', ('\n'.join(sorted(replacements)) + '\n').encode())
    print(json.dumps({'mapped': len(replacements), 'byte_identical': 5, 'scoped_excerpts': 4}))


if __name__ == '__main__':
    main()
