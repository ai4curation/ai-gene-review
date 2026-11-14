from pathlib import Path
import json
import requests
import hashlib
import xml.etree.ElementTree as ET
import concurrent.futures
import subprocess

P = Path(".cache/module-audit-logs/mla-preflight-20261107")
ids = [
    "36518166",
    "33837253",
    "30638443",
    "34873038",
    "39080293",
    "32602838",
    "30845186",
    "31235958",
]
url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
r = requests.get(
    url,
    params={
        "query": " OR ".join("EXT_ID:" + i for i in ids),
        "format": "json",
        "pageSize": 50,
    },
    timeout=60,
)
(P / "primary-metadata.json").write_bytes(r.content)
data = r.json()["resultList"]["result"]
pcms = [x["pmcid"] for x in data if x.get("pmcid")] + ["PMC6717313"]


def acquire(pmc):
    for suffix, url in [
        ("xml", f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmc}/fullTextXML"),
        ("html", f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/?report=xml"),
    ]:
        r = requests.get(url, timeout=60)
        f = P / (pmc + "." + suffix)
        f.write_bytes(r.content)
        rec = {
            "url": url,
            "status": r.status_code,
            "path": str(f),
            "sha256": hashlib.sha256(r.content).hexdigest(),
            "full_body_present": False,
        }
        try:
            root = ET.fromstring(r.content)
            body = root.find("body")
            rec["full_body_present"] = body is not None
            if body is not None:
                (P / (pmc + ".txt")).write_text(
                    "\n\n".join(
                        "".join(e.itertext()) for e in root.findall(".//body//p")
                    )
                )
                rec["title"] = "".join(root.find(".//article-title").itertext())
                return pmc, rec
        except ET.ParseError:
            pass
    return pmc, rec


results = dict(concurrent.futures.ThreadPoolExecutor(max_workers=3).map(acquire, pcms))
(P / "source-access-2.json").write_text(json.dumps(results, indent=2) + "\n")
print(json.dumps({k: v["full_body_present"] for k, v in results.items()}))
r = subprocess.check_output(
    [
        "gh",
        "api",
        "repos/ai4curation/ai-gene-review/pulls/5076/files?per_page=100",
        "--paginate",
        "--slurp",
    ],
    text=True,
)
patch = [
    x
    for page in json.loads(r)
    for x in page
    if x["filename"]
    == "modules/bacterial_mla_intermembrane_phospholipid_transport.yaml"
]
(P / "pr5076-mla-file.json").write_text(json.dumps(patch, indent=2) + "\n")
print("PR5076 patch", patch[0].get("patch", "")[:2000])
