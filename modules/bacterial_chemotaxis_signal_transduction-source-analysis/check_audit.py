"""Check preserved inputs and chemotaxis capacity with the production compiler.

Run from any directory with ``uv run python <this-file>``. The oracle supplies
biological meaning the generic compiler intentionally does not implement:
family/domain AND reviewed activity, and every active unit of a complex. An
unresolved family descriptor requires an independently curated exemplar role.
Contributions to an assembled complex never count as independently enabled
activities. These are capacity/selector checks, not predictions of native
behavior, expression, stoichiometry or cross-species subunit compatibility.
"""

from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path

import yaml

from upstream_qualifiers import original_payloads

from ai_gene_review.module_logic import (
    _atom_from_annoton, compile_node, is_satisfied,
)

ROOT = Path(__file__).resolve().parents[2]
SLUG = 'bacterial_chemotaxis_signal_transduction'
AUDIT = ROOT / 'analysis/module_audits' / SLUG


def read(path):
    return yaml.safe_load(path.read_text())


def signature(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False)


def payload(row):
    return {k: v for k, v in row.items() if k != 'review'}


def preservation(baseline):
    refined = read(AUDIT / 'PP_4332-authored-proposal-refinement.yaml')
    retired = read(AUDIT / 'retired-inherited-proposals.yaml')
    totals = Counter()
    actions = Counter()
    hashes = {}
    providers = read(AUDIT / 'provider-source-preservation.yaml')
    for name, expected_hash in providers['sha256'].items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected_hash, name
    for member in baseline['members']:
        path = ROOT / member['review_path']
        doc = read(path)
        key = member['organism'] + '/' + member['gene']
        assert doc['status'] == 'COMPLETE', key
        assert doc['id'] == member['accession'], key
        assert doc['taxon'] == member['taxon'], key
        expected = Counter(signature(a['payload']) for a in member['annotations'])
        checked_payloads = original_payloads(ROOT, AUDIT, member, doc)
        actual = Counter(signature(a) for a in checked_payloads)
        if key == refined['gene']:
            assert refined['original_row']['review']['action'] == 'NEW'
            expected.subtract({signature(payload(refined['original_row'])): 1})
            expected.update({signature(payload(refined['replacement_row'])): 1})
        for old in retired:
            if key == old['gene']:
                assert old['row']['review']['action'] == 'NEW'
                expected.subtract({signature(payload(old['row'])): 1})
        assert all(n >= 0 for n in expected.values()), key
        assert not (+expected - actual), key
        added = actual - (+expected)
        for row, checked_payload in zip(doc['existing_annotations'], checked_payloads):
            action = row['review']['action']
            assert action != 'PENDING', key
            if added[signature(checked_payload)]:
                assert action == 'NEW', key
            actions[action] += 1
        totals['genuinely_added_NEW'] += sum(added.values())
        totals['complete_reviews'] += 1
        totals['historical_rows'] += len(member['annotations'])
        totals['machine_rows_preserved'] += sum(
            a['prior_action'] != 'NEW' for a in member['annotations'])
        totals['current_rows'] += len(doc['existing_annotations'])
        for name, expected_hash in member['raw_sha256'].items():
            assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected_hash, name
            totals['raw_sources_preserved'] += 1
        hashes[member['review_path']] = hashlib.sha256(path.read_bytes()).hexdigest()
    return dict(totals) | {
        'inherited_proposals_retired': len(retired),
        'inherited_proposals_refined': 1,
        'provider_artifacts_preserved': len(providers['sha256']),
        'current_actions': dict(actions), 'review_sha256': hashes,
    }


def records(baseline):
    result = {}
    for member in baseline['members']:
        doc = read(ROOT / member['review_path'])
        identifiers = set()
        raw = ROOT / next(p for p in member['raw_sha256'] if p.endswith('-uniprot.txt'))
        for line in raw.read_text().splitlines():
            if not line.startswith('DR   '):
                continue
            fields = [s.strip() for s in line[5:].split(';')]
            if fields[0] in {'InterPro', 'PANTHER', 'Pfam', 'NCBIfam'}:
                identifiers.add(fields[0] + ':' + fields[1])
                if fields[0] == 'PANTHER':
                    identifiers.add('PANTHER:' + fields[1].split(':')[0])
        enabled, contributes = set(), set()
        for row in doc['existing_annotations']:
            review = row['review']
            if 'NOT' in row.get('qualifier', ''):
                continue
            target = contributes if row.get('qualifier') == 'contributes_to' else enabled
            if review['action'] in {'ACCEPT', 'KEEP_AS_NON_CORE', 'NEW'}:
                target.add(row['term']['id'])
            elif review['action'] == 'MODIFY':
                target.update(t['id'] for t in review.get('proposed_replacement_terms', []))
        for core in doc.get('core_functions', []):
            if core.get('molecular_function'):
                enabled.add(core['molecular_function']['id'])
            if core.get('contributes_to_molecular_function'):
                contributes.add(core['contributes_to_molecular_function']['id'])
        result[member['organism'] + '/' + member['gene']] = {
            'accession': doc['id'], 'identifiers': identifiers,
            'enabled': enabled, 'contributes': contributes,
        }
    return result


