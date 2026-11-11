# /// script
# dependencies = ["requests", "openpyxl", "xlrd"]
# ///
"""Retrieve publisher-deposited tables and extract exact Arabidopsis locus matches."""
import hashlib,io,json,zipfile
from pathlib import Path
import requests,openpyxl,xlrd
TARGETS=['AT1G31230','AT4G19710','AT2G17265','AT4G29840','AT1G14810']
report=[]
for pmid,pmc in [('28887381','PMC5672003'),('25293756','PMC4247564'),('20061580','PMC2877971'),('18431481','PMC2291561')]:
 url=f'https://www.ebi.ac.uk/europepmc/webservices/rest/{pmc}/supplementaryFiles';r=requests.get(url,timeout=120)
 entry={'pmid':pmid,'url':url,'http_status':r.status_code,'tables':[]};report.append(entry)
 if not r.ok or not zipfile.is_zipfile(io.BytesIO(r.content)):entry['result']='No usable ZIP returned';continue
 archive=zipfile.ZipFile(io.BytesIO(r.content))
 for name in sorted(archive.namelist()):
  if not name.lower().endswith(('.xls','.xlsx')):continue
  raw=archive.read(name);tab={'file':name,'sha256':hashlib.sha256(raw).hexdigest(),'sheets':[]};entry['tables'].append(tab)
  try:
   if name.endswith('.xlsx'):
    wb=openpyxl.load_workbook(io.BytesIO(raw),read_only=True,data_only=True);sheets=[(s.title,list(s.values)) for s in wb]
   else:
    wb=xlrd.open_workbook(file_contents=raw);sheets=[(s.name,[s.row_values(i) for i in range(s.nrows)]) for s in wb.sheets()]
   for title,rows in sheets:
    if 'raw' in title.lower() or 'gaussian fitted' in title.lower():continue
    matches=[{'excel_row':i+1,'values':list(row)} for i,row in enumerate(rows) if any(t in str(v).upper() for t in TARGETS for v in row)]
    tab['sheets'].append({'sheet':title,'header_rows':rows[:5],'matches':matches})
  except Exception as e:tab['error']=str(e)
Path(__file__).with_name('localization-table-extraction.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
