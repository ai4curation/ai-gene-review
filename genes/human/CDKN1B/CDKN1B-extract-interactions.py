#!/usr/bin/env python3
"""Reproduce the finite CDKN1B evidence projection from authentic downloaded inputs.

Requires PyYAML and openpyxl. Inputs are downloaded files, not live API responses;
the output pins their SHA256 hashes. No biological decisions are inferred here.
"""
import argparse,csv,hashlib,json,re
from pathlib import Path
import yaml,openpyxl

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ids(row,side):return set(re.findall(r'uniprotkb:([^| (]+)','|'.join(row[j] for j in [side,side+2,side+4])))
def main():
 p=argparse.ArgumentParser(description=__doc__)
 for n in ['review','intact','mint','opencell','variant-workbook','output']:p.add_argument('--'+n,type=Path,required=True)
 z=p.parse_args();review=yaml.safe_load(z.review.read_text());sources=[];records={};joins=[]
 fields={0:'identifiers_a',1:'identifiers_b',2:'alternative_identifiers_a',3:'alternative_identifiers_b',4:'aliases_a',5:'aliases_b',6:'method',8:'publication',9:'taxon_a',10:'taxon_b',11:'interaction_type',12:'provider',13:'interaction_ids',15:'expansion',16:'biological_roles_a',17:'biological_roles_b',18:'experimental_roles_a',19:'experimental_roles_b',28:'host',35:'negative',36:'features_a',37:'features_b'}
 for provider,path in [('IntAct',z.intact),('MINT',z.mint)]:
  url=f'https://www.ebi.ac.uk/Tools/webservices/psicquic/{provider.lower()}/webservices/current/search/query/id%3AP46527?format=tab27&maxResults=10000'
  sources.append({'provider':provider,'url':url,'sha256':sha(path),'bytes':path.stat().st_size})
  lines=path.read_text().splitlines();table=list(csv.reader(lines,delimiter='\t'))
  for index,a in enumerate(review['existing_annotations']):
   if not a.get('original_reference_id','').startswith('PMID:'):continue
   pmid=a['original_reference_id'].split(':')[1]
   for entity in a.get('supporting_entities',[]):
    if not entity.startswith('UniProtKB:'):continue
    partner=entity.split(':',1)[1];hits=[]
    for line,row in enumerate(table,1):
     if len(row)<42 or 'pubmed:'+pmid not in row[8] or row[35]=='true':continue
     if not (('P46527' in ids(row,0) and partner in ids(row,1)) or ('P46527' in ids(row,1) and partner in ids(row,0))):continue
     key=provider+':line:'+str(line);hits.append(key)
     records[key]={'source_line':line,'raw_line_sha256':hashlib.sha256(lines[line-1].encode()).hexdigest(),**{v:row[k] for k,v in fields.items()},'record_urls':['https://www.ebi.ac.uk/intact/interaction/'+v for v in re.findall(r'EBI-\d+',row[13])]}
    joins.append({'index':index,'reference_id':a['original_reference_id'],'partner':entity,'provider':provider,'positive_record_keys':hits})
 oc=list(csv.DictReader(z.opencell.open()));oc=[r for r in oc if r.get('target_gene_name')=='CDK2' and r.get('interactor_gene_name')=='CDKN1B']
 wb=openpyxl.load_workbook(z.variant_workbook,read_only=True,data_only=True);variants=[]
 for sheet in wb:
  rows=list(sheet.values)
  for num,row in enumerate(rows,1):
   if any(str(v)=='CDKN1B' for v in row):variants.append({'sheet':sheet.title,'excel_row':num,'header':list(rows[0]),'values':list(row)})
 out={'title':'CDKN1B interaction evidence: exact source-linked records and assay scope','target':'UniProtKB:P46527','index_convention':'zero-based existing_annotations index; source objects are preserved in the review','scope':'Positive source-linked curated records are evidence of the specified assay, not independent replication. Co-purification and proximity do not by themselves establish isolated direct contact. Feature-free pooling records are not WT confirmation; the 2015 workbook provides the explicit WT/I119T comparison. No long author-comment prose is copied.','sources':sources,'joins':joins,'records':records,'OpenCell':{'reference_id':'PMID:35271311','url':'https://opencell.czbiohub.org/data/datasets/opencell-protein-interactions.csv','sha256':sha(z.opencell),'rows':oc},'variant_table':{'reference_id':'PMID:25910212','url':'https://ars.els-cdn.com/content/image/1-s2.0-S0092867415004304-mmc3.xlsx','sha256':sha(z.variant_workbook),'target_rows':variants}}
 z.output.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
if __name__=='__main__':main()
