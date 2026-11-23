"""Production two-step PTS logic with independent source/role/domain/context gates."""
import copy
import json
from dataclasses import asdict
from pathlib import Path

import yaml

from ai_gene_review.module_logic import compile_node, core_atoms, is_satisfied, iter_atoms

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PANELS = {
    'ECOLI': [('manX', 'P69797', 'AB'), ('manY', 'P69801', 'C'), ('manZ', 'P69805', 'D')],
    'LACLA': [('ptnAB', 'Q9CEX8', 'AB'), ('ptnC', 'Q9CEX7', 'C'), ('ptnD', 'Q9CEX6', 'D')],
    'STRMU': [('manL', 'Q8DSC4', 'AB'), ('manM', 'Q8DSC3', 'C'), ('manN', 'Q8DSC2', 'D')],
}
TAXA = {'ECOLI': 'NCBITaxon:83333', 'LACLA': 'NCBITaxon:272623', 'STRMU': 'NCBITaxon:210007'}
DOMAINS = {'A': 'InterPro:IPR004701', 'B': 'InterPro:IPR004720',
           'C': 'InterPro:IPR004700', 'D': 'InterPro:IPR004704'}
RELAY = 'mannose_relay_activity'
TRANSPORT = 'mannose_coupled_transport_activity'


def members():
    registry = {}
    for panel, entries in PANELS.items():
        for gene, accession, roles in entries:
            path = Path(f'genes/{panel}/{gene}/{gene}-ai-review.yaml')
            doc = yaml.safe_load((ROOT / path).read_text())
            assert (doc['id'], doc['taxon']['id'], doc['status']) == (accession, TAXA[panel], 'COMPLETE')
            cores = doc['core_functions']
            assert any(c.get('contributes_to_molecular_function', {}).get('id') == 'GO:0022870'
                       and c.get('supported_by') for c in cores), path
            raw = (ROOT / path.with_name(gene + '-uniprot.txt')).read_text()
            classifications = set()
            for line in raw.splitlines():
                if line.startswith(('DR   PANTHER;', 'DR   InterPro;')):
                    db, identifier, *_ = line[5:].split(';')
                    classifications.add(db.strip() + ':' + identifier.strip())
            assert all(DOMAINS[r] in classifications for r in roles)
            registry[accession] = {'review': str(path), 'panel': panel, 'taxon': TAXA[panel],
                                   'roles': list(roles), 'classifications': sorted(classifications),
                                   'source_qualified': True, 'core_functions': cores}
    assert len(registry) == 9
    return registry


def nodes(doc):
    return {a['id']: a for p in doc['module']['parts'] for a in p['node'].get('annotons', [])}


def unit_role(unit):
    return {'eiia': 'A', 'eiib': 'B', 'eiic': 'C', 'eiid': 'D'}[unit['id'].rsplit('_', 1)[1]]


class Oracle:
    def __init__(self, doc, registry, context, disabled=()):
        self.atoms, self.registry, self.context = nodes(doc), registry, context
        self.disabled = set(disabled)
        self.bindings = {}

    def gate(self, name, condition):
        return name in self.disabled or condition

    def candidates(self, unit, atom_id):
        role = unit_role(unit)
        selector = unit['participant']
        family = selector['family'].get('term', {}).get('id')
        domain = selector.get('required_domain', {}).get('term', {}).get('id')
        found = set()
        for accession in self.context['members']:
            member = self.registry.get(accession)
            if not member:
                continue
            if not self.gate('role', role in member['roles'] and role not in self.context['disabled_roles'].get(accession, [])):
                continue
            if not self.gate('source', member['source_qualified'] and accession not in self.context['evidence_blocked']):
                continue
            if not self.gate('panel', member['panel'] == self.context['panel']):
                continue
            if family and not self.gate('family', family in member['classifications']):
                continue
            available = set(member['classifications']) - set(self.context['omitted_domains'].get(accession, []))
            if domain and not self.gate('domain', domain in available):
                continue
            if accession in self.context.get('stage_exclusions', {}).get(atom_id, []):
                continue
            found.add(accession)
        return found

    def __call__(self, atom):
        data = self.atoms[atom.node_id]
        c = self.context
        if not self.gate('interfaces', c['interfaces_supported']):
            return False
        units = data['participant']['protein_complex']['active_units']
        binding = {unit_role(u): self.candidates(u, atom.node_id) for u in units}
        self.bindings[atom.node_id] = binding
        if not all(binding.values()):
            return False
        if atom.node_id == RELAY:
            return self.gate('phospho_HPr', c['phospho_HPr'])
        if atom.node_id == TRANSPORT:
            if data['function'].get('term', {}).get('id') != 'GO:0022870':
                return False
            return (self.gate('mannose', c['substrate'] == 'D-mannose')
                    and self.gate('membrane', c['functional_membrane'])
                    and self.gate('phospho_EIIB', c['phospho_EIIB']))
        raise AssertionError(atom.node_id)


