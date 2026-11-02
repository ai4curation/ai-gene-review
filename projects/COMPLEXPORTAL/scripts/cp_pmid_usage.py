"""For each PMID cited on a ComplexPortal-assigned GOA row in genes/, ask QuickGO how many
annotations in all of GOA cite it, and how many of those are assigned by ComplexPortal.

Usage (from repo root):
  uv run python projects/COMPLEXPORTAL/scripts/cp_pmid_usage.py projects/COMPLEXPORTAL/data/cp_pmid_usage.yaml
"""
import csv, glob, sys, time, json, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor
import yaml

API = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"


def hits(params):
    url = API + "?" + urllib.parse.urlencode({**params, "limit": 1})
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)["numberOfHits"]
        except Exception:
            time.sleep(2 ** attempt)
    return None


def usage(pmid):
    total = hits({"reference": pmid})
    cp = hits({"reference": pmid, "assignedBy": "ComplexPortal"})
    return pmid, {"total_annotations": total, "complexportal_annotations": cp}


pmids = set()
for tsv in glob.glob("genes/*/*/*-goa.tsv"):
    for r in csv.DictReader(open(tsv), delimiter="\t"):
        if r.get("ASSIGNED BY") == "ComplexPortal" and r["REFERENCE"].startswith("PMID:"):
            pmids.add(r["REFERENCE"])
with ThreadPoolExecutor(6) as ex:
    out = dict(ex.map(usage, sorted(pmids)))
yaml.safe_dump({"source": "QuickGO annotation search", "pmids": out}, open(sys.argv[1], "w"), sort_keys=True)
print(len(out), "PMIDs;", sum(v["total_annotations"] is None for v in out.values()), "failed")
