"""Check immutable curation inputs and evidence-qualified System I panel capacity.

Production compile_node/is_satisfied determine topology. The independent oracle
requires curated accession/role, lineage implementation, matched taxon, frozen
family evidence and live reviewed core support. False means insufficient panel
coverage, never native genomic absence. This is not a genome-discovery or flux
predictor, and disputed CcmB membrane transport is deliberately not a gate.
"""
from collections import Counter
from copy import deepcopy
import hashlib
from pathlib import Path
import re

import yaml
from ai_gene_review.module_logic import compile_node, is_satisfied, _atom_from_annoton

ROOT = Path(__file__).resolve().parents[2]
SLUG = 'bacterial_cytochrome_c_maturation_system_i'
AUDIT = ROOT / 'analysis/module_audits' / SLUG
# Independently curated identities, not inferred from module representatives or
# a broad family name. H/I share PTHR47870, including within SF1; E variants
# share PTHR34128:SF2 despite distinct heme-linkage chemistry.
IDENTITIES = {
    'ECOLI': {'P33931': 'A', 'P0ABL8': 'B', 'P0ABM1': 'C', 'P0ABM5': 'D',
              'P69490': 'E', 'P33927': 'F', 'P0AA86': 'G', 'P0ABM9': 'HI'},
    'PSEPK': {'Q88EX5': 'A', 'Q88EX6': 'B', 'Q88EX7': 'C', 'Q88EX8': 'D',
              'Q88EX9': 'E', 'Q88EY0': 'F', 'Q88EY1': 'G', 'A0A140FWM4': 'H',
              'A0A140FWM3': 'I'},
    'OLEA2': {'Q311X1': 'A', 'Q311X2': 'B', 'Q311X3': 'C', 'F9XXF9': 'D',
              'Q311W9': 'E', 'Q311X0': 'F', 'Q311X4': 'I'},
    'RHOCB': {'P36893': 'G', 'Q00500': 'F', 'Q00501': 'H', 'D5ALI6': 'I'},
    'SHEON': {'Q8EK41': 'B'},
}
FAMILY_GATES = {
    'A': {'PANTHER:PTHR43499', 'PANTHER:PTHR42939'},
    'B': {'Pfam:PF03379'}, 'C': {'PANTHER:PTHR30071'},
    'D': {'PANTHER:PTHR37531', 'NCBIfam:TIGR04391'},
    'E': {'PANTHER:PTHR34128'}, 'F': {'PANTHER:PTHR43653'},
    'G': {'PANTHER:PTHR42852'}, 'H': {'Pfam:PF03918'},
    'I': {'InterPro:IPR017560', 'Pfam:PF23914', 'PANTHER:PTHR12558:SF13'},
}
CORE_MF = {'A': 'GO:0016887', 'C': 'GO:0020037', 'E': 'GO:0020037',
           'F': 'GO:0020037', 'G': 'GO:0015035'}
PROCESSES = {'GO:1903607', 'GO:0018063', 'GO:0017003'}
TRANSPORT = {'GO:0015232', 'GO:0015439', 'GO:0022857', 'GO:0035351', 'GO:0055085'}
# Filled with the integrated module's explicit semantic node ids. No role is
# inferred from its representative list: that would make role-swap tests circular.
ROLE_NODES = {
    'ccma_atpase': ('A', 'canonical'),
    'ccmb_membrane_subunit': ('B', 'canonical'),
    'ccmc_heme_handling_subunit': ('C', 'canonical'),
    'ccmd_accessory_subunit': ('D', 'canonical'),
    'ccme_heme_chaperone': ('E', 'canonical'),
    'ccmg_disulfide_reductase': ('G', 'canonical'),
    'ccmh_redox_component': ('H', 'canonical'),
    'ccmf_catalytic_subunit': ('F', 'canonical'),
    'ccmh_ligation_subunit': ('H', 'canonical'),
    'cych_accessory_component': ('I', 'canonical'),
    'istar_ccma_atpase': ('A', 'star'),
    'istar_ccmb_membrane_subunit': ('B', 'star'),
    'istar_ccmc_heme_handling_subunit': ('C', 'star'),
    'istar_ccmd_accessory_subunit': ('D', 'star'),
    'istar_ccme_heme_chaperone': ('E', 'star'),
    'istar_ccmf_ligation_component': ('F', 'star'),
    'istar_ccmi_accessory_component': ('I', 'star'),
}
ROUTES = {'canonical': 'canonical_ccmgh_supported_system_i',
          'star': 'g20_like_cysteine_ccme_system_i_star'}


