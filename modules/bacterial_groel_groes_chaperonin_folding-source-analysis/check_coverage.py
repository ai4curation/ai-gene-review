"""Check curated compatible folding pairs against the production module circuit.

The production compiler represents the assembled cage as one atom. This oracle
inspects its active-unit descriptors and requires a literature-supported or
explicitly curated same-system pair. It is not a generic proteome classifier.
"""
from pathlib import Path
import copy, hashlib, json, re
import yaml
from ai_gene_review.module_logic import compile_module, is_satisfied
ROOT=Path(__file__).resolve().parents[2]
M='bacterial_groel_groes_chaperonin_folding'
A=ROOT/'analysis/module_audits'/M
module=yaml.safe_load((ROOT/'modules'/f'{M}.yaml').read_text())
evidence=yaml.safe_load((A/'coverage-evidence.yaml').read_text())
proteins={p['accession']:p for p in evidence['proteins']}
hashes={}
for p in proteins.values():
    path=ROOT/p['source']; text=path.read_text();hashes[p['source']]=hashlib.sha256(path.read_bytes()).hexdigest()
    assert p['accession'] in re.search(r'^AC   (.+)$',text,re.M)[1]
    placements=re.findall(r'^DR   PANTHER; ([^;]+);',text,re.M)
    p['families']={'PANTHER:'+f for v in placements for f in [v,v.split(':')[0]]}
pairs={tuple(p['accessions']) for p in evidence['compatible_pairs']}

def covered(ids,doc=module,require_activity=True,require_pair=True):
    ann=doc['module']['parts'][0]['node']['annotons'][0]
    units=ann['participant']['protein_complex']['active_units']
    def match(unit,p):
        selector=unit['participant'];family=selector['family']['term']['id'];mf=selector['required_function']['term']['id']
        return family in p['families'] and (not require_activity or mf in p['functions'])
    candidates=[[acc for acc in ids if match(u,proteins[acc])] for u in units]
    # The cage requires exactly its two distinct active-unit roles.
    assert len(candidates)==2 and {u['id'] for u in units}=={'groel','groes'}
    good=any((a,b) in pairs or not require_pair for a in candidates[0] for b in candidates[1])
    return is_satisfied(compile_module(doc),lambda a:a.node_id==ann['id'] and good)

cases=[]
def check(name,actual,expected,meaning):
    assert actual==expected,(name,actual,expected)
    cases.append(dict(case=name,actual=actual,expected=expected,interpretation=meaning))
for pair in evidence['compatible_pairs']:
    ids=pair['accessions'];check(pair['name'],covered(ids),True,pair['evidence_scope'])
    for acc in ids:check(pair['name']+' missing '+acc,covered([p for p in ids if p!=acc]),False,'Missing a required witness does not establish genomic absence or lack of another folding route.')
check('empty',covered([]),False,'The folding cage remains required.')
check('unassayed mixed pair',covered(['P0A6F5','B8H164']),False,'No compatibility evidence for this arbitrary cross-species pair in the audited sources.')
check('mixed pair without compatibility gate',covered(['P0A6F5','B8H164'],require_pair=False),True,'Classification and individual function alone cannot establish partner compatibility.')
original=copy.deepcopy(proteins['P0A6F5']['functions']);proteins['P0A6F5']['functions']=[]
check('family membership without activity',covered(['P0A6F5','P0A6F9']),False,'A family hit cannot replace an independently supported activity.')
check('family-only false positive',covered(['P0A6F5','P0A6F9'],require_activity=False),True,'Demonstrates why the activity gate is required.')
proteins['P0A6F5']['functions']=original
mutated=copy.deepcopy(module)
for part in mutated['module']['parts'][1:]:part['optional']=False
check('making CnoX universally required loses canonical pair',covered(['P0A6F5','P0A6F9'],mutated),False,'CnoX is optional support, not a universal requirement for the cage.')
result={'status':'PASS','cases':cases,'source_sha256':hashes,'limits':evidence['limits']+['The compiler treats the whole cage as one atom; this external oracle explicitly checks both active units, activity and curated compatibility.','The role-function evidence table is a scientific assessment, not an independent experimental validation. No ancestry, universal presence, client-transfer kinetics or arbitrary pair compatibility is inferred.']}
(A/'coverage-results.yaml').write_text(yaml.safe_dump(result,sort_keys=False,width=100))
print(f'{len(cases)} source-scoped coverage checks passed')
