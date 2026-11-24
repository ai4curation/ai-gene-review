"""Fetch MF GO xrefs (with evidence) for a list of UniProt accessions via the /accessions endpoint."""
import requests, json, sys, time
from concurrent.futures import ThreadPoolExecutor
accs=[l.strip() for l in open(sys.argv[1]) if l.strip()]; out=open(sys.argv[2],"a")
B=200
def get(chunk):
    url="https://rest.uniprot.org/uniprotkb/accessions"
    for a in range(8):
        try:
            r=requests.get(url,params={"accessions":",".join(chunk),"fields":"accession,organism_id,go","format":"json","size":B},timeout=180)
            r.raise_for_status(); return r.json()["results"]
        except Exception as e:
            print("retry",a,str(e)[:100],file=sys.stderr,flush=True); time.sleep(2**a)
    print("FAILED chunk",chunk[0],file=sys.stderr,flush=True); return []
n=0
with ThreadPoolExecutor(6) as ex:
    for res in ex.map(get,[accs[i:i+B] for i in range(0,len(accs),B)]):
        for e in res:
            go=[]
            for x in e.get("uniProtKBCrossReferences",[]):
                if x["database"]=="GO":
                    p={q["key"]:q["value"] for q in x["properties"]}
                    if p.get("GoTerm","").startswith("F:"): go.append([x["id"],p.get("GoEvidenceType")])
            out.write(json.dumps({"ac":e["primaryAccession"],"taxon":e.get("organism",{}).get("taxonId"),"mf":go})+"\n"); n+=1
        out.flush(); print(n,file=sys.stderr,flush=True)
print("done",n,file=sys.stderr)
