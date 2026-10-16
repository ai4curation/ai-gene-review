#!/usr/bin/env python3
"""Is ARHGAP4's GO record an over-annotation problem or a coverage problem?

Human ARHGAP4 (``P98171``) has **no experimental function annotation at all**: its
`GO:0005096` rows are IBA, IEA and two TAS, and its only IDA rows are localisation
from HPA and LIFEdb.  Meanwhile the literature contains direct biochemistry (rat
GAP assay), structure/function mapping, human loss-of-function genetics and a
defined protein complex.  That mismatch has two possible shapes and they call for
opposite curation actions:

* **over-annotation** -- terms asserted beyond what the papers support; or
* **missing curation** -- papers that support terms nobody entered.

The question is settled by querying QuickGO **by reference** rather than by gene:
for each primary paper, how many GO annotations exist anywhere in GOA, and how
many land on ARHGAP4 in *any* species?  A paper whose central finding produced no
annotation on any ortholog is a coverage defect, not an over-annotation.

Species matters here and the query is deliberately species-blind.  Two of the
three mechanistic papers used the **rat** protein, and human ARHGAP4's
`GO_REF:0000107` rows are Ensembl-Compara projections from rat
``UniProtKB:A0A0G2JVF0``.  Asking only about ``P98171`` would score those papers
as uncurated when they may have been curated on the rat gene and projected
across; asking about every gene product named ARHGAP4/Arhgap4 separates
"uncurated" from "curated elsewhere and projected".

Counting note: QuickGO's ``numberOfHits`` counts **annotations**, not entities.  A
result set larger than the page returned is reported as ``truncated`` and its
per-gene zeros are recorded as *unknown*, never as zero -- an empty first page of
a large screen says nothing.

Run:    uv run --with requests python reference_coverage.py
        uv run --with requests python reference_coverage.py --self-test
Writes: reference_coverage.json
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
from pathlib import Path

import requests

SEARCH = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
LIMIT = 100  # QuickGO caps annotation-search rows at 100.

HUMAN = "P98171"
RAT_TREMBL = "A0A0G2JVF0"  # the Ensembl-Compara donor for every GO_REF:0000107 row

# Papers whose subject is ARHGAP4 itself (the protein, the gene, or a patient
# deletion of it).  Large-scale screens are held separately below.
PRIMARY = {
    "8570618": "Tribioli 1996 - cloning of human C1/ARHGAP4, hematopoietic, stress fibres",
    "12414125": "Foletta 2002 - rat ARHGAP4; in vitro GAP on RAC1/CDC42/RHOA; Golgi, microtubules",
    "17804252": "Vogt 2007 - FCH/GAP/SH3 structure-function; inhibits migration and axon outgrowth",
    "34524873": "Xu 2021 - ARHGAP4-SEPT2-SEPT9 complex; focal adhesions, integrin beta-1",
    "32378260": "Katsuno 2020 - whole Rho-GAP family screen; EMT suppression; Septin9",
    "30958531": "Shen 2019 - HDAC2/beta-catenin; pancreatic cancer invasion",
    "31303760": "Zhang 2019 - mTOR/HIF-1alpha; Warburg effect",
    "32021284": "Chen 2020 - miR-939-5p targets ARHGAP4",
    "37443303": "Wang 2023 - p53/DRAM1; AML",
    "40817404": "Liu 2025 - MYH9/beta-catenin/c-Jun; colorectal stemness",
    "38805788": "Sun 2024 - TGF-beta/Smad; colon cancer metastasis",
    "38355537": "Wu 2024 - granulosa cell apoptosis; PI3K-Akt",
    "38938545": "Ma 2024 - SW620 proliferation, cell cycle",
    "26707211": "Liu 2016 - ARHGAP4 T491M in an X-linked intellectual disability family",
    "39060771": "Hu 2024 - ARHGAP4 variants in X-linked early-onset temporal lobe epilepsy",
    "16781893": "Broides 2006 - SCID + NDI; 34.4 kb Xq28 deletion spanning ARHGAP4",
    "18489790": "Fujimoto 2008 - immunological profile; 11 kb AVPR2/ARHGAP4 deletion",
    "10425039": "Schoneberg 1999 - compound deletion of rhoGAP C1 and V2 receptor",
    "22965914": "Kalra 2012 - AVPR2/ARHGAP4 contiguous deletion in twins",
}

# Interactome / proteome screens.  Their entity counts are set by the screen's
# design, so they are reported apart and never used as evidence about ARHGAP4.
SCREENS = {
    "16417406": "Weiner 2006 - Hem-1/NCKAP1L complex proteomics (the GO:0005515 IPI source)",
    "18669648": "Dephoure 2008 - mitotic phosphorylation atlas",
    "19690332": "Mayya 2009 - TCR phosphoproteomics",
    "23186163": "Zhou 2013 - cancer cell phosphoproteome",
}


def query_reference(pmid: str) -> dict[str, object]:
    r = requests.get(
        SEARCH,
        params={"reference": f"PMID:{pmid}", "limit": LIMIT},
        headers={"Accept": "application/json"},
        timeout=120,
    )
    r.raise_for_status()
    d = r.json()
    results = d.get("results") or []
    hits = d.get("numberOfHits")
    # Compare numberOfHits against len(results), never against LIMIT: if the
    # service clamps silently rather than erroring, a guard keyed on the constant
    # sails past while rows were dropped.
    truncated = hits is not None and hits > len(results)

    def rows_for(pred) -> list[dict[str, str]]:
        return [
            {
                "gene_product": x["geneProductId"],
                "symbol": x.get("symbol"),
                "taxon": x.get("taxonId"),
                "go_id": x["goId"],
                "evidence": x.get("goEvidence"),
                "qualifier": x.get("qualifier"),
                "assigned_by": x.get("assignedBy"),
            }
            for x in results
            if pred(x)
        ]

    def page_scoped(rows: list[dict[str, str]]) -> object:
        # A per-gene zero taken from ONE PAGE of a truncated result is a page
        # artefact that reads as a finding.  Report unknown, not zero.
        return None if (truncated and not rows) else rows

    any_arhgap4 = rows_for(lambda x: (x.get("symbol") or "").upper() == "ARHGAP4")
    return {
        "pmid": pmid,
        "annotations_total": hits,
        "rows_returned": len(results),
        "truncated": truncated,
        "entity_count": None if truncated else len({x["geneProductId"] for x in results}),
        "human_rows": page_scoped(
            rows_for(lambda x: x["geneProductId"] == f"UniProtKB:{HUMAN}")
        ),
        "arhgap4_any_species_rows": page_scoped(any_arhgap4),
    }


GO_API_GENE = "https://api.geneontology.org/api/bioentity/gene/{gid}/function"


def ortholog_annotations(gene_product: str) -> dict[str, object]:
    """What the Ensembl-Compara donor actually carries, and on what evidence.
    A projection is only as good as its source row.

    Two resolvers, because neither covers both id spaces: QuickGO's
    ``geneProductId`` rejects MOD identifiers (``RGD:628901`` returns HTTP 400),
    while the GO API's bioentity endpoint serves them.  Dispatching on the prefix
    is not a workaround, it is the correct service for each namespace."""
    if gene_product.startswith("UniProtKB:"):
        r = requests.get(
            SEARCH,
            params={"geneProductId": gene_product, "limit": LIMIT},
            headers={"Accept": "application/json"},
            timeout=120,
        )
        r.raise_for_status()
        d = r.json()
        rows = d.get("results") or []
        if d.get("numberOfHits") is not None and d["numberOfHits"] > len(rows):
            raise RuntimeError(f"paginated annotation set for {gene_product}")
        return {
            "gene_product": gene_product,
            "source": "QuickGO",
            "n": d.get("numberOfHits"),
            "rows": [
                {
                    "go_id": x["goId"],
                    "go_name": x.get("goName"),
                    "evidence": x.get("goEvidence"),
                    "reference": x.get("reference"),
                    "qualifier": x.get("qualifier"),
                    "assigned_by": x.get("assignedBy"),
                }
                for x in rows
            ],
        }

    r = requests.get(
        GO_API_GENE.format(gid=urllib.parse.quote(gene_product, safe="")),
        params={"rows": 200},
        timeout=120,
    )
    r.raise_for_status()
    assocs = r.json().get("associations") or []
    return {
        "gene_product": gene_product,
        "source": "GO API",
        "n": len(assocs),
        "rows": [
            {
                "go_id": a["object"]["id"],
                "go_name": a["object"].get("label"),
                "evidence": (a.get("evidence_type") or ""),
                "reference": ",".join(a.get("reference") or []),
                "qualifier": ",".join(a.get("qualifiers") or []),
                "assigned_by": a.get("provided_by"),
            }
            for a in assocs
        ],
    }


def run() -> dict[str, object]:
    primary = {p: query_reference(p) for p in PRIMARY}
    screens = {p: query_reference(p) for p in SCREENS}
    assert set(primary) == set(PRIMARY), "primary PMID set changed during query"
    assert set(screens) == set(SCREENS), "screen PMID set changed during query"

    zero_anywhere = sorted(
        p
        for p, v in primary.items()
        if v["arhgap4_any_species_rows"] == [] and not v["truncated"]
    )
    zero_on_human_only = sorted(
        p
        for p, v in primary.items()
        if not v["truncated"]
        and v["human_rows"] == []
        and v["arhgap4_any_species_rows"]
    )
    unknown = sorted(p for p, v in primary.items() if v["truncated"])

    donors = {
        acc: ortholog_annotations(acc)
        for acc in (f"UniProtKB:{RAT_TREMBL}", "RGD:628901")
    }

    return {
        "human": HUMAN,
        "primary_labels": PRIMARY,
        "screen_labels": SCREENS,
        "primary_papers": primary,
        "screen_papers": screens,
        "primary_papers_with_zero_arhgap4_annotations_anywhere": zero_anywhere,
        "primary_papers_curated_on_an_ortholog_but_not_on_human": zero_on_human_only,
        "primary_papers_truncated_so_unknown": unknown,
        "n_primary": len(PRIMARY),
        "ensembl_projection_donors": donors,
    }


def self_test() -> int:
    checks: list[tuple[str, str]] = []

    # 1. The species-blind matcher must actually find a non-human ARHGAP4 row if
    #    one exists.  Run it against the rat donor's own reference set.
    rat = ortholog_annotations(f"UniProtKB:{RAT_TREMBL}")
    checks.append(
        (
            "rat donor returns annotations (query shape is right)",
            "PASS" if rat["n"] and rat["n"] > 0 else f"FAIL {rat['n']}",
        )
    )

    # 2. A reference that certainly HAS annotations must not read as zero --
    #    otherwise every 'zero' below is just a broken query.
    pos = query_reference("8570618")  # the source of four TAS rows on P98171
    checks.append(
        (
            "positive control: PMID:8570618 returns ARHGAP4 rows",
            "PASS" if pos["arhgap4_any_species_rows"] else f"FAIL {pos}",
        )
    )

    # 3. A reference with genuinely no GO annotations must read zero, not error.
    neg = query_reference("39060771")
    checks.append(
        (
            "a reference with no annotations reads as an empty list",
            "PASS"
            if neg["arhgap4_any_species_rows"] == [] and not neg["truncated"]
            else f"FAIL {neg}",
        )
    )

    # 4. Truncation must be reported as unknown, not zero.  PMID:33961781 is
    #    BioPlex 3.0, whose result set is far larger than one page; if it ever
    #    stops being truncated the guard is no longer exercised and that is
    #    itself a failure, not a silent pass.
    big = query_reference("33961781")
    if not big["truncated"]:
        checks.append(
            (
                "truncation guard exercised",
                f"FAIL (PMID:33961781 not truncated: {big['annotations_total']} hits) -- pick a larger screen",
            )
        )
    else:
        checks.append(
            (
                "truncated result reports unknown rather than zero",
                "PASS"
                if big["arhgap4_any_species_rows"] is None
                or big["arhgap4_any_species_rows"]
                else f"FAIL {big['arhgap4_any_species_rows']!r} (a page-scoped zero)",
            )
        )

    # 5. A nonsense PMID must come back empty rather than matching something.
    bogus = query_reference("99999999")
    checks.append(
        (
            "nonexistent reference returns no rows",
            "PASS" if bogus["annotations_total"] in (0, None) else f"FAIL {bogus['annotations_total']}",
        )
    )

    for name, verdict in checks:
        print(
            f"  [{verdict.split()[0]}] {name}"
            + ("" if verdict.startswith("PASS") else f" -- {verdict}")
        )
    bad = [c for c in checks if not c[1].startswith("PASS")]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} self-tests passed")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    out = run()
    dest = Path(__file__).with_name("reference_coverage.json")
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    def fmt(rows: object) -> str:
        if rows is None:
            return "unknown(truncated)"
        if not rows:
            return "-"
        return ",".join(f"{r['symbol']}:{r['go_id']}/{r['evidence']}" for r in rows)

    print("PRIMARY PAPERS ABOUT ARHGAP4")
    print(f"{'PMID':<10} {'annots':>7} {'ents':>6}  rows on ARHGAP4 (any species)")
    for p in PRIMARY:
        v = out["primary_papers"][p]
        ents = "trunc" if v["truncated"] else str(v["entity_count"])
        print(f"{p:<10} {str(v['annotations_total']):>7} {ents:>6}  {fmt(v['arhgap4_any_species_rows'])}")
    print()
    print("SCREENS")
    for p in SCREENS:
        v = out["screen_papers"][p]
        ents = "trunc" if v["truncated"] else str(v["entity_count"])
        print(f"{p:<10} annots={str(v['annotations_total']):>6} entities={ents:>6} ARHGAP4={fmt(v['arhgap4_any_species_rows'])}")
    print()
    z = out["primary_papers_with_zero_arhgap4_annotations_anywhere"]
    print(f"primary papers producing ZERO ARHGAP4 annotations in ANY species: {len(z)}/{out['n_primary']}")
    for p in z:
        print(f"   {p}  {PRIMARY[p]}")
    print("curated on an ortholog but not on human:", out["primary_papers_curated_on_an_ortholog_but_not_on_human"] or "none")
    print("truncated (coverage unknown):", out["primary_papers_truncated_so_unknown"] or "none")
    print()
    for acc, d in out["ensembl_projection_donors"].items():
        print(f"projection donor {acc}: {d['n']} annotations")
        for r in d["rows"]:
            print(f"   {r['go_id']} {r['go_name']} {r['evidence']} {r['reference']} ({r['assigned_by']})")
    print(f"\nwrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
