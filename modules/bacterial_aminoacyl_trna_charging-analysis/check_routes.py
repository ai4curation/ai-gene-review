"""Exercise native-context output routes with the production Boolean compiler.

The explicit oracle enforces organism context and all named complex subunits.
The generic compiler does not itself infer taxonomy or expand active units.
Passing a partial chemistry route is not proof of native flux or a complete genome.
"""
import json
from pathlib import Path

import yaml
from ai_gene_review.module_logic import compile_node, is_satisfied

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def main():
    doc = yaml.safe_load((ROOT / 'modules/bacterial_aminoacyl_trna_charging.yaml').read_text())
    panel = json.loads((HERE / 'members.json').read_text())
    species = {x['accession']:x['organism'] for x in panel}
    by_gene = {(x['organism'],x['gene']):x['accession'] for x in panel}
    by_org = {org:{a for a,s in species.items() if s==org} for org in set(species.values())}
    nodes = {x['id']:x for x in walk(doc['module']) if 'id' in x}
    requirements = {}
    for x in walk(doc['module']):
        for a in x.get('annotons',[]):
            requirements[a['id']]={t['term']['id'].split(':',1)[1] for t in walk(a['participant']) if str(t.get('term',{}).get('id','')).startswith('UniProtKB:')}
            assert requirements[a['id']], a['id']
    cases=[]

    def check(name,node_id,org,present,expected):
        def holds(atom):
            required = requirements[atom.node_id]
            return required <= present and all(species[a]==org for a in required)
        observed=is_satisfied(compile_node(nodes[node_id]),holds)
        assert observed==expected,(name,expected,observed)
        cases.append({'case':name,'node':node_id,'organism_context':org,'present':sorted(present),'expected':expected,'observed':observed})

    full=doc['module']['id']
    check('Empty inventory fails',full,'PSEPK',set(),False)
    check('Complete sampled KT2440 panel',full,'PSEPK',by_org['PSEPK'],True)
    for org in sorted(by_org.keys()-{'PSEPK'}):
        check('Partial '+org+' panel is not a complete program',full,org,by_org[org],False)
    for gene in ['alaS','glyQ','glyS','pheS','pheT','gatA','gatB','gatC','aspS','glnS']:
        check('KT2440 lacking '+gene,full,'PSEPK',by_org['PSEPK']-{by_gene[('PSEPK',gene)]},False)
    check('Foreign GlyRS cannot rescue a native-context missing GlyS',full,'PSEPK',(by_org['PSEPK']-{by_gene[('PSEPK','glyS')]})|by_org['THET8'],False)
    for org in ['PSEPK','PSEAE','BACSU']:
        check(org+' matched indirect Asn',''+org.lower()+'_indirect_asn',org,by_org[org],True)
        for gene in ['gatA','gatB','gatC','aspS']:
            check(org+' indirect Asn requires '+gene,org.lower()+'_indirect_asn',org,by_org[org]-{by_gene[(org,gene)]},False)
    mixed={by_gene[('PSEAE','aspS')]}|{by_gene[('PSEPK',g)] for g in ['gatA','gatB','gatC']}
    check('Mixed-species precursor and GatCAB do not form a sampled Asn route','asn_trna_output','PSEAE',mixed,False)
    check('Bacillus indirect Gln','bacsu_indirect_gln','BACSU',by_org['BACSU'],True)
    check('THEVB ND-GluRS plus foreign GatCAB is not a Gln route','gln_trna_output','THEVB',by_org['THEVB']|by_org['PSEPK'],False)
    check('Bacillus direct Asn alone','asn_trna_output','BACSU',{by_gene[('BACSU','asnS')]},True)
    check('Borrelia class I LysRS','lys_trna_output','BORBU',by_org['BORBU'],True)
    check('Thermus homodimeric GlyRS','gly_trna_output','THET8',by_org['THET8'],True)
    check('Paired bacterial Cys chemistry with explicit native-pair inference','cys_trna_output','9BACT',by_org['9BACT'],True)
    for gene in ['A0A0S7X285','A0A0S7X265']:
        check('Single '+gene+' cannot complete Cys output','cys_trna_output','9BACT',{by_gene[('9BACT',gene)]},False)
    result={'passed':len(cases),'failed':0,'oracle_limits':'Species and complete complex subunit requirements are enforced by this explicit predicate; the generic compiler does not guarantee them. Partial route success describes supported chemistry, not a new native physiological experiment.','cases':cases}
    (HERE/'route-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'{len(cases)} route/assembly/context cases passed')


if __name__=='__main__':
    main()
