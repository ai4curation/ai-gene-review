"""Compact authentic evidence acquisition confined to the read-only preflight cache."""

import concurrent.futures
import gzip
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

import requests

P = Path(__file__).resolve().parent


def get(job):
    name, url = job
    r = requests.get(url, timeout=60)
    path = P / name
    if path.exists():
        raise RuntimeError(f"Refuse overwrite {path}")
    data = r.content
    path.write_bytes(gzip.compress(data, mtime=0) if name.endswith(".gz") else data)
    result = {
        "path": name,
        "url": r.url,
        "status": r.status_code,
        "response_sha256": hashlib.sha256(data).hexdigest(),
        "file_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "retrieved": "2026-11-07",
    }
    if r.status_code == 200 and "/fullTextXML" in url:
        try:
            doc = ET.fromstring(data)
            text = "\n".join(
                " ".join(e.itertext())
                for e in doc.iter()
                if e.tag in ["article-title", "p", "table", "caption", "sec-title"]
            )
            (P / name.replace(".xml.gz", ".txt")).write_text(text)
            result["article_type"] = doc.attrib.get("article-type")
            result["ids"] = {
                e.attrib.get("pub-id-type"): e.text
                for e in doc.findall(".//article-id")
            }
        except ET.ParseError:
            result["parse_error"] = True
    return result


if __name__ == "__main__":
    jobs = [
        (
            p + ".xml.gz",
            f"https://www.ebi.ac.uk/europepmc/webservices/rest/{p}/fullTextXML",
        )
        for p in ["PMC11784392", "PMC3980101", "PMC4420905", "PMC13066941"]
    ]
    jobs += [("9HLV-entry.json", "https://data.rcsb.org/rest/v1/core/entry/9HLV")]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(get, jobs))
    (P / "acquisition.json").write_text(json.dumps(results, indent=2) + "\n")
    print(results)
