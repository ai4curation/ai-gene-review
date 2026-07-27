#!/usr/bin/env python3
"""Where do ADCK5's interaction partners live, and how independent is each interaction?

Two numbers in `RESULTS.md` and the review used to be asserted from an ad-hoc query. This
script computes them, so `audit_adck5_claims.py` can hold the prose to them:

  1. **How many of the mitochondrial-interactome partners are themselves mitochondrial.**
     This is the compartment consideration that sits alongside the NOTCH2NLA two-hybrid
     hit; note it is a supporting argument only, since ADCK5's membrane sidedness has
     never been measured.
  2. **How many distinct EXPERIMENTS support each partner**, as opposed to how many IntAct
     rows. UniProt's `NbExp=4` for ADCK5-NOTCH2NLA counts three sub-method labels of one
     yeast two-hybrid screen plus one further screen.

Deliberate choices:

* Partners are resolved by **UniProt accession** (`uniqueIdA`/`uniqueIdB`), never by gene
  symbol. Two of ADCK5's partner symbols, `HARS2` and `MRPL2`, each match two reviewed
  Swiss-Prot entries, so a symbol-keyed lookup would silently pick one.
* The IntAct pull compares `len(rows)` against `totalElements` — never against the page size
  we chose — because the service may clamp rather than error, and a page-size comparison
  cannot see that.
* Every resolved accession's entry name is printed and an empty one is a hard error: a
  deleted UniProt entry returns no name and no annotations, which is indistinguishable from a
  real protein that simply has no subcellular location.
"""

from __future__ import annotations

import json
import sys
import time
import urllib.request
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "partner_localisation.json"

SUBJECT = "Q3MIX3"
# The mitochondrial protein interaction map (Floyd et al. 2016), ADCK5's largest dataset.
MITO_INTERACTOME_PMID = "27499296"
# The two references behind ADCK5's GO:0005515 rows.
GOA_BINDING_PMIDS = {"25416956", "31515488"}


def get(url: str) -> dict:
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"Accept": "application/json"})))


def fetch_interactions() -> list[dict]:
    rows: list[dict] = []
    page = 0
    total = None
    while True:
        d = get(
            "https://www.ebi.ac.uk/intact/ws/interaction/findInteractions/"
            f"{SUBJECT}?page={page}&pageSize=100"
        )
        total = d["totalElements"]
        content = d.get("content", [])
        rows += content
        if not content or len(rows) >= total:
            break
        page += 1
    if len(rows) != total:
        raise SystemExit(
            f"FATAL: IntAct truncation - retrieved {len(rows)} of {total} records for "
            f"{SUBJECT}. Do not draw partner conclusions from a partial pull."
        )
    print(f"  IntAct: retrieved {len(rows)} of {total} records (no truncation)", file=sys.stderr)
    return rows


def pmid_of(rec: dict) -> str | None:
    for p in rec.get("publicationIdentifiers") or []:
        if "pubmed" in p:
            return p.split()[0]
    return None


def partner_of(rec: dict) -> tuple[str, str]:
    """Return (accession, symbol) of the non-ADCK5 side."""
    if rec.get("uniqueIdA") == SUBJECT:
        return rec.get("uniqueIdB"), rec.get("moleculeB")
    return rec.get("uniqueIdA"), rec.get("moleculeA")


def subcellular(acc: str) -> tuple[str, list[str]]:
    d = get(
        f"https://rest.uniprot.org/uniprotkb/{acc}.json"
        "?fields=accession,id,cc_subcellular_location"
    )
    entry_name = d.get("uniProtkbId")
    if not entry_name:
        raise SystemExit(
            f"FATAL: {acc} returned no entry name - this is what a deleted UniProt entry "
            f"looks like, and it is indistinguishable from a protein with no annotations."
        )
    locs = []
    for c in d.get("comments", []):
        if c["commentType"] == "SUBCELLULAR LOCATION":
            for l in c.get("subcellularLocations", []):
                v = l.get("location", {}).get("value")
                if v:
                    locs.append(v)
    return entry_name, sorted(set(locs))


