"""Finite, source-qualified capacity checks; not a genome-wide flux classifier."""

import copy
import json
from dataclasses import asdict
from pathlib import Path

import yaml

from ai_gene_review.module_logic import compile_node, enumerate_routes, is_satisfied, iter_atoms

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
MODULE = ROOT / 'modules/bacterial_methionine_cycle.yaml'

# These role assignments are judgments from the separately reviewed sources, not
# inferred from the module's representative list or a shared family identifier.
MEMBERS = {
    'Q88D60': ('PSEPK', 'metK', ['metk_activity']),
    'A0A140FWS3': ('PSEPK', 'ahcY', ['ahcy_activity']),
    'Q88KB5': ('PSEPK', 'metH', ['meth_activity']),
    'Q88JF1': ('PSEPK', 'metE', ['mesd_activity']),
    'P0A817': ('ECOLI', 'metK', ['metk_activity']),
    'P07364': ('ECOLI', 'cheR', ['sam_methyltransferase_activity']),
    'P0AF12': ('ECOLI', 'pfs', ['mtnn_activity']),
    'P45578': ('ECOLI', 'luxS', ['luxs_activity']),
    'P25665': ('ECOLI', 'metE', ['mete_activity']),
    'P13009': ('ECOLI', 'metH', ['meth_activity']),
    'Q47690': ('ECOLI', 'mmuM', ['mmum_activity']),
    'Q6F6Z8': ('ACIAD', 'ACIAD3523', ['mesd_activity']),
    'Q6F6Z7': ('ACIAD', 'ACIAD3524', ['mesx_partner']),
    'Q9X034': ('THEMA', 'mtaD', ['sah_deaminase_activity']),
    'O51933': ('THEMA', 'ahcY', ['ahcy_activity', 'sih_hydrolase_activity']),
    'A0A916P3S8': ('DEHMC', 'cbdbA481', ['mesb_activity']),
    'A0R6Q9': ('MYCS2', 'metE', ['mete_activity']),
    'A0QZX6': ('MYCS2', 'metH', ['meth_activity']),
}
MF = {
    'metk_activity': 'GO:0004478', 'sam_methyltransferase_activity': 'GO:0008757',
    'ahcy_activity': 'GO:0004013', 'mtnn_activity': 'GO:0008782',
    'luxs_activity': 'GO:0043768', 'sah_deaminase_activity': 'GO:0050270',
    'meth_activity': 'GO:0008705', 'mete_activity': 'GO:0003871',
    'mesd_activity': 'GO:0008172', 'mesb_activity': 'GO:0008172',
    'mmum_activity': 'GO:0061627',
}
SAH_ROUTES = [ {'ahcy_activity'}, {'mtnn_activity', 'luxs_activity'},
               {'sah_deaminase_activity', 'sih_hydrolase_activity'} ]
REMETH_ROUTES = [ {'meth_activity'}, {'mete_activity'}, {'mesd_activity', 'mesx_partner'},
                  {'mesb_activity'}, {'mmum_activity'} ]
