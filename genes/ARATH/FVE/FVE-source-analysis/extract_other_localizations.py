# /// script
# dependencies = ["requests", "openpyxl", "xlrd"]
# ///
"""Retrieve original supplements and record exact FVE rows, without editing sources."""
from pathlib import Path
import requests,io,zipfile,hashlib,json,openpyxl,xlrd
for pmid,pmc in [('15496452','PMC539170'),('25293756','PMC4247564')]:
 url=f'https://www.ebi.ac.uk/europepmc/webservices/rest/{pmc}/supplementaryFiles'
 report={'pmid':pmid,'source_url':url,'target':'AT2G19520','files':[]}
 try:
  r=requests.get(url,timeout=90);r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content))
  for name in z.namelist():
   raw=z.read(name);entry={'file':name,'sha256':hashlib.sha256(raw).hexdigest(),'matches':[]};report['files'].append(entry)
   if name.endswith('.xlsx'):
    w=openpyxl.load_workbook(io.BytesIO(raw),read_only=True,data_only=True);sheets=[(s.title,s.iter_rows(values_only=True)) for s in w]
   elif name.endswith('.xls'):
    w=xlrd.open_workbook(file_contents=raw);sheets=[(s.name,(s.row_values(i) for i in range(s.nrows))) for s in w.sheets()]
   else:
    if name.endswith(('.html','.htm','.txt','.csv','.xml')):
     t=raw.decode(errors='replace'); lines=t.splitlines();entry['matches']=[{'line':i,'text':v} for i,v in enumerate(lines,1) if any(s in v.upper() for s in ['AT2G19520','O22607','MSI4','NFC4'])]
    continue
   for sheet,rows in sheets:
    for i,row in enumerate(rows,1):
     if any(any(s in str(v).upper() for s in ['AT2G19520','O22607','MSI4','NFC4']) for v in row):entry['matches'].append({'sheet':sheet,'row':i,'values':list(row)})
 except Exception as e:report['access_error']=str(e)
 Path(__file__).with_name(f'localization-{pmid}.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
 print(pmid,[(x['file'],len(x['matches'])) for x in report['files']],report.get('access_error'))
