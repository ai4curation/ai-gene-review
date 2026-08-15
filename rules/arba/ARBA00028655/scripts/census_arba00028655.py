#!/usr/bin/env python3
"""Census of the proteins that ARBA00028655 actually annotates.

ARBA00028655 asserts GO:0006661 "phosphatidylinositol biosynthetic process".
This script asks QuickGO for every GO:0006661 / ECO:0000256 / GO_REF:0000117
annotation whose ``withFrom`` names ARBA00028655, then resolves the accessions to
UniProt protein names so the functional composition of the hit set can be counted.

Run:
    uv run python rules/arba/ARBA00028655/scripts/census_arba00028655.py

Nothing here is hardcoded: if the rule changes upstream, the numbers change.
Output is written to stdout; RESULTS in ARBA00028655-analysis.md records the run
made on 2026-08-15.
"""

from __future__ import annotations

import collections
import json
import urllib.parse
import urllib.request

QUICKGO = (
    "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
    "?goId=GO:0006661&goUsage=exact&evidenceCode=ECO:0000256"
    "&reference=GO_REF:0000117&limit={limit}&page={page}"
)
UNIPROT = "https://rest.uniprot.org/uniprotkb/search"

# QuickGO caps paging at 100k results but returns 400 past ~page 5 for limit=200,
# so sample with limit=100 over pages spread across the result set.
SAMPLE_PAGES = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45]


def fetch_page(page: int, limit: int = 100) -> dict:
    url = QUICKGO.format(limit=limit, page=page)
    with urllib.request.urlopen(url) as fh:
        return json.load(fh)


def accessions_from(payload: dict, rule_id: str) -> list[str]:
    out = []
    for row in payload.get("results", []):
        xrefs = [
            x["id"]
            for group in (row.get("withFrom") or [])
            for x in group.get("connectedXrefs", [])
        ]
        if rule_id in xrefs:
            out.append(row["geneProductId"].split(":", 1)[1])
    return out


def protein_names(accessions: list[str]) -> collections.Counter:
    names: collections.Counter = collections.Counter()
    for i in range(0, len(accessions), 100):
        batch = accessions[i : i + 100]
        query = " OR ".join(f"accession:{a}" for a in batch)
        url = (
            f"{UNIPROT}?query={urllib.parse.quote(query)}"
            "&fields=accession,protein_name&format=tsv&size=500"
        )
        with urllib.request.urlopen(url) as fh:
            text = fh.read().decode()
        for line in text.splitlines()[1:]:
            parts = line.split("\t")
            if len(parts) > 1:
                names[parts[1].split(" (")[0]] += 1
    return names


def main(rule_id: str = "ARBA00028655") -> None:
    first = fetch_page(SAMPLE_PAGES[0])
    total = first["numberOfHits"]
    print(f"{rule_id}: {total} GO:0006661 IEA annotations under GO_REF:0000117")

    accessions = accessions_from(first, rule_id)
    for page in SAMPLE_PAGES[1:]:
        try:
            accessions += accessions_from(fetch_page(page), rule_id)
        except Exception as exc:  # paging limits vary; report rather than fail
            print(f"  (page {page} unavailable: {exc})")

    print(f"sampled {len(accessions)} accessions across pages {SAMPLE_PAGES}")
    names = protein_names(accessions)
    resolved = sum(names.values())
    for name, count in names.most_common():
        print(f"{count:5d} ({100 * count / resolved:5.1f}%)  {name}")


if __name__ == "__main__":
    main()
