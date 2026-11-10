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
TERM_QUERIES = {'nicotinic-term-definitions.json': ['GO:0042472', 'GO:0015643', 'GO:0005102', 'GO:0060079', 'GO:0050910', 'GO:0051899', 'GO:0022848', 'GO:0007274'], 'nicotinic-alpha7-term-definitions.json': ['GO:0017081', 'GO:0042803', 'GO:0009409', 'GO:0051247', 'GO:1902004', 'GO:1905906', 'GO:0005262']}
for name, terms in TERM_QUERIES.items():
    out={}
    for term in terms:
        r=requests.get('https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/'+term,headers={'Accept':'application/json'},timeout=60);r.raise_for_status();out[term]=r.json()['results'][0]
    (ROOT/name).write_text(json.dumps(out,indent=2))