def index_nodes(root):
    nodes, annotons = {}, {}

    def visit(node):
        assert node['id'] not in nodes
        nodes[node['id']] = node
        for annoton in node.get('annotons', []):
            assert annoton['id'] not in annotons
            annotons[annoton['id']] = annoton
        for part in node.get('parts', []):
            visit(part['node'])
        for variants in node.get('variant_sets', []):
            for variant in variants['variants']:
                visit(variant)
    visit(root)
    return nodes, annotons


def oracle(annotons, available, family_scan=False):
    def match(atom, complex_functions=()):
        for record in available:
            # Without a known family ID, exemplars carry independently curated
            # role identity. A receiver domain is not a motor-output role.
            if not family_scan or not atom.family_ids:
                if record['accession'] not in atom.uniprots:
                    continue
            if atom.family_ids and not set(atom.family_ids) <= record['identifiers']:
                continue
            if not set(atom.domain_ids) <= record['identifiers']:
                continue
            if not set(atom.function_ids) <= record['enabled']:
                continue
            if not set(complex_functions) <= record['enabled'] | record['contributes']:
                continue
            return True
        return False

    def predicate(atom):
        annoton = annotons[atom.node_id]
        participant = annoton.get('participant', {})
        if participant.get('selector_type') != 'PROTEIN_COMPLEX':
            return match(atom)
        units = participant['protein_complex'].get('active_units', [])
        assert units, 'A complex must have explicit active units'
        return all(match(_atom_from_annoton(unit), atom.function_ids) for unit in units)
    return predicate


