from pathlib import Path
import json,hashlib,re,xml.etree.ElementTree as ET
O=None;E=None
def configure(root):
 global O,E
 O=Path(root);E=O/'owner-evidence-v1'
J=lambda p:json.loads(p.read_text())
def need(v,m):
 if not v:raise ValueError(m)
def derive():
 S=J(O/'bootstrap-v1/source-objects.json');U=J(O/'intake-v1/raw/UniProt-P17813.json');tree=J(E/'raw/PTHR14002-tree.json')['search']['tree_topology']['annotation_node'];nodes={};paths={}
 def visit(n,path):
  k=n['persistent_id'];nodes[k]=n;paths[k]=path+[k];c=n.get('children',{}).get('annotation_node',[])
  for a in c if isinstance(c,list)else[c]:visit(a,paths[k])
 visit(tree,[]);leaf=next(n for n in nodes.values()if n.get('node_name')=='HUMAN|HGNC=3349|UniProtKB=P17813');target=leaf['persistent_id'];path=paths[target]
 msa=J(E/'raw/PTHR14002-msa.json')['search']['MSA_list']['sequence_info'];seq=next(x['sequence']for x in msa if x['persistent_id']==target);ungapped=re.sub('[^A-Za-z]','',seq).upper();need(ungapped==U['sequence']['value'],'human MSA identity')
 ibd=O/'frozen-inputs/IBD.gaf';records=[];family=[]
 for i,line in enumerate(ibd.read_text().splitlines(),1):
  if line.startswith('!'):continue
  f=line.split('\t')
  if len(f)<15:continue
  if f[1]in nodes:family.append({'line':i,'fields':f})
  if f[1]in path:records.append({'line':i,'fields':f})
 paints=[]
 for i in [2,41,54]:
  source=S[i];hits=[x for x in records if x['fields'][4]==source['term']['id']and x['fields'][6]=='IBD'];need(len(hits)==1,'one exact ancestor IBD');h=hits[0]
  expected=set(h['fields'][7].split('|'))|{'PANTHER:'+h['fields'][1]};need(set(source['supporting_entities'])==expected,'literal IBA donor/node join')
  paints.append({'source_index':i,'source':source,'IBD':h,'assertion_node_on_target_path':True,'recorded_loss_on_path':[x for x in records if x['fields'][6]in['IRD','IKR']or'NOT'in x['fields'][3]]})
 q=J(E/'raw/Q63961-QuickGO-page1.json');need(q['numberOfHits']==len(q['results']),'complete mouse query');mouse=J(E/'raw/UniProt-Q63961.json');need(mouse['organism']['taxonId']==10090,'mouse donor identity')
 joins=[]
 for i,s in enumerate(S):
  if 'UniProtKB:Q63961'not in s.get('supporting_entities',[])and not any('ENSMUSP00000009705'in x for x in s.get('supporting_entities',[])):continue
  matches=[a for a in q['results']if a['goId']==s['term']['id']and ('NOT'in a['qualifier'])==bool(s.get('negated'))]
  joins.append({'source_index':i,'source':s,'current_matching_donor_records':matches,'boundary':'Same GO and negation applicability join; not a reconstruction of the historical Ensembl/manual transfer event.'})
 arba=J(E/'raw/ARBA00090009.json');cs=arba['mainRule']['conditionSets'][0];xr={(x['database'],x['id'])for x in U['uniProtKBCrossReferences']};conditions=[]
 for c in cs['conditions']:
  vals=c['conditionValues'];typ=c['type'];need(not c['isNegative'],'expected positive first clause')
  ok=any((typ=='InterPro id'and('InterPro',v['value'])in xr)or(typ=='PANTHER id'and('PANTHER',v['value'])in xr)or(typ=='taxon'and v['value']in U['organism']['lineage'])for v in vals)
  need(ok,'ARBA first clause predicate');conditions.append({'condition':c,'target_match':ok})
 hpa=ET.fromstring((E/'raw/HPA-ENSG00000106991.xml').read_bytes()).find('entry');need(hpa.findtext('name')=='ENG','HPA identity');icc=hpa.find("cellExpression[@technology='ICC/IF']");need(icc is not None,'HPA ICC');hpa_summary=ET.tostring(icc,encoding='unicode');need('GO:0005886'in hpa_summary and 'supported'in hpa_summary,'HPA summary support')
 sl=[x for x in (E/'raw/uniprotkb_sl2go.txt').read_text().splitlines()if x.startswith('UniProtKB-SubCell:SL-0039 ')];need(len(sl)==1 and 'GO:0005886'in sl[0],'SL mapping')
 terms=J(E/'raw/QuickGO-terms.json')['results'];needed={x['term']['id']for x in S};need(needed<={x['id']for x in terms},'all literal source definitions')
 return {'source_objects':len(S),'human_leaf':{'node':target,'node_name':leaf['node_name'],'subfamily':leaf['prop_sf_id'],'path':path,'MSA_length':len(ungapped),'MSA_matches_official':True},'family_IBD_records':len(family),'path_records':records,'paint_joins':paints,'mouse_identity':{'accession':mouse['primaryAccession'],'taxon':10090,'length':mouse['sequence']['length']},'mouse_query_records':len(q['results']),'mouse_source_joins':joins,'ARBA':{'source_index':83,'rule':arba['uniRuleId'],'OR_clause_count':len(arba['mainRule']['conditionSets']),'verified_clause_index':0,'conditions':conditions,'annotations':arba['mainRule']['annotations'],'boundary':'Only one sufficient OR clause is evaluated; no assertion that every alternative clause matches.'},'HPA':{'source_index':48,'entry':hpa.attrib,'ICC_IF_summary_xml':hpa_summary,'boundary':'Official XML assertions only; no figure-pixel or all-secondary-location claim.'},'SL_mapping':{'source_index':49,'literal_line':sl[0]},'term_definitions':[{'id':x['id'],'name':x['name'],'definition':x.get('definition')}for x in terms if x['id']in needed]}
