import json, urllib.parse, urllib.request, sys
Q = {
 "title_go": 'TITLE:"gene ontology" OR TITLE:"GO annotation*" OR TITLE:"GO-CAM"',
 "abstract_curation": 'ABSTRACT:("GO annotation" OR "GO annotations" OR "Gene Ontology annotation" OR "GO curation") AND (ABSTRACT:guideline* OR ABSTRACT:"best practice*" OR ABSTRACT:curators OR ABSTRACT:biocurat*)',
 "eco_paint_biocuration": '(TITLE:"evidence and conclusion ontology" OR TITLE:"evidence ontology") OR (TITLE:phylogenetic AND TITLE:annotation AND ABSTRACT:"gene ontology") OR (TITLE:biocuration AND ABSTRACT:"gene ontology") OR (TITLE:"annotation extension*")',
 "go_handbook": 'TITLE:"gene ontology handbook" OR (ISSN:"1064-3745" AND TITLE:"gene ontology" AND PUB_YEAR:2017)',
}
out = {}
for qname, q in Q.items():
    cursor = "*"
    while True:
        url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(
            {"query": q, "format": "json", "resultType": "core", "pageSize": 1000, "cursorMark": cursor})
        j = json.load(urllib.request.urlopen(url))
        for r in j["resultList"]["result"]:
            key = r.get("pmid") and f"PMID:{r['pmid']}" or (r.get("doi") and f"DOI:{r['doi']}") or f"{r['source']}:{r['id']}"
            e = out.setdefault(key, {"id": key, "title": r.get("title"), "year": r.get("pubYear"),
                 "journal": (r.get("journalInfo") or {}).get("journal", {}).get("title") or r.get("bookOrReportDetails", {}).get("publisher"),
                 "authors": r.get("authorString", "")[:200], "doi": r.get("doi"), "pubtype": r.get("pubTypeList", {}).get("pubType"),
                 "abstract": r.get("abstractText", ""), "queries": []})
            e["queries"].append(qname)
        nc = j.get("nextCursorMark")
        if not nc or nc == cursor or not j["resultList"]["result"]: break
        cursor = nc
json.dump(list(out.values()), open(sys.argv[1], "w"), indent=1)
print(len(out))