ENTRY = {'metk_activity', 'sam_methyltransferase_activity'}
REQUIRED_CONTEXT = {
    'metk_activity': {'methionine', 'ATP', 'compatible_MetK_cations'},
    'sam_methyltransferase_activity': {'SAM_for_methylation', 'methyl_acceptor'},
    'ahcy_activity': {'SAH', 'water', 'bound_NAD', 'hydrolytic_product_clearance'},
    'mtnn_activity': {'SAH', 'water'}, 'luxs_activity': {'SRH', 'LuxS_metal'},
    'sah_deaminase_activity': {'SAH', 'water', 'MtaD_metal'},
    'sih_hydrolase_activity': {'SIH', 'water', 'bound_NAD'},
    'meth_activity': {'homocysteine', 'methyl_folate', 'cobalamin', 'reactivation_context'},
    'mete_activity': {'homocysteine', 'methyl_polyglutamyl_folate', 'catalytic_zinc', 'MetE_active'},
    'mesd_activity': {'homocysteine', 'MesD_tested_growth_context'},
    'mesx_partner': {'MesD_tested_growth_context'},
    'mesb_activity': {'homocysteine', 'assay_methylcobalamin', 'reported_anoxic_assay'},
    'mmum_activity': {'homocysteine', 'SMM', 'catalytic_zinc'},
}
CONTEXT_PROFILES = {
    'ECOLI': {
        'available': sorted(set().union(*(REQUIRED_CONTEXT[k] for k in
                           ['metk_activity', 'sam_methyltransferase_activity', 'mtnn_activity',
                            'luxs_activity', 'meth_activity', 'mete_activity', 'mmum_activity']))),
        'source_ids': ['PMID:6251075', 'PMID:15916610', 'PMID:11489131', 'PMID:8823155',
                       'PMID:9201956', 'PMID:15502870', 'PMID:9882684'],
        'scope': 'Inputs and active enzyme states are explicit supplied assumptions for an integrated K-12 accession panel. Different cited experiments establish individual requirements, not a single culture with every condition or measured full-cycle flux.',
    },
    'THEMA': {
        'available': sorted(REQUIRED_CONTEXT['ahcy_activity'] | REQUIRED_CONTEXT['sah_deaminase_activity'] |
                            REQUIRED_CONTEXT['sih_hydrolase_activity']),
        'source_ids': ['PMID:17603473', 'PMID:23968233'],
        'scope': 'Source-qualified purified Thermotoga capacities with substrate and enzyme/cofactor context supplied. Product clearance is an explicit condition on net direct SAH hydrolysis, not a native flux measurement.',
    },
    'ACIAD': {
        'available': sorted(REQUIRED_CONTEXT['mesd_activity']),
        'source_ids': ['PMID:18319726', 'PMID:18840283', 'PMID:33534785'],
        'scope': 'Matched ADP1 pair in the native genetic growth context; chemistry is assigned using the subsequent MesD interpretation. No identified methyl donor, purified ADP1 enzyme assay or ADP1 oxygen-dependence measurement is asserted.',
    },
    'DEHMC': {
        'available': sorted(REQUIRED_CONTEXT['mesb_activity']),
        'source_ids': ['PMID:32034217'],
        'scope': 'Purified CBDB1 MesB in the reported anoxic assay with methylcobalamin and homocysteine supplied. This profile does not supply or establish the hypothetical native AcsCD donor.',
    },
    'MYCS2': {
        'available': sorted(REQUIRED_CONTEXT['meth_activity'] | REQUIRED_CONTEXT['mete_activity']),
        'source_ids': ['PMID:33468593'],
        'scope': 'The case selects enzyme availability to represent the source-defined cobalamin/regulatory context. Required substrates and catalytic state are supplied assumptions; no complete native cycle flux is inferred.',
    },
    'PSEPK': {
        'available': [],
        'source_ids': ['file:genes/PSEPK/metK/metK-ai-review.yaml'],
        'scope': 'Partial reviewed panel without an independently supplied complete-cycle context. A negative finite-panel result does not establish absence of those functions from KT2440.',
    },
}


def index_nodes(data):
    result = {}

    def visit(value):
        if isinstance(value, dict):
            if 'id' in value:
                result[value['id']] = value
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    visit(data['module'])
    return result


def effective_terms(doc):
    terms = set()
    for row in doc.get('existing_annotations', []):
        review = row['review']
        if review['action'] in {'ACCEPT', 'KEEP_AS_NON_CORE', 'NEW'}:
            terms.add(row['term']['id'])
        elif review['action'] == 'MODIFY':
            terms.update(term['id'] for term in review.get('proposed_replacement_terms', []))
    for core in doc.get('core_functions', []):
        for key in ('molecular_function', 'contributes_to_molecular_function'):
            if key in core:
                terms.add(core[key]['id'])
    return terms


def registry():
    result = {}
    for accession, (organism, gene, roles) in MEMBERS.items():
        path = ROOT / 'genes' / organism / gene / (gene + '-ai-review.yaml')
        doc = yaml.safe_load(path.read_text())
        assert doc['id'] == accession and doc['status'] == 'COMPLETE', path
        assert all(row['review']['action'] != 'PENDING' for row in doc.get('existing_annotations', [])), path
        terms = effective_terms(doc)
        if accession == 'P07364':
            # The direct CheR activity is more precise than the distributed role.
            assert 'GO:0008983' in terms
            raw = path.with_name(gene + '-uniprot.txt').read_text()
            assert 'RHEA:24452' in raw and 'S-adenosyl-L-homocysteine' in raw
            terms.add('GO:0008757')
        for role in roles:
            if role in MF:
                assert MF[role] in terms, (path, role, terms)
            elif role == 'sih_hydrolase_activity':
                assert any(core.get('proposed_molecular_function') == 'S-inosyl-L-homocysteine hydrolase activity'
                           for core in doc.get('core_functions', [])), path
            elif role == 'mesx_partner':
                assert any(ref['id'] == 'PMID:18319726' for ref in doc.get('references', [])), path
        classifications = set()
        for line in path.with_name(gene + '-uniprot.txt').read_text().splitlines():
            if line.startswith(('DR   PANTHER;', 'DR   InterPro;')):
                db, identifier, *_ = line[5:].split(';')
                classifications.add(db.strip() + ':' + identifier.strip())
        result[accession] = {'organism': organism, 'gene': gene, 'taxon': doc['taxon']['id'],
                             'roles': roles, 'functions': sorted(terms),
                             'classifications': sorted(classifications),
                             'review': str(path.relative_to(ROOT))}
    return result


