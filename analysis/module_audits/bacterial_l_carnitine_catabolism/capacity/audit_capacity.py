"""Source-qualified capacity checks over the production module boolean compiler.

The independent fixture records chemistry and evidence, never annotation-action counts.
Original module descriptors supply selectors, complexes and reaction substrates/products;
module_logic supplies AND/OR/optional-part semantics. Neither substitutes for the other.
"""
import argparse
from collections import Counter
from copy import deepcopy
from dataclasses import asdict
from hashlib import sha256
from pathlib import Path
import re

import yaml

from ai_gene_review.module_logic import compile_module, enumerate_routes, is_satisfied, iter_atoms

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
MODULE = ROOT / 'modules/bacterial_l_carnitine_catabolism.yaml'
FIXTURE = ROOT / 'modules/bacterial_l_carnitine_catabolism-source-analysis/evidence-fixture.yaml'
RELEASE_UPDATE = ROOT / 'analysis/module_audits/bacterial_l_carnitine_catabolism/pseae-consultation/cdhb-consistency-followup/handoff-update.json'
FAMILIES = ['PTHR48075', 'PTHR37418', 'PTHR31793', 'PTHR43869', 'PTHR47737']
ALIASES = {'N,N,N-trimethylglycyl-CoA (betainyl-CoA)': 'betainyl-CoA',
           'L-carnitine (outside)': 'L-carnitine outside', 'L-carnitine (inside)': 'L-carnitine inside'}


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def norm(text):
    return ' '.join(re.sub(r'(?m)^CC\s+', '', text).split())


def walk(node):
    yield node
    for part in node.get('parts', []):
        yield from walk(part['node'])
    for variant_set in node.get('variant_sets', []):
        for variant in variant_set.get('variants', []):
            yield from walk(variant)


def annotons(doc):
    result = {}
    for node in walk(doc['module']):
        for annoton in node.get('annotons', []):
            assert annoton['id'] not in result, 'duplicate annoton ID'
            result[annoton['id']] = annoton
    return result


def chemistry(function):
    return tuple(tuple(sorted(ALIASES.get(x['preferred_term'], x['preferred_term'])
                              for x in function.get(side, []))) for side in ['substrates', 'products'])


def reaction_role(annoton, fixture):
    found = [role for role, reaction in fixture['reactions'].items()
             if chemistry(annoton.get('function', {})) == tuple(tuple(sorted(reaction[side]))
                                                               for side in ['substrates', 'products'])]
    return found[0] if len(found) == 1 else None


def selector_errors(selector, candidate, disabled=()):
    kind = selector.get('selector_type')
    if kind == 'FAMILY':
        family = selector.get('family', {})
        ids = {x['id'] for x in [family.get('term'), *family.get('family_terms', [])] if x}
        if 'family' not in disabled and (not ids or not ids.intersection(candidate['families'])):
            return ['family_selector_not_supported']
    elif kind == 'ORTHOLOG_OF':
        exemplar = selector.get('ortholog_of', {}).get('term', {}).get('id', '').removeprefix('UniProtKB:')
        if 'orthology' not in disabled and exemplar not in candidate.get('orthologs_of', []):
            return ['ortholog_identity_not_established']
    else:
        return ['unsupported_selector:' + str(kind)]
    return []


