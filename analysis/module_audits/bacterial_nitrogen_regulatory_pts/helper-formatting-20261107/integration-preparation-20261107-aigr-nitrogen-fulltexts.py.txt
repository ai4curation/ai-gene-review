import urllib.request,urllib.parse,json,hashlib,datetime,xml.etree.ElementTree as ET,concurrent.futures
from pathlib import Path
w=Path('/private/tmp/aigr-nitrogen-pts-taxon-audit');c=w/'analysis/module_audits/bacterial_nitrogen_regulatory_pts/literature-acquisition-20261107';c.mkdir(exist_ok=True)
items=[('18296519','PMC2347394'),('17416664','PMC1913348'),('26224366',None),('21236318',None),('27109061','PMC4848567'),('24633875',None),('41870250','PMC13104625')]
def fetch(pair):
 pmid,pmc=pair; attempts=[];d=None
 try:
  u='https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urllib.parse.urlencode({'query':'EXT_ID:'+pmid+' AND SRC:MED','format':'json','resultType':'core'})
  with urllib.request.urlopen(u,timeout=25) as f:b=f.read()
  d=json.loads(b);rs=d['resultList']['result'];r=rs[0] if rs else {};pmc=pmc or r.get('pmcid');attempts.append({'url':u,'status':200})
 except Exception as e:attempts.append({'url':u,'error':str(e)})
 raw=None
 if pmc:
  u=f'https://www.ebi.ac.uk/europepmc/webservices/rest/{pmc}/fullTextXML'
  try:
   with urllib.request.urlopen(u,timeout=25) as f:raw=f.read()
   xml=ET.fromstring(raw);ids=[x.text for x in xml.findall('.//article-id[@pub-id-type="pmid"]')];assert pmid in ids,(pmid,ids)
   attempts.append({'url':u,'status':200,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
  except Exception as e:attempts.append({'url':u,'error':str(e)});raw=None
 return pmid,pmc,d,raw,attempts
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: results=list(ex.map(fetch,items))
for pmid,pmc,metadata,raw,attempts in results:
 receipt={'pmid':pmid,'pmcid':pmc,'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'attempts':attempts,'canonical_cache_modified':False}
 if metadata:(c/f'PMID_{pmid}-metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
 if raw:
  (c/f'PMID_{pmid}-fulltext.xml').write_bytes(raw);xml=ET.fromstring(raw)
  lines=[]
  for n in xml.iter():
   if n.tag in ('article-title','title','p','table'):lines.append(''.join(n.itertext()))
  text='\n\n'.join(lines)+'\n';(c/f'PMID_{pmid}-fulltext.txt').write_text(text)
  receipt.update(fulltext=True,extraction='ElementTree itertext on article-title,title,p,table; source XML retained',text_sha256=hashlib.sha256(text.encode()).hexdigest())
 else:receipt['fulltext']=False
 (c/f'PMID_{pmid}-retrieval.json').write_text(json.dumps(receipt,indent=2)+'\n');print(pmid,'fulltext',bool(raw),'errors',[a.get('error') for a in attempts if 'error' in a],flush=True)
