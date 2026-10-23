"""Reconstruct ELAC2 database provenance from saved raw bytes (no network)."""
from pathlib import Path
import json, re, hashlib, xml.etree.ElementTree as ET
import reconstruct_paint
D=Path(__file__).resolve().parent;F=D/'frozen-inputs'
INDICES=[2,10,11,12,14,16,19,20,21,22,23,25,27,28,29,30,31,33]
def read(name):return json.loads((D/'raw'/name).read_text())
def pick(x,keys):return {k:x[k] for k in keys if k in x}
def aslist(x):return x if isinstance(x,list) else [x] if x else []
def elem(x):
 return {'tag':x.tag,'attributes':x.attrib,'text':(x.text or '').strip(),'children':[elem(c) for c in x]}
def sources():return json.loads((F/'source-objects.json').read_text())
def termproof():
 ts=read('QuickGO-terms.json')['results'];out=[]
 for t in ts:
  a=read(t['id'].replace(':','')+'-ancestors-is_a.json')['results']
  if len(a)!=1 or a[0]['id']!=t['id']:raise ValueError('ancestor identity')
  out.append({'term':t,'is_a_ancestors_including_self':a[0].get('ancestors',[])})
 return sorted(out,key=lambda x:x['term']['id'])
def paint():
 p=reconstruct_paint.run();exp={'EXP','IDA','IMP','IPI','IGI','IEP','HTP','HDA','HMP','HGI','HEP'}
 mapping={'UniProtKB:Q9BQ52':'Q9BQ52','MGI:MGI:1890496':'Q80Y81','AGI_LocusCode:AT1G52160':'Q8VYS2','AGI_LocusCode:AT3G16260':'F4J1H7','WB:WBGene00001983':'O44476','FB:FBgn0028426':'Q8MKW7','SGD:S000001787':'P36159','PomBase:SPBC3D6.03c':'P87168','PomBase:SPAC1D4.10':'Q10155'}
 pages={}
 for ac in sorted(set(mapping.values())):
  path=F/'QuickGO-Q9BQ52-page1.json' if ac=='Q9BQ52' else D/'raw'/('QuickGO-'+ac+'-page1.json')
  j=json.loads(path.read_text())
  if j['pageInfo']['total']!=1 or len(j['results'])!=j['numberOfHits']:raise ValueError('incomplete donor page')
  pages[ac]={'path':str(path.relative_to(D)),'numberOfHits':j['numberOfHits'],'records':j['results']}
 for join in p['joins']:
  term=join['source']['term']['id'];joins=[]
  for identifier in join['IBD']['fields'][7].split('|'):
   ac=mapping[identifier];allrows=pages[ac]['records'];selected=[{'result_index':i,'record':r} for i,r in enumerate(allrows) if r['goId']==term]
   joins.append({'IBD_donor':identifier,'accession':ac,'raw':pages[ac]['path'],'complete_page_count':len(allrows),'exact_term_records':selected,'experimental_exact_term_records':[r for r in selected if r['record']['goEvidence'] in exp]})
  join['current_donor_grounding']=joins
 p['donor_pages']=pages
 # Aliases below are resolved by the literal tree identifiers and official UniProt record fields.
 p['additional_official_identity_records']={ac:pick(read('UniProt-'+ac+'.json'),['primaryAccession','genes','organism','uniProtKBCrossReferences']) for ac in ['Q8VYS2','F4J1H7','Q80Y81']}
 return p

def reactome():
 s=sources();out=[]
 for i in INDICES:
  src=s[i]
  if not src['original_reference_id'].startswith('Reactome:'):continue
  event=src['original_reference_id'].split(':',1)[1];root=read('Reactome-'+event+'.json');paths=[]
  events=[(root,[])]
  if root['schemaClass']=='Pathway':
   events=[]
   for j,e in enumerate(root.get('hasEvent',[])):
    ep=D/'raw'/('Reactome-'+e['stId']+'.json')
    if ep.exists():events.append((json.loads(ep.read_text()),[{'file':'Reactome-'+event+'.json','pointer':f'/hasEvent/{j}','dbId':e['dbId']}]))
  for ev,pre in events:
   for j,c in enumerate(ev.get('catalystActivity',[])):
    cat=read('Reactome-'+str(c['dbId'])+'.json');pe=read('Reactome-'+str(cat['physicalEntity']['dbId'])+'.json');ref=pe['referenceEntity']
    if ref.get('identifier')!='Q9BQ52':continue
    path=pre+[{'file':'Reactome-'+ev['stId']+'.json','pointer':f'/catalystActivity/{j}','dbId':c['dbId']},{'file':'Reactome-'+str(c['dbId'])+'.json','pointer':'/physicalEntity','dbId':pe['dbId']},{'file':'Reactome-'+str(pe['dbId'])+'.json','pointer':'/referenceEntity','dbId':ref['dbId'],'identifier':ref['identifier']}]
    paths.append({'edges':path,'event':pick(ev,['dbId','stId','stIdVersion','displayName','schemaClass','isInferred','isChimeric','speciesName','goBiologicalProcess','summation']), 'event_references':ev.get('literatureReference',[]),'inputs':[pick(x,['dbId','stId','displayName','schemaClass']) for x in ev.get('input',[])],'outputs':[pick(x,['dbId','stId','displayName','schemaClass']) for x in ev.get('output',[])],'catalyst_activity':cat['activity'],'target':pick(pe,['dbId','stId','stIdVersion','displayName','speciesName','startCoordinate','endCoordinate','compartment','literatureReference']),'reference_entity':pick(ref,['dbId','identifier','databaseName','sequenceLength','chain'])})
  if not paths:raise ValueError('No target witness for '+str(i))
  out.append({'annotation_index':i,'source':src,'root':pick(root,['dbId','stId','stIdVersion','schemaClass','displayName','goBiologicalProcess']),'target_paths':paths,'unexpanded_root_child_events':[pick(x,['dbId','stId','displayName','schemaClass']) for x in root.get('hasEvent',[]) if not (D/'raw'/('Reactome-'+x.get('stId','')+'.json')).exists()]})
 return {'rows':out,'cytosolic_input_members':read('Reactome-9708815.json')['hasMember'],'cytosolic_output_members':read('Reactome-9708818.json')['hasMember'],'scope':'Exact target catalyst chains. Unexpanded siblings are not absence evidence. Database entity coordinates are not experimentally authenticated construct or isoform assignments.'}