class Oracle:
    def __init__(self, doc, fixture, panel, candidates, profile='qualified', disabled=(), blocked_assembly=False):
        self.doc = doc
        self.fixture = fixture
        self.panel = panel
        self.candidates = candidates
        self.profile = profile
        self.allowed = fixture['profiles'][profile]
        self.disabled = disabled
        self.blocked_assembly = blocked_assembly
        self.lookup = annotons(doc)
        self.taxon = fixture['panels'][panel]['taxon']

    def candidate_errors(self, candidate, role, selector):
        errors = []
        if candidate['accession'] not in self.fixture['members']:
            errors.append('no_member_specific_source_evidence')
        if 'taxon' not in self.disabled and candidate.get('taxon') != self.taxon:
            errors.append('outside_selected_strain_panel')
        errors.extend(selector_errors(selector, candidate, self.disabled))
        claim = candidate.get('roles', {}).get(role)
        if claim is None and 'exact_chemistry' not in self.disabled:
            errors.append('exact_role_or_substrate_not_established')
        elif claim and 'tier' not in self.disabled and claim['tier'] not in self.allowed:
            errors.append('evidence_below_selected_profile')
        if role in self.fixture['reactions'] and role != 'import':
            go = self.fixture['reactions'][role]['go']
            if go not in candidate.get('functions', []):
                errors.append('corresponding_MF_not_supported')
        return errors

    def import_result(self, annoton):
        selector = annoton.get('participant', {})
        if selector.get('selector_type') != 'PROTEIN_COMPLEX':
            return {'holds': False, 'reason': 'import_requires_compatible_complex', 'witnesses': []}
        units = selector.get('protein_complex', {}).get('active_units', [])
        wanted = set(self.fixture['reactions']['import']['required_unit_roles'])
        assignments = []
        for unit in units:
            eligible = [(c['accession'], role) for role in wanted for c in self.candidates
                        if not self.candidate_errors(c, role, unit.get('participant', {}))]
            assignments.append(eligible)
        # A recognized assembly supplies all independently required roles, once each.
        # Gene copy number is not equated to protein stoichiometry.
        for assembly in self.fixture['assemblies']:
            if assembly['panel'] != self.panel or self.blocked_assembly:
                continue
            if 'interfaces' not in self.disabled and assembly['tier'] not in self.allowed:
                continue
            available = {c['accession'] for c in self.candidates}
            if not set(assembly['members']) <= available:
                continue
            from itertools import product
            for combination in product(*assignments):
                if (len(combination) == len(wanted)
                        and {r for _, r in combination} == wanted
                        and {a for a, _ in combination} == set(assembly['members'])):
                    return {'holds': True, 'witnesses': list(combination), 'assembly_tier': assembly['tier']}
        return {'holds': False, 'reason': 'missing_recognition_core_or_cognate_assembly_evidence',
                'unit_candidates': assignments, 'witnesses': []}

    def atom_result(self, atom):
        annoton = self.lookup[atom.node_id]
        role = reaction_role(annoton, self.fixture)
        if role is None:
            return {'holds': False, 'reason': 'unrecognized_exact_chemistry', 'witnesses': []}
        expected_go = self.fixture['reactions'][role]['go']
        if set(atom.function_ids) != {expected_go}:
            return {'holds': False, 'reason': 'MF_descriptor_inconsistent_with_exact_reaction', 'witnesses': []}
        if role == 'import':
            return {'role': role, **self.import_result(annoton)}
        rejections = {c['accession']: self.candidate_errors(c, role, annoton['participant'])
                      for c in self.candidates}
        witnesses = [acc for acc, errors in rejections.items() if not errors]
        return {'role': role, 'holds': bool(witnesses), 'witnesses': witnesses,
                'rejections': rejections if not witnesses else {}}

    def evaluate(self):
        circuit = compile_module(self.doc)
        atom_values = {a.node_id: self.atom_result(a) for a in iter_atoms(circuit)}
        def holds(atom):
            return atom_values[atom.node_id]['holds']

        chemical = is_satisfied(circuit, holds)
        role_values = {role: any(v.get('role') == role and v['holds'] for v in atom_values.values())
                       for role in self.fixture['reactions']}
        return {'compiler_satisfied': chemical,
                'uptake_supported': role_values['import'],
                'uptake_plus_catabolism': chemical and role_values['import'],
                'missing_required_reactions': [r for r in self.fixture['required_reactions'] if not role_values[r]],
                'role_values': role_values, 'atoms': atom_values}


def validate_fixture(fixture):
    """Require an explicit, resolvable provenance chain for every positive claim."""
    source_ids = set(fixture['sources'])
    allowed_tiers = set().union(*(set(v) for v in fixture['profiles'].values()))
    for role, reaction in fixture['reactions'].items():
        assert reaction['sources'] and set(reaction['sources']) <= source_ids, role
    for accession, member in fixture['members'].items():
        assert accession == member['accession']
        for role, claim in member['roles'].items():
            assert claim['sources'] and set(claim['sources']) <= source_ids, (accession, role)
            assert claim['tier'] in allowed_tiers and claim['scope'], (accession, role)
    for assembly in fixture['assemblies']:
        assert set(assembly['members']) <= set(fixture['members'])
        assert assembly['tier'] in allowed_tiers
        assert assembly['sources'] and set(assembly['sources']) <= source_ids


