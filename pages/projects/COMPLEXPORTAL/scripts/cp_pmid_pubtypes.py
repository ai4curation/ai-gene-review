"""Add PubMed publication types to cp_pmid_usage.yaml (NCBI E-utilities esummary).

Usage (from repo root):
  uv run python projects/COMPLEXPORTAL/scripts/cp_pmid_pubtypes.py projects/COMPLEXPORTAL/data/cp_pmid_usage.yaml
"""
import json, sys, time, urllib.request
import yaml

path = sys.argv[1]
d = yaml.safe_load(open(path))
ids = [p.split(":")[1] for p in d["pmids"]]
for i in range(0, len(ids), 150):
    chunk = ids[i:i + 150]
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(chunk)
    res = None
    for attempt in range(5):
        try:
            res = json.load(urllib.request.urlopen(url, timeout=60))["result"]
            break
        except Exception:
            time.sleep(2 ** attempt)
    if res is None:
        print(f"chunk starting {chunk[0]}: all retries failed; left untyped", file=sys.stderr)
        continue
    for uid in res.get("uids", []):
        d["pmids"]["PMID:" + uid]["pubtype"] = res[uid].get("pubtype", [])
        d["pmids"]["PMID:" + uid]["year"] = res[uid].get("pubdate", "")[:4]
    time.sleep(0.5)
yaml.safe_dump(d, open(path, "w"), sort_keys=True)
print(sum("pubtype" in v for v in d["pmids"].values()), "of", len(ids), "typed")
