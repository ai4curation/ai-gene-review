"""Execute production LPS module logic with a separate evidence-qualified oracle.

This oracle checks a bounded reviewed panel, not arbitrary genome capacity or flux.
"""
import copy
import json
from dataclasses import asdict
from pathlib import Path

import yaml

from ai_gene_review.module_logic import compile_node, core_atoms, count_routes, is_satisfied, iter_atoms

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
MODULE = ROOT / 'modules/bacterial_lps_transport.yaml'
ROLE_UNITS = {'lptb_atpase': 'B', 'lptf_permease': 'F', 'lptg_permease': 'G',
              'lptd_barrel': 'D', 'lpte_plug': 'E', 'neis_lptd_component': 'D'}
SIMPLE = {'lptc_bridge_anchor': 'C', 'lpta_bridge': 'A', 'neis_lpte_assembly': 'E',
          'lptM_accessory': 'M', 'yedD_accessory': 'Y'}
COMPLEX_FUNCTIONS = {'lptb2fg_extractor': 'GO:0140332', 'lptde_translocon': 'GO:0015221',
                     'neis_lptd_insertion': 'GO:0015221'}
ROLE_MF = {'A': ('molecular_function', 'GO:0140332'),
           'B': ('molecular_function', 'GO:0016887'),
           'C': ('molecular_function', 'GO:0140332'),
           'D': ('contributes_to_molecular_function', 'GO:0015221'),
           'E': ('contributes_to_molecular_function', 'GO:0015221'),
           'F': ('contributes_to_molecular_function', 'GO:0140332'),
           'G': ('contributes_to_molecular_function', 'GO:0140332'),
           'M': ('contributes_to_molecular_function', 'GO:0015221'),
           'Y': ('contributes_to_molecular_function', 'GO:0015221')}
PANELS = {
    'ECOLI': {'A': 'P0ADV1', 'B': 'P0A9V1', 'C': 'P0ADV9', 'D': 'P31554',
              'E': 'P0ADC1', 'F': 'P0AF98', 'G': 'P0ADC6', 'M': 'P0ADN6', 'Y': 'P31063'},
    'PSEPK': {'A': 'Q88P98', 'B': 'Q88P99', 'C': 'Q88P97', 'D': 'A0A140FVZ0',
              'E': 'Q88DN0', 'F': 'Q88P71', 'G': 'Q88P70'},
    'H44': {'A': 'Q7DDQ9', 'D': 'F0MIT7', 'E': 'Q9K0A7'},
}
TAXA = {'ECOLI': ['NCBITaxon:2', 'NCBITaxon:1236', 'NCBITaxon:91347', 'NCBITaxon:83333'],
        'PSEPK': ['NCBITaxon:2', 'NCBITaxon:1236', 'NCBITaxon:160488'],
        'H44': ['NCBITaxon:2', 'NCBITaxon:487', 'NCBITaxon:909420']}


def load_members():
    registry = {}
    for panel, roles in PANELS.items():
        for role, accession in roles.items():
            species = 'NEIMH' if accession == 'F0MIT7' else 'NEIMB' if panel == 'H44' else panel
            gene = {'Q88P71': 'PP_0982', 'Q88P70': 'PP_0983', 'Q7DDQ9': 'lptH',
                    'P31063': 'yedD'}.get(accession, 'lpt' + role)
            path = Path(f'genes/{species}/{gene}/{gene}-ai-review.yaml')
            doc = yaml.safe_load((ROOT / path).read_text())
            assert doc['id'] == accession and doc['status'] == 'COMPLETE'
            expected_taxon = 'NCBITaxon:122586' if species == 'NEIMB' else TAXA[panel][-1]
            assert doc['taxon']['id'] == expected_taxon
            cores = doc['core_functions']
            if panel == 'H44' and role == 'E':
                licensed = any(any(t['id'] == 'GO:0043165' for t in c.get('directly_involved_in', []))
                               and c.get('supported_by') for c in cores)
                assert not any(c.get('contributes_to_molecular_function') for c in cores)
            else:
                slot, term = ROLE_MF[role]
                licensed = any(c.get(slot, {}).get('id') == term and c.get('supported_by') for c in cores)
                assert licensed, (accession, role, slot, term)
            raw = (ROOT / path.with_name(gene + '-uniprot.txt')).read_text()
            families = []
            for line in raw.splitlines():
                if line.startswith(('DR   PANTHER;', 'DR   NCBIfam;')):
                    parts = line.split(';')
                    db = 'PANTHER' if 'PANTHER' in parts[0] else 'NCBIfam'
                    families.append(db + ':' + parts[1].strip())
            registry[accession] = {'review': str(path), 'role': role, 'panel': panel,
                                   'taxon': expected_taxon, 'licensed': bool(licensed),
                                   'families': families, 'core_functions': cores,
                                   'evidence_tier': ('native/target primary plus curated synthesis' if panel == 'ECOLI'
                                                     else 'curated ortholog inference; not native KT2440 assay' if panel == 'PSEPK'
                                                     else 'H44/76 native phenotype; exact MC58 protein bridge for E/H')}
    assert len(registry) == 19
    return registry


