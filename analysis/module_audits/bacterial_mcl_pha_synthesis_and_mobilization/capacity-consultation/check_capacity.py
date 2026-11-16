"""Finite source-qualified oracle over the production module_logic circuit.

The independent fixtures specify biological roles, source tiers and expected cases.
They do not generate the module topology. Synthetic records are fault-injection
controls only, not purported gene annotations or newly inferred real proteins.
"""
from copy import deepcopy
from dataclasses import asdict
import hashlib
import json
from pathlib import Path

import yaml

from ai_gene_review.module_logic import compile_node, core_atoms, enumerate_routes, is_satisfied, iter_atoms

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
MODULE = ROOT / 'modules/bacterial_mcl_pha_synthesis_and_mobilization.yaml'
SUPPORTED_TIERS = {'target_role_with_comparative_chemistry',
                   'close_strain_chemistry_with_native_support', 'target_genetic_role'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def walk(node):
    yield node
    for part in node.get('parts', []):
        yield from walk(part['node'])
    for variants in node.get('variant_sets', []):
        for variant in variants['variants']:
            yield from walk(variant)


def find(node, ident):
    return next(n for n in walk(node) if n.get('id') == ident)


def registry(fixtures):
    members = deepcopy(fixtures['members'])
    controls = {
        'TEST_ACYL': ('Q88D25', {'role': 'unrelated_acyltransferase'}),
        'TEST_MAG': ('P26495', {'product': 'acylglycerol'}),
        'TEST_FAMILY': ('Q88D25', {'activities': []}),
        'TEST_SECRETED': ('Q88D24', {'intracellular': False}),
        'TEST_PHB': ('Q88D25', {'product': 'phb_only'}),
        'TEST_BIOH': ('O85207', {'product': 'biotin_precursor'}),
        'TEST_NO_SOURCE': ('Q88D25', {'evidence': 'family_only'}),
    }
    for key, (template, changes) in controls.items():
        members[key] = deepcopy(members[template]) | changes | {'gene': None, 'synthetic': True}
    return members


def evaluate(node, case, fixtures, disabled=frozenset()):
    members = registry(fixtures)
    roles = fixtures['role_by_atom']
    circuits = {n['id']: compile_node(n) for n in walk(node)}
    # Profile boundaries are evaluated by the actual root and subnode circuits.
    # No hard-coded requirement for a mobilizer is added outside the root: deleting
    # the module's mandatory mobilization part is therefore observable by mutation.
    def holds(atom):
        role = roles.get(atom.node_id)
        if role is None:
            return False
        for key in case['members']:
            member = members.get(key)
            if not member:
                continue
            if 'panel' not in disabled and member['panel'] != case['panel']:
                continue
            if 'family' not in disabled and atom.family_ids and member['family'] not in atom.family_ids:
                continue
            if 'activity' not in disabled and not set(atom.function_ids).issubset(member['activities']):
                continue
            if 'domain' not in disabled and not set(atom.domain_ids).issubset(member['domains']):
                continue
            if 'role' not in disabled and member['role'] != role:
                continue
            if 'source' not in disabled and member['evidence'] not in SUPPORTED_TIERS:
                continue
            if case.get('evidence_policy') == 'purified_target' and not member.get('purified_target_forward', False):
                # None of these finite fixtures asserts purified forward native
                # target kinetics for every required role. This is NOT inactivity.
                continue
            expected = 'mcl_hydroxyacyl_coa' if role == 'monomer_routing' else 'mcl_storage_polymer'
            if 'product' not in disabled and member['product'] != expected:
                continue
            if role == 'polymerization' and not case.get('compatible_polymer', True):
                continue
            if role == 'mobilization' and 'access' not in disabled:
                if not member['intracellular'] or not case.get('intracellular_access', True):
                    continue
            return True
        return False

    root = compile_node(node)
    synth = circuits.get('mcl_pha_polymerization')
    supply = circuits.get('pha_monomer_supply_from_fas')
    supply_ok = bool(supply and is_satisfied(supply, holds))
    input_kind = case.get('input', 'external_mcl_coa')
    input_ok = input_kind == 'external_mcl_coa' or (input_kind == 'fas' and supply_ok)
    # The root compiler does not encode chemical input-pool availability.
    return {
        'combined': is_satisfied(root, holds) and input_ok,
        'synthesis': bool(synth and is_satisfied(synth, holds)) and input_ok,
        'supply': supply_ok,
        'comonomer_incorporation': any(members.get(k, {}).get('observed_mcl_comonomer', False)
                                      for k in case['members']),
        'raw_circuit': is_satisfied(root, holds),
        'atom_truth': {a.node_id: holds(a) for a in iter_atoms(root)},
    }


def run_cases(node, fixtures):
    output = []
    for case in fixtures['cases']:
        result = evaluate(node, case, fixtures)
        errors = {k: {'expected': case[k], 'actual': result[k]}
                  for k in ['combined', 'synthesis', 'supply', 'comonomer_incorporation']
                  if k in case and case[k] != result[k]}
        output.append({'id': case['id'], 'result': result, 'errors': errors})
    return output


def mutation_checks(node, fixtures):
    mutations = {}
    n = deepcopy(node)
    n['parts'] = [p for p in n['parts'] if p['node']['id'] != 'mcl_pha_depolymerization']
    mutations['omit_required_mobilization'] = n
    n = deepcopy(node)
    n['parts'] = [p for p in n['parts'] if p['node']['id'] != 'mcl_pha_polymerization']
    mutations['omit_required_synthesis'] = n
    n = deepcopy(node)
    next(p for p in n['parts'] if p['node']['id'] == 'pha_monomer_supply_from_fas')['optional'] = False
    mutations['make_phag_universally_required'] = n
    n = deepcopy(node)
    a = find(n, 'mcl_pha_polymerization')['annotons'][0]
    a['participant']['family']['term']['id'] = 'PANTHER:PTHR43194'
    mutations['wrong_synthase_family'] = n
    n = deepcopy(node)
    z = find(n, 'mcl_pha_depolymerization')
    variants = z.pop('variant_sets')[0]['variants']
    z['parts'] = [{'node': variant} for variant in variants]
    mutations['require_both_phaz_lineages'] = n
    n = deepcopy(node)
    find(n, 'mcl_phaz_gpo1')['annotons'][0]['function']['term']['id'] = 'GO:0050527'
    mutations['force_precise_oligomer_claim_on_gpo1'] = n
    n = deepcopy(node)
    find(n, 'mcl_pha_depolymerization')['variant_sets'][0]['selection'] = 'ZERO_OR_MORE'
    mutations['make_mobilization_optional'] = n
    results = {}
    for name, changed in mutations.items():
        failures = [r['id'] for r in run_cases(changed, fixtures) if r['errors']]
        assert failures, f'Undetected mutation: {name}'
        results[name] = {'caught_by_cases': failures}
    return results


def sensitivity_checks(node, fixtures):
    cases = {c['id']: c for c in fixtures['cases']}
    probes = [
        ('role', 'generic_acyl_false_positive'),
        ('product', 'generic_mag_false_positive'),
        ('activity', 'family_only_false_positive'),
        ('access', 'secreted_phaz_false_positive'),
        ('panel', 'unverified_mixed_panel'),
    ]
    out = {}
    for gate, case_id in probes:
        before = evaluate(node, cases[case_id], fixtures)['combined']
        after = evaluate(node, cases[case_id], fixtures, {gate})['combined']
        assert before is False and after is True, (gate, before, after)
        out[gate] = {'case': case_id, 'normal': before, 'gate_disabled': after}
    case = {'id': 'no_source', 'panel': 'KT2440', 'members': ['TEST_NO_SOURCE', 'Q88D24']}
    assert not evaluate(node, case, fixtures)['combined']
    assert evaluate(node, case, fixtures, {'source'})['combined']
    out['source'] = {'case': 'no_source', 'normal': False, 'gate_disabled': True}
    # A synthetic non-class-II synthase with the same positive storage-polymer
    # evidence is admitted without IPR011287. This tests lack of a hidden class
    # gate; it is not a new claim about H16 or any real protein.
    revised = deepcopy(fixtures)
    revised['members']['Q88D25']['domains'] = ['InterPro:IPR010963']
    positive = {'panel': 'KT2440', 'members': ['Q88D25', 'Q88D24']}
    assert evaluate(node, positive, revised)['combined']
    out['class_independence'] = {'synthetic_class_i_domain_with_positive_mcl_product': True,
                                 'biological_assertion_about_H16': False}
    return out


def review_alignment(fixtures):
    result = {}
    for accession, member in fixtures['members'].items():
        org, gene = member['gene'].split('/')
        path = ROOT / f'genes/{org}/{gene}/{gene}-ai-review.yaml'
        if not path.exists() or yaml.safe_load(path.read_text()).get('status') != 'COMPLETE':
            result[accession] = {'state': 'PENDING_REVIEW', 'path': str(path.relative_to(ROOT))}
            continue
        review = yaml.safe_load(path.read_text())
        assert review['id'] == accession
        core = {c.get('molecular_function', {}).get('id') for c in review.get('core_functions', [])}
        assert set(member['activities']).issubset(core), (accession, core)
        result[accession] = {'state': 'ALIGNED', 'core_terms': sorted(x for x in core if x),
                             'review_sha256': sha(path)}
    return result


def main():
    doc = yaml.safe_load(MODULE.read_text())
    fixtures = yaml.safe_load((HERE / 'fixtures.yaml').read_text())
    node = doc['module']
    results = run_cases(node, fixtures)
    assert not [r for r in results if r['errors']], results
    circuit = compile_node(node)
    out = {'module_sha256': sha(MODULE), 'fixtures_sha256': sha(HERE / 'fixtures.yaml'),
           'compiler_sha256': sha(ROOT / 'src/ai_gene_review/module_logic.py'),
           'status': 'PASS', 'case_count': len(results), 'cases': results,
           'mutations': mutation_checks(node, fixtures),
           'gate_sensitivity': sensitivity_checks(node, fixtures),
           'compiled_atoms': [asdict(a) for a in iter_atoms(circuit)],
           'core_atoms': [a.node_id for a in core_atoms(circuit)],
           'routes': [[a.node_id for a in r] for r in enumerate_routes(circuit)],
           'review_alignment': review_alignment(fixtures),
           'limits': 'Finite evidence oracle, not assay-independent validation or genome discovery. Compiler handles AND/OR only; substrate, access, evidence and matching-panel gates are external. ONE_OR_MORE variants are existential, not flux or stoichiometry. Unknown capacity is not biological impossibility.'}
    serialized = json.dumps(out, indent=2, sort_keys=True) + '\n'
    # Reevaluate the independent cases to detect accidental state dependence.
    assert run_cases(node, fixtures) == results
    (HERE / 'capacity-results.json').write_text(serialized)
    print(json.dumps({'status': out['status'], 'cases': len(results), 'mutations': len(out['mutations']),
                      'gate_checks': len(out['gate_sensitivity']), 'module_sha256': out['module_sha256']}))


if __name__ == '__main__':
    main()
