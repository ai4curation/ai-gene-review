"""Archive official PANTHER trees/MSAs within this consultation only."""

import concurrent.futures
import gzip
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import requests

P = Path(__file__).resolve().parent
FAMILIES = [
    "PTHR" + x
    for x in ["11601", "11933", "33279", "34874", "37010", "37526", "38780", "43586"]
]


def acquire(job):
    family, endpoint = job
    path = P / f"{family}-{endpoint}.json.gz"
    assert not path.exists(), path
    url = f"https://www.pantherdb.org/services/oai/pantherdb/{endpoint}"
    try:
        response = requests.get(url, params={"family": family}, timeout=90)
        path.write_bytes(gzip.compress(response.content, mtime=0))
        return {
            "family": family,
            "endpoint": endpoint,
            "url": response.url,
            "status": response.status_code,
            "path": path.name,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "retrieved": datetime.now(timezone.utc).isoformat(),
        }
    except requests.RequestException as error:
        return {
            "family": family,
            "endpoint": endpoint,
            "url": url,
            "error": str(error),
            "retrieved": datetime.now(timezone.utc).isoformat(),
        }


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    rows = list(
        pool.map(acquire, [(f, e) for f in FAMILIES for e in ["treeinfo", "familymsa"]])
    )
(P / "phylogeny-acquisition.json").write_text(json.dumps(rows, indent=2) + "\n")
print(json.dumps(rows, indent=2))
