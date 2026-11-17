"""Check frozen curation inputs and reviewed-panel OAS/sulfide capacity.

Production compile_node/is_satisfied supplies topology. The external oracle requires
an exact reviewed core reaction, an independently curated route role, module member
selection, actual source family membership, and a common strain taxon. This is a
panel capability test, not genome completeness, expression, flux, or native growth.
Run --assemble-baseline once from pristine captures; normal runs never reseed.
"""
from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re

import yaml

from ai_gene_review.module_logic import compile_node, is_satisfied, iter_atoms

ROOT = Path(__file__).resolve().parents[2]
SLUG = 'bacterial_cysteine_biosynthesis_via_o_acetylserine'
AUDIT = ROOT / 'analysis/module_audits' / SLUG
LOG = ROOT / '.cache/module-audit-logs/cysteine-20261106'
SAT = 'GO:0009001'
OASS = 'GO:0004124'
# Exact reviewed reaction roles, independent of annotation presence or gene name.
# KT2440 assignments are conserved-role inferences, not direct native assays.
ROLE_MEMBERS = {
    SAT: {'P0A9D4', 'Q88PL0', 'Q9HXI6', 'Q0PAC7', 'Q06750', 'P95231'},
    OASS: {'P0ABK5', 'P16703', 'Q88E95', 'Q88MC0', 'Q9I0D3', 'Q9I526',
           'P71128', 'P37887', 'P9WP55'},
}
COMPARATOR = 'P9WP53'
REACTIONS = {
    SAT: ({'CHEBI:33384', 'CHEBI:57288'}, {'CHEBI:58340', 'CHEBI:57287'}),
    OASS: ({'CHEBI:58340', 'CHEBI:29919'}, {'CHEBI:35235', 'CHEBI:30089'}),
}


