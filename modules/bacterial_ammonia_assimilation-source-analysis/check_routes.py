"""Exhaustively test the 12-protein capacity model with an assembly-aware oracle.

The production compiler treats each complex as an atom. Its predicate must
resolve all native active units; atom presence alone is not physical assembly.
The independent expected answer is the presence of any complete native triple.
Neither predicate nor result establishes expression, flux or growth sufficiency.
"""
from pathlib import Path
import itertools,json,yaml
from ai_gene_review.module_logic import compile_module,is_satisfied,enumerate_routes
from check_module import walk
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent

def main():
    d=yaml.safe_load((ROOT/'modules/bacterial_ammonia_assimilation.yaml').read_text());panel=json.loads((HERE/'members.json').read_text());objects={x['id']:x for x in walk(d) if isinstance(x.get('id'),str)}
    names=sorted(m['accession'] for m in panel);groups={}
    for m in panel:groups.setdefault(m['organism'],set()).add(m['accession'])
    assert len(names)==12 and len(groups)==4 and all(len(x)==3 for x in groups.values())
    circuit=compile_module(d);routes=list(enumerate_routes(circuit));assert len(routes)==4 and all(len(x)==2 for x in routes)
    def present(s,available):
        if s['selector_type']=='GENE_PRODUCT':return s['gene_product']['term']['id'].split(':')[1] in available
        assert s['selector_type']=='PROTEIN_COMPLEX'
        units=s['protein_complex']['active_units'];assert len(units)==2
        assert all(u['participant']['taxon']['term']['id']==s['taxon']['term']['id'] for u in units)
        return all(present(u['participant'],available) for u in units)
    cases=[];naive_failures=[];any_chain_failures=[]
    for bits in itertools.product([False,True],repeat=12):
        available={a for a,b in zip(names,bits) if b};expected=any(g<=available for g in groups.values())
        actual=is_satisfied(circuit,lambda atom:present(objects[atom.node_id]['participant'],available));assert actual==expected,(available,actual,expected)
        naive=is_satisfied(circuit,lambda atom:bool(set(atom.uniprots)&available))
        any_chain=is_satisfied(circuit,lambda atom:any(x['gene_product']['term']['id'].split(':')[1] in available for x in walk(objects[atom.node_id]['participant']) if x.get('selector_type')=='GENE_PRODUCT'))
        if any_chain!=expected:any_chain_failures.append({'available':sorted(available),'any_chain':any_chain,'required':expected})
        if naive!=expected:naive_failures.append({'available':sorted(available),'naive':naive,'required':expected})
        cases.append({'available':sorted(available),'satisfied':actual})
    focused=[]
    for org,g in groups.items():
        assert any(c['available']==sorted(g) and c['satisfied'] for c in cases)
        for absent in g:
            a=g-{absent};assert not is_satisfied(circuit,lambda atom:present(objects[atom.node_id]['participant'],a));focused.append({'case':org+' missing '+absent,'available':sorted(a),'satisfied':False})
    # Exactly one GS and both other chains borrowed from another organism cannot complete a route.
    for first,second in itertools.permutations(groups,2):
        gs=next(m['accession'] for m in panel if m['organism']==first and m['role']=='GS');others={m['accession'] for m in panel if m['organism']==second and m['role']!='GS'};a={gs}|others
        assert not is_satisfied(circuit,lambda atom:present(objects[atom.node_id]['participant'],a));focused.append({'case':first+' GS with '+second+' GOGAT','available':sorted(a),'satisfied':False})
    report={'subsets':len(cases),'positive':sum(x['satisfied'] for x in cases),'negative':sum(not x['satisfied'] for x in cases),'native_routes':len(routes),'focus_cases':focused,'naive_atom_presence_disagreements':len(naive_failures),'any_single_chain_presence_false_positives':len(any_chain_failures),'limitation':'Assembly/context requirements are supplied by the explicit oracle, not by the generic activity compiler. These are biochemical-capacity checks, not experimental evidence for assembly or flux.'}
    out=ROOT/'.cache/module-audit-logs/ammonia-module-review';(out/'route-cases.json').write_text(json.dumps(cases,indent=2));(out/'route-summary.json').write_text(json.dumps(report,indent=2));(out/'naive-oracle-counterexamples.json').write_text(json.dumps({'atom_presence':naive_failures,'any_chain_presence':any_chain_failures},indent=2));print(json.dumps(report,indent=2))
if __name__=='__main__':main()
