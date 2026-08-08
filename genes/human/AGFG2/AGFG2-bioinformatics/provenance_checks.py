#!/usr/bin/env python3
"""Provenance checks on AGFG2's non-IBA rows.

Three independent questions:

1. **Reference-projection test.** For each supporting reference, how many distinct
   gene products does it annotate, and does any *functional* term spread across the
   set or stay on one entity?  A reference that annotates N entities with one
   identical term is an import, not N findings.  Entity counts are derived as a
   distinct set of gene-product ids — an annotation count is not an entity count —
   and the query is fully paginated with a truncation assertion.

2. **Which InterPro signature actually supplies `GO:0005096`.**  AGFG2 matches four
   InterPro entries; enumerating each one's interpro2go mapping separately shows
   which entry carries the activity claim and which behave with restraint.  The
   entries that map to nothing are the control.

3. **Family census.** Do the other reviewed members of PANTHER PTHR46134 carry
   `GO:0005096`, and by what evidence?  Reported explicitly as the Swiss-Prot
   subset, never as "the family".
"""

from __future__ import annotations

import csv
import json
import pathlib
import sys
import urllib.parse
from collections import defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import EXPERIMENTAL_CODES, get_json, quickgo_annotations  # noqa: E402

HERE = pathlib.Path(__file__).parent
GOA = HERE.parent / "AGFG2-goa.tsv"
PANTHER_CSV = (HERE.parents[3] / "interpro" / "panther" / "PTHR46134"
               / "PTHR46134-entries.csv")
PANTHER_META = (HERE.parents[3] / "interpro" / "panther" / "PTHR46134"
                / "PTHR46134-metadata.yaml")

SIGNATURES = ["IPR052248", "IPR037278", "IPR001164", "IPR038508"]


def projection_test(reference: str) -> dict:
    rows = quickgo_annotations(reference=reference, limit=100)
    entities = sorted({r["geneProductId"] for r in rows})
    per_term: dict[str, set] = defaultdict(set)
    for r in rows:
        per_term[r["goId"]].add(r["geneProductId"])
    return {
        "reference": reference,
        "n_annotations": len(rows),
        "n_entities": len(entities),
        "entities": entities if len(entities) <= 60 else entities[:60] + ["..."],
        "terms": {t: {"n_entities": len(v),
                      "aspect_hint": t,
                      "entities": sorted(v) if len(v) <= 20 else sorted(v)[:20] + ["..."]}
                  for t, v in sorted(per_term.items())},
        "evidence_codes": sorted({r["goEvidence"] for r in rows}),
        "assigned_by": sorted({r["assignedBy"] for r in rows}),
    }


def interpro2go(entry: str) -> dict:
    d = get_json(f"https://www.ebi.ac.uk/interpro/api/entry/interpro/{entry}/")
    md = d["metadata"]
    terms = md.get("go_terms") or []
    return {
        "accession": entry,
        "name": (md.get("name") or {}).get("name"),
        "type": md.get("type"),
        "n_proteins": (md.get("counters") or {}).get("matches"),
        "go_terms": [
            {"id": t.get("identifier"), "name": (t.get("name")),
             "category": (t.get("category") or {}).get("code")}
            for t in terms
        ],
    }


def family_census() -> dict:
    with PANTHER_CSV.open() as fh:
        members = list(csv.DictReader(fh))
    total_proteins = None
    for line in PANTHER_META.read_text().splitlines():
        s = line.strip()
        if s.startswith("proteins:"):
            total_proteins = int(s.split(":")[1])
    out = {
        "reviewed_members_in_cached_csv": len(members),
        "family_total_proteins": total_proteins,
        "reviewed_fraction_pct": (
            round(100.0 * len(members) / total_proteins, 2) if total_proteins else None
        ),
        "caveat": (
            "the cached PTHR46134-entries.csv is built from InterPro's REVIEWED-only "
            "protein endpoint, so this is the Swiss-Prot subset, not the family"
        ),
        "members": {},
    }
    for m in members:
        rows = quickgo_annotations(
            geneProductId=f"UniProtKB:{m['id']}",
            goId="GO:0005096",
            goUsage="descendants",
            goUsageRelationships="is_a,part_of",
        )
        out["members"][m["id"]] = {
            "gene": m["gene"],
            "organism": m["source_tax_name"],
            "subfamily": m["subfamily"],
            "length": int(m["length"]),
            "GO_0005096_rows": [
                {"goId": r["goId"], "evidence": r["goEvidence"],
                 "reference": r["reference"], "withFrom": [
                     f"{c['db']}:{c['id']}"
                     for w in (r.get("withFrom") or [])
                     for c in (w.get("connectedXrefs") or [])
                 ]}
                for r in rows
            ],
            "n_experimental": sum(1 for r in rows if r["goEvidence"] in EXPERIMENTAL_CODES),
        }
    return out


def main() -> None:
    with GOA.open() as fh:
        goa = list(csv.DictReader(fh, delimiter="\t"))
    refs = sorted({r["REFERENCE"] for r in goa if r["REFERENCE"].startswith("PMID:")})

    out: dict = {"projection": {}, "interpro2go": {}, "family_census": {}}

    # Positive control for the projection endpoint: a reference known to annotate
    # many entities, so a small count cannot be a broken query.
    ctrl = quickgo_annotations(reference="GO_REF:0000033", limit=100, taxonId="9606",
                               goId="GO:0005096", goUsage="descendants",
                               goUsageRelationships="is_a,part_of")
    if not ctrl:
        raise AssertionError("projection positive control returned zero")
    out["projection_positive_control"] = {
        "reference": "GO_REF:0000033 (human, GO:0005096 descendants)",
        "n_annotations": len(ctrl),
        "n_entities": len({r["geneProductId"] for r in ctrl}),
    }

    for ref in refs:
        out["projection"][ref] = projection_test(ref)

    for sig in SIGNATURES:
        out["interpro2go"][sig] = interpro2go(sig)

    out["family_census"] = family_census()

    (HERE / "provenance.json").write_text(json.dumps(out, indent=2, sort_keys=True))

    print("=== projection positive control ===")
    print(f"  {out['projection_positive_control']}")
    print("\n=== reference-projection test ===")
    for ref, d in out["projection"].items():
        print(f"  {ref}: {d['n_annotations']} annotations over {d['n_entities']} "
              f"entities; codes={d['evidence_codes']}; assignedBy={d['assigned_by']}")
        for t, v in d["terms"].items():
            print(f"      {t}: {v['n_entities']} entities")

    print("\n=== which InterPro signature supplies GO:0005096 ===")
    for sig, d in out["interpro2go"].items():
        gts = ", ".join(f"{t['id']} ({t['category']})" for t in d["go_terms"]) or "NONE"
        print(f"  {sig} [{d['type']}, {d['n_proteins']} proteins] {d['name']}\n"
              f"      -> {gts}")

    fc = out["family_census"]
    print(f"\n=== PTHR46134 census: {fc['reviewed_members_in_cached_csv']} reviewed "
          f"(Swiss-Prot) members of {fc['family_total_proteins']} proteins "
          f"({fc['reviewed_fraction_pct']}%) ===")
    for acc, m in fc["members"].items():
        rows = m["GO_0005096_rows"]
        desc = "; ".join(f"{r['goId']} {r['evidence']} {r['reference']}" for r in rows) or "none"
        print(f"  {acc} {m['organism']:24s} {m['gene']:7s} {m['subfamily']:16s} "
              f"exp={m['n_experimental']}  {desc}")


if __name__ == "__main__":
    main()
