"""Check module wiring against explicit reaction evidence, not native pathway flux."""
from pathlib import Path
import hashlib
import re
import yaml
from ai_gene_review.module_logic import compile_module, is_satisfied, iter_atoms

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / 'analysis/module_audits/bacterial_gallate_catabolism'
REACTIONS = {
    'galp_outer_membrane_porin': 'GO:0015288',
    'gala_gallate_dioxygenase': 'RHEA:28927',
    'gald_oxalomesaconate_tautomerase': 'RHEA:28931',
    'galb_oxalomesaconate_hydratase': 'RHEA:17401',
    'ligu_oxalomesaconate_isomerase': 'RHEA:58504',
    'ligj_kch_hydratase': 'RHEA:58508',
    'galc_cha_aldolase': 'RHEA:28935',
}


def main():
    doc = yaml.safe_load((ROOT / 'modules/bacterial_gallate_catabolism.yaml').read_text())
    circuit = compile_module(doc)
    atoms = {a.node_id: a for a in iter_atoms(circuit)}
    assert set(atoms) == set(REACTIONS), sorted(atoms)
    def check_chemistry(obj):
        if isinstance(obj, dict):
            for annoton in obj.get('annotons', []):
                function = annoton['function']
                reaction = REACTIONS[annoton['id']]
                if reaction.startswith('RHEA:'):
                    assert reaction in {e['source_id'] for e in function['evidence']}
                    required = annoton['participant']['required_function']
                    assert required['substrates'] == function['substrates']
                    assert required['products'] == function['products']
            for value in obj.values():
                check_chemistry(value)
        elif isinstance(obj, list):
            for value in obj:
                check_chemistry(value)
    check_chemistry(doc['module'])
    evidence = yaml.safe_load((AUDIT / 'coverage-evidence.yaml').read_text())
    proteins = {}
    source_hashes = {}
    for row in evidence['proteins']:
        p = ROOT / row['uniprot_path']
        text = p.read_text()
        families = {db + ':' + acc for db, acc in re.findall(
            r'^DR   (PANTHER|NCBIfam|InterPro); ([^;]+);', text, re.M)}
        proteins[row['accession']] = {**row, 'families': families}
        source_hashes[row['uniprot_path']] = hashlib.sha256(p.read_bytes()).hexdigest()
        review = yaml.safe_load((ROOT / row['review_path']).read_text())
        assert review['id'] == row['accession']

    def matches(node, acc, require_reaction=True):
        row = proteins[acc]
        return bool(set(atoms[node].family_ids) & row['families']) and (
            not require_reaction or REACTIONS[node] in row['reaction_ids'])

    def covered(accessions):
        return is_satisfied(circuit, lambda a: any(matches(a.node_id, x) for x in accessions))

    cases = []
    def check(case, actual, expected, scope):
        assert actual == expected, (case, actual, expected)
        cases.append(dict(case=case, actual=actual, expected=expected, scope=scope))

    pset = ['Q88JX5', 'Q88JY0', 'Q88JX8', 'Q88JX9']
    check('Pseudomonas catalytic panel', covered(pset), True,
          'Catalytic evidence; not parental KT2440 growth without repaired GalT.')
    check('Pseudomonas optional porin', covered(pset + ['Q88JX6']), True,
          'Optional entry must not become an obligatory chemical step.')
    for acc in pset:
        check('Pseudomonas minus ' + acc, covered([x for x in pset if x != acc]), False,
              'Missing curated catalytic witness, not an experimental knockout prediction.')
    composite = ['Q5NTE5', 'Q0KJL4', 'G2IQQ5', 'G2IQQ8']
    check('Synthetic sphingomonad mechanism panel', covered(composite), True,
          'Cross-strain assembly demonstrates wiring only; not one native organism.')
    check('SYK-6 exemplar subset', covered(['Q5NTE5', 'G2IQQ5', 'G2IQQ8']), False,
          'Missing a same-strain LigU exemplar in this panel does not establish biological absence.')
    check('BURL3 partial evidence', covered(['Q39LQ0', 'Q39LQ2', 'Q39LQ3']), False,
          'Native growth does not resolve the isomerase and hydratase intermediates.')
    check('GalD with LigJ mismatch', covered(['Q88JX5', 'Q88JY0', 'G2IQQ5', 'Q88JX9']), False,
          'Enol formation cannot satisfy the KCH-forming reaction.')
    check('LigU with GalB mismatch', covered(['Q88JX5', 'Q0KJL4', 'Q88JX8', 'Q88JX9']), False,
          'KCH formation cannot supply the GalB enol reaction.')
    for node, reaction in REACTIONS.items():
        for acc, row in proteins.items():
            if reaction in row['reaction_ids']:
                check(node + ' / ' + acc, matches(node, acc), True, row['evidence_scope'])
    node = 'ligj_kch_hydratase'
    check('Unresolved BURL3 hydratase rejected', matches(node, 'Q39LQ2'), False,
          'Family and broad hydro-lyase activity do not resolve substrate.')
    check('Family-only mutation exposes false positive', matches(node, 'Q39LQ2', False), True,
          'Negative control demonstrates why an external reaction-specific oracle is required.')
    result = {
        'status': 'PASS', 'cases': cases, 'source_sha256': source_hashes,
        'limits': [evidence['interpretation'],
                   'The production compiler does not enforce reaction substrate identity; this checker supplies that gate explicitly.',
                   'Curation actions are not used as the activity oracle.',
                   'Coverage is neither native flux nor taxonomic absence; the mixed-strain positive is explicitly synthetic.'],
    }
    (AUDIT / 'coverage-results.yaml').write_text(yaml.safe_dump(result, sort_keys=False, width=100))
    print(f'{len(cases)} coverage and boundary cases passed')


if __name__ == '__main__':
    main()
