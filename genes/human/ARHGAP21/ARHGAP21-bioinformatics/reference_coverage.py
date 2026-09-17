#!/usr/bin/env python3
"""Ask what each ARHGAP21 primary paper actually produced in GOA, and check the
ARHGAP10/ARHGAP21 nomenclature trap.

Two independent questions, both answered by querying QuickGO **by reference**
rather than by gene:

1. **Coverage.**  For each primary paper about the human protein, how many GO
   annotations exist anywhere in GOA, and how many are on ARHGAP21?  A paper
   whose central finding produced no annotation is a coverage defect, and a
   paper that annotates many entities with identical evidence is a projection
   rather than N independent findings.

2. **Mis-attribution.**  Both 2005 primary papers call the protein
   "ARHGAP10", which was ARHGAP21's symbol at the time.  HGNC has since
   assigned `ARHGAP10` to a *different* gene (A1A4S6, a GRAF-family protein
   that is NOT in PANTHER PTHR23175).  If any annotation from those PMIDs
   landed on A1A4S6, that is a name-collision error.  Querying by reference
   settles it: the answer is the full entity list for the reference, so the
   check cannot miss a hit the way a gene-keyed query would.

Note on counting: QuickGO's `numberOfHits` counts **annotations**, not
entities; one entity can hold several.  Entities are derived here as a distinct
set of gene-product ids.  If a result is paginated (hits > rows returned) the
entity count is reported as unavailable rather than inferred from one page.

Run:  uv run --with requests python reference_coverage.py
Writes: reference_coverage.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import requests

SEARCH = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

ARHGAP21 = "Q5T5U3"
# The gene that now holds the symbol ARHGAP21 used to carry.
ARHGAP10_MODERN = "A1A4S6"
# The close paralog, PTHR23175:SF5.
ARHGAP23 = "Q9P227"

# Primary papers about the human protein (excludes large-scale interactome
# screens, whose entity counts are dominated by the screen's design).
PRIMARY_PMIDS = {
    "15793564": "Dubois 2005 - Cdc42 GAP, ARF1 recruitment, Arp2/3 & F-actin",
    "16184169": "Sousa 2005 - alpha-catenin, RhoA+Cdc42 GAP, Listeria entry",
    "16527809": "Klein 2006 - ARF6 GDP/GTP cycle",
    "17347647": "Menetrey 2007 - ARF1/ArfBD crystal structure 2.1 A",
    "20525016": "Hehnly 2010 - microtubule-dependent Golgi positioning",
    "21173159": "Anthony 2011 - beta-arrestin1 inhibits GAP, RhoA",
    "22922005": "Bigarella 2012 - SUMO2/3 at K1444",
    "23200924": "Lazarini 2013 - RhoA/RhoC GAP in PC3",
    "23235160": "Barcellos 2013 - Cdc42 at junctions, alpha-tubulin acetylation",
    "29212046": "Rodrigues 2017 - RhoC, hematopoiesis",
}

# Large-scale screens, kept separate so their entity counts do not get read as
# evidence about ARHGAP21.
SCREEN_PMIDS = {
    "15161933": "Meek 2004 - 14-3-3 proteomics",
    "15778465": "Benzinger 2005 - 14-3-3 sigma proteomics",
    "26496610": "Hein 2015 - 3D interactome",
    "28514442": "Huttlin 2017 - BioPlex",
    "33961781": "Huttlin 2021 - BioPlex 3.0",
    "36115835": "Gogl 2022 - PDZ/PBM fragmentomics",
    "36931259": "Segal 2023 - 14-3-3 chaperone-like",
}

LIMIT = 100  # QuickGO caps annotation-search rows at 100.


def query_reference(pmid: str) -> dict[str, object]:
    resp = requests.get(
        SEARCH,
        params={"reference": f"PMID:{pmid}", "limit": LIMIT},
        headers={"Accept": "application/json"},
        timeout=90,
    )
    resp.raise_for_status()
    d = resp.json()
    results = d.get("results") or []
    hits = d.get("numberOfHits")

    # Compare numberOfHits against len(results), never against a page-size
    # constant: if the service clamps instead of erroring, a guard keyed on the
    # constant sails past while rows were silently dropped.
    truncated = hits is not None and hits > len(results)

    entities = sorted({r["geneProductId"] for r in results})
    on_target = [r for r in results if r["geneProductId"] == f"UniProtKB:{ARHGAP21}"]
    on_arhgap10 = [
        r for r in results if r["geneProductId"] == f"UniProtKB:{ARHGAP10_MODERN}"
    ]
    on_arhgap23 = [
        r for r in results if r["geneProductId"] == f"UniProtKB:{ARHGAP23}"
    ]
    return {
        "pmid": pmid,
        "annotations_total": hits,
        "rows_returned": len(results),
        "truncated": truncated,
        "entity_count": None if truncated else len(entities),
        "entities": None if truncated else entities,
        "arhgap21_rows": [
            {"go_id": r["goId"], "evidence": r["goEvidence"], "assigned_by": r.get("assignedBy")}
            for r in on_target
        ],
        "arhgap10_modern_rows": [
            {"go_id": r["goId"], "evidence": r["goEvidence"]} for r in on_arhgap10
        ],
        "arhgap23_rows": [
            {"go_id": r["goId"], "evidence": r["goEvidence"]} for r in on_arhgap23
        ],
    }


def main() -> int:
    primary = {p: query_reference(p) for p in PRIMARY_PMIDS}
    screens = {p: query_reference(p) for p in SCREEN_PMIDS}

    # Assert presence rather than validating only what we happen to find.
    assert set(primary) == set(PRIMARY_PMIDS), "primary PMID set changed during query"
    assert set(screens) == set(SCREEN_PMIDS), "screen PMID set changed during query"

    misattributed = {
        p: v["arhgap10_modern_rows"]
        for p, v in {**primary, **screens}.items()
        if v["arhgap10_modern_rows"]
    }

    # A paper that produced no ARHGAP21 annotation at all is a coverage gap.
    # Distinguish it from a paper we could not fully read (truncated).
    zero_on_target = sorted(
        p for p, v in primary.items() if not v["arhgap21_rows"] and not v["truncated"]
    )
    unknown_on_target = sorted(p for p, v in primary.items() if v["truncated"])

    out = {
        "arhgap21": ARHGAP21,
        "arhgap10_modern": ARHGAP10_MODERN,
        "arhgap23": ARHGAP23,
        "primary_papers": primary,
        "screen_papers": screens,
        "primary_labels": PRIMARY_PMIDS,
        "screen_labels": SCREEN_PMIDS,
        "primary_papers_with_zero_arhgap21_annotations": zero_on_target,
        "primary_papers_truncated_so_unknown": unknown_on_target,
        "misattributed_to_modern_arhgap10": misattributed,
    }

    dest = Path(__file__).with_name("reference_coverage.json")
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print("PRIMARY PAPERS (human ARHGAP21)")
    print(f"{'PMID':<10} {'annots':>7} {'ents':>5} {'onARHGAP21':>11}  terms")
    for p in sorted(PRIMARY_PMIDS):
        v = primary[p]
        terms = ",".join(r["go_id"] + "/" + r["evidence"] for r in v["arhgap21_rows"])
        ents = "trunc" if v["truncated"] else str(v["entity_count"])
        print(
            f"{p:<10} {str(v['annotations_total']):>7} {ents:>5} "
            f"{len(v['arhgap21_rows']):>11}  {terms or '-'}"
        )
    print()
    print("SCREENS")
    for p in sorted(SCREEN_PMIDS):
        v = screens[p]
        ents = "trunc" if v["truncated"] else str(v["entity_count"])
        print(
            f"{p:<10} annots={str(v['annotations_total']):>6} entities={ents:>6} "
            f"onARHGAP21={len(v['arhgap21_rows'])}"
        )
    print()
    print("primary papers producing ZERO ARHGAP21 annotations:", zero_on_target)
    print("primary papers truncated (coverage unknown):", unknown_on_target)
    print("annotations mis-landed on modern ARHGAP10 (A1A4S6):", misattributed or "NONE")
    print(f"\nwrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