def capacity(doc, panel):
    nodes, annotons = index_nodes(doc['module'])
    cases = []

    def check(name, node, members, expected, *, scan=False, masks=(), synthetic=()):
        available = [deepcopy(panel[m]) for m in members]
        available.extend(deepcopy(list(synthetic)))
        for record in available:
            record['enabled'].difference_update(masks)
            record['contributes'].difference_update(masks)
        actual = is_satisfied(compile_node(nodes[node]), oracle(annotons, available, scan))
        cases.append({'case': name, 'node': node, 'members': members,
                      'family_scan': scan, 'masked_functions': list(masks),
                      'synthetic_controls': [r['accession'] for r in synthetic],
                      'expected': expected, 'observed': actual})

    psepk = [k for k in panel if k.startswith('PSEPK/')]
    root = SLUG
    check('complete KT2440 basal machinery', root, psepk, True)
    for gene in ['cheA', 'cheY', 'fliN', 'fliG', 'fliM', 'PP_4332']:
        check('KT2440 missing ' + gene, root, [k for k in psepk if k != 'PSEPK/' + gene], False)
    check('basal capacity without accelerators or methylation is not wild-type behavior', root,
          [k for k in psepk if k not in {'PSEPK/cheR2', 'PSEPK/cheB1', 'PSEPK/cheZ'}], True)
    for pair in [('motA', 'motB'), ('PP_4336', 'PP_4335')]:
        check('remaining intact stator after removing ' + '/'.join(pair), root,
              [k for k in psepk if k not in {'PSEPK/' + g for g in pair}], True)
    check('no complete stator pair', root,
          [k for k in psepk if k not in {'PSEPK/motB', 'PSEPK/PP_4335'}], False)
    for node, pair in [('motab_stator', ['PSEPK/motA', 'PSEPK/motB']),
                       ('motcd_stator', ['PSEPK/PP_4336', 'PSEPK/PP_4335']),
                       ('pomab_stator', ['VIBAL/pomA', 'VIBAL/pomB'])]:
        check(node + ' complete pair', node, pair, True)
        for member in pair:
            check(node + ' isolated ' + member, node, [member], False)
    check('sodium stator cannot fill proton stator', 'motab_stator', ['VIBAL/pomA', 'VIBAL/pomB'], False, scan=True)
    check('proton stator cannot fill sodium stator', 'pomab_stator', ['PSEPK/motA', 'PSEPK/motB'], False, scan=True)
    for member in ['ECOLI/cheW', 'PSEPK/PP_4332', 'BACSU/cheW']:
        check('standalone adaptor ' + member, 'standalone_chew_coupling', [member], True)
    check('CheA CheW domain is not standalone adaptor', 'standalone_chew_coupling', ['BACSU/cheA'], False, scan=True)
    check('CheV coupling', 'chev_coupling', ['BACSU/cheV'], True)
    check('CheV receiver adaptation', 'chev_receiver_adaptation', ['BACSU/cheV'], True)
    check('CheV coupling independent of receiver chemistry', 'chev_coupling', ['BACSU/cheV'], True, masks=['GO:0000156'])
    check('CheV adaptation requires receiver chemistry', 'chev_receiver_adaptation', ['BACSU/cheV'], False, masks=['GO:0000156'])
    for node, member in [('cytoplasmic_tlpd_input', 'HELPY/tlpD'), ('bacillus_mcp_input', 'BACSU/mcpB'), ('bacillus_mcp_input', 'BACSU/mcpC')]:
        check('receptor ' + member, node, [member], True)
    for member in ['ECOLI/cheY', 'PSEPK/cheY', 'BACSU/cheY', 'RHIML/cheY2']:
        check('motor output ' + member, 'chey_response_output', [member], True)
    check('sink receiver cannot fill motor-output role', 'chey_response_output', ['RHIML/cheY1'], False, scan=True)
    generic = {'accession': 'synthetic_receiver_only', 'identifiers': {'InterPro:IPR001789', 'PANTHER:PTHR43228'}, 'enabled': {'GO:0000156'}, 'contributes': set()}
    check('generic receiver domain and MF do not establish motor role', 'chey_response_output', [], False, scan=True, synthetic=[generic])
    for node, member in [('canonical_chez_reset', 'ECOLI/cheZ'), ('helicobacter_chez_reset', 'HELPY/cheZ'), ('fliy_accelerated_reset', 'BACSU/fliY'), ('chec_accelerated_reset', 'BACSU/cheC')]:
        check('reset ' + member, node, [member], True, scan=True)
    for node, member in [('canonical_chez_reset', 'BACSU/cheC'), ('canonical_chez_reset', 'HELPY/cheZ'), ('fliy_accelerated_reset', 'PSEPK/fliN'), ('fliy_accelerated_reset', 'BACSU/fliM')]:
        check('reject catalytic family conflation ' + member + ' as ' + node, node, [member], False, scan=True)
    check('CheC/CheD binding feedback', 'chec_ched_feedback', ['BACSU/cheC', 'BACSU/cheD'], True)
    check('CheC/CheD binding feedback without enzyme activities', 'chec_ched_feedback', ['BACSU/cheC', 'BACSU/cheD'], True, masks=['GO:0004721', 'GO:0050568'])
    check('CheC alone lacks feedback partner', 'chec_ched_feedback', ['BACSU/cheC'], False)
    check('selected receptor deamidation', 'ched_selected_receptor_deamidation', ['BACSU/cheD'], True)
    check('deamidation requires enzyme activity', 'ched_selected_receptor_deamidation', ['BACSU/cheD'], False, masks=['GO:0050568'])
    check('Sinorhizobium phosphate drain', 'chey_phosphate_drain', ['RHIME/cheA', 'RHIML/cheY1'], True)
    check('sink requires phosphotransfer partner', 'chey_phosphate_drain', ['RHIML/cheY1'], False)
    check('motor receiver cannot replace sink receiver', 'chey_phosphate_drain', ['RHIME/cheA', 'RHIML/cheY2'], False)
    check('CheT sink acceleration', 'chet_sink_dephosphorylation', ['RHIME/cheT'], True)
    check('CheZ cannot replace CheT by phosphatase MF alone', 'chet_sink_dephosphorylation', ['ECOLI/cheZ'], False, scan=True)
    for members in [[], ['VIBVU/VV1_1397'], ['VIBVU/VV1_1954'], ['VIBVU/VV1_1397', 'VIBVU/VV1_1954']]:
        check('Vibrio coexisting reset systems ' + str(len(members)) + ' ' + ','.join(members), 'accelerated_signal_reset', members, bool(members))
    check('FliN C-ring', 'flin_c_ring', ['PSEPK/fliG', 'PSEPK/fliM', 'PSEPK/fliN'], True)
    check('FliY C-ring synthetic role coverage, not cross-species assembly', 'fliy_c_ring', ['PSEPK/fliG', 'BACSU/fliM', 'BACSU/fliY'], True)
    check('FliY cannot supply whole C-ring alone', 'fliy_c_ring', ['BACSU/fliY'], False)
    anchor = {'accession': 'synthetic_OmpA_like_anchor', 'identifiers': {'PANTHER:PTHR30329'}, 'enabled': {'GO:0042834'}, 'contributes': set()}
    check('broad anchor family cannot replace PomB', 'pomab_stator', ['VIBAL/pomA'], False, scan=True, synthetic=[anchor])
    failures = [case for case in cases if case['observed'] != case['expected']]
    assert not failures, json.dumps(failures, indent=2)
    return {'case_count': len(cases), 'all_passed': True,
            'scope': 'Curated exemplar capacity and selector specificity; no native phenotype or cross-species complex-assembly inference.',
            'complex_oracle': 'Every active unit must match its family/domain and independently support or contribute to the assembled activity.',
            'cases': cases}


def main():
    baseline = read(AUDIT / 'seed-baseline.yaml')
    report = preservation(baseline)
    checks = capacity(read(ROOT / 'modules' / (SLUG + '.yaml')), records(baseline))
    (AUDIT / 'preservation-results.yaml').write_text(yaml.safe_dump(report, sort_keys=False, width=100))
    (AUDIT / 'capacity-results.yaml').write_text(yaml.safe_dump(checks, sort_keys=False, width=100))
    print(json.dumps({k: v for k, v in report.items() if k != 'review_sha256'} | {'capacity_cases': checks['case_count']}, indent=2))


if __name__ == '__main__':
    main()