def automatic():
 target=json.loads((F/'UniProt-Q9BQ52.json').read_text());xrefs=target['uniProtKBCrossReferences'];rule=read('ARBA00086796.json');checks=[]
 for si,cs in enumerate(rule['mainRule']['conditionSets']):
  cc=[]
  for c in cs['conditions']:
   vals=c['conditionValues'];typ=c['type']
   if typ=='FunFam id':matches=[x for x in xrefs if x['database']=='FunFam' and x['id'] in [v['value'] for v in vals]]
   elif typ=='taxon':matches=[x for x in target['organism']['lineage'] if x in [v['value'] for v in vals]]
   else:raise ValueError('unhandled rule premise '+typ)
   cc.append({'condition':c,'target_matches':matches,'satisfied': bool(matches)!=c.get('isNegative',False)})
  checks.append({'condition_set_index':si,'conditions':cc,'all_satisfied':all(x['satisfied'] for x in cc)})
 ipr=read('InterPro-Q9BQ52-matches.json');
 if ipr.get('next'):raise ValueError('incomplete InterPro page')
 ec=[{'line':i,'text':l} for i,l in enumerate((D/'raw/ec2go.txt').read_text().splitlines(),1) if l.startswith('EC:3.1.26.11 ')]
 return {'target_relevant_comments':[x for x in target['comments'] if x['commentType'] in ['FUNCTION','SUBCELLULAR LOCATION','CATALYTIC ACTIVITY']], 'target_relevant_crossreferences':[x for x in xrefs if x['database'] in ['FunFam','InterPro','PANTHER','HPA','Ensembl']], 'ARBA':{'rule':rule,'target_premise_checks':checks},'InterPro':{'IPR027794':read('InterPro-IPR027794.json'),'IPR047151':read('InterPro-IPR047151.json'),'target_matches':ipr},'EC_mapping':ec,'subcell_mappings':{k:read(k+'.json') for k in ['SL-0191','SL-0173','SL-0269']},'mouse_ensembl_translation':read('ENSMUSP00000098610.json'),'mouse_uniprot':{'primaryAccession':read('UniProt-Q80Y81.json')['primaryAccession'],'ensembl':[x for x in read('UniProt-Q80Y81.json')['uniProtKBCrossReferences'] if x['database']=='Ensembl'],'subcell_comments':[x for x in read('UniProt-Q80Y81.json')['comments'] if x['commentType']=='SUBCELLULAR LOCATION']},'mouse_nucleoid_records':[{'result_index':i,'record':r} for i,r in enumerate(read('QuickGO-Q80Y81-page1.json')['results']) if r['goId']=='GO:0042645']}

def hpa():
 entry=ET.parse(D/'raw/HPA-ENSG00000006744.xml').getroot().find('entry');target=json.loads((F/'UniProt-Q9BQ52.json').read_text());out=[]
 for a in entry.findall('antibody'):
  seq=a.findtext('antigenSequence');p=target['sequence']['value'].find(seq) if seq else -1
  out.append({'antibody_attributes':a.attrib,'antigen_sequence':seq,'canonical_exact_interval':None if p<0 else [p+1,p+len(seq)],'cellExpression':[elem(e) for e in a.findall('cellExpression')]})
 return {'entry_identifiers':[elem(e) for e in entry if e.tag in ['name','synonym','identifier']],'gene_cellExpression':[elem(e) for e in entry.findall('cellExpression')],'antibodies':out,'read_scope':'Official XML annotations and validation metadata; linked IF image pixels not inspected. No splice-form-specific localization or universal exclusion inferred.'}

def run():return {'source_indices':INDICES,'exact_sources':[{'annotation_index':i,'source':sources()[i]} for i in INDICES],'terms':termproof(),'paint':paint(),'reactome':reactome(),'automatic':automatic(),'HPA':hpa()}
if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