def read(path):
    return yaml.safe_load(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def source_exists(reference):
    if reference.startswith('PMID:'):
        return (ROOT / 'publications' / ('PMID_' + reference.split(':')[1] + '.md')).exists()
    if reference.startswith('file:'):
        return any((base / reference[5:]).is_file() for base in (ROOT / 'genes', ROOT))
    return False


def load_panel():
    baseline = read(AUDIT / 'seed-baseline.yaml')
    totals, actions, panel, hashes = Counter(), Counter(), {}, {}
    for member in baseline['members']:
        path = ROOT / member['review_path']
        doc = read(path)
        assert doc['status'] == 'COMPLETE', path
        assert doc['id'] == member['accession'] and doc['taxon'] == member['taxon'], path
        rows, seeds = doc.get('existing_annotations', []), member['annotations']
        assert len(rows) >= len(seeds), path
        for seed, row in zip(seeds, rows):
            assert {k: v for k, v in row.items() if k != 'review'} == seed['payload'], path
            if seed['prior_action'] == 'NEW':
                assert row['review']['action'] == 'NEW', path
                totals['inherited_NEW'] += 1
            else:
                totals['historical_machine_rows'] += 1
        for row in rows[len(seeds):]:
            assert row['review']['action'] == 'NEW', path
            totals['genuinely_added_NEW'] += 1
        for row in rows:
            assert row['review']['action'] != 'PENDING', path
            actions[row['review']['action']] += 1
        for name, digest in member['raw_sha256'].items():
            assert sha(ROOT / name) == digest, name
            totals['raw_sources_preserved'] += 1
        totals.update(complete_reviews=1, historical_rows=len(seeds), current_rows=len(rows))
        hashes[member['review_path']] = sha(path)
        raw = path.with_name(member['gene'] + '-uniprot.txt').read_text()
        families = {db + ':' + ident for db, ident in re.findall(
            r'^DR\s+(PANTHER|InterPro|NCBIfam|Pfam); ([^;]+);', raw, re.M)}
        families |= {x.split(':SF')[0] for x in families if x.startswith('PANTHER:')}
        org, accession = member['organism'], doc['id']
        assert accession in IDENTITIES[org], accession
        # Capacity comes from the reviewed core, never pending/removed machine
        # annotation terms. Removing a live core must remove the capability even
        # when an inherited annotation still uses the same GO id.
        cores = deepcopy(doc.get('core_functions', []))
        for core in cores:
            core['_supported'] = any(source_exists(x.get('reference_id', ''))
                                     for x in core.get('supported_by', []))
        panel[accession] = dict(accession=accession, organism=org, taxon=doc['taxon']['id'],
                                roles=set(IDENTITIES[org][accession]),
                                branch='star' if org == 'OLEA2' else 'canonical',
                                linkage='cysteine' if org == 'OLEA2' else 'histidine',
                                families=families, cores=cores)
    for name, digest in baseline['provider_sha256'].items():
        assert sha(ROOT / name) == digest, name
        totals['provider_artifacts_preserved'] += 1
    assert totals['complete_reviews'] == 29 and totals['historical_rows'] == 227
    assert totals['historical_machine_rows'] == 224 and totals['inherited_NEW'] == 3
    assert totals['raw_sources_preserved'] == 58 and totals['provider_artifacts_preserved'] == 6
    assert set(panel) == {x for group in IDENTITIES.values() for x in group}
    return panel, totals, actions, hashes


def core_support(record, role, masks):
    cores = [c for c in record['cores'] if c.get('_supported')]
    if not cores:
        return False
    processes = {x['id'] for c in cores for x in c.get('directly_involved_in', [])}
    if not processes & PROCESSES:
        return False
    enabled = {c['molecular_function']['id'] for c in cores if c.get('molecular_function')} - masks
    contributes = {c['contributes_to_molecular_function']['id'] for c in cores
                   if c.get('contributes_to_molecular_function')} - masks
    if role in CORE_MF and CORE_MF[role] not in enabled:
        return False
    if role == 'F' and 'GO:0004408' not in contributes:
        return False
    return True


def evaluate(doc, panel, node_id, present, context, *, drop_roles=(), drop_cores=(),
             masks=(), drop_families=(), synthetic=(), branch_overrides=None,
             linkage_overrides=None):
    nodes = {n['id']: n for n in walk(doc['module']) if 'id' in n}
    records = [deepcopy(panel[x]) for x in present] + list(deepcopy(synthetic))
    for record in records:
        if record['accession'] in drop_cores:
            record['cores'] = []
        if record['accession'] in drop_families:
            record['families'] = set()
        if branch_overrides and record['accession'] in branch_overrides:
            record['branch'] = branch_overrides[record['accession']]
        if linkage_overrides and record['accession'] in linkage_overrides:
            record['linkage'] = linkage_overrides[record['accession']]
    taxon = next(panel[x]['taxon'] for x in IDENTITIES[context])

    def match(atom):
        assert atom.node_id in ROLE_NODES, ('Unclassified biological role', atom.node_id)
        role, branch = ROLE_NODES[atom.node_id]
        for record in records:
            accession = record['accession']
            if accession not in IDENTITIES[context] or role not in IDENTITIES[context][accession]:
                continue
            if record['taxon'] != taxon or record['organism'] != context:
                continue
            if record['branch'] != branch or role not in record['roles']:
                continue
            if (accession, role) in drop_roles or accession not in atom.uniprots:
                continue
            if not FAMILY_GATES[role] & record['families']:
                continue
            if not set(atom.family_ids) <= record['families'] or not set(atom.domain_ids) <= record['families']:
                continue
            if role == 'E' and record['linkage'] != ('cysteine' if branch == 'star' else 'histidine'):
                continue
            if not core_support(record, role, set(masks)):
                continue
            enabled = {c['molecular_function']['id'] for c in record['cores']
                       if c.get('_supported') and c.get('molecular_function')} - set(masks)
            contributes = {c['contributes_to_molecular_function']['id'] for c in record['cores']
                           if c.get('_supported') and c.get('contributes_to_molecular_function')} - set(masks)
            # A listed contribution never becomes an independently enabled
            # reaction; it is admitted only within this specified maturation role.
            if not set(atom.function_ids) <= enabled | contributes:
                continue
            return True
        return False

    def predicate(atom):
        node = nodes[atom.node_id]
        complex_ = node.get('participant', {}).get('protein_complex')
        if complex_:
            units = complex_.get('active_units', [])
            return bool(units) and all(match(_atom_from_annoton(u)) for u in units)
        return match(atom)

    node = nodes[node_id]
    compiled_node = {'id': node_id + '_single_step', 'annotons': [node]} if 'participant' in node else node
    return is_satisfied(compile_node(compiled_node), predicate)


def main():
    panel, totals, actions, hashes = load_panel()
    doc = read(ROOT / 'modules' / (SLUG + '.yaml'))
    assert ROLE_NODES and ROUTES, 'Integrated module role ids must be fixed before final evaluation'
    run_cases(doc, panel, totals, actions, hashes)


def run_cases(doc, panel, totals, actions, hashes):
    nodes = {n['id']: n for n in walk(doc['module']) if 'id' in n}
    assert set(ROLE_NODES) <= set(nodes)
    route_set = next(x for x in doc['module']['variant_sets'] if x['id'] == 'ccm_route_architectures')
    assert route_set['selection'] in {'ONE_OR_MORE', 'EXACTLY_ONE'}
    assert {v['id'] for v in route_set['variants']} == set(ROUTES.values())
    assert all(len(nodes[x].get('parts', [])) >= 2 for x in ROUTES.values())
    representatives = {n['id'].split(':', 1)[1] for n in walk(doc['module'])
                       if str(n.get('id', '')).startswith('UniProtKB:')}
    assert representatives == set(panel), (representatives ^ set(panel))
    for node_id, (role, branch) in ROLE_NODES.items():
        atom = _atom_from_annoton(nodes[node_id])
        assert atom.uniprots, node_id
        for accession in atom.uniprots:
            assert accession in panel and role in panel[accession]['roles'], (node_id, accession)
            assert panel[accession]['branch'] == branch, (node_id, accession)
        assert not set(atom.function_ids) & TRANSPORT, node_id
    # A complex-level synthase annotation must still require both active units.
    complex_node = nodes['ccmfh_synthetase_activity']
    units = complex_node['participant']['protein_complex']['active_units']
    assert {ROLE_NODES[u['id']][0] for u in units} == {'F', 'H'} and len(units) == 2
    assert complex_node['function']['term']['id'] == 'GO:0004408'
    cases = []

    def check(name, node, present, context, expected, *, alternate_doc=None, **options):
        observed = evaluate(alternate_doc or doc, panel, node, present, context, **options)
        assert observed == expected, (name, node, context, expected, observed)
        rendered = {}
        for key, value in options.items():
            if key == 'synthetic':
                rendered[key] = [dict(accession=x['accession'], organism=x['organism'],
                                      taxon=x['taxon'],
                                      core_molecular_functions=[c['molecular_function']['id']
                                          for c in x['cores'] if c.get('molecular_function')])
                                 for x in value]
            elif isinstance(value, (set, tuple)):
                rendered[key] = sorted(value)
            else:
                rendered[key] = value
        cases.append(dict(case=name, node=node, context=context, present=sorted(present),
                          expected=expected, observed=observed, mutations=rendered,
                          module_mutated=alternate_doc is not None))

    for org, branch in [('ECOLI', 'canonical'), ('PSEPK', 'canonical'), ('OLEA2', 'star')]:
        present = set(IDENTITIES[org])
        route = ROUTES[branch]
        check(org + ' curated coherent panel satisfies its route', route, present, org, True)
        check(org + ' coherent panel satisfies one root alternative', SLUG, present, org, True)
        check(org + ' does not silently realize the other architecture',
              ROUTES['star' if branch == 'canonical' else 'canonical'], present, org, False)
        check(org + ' disputed transporter terms are not a capacity gate', SLUG, present, org,
              True, masks=TRANSPORT)
        required = 'ABCDEF' if branch == 'star' else 'ABCDEFGH'
        for role in required:
            accession = next(x for x, roles in IDENTITIES[org].items() if role in roles)
            check(org + ' missing required ' + role, SLUG, present - {accession}, org, False)
            check(org + ' family alone without reviewed core ' + role, SLUG, present, org,
                  False, drop_cores=(accession,))
            check(org + ' missing family evidence ' + role, SLUG, present, org,
                  False, drop_families=(accession,))
            check(org + ' lost curated role ' + role, SLUG, present, org,
                  False, drop_roles=((accession, role),))
            if role in CORE_MF:
                check(org + ' missing core chemistry ' + role, SLUG, present, org,
                      False, masks=(CORE_MF[role],))
        check(org + ' heme binding cannot replace ligase contribution', SLUG, present, org,
              False, masks=('GO:0004408',))
        accessory = next(x for x, roles in IDENTITIES[org].items() if 'I' in roles)
        check(org + ' optional CcmI role is not required', SLUG, present, org, True,
              drop_roles=((accessory, 'I'),))
        if IDENTITIES[org][accessory] == 'I':
            check(org + ' accessory deletion retains bounded capacity', SLUG,
                  present - {accessory}, org, True)
        e = next(x for x, roles in IDENTITIES[org].items() if roles == 'E')
        wrong_linkage = 'histidine' if branch == 'star' else 'cysteine'
        check(org + ' same CcmE family with opposite linkage is insufficient', SLUG, present,
              org, False, linkage_overrides={e: wrong_linkage})
        check(org + ' same CcmE family cannot cross implementation branch', SLUG, present,
              org, False, branch_overrides={e: 'canonical' if branch == 'star' else 'star'})

    for org in ['RHOCB', 'SHEON']:
        check(org + ' partial panel does not establish full native capacity', SLUG,
              set(IDENTITIES[org]), org, False)
    check('Empty inventory cannot establish capacity', SLUG, set(), 'ECOLI', False)
    check('RHOCB curated F and H support only the modeled ligation component',
          'ccmfh_ligation_complex', {'Q00500', 'Q00501'}, 'RHOCB', True)
    check('RHOCB CcmI cannot replace CcmH despite shared PTHR47870 SF1',
          'ccmfh_ligation_complex', {'Q00500', 'D5ALI6'}, 'RHOCB', False)
    check('RHOCB helX protein-substrate reductase evidence satisfies precise chemistry',
          'ccmg_disulfide_reductase', {'P36893'}, 'RHOCB', True)
    broad_redox = deepcopy(panel['P36893'])
    for core in broad_redox['cores']:
        if core.get('molecular_function', {}).get('id') == 'GO:0015035':
            core['molecular_function'] = {'id': 'GO:0015036', 'label': 'disulfide oxidoreductase activity'}
    check('Broad oxidoreductase alone never silently entails protein-disulfide reductase',
          'ccmg_disulfide_reductase', set(), 'RHOCB', False, synthetic=(broad_redox,))
    check('RHOCB CcmF alone does not establish complete canonical ligation complex',
          'ccmfh_ligation_complex', {'Q00500'}, 'RHOCB', False)
    check('SHEON CcmB role does not require settled heme-transporter chemistry',
          'ccmb_membrane_subunit', {'Q8EK41'}, 'SHEON', True, masks=TRANSPORT)
    check('Ecoli H fusion does not pretend to be the separate CcmI selector',
          'ccmi_cych_accessory', {'P0ABM9'}, 'ECOLI', False)
    check('PSEPK separate CcmI accessory is independently grounded',
          'ccmi_cych_accessory', {'A0A140FWM3'}, 'PSEPK', True)
    check('RHOCB separate CcmI accessory is independently grounded',
          'ccmi_cych_accessory', {'D5ALI6'}, 'RHOCB', True)
    # Canonical Ecoli H/I fusion is still one H-containing product: optional-I
    # status cannot make deletion of that product optional for H-dependent CCM.
    check('Ecoli fusion I role alone cannot replace lost H role', SLUG,
          set(IDENTITIES['ECOLI']), 'ECOLI', False, drop_roles=(('P0ABM9', 'H'),))
    eco, pse, star = (set(IDENTITIES[x]) for x in ['ECOLI', 'PSEPK', 'OLEA2'])
    check('Cross-strain ATPase complementation is not presumed', SLUG,
          eco - {'P33931'} | {'Q88EX5'}, 'ECOLI', False)
    check('Mixed canonical half-panels cannot be assembled by the oracle', SLUG,
          {'P33931', 'P0ABL8', 'P0ABM1', 'P0ABM5', 'Q88EX9', 'Q88EY0', 'Q88EY1', 'A0A140FWM4'},
          'ECOLI', False)
    check('Cysteine-CcmE cannot replace canonical CcmE', SLUG,
          eco - {'P69490'} | {'Q311W9'}, 'ECOLI', False)
    check('Histidine-CcmE cannot replace System I star CcmE', SLUG,
          star - {'Q311W9'} | {'P69490'}, 'OLEA2', False)
    check('Canonical CcmF cannot silently replace System I star CcmF', SLUG,
          star - {'Q311X0'} | {'P33927'}, 'OLEA2', False)
    check('Adding unrelated G H does not alter supported System I star capacity', SLUG,
          star | {'P0AA86', 'P0ABM9'}, 'OLEA2', True)
    # Artificial controls are explicitly synthetic, never proposed biological
    # records. Matching a known accession/family cannot erase a strain conflict.
    wrong_strain = deepcopy(panel['P33931'])
    wrong_strain['taxon'] = 'NCBITaxon:SYNTHETIC_OTHER_STRAIN'
    check('Correct accession and family but mismatched strain fails', SLUG,
          eco - {'P33931'}, 'ECOLI', False, synthetic=(wrong_strain,))
    fake = deepcopy(panel['P33931'])
    fake['accession'] = 'SYNTHETIC_SAME_FAMILY_ATPASE'
    check('Generic same-family ATPase cannot replace verified CcmA', SLUG,
          eco - {'P33931'}, 'ECOLI', False, synthetic=(fake,))
    # Poisoning the model's representative selector cannot bypass the independent
    # accession-role registry, even for the same subfamily within one strain.
    poisoned = deepcopy(doc)
    bad_nodes = {n['id']: n for n in walk(poisoned['module']) if 'id' in n}
    for node_id in ['ccmh_redox_component', 'ccmh_ligation_subunit']:
        bad_nodes[node_id]['participant']['family']['representative_members'].append(
            {'preferred_term': 'synthetic wrong-role CcmI assignment',
             'term': {'id': 'UniProtKB:D5ALI6', 'label': 'CycH'}})
    check('Even a poisoned H selector cannot make RHOCB CcmI a CcmH',
          'ccmfh_ligation_complex', {'Q00500', 'D5ALI6'}, 'RHOCB', False,
          alternate_doc=poisoned)
    bad_nodes['ccma_atpase']['participant']['family']['representative_members'].append(
        {'preferred_term': 'synthetic unknown ATPase',
         'term': {'id': 'UniProtKB:SYNTHETIC_SAME_FAMILY_ATPASE', 'label': 'synthetic ATPase'}})
    check('Poisoned selector cannot turn family membership into curated role', SLUG,
          eco - {'P33931'}, 'ECOLI', False, alternate_doc=poisoned, synthetic=(fake,))
    assert totals['genuinely_added_NEW'] == 6, 'Unexpected new annotations require explicit review'
    (AUDIT / 'integration-checks.yaml').write_text(yaml.safe_dump(dict(
        status='PASS', **dict(totals), actions=dict(actions), review_sha256=hashes,
        module_sha256=sha(ROOT / 'modules' / (SLUG + '.yaml')),
        seed_baseline_sha256=sha(AUDIT / 'seed-baseline.yaml'),
        checker_sha256=sha(Path(__file__)),
        scope='29 frozen curated exemplars; preserved historical payloads/raw/provider bytes. New rows are separately counted. No native-genome absence inference.'), sort_keys=False))
    (AUDIT / 'capacity-results.yaml').write_text(yaml.safe_dump(dict(
        status='PASS', case_count=len(cases),
        semantics='Production compile_node/is_satisfied with independent accession-role, matched-strain, branch chemistry, family and reviewed-core oracle. Capacity is bounded curated-panel coverage; heterologous and inferred roles do not become native flux or genome completeness. False means unsupported panel coverage, not biological absence.',
        limitations=[
            'G20 CcmB coupling is inferred from conserved architecture and functional operon; no individual deletion assay is claimed.',
            'G20 CcmC locus is mapped but experimental versus reference residue numbering remains unresolved.',
            'KT2440 assignments are mechanistic ortholog inference; its histidine CcmE site is sequence/HAMAP-supported, not a direct linkage assay.',
            'Rhodobacter and Shewanella panels are partial; no complete native-system capacity is asserted.',
            'Disputed CcmB/CcmCD heme-translocation interpretations do not decide the pathway gate.',
            'Optional CcmI enhancement, including the Ecoli H/I fusion, is distinct from required canonical CcmH.'
        ], cases=cases), sort_keys=False))
    print(dict(totals), 'capacity cases', len(cases), 'PASS')


if __name__ == '__main__':
    main()
