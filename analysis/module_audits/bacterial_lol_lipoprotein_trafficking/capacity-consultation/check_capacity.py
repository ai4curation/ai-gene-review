"""Bounded Lol evidence oracle over the production module compiler.

Run with uv run python <this-file>. No source or curated record is changed.
"""

from __future__ import annotations

import copy
import hashlib
import itertools
import json
from pathlib import Path

import yaml

from ai_gene_review.module_logic import compile_node, core_atoms, is_satisfied, iter_atoms

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
MODULE = ROOT / 'modules/bacterial_lol_lipoprotein_trafficking.yaml'
INSERTION = 'outer-membrane lipoprotein insertion activity'
ALIAS = {'Q9EYM3': 'A0ACM8PZZ0'}
PANELS = {
    'ECOLI': {'C': 'P0ADC3', 'D': 'P75957', 'E': 'P75958', 'A': 'P61316', 'B': 'P61320'},
    'PSEPK': {'C': 'Q88KY5', 'D': 'Q88KY4', 'E': 'Q88KY3', 'A': 'Q88FS9', 'B': 'Q88PX4'},
    'ACIAD': {'F': 'A0ACM8PZZ0', 'D': 'Q9EYM2', 'A': 'Q6F8G3', 'B': 'Q6F8J1'},
    'FLAJ1': {'A': 'A5FI22', 'B': 'A5FL25'},
    'CAUVC': {'AB': 'Q9A261'},
}
TAXA = {'ECOLI': 'NCBITaxon:83333', 'PSEPK': 'NCBITaxon:160488',
        'ACIAD': 'NCBITaxon:62977', 'FLAJ1': 'NCBITaxon:376686', 'CAUVC': 'NCBITaxon:190650'}