def descriptors(doc):
    nodes, atoms = {}, {}

    def walk(node, taxa=()):
        own = tuple(x['term']['id'] for x in node.get('context', {}).get('taxa', []))
        taxa = taxa + own
        nodes[node['id']] = node
        for atom in node.get('annotons', []):
            atoms[atom['id']] = (atom, taxa)
        for part in node.get('parts', []):
            walk(part['node'], taxa)
        for variants in node.get('variant_sets', []):
            for variant in variants['variants']:
                walk(variant, taxa)
    walk(doc['module'])
    return nodes, atoms


def selector_members(selector):
    if selector['selector_type'] == 'GENE_PRODUCT':
        return {selector['gene']['term']['id'].removeprefix('UniProtKB:')}, []
    family = selector['family']
    return ({x['term']['id'].removeprefix('UniProtKB:') for x in family['representative_members']},
            [family['term']['id']] if family.get('term') else [])


class Oracle:
    def __init__(self, doc, registry, case, disabled=()):
        self.nodes, self.atoms = descriptors(doc)
        self.registry, self.case, self.disabled = registry, case, set(disabled)

    def gate(self, name, condition):
        return name in self.disabled or condition

    def role(self, role, selector=None):
        candidates = set(self.case['members'])
        if selector is not None:
            representatives, families = selector_members(selector)
            candidates &= representatives
        else:
            families = []
        for accession in candidates:
            member = self.registry.get(accession)
            if not member:
                continue
            if not self.gate('role', member['role'] == role):
                continue
            if not self.gate('evidence', member['licensed'] and accession not in self.case.get('evidence_blocked', [])):
                continue
            if not all(f in member['families'] for f in families):
                continue
            if not self.gate('panel', member['panel'] == self.case['panel']):
                continue
            if member['taxon'] == 'NCBITaxon:122586' and self.case['panel'] == 'H44':
                if not self.gate('identity_bridge', self.case['sequence_bridge']):
                    continue
            return True
        return False

    def __call__(self, atom):
        item, taxa = self.atoms[atom.node_id]
        c = self.case
        if not self.gate('lineage', all(t in c['taxa'] for t in taxa)):
            return False
        if not self.gate('substrate', c['substrate'] in {'LPS', 'LOS'}):
            return False
        if not self.gate('diderm', c['diderm']):
            return False
        if not self.gate('interfaces', c['interfaces']):
            return False
        if atom.node_id in COMPLEX_FUNCTIONS:
            if item.get('function', {}).get('term', {}).get('id') != COMPLEX_FUNCTIONS[atom.node_id]:
                return False
            units = item['participant']['protein_complex']['active_units']
            result = all(self.role(ROLE_UNITS[unit['id']], unit['participant']) for unit in units)
            if atom.node_id == 'lptb2fg_extractor':
                return result and self.gate('ATP', c['ATP'])
            # Terminal activity is a component of a compatible native bridge, not isolated D/DE flux.
            return result and c['native_bridge'] and self.role('A')
        if atom.node_id in SIMPLE:
            if atom.node_id in {'lptc_bridge_anchor', 'lpta_bridge'} and atom.function_ids != ('GO:0140332',):
                return False
            result = self.role(SIMPLE[atom.node_id], item['participant'])
            if atom.node_id in {'neis_lpte_assembly', 'lptM_accessory', 'yedD_accessory'}:
                result = result and c['native_bridge'] and self.role('D') and self.role('A')
            return result
        raise AssertionError('Unassessed atom ' + atom.node_id)


