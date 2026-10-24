"""Freeze InterPro family descriptions and PANTHER metadata for benchmark families."""

import concurrent.futures
import datetime
import json
from pathlib import Path

import requests
import yaml

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]


def fetch_one(family):
    result = {
        "family": family,
        "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    path = ROOT / "interpro/panther" / family / f"{family}-metadata.yaml"
    if path.exists():
        data = yaml.safe_load(path.read_text())
        result["panther_source_file"] = str(path.relative_to(ROOT))
        result["panther"] = data
    else:
        url = f"https://www.ebi.ac.uk/interpro/api/entry/panther/{family}/"
        result["panther_url"] = url
        try:
            response = requests.get(url, timeout=60)
            result["panther_status"] = response.status_code
            if response.ok:
                result["panther"] = response.json()
        except requests.RequestException as error:
            result["panther_error"] = str(error)
    integrated = result.get("panther", {}).get("metadata", {}).get("integrated")
    if integrated:
        url = f"https://www.ebi.ac.uk/interpro/api/entry/interpro/{integrated}/"
        result["interpro_url"] = url
        try:
            response = requests.get(url, timeout=60)
            result["interpro_status"] = response.status_code
            if response.ok:
                result["interpro"] = response.json()
        except requests.RequestException as error:
            result["interpro_error"] = str(error)
    return result


def main():
    families = sorted(json.loads((BASE / "family-groups.json").read_text()))
    destination = BASE / "family-sources"
    destination.mkdir(exist_ok=True)
    needed = [f for f in families if not (destination / f"{f}.json").exists()]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for i, result in enumerate(pool.map(fetch_one, needed), 1):
            (destination / f"{result['family']}.json").write_text(
                json.dumps(result, indent=2) + "\n"
            )
            if i % 25 == 0:
                print(i, result["family"], flush=True)


if __name__ == "__main__":
    main()