ROLE = {acc: role for panel in PANELS.values() for role, acc in panel.items()}
UNIT_ROLE = {'lolc_unit': 'C', 'lole_unit': 'E', 'lold_unit': 'D',
             'lolf_unit': 'F', 'lolfd_lold_unit': 'D'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def walk(node):
    yield node
    for part in node.get('parts', []):
        yield from walk(part['node'])
    for group in node.get('variant_sets', []):
        for variant in group['variants']:
            yield from walk(variant)


def load_members():
    records = {}
    for panel, roles in PANELS.items():
        for acc in roles.values():
            matches = []
            folders = ['lolA', 'lolB', 'lolC', 'lolD', 'lolE'] if panel in {'ECOLI', 'PSEPK', 'ACIAD'} else (['Fjoh_2111', 'Fjoh_1066'] if panel == 'FLAJ1' else ['CC_3705'])
            for folder in folders:
                path = ROOT / 'genes' / panel / folder / f'{folder}-ai-review.yaml'
                if not path.exists():
                    continue
                data = yaml.safe_load(path.read_text())
                if data['id'] == acc:
                    matches.append((path, data))
            assert len(matches) == 1, (acc, matches)
            path, data = matches[0]
            assert data.get('status') == 'COMPLETE', path
            assert data['taxon']['id'] == TAXA[panel], (path, data['taxon'])
            raw = path.with_name(path.name.replace('-ai-review.yaml', '-uniprot.txt'))
            families = set()
            for line in raw.read_text().splitlines():
                if line.startswith('DR   '):
                    fields = [s.strip() for s in line[5:].split(';')]
                    if fields[0] in {'PANTHER', 'Pfam', 'NCBIfam'}:
                        prefix = {'PANTHER': 'PANTHER', 'Pfam': 'Pfam', 'NCBIfam': 'NCBIfam'}[fields[0]]
                        families.add(f'{prefix}:{fields[1]}')
                        if fields[0] == 'PANTHER':
                            families.add(f'PANTHER:{fields[1].split(":")[0]}')
            mf, contributes, proposed = set(), set(), set()
            for core in data.get('core_functions', []):
                if core.get('molecular_function'):
                    mf.add(core['molecular_function']['id'])
                if core.get('contributes_to_molecular_function'):
                    contributes.add(core['contributes_to_molecular_function']['id'])
                if core.get('proposed_molecular_function'):
                    proposed.add(core['proposed_molecular_function'])
            records[acc] = dict(panel=panel, taxon=data['taxon']['id'], role=ROLE[acc],
                                path=str(path.relative_to(ROOT)), raw=str(raw.relative_to(ROOT)),
                                mf=mf, contributes=contributes, proposed=proposed, families=families)
    assert len(records) == 17
    return records


def selector(participant, records, present, activity=True):
    """Closed reviewed exemplars, with independently checked source family membership."""
    family = participant.get('family', {})
    reps = {r['term']['id'].removeprefix('UniProtKB:')
            for r in family.get('representative_members', [])}
    gene = participant.get('gene_product') or participant.get('gene')
    if gene:
        reps = {gene['term']['id'].removeprefix('UniProtKB:')}
    term = family.get('term', {}).get('id')
    candidates = present & reps & records.keys()
    if term:
        candidates = {a for a in candidates if term in records[a]['families']}
    required = participant.get('required_function', {})
    go = required.get('term', {}).get('id')
    name = required.get('preferred_term')
    if activity and go:
        candidates = {a for a in candidates if go in records[a]['mf']}
    elif activity and name == INSERTION:
        candidates = {a for a in candidates if INSERTION in records[a]['proposed']}
    return candidates


def evaluate(document, case, records, *, compatibility=True, activity=True, assembly=True):
    nodes = {n['id']: n for n in walk(document['module'])}
    annotons = {a['id']: a for n in nodes.values() for a in n.get('annotons', [])}
    present = {ALIAS.get(a, a) for a in case['members']}
    values, groups = {}, {}
    for aid, annoton in annotons.items():
        participant = annoton['participant']
        if participant['selector_type'] != 'PROTEIN_COMPLEX':
            continue
        sets = []
        for unit in participant['protein_complex']['active_units']:
            candidates = selector(unit['participant'], records, present, activity)
            role = UNIT_ROLE[unit['id']]
            candidates = {a for a in candidates if records[a]['role'] == role}
            if activity:
                candidates = {a for a in candidates if 'GO:0140306' in records[a]['contributes']}
            assert int(unit['stoichiometry']) > 0
            sets.append(candidates)
        # A stoichiometric homodimer uses multiple protein copies of ONE gene product.
        combinations = list(itertools.product(*sets)) if sets else []
        if compatibility:
            combinations = [c for c in combinations if len({records[a]['panel'] for a in c}) == 1]
        if not assembly:
            combinations = [(a,) for a in present & records.keys()
                            if 'GO:0140306' in records[a]['contributes']]
        values[aid] = bool(combinations)
        groups[aid] = {records[c[0]]['panel'] for c in combinations}
    extractor_panels = set().union(*groups.values())
    candidates = {}
    for aid, annoton in annotons.items():
        if aid in values:
            continue
        found = selector(annoton['participant'], records, present, activity)
        function = annoton.get('function', {})
        go = function.get('term', {}).get('id')
        name = function.get('preferred_term')
        if activity and go:
            found = {a for a in found if go in records[a]['mf']}
        if activity and name == INSERTION:
            found = {a for a in found if INSERTION in records[a]['proposed']}
        candidates[aid] = found
    carriers = candidates.get('lola_carrier', set())
    for bid in ('classical_lolb_insertase', 'duf4292_lolb_insertase'):
        pairs = [(a, b) for a in carriers for b in candidates.get(bid, set())]
        if compatibility:
            pairs = [(a, b) for a, b in pairs
                     if records[a]['panel'] == records[b]['panel']
                     and (not extractor_panels or records[a]['panel'] in extractor_panels)]
        values[bid] = bool(pairs)
    values['lola_carrier'] = bool(carriers)
    # One reviewed polypeptide must carry BOTH functions; separate hits do not suffice.
    shared = (candidates.get('bifunctional_lola_carrier', set())
              & candidates.get('bifunctional_lola_insertase', set()))
    if compatibility and extractor_panels:
        shared = {a for a in shared if records[a]['panel'] in extractor_panels
                  or (case['context'] == 'cviLolAeco_in_permissive_ecoli'
                      and extractor_panels == {'ECOLI'} and a == 'Q9A261')}
    values['bifunctional_lola_carrier'] = bool(shared)
    values['bifunctional_lola_insertase'] = bool(shared)
    result = {}
    for key, node in [('extraction', nodes['lipoprotein_extraction']),
                      ('delivery', nodes['lipoprotein_delivery']), ('complete', document['module'])]:
        circuit = compile_node(node)
        result[key] = is_satisfied(circuit, lambda atom: values.get(atom.node_id, False))
    return result, values


def main():
    document = yaml.safe_load(MODULE.read_text())
    source = yaml.safe_load((HERE / 'cases.yaml').read_text())
    records = load_members()
    cases = source['cases']
    cases.extend([
        dict(id='taxon_label_without_members', members=[], context='ECOLI',
             expected=dict(extraction=False, delivery=False, complete=False)),
        dict(id='flaj1_pair_with_foreign_extractor',
             members=['P0ADC3', 'P75957', 'P75958', 'A5FI22', 'A5FL25'],
             context='reviewed_native_panel', expected=dict(extraction=True, delivery=False, complete=False)),
    ])
    results = []
    for case in cases:
        result, atoms = evaluate(document, case, records)
        assert result == case['expected'], (case['id'], result, case['expected'])
        results.append(dict(id=case['id'], result=result, atom_truth=atoms))
    by_id = {c['id']: c for c in cases}
    sensitivity = []
    for name, cid, flags in [
        ('disable_assembly', 'isolated_lold', dict(assembly=False)),
        ('disable_partner_compatibility', 'mixed_ecoli_A_flaj1_B', dict(compatibility=False)),
        ('disable_extractor_compatibility', 'mixed_extractors', dict(compatibility=False)),
        ('disable_construct_scope', 'cb15_native_with_ecoli_extractor', dict(compatibility=False)),
    ]:
        qualified = evaluate(document, by_id[cid], records)[0]
        weakened = evaluate(document, by_id[cid], records, **flags)[0]
        assert qualified != weakened, name
        sensitivity.append(dict(gate=name, case=cid, qualified=qualified, weakened=weakened))
    # Mask measured/curated activity while preserving identity/family: presence must not suffice.
    masked = copy.deepcopy(records)
    masked['P61316']['mf'].clear()
    qualified = evaluate(document, by_id['ecoli_complete'], masked)[0]
    weakened = evaluate(document, by_id['ecoli_complete'], masked, activity=False)[0]
    assert not qualified['complete'] and weakened['complete']
    sensitivity.append(dict(gate='activity_masked_carrier', case='ecoli_complete',
                            qualified=qualified, weakened=weakened))
    mutations = []
    for name in ['delete_D_requirement', 'make_delivery_optional', 'force_CDE', 'collapse_C_E_role',
                 'split_bifunctional_polypeptide']:
        mutated = copy.deepcopy(document)
        nodes = {n['id']: n for n in walk(mutated['module'])}
        anns = {a['id']: a for n in nodes.values() for a in n.get('annotons', [])}
        if name == 'delete_D_requirement':
            units = anns['lolcde_release_complex']['participant']['protein_complex']['active_units']
            units[:] = [u for u in units if u['id'] != 'lold_unit']
        elif name == 'make_delivery_optional':
            for part in mutated['module']['parts']:
                if part['node']['id'] == 'lipoprotein_delivery':
                    part['optional'] = True
        elif name == 'force_CDE':
            nodes['lipoprotein_extraction']['variant_sets'][0]['variants'][:] = [nodes['lolcde_release_step']]
        elif name == 'collapse_C_E_role':
            units = anns['lolcde_release_complex']['participant']['protein_complex']['active_units']
            cunit = next(u for u in units if u['id'] == 'lolc_unit')
            eunit = next(u for u in units if u['id'] == 'lole_unit')
            eunit['participant'] = copy.deepcopy(cunit['participant'])
        else:
            anns['bifunctional_lola_insertase']['participant']['gene_product']['term']['id'] = 'UniProtKB:P61320'
        detected = [case['id'] for case in cases
                    if evaluate(mutated, case, records)[0] != case['expected']]
        assert detected, ('undetected mutation', name)
        mutations.append(dict(mutation=name, detected_by=detected))
    circuit = compile_node(document['module'])
    report = dict(status='PASS', module_sha256=sha(MODULE), module_status=document.get('status'),
                  production_engine_sha256=sha(ROOT / 'src/ai_gene_review/module_logic.py'),
                  member_count=len(records), case_count=len(cases), results=results,
                  production_atoms=[dict(id=a.node_id, function_ids=a.function_ids,
                                         members=a.uniprots, family_ids=a.family_ids)
                                    for a in iter_atoms(circuit)],
                  production_core_atoms=[a.node_id for a in core_atoms(circuit)],
                  mutations=mutations, sensitivity=sensitivity,
                  limitation='External source-qualified predicate supplies complex assembly, exact roles, '
                             'proposed insertion activity, compatibility and construct scope. Boolean engine '
                             'does not infer these facts. Negative means unlicensed canonical capacity, '
                             'not a biological impossibility or demonstrated loss.')
    (HERE / 'results.json').write_text(json.dumps(report, indent=2) + '\n')
    (HERE / 'member-closure.json').write_text(json.dumps(records, indent=2,
                                                      default=lambda x: sorted(x)) + '\n')
    print(json.dumps({k: report[k] for k in ['status', 'member_count', 'case_count', 'module_sha256']}))


if __name__ == '__main__':
    main()