def base_case(panel, members=None):
    return {'panel': panel, 'members': members or [v for r, v in PANELS[panel].items() if r not in {'M', 'Y'}],
            'taxa': TAXA[panel], 'substrate': 'LOS' if panel == 'H44' else 'LPS',
            'diderm': True, 'ATP': True, 'interfaces': True, 'native_bridge': True,
            'sequence_bridge': True, 'evidence_blocked': []}


def cases():
    out = []

    def add(name, context, whole, terminal, note=''):
        out.append({'id': name, 'context': context, 'expected_whole': whole,
                    'expected_terminal': terminal, 'scope': note})
    for panel in ['ECOLI', 'PSEPK']:
        base = base_case(panel)
        add(panel + '_complete', base, True, True,
            'Complete reviewed native component panel; KT2440 activity remains inferred rather than directly assayed.' )
        for role in 'ABCDEFG':
            c = copy.deepcopy(base)
            c['members'].remove(PANELS[panel][role])
            add(panel + '_missing_' + role, c, False, role not in 'ADE',
                'Failure of the demonstrated canonical panel, not a universal biological impossibility.')
        for gate, value in [('ATP', False), ('substrate', 'phospholipid'), ('diderm', False), ('interfaces', False)]:
            c = copy.deepcopy(base)
            c[gate] = value
            add(panel + '_no_' + gate, c, False, gate == 'ATP')
    for extra in [('M',), ('Y',), ('M', 'Y')]:
        c = base_case('ECOLI')
        c['members'] += [PANELS['ECOLI'][r] for r in extra]
        add('ECOLI_optional_' + ''.join(extra), c, True, True,
            'Accessory role can improve terminal work; no quantitative flux is inferred.')
    c = base_case('ECOLI')
    c['members'] = [v for v in c['members'] if v != PANELS['ECOLI']['G']] + [PANELS['ECOLI']['F']]
    add('duplicate_F_not_G', c, False, True, 'Two copies of F do not supply the distinct G role.')
    c = base_case('ECOLI')
    c['members'].remove(PANELS['ECOLI']['B'])
    c['members'].append('GENERIC_ABC_ATPASE')
    add('generic_ABC_not_B', c, False, True)
    c = base_case('ECOLI', ['GENERIC_LPT_FAMILY', 'GENERIC_ABC_ATPASE', 'GENERIC_LPS_BINDER'])
    add('family_GO_only', c, False, False, 'No source-qualified role assignments.')
    for role in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        c = base_case('ECOLI')
        c['members'].remove(PANELS['ECOLI'][role])
        c['members'].append(PANELS['PSEPK'][role])
        add('cross_panel_' + role, c, False, role not in 'ADE', 'No positive mixed-interface evidence; not proof of incompatibility in all engineered conditions.')
    c = base_case('ECOLI')
    c['evidence_blocked'] = [PANELS['ECOLI']['B']]
    add('B_evidence_removed', c, False, True)
    c = base_case('ECOLI')
    c['members'].remove(PANELS['ECOLI']['C'])
    add('documented_C_suppressor_boundary', c, False, True,
        'PMID27529623 selected LptF suppressors support conditional bypass outside this canonical profile. No normal C-independent route asserted.')
    c = base_case('ECOLI')
    c['members'].remove(PANELS['ECOLI']['E'])
    c['members'].append(PANELS['H44']['E'])
    add('neis_E_not_canonical_E', c, False, False)
    for members, suffix in [(['A', 'D', 'E'], 'DHE'), (['A', 'D'], 'DH_without_E'), (['D'], 'D_only'), (['E'], 'E_only'), (['A'], 'H_only')]:
        c = base_case('H44', [PANELS['H44'][r] for r in members])
        add('H44_' + suffix, c, False, 'A' in members and 'D' in members,
            'Partial reviewed H44-compatible panel; MC58 E/H proteins are exact native CDS matches, not MC58 phenotype assays. No reviewed extractor panel.')
    c = base_case('H44')
    c['sequence_bridge'] = False
    add('H44_without_identity_bridge', c, False, False)
    c = base_case('H44')
    c['panel'] = 'MC58'
    c['taxa'] = ['NCBITaxon:2', 'NCBITaxon:487', 'NCBITaxon:122586']
    add('cross_strain_not_native_MC58', c, False, False)
    c = base_case('H44')
    c['native_bridge'] = False
    add('isolated_neis_components', c, False, False)
    c = base_case('ECOLI', [PANELS['ECOLI']['M'], PANELS['ECOLI']['Y']])
    add('accessories_only', c, False, False)
    c = base_case('ECOLI')
    c['members'] += [PANELS['ECOLI']['M'], PANELS['ECOLI']['Y']]
    c['members'].remove(PANELS['ECOLI']['D'])
    add('accessories_cannot_replace_D', c, False, False)
    c = base_case('ECOLI')
    c['substrate'] = 'absent'
    add('LPS_free_diderm', c, False, False, 'Lpt-like homologs in a diderm lacking LPS do not establish LPS transport.')
    for role, accession, family in [('A', 'Q9RS08', 'PTHR36504:SF1'),
                                    ('B', 'Q9RSJ0', 'PTHR45772:SF10'),
                                    ('G', 'Q9RVF4', 'PTHR33529:SF2'),
                                    ('D', 'Q9X257', 'PTHR30189:SF1')]:
        c = base_case('ECOLI')
        c['members'].remove(PANELS['ECOLI'][role])
        c['members'].append(accession)
        add('same_subfamily_unlicensed_' + role, c, False, role not in 'AD',
            accession + ' is in ' + family + ' in the frozen family tree; family membership and native non-LPS context do not license an LPS role or compatible substitution. No universal loss of lipid transport inferred.')
    c = base_case('ECOLI', ['MSBA', 'LIPID_A_BIOSYNTHESIS'])
    add('upstream_not_Lpt', c, False, False, 'Synthesis/flipping is outside the modeled starting boundary.')
    return out