def load_candidates(fixture):
    result = {}
    for acc, member in fixture['members'].items():
        review = yaml.safe_load((ROOT / member['review_path']).read_text())
        raw = (ROOT / member['raw_path']).read_text()
        assert review['id'] == acc and re.search(r'^AC\s+' + re.escape(acc) + ';', raw, re.M)
        families = ['PANTHER:' + x for x in re.findall(r'^DR   PANTHER; ([^;]+);', raw, re.M)]
        functions = {c[slot]['id'] for c in review.get('core_functions', [])
                     for slot in ['molecular_function', 'contributes_to_molecular_function'] if c.get(slot)}
        for role in member['roles']:
            if role in fixture['required_reactions']:
                assert fixture['reactions'][role]['go'] in functions, (acc, role, 'review/core disagrees with fixture')
        result[acc] = {**deepcopy(member), 'taxon': review['taxon']['id'],
                       'families': families, 'functions': sorted(functions)}
    return result


def model_contract(doc, fixture):
    """Independent chemical pathway constraints, not a list copied from module IDs."""
    errors = []
    lookup = annotons(doc)
    role_map = {key: reaction_role(a, fixture) for key, a in lookup.items()}
    for key, role in role_map.items():
        if role in fixture['required_reactions']:
            sources = {x.get('source_id') for x in lookup[key].get('function', {}).get('evidence', [])}
            if fixture['reactions'][role]['rhea'] not in sources:
                errors.append('exact_reaction_provenance_missing_or_wrong')
    if None in role_map.values():
        errors.append('unknown_or_wrong_substrate_product_reaction')
    circuit = compile_module(doc)
    route_roles = []
    for route in enumerate_routes(circuit):
        roles = [role_map[a.node_id] for a in route]
        route_roles.append(roles)
        counts = Counter(roles)
        if any(counts[r] != 1 for r in fixture['required_reactions']):
            errors.append('route_omits_or_duplicates_required_chemistry')
        if any(r not in fixture['required_reactions'] + fixture['optional_reactions'] for r in roles):
            errors.append('route_contains_unestablished_chemistry')
    if not any('import' not in roles for roles in route_roles):
        errors.append('optional_import_became_universally_required')
    if not any('import' in roles for roles in route_roles):
        errors.append('optional_import_role_disappeared')
    for node in walk(doc['module']):
        for variant_set in node.get('variant_sets', []):
            branch_roles = [{reaction_role(a, fixture) for n in walk(v) for a in n.get('annotons', [])}
                            for v in variant_set.get('variants', [])]
            if branch_roles and all(roles == {'hydrolysis'} for roles in branch_roles):
                if variant_set.get('variant_kind') != 'REALIZER' or variant_set.get('selection') != 'ONE_OR_MORE':
                    errors.append('hydrolase_architectures_not_required_realizer_alternatives')
    node_roles = {n['id']: {reaction_role(a, fixture) for x in walk(n) for a in x.get('annotons', [])}
                  for n in walk(doc['module'])}
    edges = {(a, b) for edge in doc['module'].get('connections', [])
             if edge.get('connection_type') == 'PROVIDES_INPUT_FOR'
             for a in node_roles.get(edge['source'], set()) for b in node_roles.get(edge['target'], set())}
    expected = {('import', 'oxidation'), ('oxidation', 'cleavage'), ('cleavage', 'hydrolysis')}
    if edges != expected:
        errors.append('reaction_handoff_graph_mismatch')
    return sorted(set(errors))


def resolve_source(value):
    if value.startswith('PMID:') and value[5:].isdigit():
        path = ROOT / f'publications/PMID_{value[5:]}.md'
    elif value.startswith('file:'):
        path = ROOT / value[5:]
        if not path.exists():
            path = ROOT / 'genes' / value[5:]
    else:
        return None
    return path if path.is_file() else None


def reference_strings(data):
    if isinstance(data, dict):
        for value in data.values():
            yield from reference_strings(value)
    elif isinstance(data, list):
        for value in data:
            yield from reference_strings(value)
    elif isinstance(data, str) and (data.startswith('file:') or re.fullmatch(r'PMID:\d+', data)):
        yield data


