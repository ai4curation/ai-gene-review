"""Exercise production module wiring against explicit, source-based reaction inputs.

This is an evidence-panel check, not a proteome scan or native-flux prediction.
The reaction assignments below are manual judgments from curated UniProt and
the named literature; review actions are deliberately not the activity oracle.
"""
from pathlib import Path
import copy
import hashlib
import re

import yaml
from ai_gene_review.module_logic import compile_module, is_satisfied, iter_atoms

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / 'analysis/module_audits/bacterial_glutamate_to_p5c_biosynthesis'
KINASE = 'GO:0004349'
REDUCTASE = 'GO:0004350'
FAMILY_K = 'PANTHER:PTHR43654'
FAMILY_R = 'PANTHER:PTHR11063'


def main():
    doc = yaml.safe_load((ROOT / 'modules/bacterial_glutamate_to_p5c_biosynthesis.yaml').read_text())
    circuit = compile_module(doc)
    atoms = {a.node_id: a for a in iter_atoms(circuit)}
    assert len(atoms) == 2
    assert {a.function_ids for a in atoms.values()} == {(KINASE,), (REDUCTASE,)}
    for part in doc['module']['parts']:
        for ann in part['node']['annotons']:
            required = ann['participant']['required_function']
            for key in ['term', 'substrates', 'products']:
                assert required[key] == ann['function'][key]
    evidence = yaml.safe_load((AUDIT / 'coverage-evidence.yaml').read_text())
    proteins = {}
    source_hashes = {}
    for row in evidence['proteins']:
        p = ROOT / row['source']
        text = p.read_text()
        source_hashes[row['source']] = hashlib.sha256(p.read_bytes()).hexdigest()
        families = {'PANTHER:' + x for x in re.findall(r'^DR   PANTHER; ([^;]+);', text, re.M)}
        assert row['accession'] in re.search(r'^AC   (.+)$', text, re.M).group(1)
        proteins[row['accession']] = {**row, 'families': families}

    def matches(atom, protein, require_function=True):
        return bool(set(atom.family_ids) & protein['families']) and (
            not require_function or bool(set(atom.function_ids) & set(protein['functions'])))

    def covered(ids, require_system=True, require_bacteria=True, require_split=True,
                require_function=True, extra=None):
        pool = dict(proteins)
        pool.update(extra or {})
        rows = [pool[x] for x in ids]
        if require_bacteria:
            rows = [r for r in rows if r['domain'] == 'Bacteria']
        systems = {r['system'] for r in rows} if require_system else {'synthetic'}
        for system in systems:
            subset = [r for r in rows if not require_system or r['system'] == system]
            if not is_satisfied(circuit, lambda a: any(matches(a, r, require_function) for r in subset)):
                continue
            if require_split:
                kinase = [r for r in subset if KINASE in r['functions'] and FAMILY_K in r['families']]
                reductase = [r for r in subset if REDUCTASE in r['functions'] and FAMILY_R in r['families']]
                if not any(k['accession'] != r['accession'] for k in kinase for r in reductase):
                    continue
            return True
        return False

    cases = []

    def check(name, result, expected, scope):
        assert result == expected, (name, result, expected)
        cases.append({'case': name, 'actual': result, 'expected': expected, 'scope': scope})

    panels = [(['P0A7B5', 'P07004'], 'E. coli K12'),
              (['Q88Q07', 'Q88DL4'], 'P. putida KT2440 inferred chemistry'),
              (['P39820', 'P39821'], 'B. subtilis168 anabolic reference pair'),
              (['O07509', 'P39821'], 'B. subtilis168 alternative ProJ kinase pair'),
              (['P0C1E2', 'P0C1E0'], 'C. glutamicum13032 inferred reference pair')]
    for ids, name in panels:
        check(name, covered(ids), True, 'Reaction coverage at the stated evidence level; not an exact-strain flux measurement.')
        for remove in ids:
            check(name + ' without ' + remove, covered([x for x in ids if x != remove]), False,
                  'Missing witness in this panel, not a biological knockout or absence claim.')
    check('empty panel', covered([]), False, 'Both chemical steps require a witness.')
    check('cross-strain stitching rejected', covered(['P0A7B5', 'Q88DL4']), False, 'An organism-level claim cannot combine two organisms.')
    check('system-gate removal exposes synthetic coverage', covered(['P0A7B5', 'Q88DL4'], require_system=False), True,
          'Explicitly synthetic control; the production circuit itself does not enforce strain identity.')
    check('fungal split pair excluded', covered(['P32264', 'P54885']), False, 'The reaction exists outside the module taxon.')
    check('taxon-gate removal admits fungal chemistry', covered(['P32264', 'P54885'], require_bacteria=False), True,
          'Same chemistry does not make yeast a bacterial exemplar.')
    kinase_atom = next(a for a in atoms.values() if KINASE in a.function_ids)
    check('IPK family alone insufficient', matches(kinase_atom, proteins['Q8H1F7']), False,
          'Curated isopentenyl-phosphate kinase activity is not glutamate phosphorylation.')
    check('activity-gate removal exposes IPK family false positive', matches(kinase_atom, proteins['Q8H1F7'], False), True,
          'PANTHER family membership is not an assay for the required reaction.')
    fused = copy.deepcopy(proteins['P0A7B5'])
    fused.update(accession='synthetic_fusion', functions=[KINASE, REDUCTASE], families={FAMILY_K, FAMILY_R})
    check('synthetic dual-domain fusion excluded', covered(['synthetic_fusion'], extra={'synthetic_fusion': fused}), False,
          'Counterfactual dual-family protein is one polypeptide, outside split architecture.')
    check('split-gate removal admits synthetic fusion', covered(['synthetic_fusion'], require_split=False, extra={'synthetic_fusion': fused}), True,
          'Architecture is supplied by this checker; free-text module notes do not enforce it in the compiler.')
    for acc, protein in proteins.items():
        if protein['domain'] != 'Bacteria':
            continue
        for atom in atoms.values():
            if set(atom.function_ids) & set(protein['functions']):
                check('individual reaction ' + acc, matches(atom, protein), True, protein['evidence_scope'])
    result = {'status':'PASS', 'cases':cases, 'source_sha256':source_hashes,
              'limits':[evidence['interpretation'],
                        'The production circuit does not enforce taxon, same-system or distinct-polypeptide identity; the explicit external gates do.',
                        'Curation actions and RNA-binding judgments are not used to create positive catalytic evidence.',
                        'A panel failure cannot establish a missing genomic pathway, especially where a bypass is known.']}
    (AUDIT / 'coverage-results.yaml').write_text(yaml.safe_dump(result,sort_keys=False,width=100))
    print(f'{len(cases)} coverage and boundary cases passed')


if __name__ == '__main__':
    main()
