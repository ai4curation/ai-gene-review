#!/usr/bin/env python3
"""Census of the proteins that ARBA00028655 actually annotates.

ARBA00028655 asserts GO:0006661 "phosphatidylinositol biosynthetic process".
This script asks QuickGO for every GO:0006661 / ECO:0000256 / GO_REF:0000117
annotation whose ``withFrom`` names ARBA00028655, then resolves the accessions to
UniProt protein names so the functional composition of the hit set can be counted.

Run:
    uv run python rules/arba/ARBA00028655/scripts/census_arba00028655.py

    # whole-set census, sampled across pages (the hit set is far too large to enumerate)
    uv run python rules/arba/ARBA00028655/scripts/census_arba00028655.py --taxon 9606

    # single-taxon census: small enough to enumerate exhaustively, reported per gene

Nothing here is hardcoded: if the rule changes upstream, the numbers change.
Output is written to stdout; RESULTS in ARBA00028655-analysis.md records the runs
made on 2026-08-15.
"""

from __future__ import annotations

import argparse
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


def fetch_page(page: int, limit: int = 100, taxon: str | None = None) -> dict:
    url = QUICKGO.format(limit=limit, page=page)
    if taxon:
        url += f"&taxonId={taxon}&taxonUsage=exact"
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


def uniprot_fields(accessions: list[str], fields: list[str]) -> collections.Counter:
    """Count accessions by UniProt fields, falling back through ``fields`` in order.

    Many TrEMBL entries (cDNA clones) carry no primary gene name, so a gene-level
    census must fall back to the protein name or it silently drops those accessions.
    """
    names: collections.Counter = collections.Counter()
    for i in range(0, len(accessions), 100):
        batch = accessions[i : i + 100]
        query = " OR ".join(f"accession:{a}" for a in batch)
        url = (
            f"{UNIPROT}?query={urllib.parse.quote(query)}"
            f"&fields=accession,{','.join(fields)}&format=tsv&size=500"
        )
        with urllib.request.urlopen(url) as fh:
            text = fh.read().decode()
        rows = {}
        for line in text.splitlines()[1:]:
            parts = line.split("\t")
            if len(parts) > len(fields):
                rows[parts[0]] = parts[1:]
        for acc in batch:
            values = [v for v in rows.get(acc, []) if v]
            if values:
                names[values[0].split(" (")[0]] += 1
            else:
                names[f"(unresolved: {acc})"] += 1
    return names


def collect_taxon(rule_id: str, taxon: str) -> list[str]:
    """Enumerate every accession in a single taxon (small enough to page through)."""
    accessions: list[str] = []
    page = 1
    while True:
        payload = fetch_page(page, taxon=taxon)
        accessions += accessions_from(payload, rule_id)
        pages = payload.get("pageInfo", {}).get("total", 1)
        if page >= pages:
            break
        page += 1
    return accessions


def main(rule_id: str = "ARBA00028655", taxon: str | None = None) -> None:
    first = fetch_page(SAMPLE_PAGES[0], taxon=taxon)
    total = first["numberOfHits"]
    scope = f" in taxon {taxon}" if taxon else ""
    print(f"{rule_id}: {total} GO:0006661 IEA annotations under GO_REF:0000117{scope}")

    if taxon:
        # A single-taxon hit set is small; enumerate it all and report per gene.
        accessions = collect_taxon(rule_id, taxon)
        print(f"enumerated {len(accessions)} accessions attributed to {rule_id}")
        fields = ["gene_primary", "protein_name"]
    else:
        accessions = accessions_from(first, rule_id)
        for page in SAMPLE_PAGES[1:]:
            try:
                accessions += accessions_from(fetch_page(page), rule_id)
            except Exception as exc:  # paging limits vary; report rather than fail
                print(f"  (page {page} unavailable: {exc})")
        print(f"sampled {len(accessions)} accessions across pages {SAMPLE_PAGES}")
        fields = ["protein_name"]

    names = uniprot_fields(accessions, fields)
    resolved = sum(names.values())
    print(f"counted {resolved} of {len(accessions)} accessions via UniProt")
    for name, count in names.most_common():
        print(f"{count:5d} ({100 * count / resolved:5.1f}%)  {name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rule", default="ARBA00028655", help="ARBA rule id")
    parser.add_argument(
        "--taxon",
        default=None,
        help="NCBI taxon id (e.g. 9606); enumerates that taxon exhaustively, by gene",
    )
    parsed = parser.parse_args()
    main(parsed.rule, parsed.taxon)