def input_closure(fixture):
    seeds = {MODULE, FIXTURE, HERE / 'audit_capacity.py', HERE / 'make_fixture.py', RELEASE_UPDATE}
    update = yaml.safe_load(RELEASE_UPDATE.read_text())
    seeds.update(ROOT / path for path in update['prior_manifests_unchanged'])
    seeds.update(ROOT / path for path in update['files'])
    for source in fixture['sources'].values():
        seeds.add(ROOT / source['path'])
        content = norm((ROOT / source['path']).read_text())
        for quote in source['quotes']:
            assert norm(quote) in content, (source['path'], quote)
    for member in fixture['members'].values():
        seeds.update(ROOT / member[k] for k in ['review_path', 'raw_path'])
    for family in FAMILIES:
        seeds.add(ROOT / f'interpro/panther/{family}/{family}-review.yaml')
    for control in fixture['negative_descriptor_controls']:
        seeds.add(ROOT / control['source'])
    seeds.update(ROOT / 'src/ai_gene_review' / f for f in ['module_logic.py', 'module_gene_symbols.py', 'module_qc.py', 'render_modules.py'])
    seeds.update(ROOT / path for path in [
        'analysis/module_audits/bacterial_l_carnitine_catabolism/psepk-consultation/24240508-data246.xlsx',
        'analysis/module_audits/bacterial_l_carnitine_catabolism/psepk-consultation/24240508-data248.xlsx',
        'analysis/module_audits/bacterial_l_carnitine_catabolism/rhime-consultation/sequence-comparison.json',
        'analysis/module_audits/bacterial_l_carnitine_catabolism/rhime-consultation/CP004140.1-2423202-2443202.gb',
        'genes/RHIME/bcoE-bcoF/bcoE-bcoF-source-analysis/provenance.json',
    ])
    # Follow all file:/PMID: references of every consumed YAML, not only row evidence.
    queue = list(seeds)
    missing = set()
    while queue:
        path = queue.pop()
        assert path.is_file(), path
        if path.suffix not in ['.yaml', '.yml']:
            continue
        for ref in reference_strings(yaml.safe_load(path.read_text())):
            resolved = resolve_source(ref)
            if resolved is None:
                missing.add(ref)
            elif resolved not in seeds:
                seeds.add(resolved)
                queue.append(resolved)
    assert not missing, sorted(missing)
    return {str(path.relative_to(ROOT)): digest(path) for path in sorted(seeds)}


def panel_members(fixture, candidates, panel):
    return [deepcopy(candidates[acc]) for acc in fixture['panels'][panel]['members']]


