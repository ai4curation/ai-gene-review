from pathlib import Path
import concurrent.futures
import hashlib
import json
import requests
import xml.etree.ElementTree as ET

P = Path(".cache/module-audit-logs/mla-preflight-20261107")
ids = [
    "PMC10212509",
    "PMC11131202",
    "PMC12981311",
    "PMC7981291",
    "PMC7500953",
    "PMC12002339",
]


def get(pmc):
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmc}/fullTextXML"
    try:
        r = requests.get(url, timeout=60)
        (P / (pmc + ".xml")).write_bytes(r.content)
        result = {
            "url": url,
            "status": r.status_code,
            "path": str(P / (pmc + ".xml")),
            "sha256": hashlib.sha256(r.content).hexdigest(),
        }
        try:
            root = ET.fromstring(r.content)
            body = root.find("body")
            result["full_body_present"] = body is not None
            result["pmid"] = root.findtext('.//article-id[@pub-id-type="pmid"]')
            result["doi"] = root.findtext('.//article-id[@pub-id-type="doi"]')
            result["title"] = "".join(root.find(".//article-title").itertext())
            (P / (pmc + ".txt")).write_text(
                "\n\n".join("".join(e.itertext()) for e in root.findall(".//body//p"))
            )
        except (ET.ParseError, AttributeError):
            result["full_body_present"] = False
    except Exception as e:
        result = {"url": url, "error": str(e)}
    return pmc, result


results = dict(concurrent.futures.ThreadPoolExecutor(max_workers=3).map(get, ids))
(P / "source-access-1.json").write_text(json.dumps(results, indent=2) + "\n")
print(json.dumps(results, indent=2))
