#!/usr/bin/env python3
"""Download the FUNG-GROWTH carbon-source growth matrix.

FUNG-GROWTH (https://www.fung-growth.org/, de Vries et al. 2025, Microbiol
Resour Announc 14:9) is a BioloMICS website backed by the Westerdijk/Bio-Aware
web service. The public site is an Angular app; this script calls the same
JSON endpoints the app's search grid uses, so no login is needed.

Outputs (in ./data):
  fung_growth_fields.tsv        field key -> carbon source / attribute
  fung_growth_strains.tsv       one row per strain (genome + CAZy links etc.)
  fung_growth_ratings.tsv       long format: strain, carbon source, rating, sporulation
  fung_growth_matrix.tsv        wide format: strain x carbon source growth rating

Usage:  python projects/FUNG_GROWTH/fetch_fung_growth.py
"""

from __future__ import annotations

import csv
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

BASE = "https://webservices.bio-aware.com/cbsdatabase"
WEBSITE_ID = "87"  # from https://www.fung-growth.org/config.json
TABLE_KEY = "14682616000000025"  # "Fungal growth" table behind the "Query FG" page
OUT = Path(__file__).parent / "data"

# Attribute suffixes used in the field titles, e.g. "D-xylose growth rating".
SUFFIXES = ["growth rating", "sporulation", "picture", "growth"]
META_FIELDS = {
    "Genomes": "genome_url",
    "Link to CAZY": "cazy_url",
    "Publication": "publication",
    "Temparture": "temperature",  # sic, as named in the source database
}


def call(method: str, path: str, payload: dict | None = None, retries: int = 4):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(
        f"{BASE}{path}",
        data=data,
        method=method,
        headers={"WebsiteId": WEBSITE_ID, "Content-Type": "application/json"},
    )
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                return json.loads(resp.read())
        except Exception as exc:  # network flakiness through proxies
            if attempt == retries - 1:
                raise
            wait = 2 ** (attempt + 1)
            print(f"retry {path} in {wait}s ({exc})", file=sys.stderr)
            time.sleep(wait)


def split_title(title: str) -> tuple[str, str] | None:
    for suffix in SUFFIXES:
        if title.endswith(" " + suffix):
            return title[: -len(suffix) - 1].strip(), suffix
    return None


def cell_text(cell: dict | None) -> str:
    if not cell or cell.get("IsEmpty"):
        return ""
    value = cell.get("Value")
    if isinstance(value, list) and value and "X" in value[0]:
        # growth curve: (day, colony measurement) pairs
        return " ".join(f"d{v['X']:g}:{v['Y']:g}" for v in value)
    if isinstance(value, list):
        return "; ".join(str(v.get("Value") or v.get("Name") or "") for v in value)
    return str(cell.get("DataToView") if value is None else value).strip()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    fields = call("POST", "/api/Table/GeFieldListByTableKey", {"TableKey": TABLE_KEY, "FieldFilter": None})["Data"]

    carbon: dict[str, dict[str, str]] = {}  # carbon source -> attribute -> field key
    meta: dict[str, str] = {}  # column name -> field key
    with open(OUT / "fung_growth_fields.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["field_key", "field_type", "title", "carbon_source", "attribute"])
        for f in fields:
            title = f.get("title") or f["FieldName"]
            parsed = split_title(title)
            if parsed:
                carbon.setdefault(parsed[0], {})[parsed[1]] = f["FieldKey"]
            elif title in META_FIELDS:
                meta[META_FIELDS[title]] = f["FieldKey"]
            w.writerow([f["FieldKey"], f["FieldType"], title, *(parsed or ("", ""))])

    wanted = ["-100", *meta.values()]
    for attrs in carbon.values():
        wanted += [attrs[a] for a in ("growth rating", "sporulation", "growth") if a in attrs]

    rows, start, page = [], 0, 200
    while True:
        res = call(
            "POST",
            "/api/Search/GetData",
            {
                "TableKey": TABLE_KEY,
                "iDisplayLength": page,
                "iDisplayStart": start,
                "ListOfConditionEntity": [],
                "ComplexQuery": None,
                "SearchKey": "",
                "SortColumn": None,
                "SortDirection": None,
                "FieldKeys": wanted,
                "SummarizedData": True,
            },
        )
        batch = res["Data"]["RowData"]
        rows += batch
        if len(batch) < page:
            break
        start += page

    sources = sorted(carbon, key=str.lower)
    with open(OUT / "fung_growth_strains.tsv", "w", newline="") as sfh, open(
        OUT / "fung_growth_ratings.tsv", "w", newline=""
    ) as rfh, open(OUT / "fung_growth_matrix.tsv", "w", newline="") as mfh:
        sw, rw, mw = (csv.writer(x, delimiter="\t") for x in (sfh, rfh, mfh))
        sw.writerow(["record_id", "strain", "species", *META_FIELDS.values()])
        rw.writerow(["record_id", "strain", "carbon_source", "growth_rating", "sporulation", "growth_curve"])
        mw.writerow(["strain", *sources])
        for row in rows:
            rid = cell_text(row.get("-101"))
            strain = cell_text(row.get("-100"))
            species = " ".join(re.sub(r"[^\w\s.-]", "", strain).split()[:2])
            sw.writerow([rid, strain, species, *(cell_text(row.get(meta.get(k, ""))) for k in META_FIELDS.values())])
            matrix = []
            for src in sources:
                a = carbon[src]
                rating = cell_text(row.get(a.get("growth rating", "")))
                spor = cell_text(row.get(a.get("sporulation", "")))
                note = cell_text(row.get(a.get("growth", "")))
                if rating in ("?",):
                    rating = ""
                if rating or spor or note:
                    rw.writerow([rid, strain, src, rating, spor, note])
                matrix.append(rating)
            mw.writerow([strain, *matrix])

    print(f"{len(rows)} strains x {len(sources)} carbon sources -> {OUT}")


if __name__ == "__main__":
    main()