def main() -> int:
    rows = fetch_interactions()

    # --- experiment independence per partner ---
    per_partner: dict[str, dict] = defaultdict(
        lambda: {"symbol": None, "pmids": set(), "methods": set(), "n_rows": 0, "scores": set()}
    )
    for r in rows:
        acc, sym = partner_of(r)
        p = per_partner[acc]
        p["symbol"] = sym
        p["n_rows"] += 1
        pm = pmid_of(r)
        if pm:
            p["pmids"].add(pm)
        p["methods"].add(r.get("detectionMethod"))
        if r.get("intactMiscore") is not None:
            p["scores"].add(r["intactMiscore"])

    # --- localisation of the mitochondrial-interactome partners ---
    mito_partners = {}
    for r in rows:
        if pmid_of(r) == MITO_INTERACTOME_PMID:
            acc, sym = partner_of(r)
            mito_partners[acc] = sym

    print(f"  resolving {len(mito_partners)} partner accessions...", file=sys.stderr)
    resolved = {}
    n_mito = 0
    for acc, sym in sorted(mito_partners.items()):
        entry_name, locs = subcellular(acc)
        is_mito = any("Mitochond" in x for x in locs)
        n_mito += is_mito
        resolved[acc] = {
            "symbol": sym,
            "entry_name": entry_name,
            "locations": locs,
            "mitochondrial": is_mito,
        }
        print(f"    {acc} {entry_name:<14} {sym:<10} mito={is_mito}", file=sys.stderr)
        time.sleep(0.05)

    # --- the GO:0005515 partners specifically ---
    goa_partners = {}
    for r in rows:
        if pmid_of(r) in GOA_BINDING_PMIDS:
            acc, sym = partner_of(r)
            g = goa_partners.setdefault(
                acc,
                {
                    "symbol": sym,
                    "rows": [],
                    "pmids": set(),
                    "methods": set(),
                    # Per-PMID method split: this is what shows that one screen is logged
                    # under several sub-method labels, as opposed to several screens agreeing.
                    "methods_by_pmid": defaultdict(set),
                    "mi_scores": set(),
                },
            )
            g["rows"].append(r.get("detectionMethod"))
            g["pmids"].add(pmid_of(r))
            g["methods"].add(r.get("detectionMethod"))
            g["methods_by_pmid"][pmid_of(r)].add(r.get("detectionMethod"))
            if r.get("intactMiscore") is not None:
                g["mi_scores"].add(r["intactMiscore"])

    out = {
        "subject": SUBJECT,
        "n_intact_records": len(rows),
        "n_distinct_partners": len(per_partner),
        "mito_interactome": {
            "pmid": MITO_INTERACTOME_PMID,
            "n_partners": len(mito_partners),
            "n_mitochondrial": n_mito,
            "fraction_text": f"{n_mito} of {len(mito_partners)}",
            "partners": resolved,
        },
        "goa_binding_partners": {
            acc: {
                "symbol": g["symbol"],
                "n_intact_rows": len(g["rows"]),
                "n_distinct_pmids": len(g["pmids"]),
                "pmids": sorted(g["pmids"]),
                "distinct_methods": sorted(m for m in g["methods"] if m),
                "methods_by_pmid": {
                    pm: sorted(ms) for pm, ms in sorted(g["methods_by_pmid"].items())
                },
                # A single distinct score across every row is itself evidence that the rows
                # are not independent observations.
                "mi_scores": sorted(g["mi_scores"]),
            }
            for acc, g in goa_partners.items()
        },
        "orthogonal_assay_for_goa_partners": {
            acc: any(
                m and "two hybrid" not in m.lower()
                for m in per_partner[acc]["methods"]
            )
            for acc in goa_partners
        },
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print()
    print(f"IntAct records: {out['n_intact_records']}   distinct partners: {out['n_distinct_partners']}")
    print(
        f"Mitochondrial-interactome partners annotated to the mitochondrion: "
        f"{out['mito_interactome']['fraction_text']}"
    )
    print()
    print("GO:0005515 partners:")
    for acc, g in out["goa_binding_partners"].items():
        orth = out["orthogonal_assay_for_goa_partners"][acc]
        print(
            f"  {g['symbol']} ({acc}): {g['n_intact_rows']} IntAct rows across "
            f"{g['n_distinct_pmids']} publication(s); MI scores = {g['mi_scores']}"
        )
        for pm, ms in g["methods_by_pmid"].items():
            print(f"    PMID:{pm}: {len(ms)} method label(s) -> {ms}")
        print(f"    any non-two-hybrid assay anywhere in IntAct for this pair? {orth}")
    print(f"\nWrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