def read(path):
    return yaml.safe_load(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload(row):
    return {k: v for k, v in row.items() if k != 'review'}


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def assemble_baseline():
    """Only pre-edit captures are inputs; never read current gene reviews here."""
    destination = AUDIT / 'seed-baseline.yaml'
    assert not destination.exists(), 'Refusing to overwrite the frozen seed baseline'
    members, sources = [], []

    def load(name):
        path = LOG / name
        sources.append({'path': str(path.relative_to(ROOT)), 'sha256': digest(path)})
        return json.loads(path.read_text())

    def add(path, doc, raw, providers=None, origin='new_seed'):
        members.append({
            'review_path': path, 'accession': doc['id'], 'taxon': doc['taxon'],
            'gene_symbol': doc['gene_symbol'], 'origin': origin,
            'annotations': [{'payload': payload(row),
                             'prior_action': row.get('review', {}).get('action')}
                            for row in doc.get('existing_annotations', [])],
            'raw_sha256': raw, 'provider_sha256': providers or {},
        })

    original = load('original-members-baseline.json')
    assert sum(len(m['document']['existing_annotations']) for m in original['members']) == 79
    for member in original['members']:
        add(member['review_path'], member['document'], member['raw_sha256'],
            member['provider_sha256'], 'original_review')
    seeded = load('pseae-cysk-baseline.json')
    assert seeded['review']['status'] == 'INITIALIZED'
    assert seeded['payloads'] == [payload(r) for r in seeded['review']['existing_annotations']]
    add('genes/PSEAE/cysK/cysK-ai-review.yaml', seeded['review'], seeded['raw_hashes'])
    for target in ['CAMJE-cysE', 'CAMJE-cysM', 'MYCTU-cysE', 'MYCTU-cysK1',
                   'MYCTU-cysM', 'BACSU-cysE', 'BACSU-cysK']:
        seeded = load(f'alternative-panel/{target}-baseline.json')
        doc = seeded['seed_document']
        assert doc['status'] == 'INITIALIZED'
        assert seeded['original_payloads'] == [payload(r) for r in doc['existing_annotations']]
        add(seeded['review_path'], doc, seeded['raw_sha256'])
    assert len(members) == 16
    AUDIT.mkdir(parents=True, exist_ok=True)
    destination.write_text(yaml.safe_dump({
        'scope': 'Pristine row payloads and source hashes; assembled only from pre-edit captures.',
        'capture_sources': sources, 'members': members,
    }, sort_keys=False))
    print(f'Frozen {len(members)} members from {len(sources)} pre-edit captures')


def load_panel(baseline):
    panel, counts, actions, review_hashes = {}, Counter(), Counter(), {}
    for member in baseline['members']:
        path = ROOT / member['review_path']
        gene = read(path)
        assert gene['status'] == 'COMPLETE', path
        for key in ['id', 'taxon', 'gene_symbol']:
            assert gene[key] == member['accession' if key == 'id' else key], path
        rows, seeds = gene.get('existing_annotations', []), member['annotations']
        assert len(rows) >= len(seeds), path
        for seed, row in zip(seeds, rows):
            assert payload(row) == seed['payload'], (path, row['term'])
            inherited = seed['prior_action'] == 'NEW'
            if inherited:
                assert row['review']['action'] == 'NEW', path
            counts['inherited_NEW' if inherited else 'machine_rows_preserved'] += 1
        for row in rows[len(seeds):]:
            assert row['review']['action'] == 'NEW', (path, row)
            counts['genuinely_added_NEW'] += 1
        for row in rows:
            assert row['review']['action'] != 'PENDING', path
            actions[row['review']['action']] += 1
        counts.update(complete_reviews=1, historical_rows=len(seeds), current_rows=len(rows))
        if member['origin'] == 'original_review':
            counts['original_rows'] += len(seeds)
        for field, count in [('raw_sha256', 'raw_files_preserved'),
                             ('provider_sha256', 'provider_artifacts_preserved')]:
            for filename, expected in member[field].items():
                assert digest(ROOT / filename) == expected, filename
                counts[count] += 1
        raw = path.with_name(path.name.replace('-ai-review.yaml', '-uniprot.txt')).read_text()
        families = set()
        for db, ident in re.findall(r'^DR\s+(PANTHER|InterPro|Pfam|NCBIfam); ([^;]+);', raw, re.M):
            families.add(f'{db}:{ident}')
            if db == 'PANTHER':
                families.add(f'PANTHER:{ident.split(":")[0]}')
        core = {c['molecular_function']['id'] for c in gene.get('core_functions', [])
                if c.get('molecular_function')}
        panel[gene['id']] = {
            'accession': gene['id'], 'taxon': gene['taxon']['id'], 'families': families,
            'core': core, 'roles': {mf for mf, members in ROLE_MEMBERS.items() if gene['id'] in members},
        }
        review_hashes[member['review_path']] = digest(path)
    assert counts['original_rows'] == 79
    assert counts['inherited_NEW'] == 3
    assert counts['raw_files_preserved'] == 32
    assert counts['provider_artifacts_preserved'] == 3
    return panel, counts, actions, review_hashes


def main():
    baseline = read(AUDIT / 'seed-baseline.yaml')
    doc = read(ROOT / 'modules' / f'{SLUG}.yaml')
    panel, counts, actions, hashes = load_panel(baseline)
    circuit = compile_node(doc['module'])
    atoms = list(iter_atoms(circuit))
    annotons = {n['id']: n for n in walk(doc['module']) if 'participant' in n and 'function' in n}
    representatives = {acc for a in atoms for acc in a.uniprots}
    assert representatives == set(panel) - {COMPARATOR}, 'Final positive panel integration incomplete or comparator selected'
    assert len(atoms) == 4, 'Expected CysE plus three terminal implementation descriptors'
    for atom in atoms:
        assert len(atom.function_ids) == 1
        mf = atom.function_ids[0]
        substrates, products = REACTIONS[mf]
        function = annotons[atom.node_id]['function']
        assert {x['term']['id'] for x in function['substrates']} == substrates
        assert {x['term']['id'] for x in function['products']} == products
        assert atom.family_ids, atom
        for accession in atom.uniprots:
            assert accession in panel
            assert mf in panel[accession]['roles']
            assert set(atom.family_ids) <= panel[accession]['families'], accession
            assert mf in panel[accession]['core'], accession
    unplaced = annotons['unplaced_oas_sulfhydrylase_activity']['participant']['family']
    assert {x['term']['id'] for x in unplaced['representative_members']} == {'UniProtKB:P71128'}
    assert not unplaced.get('ancestral_nodes'), 'Cj symbol cannot manufacture a PAINT placement'
    assert not any('cysteine synthase complex' in a.label.lower() for a in atoms)

    cases = []

    def capacity(available, tested_circuit=circuit, drop_roles=(), drop_core=(), drop_families=()):
        records = deepcopy(available)
        for record in records:
            if record['accession'] in drop_roles:
                record['roles'].clear()
            if record['accession'] in drop_core:
                record['core'].clear()
            if record['accession'] in drop_families:
                record['families'].clear()
        # A route must be satisfied wholly within one actual strain taxon.
        def holds(atom, taxon):
            return any(r['taxon'] == taxon and r['accession'] in atom.uniprots
                       and set(atom.function_ids) <= r['core']
                       and set(atom.function_ids) <= r['roles']
                       and set(atom.family_ids) <= r['families'] for r in records)
        return any(is_satisfied(tested_circuit, lambda a: holds(a, taxon))
                   for taxon in {r['taxon'] for r in records})

    def check(name, accessions, expected, **kwargs):
        records = kwargs.pop('records', [panel[a] for a in accessions])
        observed = capacity(records, **kwargs)
        cases.append({'name': name, 'accessions': accessions, 'expected': expected, 'observed': observed})
        assert observed == expected, name

    for sat in sorted(ROLE_MEMBERS[SAT]):
        terminals = sorted(a for a in ROLE_MEMBERS[OASS] if panel[a]['taxon'] == panel[sat]['taxon'])
        assert terminals, sat
        check(f'{sat}: missing terminal', [sat], False)
        check(f'{sat}: terminals without CysE', terminals, False)
        for terminal in terminals:
            pair = [sat, terminal]
            check(f'{sat}+{terminal}: reviewed route without required CSC', pair, True)
            for gate in ['drop_roles', 'drop_core', 'drop_families']:
                check(f'{sat}+{terminal}: terminal {gate}', pair, False, **{gate: [terminal]})
        if len(terminals) > 1:
            check(f'{sat}: both terminal alternatives coexist', [sat, *terminals], True)
    check('Empty panel', [], False)
    check('Cross-strain CysE/terminal cannot combine', ['P0A9D4', 'Q88E95'], False)
    check('MYCTU OPS/CysO comparator does not replace CysK1', ['P95231', COMPARATOR], False)
    mutant = deepcopy(panel[COMPARATOR])
    mutant['core'].add(OASS)
    check('Even hypothetical secondary GO0004124 acceptance is not curated OAS route',
          ['P95231', COMPARATOR], False, records=[panel['P95231'], mutant])
    # Also mutate module selection, showing the independent role gate still protects it.
    altered = deepcopy(doc['module'])
    target = next(n for n in walk(altered) if n.get('id') == 'cysM_activity')
    target['participant']['family']['representative_members'].append(
        {'term': {'id': f'UniProtKB:{COMPARATOR}', 'label': 'Synthetic comparator insertion'}})
    check('Comparator selected plus hypothetical MF still lacks curated route role',
          ['P95231', COMPARATOR], False, records=[panel['P95231'], mutant],
          tested_circuit=compile_node(altered))
    for label in ['generic CBS', 'OPS sulfurtransferase']:
        fake = {'accession': f'SYNTHETIC_{label}', 'taxon': panel['P0A9D4']['taxon'],
                'families': {'PANTHER:PTHR10314'}, 'core': {OASS}, 'roles': set()}
        check(f'Family plus GO alone: {label}', [], False, records=[panel['P0A9D4'], fake])
    check('All 15 positive exemplars coexist', sorted(representatives), True)
    result = {
        'scope': 'Reviewed-panel biochemical capability; not genome completeness, native flux or growth. '
                 'KT2440 roles are inference. Minor chemistry and gene names cannot establish a core route.',
        'engine': 'ai_gene_review.module_logic.compile_node/is_satisfied',
        'oracle_requirements': ['reviewed core reaction', 'curated exact-member route role',
                                'module representative', 'actual family', 'same strain taxon'],
        'limitations': ['The production compiler does not enforce taxon or substrate semantics; this oracle does.',
                        'No family-only genome inference or unsupported native pathway use is claimed.'],
        'passed': len(cases), 'cases': cases,
    }
    (AUDIT / 'capacity-results.yaml').write_text(yaml.safe_dump(result, sort_keys=False))
    checks = {'counts': dict(counts), 'actions': dict(actions), 'review_sha256': hashes,
              'seed_baseline_sha256': digest(AUDIT / 'seed-baseline.yaml'),
              'module_sha256': digest(ROOT / 'modules' / f'{SLUG}.yaml'),
              'checks': {'machine_payloads_preserved': True, 'inherited_NEW_preserved': True,
                         'raw_and_provider_bytes_preserved': True, 'complete_reviews': True,
                         'module_members_match_positive_panel': True, 'exact_reaction_boundaries': True,
                         'CAMJE_no_invented_PTN': True, 'capacity_cases_passed': len(cases)}}
    (AUDIT / 'integration-checks.yaml').write_text(yaml.safe_dump(checks, sort_keys=False))
    print(f'PASS: {dict(counts)}; {len(cases)} production-compiler capacity cases')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--assemble-baseline', action='store_true')
    args = parser.parse_args()
    if args.assemble_baseline:
        assemble_baseline()
    else:
        main()
