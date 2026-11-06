"""Verify reviewed-panel preservation and choline/betaine pathway coverage.

The production compiler supplies topology; the oracle supplies reviewed activity,
family and subunit roles. False is incomplete evidence in this panel, not biological
absence. Synthetic controls are explicit and do not assert native compatibility.
"""
from collections import Counter
from copy import deepcopy
import hashlib
from pathlib import Path
import re

import yaml
from ai_gene_review.module_logic import compile_node, is_satisfied, _atom_from_annoton

ROOT = Path(__file__).resolve().parents[2]
SLUG = 'bacterial_choline_to_glycine_betaine_biosynthesis'
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
    for member in baseline['members']:
        path = ROOT / member['review_path']
        review = read(path)
        assert review['status'] == 'COMPLETE'
        assert review['id'] == member['accession']
        assert review['taxon'] == member['taxon']
        rows = review.get('existing_annotations', [])
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
            target = contributes if row.get('qualifier') == 'contributes_to' else enabled
            decision = row['review']
            if decision['action'] in {'ACCEPT', 'NEW', 'KEEP_AS_NON_CORE'}:
                target.add(row['term']['id'])
            elif decision['action'] == 'MODIFY':
                target.update(t['id'] for t in decision.get('proposed_replacement_terms', []))
        for core in review.get('core_functions', []):
            for slot, target in [('molecular_function', enabled), ('contributes_to_molecular_function', contributes)]:
                if core.get(slot):
                    target.add(core[slot]['id'])
        panel[review['id']] = dict(accession=review['id'], families=families,
                                   enabled=enabled, contributes=contributes,
                                   bacterial=bool(re.search(r'^OC   Bacteria;', raw, re.M)))
    providers = read(AUDIT / 'provider-source-preservation.yaml')['sha256']
    for name, digest in providers.items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    totals['provider_artifacts_preserved'] = len(providers)
    nodes = {n['id']: n for n in walk(doc['module']) if 'id' in n}
    reps = {n['id'].split(':', 1)[1] for n in walk(doc['module'])
            if str(n.get('id', '')).startswith('UniProtKB:')}
    assert reps <= set(panel)
    assert set(panel) - reps == {'Q88CW9'}, 'BetT-I is the explicitly unresolved comparator'
    assert all(r['bacterial'] for r in panel.values())
    units = nodes['opub_transport_activity']['participant']['protein_complex']['active_units']
    assert len(units) == 4
    scoped = read(AUDIT / 'curated-substrate-capabilities.yaml')
    scope_key = lambda item: tuple(item[k] for k in ['function', 'substrate', 'acceptor'])
    requirements = {}
    for ident, required in scoped['required_scopes'].items():
        annoton = nodes[ident]
        assert required['function'] == annoton['function']['term']['id']
        substrates = {x['preferred_term'] for x in annoton['function']['substrates']}
        assert {required['substrate'], required['acceptor']} <= substrates
        requirements[ident] = scope_key(required)
    for record in panel.values():
        record['scoped_activities'] = set()
    for accession, entry in scoped['members'].items():
        gene = read(ROOT / entry['review_path'])
        assert gene['id'] == accession
        for activity in entry['scopes']:
            cores = [c for c in gene['core_functions']
                     if c.get('molecular_function', {}).get('id') == activity['function']]
            assert cores
            sources = {x['reference_id'] for c in cores for x in c.get('supported_by', [])}
            assert set(activity['references']) <= sources
            panel[accession]['scoped_activities'].add(scope_key(activity))
    opub = {'Q45460', 'Q45461', 'Q45462', 'P39775'}
    cases = []

    def check(name, node, present, expected, *, masks=(), drop_roles=(),
              family_scan=False, synthetic=(), enforce_taxon=True):
        available = [deepcopy(panel[x]) for x in present] + list(deepcopy(synthetic))
        for record in available:
            record['enabled'].difference_update(masks)
            record['contributes'].difference_update(masks)
        def match(atom, complex_functions=()):
            for record in available:
                if enforce_taxon and not record['bacterial']:
                    continue
                if atom.node_id in requirements and requirements[atom.node_id] not in record['scoped_activities']:
                    continue
                if record['accession'] in drop_roles:
                    continue
                if not family_scan or not atom.family_ids:
                    if record['accession'] not in atom.uniprots:
                        continue
                if not set(atom.family_ids) <= record['families']:
                    continue
                if not set(atom.domain_ids) <= record['families']:
                    continue
                if not set(atom.function_ids) <= record['enabled']:
                    continue
                if not set(complex_functions) <= record['enabled'] | record['contributes']:
                    continue
                return True
            return False
        def predicate(atom):
            if atom.node_id == 'opub_transport_activity':
                # Complex subunit identity is independently curated. Scanning a
                # broad family does not license arbitrary OpuB/OpuC substitutions.
                assert not family_scan
                return all(match(_atom_from_annoton(unit), atom.function_ids) for unit in units)
            return match(atom)
        actual = is_satisfied(compile_node(nodes[node]), predicate)
        assert actual == expected, (name, expected, actual)
        cases.append(dict(case=name, node=node, present=sorted(present), expected=expected,
                          observed=actual, masked_functions=list(masks),
                          dropped_roles=list(drop_roles), family_scan=family_scan,
                          taxon_oracle=enforce_taxon,
                          synthetic_controls=[x['accession'] for x in synthetic]))

    root, uptake, oxidation = SLUG, 'choline_import', 'choline_to_betaine_oxidation'
    ecoli = {'P0ABC9', 'P17444', 'P17445'}
    bacillus = opub | {'P71016', 'P71017'}
    check('Ecoli characterized uptake and synthesis inventory', root, ecoli, True)
    for accession in sorted(ecoli):
        check('Ecoli missing required role ' + accession, root, ecoli - {accession}, False)
    check('Ecoli oxidation without import', oxidation, {'P17444', 'P17445'}, True)
    check('Ecoli BetA alone does not supply both oxidation steps', oxidation, {'P17444'}, False)
    check('BetB alone lacks first oxidation', oxidation, {'P17445'}, False)
    check('Bacillus OpuB GbsAB complete inventory', root, bacillus, True)
    for accession in sorted(bacillus):
        check('Bacillus missing required component ' + accession, root, bacillus - {accession}, False)
    check('Bacillus GbsAB supplies oxidative segment', oxidation, {'P71016', 'P71017'}, True)
    check('Bacillus GbsB alone does not demonstrate aldehyde oxidation', oxidation, {'P71017'}, False)
    check('GbsA alone lacks first oxidation', oxidation, {'P71016'}, False)
    check('Four OpuB subunit types supply import', uptake, opub, True)
    check('OpuB import does not imply synthesis', root, opub, False)
    for accession in sorted(opub):
        check('Single OpuB unit cannot import ' + accession, uptake, {accession}, False)
        check('Family identity without curated OpuB role ' + accession, uptake,
              opub, False, drop_roles=(accession,))
    check('OpuB requires independently supported choline activity', uptake, opub, False,
          masks=('GO:0033266',))
    check('KT2440 BetA BetB cover oxidation', oxidation, {'Q88CW6', 'Q88CW7'}, True)
    check('KT2440 locus-associated BetT-I does not resolve uptake', root,
          {'Q88CW9', 'Q88CW6', 'Q88CW7'}, False)
    check('Generic BetT-I transporter does not establish choline specificity', uptake, {'Q88CW9'}, False)
    check('CodA two separately evidenced activities cover oxidation', oxidation, {'Q7X2H8'}, True)
    check('CodA alone does not identify a native importer', root, {'Q7X2H8'}, False)
    check('CodA choline oxidase term alone cannot imply aldehyde oxidation', oxidation,
          {'Q7X2H8'}, False, masks=('GO:0004031',))
    check('CodA aldehyde activity alone cannot imply first oxidation', oxidation,
          {'Q7X2H8'}, False, masks=('GO:0033713',))
    check('NAD BetB activity cannot satisfy oxygen-dependent CodA role',
          'coda_aldehyde_oxidation', {'P17445'}, False)
    check('CodA oxygen chemistry cannot satisfy NAD-dependent BetB role',
          'betb_glycine_betaine_formation', {'Q7X2H8'}, False)
    check('GbsB recognized without GMC family', 'choline_dehydrogenation', {'P71017'}, True)
    check('BetA recognized without typeIII family', 'choline_dehydrogenation', {'P17444'}, True)
    fungal = deepcopy(panel['Q7X2H8']); fungal['accession'] = 'SYNTHETIC_NONBACTERIAL_CODA'; fungal['bacterial'] = False
    check('Family and activity alone do not enforce Bacteria scope', 'coda_complete_oxidation',
          set(), True, family_scan=True, synthetic=(fungal,), enforce_taxon=False)
    check('Taxon oracle excludes nonbacterial same-family activity', 'coda_complete_oxidation',
          set(), False, family_scan=True, synthetic=(fungal,))
    check('Actual CodA supports substrate-qualified family scan', 'coda_complete_oxidation',
          {'Q7X2H8'}, True, family_scan=True)
    generic = deepcopy(panel['Q7X2H8'])
    generic['accession'] = 'SYNTHETIC_GENERIC_ALDEHYDE_OXIDASE'
    generic['scoped_activities'] = set()
    check('Same family and generic GO4031 do not establish betaine-aldehyde oxidation',
          'coda_complete_oxidation', set(), False, family_scan=True, synthetic=(generic,))
    (AUDIT / 'integration-checks.yaml').write_text(yaml.safe_dump(dict(status='PASS', **dict(totals),
        actions=dict(actions), review_sha256=hashes,
        scope='Thirteen reviewed bacterial proteins; BetT-I is an unresolved importer comparator.'), sort_keys=False))
    (AUDIT / 'capacity-results.yaml').write_text(yaml.safe_dump(dict(status='PASS', case_count=len(cases),
        semantics='Production topology with explicit family, reviewed-function, complex-unit and Bacteria-context oracle. Native Ecoli/Bacillus complete-root cases; other panels test component coverage. False does not assert pathway absence.',
        cases=cases), sort_keys=False))
    print(dict(totals), 'capacity cases', len(cases), 'PASS')


if __name__ == '__main__':
    main()
