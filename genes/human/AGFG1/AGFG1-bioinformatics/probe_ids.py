"""Probe which gene-product identifier forms QuickGO's annotation search accepts.

A rejected query and an empty result look identical downstream, so every zero
needs a nearby non-zero from the same endpoint in the same call pattern. The
positive control here is UniProtKB:P52594 (AGFG1 itself), which is known to have
annotations.

Usage: uv run python probe_ids.py
"""

from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request

CANDIDATES = [
    "UniProtKB:P52594",  # positive control - must be HTTP 200 with hits > 0
    "UniProtKB:Q8K2K6",  # mouse Agfg1
    "MGI:MGI:1333754",
    "MGI:1333754",
    "FB:FBgn0020304",
    "FlyBase:FBgn0020304",
    "UniProtKB:O96639",  # a drongo TrEMBL accession
    "UniProtKB:O95081",  # AGFG2
]


def probe(gid: str) -> tuple[int, object]:
    q = urllib.parse.urlencode({"geneProductId": gid, "limit": 1})
    url = f"https://www.ebi.ac.uk/QuickGO/services/annotation/search?{q}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req) as fh:
            return fh.status, json.load(fh)["numberOfHits"]
    except urllib.error.HTTPError as exc:
        return exc.code, json.loads(exc.read()).get("messages")


def main() -> None:
    results = {}
    for gid in CANDIDATES:
        status, payload = probe(gid)
        results[gid] = (status, payload)
        print(f"{gid:28s} HTTP {status}  {payload}")
    ctrl = results["UniProtKB:P52594"]
    assert ctrl[0] == 200 and isinstance(ctrl[1], int) and ctrl[1] > 0, (
        f"positive control failed: {ctrl} - a zero elsewhere would be uninterpretable"
    )
    print("\npositive control OK: the endpoint and call pattern work")


if __name__ == "__main__":
    main()
