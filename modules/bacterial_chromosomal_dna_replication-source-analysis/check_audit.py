"""Frozen-panel preservation and replication capacity using the production compiler.

This is an evidence-bounded capability audit, not a genome-wide predictor or proof
of native replication sufficiency. A role requires reviewed chemistry AND curated
role identity. All roles are evaluated within one taxon at a time; complex units
must be distinct compatible proteins. Fused proofreading must occur on the same
protein as polymerization. Native Bacillus gap-filler assignment stays unresolved
unless the caller explicitly requests its demonstrated in-vitro PolA capacity.
"""
from collections import Counter
from copy import deepcopy
import hashlib
import itertools
import json
from pathlib import Path

import yaml
from ai_gene_review.module_logic import _atom_from_annoton, compile_node, is_satisfied

ROOT = Path(__file__).resolve().parents[2]
SLUG = 'bacterial_chromosomal_dna_replication'
AUDIT = ROOT / 'analysis/module_audits' / SLUG


def read(path):
    return yaml.safe_load(path.read_text())


def payload(row):
    return {k: v for k, v in row.items() if k != 'review'}


def signature(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False)


def preservation(baseline):
    totals, actions, hashes = Counter(), Counter(), {}
    for member in baseline['members']:
        path = ROOT / member['review_path']
        doc = read(path)
        assert doc['status'] == 'COMPLETE', member['review_path']
        assert doc['id'] == member['accession'] and doc['taxon'] == member['taxon']
        expected = Counter(signature(a['payload']) for a in member['annotations'])
        actual = Counter(signature(payload(a)) for a in doc.get('existing_annotations', []))
        assert not expected - actual, member['review_path']
        added = actual - expected
        for row in doc.get('existing_annotations', []):
            action = row['review']['action']
            assert action != 'PENDING', member['review_path']
            if added[signature(payload(row))]:
                assert action == 'NEW', member['review_path']
            actions[action] += 1
        totals.update(complete_reviews=1, historical_rows=sum(expected.values()),
                      current_rows=sum(actual.values()), added_NEW=sum(added.values()),
                      inherited_NEW=sum(a['prior_action'] == 'NEW' for a in member['annotations']),
                      machine_rows_preserved=sum(a['prior_action'] != 'NEW' for a in member['annotations']))
        for field, key in [('raw_sha256', 'raw_files_preserved'), ('provider_sha256', 'provider_files_preserved')]:
            for p, h in member[field].items():
                assert hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h, p
                totals[key] += 1
        hashes[member['review_path']] = hashlib.sha256(path.read_bytes()).hexdigest()
    return {'status': 'PASS', **dict(totals), 'actions': dict(actions), 'review_sha256': hashes}


def records(baseline):
    panel = {}
    for member in baseline['members']:
        doc = read(ROOT / member['review_path'])
        identifiers, enabled, contributes, proposed = set(), set(), set(), set()
        raw = next(p for p in member['raw_sha256'] if p.endswith('-uniprot.txt'))
        for line in (ROOT / raw).read_text().splitlines():
            if line.startswith('DR   '):
                fields = [s.strip() for s in line[5:].split(';')]
                if fields[0] in {'InterPro', 'PANTHER', 'Pfam', 'NCBIfam'}:
                    identifiers.add(fields[0] + ':' + fields[1])
                    if fields[0] == 'PANTHER':
                        identifiers.add('PANTHER:' + fields[1].split(':')[0])
        for row in doc.get('existing_annotations', []):
            if 'NOT' in row.get('qualifier', ''):
                continue
            decision = row['review']
            qualifier = row.get('qualifier', 'enables')
            corrections = {x.get('corrected_value') for x in decision.get('source_defects', [])
                           if x.get('defect_type') == 'WRONG_QUALIFIER' and x.get('asserted_value') == qualifier}
            if corrections:
                assert corrections == {'contributes_to'} and qualifier == 'enables'
                qualifier = 'contributes_to'
            target = contributes if qualifier == 'contributes_to' else enabled
            if decision['action'] in {'ACCEPT', 'KEEP_AS_NON_CORE', 'NEW'}:
                target.add(row['term']['id'])
            elif decision['action'] == 'MODIFY':
                target.update(t['id'] for t in decision.get('proposed_replacement_terms', []) if t['id'] != 'NTR')
        for core in doc.get('core_functions', []):
            if core.get('molecular_function'):
                enabled.add(core['molecular_function']['id'])
            if core.get('contributes_to_molecular_function'):
                contributes.add(core['contributes_to_molecular_function']['id'])
            if core.get('proposed_molecular_function'):
                name = core['proposed_molecular_function']
                term = next(t for t in doc.get('proposed_new_terms', []) if t['proposed_name'] == name)
                assert core.get('supported_by') or term.get('supported_by')
                proposed.add(name)
        panel[member['organism'] + '/' + member['gene']] = {
            'accession': doc['id'], 'taxon': doc['taxon']['id'],
            'identifiers': identifiers, 'enabled': enabled,
            'contributes': contributes, 'proposed': proposed,
        }
    return panel


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


