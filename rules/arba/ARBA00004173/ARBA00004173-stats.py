import json, re
from collections import Counter
RD='rules/arba/ARBA00004173/'
raw=json.load(open(RD+'ARBA00004173.json'))
enr=json.load(open(RD+'ARBA00004173.enriched.json'))
cs=raw['mainRule']['conditionSets']
ecs=enr['mainRule']['conditionSets']
print('condition_sets: %d' % len(cs))
print('statistics: %s' % json.dumps(raw['statistics']))
ct=Counter(c['type'] for s in cs for c in s['conditions'])
print('condition_type_usage: %s' % dict(ct.most_common()))
shapes=Counter()
single_ff=0
for s in cs:
    sig=[c for c in s['conditions'] if c['type']!='taxon']
    shapes[tuple(sorted(c['type'] for c in sig))]+=1
    if len(sig)==1 and sig[0]['type']=='FunFam id': single_ff+=1
print('single_funfam_only_sets: %d (%.1f%%)' % (single_ff, 100*single_ff/len(cs)))
unlabeled_ff=0
for s in ecs:
    sig=[c for c in s['conditions'] if c['type']!='taxon']
    if len(sig)==1 and sig[0]['type']=='FunFam id' and not sig[0]['conditionValues'][0].get('label'):
        unlabeled_ff+=1
print('single_funfam_only_sets_with_no_resolved_label: %d' % unlabeled_ff)
print('condition_set_shapes: %s' % dict(shapes.most_common()))
neg_only=sum(1 for s in cs if all(c['isNegative'] for c in s['conditions'] if c['type']=='taxon'))
print('sets_with_no_positive_taxon_condition: %d (%.1f%%)' % (neg_only, 100*neg_only/len(cs)))
pos=Counter(v['value'] for s in cs for c in s['conditions'] if c['type']=='taxon' and not c['isNegative'] for v in c['conditionValues'])
print('sets_with_positive_taxon_condition: %d ; distinct_clades: %d' % (sum(pos.values()), len(pos)))
mito=sum(1 for s in ecs if any(re.search('mitochondri',(v.get('label') or ''),re.I) for c in s['conditions'] if c['type']!='taxon' for v in c['conditionValues']))
print('sets_with_a_signature_label_matching_mitochondri*: %d (%.1f%%)' % (mito, 100*mito/len(cs)))
ipr={v['value'] for s in cs for c in s['conditions'] if c['type']=='InterPro id' for v in c['conditionValues']}
m={}
for line in open(RD+'../_interpro2go.txt'):
    if line.startswith('!'): continue
    mm=re.match(r'InterPro:(IPR\d+)\s+.*?>\s*GO:(.*?)\s*;\s*(GO:\d+)', line)
    if mm: m.setdefault(mm.group(1),set()).add(mm.group(3))
mapped=[i for i in ipr if i in m]
mito_mapped=[i for i in mapped if 'GO:0005739' in m[i]]
print('distinct_InterPro_ids: %d ; with_any_InterPro2GO_mapping: %d ; mapped_to_GO:0005739: %d'
      % (len(ipr), len(mapped), len(mito_mapped)))
def sigsets(p):
    d=json.load(open(p))
    return [frozenset(v['value'] for c in s['conditions'] if c['type']!='taxon' and not c['isNegative'] for v in c['conditionValues'])
            for s in d['mainRule']['conditionSets']]
mine=sigsets(RD+'ARBA00004173.json')
print('distinct_signature_sets_within_rule: %d (of %d -> no exact duplicates)' % (len(set(mine)), len(mine)))
try:
    cyto=set(sigsets('/tmp/ARBA00004496.json')); pero=set(sigsets('/tmp/ARBA00004275.json'))
    sc=sum(1 for s in mine if s in cyto); sp=sum(1 for s in mine if s in pero)
    print('signature_sets_shared_with_ARBA00004496_Cytoplasm: %d (%.1f%%)' % (sc, 100*sc/len(mine)))
    print('signature_sets_shared_with_ARBA00004275_Peroxisome: %d (%.1f%%)' % (sp, 100*sp/len(mine)))
    print('shared_with_both: %d' % sum(1 for s in mine if s in cyto and s in pero))
except FileNotFoundError:
    print('sibling rule JSONs not cached locally; re-fetch from https://rest.uniprot.org/arba/{id}.json')
