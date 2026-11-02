#!/usr/bin/env python3
"""Generate the CDH1 interaction extract from authentic archived inputs.

Requires PyYAML. This offline transformation performs exact accession/publication
joins against raw PSI-MITAB responses, retains assay fields and raw-line hashes,
and selects the literal OpenCell CTNNB1-bait/CDH1-prey row. It does not fetch or
manufacture records. Supply the baseline review and GOA that were used for source
indexing, the current reviewed YAML, raw response directory and official OpenCell
CSV plus retrieval receipt. Retrieval URLs/hashes remain in the resulting JSON.
The primary_assay_resolutions section is explicitly reviewer-supplied prose;
provider records are literal source fields, not independent replications.
"""
import argparse,csv,hashlib,json,re
from pathlib import Path
import yaml

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def ids(row,k):return set(re.findall(r'uniprotkb:([^| (]+)','|'.join(row[j]for j in [k,k+2,k+4])))
def main():
 p=argparse.ArgumentParser(description=__doc__)
 for key in ['baseline-yaml','baseline-goa','review-yaml','source-dir','opencell-csv','opencell-receipt','output']:p.add_argument('--'+key,type=Path,required=True)
 a=p.parse_args();before=yaml.safe_load(a.baseline_yaml.read_text());review=yaml.safe_load(a.review_yaml.read_text());goa=list(csv.DictReader(a.baseline_goa.open(),delimiter='\t'));mapping=[]
 for i,row in enumerate(before['existing_annotations']):
  if row['term']['id']=='GO:0005515':mapping.append({'index':i,'source_before':{k:v for k,v in row.items()if k!='review'},'matching_original_goa_rows':[g for g in goa if g['GO TERM']==row['term']['id']and g['REFERENCE']==row['original_reference_id']and g['GO EVIDENCE CODE']==row['evidence_type']]})
 result={'gene':'CDH1','uniprot':'P12830','schema_version':1,'scope':'Literal selected source-linked interaction records and original partner mapping. These records share provenance with GOA and are not independent experimental replication. Negative database lookups are not negative biological evidence. Original YAML source fields are not backfilled or rewritten.','baseline_yaml_sha256':sha(a.baseline_yaml),'baseline_goa_sha256':sha(a.baseline_goa),'original_generic_assertions':mapping,'providers':{}}
 for name in ['IntAct','MINT']:
  rawpath=a.source_dir/('binding-intact.tsv'if name=='IntAct'else'binding-mint.tsv');raw=list(csv.reader(rawpath.open(),delimiter='\t'));lines=rawpath.read_text().splitlines();rows=[];records={}
  receipt=json.loads((a.source_dir/('binding-retrieval.json'if name=='IntAct'else'binding-mint-retrieval.json')).read_text())
  if name=='IntAct':receipt=receipt[0]
  assert receipt['sha256']==sha(rawpath),'Raw provider response differs from its retrieval receipt'
  for source in mapping:
   pm=source['source_before']['original_reference_id'].split(':')[1];pairs=[]
   for g in source['matching_original_goa_rows']:
    partner=g['WITH/FROM'].split(':',1)[1];hits=[]
    for line,r in enumerate(raw,1):
     if len(r)<42 or 'pubmed:'+pm not in r[8]or r[35]=='true':continue
     if not(('P12830'in ids(r,0)and partner in ids(r,1))or('P12830'in ids(r,1)and partner in ids(r,0))):continue
     key=r[13];hits.append(key)
     records[key]=dict(source_line=line,identifiers_a=r[0],identifiers_b=r[1],alternative_identifiers_a=r[2],alternative_identifiers_b=r[3],method=r[6],publication=r[8],taxon_a=r[9],taxon_b=r[10],interaction_type=r[11],provider=r[12],interaction_ids=key,expansion=r[15],biological_roles_a=r[16],biological_roles_b=r[17],experimental_roles_a=r[18],experimental_roles_b=r[19],host=r[28],negative=r[35],features_a=r[36],features_b=r[37],record_urls=['https://www.ebi.ac.uk/intact/interaction/'+v for v in re.findall(r'EBI-\d+',key)],raw_line_sha256=hashlib.sha256(lines[line-1].encode()).hexdigest())
    pairs.append(dict(partner=partner,exact_positive_records=sorted(set(hits))))
   rows.append(dict(index=source['index'],pmid=pm,pairs=pairs))
  result['providers'][name]={'query_receipt':receipt,'assertion_joins':rows,'records':records}
 selected=[r for r in csv.DictReader(a.opencell_csv.open())if r['target_gene_name']=='CTNNB1'and r['interactor_gene_name']=='CDH1'];assert len(selected)==1
 result['opencell']={'source_pmid':'35271311','source_file_sha256':sha(a.opencell_csv),'retrieval_receipt':json.loads(a.opencell_receipt.read_text()),'selected_rows':selected,'scope':'CTNNB1 bait / CDH1 prey protein group. P12830-2 occurs within a multi-accession prey group and is not separately resolved. Association is AP-MS, not a purified interface.'}
 result['source_identity_exceptions']=[{'original_index':i,'action':'REMOVE','reason':'Primary experimental construct identifies APC/C coactivator FZR1/Cdh1, not E-cadherin. A curated accession mapping does not override construct identity.'}for i in [43,44,189]]
 result['primary_assay_resolutions']=[{'index':i,'reference_id':review['existing_annotations'][i]['original_reference_id'],'summary':review['existing_annotations'][i]['review']['summary'],'limits':review['existing_annotations'][i]['review'].get('reason','')}for i in [33,37,38,39,46,47,49,54,130,139,141,172,183]]
 a.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
if __name__=='__main__':main()