def oracle(annotons, available, *, allow_in_vitro_gap_filling=False):
    def matching(atom, complex_functions=()):
        for record in available:
            # Named exemplars identify independently curated roles. A broad
            # PANTHER SF0 or ATPase activity is deliberately not a role classifier.
            if record['accession'] not in atom.uniprots:
                continue
            if not set(atom.family_ids) <= record['identifiers']:
                continue
            if not set(atom.domain_ids) <= record['identifiers']:
                continue
            if not set(atom.function_ids) <= record['enabled']:
                continue
            if not set(complex_functions) <= record['contributes']:
                continue
            yield record

    def predicate(atom):
        annoton = annotons[atom.node_id]
        if atom.node_id == 'bacillus_gap_filling_activity' and not allow_in_vitro_gap_filling:
            return False
        participant = annoton.get('participant', {})
        if participant.get('selector_type') == 'PROTEIN_COMPLEX':
            units = participant['protein_complex'].get('active_units', [])
            assert units, atom.node_id
            candidates = [list(matching(_atom_from_annoton(unit), atom.function_ids)) for unit in units]
            return any(len({r['accession'] for r in assignment}) == len(units)
                       and len({r['taxon'] for r in assignment}) == 1
                       for assignment in itertools.product(*candidates))
        candidates = list(matching(atom))
        if atom.node_id in {'dnac_helicase_loading_activity', 'dcia_helicase_loading_activity'}:
            return any('replicative DNA helicase loader activity' in r['proposed'] for r in candidates)
        if atom.node_id in {'dnae_php_proofreading', 'polc_proofreading'}:
            # Both functions must be borne by one physical protein record, not
            # supplied by two synthetic split-function copies with the same id.
            return any({'GO:0003887', 'GO:0008296'} <= r['enabled'] for r in candidates)
        if atom.node_id == 'hold_accessory':
            return any('GO:0003689' in r['contributes'] for r in candidates)
        return bool(candidates)
    return predicate


def evaluate(node, annotons, available, **kwargs):
    # Do not combine one organism's origin, another's loader and a third's
    # polymerase to infer a complete native implementation.
    return any(is_satisfied(compile_node(node), oracle(annotons, [r for r in available if r['taxon'] == taxon], **kwargs))
               for taxon in {r['taxon'] for r in available})


