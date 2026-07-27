#!/usr/bin/env python3
"""GO-annotation census of the five human UbiB / aarF-domain kinase genes, plus the
PAINT node-level term assignments for the two PANTHER families that contain them.

Purpose: ADCK5's review turns on two comparative claims that must be measured, not
assumed:

  1. ADCK5 carries NO IBA annotation, while every other human UbiB-family gene does.
  2. UniProt still assigns ADCK5 (and ADCK2) the protein-serine/threonine-kinase
     keyword and EC 2.7.11.-, while the two members whose activity was actually
     tested (COQ8A, COQ8B) have been downgraded to EC 2.7.-.- and carry explicit
     NOT|enables GO:0004672 annotations.

Both are checked here against complete (non-truncated) API responses.

Anti-truncation discipline: every QuickGO call compares `numberOfHits` against
`len(results)` — never against the page-size constant we chose — because the service
clamps rather than errors, so a page-size comparison would sail past a silent truncation.
"""

from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "family_census.json"

# The five human UbiB (aarF-domain) genes.
GENES = {
    "ADCK5": "Q3MIX3",
    "ADCK1": "Q86TW2",
    "ADCK2": "Q7Z695",
    "COQ8A": "Q8NI60",
    "COQ8B": "Q96D53",
}

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}


def get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    return json.load(urllib.request.urlopen(req))


def quickgo_all(acc: str) -> list[dict]:
    """All GO annotations for one accession, with a truncation guard."""
    rows: list[dict] = []
    page = 1
    while True:
        d = get(
            "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
            f"?geneProductId=UniProtKB:{acc}&limit=100&page={page}"
        )
        total = d["numberOfHits"]
        rows += d["results"]
        # Compare against len(rows), not against our chosen limit: if the service clamps
        # results-per-page instead of erroring, a limit-based check cannot see it.
        if not d["results"] or len(rows) >= total:
            break
        page += 1
    if len(rows) != total:
        raise SystemExit(
            f"FATAL: truncated QuickGO response for {acc}: got {len(rows)} of {total}"
        )
    return rows


def uniprot_entry(acc: str) -> dict:
    return get(
        f"https://rest.uniprot.org/uniprotkb/{acc}.json"
        "?fields=accession,id,protein_name,keyword,cc_function,ec"
    )


def main() -> int:
    census: dict[str, dict] = {}

    for sym, acc in GENES.items():
        rows = quickgo_all(acc)
        ent = uniprot_entry(acc)
        entry_name = ent.get("uniProtkbId")
        if not entry_name:
            raise SystemExit(f"FATAL: {acc} returned no entry name (dead accession?)")

        ecs = [
            e["value"]
            for e in ent["proteinDescription"]
            .get("recommendedName", {})
            .get("ecNumbers", [])
        ]
        kws = [k["name"] for k in ent.get("keywords", [])]

        iba = [r for r in rows if r["goEvidence"] == "IBA"]
        iba_nodes = sorted(
            {
                c["id"]
                for r in iba
                for e in (r.get("withFrom") or [])
                for c in e["connectedXrefs"]
                if c["id"].startswith("PTN")
            }
        )
        negated = [
            f"NOT|{r['goId']} ({r['goEvidence']}, {r['reference']})"
            for r in rows
            if str(r.get("qualifier", "")).startswith("NOT")
        ]
        kinase_terms = sorted(
            {
                f"{r['goId']} {r['goEvidence']} {r['qualifier']}"
                for r in rows
                # GO:0004672 protein kinase / GO:0004674 protein Ser-Thr kinase /
                # GO:0016301 kinase activity / GO:0006468 protein phosphorylation
                if r["goId"] in {"GO:0004672", "GO:0004674", "GO:0016301", "GO:0006468"}
            }
        )

        census[sym] = {
            "accession": acc,
            "entry_name": entry_name,
            "reviewed": ent["entryType"].startswith("UniProtKB reviewed"),
            "ec_numbers": ecs,
            "has_ser_thr_kinase_keyword": "Serine/threonine-protein kinase" in kws,
            "n_annotations": len(rows),
            "n_iba": len(iba),
            "iba_nodes": iba_nodes,
            "negated_annotations": negated,
            "kinase_related_terms": kinase_terms,
            "n_experimental": sum(1 for r in rows if r["goEvidence"] in EXPERIMENTAL),
        }

    # ---- the two load-bearing comparative claims, asserted ----
    problems: list[str] = []

    if census["ADCK5"]["n_iba"] != 0:
        problems.append(
            f"claim 1 broken: ADCK5 now has {census['ADCK5']['n_iba']} IBA annotations"
        )
    others_without_iba = [s for s in GENES if s != "ADCK5" and census[s]["n_iba"] == 0]
    if others_without_iba:
        problems.append(
            "claim 1 weakened: ADCK5 is not the only UbiB gene lacking IBA; "
            f"also {others_without_iba}"
        )

    tested = ["COQ8A", "COQ8B"]
    untested = ["ADCK5", "ADCK2"]
    for s in tested:
        if census[s]["ec_numbers"] != ["2.7.-.-"]:
            problems.append(f"claim 2: {s} EC is {census[s]['ec_numbers']}, expected ['2.7.-.-']")
        if not census[s]["negated_annotations"]:
            problems.append(f"claim 2: {s} carries no NOT| annotation any more")
    for s in untested:
        if census[s]["ec_numbers"] != ["2.7.11.-"]:
            problems.append(
                f"claim 2: {s} EC is {census[s]['ec_numbers']}, expected ['2.7.11.-']"
            )
        if not census[s]["has_ser_thr_kinase_keyword"]:
            problems.append(f"claim 2: {s} no longer has the Ser/Thr-kinase keyword")

    OUT.write_text(json.dumps({"census": census, "problems": problems}, indent=2) + "\n")

    hdr = f"{'gene':<8}{'EC':<12}{'S/T kw':<8}{'ann':<5}{'IBA':<5}{'exp':<5}{'IBA node(s)':<18}{'NOT|'}"
    print(hdr)
    print("-" * (len(hdr) + 24))
    for sym in GENES:
        c = census[sym]
        print(
            f"{sym:<8}{','.join(c['ec_numbers']):<12}"
            f"{('yes' if c['has_ser_thr_kinase_keyword'] else 'no'):<8}"
            f"{c['n_annotations']:<5}{c['n_iba']:<5}{c['n_experimental']:<5}"
            f"{(','.join(c['iba_nodes']) or '-'):<18}"
            f"{len(c['negated_annotations'])}"
        )
    print()
    for sym in GENES:
        c = census[sym]
        if c["kinase_related_terms"] or c["negated_annotations"]:
            print(f"{sym}: kinase-related GO = {c['kinase_related_terms'] or 'none'}")
            for n in c["negated_annotations"]:
                print(f"    {n}")
    print()
    if problems:
        print("CLAIM CHECKS FAILED:")
        for p in problems:
            print("  -", p)
        return 1
    print("Both comparative claims hold against current UniProt + QuickGO.")
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
