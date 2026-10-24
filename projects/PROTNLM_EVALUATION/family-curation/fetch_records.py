"""Fetch current exact-accession records for the explicit benchmark scope."""

import concurrent.futures
import csv
import datetime
import gzip
import json
from pathlib import Path

import requests

BASE = Path(__file__).resolve().parent


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json"
    result = {
        "accession": acc,
        "url": url,
        "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    try:
        response = requests.get(url, timeout=90)
        result["status"] = response.status_code
        result["resolved_url"] = response.url
        if response.ok:
            result["record"] = response.json()
        else:
            result["error"] = response.text[:1000]
    except requests.RequestException as error:
        result["status"] = "REQUEST_FAILED"
        result["error"] = str(error)
    return result


def main():
    accessions = sorted(
        {r["accession"] for r in csv.DictReader((BASE / "scope.csv").open())}
    )
    destination = BASE / "uniprot-records.jsonl.gz"
    if destination.exists():
        raise SystemExit(
            "Snapshot already exists; preserve it and use a new dated bundle for refreshes."
        )
    with (
        concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool,
        gzip.open(destination, "wt") as stream,
    ):
        for i, result in enumerate(pool.map(fetch, accessions), 1):
            stream.write(json.dumps(result) + "\n")
            stream.flush()
            if i % 40 == 0 or result["status"] != 200:
                print(i, result["accession"], result["status"], flush=True)


if __name__ == "__main__":
    main()
