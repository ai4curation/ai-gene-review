"""Rebuild the CEBPA machine-field evidence extract from authentic archived inputs.

Requires Python 3 and PyYAML. Input URLs/hashes are in CEBPA-source-evidence.json.
The original supplement/thesis text inputs are produced with pdftotext -layout.
This reads local raw sources; it does not fabricate unavailable supplements or fetch
replacement data. Pass --seed as the immutable normal seed (review fields ignored).

Example:
  python CEBPA-extract-source-evidence.py --seed CEBPA-ai-review.yaml \
    --source-dir primary-inputs --bzip-dir bzip-inputs --output extract.json

source-dir: IntAct-P49715.mitab, retrievals-round1.json, CPX-*.json,
P53566-goa.json, P05554-goa.json, 20102225-mit-thesis.pdf/.txt.
bzip-dir: bi902065k_si_001.pdf and 2010-si.txt.
"""
import argparse,hashlib,json,re
from pathlib import Path
import yaml

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def build(seed,source,bzip):
 y=yaml.safe_load(seed.read_text());A=y['existing_annotations'];raw=(source/'IntAct-P49715.mitab').read_bytes()
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
  entries.append(dict(seed_index=i,term=a['term'],source_reference=a['original_reference_id'],exact_partners=partners,records=rows))
 receipt=next(r for r in json.loads((source/'retrievals-round1.json').read_text()) if r['file']=='IntAct-P49715.mitab');assert receipt['sha256']==sha(source/'IntAct-P49715.mitab')
 intact=dict(artifact_type='Exact source-linked machine-field extract; no curated prose quotations',target='UniProtKB:P49715',seed_sha256=sha(seed),source_query=receipt,selection_rules=['Exact primary accession and partner accession; no isoform suffix collapsing','Exact PMID field match','Retain negative flags and mutant/construct features; positive support judged separately','Copied machine fields are source records, not independent experimental replication','No author/curator prose; empty matches are not evidence of absence'],annotations=entries)
 symbols={'P17676':'CEBPB','P18848':'ATF4','P35638':'DDIT3','P49716':'CEBPD','P53567':'CEBPG','Q16520':'BATF','Q9Y2D1':'ATF5','P01100':'FOS','P18847':'ATF3','Q15744':'CEBPE','Q8N1L9':'BATF2','Q9NR55':'BATF3','P49715':'CEBPA'}
 lines=(bzip/'2010-si.txt').read_text().splitlines();h=next(i for i,s in enumerate(lines) if s.split()[:3]==['CEBPA','CEBPB','CEBPD']);header=lines[h].split();matrix={}
 for line in lines[h+1:h+1+len(header)]:
  t=line.split();assert len(t)==len(header)+1;matrix[t[0]]=dict(zip(header,t[1:]))
 assert len(matrix)==37
 page=(source/'20102225-mit-thesis.txt').read_text().split('\f')[194];assert 'Table 5.2:' in page and 'Human bZIP interactions.' in page
 thesis={}
 for line in page.splitlines():
  t=line.split()
  if len(t)==8 and t[1] in symbols.values() and t[2] not in ['DDIT3','Protein']:thesis[t[1]]=t[4]
 assert len(thesis)==11
 complexes=[]
 for p in sorted(source.glob('CPX-*.json')):
  d=json.loads(p.read_text())
  if 'participants' not in d:continue
  complexes.append(dict(id=p.stem,url='https://www.ebi.ac.uk/complexportal/complex/'+p.stem,source_file=p.name,source_sha256=sha(p),species=d['species'],participants=[dict(accession=x['identifier'],symbol=x['name'],stoichiometry=x['stochiometry']) for x in d['participants']],pubmed_ids=[x['identifier'] for x in d['crossReferences'] if x['database']=='pubmed'],linked_features=[dict(feature_id=f['featureAc'],feature_participant_accession=f['participantId'],ranges=f['ranges'],feature_type=f['featureTypeMI']) for x in d['participants'] for f in x.get('linkedFeatures',[])]))
 rows=[]
 for i in list(range(31,48))+[100,101]:
  a={k:v for k,v in A[i].items() if k!='review'};accession=a['supporting_entities'][0].split(':')[1];sym=symbols[accession]
  r=dict(index=i,source_before=a,partner_symbol=sym,species='NCBITaxon:9606',construct_scope='purified bZIP/leucine-zipper domains, not all full-length products or physiological partnerships')
  if a['original_reference_id']=='PMID:20102225':r['published_2010_table_s2']=dict(CEBPA_surface_partner_solution=matrix['CEBPA'][sym],partner_surface_CEBPA_solution=matrix[sym]['CEBPA'],units='background-corrected fluorescence, not Kd',source_doi='10.1021/bi902065k.s001',pdf_page=9,figure_s2_visually_read_page=3)
  else:r['thesis_2012_table_5_2']=dict(CEBPA_partner_kd_nM=thesis[sym],pdf_and_printed_page=195,original_2013_supplement_equivalence='not established',source_url='https://web.mit.edu/biology/keating/extra_files/aaronreinke_thesis_022012.pdf',orientation_rule='lower Kd from the two heterodimer orientations; not independent replication')
  r['complex_records']=[c['id'] for c in complexes if accession in [x['accession'] for x in c['participants']] and (accession!='P49715' or len(c['participants'])==1)];rows.append(r)
 bd=dict(seed_sha256=sha(seed),source_scope='Targeted archived primary table cells and source-linked curated complexes. Thesis values are not relabeled as the 2013 released table. No independent replication is asserted.',primary_sources={'2010_supplement':dict(doi='10.1021/bi902065k.s001',url='https://ndownloader.figshare.com/files/4480228',sha256=sha(bzip/'bi902065k_si_001.pdf'),md5_matches_publisher=hashlib.md5((bzip/'bi902065k_si_001.pdf').read_bytes()).hexdigest()=='ff8ff359c144d71a9521410d671f31d7'), '2012_thesis':dict(url='https://web.mit.edu/biology/keating/extra_files/aaronreinke_thesis_022012.pdf',sha256=sha(source/'20102225-mit-thesis.pdf'),title='Determining Protein Interaction Specificity of Native and Designed bZIP Family Transcription Factors',author='Aaron W. Reinke',year=2012)},rows=rows,curated_complex_records=complexes)
 orth=[]
 for n in ['P53566','P05554']:
  for r in json.loads((source/f'{n}-goa.json').read_text())['results']:
   if r['goId'] in ['GO:0071837','GO:0043032','GO:0050729','GO:0055088','GO:0097009','GO:0030851','GO:0045444']:orth.append({k:r.get(k) for k in ['geneProductId','goId','reference','goEvidence','qualifier','assignedBy','withFrom','taxonId','date']})
 return dict(title='CEBPA source evidence: exact interaction records, bZIP target measurements and ortholog links',source_seed_sha256=sha(seed),intact=intact,bzip=bd,ortholog_records=orth)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--seed',required=True,type=Path);p.add_argument('--source-dir',required=True,type=Path);p.add_argument('--bzip-dir',required=True,type=Path);p.add_argument('--output',required=True,type=Path);args=p.parse_args();args.output.write_text(json.dumps(build(args.seed,args.source_dir,args.bzip_dir),indent=2)+'\n')
