#!/usr/bin/env python3
"""Reproduce source-provenance queries; requires requests, no GO qualifiers used."""
import json
from pathlib import Path
import requests
ROOT=Path(__file__).resolve().parent
FIELDS=['geneProductId','symbol','goId','reference','goEvidence','withFrom','assignedBy']
for name,accessions in [('nicotinic-donor-trace.json',['P12389','Q91X60','Q8R4G9','P04757','Q9R0W9','Q8BMN3','Q2MKA5','Q8R493']),('nicotinic-alpha7-donor-trace.json',['P49582','Q05941','Q866A2'])]:
    out={}
    for ac in accessions:
        entries=[];page=1;total=1;urls=[]
        while len(entries)<total:
            r=requests.get('https://www.ebi.ac.uk/QuickGO/services/annotation/search',params={'geneProductId':'UniProtKB:'+ac,'limit':200,'page':page},headers={'Accept':'application/json'},timeout=60)
            r.raise_for_status();j=r.json();total=j['numberOfHits'];urls.append(r.url)
            entries.extend({k:x.get(k) for k in FIELDS} for x in j['results'])
            if not j['results']:break
            page+=1
        out[ac]={'urls':urls,'total':total,'annotations':entries}
    (ROOT/name).write_text(json.dumps(out,indent=2))
for name in ['nicotinic-term-definitions.json','nicotinic-alpha7-term-definitions.json']:
    old=json.loads((ROOT/name).read_text());out={}
    for term in old:
        r=requests.get('https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/'+term,headers={'Accept':'application/json'},timeout=60);r.raise_for_status();out[term]=r.json()['results'][0]
    (ROOT/name).write_text(json.dumps(out,indent=2))
