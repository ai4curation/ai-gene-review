# /// script
# dependencies = ["requests", "openpyxl"]
# ///
"""Reproduce target-row extraction from the publisher-deposited PMC supplement."""
import hashlib,io,json,zipfile
from pathlib import Path
import requests,openpyxl
url='https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5672003/supplementaryFiles'
r=requests.get(url,timeout=120);r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content))
report={'source_url':url,'pmid':'28887381','pmcid':'PMC5672003','target':'AT3G57560','tables':[]}
for name in sorted(z.namelist()):
 if not name.endswith('.xlsx'):continue
 raw=z.read(name);w=openpyxl.load_workbook(io.BytesIO(raw),read_only=True,data_only=True);matches=[]
 for sheet in w:
  for i,row in enumerate(sheet.iter_rows(values_only=True),1):
   if any('AT3G57560' in str(v).upper() for v in row):
    matches.append({'sheet':sheet.title,'excel_row':i,'values':list(row)})
 report['tables'].append({'file':name,'sha256':hashlib.sha256(raw).hexdigest(),'matches':matches})
out=Path(__file__).parent/'membrane-table-extraction.json';out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
