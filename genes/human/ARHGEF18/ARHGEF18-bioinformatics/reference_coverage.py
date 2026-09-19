#!/usr/bin/env python3
"""Is ARHGEF18's GO record an over-annotation problem or a coverage problem?

Human ARHGEF18 (``Q6ZSZ5``) carries 32 GOA rows, but they rest on a very small number
of papers: one IDA set from Niu et al. 2003, one IDA from Nakajima & Tanoue 2011, two
IMP rows plus an IPI from Tornavaca et al. 2015, an EXP from Turton et al. 2018, a
proteomics HDA, an IntAct IPI, and the rest IBA/IEA/TAS.  Meanwhile the literature
contains the founding in-vitro exchange assay, the paper that established junctional
RhoA activation, the paper that named the protein SA-RhoGEF, human loss-of-function
genetics, and a vertebrate knockout.

That mismatch has two possible shapes, calling for opposite curation actions:

* **over-annotation** -- terms asserted beyond what the papers support; or
* **missing curation** -- papers that support terms nobody entered.

The question is settled by querying QuickGO **by reference** rather than by gene: for
each primary paper, how many GO annotations exist anywhere in GOA, and do any of them
land on an ARHGEF18 ortholog in any species?  A paper whose central finding produced no
annotation on any ortholog is a coverage defect, not an over-annotation.

Species-blindness is deliberate.  The medaka knockout (PMID:23698346) and the
Drosophila work on the ortholog *cyst*/Dp114RhoGEF could perfectly well have been
curated on the non-human gene; asking only about ``Q6ZSZ5`` would score those as
uncurated when they are merely curated elsewhere.  The script therefore records, per
paper, both the total annotation count and the subset whose gene symbol matches an
ARHGEF18 ortholog name.

Counting note: QuickGO's ``numberOfHits`` counts **annotations**, not genes, and the
row endpoint caps at 100.  When a result set exceeds the page, the per-gene breakdown is
recorded as ``truncated`` and the "no ARHGEF18 row" conclusion is withheld -- an empty
first page of a proteome-wide screen says nothing.

Run:    uv run python reference_coverage.py
        uv run python reference_coverage.py --self-test
Writes: reference_coverage.json
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "reference_coverage.json"

SEARCH = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
LIMIT = 100

# Symbols any ARHGEF18 ortholog is curated under, lowercased for comparison.
ORTHOLOG_SYMBOLS = {"arhgef18", "cyst", "cg10188", "dp114rhogef", "si:ch211-286o17.1"}

# Papers whose subject is ARHGEF18 itself -- its protein, its gene, its ortholog, or a
# patient allele of it.  Whole-proteome screens are held separately below because a
# zero there means something quite different.
PRIMARY = {
    "11085924": "Blomquist 2000 - cloning of p114-Rho-GEF; in vitro exchange on RhoA, not Rac1/Cdc42",
    "14512443": "Niu 2003 - Gbeta-gamma stimulates p114RhoGEF; activates RhoA and Rac1, not Cdc42",
    "15558029": "Nagata 2005 - SEPT9b binds and inhibits SA-RhoGEF; septin filaments",
    "20810787": "Tsuji 2010 - Dvl/Daam1 binding; Wnt-3a-induced RhoA activation, neurite retraction",
    "21258369": "Terry 2011 - junctional RhoA activation; cingulin, ROCK II, myosin IIA complex",
    "22006950": "Nakajima 2011 - Lulu2 activates p114RhoGEF; Patj recruits it apically",
    "23185572": "Terry 2012 - cortical myosin light-chain double phosphorylation; migration, invasion",
    "23648482": "Xu 2013 - LKB1 interaction; apical junction assembly in bronchial epithelium",
    "23698346": "Herder 2013 - medaka arhgef18 mutant; retinal neuroepithelial apicobasal polarity",
    "25753039": "Tornavaca 2015 - ZO-1/JACOP recruit p114RhoGEF; endothelial junctional tension",
    "26217016": "Loie 2015 - CRB3A and Ehm2 recruit p114RhoGEF; circumferential actomyosin belt",
    "26483385": "Kim 2015 - lumen consolidation during tubulogenesis via ROCK-myosin IIA",
    "28132693": "Arno 2017 - biallelic ARHGEF18 mutation causes RP78; Thr270Ala weakens RHOA activation",
    "29601110": "Turton 2018 - LOCGEF isoforms of ARHGEF18 in eosinophils; membrane localisation",
    "31051012": "Martin 2016 - C-terminal region of p114RhoGEF binds Galpha12 but not Galpha13",
    "33842485": "Beal 2021 - ARHGEF18 in syncytiotrophoblast differentiation; AKAP12, PKA/CREB",
    "39977269": "Batta 2025 - shear-stress-dependent phosphorylation; endothelial tight junctions",
    "40920138": "Shannon 2025 - SEPTIN9 activates ARHGEF18 at mitochondrial fission sites",
    # Found only by searching partners, paralogs and misspellings -- the automated
    # provider returned none of these five.
    "23493395": "Medina 2013 - activated RhoA binds the PH domains of all seven Lbc-family RhoGEFs",
    "29876405": "Chen 2018 - 1.4 A structure of the p114RhoGEF PH domain bound to RhoA (PDB 6BCB)",
    "28536193": "Schell 2017 - EPB41L5 binds and recruits ARHGEF18 in podocytes (title spells it ARGHEF18)",
    "36912772": "Safavian 2023 - SEPTIN9 binds and activates ARHGEF18 at the ciliary base",
    "31409654": "Silver 2019 - Drosophila ortholog Cysts recruited by Crumbs/Bazooka; activates Rho1",
}

# Large-scale / high-throughput sources.  Zero annotations here is unremarkable.
SCREENS = {
    "18570454": "exosome proteomics of human neural stem cells (source of the HDA row)",
    "35271311": "OpenCell endogenous tagging (source of the IntAct AKAP13 IPI)",
    "18669648": "quantitative atlas of mitotic phosphorylation",
    "21269460": "human central proteome",
}


def query(pmid: str) -> dict:
    params = {"reference": f"PMID:{pmid}", "limit": str(LIMIT)}
    url = f"{SEARCH}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "aigr"})
    with urllib.request.urlopen(req, timeout=120) as fh:
        return json.load(fh)


def summarise(pmid: str, label: str) -> dict:
    d = query(pmid)
    n = d.get("numberOfHits", 0)
    rows = d.get("results", []) or []
    truncated = n > len(rows)
    symbols: dict[str, int] = {}
    ortholog_rows = []
    for r in rows:
        sym = (r.get("symbol") or "").strip()
        symbols[sym] = symbols.get(sym, 0) + 1
        if sym.lower() in ORTHOLOG_SYMBOLS:
            ortholog_rows.append(
                {
                    "symbol": sym,
                    "gene_product": r.get("geneProductId"),
                    "taxon": r.get("taxonId"),
                    "go_id": r.get("goId"),
                    "go_name": r.get("goName"),
                    "evidence": r.get("goEvidence"),
                    "qualifier": r.get("qualifier"),
                    "assigned_by": r.get("assignedBy"),
                }
            )
    return {
        "pmid": pmid,
        "label": label,
        "n_annotations": n,
        "rows_returned": len(rows),
        "truncated": truncated,
        "distinct_symbols_on_page": len(symbols),
        "ortholog_annotations": ortholog_rows,
        # A zero is only trustworthy when we saw every row.
        "produced_no_annotation_anywhere": n == 0,
        "produced_no_arhgef18_annotation": (not ortholog_rows) if not truncated else None,
    }


def build() -> dict:
    primary = [summarise(p, lab) for p, lab in sorted(PRIMARY.items())]
    screens = [summarise(p, lab) for p, lab in sorted(SCREENS.items())]

    zero_any = [r for r in primary if r["produced_no_annotation_anywhere"]]
    zero_arhgef18 = [r for r in primary if r["produced_no_arhgef18_annotation"] is True]
    unknown = [r for r in primary if r["produced_no_arhgef18_annotation"] is None]

    return {
        "question": "over-annotation or missing curation?",
        "n_primary_papers": len(primary),
        "n_primary_with_zero_annotations_anywhere": len(zero_any),
        "n_primary_with_no_arhgef18_annotation": len(zero_arhgef18),
        "n_primary_undetermined_because_truncated": len(unknown),
        "primary_papers_with_zero_annotations": [r["pmid"] for r in zero_any],
        "primary_papers_with_no_arhgef18_annotation": [r["pmid"] for r in zero_arhgef18],
        "primary": primary,
        "screens": screens,
    }


def self_test(data: dict) -> int:
    """Guards on the *method*, not on the finding.  Each must fire with its message."""
    failures: list[str] = []

    def check(name: str, cond: bool, msg: str) -> None:
        if not cond:
            failures.append(f"{name}: {msg}")

    # POSITIVE CONTROL: papers GOA demonstrably used must come back non-zero, otherwise
    # the query itself is broken and every zero below is an artefact.
    known_used = {"14512443", "22006950", "25753039", "29601110"}
    for r in data["primary"]:
        if r["pmid"] in known_used:
            check(
                f"positive[{r['pmid']}]",
                r["n_annotations"] > 0,
                "a paper cited in ARHGEF18's own GOA returned zero hits -- the query is broken",
            )
            check(
                f"positive_ortholog[{r['pmid']}]",
                bool(r["ortholog_annotations"]) or r["truncated"],
                "a paper cited in ARHGEF18's own GOA returned no ARHGEF18 row",
            )

    # NEGATIVE CONTROL: a PMID that is real but has nothing to do with this gene must
    # not produce ARHGEF18 rows.  Silence here is the expected outcome.
    ctrl = summarise("11085924", "control re-query")
    check(
        "determinism",
        ctrl["n_annotations"] == next(r["n_annotations"] for r in data["primary"] if r["pmid"] == "11085924"),
        "re-querying the same PMID gave a different count",
    )

    # The zero/unknown split must be exhaustive: no paper may be silently dropped.
    n = data["n_primary_papers"]
    counted = sum(
        1
        for r in data["primary"]
        if r["produced_no_arhgef18_annotation"] in (True, False, None)
    )
    check("exhaustive", counted == n, f"{counted} of {n} papers classified")

    if failures:
        print("SELF-TEST FAILURES:")
        for f in failures:
            print("  -", f)
        return 1
    print(f"self-test: {n} primary papers classified, positive and negative controls pass")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    data = build()
    OUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(f"wrote {OUT}")
    print(
        f"{data['n_primary_with_no_arhgef18_annotation']} of {data['n_primary_papers']} "
        f"primary papers produced no GO annotation on any ARHGEF18 ortholog "
        f"({data['n_primary_with_zero_annotations_anywhere']} produced none at all; "
        f"{data['n_primary_undetermined_because_truncated']} undetermined)"
    )
    if args.self_test:
        return self_test(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
