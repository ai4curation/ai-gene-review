#!/usr/bin/env python3
"""Extract literal target records from the published MitoCoP XLSX and OpenCell CSV.

Python standard library only. Inputs may be supplied locally; --download obtains the
public original sources and authenticates their fixed bytes. No API key is required.
The output contains measurements, not automated GO or interaction verdicts.
"""
import argparse,csv,hashlib,io,json,pathlib,posixpath,re,urllib.request,zipfile
import xml.etree.ElementTree as ET

SOURCES={
 'mitocop':{'sha256':'10690847c50567e11055d474fbe265fe5d699384f38437acd95734f0a87a9183','url':'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8664129/supplementaryFiles','archive_sha256':'ba78a3c662f31266f9712f1f6400b2f181f35c3fb07977269917def7137a5a85','member_suffix':'mmc2.xlsx'},
 'opencell':{'sha256':'a9422ca12b8b5fce52439f247a7439fbc693cb34b4ca45ced597aa02d267e376','url':'https://opencell.czbiohub.org/data/datasets/opencell-protein-interactions.csv'}}
N={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
def digest(b):return hashlib.sha256(b).hexdigest()
def download(key,folder):
 spec=SOURCES[key];req=urllib.request.Request(spec['url'],headers={'User-Agent':'DNMT1-source-extract/1.0'})
 with urllib.request.urlopen(req,timeout=180) as r:b=r.read()
 if key=='mitocop':
  if digest(b)!=spec['archive_sha256']:raise ValueError('Published supplementary archive changed; inspect before updating the pinned source.')
  with zipfile.ZipFile(io.BytesIO(b)) as z:
   names=[x for x in z.namelist() if x.endswith(spec['member_suffix'])]
   if len(names)!=1:raise ValueError('Expected exactly one published mmc2.xlsx')
   b=z.read(names[0])
 if digest(b)!=spec['sha256']:raise ValueError(key+' source hash differs from the inspected original')
 p=folder/('34800366-mmc2.xlsx' if key=='mitocop' else 'OpenCell-protein-interactions.csv');p.write_bytes(b);return p

def column(s):
 n=0
 for c in re.match('[A-Z]+',s)[0]:n=n*26+ord(c)-64
 return n-1

def workbook(path):
 with zipfile.ZipFile(path) as z:
  ss=[]
  if 'xl/sharedStrings.xml' in z.namelist():
   ss=[''.join(x.itertext()) for x in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('s:si',N)]
  rel={x.attrib['Id']:x.attrib['Target'] for x in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
  for sheet in ET.fromstring(z.read('xl/workbook.xml')).findall('s:sheets/s:sheet',N):
   target=rel[sheet.attrib['{'+N['r']+'}id']];target=target.lstrip('/') if target.startswith('/') else posixpath.normpath('xl/'+target)
   rows=[]
   for row in ET.fromstring(z.read(target)).findall('s:sheetData/s:row',N):
    vals={}
    for c in row.findall('s:c',N):
     typ=c.attrib.get('t');v=c.find('s:v',N);v=v.text if v is not None else None
     if typ=='s':v=ss[int(v)] if v is not None else None
     elif typ=='inlineStr':v=''.join(c.find('s:is',N).itertext()) if c.find('s:is',N) is not None else None
     elif typ=='b':v=(v=='1') if v is not None else None
     elif typ not in ('str','e') and v is not None:v=float(v) if any(x in v.lower()for x in '.e')else int(v)
     vals[column(c.attrib['r'])]=v
    width=max(vals,default=-1)+1;rows.append((int(row.attrib['r']),[vals.get(i)for i in range(width)]))
   yield sheet.attrib['name'],rows

def extract(mitocop,opencell,gene):
 for key,p in [('mitocop',mitocop),('opencell',opencell)]:
  if digest(p.read_bytes())!=SOURCES[key]['sha256']:raise ValueError(key+' source hash mismatch')
 hits=[]
 for name,rows in workbook(mitocop):
  if not name.startswith(('(A)','(B)')):continue
  header=next((r for _,r in rows if 'All gene names' in r or 'Gene names' in r or 'Gene name' in r),None)
  if header is None:raise ValueError('No gene-name header in '+name)
  gi=[i for i,x in enumerate(header)if x in ('All gene names','Gene names','Gene name')]
  for number,row in rows:
   if any(gene in str(row[i]).split(';') for i in gi if i<len(row)):
    row=row+[None]*(len(header)-len(row));hits.append({'sheet':name,'excel_row':number,'headers':header,'values':row})
 with opencell.open(newline='',encoding='utf-8-sig') as f:
  records=[{'data_index_zero_based':i,'csv_line_one_based_including_header':i+2,'record':r}for i,r in enumerate(csv.DictReader(f)) if gene in (r.get('target_gene_name'),r.get('interactor_gene_name'))]
 return {'gene':gene,'sources':SOURCES,'mitocop_rows':hits,'opencell_records':records}

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--mitocop',type=pathlib.Path);p.add_argument('--opencell',type=pathlib.Path);p.add_argument('--download',type=pathlib.Path,help='Directory for authenticated original downloads');p.add_argument('--gene',default='DNMT1');p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
 if a.download:a.download.mkdir(parents=True,exist_ok=True)
 m=a.mitocop or (download('mitocop',a.download) if a.download else None);o=a.opencell or(download('opencell',a.download)if a.download else None)
 if m is None or o is None:p.error('Supply both local source paths or --download')
 result=extract(m,o,a.gene);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
 print(json.dumps({'gene':a.gene,'mitocop_rows':len(result['mitocop_rows']),'opencell_records':len(result['opencell_records']),'sha256':digest(a.output.read_bytes())}))
if __name__=='__main__':main()
