"""Check production module wiring against independently assessed source chemistry.

The inputs mix direct assays and curated inferences, explicitly labeled in the
evidence file. Passing this panel is not proof of native pathway flux.
"""
from pathlib import Path
import hashlib
import re
import yaml
from ai_gene_review.module_logic import compile_module, is_satisfied, iter_atoms

ROOT = Path(__file__).resolve().parents[2]
A = ROOT / 'analysis/module_audits/bacterial_glycerol_uptake_catabolism'
doc = yaml.safe_load((ROOT / 'modules/bacterial_glycerol_uptake_catabolism.yaml').read_text())
circuit = compile_module(doc)
atoms = list(iter_atoms(circuit))
assert len(atoms) == 3
assert {a.function_ids for a in atoms} == {('GO:0015254',), ('GO:0004370',), ('GO:0004368',)}
for part in doc['module']['parts']:
    ann = part['node']['annotons'][0]
    for key in ['term', 'substrates', 'products']:
        assert ann['participant']['required_function'][key] == ann['function'][key]

evidence = yaml.safe_load((A / 'coverage-evidence.yaml').read_text())
proteins, hashes = {}, {}
for row in evidence['proteins']:
    path = ROOT / row['source']
    text = path.read_text()
    assert row['accession'] in re.search(r'^AC   (.+)$', text, re.M).group(1)
    families = {'PANTHER:' + x for x in re.findall(r'^DR   PANTHER; ([^;]+);', text, re.M)}
    proteins[row['accession']] = {**row, 'families': families}
    hashes[row['source']] = hashlib.sha256(path.read_bytes()).hexdigest()

def matches(atom, protein, activity=True, architecture=True):
    return (bool(set(atom.family_ids) & protein['families'])
            and (not activity or bool(set(atom.function_ids) & set(protein['functions'])))
            and (not architecture or protein['architecture'] == 'single_gene_activity'))

def covered(ids, same_system=True, activity=True, architecture=True):
    rows = [proteins[x] for x in ids if proteins[x]['domain'] == 'Bacteria']
    systems = {r['system'] for r in rows} if same_system else {'synthetic'}
    return any(is_satisfied(circuit, lambda a: any(
        matches(a, p, activity, architecture) for p in rows
        if not same_system or p['system'] == system)) for system in systems)

cases = []
def check(name, actual, expected, meaning):
    assert actual == expected, (name, actual, expected)
    cases.append(dict(case=name, actual=actual, expected=expected, interpretation=meaning))

for system in ['ECOLI', 'PSEPK', 'BACSU']:
    panel = [a for a,p in proteins.items() if p['system'] == system and p['architecture'] == 'single_gene_activity']
    check(system+' three-step panel', covered(panel), True, 'Reaction coverage at the documented evidence level, not equal assay depth.')
    for acc in panel:
        check(system+' missing '+acc, covered([p for p in panel if p != acc]), False,
              'A missing panel witness does not imply genomic absence or loss of growth; other uptake/routes may exist.')
check('empty panel', covered([]), False, 'All three steps require witnesses.')
check('cross-strain stitching', covered(['P0AER0','Q88NX8','P18158']), False, 'Do not combine three organisms into one native pathway.')
check('synthetic mixed-species pool', covered(['P0AER0','Q88NX8','P18158'], same_system=False), True,
      'The production circuit does not impose organism identity; the external gate does.')
glpd = next(a for a in atoms if a.function_ids == ('GO:0004368',))
check('same-family oxidase excluded', matches(glpd, proteins['O86963']), False, 'Oxygen/peroxide chemistry is not quinone reduction.')
check('oxidase false positive without activity gate', matches(glpd, proteins['O86963'], activity=False), True,
      'Family membership alone cannot identify the electron acceptor.')
check('isolated GlpA excluded', matches(glpd, proteins['P0A9C0']), False, 'GlpA requires other subunits for the assembled enzyme.')
check('GlpA false positive without architecture gate', matches(glpd, proteins['P0A9C0'], architecture=False), True,
      'The family and quinone reaction alone do not distinguish GlpD from GlpABC.')
check('GlpA cannot complete Ecoli GlpD route', covered(['P0AER0','P0A6F3','P0A9C0']), False,
      'This module models the single-gene GlpD route, not an unrepresented GlpABC assembly.')
for acc,p in proteins.items():
    if p['architecture'] != 'single_gene_activity' or acc == 'O86963':
        continue
    atom = next(a for a in atoms if set(a.function_ids) & set(p['functions']))
    check('individual witness '+acc, matches(atom,p), True, p['evidence_scope'])

result = dict(status='PASS', cases=cases, source_sha256=hashes, limits=[
    evidence['interpretation'],
    'The production compiler carries family/function IDs but does not enforce taxon, same-strain identity, PAINT ancestry or complex architecture; the stated external gates do.',
    'PAINT nodes are curated context, not tested ancestry predicates in this checker.',
    'A required GlpF witness defines this implementation, not all biological glycerol uptake.'])
(A / 'coverage-results.yaml').write_text(yaml.safe_dump(result,sort_keys=False,width=100))
print(f'{len(cases)} coverage and boundary checks passed')