def evaluate(doc, registry, case, disabled=()):
    oracle = Oracle(doc, registry, case['context'], disabled)
    circuit = compile_node(doc['module'])
    terminal = compile_node(oracle.nodes['outer_membrane_lptde'])
    return {'whole': is_satisfied(circuit, oracle), 'terminal': is_satisfied(terminal, oracle),
            'atoms': {a.node_id: oracle(a) for a in iter_atoms(circuit)}}


def mutated_models(doc):
    mutations = []

    def mutate(name, operation):
        clone = copy.deepcopy(doc)
        nodes, atoms = descriptors(clone)
        operation(clone, nodes, atoms)
        mutations.append((name, clone))
    for index, label in [(0, 'extraction'), (1, 'bridge'), (2, 'terminal')]:
        mutate('erase_required_' + label, lambda d, n, a, i=index: d['module']['parts'].pop(i))
    for unit in ['lptb_atpase', 'lptf_permease', 'lptg_permease']:
        def remove_unit(d, n, a, u=unit):
            units = a['lptb2fg_extractor'][0]['participant']['protein_complex']['active_units']
            units[:] = [x for x in units if x['id'] != u]
        mutate('erase_' + unit, remove_unit)
    mutate('erase_C_requirement', lambda d, n, a: n['inner_membrane_lptb2fgc']['annotons'].pop(1))
    mutate('erase_canonical_E', lambda d, n, a: a['lptde_translocon'][0]['participant']['protein_complex']['active_units'].pop(1))
    for part_id in ['lptM_terminal_support', 'yedD_terminal_support']:
        def required(d, n, a, pid=part_id):
            next(p for p in d['module']['parts'] if p['node']['id'] == pid)['optional'] = False
        mutate('force_' + part_id, required)
    mutate('force_neis_E', lambda d, n, a: n['meningococcal_lptd_delivery']['parts'][0].update(optional=False))
    def false_neis(d, n, a):
        n['meningococcal_lptd_delivery'].pop('context')
        unit = a['neis_lptd_insertion'][0]['participant']['protein_complex']['active_units'][0]
        unit['participant'] = copy.deepcopy(a['lptde_translocon'][0]['participant']['protein_complex']['active_units'][0]['participant'])
    mutate('generalize_neis_E_bypass', false_neis)
    mutate('wrong_extractor_activity', lambda d, n, a: a['lptb2fg_extractor'][0]['function']['term'].update(id='GO:0005524'))
    mutate('wrong_bridge_activity', lambda d, n, a: a['lpta_bridge'][0]['function']['term'].update(id='GO:0005524'))
    return mutations