def structural_requirements(doc):
    nodes = index_nodes(doc)
    assert nodes['bacterial_methionine_cycle']['context']['taxa'][0]['term']['id'] == 'NCBITaxon:2'
    circuit = compile_node(doc['module'])
    expected = {frozenset(ENTRY | sah | remeth) for sah in SAH_ROUTES for remeth in REMETH_ROUTES}
    actual = {frozenset(atom.node_id for atom in route) for route in enumerate_routes(circuit)}
    assert actual == expected, (actual - expected, expected - actual)
    atoms = {a.node_id: a for a in iter_atoms(circuit)}
    for role, go in MF.items():
        assert atoms[role].function_ids == (go,), (role, atoms[role].function_ids)
    assert not atoms['mesx_partner'].function_ids, 'Do not invent MesX enzymatic activity'
    assert not atoms['sih_hydrolase_activity'].function_ids, 'No established SIH-specific GO term'
    assert atoms['mesx_partner'].domain_ids == ('InterPro:IPR015004',)
    assert 'Q88JF1' not in atoms['mete_activity'].uniprots
    assert set(atoms['mete_activity'].uniprots) == {'P25665', 'A0R6Q9'}
    assert not nodes['mesx_step'].get('optional'), 'MesX is required'
    return circuit, nodes


class Oracle:
    def __init__(self, members, context, disabled=()):
        self.members, self.context, self.disabled = members, context, set(disabled)

    def gate(self, name, value):
        return name in self.disabled or value

    def __call__(self, atom):
        c = self.context
        if not self.gate('taxon', c.get('bacterial', True)):
            return False
        if not self.gate('source', atom.node_id not in c.get('unsupported_roles', [])):
            return False
        if not self.gate('context', atom.node_id not in c.get('unavailable_activities', [])):
            return False
        if not self.gate('input_context', REQUIRED_CONTEXT[atom.node_id] <= set(c.get('available_inputs', []))):
            return False
        if not self.gate('native_flux', c.get('profile') != 'native_flux'):
            # None of these collections measures the complete native cycle flux.
            return False
        for accession in c['members']:
            row = self.members.get(accession)
            if row is None or accession not in atom.uniprots:
                continue
            if not self.gate('panel', row['organism'] == c['organism']):
                continue
            roles = set(row['roles']) - set(c.get('masked_roles', {}).get(accession, []))
            if not self.gate('role', atom.node_id in roles):
                continue
            functions = set(row['functions']) - set(c.get('masked_functions', {}).get(accession, []))
            if not self.gate('function', set(atom.function_ids) <= functions):
                continue
            available = set(row['classifications']) - set(c.get('masked_classifications', []))
            if not self.gate('family', set(atom.family_ids) <= available):
                continue
            if not self.gate('domain', set(atom.domain_ids) <= available):
                continue
            return True
        return False


