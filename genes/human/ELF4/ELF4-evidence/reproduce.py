"""Offline literal source projection. Python standard library; no extraction or network."""
from pathlib import Path,PurePosixPath
import argparse,collections,csv,hashlib,io,json,re,stat,sys,zipfile
import xml.etree.ElementTree as ET

D=Path(__file__).resolve().parent
def need(v,msg):
 if not v:raise ValueError(msg)
def sha(b):return hashlib.sha256(b).hexdigest()
def load_inputs(root=D):
 m=json.loads((root/'inputs.json').read_text());ap=root/m['archive']
 need(m['archive']=='database-inputs.zip','Unexpected archive filename')
 need(ap.stat().st_size<64*2**20,'Archive is too large')
 need(sha(ap.read_bytes())==m['sha256'],'Archive SHA256 mismatch')
 result={}
 with zipfile.ZipFile(ap)as z:
  inf=z.infolist();names=[i.filename for i in inf]
  need(len(names)==len(set(names)) and set(names)==set(m['members']),'Missing, extra or duplicate archive members')
  need(sum(i.file_size for i in inf)<128*2**20,'Uncompressed archive is too large')
  for i in inf:
   name=i.filename;p=PurePosixPath(name);mode=i.external_attr>>16;r=m['members'][name]
   need(not p.is_absolute() and '..'not in p.parts and '\\'not in name and re.fullmatch(r'[A-Za-z0-9_./-]+',name),'Unsafe archive member')
   need(not i.is_dir() and not stat.S_ISLNK(mode) and not(i.flag_bits&1),'Directory, link or encrypted member')
   need(i.file_size==r['bytes'] and i.file_size<64*2**20,'Member size mismatch')
   b=z.read(i);need(sha(b)==r['sha256'],'Member SHA256 mismatch: '+name);result[name]=b
 return result