def cases(fixture, candidates):
    result = []

    def add(name, panel, members, chemical, uptake=False, profile='qualified', context='defined_reaction_profile'):
        result.append({'name': name, 'panel': panel, 'candidates': members,
                       'expected': {'compiler_satisfied': chemical, 'uptake_supported': uptake,
                                    'uptake_plus_catabolism': chemical and uptake},
                       'profile': profile, 'context': context})

    for panel in fixture['panels']:
        full = panel_members(fixture, candidates, panel)
        add(panel + '_qualified', panel, full, True, panel != 'RHIME1021')
        add(panel + '_direct_or_identical_only', panel, full, panel == 'RHIME1021', profile='direct_or_identical')
        enzymes = [c for c in full if any(r in c['roles'] for r in fixture['required_reactions'])]
        add(panel + '_without_optional_import', panel, enzymes, True)
        for role in fixture['required_reactions']:
            changed = deepcopy(full)
            for candidate in changed:
                candidate['roles'].pop(role, None)
            add(panel + '_withdraw_' + role + '_evidence', panel, changed, False, panel != 'RHIME1021')
            omitted = [c for c in full if role not in c['roles']]
            add(panel + '_omit_' + role + '_carrier', panel, omitted, False, panel != 'RHIME1021')
        family_only = deepcopy(full)
        for candidate in family_only:
            candidate['roles'] = {}
        add(panel + '_GO_and_family_only', panel, family_only, False)
        if panel != 'RHIME1021':
            for role in fixture['reactions']['import']['required_unit_roles']:
                changed = [c for c in full if role not in c['roles']]
                add(panel + '_no_' + role, panel, changed, True)
            core_only = [c for c in full if any(r in c['roles'] for r in ['ATP_coupling', 'translocation'])]
            add(panel + '_CbcWV_without_CaiX_or_enzymes', panel, core_only, False)
    add('BcoEF_alone_cannot_supply_BcoG', 'RHIME1021', [deepcopy(candidates['Q92NF5'])], False)
    add('BcoG_alone_cannot_supply_fusion_roles', 'RHIME1021', [deepcopy(candidates['Q92NF6'])], False)
    add('lone_LcdH', 'KT2440', [deepcopy(candidates['Q88R32'])], False)
    for control, role in zip(fixture['negative_descriptor_controls'], fixture['required_reactions']):
        synthetic = {'accession': 'synthetic:' + control['id'], 'taxon': fixture['panels']['KT2440']['taxon'],
                     'families': [control['family']], 'functions': [control['go']], 'roles': {}}
        panel = [c for c in panel_members(fixture, candidates, 'KT2440') if role not in c['roles']]
        add('replace_' + role + '_with_' + control['id'], 'KT2440', panel + [synthetic], False, True)
    mixed = panel_members(fixture, candidates, 'PAO1')
    mixed = [c for c in mixed if 'cleavage' not in c['roles']] + [deepcopy(candidates['Q88R31'])]
    add('mixed_strain_panel', 'PAO1', mixed, False, True, context='cognate_panel_unestablished_not_invitro_impossibility')
    add('lone_Hbd_family_descriptor', 'KT2440', [{
        'accession': 'synthetic:Hbd_like_descriptor', 'taxon': 'NCBITaxon:160488',
        'families': ['PANTHER:PTHR48075:SF5'], 'functions': ['GO:0016491'], 'roles': {},
    }], False)
    boundaries = {
        'CntAB_TMA_route': ['carnitine_oxygenolysis_to_TMA'],
        'Cai_reduction_to_GBB': ['carnitine_reduction_to_gamma_butyrobetaine'],
        'CJ25_hypothetical_Fad_route': ['proposed_FadJ_redox', 'proposed_FadI_downstream_step', 'GB_production_observed'],
    }
    for boundary, claims in boundaries.items():
        selected = [{'accession': 'boundary_evidence:' + claim, 'taxon': 'outside_selected_panel',
                     'families': [], 'functions': [],
                     'roles': {claim: {'tier': 'ALTERNATIVE_ROUTE_OR_HYPOTHESIS'}},
                     'scope': 'Source-described alternative chemistry/outcome, not an invented UniProt protein.'}
                    for claim in claims]
        add(boundary, 'KT2440', selected, False,
            context='other_route_evidence_does_not_establish_this_module')
    return result


def case_failures(doc, fixture, suite):
    failures = []
    for case in suite:
        observed = Oracle(doc, fixture, case['panel'], case['candidates'], case['profile']).evaluate()
        if any(observed[key] != value for key, value in case['expected'].items()):
            failures.append(case['name'])
    return failures


def mutations(doc, fixture):
    role_nodes = {reaction_role(a, fixture): node['id'] for node in walk(doc['module'])
                  for a in node.get('annotons', []) if reaction_role(a, fixture) in ['oxidation', 'cleavage']}
    hydro_parent = next(n for n in walk(doc['module']) if n.get('variant_sets'))['id']
    role_nodes['hydrolysis'] = hydro_parent
    output = []
    for role, node_id in role_nodes.items():
        changed = deepcopy(doc)
        changed['module']['parts'] = [p for p in changed['module']['parts'] if p['node']['id'] != node_id]
        output.append(('omit_mandatory_' + role, changed))
        changed = deepcopy(doc)
        next(p for p in changed['module']['parts'] if p['node']['id'] == node_id)['optional'] = True
        output.append(('make_mandatory_' + role + '_optional', changed))
    changed = deepcopy(doc)
    a = next(a for a in annotons(changed).values() if reaction_role(a, fixture) == 'oxidation')
    a['participant']['family']['term']['id'] = 'PANTHER:PTHR37418:SF2'
    output.append(('wrong_dehydrogenase_family', changed))
    changed = deepcopy(doc)
    a = next(a for a in annotons(changed).values() if reaction_role(a, fixture) == 'cleavage')
    a['function']['products'][0]['preferred_term'] = 'unrelated acyl-CoA'
    output.append(('wrong_cleavage_product_despite_same_GO', changed))
    changed = deepcopy(doc)
    parent = next(n for n in walk(changed['module']) if n['id'] == hydro_parent)
    vs = parent.pop('variant_sets')[0]
    parent['parts'] = [{'node': v} for v in vs['variants']]
    output.append(('hydrolase_alternatives_wrongly_AND', changed))
    changed = deepcopy(doc)
    parent = next(n for n in walk(changed['module']) if n['id'] == hydro_parent)
    parent['variant_sets'][0]['selection'] = 'ZERO_OR_MORE'
    output.append(('optional_thioesterase_variants', changed))
    changed = deepcopy(doc)
    fused = next(a for a in annotons(changed).values() if a['participant'].get('selector_type') == 'ORTHOLOG_OF')
    fused['participant']['ortholog_of']['term']['id'] = 'UniProtKB:Q9HTH8'
    output.append(('wrong_fused_ortholog_wiring', changed))
    changed = deepcopy(doc)
    uptake = next(p for p in changed['module']['parts'] if p.get('optional'))
    uptake['optional'] = False
    output.append(('optional_import_made_required', changed))
    changed = deepcopy(doc)
    importer = next(a for a in annotons(changed).values() if reaction_role(a, fixture) == 'import')
    units = importer['participant']['protein_complex']['active_units']
    units[:] = [u for u in units if u['participant'].get('selector_type') != 'ORTHOLOG_OF']
    output.append(('importer_missing_CaiX_unit', changed))
    changed = deepcopy(doc)
    edge = changed['module']['connections'][-1]
    edge['source'], edge['target'] = edge['target'], edge['source']
    output.append(('reversed_cleavage_to_hydrolysis_edge', changed))
    return output