def scenarios():
    # Whole-cycle positives are evidence-qualified biochemical capacity in a
    # K-12 accession panel, not measured native flux in one experimental culture.
    entry = ['P0A817', 'P07364', 'P0AF12', 'P45578']
    rows = []

    def case(name, organism, members, expected, node='bacterial_methionine_cycle', **context):
        profile = CONTEXT_PROFILES[organism]
        rows.append({'name': name, 'node': node, 'expected': expected,
                     'context': {'organism': organism, 'members': members,
                                 'available_inputs': list(profile['available']),
                                 'source_ids': profile['source_ids'], 'source_scope': profile['scope'],
                                 'profile': 'biochemical_capacity', **context}})

    for accession, route in [('P25665', 'MetE'), ('P13009', 'MetH'), ('Q47690', 'MmuM')]:
        case('ECOLI ' + route + ' conditional capacity', 'ECOLI', entry + [accession], True)
        case('ECOLI ' + route + ' is not native flux proof', 'ECOLI', entry + [accession], False, profile='native_flux')
    complete = entry + ['P25665']
    for accession in complete:
        case('ECOLI missing ' + accession, 'ECOLI', [x for x in complete if x != accession], False)
    for role, reason in [('metk_activity', 'ATP or compatible metal missing'),
                         ('sam_methyltransferase_activity', 'SAM/acceptor missing or radical-SAM-only evidence'),
                         ('mete_activity', 'polyglutamyl-folate missing or MetE oxidatively inactive')]:
        case(reason, 'ECOLI', complete, False, unavailable_activities=[role])
    case('MetH without usable B12/reactivation context', 'ECOLI', entry + ['P13009'], False, unavailable_activities=['meth_activity'])
    case('MmuM without available SMM donor', 'ECOLI', entry + ['Q47690'], False, unavailable_activities=['mmum_activity'])
    case('No source support for CheR reaction', 'ECOLI', complete, False, unsupported_roles=['sam_methyltransferase_activity'])
    case('Bacterial occurrence cannot license nonbacterial profile', 'ECOLI', complete, False, bacterial=False)
    case('Cross-species MetK cannot close ECOLI panel', 'ECOLI', ['Q88D60', *complete[1:]], False)
    case('MetK required classification masked', 'ECOLI', complete, False, masked_classifications=['PANTHER:PTHR11964'])
    case('MetK family identity without role evidence', 'ECOLI', complete, False, masked_roles={'P0A817': ['metk_activity']})
    case('MetK family identity without functional evidence', 'ECOLI', complete, False, masked_functions={'P0A817': ['GO:0004478']})
    case('No unstated input-context default', 'ECOLI', complete, False, available_inputs=[])
    case('MetH B12 explicitly absent', 'ECOLI', entry + ['P13009'], False,
         available_inputs=[x for x in CONTEXT_PROFILES['ECOLI']['available'] if x != 'cobalamin'])
    case('MmuM SMM explicitly absent', 'ECOLI', entry + ['Q47690'], False,
         available_inputs=[x for x in CONTEXT_PROFILES['ECOLI']['available'] if x != 'SMM'])
    case('MesD cannot stand in for canonical MetE', 'ECOLI', entry + ['Q88JF1'], False)
    case('THEMA matched deamination/hydrolysis', 'THEMA', ['Q9X034', 'O51933'], True, node='sah_deamination_route')
    case('THEMA deaminase alone', 'THEMA', ['Q9X034'], False, node='sah_deamination_route')
    case('THEMA SIH hydrolase alone', 'THEMA', ['O51933'], False, node='sah_deamination_route')
    case('THEMA ordinary SAH hydrolysis retained', 'THEMA', ['O51933'], True, node='ahcy_route')
    case('THEMA adverse hydrolysis product context', 'THEMA', ['O51933'], False, node='ahcy_route', unavailable_activities=['ahcy_activity'])
    case('THEMA subroute is not a complete cycle', 'THEMA', ['Q9X034', 'O51933'], False)
    case('ACIAD matched MesD/MesX source context', 'ACIAD', ['Q6F6Z8', 'Q6F6Z7'], True, node='mesd_mesx_variant')
    case('ACIAD MesD without MesX', 'ACIAD', ['Q6F6Z8'], False, node='mesd_mesx_variant')
    case('ACIAD MesX without MesD', 'ACIAD', ['Q6F6Z7'], False, node='mesd_mesx_variant')
    case('MesX without verified domain', 'ACIAD', ['Q6F6Z8', 'Q6F6Z7'], False, node='mesd_mesx_variant', masked_classifications=['InterPro:IPR015004'])
    case('No inferred cross-species MesD/MesX pair', 'ACIAD', ['Q88JF1', 'Q6F6Z7'], False, node='mesd_mesx_variant')
    case('ACIAD pair is not a full-cycle panel', 'ACIAD', ['Q6F6Z8', 'Q6F6Z7'], False)
    case('DEHMC measured corrinoid assay capacity', 'DEHMC', ['A0A916P3S8'], True, node='mesb_variant')
    case('DEHMC unspecified native donor is not supplied', 'DEHMC', ['A0A916P3S8'], False, node='mesb_variant', unavailable_activities=['mesb_activity'])
    case('DEHMC native-donor guess cannot replace assay methylcobalamin', 'DEHMC', ['A0A916P3S8'], False,
         node='mesb_variant', available_inputs=['homocysteine', 'reported_anoxic_assay', 'hypothetical_AcsCD'])
    case('DEHMC purified enzyme is not native cycle proof', 'DEHMC', ['A0A916P3S8'], False)
    for organism, members in [('PSEPK', ['Q88D60', 'A0A140FWS3', 'Q88KB5', 'Q88JF1']), ('MYCS2', ['A0R6Q9', 'A0QZX6'])]:
        case(organism + ' partial panel cannot imply missing genome functions', organism, members, False)
    case('MYCS2 MetH with B12 and repression of MetE', 'MYCS2', ['A0R6Q9', 'A0QZX6'], True,
         node='homocysteine_remethylation', unavailable_activities=['mete_activity'],
         available_inputs=[x for x in CONTEXT_PROFILES['MYCS2']['available'] if x != 'MetE_active'])
    case('MYCS2 MetE in permissive B12-deficient context', 'MYCS2', ['A0R6Q9', 'A0QZX6'], True,
         node='homocysteine_remethylation', unavailable_activities=['meth_activity'],
         available_inputs=[x for x in CONTEXT_PROFILES['MYCS2']['available']
                           if x not in {'cobalamin', 'reactivation_context'}])
    case('MYCS2 neither enzyme available', 'MYCS2', ['A0R6Q9', 'A0QZX6'], False, node='homocysteine_remethylation', unavailable_activities=['mete_activity', 'meth_activity'])
    return rows


