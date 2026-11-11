"""Compare the Drosophila Sec71 entry with the ComplexPortal SEC62-SEC63 complex
record that lists it, and with yeast SEC71 (the Sec63-complex subunit).

Usage: python check_complexportal.py
Prints the ComplexPortal participants and the length / domain / TM features of
fly Sec71 (Q9VJW1) and the S. cerevisiae SEC71 entry, fetched live.
"""
import json
import urllib.parse
import urllib.request

def get(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read().decode()

cpx = json.loads(get("https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-26617"))
print("ComplexPortal CPX-26617:", cpx.get("name"), "|", cpx.get("species"))
for p in cpx.get("participants", []):
    print("  participant:", p.get("identifier"), p.get("name"), "|", p.get("description"))
for x in cpx.get("crossReferences", []):
    if x.get("database") in ("pubmed", "gene ontology", "evidence ontology"):
        print("  xref:", x.get("database"), x.get("identifier"), x.get("description") or "")

def summarise(query):
    q = urllib.parse.urlencode({"query": query, "format": "json", "size": "5",
                                "fields": "accession,gene_primary,organism_name,length,ft_transmem,xref_pfam,protein_name"})
    d = json.loads(get("https://rest.uniprot.org/uniprotkb/search?" + q))
    for r in d.get("results", []):
        acc = r["primaryAccession"]
        gene = (r.get("genes") or [{}])[0].get("geneName", {}).get("value")
        org = r["organism"]["scientificName"]
        length = r["sequence"]["length"]
        tm = [f for f in r.get("features", []) if f["type"] == "Transmembrane"]
        pfam = [x["id"] + ":" + next((p["value"] for p in x.get("properties", []) if p["key"] == "EntryName"), "")
                for x in r.get("uniProtKBCrossReferences", []) if x["database"] == "Pfam"]
        name = r.get("proteinDescription", {}).get("recommendedName", r.get("proteinDescription", {}).get("submissionNames", [{}])[0] if r.get("proteinDescription", {}).get("submissionNames") else {}).get("fullName", {}).get("value")
        print(f"  {acc} {gene} [{org}] length={length} TM_segments={len(tm)} Pfam={pfam} name={name}")

print("Drosophila Sec71 (Q9VJW1):")
summarise("accession:Q9VJW1")
print("S. cerevisiae SEC71:")
summarise("gene_exact:SEC71 AND organism_id:559292")
