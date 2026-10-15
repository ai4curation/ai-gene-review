"""Download every NOT-qualified GO annotation from QuickGO.

QuickGO's downloadSearch endpoint is filtered one qualifier at a time (all
``NOT|<relation>`` values), and the rows are concatenated into
``not_annotations.tsv``. QuickGO leaves the GO NAME column empty in TSV
downloads, so labels are filled from the local GO SQLite database
(``sqlite:obo:go``, as used by runoak elsewhere in the repo).

Usage:
    uv run python projects/NOT_ANNOTATION_USAGE/fetch_not_annotations.py
"""

from __future__ import annotations

import csv
import io
import sys
import time
from pathlib import Path

import requests
from oaklib import get_adapter

HERE = Path(__file__).parent
OUT = HERE / "not_annotations.tsv"
URL = "https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch"
RELATIONS = [
    "enables",
    "contributes_to",
    "involved_in",
    "acts_upstream_of",
    "acts_upstream_of_or_within",
    "acts_upstream_of_positive_effect",
    "acts_upstream_of_negative_effect",
    "acts_upstream_of_or_within_positive_effect",
    "acts_upstream_of_or_within_negative_effect",
    "located_in",
    "part_of",
    "is_active_in",
    "colocalizes_with",
]
FIELDS = (
    "geneProductId,symbol,qualifier,goId,goName,goAspect,evidenceCode,goEvidence,"
    "reference,withFrom,taxonId,taxonName,assignedBy,date"
)


def fetch(qualifier: str) -> list[dict[str, str]]:
    for attempt in range(5):
        r = requests.get(
            URL,
            params={"qualifier": qualifier, "downloadLimit": 2000000, "selectedFields": FIELDS},
            headers={"Accept": "text/tsv"},
            timeout=600,
        )
        if r.status_code == 200:
            return list(csv.DictReader(io.StringIO(r.text), delimiter="\t"))
        time.sleep(10 * (attempt + 1))
    r.raise_for_status()
    return []


def main() -> int:
    go = get_adapter("sqlite:obo:go")
    rows: list[dict[str, str]] = []
    for rel in RELATIONS:
        got = fetch(f"NOT|{rel}")
        print(f"NOT|{rel}: {len(got)}", file=sys.stderr)
        rows.extend(got)
    labels: dict[str, str] = {}
    for row in rows:
        go_id = row["GO TERM"]
        if go_id not in labels:
            labels[go_id] = go.label(go_id) or ""
        row["GO NAME"] = labels[go_id]
    if not rows:
        print("no rows downloaded", file=sys.stderr)
        return 1
    with OUT.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} rows to {OUT}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