def main():
    doc = yaml.safe_load(MODULE.read_text())
    registry = load_members()
    examples = cases()
    outputs = []
    for case in examples:
        actual = evaluate(doc, registry, case)
        assert actual['whole'] == case['expected_whole'], (case['id'], actual)
        assert actual['terminal'] == case['expected_terminal'], (case['id'], actual)
        outputs.append({'case': case['id'], **actual})
    detected = []
    for name, changed in mutated_models(doc):
        failures = []
        for case in examples:
            # Removed terminal node is evaluated only as whole-system mutation.
            if name == 'erase_required_terminal':
                oracle = Oracle(changed, registry, case['context'])
                result = is_satisfied(compile_node(changed['module']), oracle)
                mismatch = result != case['expected_whole']
            else:
                actual = evaluate(changed, registry, case)
                mismatch = actual['whole'] != case['expected_whole'] or actual['terminal'] != case['expected_terminal']
            if mismatch:
                failures.append(case['id'])
        expected_core = {'lptb2fg_extractor', 'lptc_bridge_anchor', 'lpta_bridge'}
        changed_core = {a.node_id for a in core_atoms(compile_node(changed['module']))}
        contract_failure = changed_core != expected_core
        assert failures or contract_failure, ('undetected model mutation', name)
        detected.append({'mutation': name, 'detected_by_cases': failures,
                         'production_core_contract_detected': contract_failure,
                         'note': 'The external terminal bridge gate also requires A; deletion of the explicit A atom is caught by the compiled-core contract even when that guard prevents a changed case result.' if name == 'erase_required_bridge' else ''})
    by_id = {c['id']: c for c in examples}
    sensitivities = []
    for case_id, gate, output in [('ECOLI_no_ATP', 'ATP', 'whole'),
                                   ('LPS_free_diderm', 'substrate', 'whole'),
                                   ('ECOLI_no_diderm', 'diderm', 'whole'),
                                   ('ECOLI_no_interfaces', 'interfaces', 'whole'),
                                   ('cross_panel_G', 'panel', 'whole'),
                                   ('B_evidence_removed', 'evidence', 'whole'),
                                   ('H44_without_identity_bridge', 'identity_bridge', 'terminal')]:
        actual = evaluate(doc, registry, by_id[case_id], [gate])
        assert actual[output] and not evaluate(doc, registry, by_id[case_id])[output]
        sensitivities.append({'case': case_id, 'erased_gate': gate, 'false_positive_output': output})
    # A deliberately naive GO-only oracle exposes complex/role/lineage information lost by compilation.
    naive = is_satisfied(compile_node(doc['module']), lambda a: not a.function_ids or set(a.function_ids) <= {'GO:0140332', 'GO:0015221'})
    assert naive and not evaluate(doc, registry, by_id['family_GO_only'])['whole']
    circuit = compile_node(doc['module'])
    results = {'status': 'PASS', 'case_count': len(examples), 'mutation_count': len(detected),
               'gate_sensitivity_count': len(sensitivities), 'generic_GO_false_positive_demonstrated': naive,
               'formal_combinations': count_routes(circuit), 'core_atoms': [a.node_id for a in core_atoms(circuit)],
               'compiled_atoms': [asdict(a) for a in iter_atoms(circuit)], 'cases': outputs,
               'model_mutations': detected, 'gate_sensitivities': sensitivities,
               'scope': 'Evidence-qualified panel capacity, not measured native flux or universal impossibility. Production compiler does not expand active_units or enforce context/EXACTLY_ONE exclusivity.'}
    (HERE / 'cases.json').write_text(json.dumps(examples, indent=2) + '\n')
    (HERE / 'members.json').write_text(json.dumps(registry, indent=2, ensure_ascii=False) + '\n')
    (HERE / 'results.json').write_text(json.dumps(results, indent=2) + '\n')
    print(json.dumps({k: results[k] for k in ['status', 'case_count', 'mutation_count', 'gate_sensitivity_count', 'formal_combinations']}))


if __name__ == '__main__':
    main()
