python3 -I - <<'PY'
from pathlib import Path
import urllib.request,urllib.parse,json,concurrent.futures,datetime
out=Path('analysis/module_audits/bacterial_nonhomologous_end_joining/setup-20261107');out.mkdir(exist_ok=True)
queries={a:'https://rest.uniprot.org/uniprotkb/'+a+'.json' for a in ['Q88HU8','Q88HU3','Q9I1W5','Q9I1X7','P9WKD9','P9WNV3']}
queries['bacillus']='https://rest.uniprot.org/uniprotkb/search?'+urllib.parse.urlencode({'query':'(organism_id:224308) AND (gene_exact:ykoU OR gene_exact:ykoV OR gene_exact:ku OR gene_exact:ligD)','format':'json','size':20})
def get(kv):
 key,url=kv
 with urllib.request.urlopen(url,timeout=30) as r:data=json.load(r)
 (out/(key+'-uniprot.json')).write_text(json.dumps({'url':url,'reacquired_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'response':data},indent=2)+'\n')
 rows=data.get('results',[data]);return [{'accession':x['primaryAccession'],'entry':x['uniProtkbId'],'organism':x['organism'],'genes':x.get('genes',[])} for x in rows]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:
 for rows in e.map(get,queries.items()):
  for r in rows:print(json.dumps(r))
PY