def evaluate(doc, registry, case, disabled=()):
    circuit = compile_node(doc['module'])
    oracle = Oracle(doc, registry, case['context'], set(disabled) | set(case.get('disabled_gates', [])))
    atom_results = {a.node_id: oracle(a) for a in iter_atoms(circuit)}
    compiled = is_satisfied(circuit, lambda a: atom_results[a.node_id])
    relay_b = oracle.bindings.get(RELAY, {}).get('B', set())
    transport_b = oracle.bindings.get(TRANSPORT, {}).get('B', set())
    donor_compatible = bool(relay_b & transport_b)
    if 'same_B' in disabled:
        donor_compatible = True
    return {'whole': compiled and donor_compatible,
            'relay': atom_results.get(RELAY, False), 'transport': atom_results.get(TRANSPORT, False),
            'same_B_product': donor_compatible,
            'bindings': {a: {r: sorted(v) for r, v in b.items()} for a, b in oracle.bindings.items()}}


def context(panel):
    return {'panel': panel, 'members': [a for _, a, _ in PANELS[panel]],
            'phospho_HPr': True, 'phospho_EIIB': True, 'functional_membrane': True,
            'substrate': 'D-mannose', 'interfaces_supported': True,
            'disabled_roles': {}, 'omitted_domains': {}, 'evidence_blocked': []}


