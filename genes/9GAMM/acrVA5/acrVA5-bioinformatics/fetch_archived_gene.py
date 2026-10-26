#!/usr/bin/env python3
"""Fetch version-pinned AcrVA5 source records with the normal GOA/seed pipeline.

Run from repository root: uv run python genes/9GAMM/acrVA5/acrVA5-bioinformatics/fetch_archived_gene.py
Current UniProt endpoints return deleted records. This wrapper replaces only the
UniProt transport with a real, pinned UniSave request; the repository's normal
fetch_gene_data function still writes all source files and seeds GOA unchanged.
No biological decisions are generated here. Existing reviews are preserved.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
import requests
import yaml
from ai_gene_review.etl import gene as etl

RECORDS=[('acrVA5','A0A0U2B867',17)]
ROOT=Path(__file__).resolve().parents[4]

def main():
 for symbol,accession,version in RECORDS:
  url=f'https://rest.uniprot.org/unisave/{accession}?format=txt&versions={version}'
  response=requests.get(url,timeout=90);response.raise_for_status();record=response.text
  # UniSave returns the original record followed by a history-comment trailer.
  # Extract its flat-file block deterministically, retaining all record lines.
  match=re.search(r'^ID   .*?^//\s*$',record,re.M|re.S)
  if not match:raise ValueError(f'No complete archived flat file for {accession}')
  flat=match.group().rstrip()+'\n'
  if not re.search(r'^AC   '+re.escape(accession)+r';',flat,re.M):raise ValueError('Accession mismatch')
  if 'NCBI_TaxID=386891' not in flat:raise ValueError('Unexpected archived taxon')
  metadata=requests.get(f'https://rest.uniprot.org/unisave/{accession}?format=json',timeout=90);metadata.raise_for_status()
  versions=metadata.json()['results'];entry=next(x for x in versions if x['entryVersion']==version)
  folder=ROOT/'genes'/'9GAMM'/symbol;folder.mkdir(parents=True,exist_ok=True)
  snapshot={'accession':accession,'retrieved_at':datetime.now(timezone.utc).isoformat(),'source_url':url,'current_record_status':'Deleted from current UniProtKB; archival identity retained','unisave_records':[{'entry_version':version,'sequence_version':entry.get('sequenceVersion'),'first_release':entry['firstRelease'],'first_release_date':entry['firstReleaseDate'],'last_release':entry['lastRelease'],'last_release_date':entry['lastReleaseDate'],'record_sha256':hashlib.sha256(flat.encode()).hexdigest(),'record_text':flat}]}
  (folder/f'{symbol}-record-evidence.yaml').write_text(yaml.safe_dump(snapshot,sort_keys=False,allow_unicode=True,width=100))
  if '--snapshots-only' in sys.argv:
   print(symbol, accession, 'refreshed archival metadata only')
   continue
  original=etl.fetch_uniprot_data
  def versioned_fetch(requested,*,_acc=accession,_flat=flat):
   if requested!=_acc:raise ValueError(f'Unexpected accession requested: {requested}')
   return _flat
  try:
   etl.fetch_uniprot_data=versioned_fetch
   result=etl.fetch_gene_data(('9GAMM',symbol),uniprot_id=accession,base_path=ROOT,force=True)
  finally:
   etl.fetch_uniprot_data=original
  print(symbol,accession,f'UniSave version {version}',json.dumps(result))

if __name__=='__main__':main()