def verify_release_chain():
    update = yaml.safe_load(RELEASE_UPDATE.read_text())
    expected_update_paths = {f'genes/{org}/{gene}/{gene}-{suffix}'
                             for org, gene in [('PSEAE', 'cdhB'), ('PSEPK', 'PP_0301')]
                             for suffix in ['ai-review.yaml', 'ai-review.html', 'notes.md']}
    assert set(update['authorized_updates']) == expected_update_paths
    unchanged = 0
    changed = 0
    for name, expected in update['prior_manifests_unchanged'].items():
        assert digest(ROOT / name) == expected, 'Historical manifest changed: ' + name
        prior = yaml.safe_load((ROOT / name).read_text())
        files = prior.get('files_sha256', prior.get('files'))
        assert isinstance(files, dict), name
        for file, original in files.items():
            if file in update['authorized_updates']:
                authorized = update['authorized_updates'][file]
                assert original == authorized['before_sha256'], file
                assert digest(ROOT / file) == authorized['after_sha256'], file
                changed += 1
            else:
                assert digest(ROOT / file) == original, file
                unchanged += 1
    assert changed == 6
    for name, expected in update['files'].items():
        assert digest(ROOT / name) == expected, name
    return {'historical_manifest_files_unchanged': unchanged,
            'authorized_CdhB_prose_updates_verified': changed,
            'additive_receipt_path': str(RELEASE_UPDATE.relative_to(ROOT)),
            'additive_receipt_sha256': digest(RELEASE_UPDATE),
            'note': 'Source payloads/actions/core unchanged; alternate-substrate evidence is not a target-negative assay.'}