def cases():
    examples = []

    def add(name, c, whole, relay, transport, note=''):
        examples.append({'id': name, 'context': c, 'expected': {'whole': whole, 'relay': relay, 'transport': transport}, 'scope': note})
    for panel, entries in PANELS.items():
        base = context(panel)
        add(panel + '_native_panel', base, True, True, True,
            'Three gene products supply four roles; the fused product supplies A and B. Capacity is source-qualified, not a flux prediction.')
        for role in 'ABCD':
            c = copy.deepcopy(base)
            accession = next(a for _, a, roles in entries if role in roles)
            c['disabled_roles'][accession] = [role]
            add(panel + '_role_missing_' + role, c, False, role in 'CD', role == 'A',
                'Computational capability ablation, not a claim about a newly made biological mutant.')
            c = copy.deepcopy(base)
            c['omitted_domains'][accession] = [DOMAINS[role]]
            add(panel + '_domain_missing_' + role, c, False, role in 'CD', role == 'A',
                'Adversarial candidate-evidence fixture: general family/GO remains, required domain support removed.')
        c = copy.deepcopy(base)
        c['members'].remove(entries[0][1])
        add(panel + '_fused_chain_absent', c, False, False, False)
        for gate, value, relay, transport in [
                ('phospho_HPr', False, False, True),
                ('phospho_EIIB', False, True, False),
                ('functional_membrane', False, True, False),
                ('substrate', 'D-fructose', True, False),
                ('interfaces_supported', False, False, False)]:
            c = copy.deepcopy(base)
            c[gate] = value
            add(panel + '_no_' + gate, c, False, relay, transport,
                'HPr-negative/initial-phospho-EIIB-positive isolates a possible stoichiometric input; it does not complete a regenerated HPr-fed cycle.')
    for role in 'ABCD':
        c = context('ECOLI')
        original = next(a for _, a, rs in PANELS['ECOLI'] if role in rs)
        replacement = next(a for _, a, rs in PANELS['LACLA'] if role in rs)
        c['members'].remove(original)
        c['members'].append(replacement)
        add('unsupported_cross_panel_' + role, c, False, role in 'CD', False,
            'No positive native or measured interface support for this mixed panel; not proof that every engineered combination is impossible.')
    c = context('ECOLI')
    c['evidence_blocked'] = ['P69801']
    add('C_source_support_removed', c, False, True, False)
    c = context('ECOLI')
    c['members'] = ['P69801', 'P69805']
    add('membrane_counterflow_only', c, False, False, False,
        'PMID31209249 supplementary counterflow reports membrane exchange, not complete HPr/IIAB-coupled group translocation.')
    add('phage_or_bacteriocin_receptor_only', copy.deepcopy(c), False, False, False,
        'Receptor behavior of C/D is not evidence for a complete phosphorylation cycle.')
    c = context('ECOLI')
    c['members'] = ['P26379', 'P26380', 'P26381', 'P26382']
    add('LevDEFG_fructose_control', c, False, False, False,
        'Official architecture and explicit PMID2117666 fructose/no-mannose report do not license a mannose panel. This oracle does not deny their fructose relay.')
    for name, absent, replacement in [('IIA_only_family_not_B', 'P69797', 'P26379'),
                                       ('soluble_family_not_C', 'P69801', 'P0C8J8'),
                                       ('generic_family_not_D', 'P69805', 'UNQUALIFIED_PTHR32502'),
                                       ('C_not_D', 'P69805', 'P69801')]:
        c = context('ECOLI')
        c['members'].remove(absent)
        c['members'].append(replacement)
        add(name, c, False, absent != 'P69797', False)
    c = context('STRMU')
    c['members'].remove('Q8DSC4')
    add('UA159_alternative_uptake_control', c, False, False, False,
        'Improved growth or uptake compensation after manL perturbation does not establish this selected module; false does not mean no alternative mannose uptake.')
    c = context('ECOLI')
    c['members'] = ['Q48519', 'Q48520', 'Q48521', 'Q48522']
    add('CECT904_architecture_comparator_only', c, False, False, False,
        'Primary separate-chain architecture and heterologous B complementation are real; inactive records and partial IID do not provide a complete active reviewed reference panel.')
    c = context('ECOLI')
    c['members'].append('Q9CEX8')
    c['stage_exclusions'] = {RELAY: ['Q9CEX8'], TRANSPORT: ['P69797']}
    add('different_B_donor_control', c, False, True, True,
        'Deliberately bypass the panel gate in this adversarial fixture: both step predicates can pass, but the relay product and transport donor are different chains. No actual cross-species compatibility is asserted.')
    examples[-1]['disabled_gates'] = ['panel']
    return examples


def mutations(doc):
    output = []

    def edit(name, change):
        clone = copy.deepcopy(doc)
        change(clone, nodes(clone))
        output.append((name, clone))
    for atom_id, role in [(RELAY, 'A'), (RELAY, 'B'), (TRANSPORT, 'B'), (TRANSPORT, 'C'), (TRANSPORT, 'D')]:
        def remove(d, atoms, aid=atom_id, r=role):
            units = atoms[aid]['participant']['protein_complex']['active_units']
            units[:] = [u for u in units if unit_role(u) != r]
        edit('erase_' + atom_id + '_' + role, remove)
        def erase_domain(d, atoms, aid=atom_id, r=role):
            unit = next(u for u in atoms[aid]['participant']['protein_complex']['active_units'] if unit_role(u) == r)
            unit['participant'].pop('required_domain')
        edit('erase_domain_' + atom_id + '_' + role, erase_domain)
    edit('wrong_transport_activity', lambda d, a: a[TRANSPORT]['function']['term'].update(id='GO:0009401'))
    edit('relay_optional', lambda d, a: d['module']['parts'][0].update(optional=True))
    edit('transport_optional', lambda d, a: d['module']['parts'][1].update(optional=True))
    return output