def project(raw,config):
 def J(n):return json.loads(raw[n])
 def text(n):return raw[n].decode('utf-8')
 sources=J(config['source_member']);u=J('inputs/UniProt-Q99607.json');acc=config['target']
 need(u['primaryAccession']==acc and u['organism']['taxonId']==9606,'Target identity')
 seq=u['sequence']['value'];fasta=''.join(text('inputs/Q99607.fasta').splitlines()[1:])
 normal=text('inputs/ELF4-uniprot.txt');normal_seq=''.join(re.findall('[A-Z]+',normal.split('\nSQ ',1)[1].split('\n',1)[1].split('//',1)[0]))
 need(seq==fasta==normal_seq,'Official product sequence mismatch')
 def key(term,ev,ref,qual,entities,product):
  qs=qual.split('|');return(term,ev,ref,next((x for x in qs if x!='NOT'),''),tuple(sorted(set(entities)-{''})),'NOT'in qs,product if '-'in product else None)
 def sk(r):return(r['term']['id'],r['evidence_type'],r['original_reference_id'],r.get('qualifier',''),tuple(sorted(r.get('supporting_entities',[]))),r.get('negated',False),r.get('isoform'))
 rows=list(csv.DictReader(io.StringIO(text('inputs/ELF4-goa.tsv')),delimiter='\t'));by=collections.defaultdict(list)
 for i,r in enumerate(rows):by[key(r['GO TERM'],r['GO EVIDENCE CODE'],r['REFERENCE'],r['QUALIFIER'],r['WITH/FROM'].split('|'),r['GENE PRODUCT ID'])].append(i)
 q=J('inputs/QuickGO-Q99607.json');need(q['pageInfo']['total']==1 and q['numberOfHits']==len(q['results']),'Target donor pagination')
 qkeys=[key(r['goId'],r['goEvidence'],r['reference'],r['qualifier'],[x['db']+':'+x['id']for g in r.get('withFrom')or [] for x in g['connectedXrefs']],r['geneProductId'].split(':',1)[1])for r in q['results']]
 need(collections.Counter(qkeys)==collections.Counter(k for k,ix in by.items()for _ in ix),'Raw API/TSV multiset')
 need(set(by)==set(map(sk,sources)) and len(sources)==len(by),'Normalized full-context source join')
 joins=[{'source_index':i,'raw_indices':by[sk(s)]}for i,s in enumerate(sources)]
 duplicates=[{'source_index':j['source_index'],'raw_indices':j['raw_indices'],'raw_records':[rows[i]for i in j['raw_indices']]}for j in joins if len(j['raw_indices'])>1]
 tree=J('database/PTHR11849-treeinfo.json')['search']['tree_topology']['annotation_node'];nodes={};paths={}
 def walk(n,path):
  i=n['persistent_id'];need(i not in nodes,'Repeated tree node');nodes[i]=n;paths[i]=path+[i];children=n.get('children',{}).get('annotation_node',[])
  for c in [children]if isinstance(children,dict)else children:walk(c,path+[i])
 walk(tree,[]);hits=[i for i,n in nodes.items()if n.get('node_name','').endswith('UniProtKB='+acc)];need(len(hits)==1,'Unique PANTHER target');target=hits[0]
 msa=J('database/PTHR11849-familymsa.json')['search']['MSA_list']['sequence_info'];aligned=[x for x in msa if x['persistent_id']==target];need(len(aligned)==1,'Unique MSA target')
 need(re.sub('[^A-Za-z]','',aligned[0]['sequence']).upper()==seq,'Target MSA sequence mismatch')
 path_records=[]
 for line,txt in enumerate(text('inputs/IBD.gaf').splitlines(),1):
  f=txt.split('\t')
  if len(f)>7 and f[1]in paths[target]:path_records.append({'line':line,'fields':f})
 iba=[]
 for i,s in enumerate(sources):
  if s['evidence_type']!='IBA':continue
  ptn=[x.split(':',1)[1]for x in s.get('supporting_entities',[])if x.startswith('PANTHER:')]
  matches=[x for x in path_records if x['fields'][1]in ptn and x['fields'][4]==s['term']['id']and x['fields'][6]=='IBD'and 'NOT'not in x['fields'][3]]
  need(len(matches)==1 and all(p in paths[target]for p in ptn),'Literal IBD ancestry join')
  a=set(s['supporting_entities'])-{'PANTHER:'+p for p in ptn};b=set(matches[0]['fields'][7].split('|'))
  iba.append({'source_index':i,'assertion':matches[0],'node_on_target_path':True,'seed_only_donors':sorted(a-b),'IBD_snapshot_only_donors':sorted(b-a),'exact_donor_set':a==b})
 terms={x['id']:x for name in ['database/QuickGO-terms.json','ontology/QuickGO-ROOT-transcription.json','addendum/GO0140297.json']for x in J(name)['results']}
 typed={}
 for n in sorted(raw):
  if n.endswith('-ancestors-is_a.json'):
   for x in J(n)['results']:typed[x['id']]={'relation':'is_a','ancestors_including_self':sorted(x['ancestors'])}
 need({s['term']['id']for s in sources}<=set(terms),'Missing source term definition')
 iprs={x['id']for x in u['uniProtKBCrossReferences']if x['database']=='InterPro'};rules={}
 for rid,n in config['rules'].items():
  rule=J('database/'+rid+'.json');conditions=rule['mainRule']['conditionSets'][n]['conditions'];checked=[]
  for c in conditions:
   need(c['type']in ['InterPro id','taxon'],'Unsupported selected condition type')
   universe=iprs if c['type']=='InterPro id'else set(u['organism']['lineage']);values=[v['value']for v in c['conditionValues']];matches=[v for v in values if v in universe];passed=bool(matches)
   if c['isNegative']:passed=not passed
   checked.append({'type':c['type'],'negative':c['isNegative'],'values':values,'matched_values':matches,'condition_passes':passed})
  rules[rid]={'selected_condition_set':n,'conditions':checked,'selected_set_matches':all(c['condition_passes']for c in checked),'annotations':rule['mainRule']['annotations'],'exhaustive_rule_firing_assessed':False}
 donor=J('database/QuickGO-Q9Z2U4-page1.json');need(donor['pageInfo']['total']==1 and len(donor['results'])==donor['numberOfHits'],'Mouse pagination incomplete')
 mouse=J('database/UniProt-Q9Z2U4.json');need(mouse['primaryAccession']=='Q9Z2U4' and mouse['organism']['taxonId']==10090,'Mouse identity')
 hpa_bytes=raw['addendum/HPA-ENSG00000102034.xml'];need(b'<!DOCTYPE'not in hpa_bytes and b'<!ENTITY'not in hpa_bytes,'Unsupported XML declarations');hpa=ET.fromstring(hpa_bytes);parent={c:p for p in hpa.iter()for c in p};hp=[]
 for x in hpa.findall('.//cellExpression'):
  if x.attrib.get('technology')!='ICC/IF':continue
  ancestors=[];p=x
  while p in parent:
   p=parent[p]
   if p.tag in ['entry','antibody','proteinAtlas']:ancestors.append({'tag':p.tag,'attributes':p.attrib})
  hp.append({'ancestors':ancestors,'verification':[{'attributes':v.attrib,'value':v.text}for v in x.findall('.//verification')],'summary':x.findtext('summary'),'data':[{'cell_line':d.findtext('cellLine'),'locations':[{'label':v.text,**v.attrib}for v in d.findall('location')]}for d in x.findall('.//data')],'image_pixels_inspected_by_replay':False})
 runx=J('addendum/UniProt-Q01196.json');iso=[c for c in runx.get('comments',[])if c['commentType']=='ALTERNATIVE PRODUCTS'];need(len(iso)==1,'RUNX1 product metadata')
 maps={n:J('database/'+n)['metadata'] for n in ['InterPro-IPR000418.json','InterPro-IPR046328.json']}
 return {'raw_contexts':len(rows),'normalized_sources':len(sources),'GOA_joins':joins,'duplicate_contexts':duplicates,'product':{'accession':acc,'length':len(seq),'sha256':sha(seq.encode()),'alternative_product_blocks':[c for c in u.get('comments',[])if c['commentType']=='ALTERNATIVE PRODUCTS']},'paint':{'tree_nodes':len(nodes),'MSA_entries_including_ancestral':len(msa),'target_node':target,'target_path':paths[target],'target_subfamily':nodes[target].get('prop_sf_id'),'path_records':path_records,'joins':iba},'terms':terms,'typed_ancestry':typed,'rules':rules,'target_interpro_ids':sorted(iprs),'interpro_metadata':maps,'PML_location_mapping':J('database/SL-0465.json'),'mouse_donor':{'accession':mouse['primaryAccession'],'taxon':mouse['organism']['taxonId'],'total_rows':len(donor['results']),'experimental_records':[r for r in donor['results']if r['goEvidence']in ['IDA','IMP','IPI','IGI','IEP']]},'HPA':hp,'RUNX1_alternative_products':iso[0],'scope':'Literal database projections only; assay interpretation and annotation actions are manual. No absence claim follows from missing current records or unmatched selected rule branches.'}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--write',type=Path,help='Create a NEW results file; never overwrite');a=p.parse_args()
 raw=load_inputs();result=project(raw,json.loads((D/'config.json').read_text()))
 if a.write:
  with a.write.open('x')as f:json.dump(result,f,indent=2,ensure_ascii=False);f.write('\n')
 else:need(result==json.loads((D/'results.json').read_text()),'Saved result differs from recomputed inputs')
 print(json.dumps({'status':'PASS','members':len(raw),'raw_contexts':result['raw_contexts'],'sources':result['normalized_sources'],'product_length':result['product']['length'],'IBA_traces':len(result['paint']['joins']),'mouse_rows':result['mouse_donor']['total_rows'],'selected_rule_branches':len(result['rules']),'HPA_records':len(result['HPA'])}))
if __name__=='__main__':
 try:main()
 except (OSError,ValueError,KeyError,TypeError,zipfile.BadZipFile,ET.ParseError)as e:sys.exit('ELF4 evidence replay failed: '+str(e))
