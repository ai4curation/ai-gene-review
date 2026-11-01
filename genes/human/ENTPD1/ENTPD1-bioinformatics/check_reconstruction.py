"""Input-driven positive and corrupted-input checks; no network or file writes."""
import argparse,copy,json
from pathlib import Path
from reconstruct_products import reconstruct,fasta_records

def checks(uniprot,fasta):
 record=json.loads(uniprot.read_text());sequences=fasta_records(fasta.read_text())
 result=reconstruct(record,sequences);out={'accession':result['accession'],'positive_products':len(result['products']),'negative_controls':[]}
 def reject(name,r,f):
  try:reconstruct(r,f)
  except ValueError as e:out['negative_controls'].append({'case':name,'rejected':True,'reason':str(e)})
  else:raise AssertionError('Corrupt input accepted: '+name)
 bad=copy.deepcopy(sequences);bad[record['primaryAccession']]='X'+bad[record['primaryAccession']][1:];reject('displayed FASTA mismatch',record,bad)
 variants=[f for f in record.get('features',[]) if f['type']=='Alternative sequence']
 if variants:
  bad=copy.deepcopy(record);v=next(f for f in bad['features'] if f['type']=='Alternative sequence');v.setdefault('alternativeSequence',{})['originalSequence']='X';reject('variant preimage mismatch',bad,sequences)
  bad=copy.deepcopy(record);bad['features']=[f for f in bad['features'] if f.get('featureId')!=variants[0]['featureId']];reject('missing variant definition',bad,sequences)
 bad=copy.deepcopy(sequences);bad['UNEXPECTED']='ABC';reject('extra FASTA record',record,bad)
 return out

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--uniprot',type=Path,required=True);p.add_argument('--fasta',type=Path,required=True);a=p.parse_args();print(json.dumps(checks(a.uniprot,a.fasta),indent=2))
