"""Resolve only this module's representatives through the normal UniProt lookup.

The generated member index is an ignored validation cache, never a cited source.
The committed UniProt records and upstream API remain the evidence.
"""
from pathlib import Path
import yaml
from ai_gene_review.etl.panther_families import (
    fetch_panther_from_uniprot, member_index_path, write_member_index, load_member_index,
)

ROOT = Path(__file__).resolve().parents[2]


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def main():
    doc = yaml.safe_load((ROOT / 'modules/bacterial_2_3_butanediol_acetoin_catabolism.yaml').read_text())
    claims = {}
    for obj in walk(doc):
        if not obj.get('family', {}).get('term'):
            continue
        family = obj['family']
        for member in family['representative_members']:
            claims[member['term']['id'].split(':', 1)[1]] = family['term']['id'].removeprefix('PANTHER:')
    observed = fetch_panther_from_uniprot(claims)
    assert set(observed) == set(claims), (observed, claims)
    for accession, expected in claims.items():
        assert (observed[accession] == expected if ':SF' in expected else observed[accession].split(':')[0] == expected), (accession, observed[accession], expected)
    path = member_index_path(ROOT)
    # Seed an absent cache or append newly observed missing members. Existing indices contain alternate
    # placements and unresolved-status metadata that this bounded task keeps.
    # The live comparison above still verifies all requested representatives.
    if not path.exists():
        write_member_index(observed, path)
    else:
        existing = load_member_index(path)
        missing = {a: family for a, family in observed.items() if a not in existing}
        # Preserve every existing row, alternate and gap marker byte for byte.
        # These appended assignments come from the normal live UniProt lookup.
        if missing:
            with path.open('a') as handle:
                for accession, family in sorted(missing.items()):
                    handle.write(f'{accession}\t{family}\n')
    print(yaml.safe_dump({'source': 'https://rest.uniprot.org/uniprotkb/accessions', 'method': 'normal fetch_panther_from_uniprot', 'declared': claims, 'observed': observed}, sort_keys=False))


if __name__ == '__main__':
    main()
