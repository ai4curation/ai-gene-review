# /// script
# requires-python = ">=3.10"
# dependencies = ["PyYAML==6.0.2"]
# ///
"""Rebuild a literature/database evidence extract, not a predictive analysis.

See CEBPA-evidence-inputs.json for exact external input snapshots and
CEBPA-evidence-reproduction.md for reproducible commands and access limits.
The output joins immutable source identities, never review-list positions.
"""
import argparse,hashlib,json,re,subprocess,urllib.request
from pathlib import Path
import yaml

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def source_object(a):
 return {k:v for k,v in a.items() if k!='review'}
def stable_json(obj):
 return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False)
def source_key(a):
 return dict(term_id=a['term']['id'],reference_id=a['original_reference_id'],supporting_entities=sorted(a.get('supporting_entities',[])),source_sha256=hashlib.sha256(stable_json(source_object(a)).encode()).hexdigest())
def build(seed,source,bzip,manifest):
 y=yaml.safe_load(seed.read_text());A=sorted(y['existing_annotations'],key=lambda a:stable_json(source_key(a)))
 assertion_hash=hashlib.sha256(stable_json([source_object(a) for a in A]).encode()).hexdigest()
 raw=(source/'IntAct-P49715.mitab').read_bytes()
 columns={'participant_a':0,'participant_b':1,'detection_method':6,'publication_identifiers':8,'taxon_a':9,'taxon_b':10,'interaction_type':11,'source_database':12,'interaction_identifiers':13,'expansion_method':15,'biological_role_a':16,'biological_role_b':17,'experimental_role_a':18,'experimental_role_b':19,'participant_type_a':20,'participant_type_b':21,'host_organism':28,'negative_interaction':35,'features_a':36,'features_b':37}
 entries=[]
 for i,a in enumerate(A):
  partners=[v.split(':',1)[1] for v in a.get('supporting_entities',[]) if v.startswith('UniProtKB:')]
  if not partners or not a['original_reference_id'].startswith('PMID:'):continue
  rows=[];pmid=a['original_reference_id'].split(':')[1]
  for number,line in enumerate(raw.decode().splitlines(),1):
   c=line.split('\t')
   if len(c)<38 or 'pubmed:'+pmid not in c[8].split('|'):continue
   ids=[v.removeprefix('uniprotkb:') for v in c[:2]]
   if not any(sorted(ids)==sorted(['P49715',p]) for p in partners):continue
   r={k:c[n] for k,n in columns.items()};r.update(raw_line_number=number,raw_line_sha256=hashlib.sha256(line.encode()).hexdigest(),record_urls=['https://www.ebi.ac.uk/intact/interaction/'+v for v in re.findall(r'intact:(EBI-\d+)',c[13])]);rows.append(r)
  entries.append(dict(source_key=source_key(a),term=a['term'],source_reference=a['original_reference_id'],exact_partners=partners,records=rows))
 receipt=next(r for r in manifest['inputs'] if r['name']=='IntAct-P49715.mitab');assert receipt['sha256']==sha(source/'IntAct-P49715.mitab')
 intact=dict(artifact_type='Exact source-linked machine-field extract; no curated prose quotations',target='UniProtKB:P49715',source_assertions_sha256=assertion_hash,source_query=receipt,selection_rules=['Exact primary accession and partner accession; no isoform suffix collapsing','Exact PMID field match','Retain negative flags and mutant/construct features; positive support judged separately','Copied machine fields are source records, not independent experimental replication','No author/curator prose; empty matches are not evidence of absence'],annotations=entries)
 symbols={'P17676':'CEBPB','P18848':'ATF4','P35638':'DDIT3','P49716':'CEBPD','P53567':'CEBPG','Q16520':'BATF','Q9Y2D1':'ATF5','P01100':'FOS','P18847':'ATF3','Q15744':'CEBPE','Q8N1L9':'BATF2','Q9NR55':'BATF3','P49715':'CEBPA'}
 lines=(bzip/'2010-si.txt').read_text().splitlines();h=next(i for i,s in enumerate(lines) if s.split()[:3]==['CEBPA','CEBPB','CEBPD']);header=lines[h].split();matrix={}
 for line in lines[h+1:h+1+len(header)]:
  t=line.split();assert len(t)==len(header)+1;matrix[t[0]]=dict(zip(header,t[1:]))
 assert len(matrix)==37
 pages=(source/'20102225-mit-thesis.txt').read_text().split('\f');matches=[p for p in pages if 'Table 5.2:' in p and 'Human bZIP interactions.' in p];assert len(matches)==1, 'Expected one human bZIP Table5.2';page=matches[0]
 thesis={}
 for line in page.splitlines():
  t=line.split()
  if len(t)==8 and t[1] in symbols.values() and t[2] not in ['DDIT3','Protein']:thesis[t[1]]=t[4]
 assert len(thesis)==11
 complexes=[]
 for name in sorted(x['name'] for x in manifest['inputs'] if x['name'].startswith('CPX-') and x['name'].endswith('.json')):
  p=source/name
  d=json.loads(p.read_text())
  if 'participants' not in d:continue
  complexes.append(dict(id=p.stem,url='https://www.ebi.ac.uk/complexportal/complex/'+p.stem,source_file=p.name,source_sha256=sha(p),species=d['species'],participants=[dict(accession=x['identifier'],symbol=x['name'],stoichiometry=x['stochiometry']) for x in d['participants']],pubmed_ids=[x['identifier'] for x in d['crossReferences'] if x['database']=='pubmed'],linked_features=[dict(feature_id=f['featureAc'],feature_participant_accession=f['participantId'],ranges=f['ranges'],feature_type=f['featureTypeMI']) for x in d['participants'] for f in x.get('linkedFeatures',[])]))
 rows=[]
 for row in A:
  if row['original_reference_id'] not in ['PMID:20102225','PMID:23661758'] or row['term']['id'] not in ['GO:0005515','GO:0042802']:continue
  a=source_object(row);partners=a.get('supporting_entities',[])
  if len(partners)!=1 or not partners[0].startswith('UniProtKB:'):raise ValueError('Expected one exact UniProt bZIP partner: '+stable_json(source_key(a)))
  accession=partners[0].split(':',1)[1]
  if accession not in symbols:raise ValueError('Unmapped bZIP partner '+accession+' for '+stable_json(source_key(a)))
  sym=symbols[accession]
  r=dict(source_key=source_key(a),source_before=a,partner_symbol=sym,species='NCBITaxon:9606',construct_scope='purified bZIP/leucine-zipper domains, not all full-length products or physiological partnerships')
  if a['original_reference_id']=='PMID:20102225':r['published_2010_table_s2']=dict(CEBPA_surface_partner_solution=matrix['CEBPA'][sym],partner_surface_CEBPA_solution=matrix[sym]['CEBPA'],units='background-corrected fluorescence, not Kd',source_doi='10.1021/bi902065k.s001',pdf_page=9,figure_s2_visually_read_page=3)
  else:r['thesis_2012_table_5_2']=dict(CEBPA_partner_kd_nM=thesis[sym],pdf_and_printed_page=195,original_2013_supplement_equivalence='not established',source_url='https://web.mit.edu/biology/keating/extra_files/aaronreinke_thesis_022012.pdf',orientation_rule='lower Kd from the two heterodimer orientations; not independent replication')
  r['complex_records']=[c['id'] for c in complexes if accession in [x['accession'] for x in c['participants']] and (accession!='P49715' or len(c['participants'])==1)];rows.append(r)
 bd=dict(source_assertions_sha256=assertion_hash,source_scope='Targeted archived primary table cells and source-linked curated complexes. Thesis values are not relabeled as the 2013 released table. No independent replication is asserted.',primary_sources={'2010_supplement':dict(doi='10.1021/bi902065k.s001',url='https://ndownloader.figshare.com/files/4480228',sha256=sha(bzip/'bi902065k_si_001.pdf'),md5=hashlib.md5((bzip/'bi902065k_si_001.pdf').read_bytes()).hexdigest()), '2012_thesis':dict(url='https://web.mit.edu/biology/keating/extra_files/aaronreinke_thesis_022012.pdf',sha256=sha(source/'20102225-mit-thesis.pdf'),title='Determining Protein Interaction Specificity of Native and Designed bZIP Family Transcription Factors',author='Aaron W. Reinke',year=2012)},rows=rows,curated_complex_records=complexes)
 orth=[]
 for n in ['P53566','P05554']:
  for r in json.loads((source/f'{n}-goa.json').read_text())['results']:
   if r['goId'] in ['GO:0071837','GO:0043032','GO:0050729','GO:0055088','GO:0097009','GO:0030851','GO:0045444']:orth.append({k:r.get(k) for k in ['geneProductId','goId','reference','goEvidence','qualifier','assignedBy','withFrom','taxonId','date']})
 return dict(title='CEBPA source evidence: exact interaction records, bZIP target measurements and ortholog links',source_assertions_sha256=assertion_hash,intact=intact,bzip=bd,ortholog_records=orth)


