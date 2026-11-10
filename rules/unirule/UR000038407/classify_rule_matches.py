#!/usr/bin/env python3
"""Classify the UniProtKB entries matched by HAMAP MF_01501 (UniRule UR000038407).

Fetches every UniProtKB entry with a HAMAP MF_01501 cross-reference and reports,
from the live records only:

- reviewed / unreviewed counts,
- how many carry the MtrH-specific InterPro family IPR028342 versus only the
  broader MtrH/MtxH family IPR023467 (an MtxH-type paralog would show the latter
  without the former),
- how many have any predicted transmembrane segment,
- how many carry EC 7.2.1.4 in the protein name and the RHEA:53492 activity,
- the taxonomic classes represented.

Writes rule_matches.tsv beside this script and prints a summary.

Usage:
    python classify_rule_matches.py
"""

from __future__ import annotations

import csv
import io
import re
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

REST = "https://rest.uniprot.org/uniprotkb/search"
FIELDS = ",".join([
    "accession", "reviewed", "gene_names", "protein_name", "organism_name",
    "lineage", "xref_interpro", "ft_transmem", "cc_subcellular_location",
    "ec", "rhea",
])
OUT = Path(__file__).with_name("rule_matches.tsv")


def fetch(query: str) -> list[dict[str, str]]:
    url = REST + "?" + urllib.parse.urlencode(
        {"query": query, "fields": FIELDS, "format": "tsv", "size": 500})
    rows: list[dict[str, str]] = []
    header = None
    while url:
        with urllib.request.urlopen(url, timeout=60) as resp:
            text = resp.read().decode()
            link = resp.headers.get("Link", "")
        lines = text.splitlines()
        if header is None:
            header = lines[0]
        body = lines[1:] if lines and lines[0] == header else lines
        rows.extend(csv.DictReader(io.StringIO("\n".join([header] + body)),
                                   delimiter="\t"))
        m = re.search(r'<([^>]+)>; rel="next"', link)
        url = m.group(1) if m else None
    return rows


def lineage_class(lineage: str) -> str:
    for part in (p.strip() for p in lineage.split(",")):
        if "(class)" in part:
            return part.replace(" (class)", "")
    return "unclassified"


def main() -> None:
    rows = fetch("xref:hamap-MF_01501")
    with OUT.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    n = len(rows)
    reviewed = sum(r["Reviewed"] == "reviewed" for r in rows)
    mtrh_fam = sum("IPR028342" in r["InterPro"] for r in rows)
    mtx_only = [r["Entry"] for r in rows
                if "IPR023467" in r["InterPro"] and "IPR028342" not in r["InterPro"]]
    tm = [r["Entry"] for r in rows if r["Transmembrane"].strip()]
    loc = [r["Entry"] for r in rows if r["Subcellular location [CC]"].strip()]
    ec = sum("7.2.1.4" in r["EC number"] for r in rows)
    rhea = sum("53492" in r["Rhea ID"] for r in rows)
    print(f"entries with HAMAP MF_01501 xref: {n} ({reviewed} reviewed, {n - reviewed} unreviewed)")
    print(f"with MtrH family IPR028342: {mtrh_fam}")
    print(f"with IPR023467 (MtrH/MtxH) but not IPR028342: {len(mtx_only)} {mtx_only}")
    print(f"with any predicted/annotated transmembrane segment: {len(tm)} {tm}")
    print(f"with a CC SUBCELLULAR LOCATION statement: {len(loc)} {loc}")
    print(f"with EC 7.2.1.4: {ec}; with RHEA:53492: {rhea}")
    print("classes:", dict(Counter(lineage_class(r["Taxonomic lineage"]) for r in rows)))
    print("reviewed:", sorted(r["Entry"] for r in rows if r["Reviewed"] == "reviewed"))


if __name__ == "__main__":
    main()