def main():
    doc = yaml.safe_load(MODULE.read_text())
    circuit, nodes = structural_requirements(doc)
    members = registry()
    cases = scenarios()
    for case in cases:
        actual = is_satisfied(compile_node(nodes[case['node']]), Oracle(members, case['context']))
        case['actual'] = actual
        assert actual == case['expected'], case
    sensitivity = {}
    for gate in ['taxon', 'source', 'context', 'input_context', 'native_flux', 'panel', 'role', 'function', 'family', 'domain']:
        changed = [case['name'] for case in cases if is_satisfied(
            compile_node(nodes[case['node']]), Oracle(members, case['context'], [gate])) != case['expected']]
        assert changed, gate
        sensitivity[gate] = changed
    mutations = {}
    for name in ['drop_entry', 'pfs_without_luxs', 'deamination_without_hydrolysis', 'mesd_without_mesx',
                 'omit_mmum', 'compact_as_mete', 'wrong_mete_function', 'invent_mesx_function', 'restrict_taxon']:
        changed = copy.deepcopy(doc)
        n = index_nodes(changed)
        if name == 'drop_entry':
            n['bacterial_methionine_cycle']['parts'].pop(0)
        elif name == 'pfs_without_luxs':
            n['mtnn_luxs_route']['parts'].pop()
        elif name == 'deamination_without_hydrolysis':
            n['sah_deamination_route']['parts'].pop()
        elif name == 'mesd_without_mesx':
            n['mesd_mesx_variant']['parts'].pop()
        elif name == 'omit_mmum':
            n['methionine_synthase_route']['variants'].pop()
        elif name == 'compact_as_mete':
            n['mete_activity']['participant']['family']['representative_members'][0]['term']['id'] = 'UniProtKB:Q88JF1'
        elif name == 'wrong_mete_function':
            n['mete_activity']['function']['term']['id'] = 'GO:0008172'
        elif name == 'invent_mesx_function':
            n['mesx_partner']['function'] = {'term': {'id': 'GO:0008172'}}
        elif name == 'restrict_taxon':
            n['bacterial_methionine_cycle']['context']['taxa'][0]['term']['id'] = 'NCBITaxon:160488'
        try:
            structural_requirements(changed)
        except AssertionError:
            mutations[name] = 'DETECTED'
        else:
            raise AssertionError('Undetected model mutation: ' + name)
    output = {'status': 'PASS', 'members': members, 'cases': cases, 'gate_sensitivities': sensitivity,
              'mutations': mutations, 'compiler_atoms': [asdict(atom) for atom in iter_atoms(circuit)],
              'logical_route_count': len(list(enumerate_routes(circuit))),
              'limits': 'Finite reviewed-exemplar capacity checks. Fifteen logical route combinations are not fifteen demonstrated native pathways. Cofactor, donor, redox and product contexts are source-qualified oracle inputs; production Boolean compilation does not infer them. Partial panels cannot establish genomic absence, cross-species compatibility or complete native flux.'}
    (HERE / 'capacity-results.json').write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'members': len(members), 'cases': len(cases),
                      'mutations': len(mutations), 'gate_sensitivities': len(sensitivity)}))


if __name__ == '__main__':
    main()
