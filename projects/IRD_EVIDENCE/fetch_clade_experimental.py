"""Download experimental GO annotations for every protein under an IRD node.

If PAINT says a function was lost (diverged) at node X, a positive experimental
annotation for that function on a protein below X is a direct test of the call.
This script downloads, from QuickGO, every annotation with experimental evidence
(ECO:0000269 and descendants, which includes the high-throughput codes) for the
UniProt accessions in ``ird_clade_members.tsv.gz``. Matching to the blocked term
(including GO descendants) is done in ``analyze_ird.py``.

Input:   ird_clade_members.tsv.gz
Output:  clade_experimental_annotations.tsv.gz

Usage:
    uv run python projects/IRD_EVIDENCE/fetch_clade_experimental.py
"""

from __future__ import annotations

import csv
import gzip
import io
import sys
import time
from pathlib import Path

import requests

HERE = Path(__file__).parent
MEMBERS = HERE / "ird_clade_members.tsv.gz"
OUT = HERE / "clade_experimental_annotations.tsv.gz"
URL = "https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch"
FIELDS = "geneProductId,symbol,qualifier,goId,goAspect,evidenceCode,goEvidence,reference,withFrom,taxonId,assignedBy,date"
BATCH = 150


def fetch(accs: list[str]) -> list[dict[str, str]]:
    params = {
        "geneProductId": ",".join(accs),
        "evidenceCode": "ECO:0000269",
        "evidenceCodeUsage": "descendants",
        "downloadLimit": 2000000,
        "selectedFields": FIELDS,
    }
    for attempt in range(5):
        try:
            r = requests.get(URL, params=params, headers={"Accept": "text/tsv"}, timeout=600)
            if r.status_code == 200:
                return list(csv.DictReader(io.StringIO(r.text), delimiter="\t"))
            print(f"HTTP {r.status_code}", file=sys.stderr)
        except requests.RequestException as e:
            print(e, file=sys.stderr)
        time.sleep(10 * (attempt + 1))
    raise RuntimeError(f"QuickGO failed for batch starting {accs[0]}")


def main() -> int:
    with gzip.open(MEMBERS, "rt") as fh:
        accs = sorted({r["uniprot"] for r in csv.DictReader(fh, delimiter="\t") if r["uniprot"]})
    print(f"{len(accs)} distinct clade accessions", file=sys.stderr)
    rows: list[dict[str, str]] = []
    for i in range(0, len(accs), BATCH):
        got = fetch(accs[i : i + BATCH])
        rows.extend(got)
        if (i // BATCH) % 20 == 0:
            print(f"{i + BATCH}/{len(accs)}: {len(rows)} rows", file=sys.stderr)
    if not rows:
        print("no rows downloaded", file=sys.stderr)
        return 1
    with gzip.open(OUT, "wt", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} rows to {OUT}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