def main():
    path = ROOT / 'modules/bacterial_mannose_pts.yaml'
    doc = yaml.safe_load(path.read_text())
    registry = members()
    examples = cases()
    outputs = []
    for case in examples:
        actual = evaluate(doc, registry, case)
        assert all(actual[k] == v for k, v in case['expected'].items()), (case['id'], actual, case['expected'])
        outputs.append({'case': case['id'], **actual})
    mutation_results = []
    for label, model in mutations(doc):
        failures = []
        for case in examples:
            actual = evaluate(model, registry, case)
            if any(actual[k] != v for k, v in case['expected'].items()):
                failures.append(case['id'])
        structural = {a.node_id for a in core_atoms(compile_node(model['module']))} != {RELAY, TRANSPORT}
        assert failures or structural, ('undetected', label)
        mutation_results.append({'mutation': label, 'detected_by_cases': failures,
                                 'production_core_contract_detected': structural})
    by_id = {c['id']: c for c in examples}
    sensitivity = []
    for case, gate in [('ECOLI_no_phospho_HPr', 'phospho_HPr'),
                       ('ECOLI_no_phospho_EIIB', 'phospho_EIIB'),
                       ('ECOLI_no_functional_membrane', 'membrane'),
                       ('ECOLI_no_substrate', 'mannose'),
                       ('ECOLI_no_interfaces_supported', 'interfaces'),
                       ('C_source_support_removed', 'source'),
                       ('ECOLI_domain_missing_C', 'domain'),
                       ('unsupported_cross_panel_C', 'panel'),
                       ('different_B_donor_control', 'same_B')]:
        result = evaluate(doc, registry, by_id[case], [gate])
        assert result['whole'] and not evaluate(doc, registry, by_id[case])['whole'], (case, gate)
        sensitivity.append({'case': case, 'erased_gate': gate, 'false_positive': True})
    circuit = compile_node(doc['module'])
    assert {a.node_id for a in core_atoms(circuit)} == {RELAY, TRANSPORT}
    assert is_satisfied(circuit, lambda a: True)
    assert not is_satisfied(circuit, lambda a: a.node_id == RELAY)
    assert not is_satisfied(circuit, lambda a: a.node_id == TRANSPORT)
    # A family/domain-independent, complex-only compiler predicate is intentionally insufficient.
    bare_boolean_false_positives = [c['id'] for c in examples
                                   if not c['expected']['whole'] and is_satisfied(circuit, lambda a: True)]
    result = {'status': 'PASS', 'module_status': doc['status'], 'cases': outputs,
              'case_count': len(examples), 'mutation_count': len(mutation_results),
              'mutations': mutation_results, 'sensitivity_count': len(sensitivity), 'sensitivities': sensitivity,
              'bare_boolean_all_atoms_true_false_positives': bare_boolean_false_positives,
              'compiled_atoms': [{**asdict(a), 'is_grounded': a.is_grounded} for a in iter_atoms(circuit)],
              'core_atoms': [a.node_id for a in core_atoms(circuit)],
              'scope': 'Production compiler plus raw-active-unit role oracle; no native flux or universal biological absence inferred.'}
    for name, data in [('cases.json', examples), ('members.json', registry), ('results.json', result)]:
        (HERE / name).write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')
    print(json.dumps({k: result[k] for k in ['status', 'module_status', 'case_count', 'mutation_count', 'sensitivity_count']}))


if __name__ == '__main__':
    main()
