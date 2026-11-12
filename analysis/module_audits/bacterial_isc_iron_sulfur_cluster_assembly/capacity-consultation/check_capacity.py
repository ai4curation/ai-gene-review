"""Evaluate a source-grounded finite-panel oracle through production module_logic."""
import argparse
from collections import Counter
from copy import deepcopy
from dataclasses import asdict
import hashlib
from pathlib import Path

import yaml

from ai_gene_review.module_logic import (
    compile_module, core_atoms, enumerate_routes, is_satisfied, iter_atoms,
)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
MODULE = ROOT / 'modules/bacterial_isc_iron_sulfur_cluster_assembly.yaml'
ATOM_ROLES = {
    'iscs_cysteine_desulfurase': 'iscS', 'iscu_cluster_scaffold': 'iscU',
    'isc_ferredoxin': 'fdx', 'hscb_cochaperone': 'hscB',
    'hsca_chaperone_atpase': 'hscA', 'hsca_chaperone_atpase_family_level': 'hscA',
    'isca_cluster_carrier': 'iscA',
}
REQUIRED_ROLES = {'iscS', 'iscU', 'fdx', 'hscB', 'hscA'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Oracle:
    """Gates use curated source assertions; review actions are never counted as assays."""

    def __init__(self, ledger, organism, members, profile='supported_or_inferred',
                 blocked_edges=(), context='canonical', disabled_gates=()):
        self.ledger = ledger
        self.organism = organism
        self.members = members
        self.allowed = set(ledger['profiles'][profile])
        self.blocked_edges = set(blocked_edges)
        self.context = context
        self.disabled = set(disabled_gates)
        first = next(iter(ledger['panels'][organism].values()))
        self.taxon = ledger['members'][first]['taxon']

    def reasons(self, atom, candidate):
        role = ATOM_ROLES[atom.node_id]
        reasons = []
        accession = candidate.get('accession')
        source = self.ledger['members'].get(accession)
        if 'identity' not in self.disabled and (
                source is None or accession not in atom.uniprots):
            reasons.append('no_reviewed_representative_identity')
        if 'taxon' not in self.disabled and candidate.get('taxon') != self.taxon:
            reasons.append('different_taxon')
        if 'family' not in self.disabled and not (
                set(candidate.get('family_ids', [])) & set(atom.family_ids)):
            reasons.append('classification_mismatch')
        if 'function' not in self.disabled and not set(atom.function_ids).issubset(
                candidate.get('functions', [])):
            reasons.append('required_activity_not_supported')
        if 'role' not in self.disabled and (
                source is None or source['role'] != role
                or not candidate.get('specific_role_evidence')
                or not candidate.get('specific_signature_verified')):
            reasons.append('no_specific_isc_role_evidence')
        if 'tier' not in self.disabled and (
                source is None or source['role_tier'] not in self.allowed):
            reasons.append('role_evidence_below_profile')
        if 'interfaces' not in self.disabled:
            # Optional carrier does not create an unmodeled obligatory IscU->IscA edge.
            needed = {'iscS': ['sulfur_handoff'], 'iscU': ['sulfur_handoff', 'assisted_transfer'],
                      'fdx': ['ferredoxin_donor'], 'hscA': ['assisted_transfer'],
                      'hscB': ['assisted_transfer'], 'iscA': []}[role]
            present = {c.get('accession') for c in self.members}
            for edge in needed:
                matches = [e for e in self.ledger['interfaces']
                           if e['organism'] == self.organism and e['edge'] == edge
                           and accession in e['members'] and set(e['members']) <= present
                           and e['tier'] in self.allowed and edge not in self.blocked_edges]
                if not matches:
                    reasons.append('unestablished_cognate_interface:' + edge)
        return reasons

    def __call__(self, atom):
        return any(not self.reasons(atom, c) for c in self.members)

    def evaluate(self, circuit):
        atoms = list(iter_atoms(circuit))
        values = {a.node_id: self(a) for a in atoms}
        satisfies = is_satisfied(circuit, lambda a: values[a.node_id])
        if self.context != 'canonical':
            classification = 'OUTSIDE_CANONICAL_PROFILE'
        else:
            classification = 'PROFILE_SUPPORTED' if satisfies else 'PROFILE_NOT_ESTABLISHED'
        roles = {role: any(values[a.node_id] for a in atoms if ATOM_ROLES[a.node_id] == role)
                 for role in set(ATOM_ROLES.values())}
        return {'classification': classification, 'compiler_satisfied': satisfies,
                'roles': dict(sorted(roles.items())), 'atoms': values,
                'optional_carrier_supported': roles['iscA'],
                'missing_required_roles': sorted(REQUIRED_ROLES - {r for r, v in roles.items() if v}),
                'rejections': {a.node_id: {str(c.get('accession')): self.reasons(a, c)
                                          for c in self.members
                                          if c.get('role') in [None, ATOM_ROLES[a.node_id]]}
                               for a in atoms if not values[a.node_id]}}


def candidates(ledger, organism, omit=()):
    result = []
    for role, accession in ledger['panels'][organism].items():
        if role in omit:
            continue
        m = ledger['members'][accession]
        result.append({'accession': accession, 'role': role, 'taxon': m['taxon'],
                       'functions': list(m['core_functions']), 'family_ids': list(m['family_ids']),
                       'specific_role_evidence': m['role_tier'] != 'ROLE_UNRESOLVED',
                       'specific_signature_verified': True})
    return result


def source_check(ledger):
    for path, digest in ledger['source_sha256'].items():
        assert sha(ROOT / path) == digest, f'Consulted source changed: {path}'
    for edge in ledger['interfaces']:
        for ref in edge['sources']:
            detail = ledger['interface_evidence'][ref]
            assert detail['source_path'] in ledger['source_sha256'], (edge['edge'], ref)
            text = ' '.join((ROOT / detail['source_path']).read_text().split())
            for quote in detail['supporting_quotes']:
                assert ' '.join(quote.split()) in text, (ref, quote)
    source_edges = {e['edge']: e for e in ledger['interfaces'] if e['organism'] == 'ECOLI'}
    for edge in ledger['interfaces']:
        if edge['organism'] == 'PSEPK':
            assert edge['sources'] == source_edges[edge['edge']]['sources'], edge
            assert edge['mechanism_source_panel'] == 'ECOLI', edge
            assert edge['tier'] == 'QUALIFIED_INFERENCE', edge
        if edge['organism'] == 'AZOVI' and edge['edge'] == 'ferredoxin_donor':
            assert edge['mechanism_source_panel'] == 'ECOLI', edge
            assert 'PMID:16964969' not in edge['sources'], edge
            assert edge['tier'] == 'QUALIFIED_INFERENCE', edge
    for accession, m in ledger['members'].items():
        review = yaml.safe_load((ROOT / m['review_path']).read_text())
        assert review['id'] == accession and review['taxon']['id'] == m['taxon']
        text = (ROOT / m['raw_path']).read_text()
        assert m['specific_signature'] in text
        assert set(m['core_functions']) == {
            c['molecular_function']['id'] for c in review['core_functions']
            if c.get('molecular_function')}
    return len(ledger['source_sha256'])


def run():
    ledger = yaml.safe_load((HERE / 'evidence-ledger.yaml').read_text())
    checked = source_check(ledger)
    doc = yaml.safe_load(MODULE.read_text())
    circuit = compile_module(doc)
    atoms = list(iter_atoms(circuit))
    assert {a.node_id for a in atoms} == set(ATOM_ROLES)
    for a in atoms:
        expected_functions = {m['required_function'] for m in ledger['members'].values()
                              if m['role'] == ATOM_ROLES[a.node_id]}
        assert set(a.function_ids) == expected_functions, a.node_id
    routes = enumerate_routes(circuit)
    assert len(routes) == 4
    assert all(Counter(ATOM_ROLES[a.node_id] for a in route)['hscA'] == 1 for route in routes)
    assert {ATOM_ROLES[a.node_id] for a in core_atoms(circuit)} == REQUIRED_ROLES - {'hscA'}
    tests = []

    def check(name, organism, selected, expected, profile='supported_or_inferred',
              optional=None, context='canonical', blocked_edges=(), expected_missing=None):
        oracle = Oracle(ledger, organism, selected, profile, blocked_edges, context)
        out = oracle.evaluate(circuit)
        assert out['compiler_satisfied'] == expected, (name, out)
        if optional is not None:
            assert out['optional_carrier_supported'] == optional, name
        if context != 'canonical':
            assert out['classification'] == 'OUTSIDE_CANONICAL_PROFILE', name
        if expected_missing:
            assert set(expected_missing) <= set(out['missing_required_roles']), name
        tests.append({'name': name, 'profile': profile, 'context': context,
                      'fixture_interpretation': ('Evidence/descriptor sensitivity, not a native knockout '
                                                 'prediction or measured biological negative.'),
                      'expected_compiler_satisfied': expected, **out})
        return oracle

    for org in ledger['panels']:
        panel = candidates(ledger, org)
        check(org + '_qualified_panel', org, panel, True, optional=org != 'AZOVI')
        check(org + '_assay_only', org, panel, org == 'ECOLI', profile='assay_only',
              optional=org == 'ECOLI')
        check(org + '_omit_optional_IscA', org, candidates(ledger, org, ['iscA']), True,
              optional=False)
        for role in sorted(REQUIRED_ROLES):
            check(org + '_remove_' + role, org, candidates(ledger, org, [role]), False,
                  expected_missing=[role])
    # Exact same species is necessary, but does not substitute for interface evidence.
    mixed = candidates(ledger, 'ECOLI', ['hscA']) + [c for c in candidates(ledger, 'AZOVI')
                                                  if c['role'] == 'hscA']
    check('mixed_species_components', 'ECOLI', mixed, False, expected_missing=['hscA'])
    check('same_species_missing_transfer_interface', 'ECOLI', candidates(ledger, 'ECOLI'),
          False, blocked_edges=['assisted_transfer'], expected_missing=['hscA', 'hscB'])
    check('same_species_missing_donor_interface', 'ECOLI', candidates(ledger, 'ECOLI'),
          False, blocked_edges=['ferredoxin_donor'], expected_missing=['fdx'])
    only_redox = [c for c in candidates(ledger, 'AZOVI') if c['role'] == 'fdx']
    check('isolated_characterized_redox_protein', 'AZOVI', only_redox, False)
    family_only = candidates(ledger, 'ECOLI')
    for c in family_only:
        c['specific_role_evidence'] = False
    check('family_and_activity_without_specific_role_evidence', 'ECOLI', family_only, False)
    missing_function = candidates(ledger, 'ECOLI')
    next(c for c in missing_function if c['role'] == 'iscU')['functions'] = ['GO:0051536']
    check('IscU_binding_without_delivery', 'ECOLI', missing_function, False,
          expected_missing=['iscU'])
    optional_binding = candidates(ledger, 'ECOLI')
    next(c for c in optional_binding if c['role'] == 'iscA')['functions'] = ['GO:0051536']
    check('optional_carrier_binding_is_insufficient', 'ECOLI', optional_binding, True, optional=False)
    missing_signature = candidates(ledger, 'ECOLI')
    next(c for c in missing_signature if c['role'] == 'fdx')['specific_signature_verified'] = False
    check('ferredoxin_role_without_specific_signature', 'ECOLI', missing_signature, False,
          expected_missing=['fdx'])
    controls = [
        ('arbitrary_DnaK_Hsp70', 'hscA', {'accession': 'Q88DU2', 'taxon': 'NCBITaxon:160488',
                                        'functions': ['GO:0016887'],
                                        'family_ids': ['PANTHER:PTHR19375']}),
        ('generic_ferredoxin_descriptor', 'fdx', {'accession': None,
                                                'taxon': 'NCBITaxon:160488',
                                                'functions': ['GO:0009055'],
                                                'family_ids': ['PANTHER:PTHR23426:SF65']}),
        ('SufU_broad_family_ambiguity', 'iscU', {'accession': 'O32163',
                                               'taxon': 'NCBITaxon:224308',
                                               'functions': ['GO:0051536'],
                                               'family_ids': ['PANTHER:PTHR10093']}),
    ]
    for name, role, control in controls:
        check(name, 'PSEPK', candidates(ledger, 'PSEPK', [role]) + [control], False,
              expected_missing=[role])
    check('AZOVI_IscA_is_not_cluster_delivery_witness', 'AZOVI',
          [c for c in candidates(ledger, 'AZOVI') if c['role'] == 'iscA'], False, optional=False)
    check('anaerobic_Fdx_bypass_context', 'ECOLI', candidates(ledger, 'ECOLI', ['fdx']), False,
          context='anaerobic_alternative_reductant', expected_missing=['fdx'])
    check('IscU_suppressor_HscBA_bypass_context', 'ECOLI',
          candidates(ledger, 'ECOLI', ['hscA', 'hscB']), False,
          context='scaffold_suppressor_alternative', expected_missing=['hscA', 'hscB'])
    # Sensitivity: each nontrivial evidence gate must reject even a recognized member
    # when the corresponding evidence is withheld. Disabling that gate restores the fixture.
    sensitivities = []
    for gate in ['taxon', 'family', 'function', 'role', 'interfaces']:
        panel = candidates(ledger, 'ECOLI')
        candidate = next(c for c in panel if c['role'] == 'hscA')
        blocked = []
        if gate == 'taxon':
            candidate['taxon'] = 'NCBITaxon:160488'
        elif gate == 'family':
            candidate['family_ids'] = []
        elif gate == 'function':
            candidate['functions'] = []
        elif gate == 'role':
            candidate['specific_role_evidence'] = False
        else:
            blocked = ['assisted_transfer']
        strict = Oracle(ledger, 'ECOLI', panel, blocked_edges=blocked).evaluate(circuit)
        ablated = Oracle(ledger, 'ECOLI', panel, blocked_edges=blocked,
                         disabled_gates=[gate]).evaluate(circuit)
        assert not strict['compiler_satisfied'] and ablated['compiler_satisfied'], gate
        sensitivities.append({'gate': gate, 'strict': False, 'gate_ablated': True,
                              'meaning': 'Synthetic evidence withdrawal, not a biological loss assertion.'})
    # The role and interface tiers independently protect the Azotobacter donor-edge limit.
    az = candidates(ledger, 'AZOVI')
    for disabled in [['tier'], ['interfaces']]:
        assert not Oracle(ledger, 'AZOVI', az, 'assay_only',
                          disabled_gates=disabled).evaluate(circuit)['compiler_satisfied']
    assert Oracle(ledger, 'AZOVI', az, 'assay_only',
                  disabled_gates=['tier', 'interfaces']).evaluate(circuit)['compiler_satisfied']
    sensitivities.append({'gate': 'AZOVI_donor_role_and_interface_tiers',
                          'either_gate_alone_retained': False, 'both_gates_ablated': True})
    # Model-structure mutants: prove tests detect accidental mandatory accessory/AND HscA.
    mutated = deepcopy(doc)
    next(p for p in mutated['module']['parts'] if p['node']['id'] == 'isca_cluster_transfer')[
        'optional'] = False
    assert not Oracle(ledger, 'AZOVI', az).evaluate(compile_module(mutated))['compiler_satisfied']
    mutated = deepcopy(doc)
    hsca = next(p['node'] for p in mutated['module']['parts']
                if p['node']['id'] == 'hsca_atp_remodeling')
    vs = hsca.pop('variant_sets')[0]
    hsca['parts'] = [{'node': v} for v in vs['variants']]
    assert all(not Oracle(ledger, org, candidates(ledger, org)).evaluate(
        compile_module(mutated))['compiler_satisfied'] for org in ledger['panels'])
    result = {
        'status': 'PASS', 'module_sha256': sha(MODULE), 'production_engine_sha256': sha(
            ROOT / 'src/ai_gene_review/module_logic.py'), 'protected_sources_checked': checked,
        'test_count': len(tests), 'sensitivity_count': len(sensitivities),
        'compiler_atoms': [asdict(a) for a in atoms],
        'routes': [[a.node_id for a in r] for r in routes],
        'mutation_checks': ['IscA made required breaks AZOVI',
                            'HscA classification alternatives changed to AND break all panels'],
        'sensitivities': sensitivities, 'tests': tests,
        'limits': ['Finite curated representatives; not a genome-wide predictor.',
                   'Assay-only means separately assayed roles/interfaces, not simultaneous whole-pathway flux.',
                   'Profile failure is insufficient evidence for this canonical route, not native biological inactivity.',
                   'Taxon and compatibility are oracle gates, not features enforced by module_logic.'],
    }
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=HERE / 'capacity-results.yaml')
    args = parser.parse_args()
    result = run()
    args.output.write_text(yaml.safe_dump(result, sort_keys=False, width=100))
    print({key: result[key] for key in ['status', 'test_count', 'sensitivity_count',
                                      'protected_sources_checked']})


if __name__ == '__main__':
    main()
