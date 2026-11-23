"""Check frozen member payloads and evidence-qualified COS module capacity.

The production compiler supplies topology. This panel oracle supplies curated
subunit identity, cargo evidence and explicit whole-cell physiological evidence.
False means insufficient evidence in this panel, not biological absence. No
cross-species assembly or generic transporter-to-cargo inference is performed.
"""
from collections import Counter
from copy import deepcopy
import hashlib
from pathlib import Path
import re

import yaml
from ai_gene_review.module_logic import compile_node, is_satisfied, _atom_from_annoton

ROOT = Path(__file__).resolve().parents[2]
SLUG = 'bacterial_choline_o_sulfate_uptake_and_desulfation'
AUDIT = ROOT / 'analysis/module_audits' / SLUG


def read(path):
    return yaml.safe_load(path.read_text())


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def main():
    baseline = read(AUDIT / 'seed-baseline.yaml')
    doc = read(ROOT / 'modules' / (SLUG + '.yaml'))
    panel, totals, actions, hashes = {}, Counter(), Counter(), {}
    withdrawn = read(ROOT / 'genes/RUEPO/SPO1087/SPO1087-source-analysis/prior-choline-transport-proposal.yaml')
    assert withdrawn['review_path'] == 'genes/RUEPO/SPO1087/SPO1087-ai-review.yaml'
    assert withdrawn['accession'] == 'Q5LUG7'
    assert withdrawn['original_row']['review']['action'] == 'NEW'
    withdrawn_payload = {k: v for k, v in withdrawn['original_row'].items() if k != 'review'}
    assert withdrawn_payload == {
        'term': {'id': 'GO:0015220', 'label': 'choline transmembrane transporter activity'},
        'evidence_type': 'IMP', 'original_reference_id': 'PMID:26058574'}
    for member in baseline['members']:
        path = ROOT / member['review_path']
        review = read(path)
        assert review['status'] == 'COMPLETE'
        assert review['id'] == member['accession']
        assert review['taxon'] == member['taxon']
        rows = review.get('existing_annotations', [])
        if member['review_path'] == withdrawn['review_path']:
            assert not any({k: v for k, v in row.items() if k != 'review'} == withdrawn_payload
                           for row in rows), 'The withdrawn cargo proposal must not remain asserted'
            totals['withdrawn_authored_proposals'] += 1
        seeds = member['annotations']
        assert len(rows) >= len(seeds)
        for seed, row in zip(seeds, rows):
            assert {k: v for k, v in row.items() if k != 'review'} == seed['payload']
            if seed['prior_action'] == 'NEW':
                assert row['review']['action'] == 'NEW'
                totals['inherited_NEW'] += 1
            else:
                totals['machine_rows_preserved'] += 1
        for row in rows[len(seeds):]:
            assert row['review']['action'] == 'NEW'
            totals['genuinely_added_NEW'] += 1
        for row in rows:
            assert row['review']['action'] != 'PENDING'
            actions[row['review']['action']] += 1
        totals.update(complete_reviews=1, historical_rows=len(seeds), current_rows=len(rows))
        for name, digest in member['raw_sha256'].items():
            assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
            totals['raw_sources_preserved'] += 1
        hashes[member['review_path']] = hashlib.sha256(path.read_bytes()).hexdigest()
        raw = path.with_name(member['gene'] + '-uniprot.txt').read_text()
        families = set()
        for db, ident in re.findall(r'^DR\s+(PANTHER|InterPro|NCBIfam|Pfam); ([^;]+);', raw, re.M):
            families.add(db + ':' + ident)
            if db == 'PANTHER':
                families.add('PANTHER:' + ident.split(':')[0])
        enabled, contributes = set(), set()
        for row in rows:
            if 'NOT' in row.get('qualifier', ''):
                continue
            decision = row['review']
            qualifier = row.get('qualifier', 'enables')
            corrections = {defect['corrected_value'] for defect in decision.get('source_defects', [])
                           if defect['defect_type'] == 'WRONG_QUALIFIER'
                           and defect.get('asserted_value') == qualifier}
            if corrections:
                assert corrections == {'contributes_to'} and qualifier == 'enables'
                qualifier = 'contributes_to'
            target = contributes if qualifier == 'contributes_to' else enabled
            if decision['action'] in {'ACCEPT', 'NEW', 'KEEP_AS_NON_CORE'}:
                target.add(row['term']['id'])
            elif decision['action'] == 'MODIFY':
                target.update(t['id'] for t in decision.get('proposed_replacement_terms', []))
        for core in review.get('core_functions', []):
            for slot, target in [('molecular_function', enabled), ('contributes_to_molecular_function', contributes)]:
                if core.get(slot):
                    target.add(core[slot]['id'])
        panel[review['id']] = dict(accession=review['id'], families=families,
                                   enabled=enabled, contributes=contributes)
    providers = read(AUDIT / 'provider-source-preservation.yaml')['sha256']
    for name, digest in providers.items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    totals['provider_artifacts_preserved'] = len(providers)
    assert totals['withdrawn_authored_proposals'] == 1
    assert totals['genuinely_added_NEW'] == 11
    assert 'GO:0015220' not in panel['Q5LUG7']['enabled']
    assert 'GO:0031459' not in panel['O34992']['enabled']
    assert 'GO:0031459' in panel['O34992']['contributes']
    assert not {'GO:0031459', 'GO:0033266'} & panel['O32243']['enabled']
    assert {'GO:0031459', 'GO:0033266'} <= panel['O32243']['contributes']
    nodes = {n['id']: n for n in walk(doc['module']) if 'id' in n}
    representatives = {n['id'].split(':', 1)[1] for n in walk(doc['module'])
                       if str(n.get('id', '')).startswith('UniProtKB:')}
    assert representatives == set(panel)
    opuc = {'O34992', 'O34878', 'O32243', 'O34742'}
    complex_node = nodes['opuc_cos_transport']
    assert {x['term']['id'] for x in complex_node['function']['cargo']} == {'CHEBI:16822'}
    assert any(x['source_id'] == 'PMID:9925583' for x in complex_node['evidence'])
    unknown = nodes['unresolved_cos_import_activity']
    assert unknown['participant']['selector_type'] == 'ANY_WITH_FUNCTION'
    assert {x['source_id'] for x in unknown['evidence']} == {'PMID:17116241'}
    units = complex_node['participant']['protein_complex']['active_units']
    assert len(units) == 4
    cases = []

    def check(name, node, present, expected, *, opuc_cargo=True, physiology=None,
              drop_roles=(), masks=(), synthetic=()):
        records = [deepcopy(panel[x]) for x in present] + list(deepcopy(synthetic))
        for record in records:
            record['enabled'].difference_update(masks)
        def match(atom, *, functions=True):
            # Representative membership is the independently curated role gate.
            # Family identity alone cannot assign OpuC versus related OpuB roles.
            for record in records:
                if record['accession'] in drop_roles or record['accession'] not in atom.uniprots:
                    continue
                if not set(atom.family_ids) <= record['families']:
                    continue
                if not set(atom.domain_ids) <= record['families']:
                    continue
                if functions and not set(atom.function_ids) <= record['enabled']:
                    continue
                return True
            return False
        def predicate(atom):
            if atom.node_id == 'ruegeria_bett_candidate':
                # Verified locus/family plausibility is not evidence that this
                # protein transports the proposed cargo; the insertion phenotype
                # remains confounded by downstream betA polarity.
                return False
            if atom.node_id == 'unresolved_cos_import_activity':
                # Only direct intact-accumulation physiology is admitted. COS
                # growth alone cannot distinguish transport from external cleavage.
                return (physiology == 'KT2440 intact COS accumulation; PMID:17116241'
                        and bool(present) and set(present) <= {'Q88RQ2', 'Q88RQ3', 'Q88RQ4'})
            if atom.node_id == 'opuc_cos_transport':
                return opuc_cargo and all(match(_atom_from_annoton(unit)) for unit in units)
            return match(atom)
        observed = is_satisfied(compile_node(nodes[node]), predicate)
        assert observed == expected, (name, expected, observed)
        cases.append(dict(case=name, node=node, present=sorted(present), expected=expected,
                          observed=observed, opuc_cargo_evidence=opuc_cargo,
                          physiology=physiology, dropped_curated_roles=list(drop_roles),
                          masked_functions=list(masks), synthetic_accessions=[r['accession'] for r in synthetic]))

    uptake, hydrolysis = 'choline_o_sulfate_import', 'betc_choline_o_sulfate_hydrolysis'
    check('Assembled Bacillus OpuC imports intact COS', uptake, opuc, True)
    check('Bacillus import-only panel does not close hydrolysis', SLUG, opuc, False)
    check('OpuC families without documented COS cargo are insufficient', uptake, opuc, False, opuc_cargo=False)
    for accession in sorted(opuc):
        check('OpuC missing subunit ' + accession, uptake, opuc - {accession}, False)
        check('OpuC family match without curated role ' + accession, uptake, opuc, False, drop_roles=(accession,))
        check('Individual OpuC subunit cannot import independently ' + accession, uptake, {accession}, False)
    # Synthetic same-family ATPase control is not an invented biological member.
    fake = deepcopy(panel['O34992'])
    fake['accession'] = 'SYNTHETIC_SAME_FAMILY_ATPASE'
    check('Related-family ATPase cannot replace the OpuCA role', uptake,
          opuc - {'O34992'}, False, synthetic=(fake,))
    for accession in ['Q88RQ2', 'O69787', 'Q5LUH1']:
        check('Supported BetC hydrolysis ' + accession, hydrolysis, {accession}, True)
        check('BetC alone cannot establish intact import ' + accession, SLUG, {accession}, False)
        check('Family alone without reviewed catalytic function ' + accession, hydrolysis,
              {accession}, False, masks=('GO:0047753',))
    psepk = {'Q88RQ2', 'Q88RQ3', 'Q88RQ4'}
    check('KT2440 gene panel leaves importer unresolved', SLUG, psepk, False)
    check('BetD and BetE candidate pair is not a demonstrated COS importer', uptake,
          {'Q88RQ3', 'Q88RQ4'}, False)
    check('KT2440 physiology plus BetC establishes the two roles', SLUG, psepk, True,
          physiology='KT2440 intact COS accumulation; PMID:17116241')
    check('Physiological uptake does not substitute for BetC hydrolysis', SLUG,
          {'Q88RQ3', 'Q88RQ4'}, False, physiology='KT2440 intact COS accumulation; PMID:17116241')
    check('Ruegeria BetT candidate does not establish COS import', uptake, {'Q5LUG7'}, False)
    check('Ruegeria locus and family evidence do not resolve choline cargo',
          'ruegeria_bett_candidate_context', {'Q5LUG7'}, False)
    check('Ruegeria utilization does not establish intact intracellular uptake', SLUG,
          {'Q5LUH1', 'Q5LUG7'}, False, physiology='Ruegeria COS growth; PMID:26058574')
    check('KT2440 physiology cannot be transferred to Ruegeria', SLUG,
          {'Q5LUH1', 'Q5LUG7'}, False,
          physiology='KT2440 intact COS accumulation; PMID:17116241')
    check('Mixed-lineage inventory cannot inherit KT2440 physiological uptake', SLUG,
          {'Q88RQ4', 'Q5LUH1'}, False,
          physiology='KT2440 intact COS accumulation; PMID:17116241')
    (AUDIT / 'integration-checks.yaml').write_text(yaml.safe_dump(dict(status='PASS', **dict(totals),
        actions=dict(actions), review_sha256=hashes, scope='Frozen ten-member panel; original payloads, raw and provider sources preserved.'), sort_keys=False))
    (AUDIT / 'capacity-results.yaml').write_text(yaml.safe_dump(dict(status='PASS', case_count=len(cases),
        semantics='Production topology with explicit role/cargo/physiology oracle. False denotes unresolved panel coverage, not absence. No synthetic cross-species assembly claim.', cases=cases), sort_keys=False))
    print(dict(totals), 'capacity cases', len(cases), 'PASS')


if __name__ == '__main__':
    main()