def prepare_inputs(folder,manifest,fetch):
 folder.mkdir(parents=True,exist_ok=True)
 for item in manifest['inputs']:
  path=folder/item['name']
  if not path.exists() and fetch:
   try:
    req=urllib.request.Request(item['url'],headers={'User-Agent':'ai-gene-review evidence reproduction'})
    with urllib.request.urlopen(req,timeout=60) as response:data=response.read()
   except Exception as e:raise RuntimeError('Could not retrieve '+item['name']+' from '+item['url']) from e
   digest=hashlib.sha256(data).hexdigest()
   if digest!=item['sha256']:raise ValueError('Source snapshot changed for '+item['name']+': received '+digest+', expected '+item['sha256']+'. No replacement accepted.')
   path.write_bytes(data)
  if not path.exists():raise FileNotFoundError('Missing reviewed input '+str(path)+'; use --fetch-inputs or supply the exact snapshot listed in the manifest.')
  digest=sha(path)
  if digest!=item['sha256']:raise ValueError('Input hash mismatch for '+str(path)+': '+digest)
 for pdf,txt in [('20102225-mit-thesis.pdf','20102225-mit-thesis.txt'),('bi902065k_si_001.pdf','2010-si.txt')]:
  try:subprocess.run(['pdftotext','-layout',str(folder/pdf),str(folder/txt)],check=True,capture_output=True)
  except FileNotFoundError as e:raise RuntimeError('Install Poppler pdftotext to extract the two original PDF inputs.') from e

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--seed',required=True,type=Path);p.add_argument('--inputs',required=True,type=Path);p.add_argument('--manifest',type=Path,default=Path(__file__).with_name('CEBPA-evidence-inputs.json'));p.add_argument('--fetch-inputs',action='store_true');p.add_argument('--output',required=True,type=Path)
 args=p.parse_args();manifest=json.loads(args.manifest.read_text());prepare_inputs(args.inputs,manifest,args.fetch_inputs)
 result=build(args.seed,args.inputs,args.inputs,manifest)
 args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
