# /// script
# dependencies = ["requests", "openpyxl", "xlrd"]
# ///
import requests,zipfile,io,openpyxl,xlrd,json,hashlib
from pathlib import Path
sources={'17151019':'PMC2391258','21533090':'PMC3080382','22430844':'PMC3375956','31519798':'PMC6881120','20061580':'PMC2877971'}
targets=['AT5G19550','AT5G65010','AT1G17290','AT4G31990','AT2G22250']
out=[]
for pm,pc in sources.items():
 url=f'https://www.ebi.ac.uk/europepmc/webservices/rest/{pc}/supplementaryFiles'
 r=requests.get(url,timeout=90);e={'pmid':pm,'url':url,'http_status':r.status_code,'tables':[]};out.append(e)
 try:z=zipfile.ZipFile(io.BytesIO(r.content))
 except Exception:print(pm,r.status_code,'not zip',flush=True);continue
 for n in z.namelist():
  if not n.endswith(('.xlsx','.xls')):continue
  b=z.read(n);tables={}
  try:
   if n.endswith('.xlsx'):tables={s.title:list(s.values) for s in openpyxl.load_workbook(io.BytesIO(b),read_only=True,data_only=True)}
   else:
    w=xlrd.open_workbook(file_contents=b);tables={s.name:[s.row_values(i) for i in range(s.nrows)] for s in w.sheets()}
  except Exception as ex:print(n,str(ex),flush=True);continue
  for sn,rows in tables.items():
   matches=[{'row':i+1,'values':list(row)} for i,row in enumerate(rows) if any(t in str(v).upper() for t in targets for v in row)]
   if matches:e['tables'].append({'name':n,'sha256':hashlib.sha256(b).hexdigest(),'sheet':sn,'headers':rows[:8],'matches':matches})
 print(pm,[(t['name'],len(t['matches'])) for t in e['tables']],flush=True)
Path('genes/ARATH/ASP2/ASP2-source-analysis/additional-table-extraction.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