def run(capture_inputs=False):
    doc = yaml.safe_load(MODULE.read_text())
    fixture = yaml.safe_load(FIXTURE.read_text())
    validate_fixture(fixture)
    inputs = input_closure(fixture)
    input_path = HERE / 'input-hashes.yaml'
    if capture_inputs:
        input_path.write_text(yaml.safe_dump({'files_sha256': inputs}, sort_keys=False))
    else:
        assert yaml.safe_load(input_path.read_text())['files_sha256'] == inputs, 'Input closure changed; review before explicitly recapturing'
    release_chain = verify_release_chain()
    candidates = load_candidates(fixture)
    suite = cases(fixture, candidates)
    assert not model_contract(doc, fixture), model_contract(doc, fixture)
    assert not case_failures(doc, fixture, suite), case_failures(doc, fixture, suite)
    results = []
    for case in suite:
        observed = Oracle(doc, fixture, case['panel'], case['candidates'], case['profile']).evaluate()
        results.append({k: v for k, v in case.items() if k != 'candidates'} | {'observed': observed})
    mutation_results = []
    for name, mutated in mutations(doc, fixture):
        contract_errors = model_contract(mutated, fixture)
        failed_cases = case_failures(mutated, fixture, suite)
        assert contract_errors or failed_cases, 'Undetected module mutation: ' + name
        mutation_results.append({'mutation': name, 'contract_errors': contract_errors,
                                 'independent_fixture_failures': failed_cases})
    sensitivity = []
    for gate in ['family', 'taxon', 'exact_chemistry']:
        panel = panel_members(fixture, candidates, 'KT2440')
        candidate = next(c for c in panel if c['accession'] == 'Q88R31')
        if gate == 'family':
            candidate['families'] = []
        elif gate == 'taxon':
            candidate['taxon'] = 'NCBITaxon:208964'
        else:
            candidate['roles'] = {}  # broad core GO is deliberately left intact
        strict = Oracle(doc, fixture, 'KT2440', panel).evaluate()['compiler_satisfied']
        ablated = Oracle(doc, fixture, 'KT2440', panel, disabled=[gate]).evaluate()['compiler_satisfied']
        assert not strict and ablated, gate
        sensitivity.append({'gate': gate, 'strict': strict, 'gate_ablated': ablated,
                            'interpretation': 'Synthetic evidence withdrawal, not mutation or biological loss.'})
    rhime = panel_members(fixture, candidates, 'RHIME1021')
    rhime[0]['roles']['hydrolysis']['tier'] = 'QUALIFIED_INFERENCE'
    assert not Oracle(doc, fixture, 'RHIME1021', rhime, 'direct_or_identical').evaluate()['compiler_satisfied']
    assert Oracle(doc, fixture, 'RHIME1021', rhime, 'direct_or_identical', disabled=['tier']).evaluate()['compiler_satisfied']
    sensitivity.append({'gate': 'evidence_tier', 'strict': False, 'gate_ablated': True})
    panel = panel_members(fixture, candidates, 'PAO1')
    blocked = Oracle(doc, fixture, 'PAO1', panel, blocked_assembly=True).evaluate()
    assert blocked['compiler_satisfied'] and not blocked['uptake_plus_catabolism']
    sensitivity.append({'gate': 'cognate_import_assembly', 'enzyme_capacity_retained': True,
                        'uptake_profile_without_assembly_evidence': False})
    fused = Oracle(doc, fixture, 'RHIME1021', panel_members(fixture, candidates, 'RHIME1021')).evaluate()
    fused_witnesses = {role: sorted({w for result in fused['atoms'].values()
                                    if result.get('role') == role for w in result['witnesses']})
                       for role in fixture['required_reactions']}
    assert fused_witnesses == {'oxidation': ['Q92NF5'], 'cleavage': ['Q92NF6'], 'hydrolysis': ['Q92NF5']}
    circuit = compile_module(doc)
    result = {'status': 'PASS', 'module_sha256': digest(MODULE), 'fixture_sha256': digest(FIXTURE),
              'input_closure_files': len(inputs), 'released_gene_manifest_chain': release_chain,
              'production_atoms': [asdict(a) for a in iter_atoms(circuit)],
              'production_routes': [[a.node_id for a in route] for route in enumerate_routes(circuit)],
              'fusion_witnesses': fused_witnesses,
              'case_count': len(results), 'module_mutation_count': len(mutation_results),
              'gate_sensitivity_count': len(sensitivity), 'cases': results,
              'module_mutations': mutation_results, 'gate_sensitivities': sensitivity,
              'native_phenotypes_not_computed': {k: p['native_phenotype'] for k, p in fixture['panels'].items()},
              'limitations': ['Finite reviewed-member oracle; not genome-wide classifier.',
                              'Direct-or-identical profile is separately measured enzyme chemistry, not native pathway flux or growth.',
                              'Compiler supplies Boolean topology; oracle separately inspects exact chemistry, original selectors and complex units.',
                              'Same-strain gate defines a coherent finite panel, not an assertion that cross-species reconstitution is impossible.',
                              'No PAINT node placement or family-wide exact-substrate specificity inferred.',
                              'Source evidence, not ACCEPT actions or presence of broad GO terms, determines assay tiers.']}
    (HERE / 'results.yaml').write_text(yaml.safe_dump(result, sort_keys=False, width=100))
    print({k: result[k] for k in ['status', 'module_sha256', 'input_closure_files', 'case_count',
                                 'module_mutation_count', 'gate_sensitivity_count']})


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--capture-inputs', action='store_true', help='Explicitly refresh input hashes after scientific review; default verifies the frozen closure.')
    run(parser.parse_args().capture_inputs)