def capacity(doc, panel):
    nodes, annotons = index_nodes(doc['module'])
    cases = []
    def check(name, node, members, expected, *, masks=(), in_vitro=False, synthetic=(), drop_proposals=False):
        available = [deepcopy(panel[m]) for m in members] + deepcopy(list(synthetic))
        for record in available:
            record['enabled'].difference_update(masks)
            record['contributes'].difference_update(masks)
            if drop_proposals:
                record['proposed'].clear()
        actual = evaluate(nodes[node], annotons, available, allow_in_vitro_gap_filling=in_vitro)
        cases.append({'case': name, 'node': node, 'members': members,
                      'masked_functions': list(masks), 'allow_in_vitro_gap_filling': in_vitro,
                      'synthetic_controls': [r['accession'] for r in synthetic],
                      'removed_proposed_activity': drop_proposals,
                      'expected': expected, 'observed': actual})
    ecoli = [k for k in panel if k.startswith('ECOLI/')]
    check('E. coli covers every represented required role', SLUG, ecoli, True)
    for gene in ['dnaA','dnaB','dnaC','dnaG','dnaE','dnaQ','dnaX','dnaN','holA','holB','ssb','ligA','polA','gyrA','gyrB','parC','parE']:
        check('Required role lost without E. coli '+gene, SLUG, [k for k in ecoli if k != 'ECOLI/'+gene], False)
    check('Minimal role coverage does not require optional HolC', SLUG, [k for k in ecoli if k != 'ECOLI/holC'], True)
    for org in ['PSEPK','BACSU','MYCTU','VIBCH']:
        check(org+' incomplete panel is unresolved, not pathway absence', SLUG, [k for k in panel if k.startswith(org+'/')], False)
    check('Different species cannot repair missing E. coli polymerase role', SLUG,
          [k for k in ecoli if k!='ECOLI/dnaE']+['PSEPK/dnaEA'], False)
    for node, genes in [('dnac_helicase_loading',['ECOLI/dnaC']),('dcia_helicase_loading',['VIBCH/dciA']),('bacillus_helicase_loading',['BACSU/dnaD','BACSU/dnaB','BACSU/dnaI'])]:
        check(node+' supported implementation',node,genes,True)
        for g in genes:
            check(node+' missing '+g,node,[x for x in genes if x!=g],False)
    check('DnaC name does not equate Bacillus helicase and E. coli loader','dnac_helicase_loading',['BACSU/dnaC'],False)
    check('DnaB name does not equate accessory and helicase','fork_unwinding_protection',['BACSU/dnaB','BACSU/ssbA'],False)
    for node,gene in [('dnac_helicase_loading','ECOLI/dnaC'),('dcia_helicase_loading','VIBCH/dciA')]:
        check('Loader identity without reviewed loader activity '+node,node,[gene],False,drop_proposals=True)
    for org in ['ECOLI','PSEPK','BACSU']:
        genes=[org+'/'+g for g in ['dnaX','holA','holB']]
        check(org+' assembled minimal clamp loader','clamp_loader_activity',genes,True)
        for g in genes:
            check(org+' incomplete loader without '+g,'clamp_loader_activity',[x for x in genes if x!=g],False)
        check(org+' loader needs reviewed contributions','clamp_loader_activity',genes,False,masks=['GO:0003689'])
    check('Cross-species loader subunits do not assemble by assertion','clamp_loader_activity',['ECOLI/dnaX','PSEPK/holA','BACSU/holB'],False)
    check('DnaE1 plus epsilon','dnae_dnaq_synthesis',['ECOLI/dnaE','ECOLI/dnaQ'],True)
    check('Bacillus DnaE3 cannot substitute for DnaE1','dnae_dnaq_synthesis',['BACSU/dnaE','ECOLI/dnaQ'],False)
    compatible_epsilon=deepcopy(panel['ECOLI/dnaQ'])
    compatible_epsilon['taxon']=panel['BACSU/dnaE']['taxon']
    check('DnaE3 still fails DnaE1 role after removing taxon confound','dnae_dnaq_synthesis',['BACSU/dnaE'],False,synthetic=[compatible_epsilon])
    check('Active PHP DnaE1 supports fused implementation','dnae_php_synthesis',['MYCTU/dnaE1'],True)
    check('PHP polymerase needs measured proofreading','dnae_php_synthesis',['MYCTU/dnaE1'],False,masks=['GO:0008296'])
    check('PHP domain on E. coli alpha is not active PHP proofreader','dnae_php_synthesis',['ECOLI/dnaE'],False)
    check('Bacillus dual polymerase implementation','polc_dnae3_synthesis',['BACSU/polC','BACSU/dnaE'],True)
    for g in ['BACSU/polC','BACSU/dnaE']:
        check('Dual polymerase missing '+g,'polc_dnae3_synthesis',[x for x in ['BACSU/polC','BACSU/dnaE'] if x!=g],False)
    check('PolC proofreading is necessary','polc_dnae3_synthesis',['BACSU/polC','BACSU/dnaE'],False,masks=['GO:0008296'])
    for node,key in [('dnae_php_synthesis','MYCTU/dnaE1'),('polc_dnae3_synthesis','BACSU/polC')]:
        p,q=deepcopy(panel[key]),deepcopy(panel[key])
        p['enabled'].discard('GO:0008296')
        q['enabled'].discard('GO:0003887')
        check('Fused activities cannot be pooled across split proteins '+node,node,[] if key.startswith('MYCTU') else ['BACSU/dnaE'],False,synthetic=[p,q])
    fake=deepcopy(panel['ECOLI/dnaE'])
    fake['accession']='synthetic_same_family_polymerase'
    check('Family and chemistry alone do not establish replicative role','dnae_dnaq_synthesis',['ECOLI/dnaQ'],False,synthetic=[fake])
    check('E. coli PolA removal and replacement','rna_primer_removal',['ECOLI/polA'],True)
    check('E. coli gap filling','dna_gap_filling',['ECOLI/polA'],True)
    check('FenA can remove primer flaps','rna_primer_removal',['BACSU/fenA'],True)
    check('RNase HIII with PolA alternative','rna_primer_removal',['BACSU/rnhC','BACSU/polA'],True)
    for g in ['BACSU/rnhC','BACSU/polA']:
        check('RNase HIII route missing '+g,'bacillus_rnhc_pola_removal',[x for x in ['BACSU/rnhC','BACSU/polA'] if x!=g],False)
    check('Bacillus native gap-filler assignment unresolved','dna_gap_filling',['BACSU/polA'],False)
    check('Bacillus measured in-vitro PolA capacity','dna_gap_filling',['BACSU/polA'],True,in_vitro=True)
    check('PolC gap filling is not established by polymerase activity','dna_gap_filling',['BACSU/polC'],False,in_vitro=True)
    for node,genes in [('torsional_stress_relief',['ECOLI/gyrA','ECOLI/gyrB']),('daughter_dna_unlinking',['ECOLI/parC','ECOLI/parE'])]:
        check(node+' assembled complex',node,genes,True)
        for g in genes:
            check(node+' isolated '+g,node,[g],False)
        check(node+' cannot use ATPase without strand-passage contribution',node,genes,False,masks=['GO:0003918'])
    check('Gyrase family alone does not establish E. coli decatenation role','daughter_dna_unlinking',['ECOLI/gyrA','ECOLI/gyrB'],False)
    check('TopoIV family alone does not establish gyrase torsional role','torsional_stress_relief',['ECOLI/parC','ECOLI/parE'],False)
    for node in ['torsional_stress_relief','daughter_dna_unlinking']:
        genes=['MYCTU/gyrA','MYCTU/gyrB']
        check('H37Rv gyrase experimentally supports '+node,node,genes,True)
        for g in genes:
            check('H37Rv isolated subunit lacks '+node,node,[g],False)
        check('H37Rv intrinsic ATPase cannot substitute for '+node,node,genes,False,masks=['GO:0003918'])
        check('Cross-species GyrA/B mixture cannot supply '+node,node,['ECOLI/gyrA','MYCTU/gyrB'],False)
    check('H37Rv gyrase not assigned by arbitrary family members','myctu_gyrase_decatenation',['ECOLI/gyrA','ECOLI/gyrB'],False)
    check('Measured decatenation does not equate unrelated type-II complexes','myctu_gyrase_decatenation',['ECOLI/parC','ECOLI/parE'],False)
    check('Tau scaffolding is not generic DnaX ATPase','tau_coupling',['ECOLI/dnaX'],False,masks=['GO:0140378'])
    return cases


