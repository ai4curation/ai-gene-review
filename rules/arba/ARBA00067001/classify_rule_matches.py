"""Classify the proteins annotated by ARBA00067001 / ARBA00052213 as MCR-type or ASD-type.

Both rules have the same single condition set (CATH FunFam 3.40.50.720:FF:000411
AND taxon Archaea). ARBA00067001 assigns EC 1.2.1.75 in the recommended name;
ARBA00052213 assigns the malonyl-CoA reductase catalytic activity (RHEA:26446).

For every archaeal UniProt entry matching that FunFam, this script records:

- whether the entry's EC 1.2.1.75 name and catalytic activity carry ARBA
  evidence from each rule (read from the entry's evidence tags);
- which conserved-domain (CDD) subfamily models it matches: MCR-type
  (cd23940, cd24150) or archaeal/fungal ASD-type (cd18130, cd02315);
- whether it carries NCBIfam TIGR00978 (asd_EA).

Data are fetched live from UniProt REST, so counts can change between releases.
Run: ``uv run python rules/arba/ARBA00067001/classify_rule_matches.py``
Output (TSV on stdout, summary on stderr) is saved next to this script.
"""

from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request

REST = "https://rest.uniprot.org/uniprotkb/search"
FUNFAM = "3.40.50.720:FF:000411"
NAME_RULE = "ARBA00067001"
ACTIVITY_RULE = "ARBA00052213"
MCR_CDD = {"cd23940", "cd24150"}
ASD_CDD = {"cd18130", "cd02315"}


def search(query: str) -> list[dict]:
    """Return all UniProt entries (JSON) matching a query, following pagination."""
    params = urllib.parse.urlencode({"query": query, "format": "json", "size": 500})
    url: str | None = f"{REST}?{params}"
    results: list[dict] = []
    while url:
        with urllib.request.urlopen(url, timeout=60) as resp:
            results.extend(json.load(resp)["results"])
            link = resp.headers.get("Link", "")
        url = link.split(";")[0].strip("<>") if 'rel="next"' in link else None
    return results


def evidence_sources(obj: object) -> set[str]:
    """Collect ``source:id`` strings of every evidence tag under a JSON object."""
    found: set[str] = set()
    if isinstance(obj, dict):
        for ev in obj.get("evidences", []):
            found.add(f"{ev.get('source')}:{ev.get('id')}")
        for value in obj.values():
            found |= evidence_sources(value)
    elif isinstance(obj, list):
        for item in obj:
            found |= evidence_sources(item)
    return found


def classify(entry: dict) -> dict:
    """Summarise one entry: rule evidence, CDD class, TIGR00978, name."""
    xrefs = entry.get("uniProtKBCrossReferences", [])
    cdd = {x["id"] for x in xrefs if x.get("database") == "CDD"}
    ncbifam = {x["id"] for x in xrefs if x.get("database") == "NCBIfam"}
    name_ev = evidence_sources(entry.get("proteinDescription", {}))
    activity_ev = evidence_sources(
        [c for c in entry.get("comments", []) if c.get("commentType") == "CATALYTIC ACTIVITY"]
    )
    if cdd & MCR_CDD and not cdd & ASD_CDD:
        cdd_class = "MCR"
    elif cdd & ASD_CDD and not cdd & MCR_CDD:
        cdd_class = "ASD"
    elif cdd & MCR_CDD and cdd & ASD_CDD:
        cdd_class = "BOTH"
    else:
        cdd_class = "NONE"
    rec = entry.get("proteinDescription", {}).get("recommendedName", {})
    genes = entry.get("genes", [{}])
    locus = ",".join(
        o["value"] for g in genes for o in g.get("orderedLocusNames", [])
    )
    return {
        "accession": entry["primaryAccession"],
        "organism": entry.get("organism", {}).get("scientificName", ""),
        "locus": locus,
        "name": rec.get("fullName", {}).get("value", ""),
        "name_ecs": ",".join(e["value"] for e in rec.get("ecNumbers", [])),
        "name_rule": f"ARBA:{NAME_RULE}" in name_ev,
        "activity_rule": f"ARBA:{ACTIVITY_RULE}" in activity_ev,
        "cdd_class": cdd_class,
        "cdd": ",".join(sorted(cdd)),
        "tigr00978": "TIGR00978" in ncbifam,
    }


def main() -> None:
    """Fetch FunFam-matching archaeal entries and print a classification table."""
    entries = search(f'"{FUNFAM}" AND taxonomy_id:2157')
    rows = sorted((classify(e) for e in entries), key=lambda r: (r["cdd_class"], r["accession"]))
    cols = list(rows[0].keys()) if rows else []
    print("\t".join(cols))
    for row in rows:
        print("\t".join(str(row[c]) for c in cols))

    def count(pred) -> int:  # type: ignore[no-untyped-def]
        return sum(1 for r in rows if pred(r))

    print(f"entries matching FunFam {FUNFAM} in Archaea: {len(rows)}", file=sys.stderr)
    for rule_key, label in (("name_rule", NAME_RULE), ("activity_rule", ACTIVITY_RULE)):
        hit = [r for r in rows if r[rule_key]]
        by_class = {c: sum(1 for r in hit if r["cdd_class"] == c) for c in ("MCR", "ASD", "BOTH", "NONE")}
        print(f"{label}: {len(hit)} entries with rule evidence; by CDD class {by_class}", file=sys.stderr)
    print(
        f"TIGR00978 present: MCR-type {count(lambda r: r['cdd_class'] == 'MCR' and r['tigr00978'])}"
        f"/{count(lambda r: r['cdd_class'] == 'MCR')}, "
        f"ASD-type {count(lambda r: r['cdd_class'] == 'ASD' and r['tigr00978'])}"
        f"/{count(lambda r: r['cdd_class'] == 'ASD')}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