def main():
    baseline = read(AUDIT / 'seed-baseline.yaml')
    doc = read(ROOT / 'modules' / (SLUG+'.yaml'))
    required = {'dnaa_origin_initiation','replicative_helicase_loading','fork_unwinding_protection',
                'dnag_priming','replicative_synthesis_proofreading','clamp_loader_activity',
                'dnan_processivity','rna_primer_removal','dna_gap_filling','ligation',
                'torsional_stress_relief','daughter_dna_unlinking'}
    assert {p['node']['id'] for p in doc['module']['parts'] if not p.get('optional')} == required
    integration = preservation(baseline)
    panel = records(baseline)
    cases = capacity(doc, panel)
    failures = [c for c in cases if c['expected'] != c['observed']]
    (AUDIT/'integration-checks.yaml').write_text(yaml.safe_dump(integration,sort_keys=False,width=100))
    (AUDIT/'capacity-results.yaml').write_text(yaml.safe_dump({'status':'FAIL' if failures else 'PASS','cases':cases,'limitations':__doc__},sort_keys=False,width=100))
    print(json.dumps({k:v for k,v in integration.items() if k!='review_sha256'},indent=2))
    print(f'{len(cases)} capacity cases; {len(failures)} failures')
    for case in failures:
        print(json.dumps(case))
    assert not failures

if __name__=='__main__':
    main()
