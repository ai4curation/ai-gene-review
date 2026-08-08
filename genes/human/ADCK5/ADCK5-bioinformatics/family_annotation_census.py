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
        "?fields=accession,id,protein_name,keyword,cc_function,ec,cc_subcellular_location"
    )


def subcellular_evidence(entry: dict) -> list[dict]:
    """Each SUBCELLULAR LOCATION term with the evidence codes and sources behind it.

    Recorded because this review argues about *why* UniProt gives ADCK1 and ADCK2 a
    mitochondrial location and ADCK5 only a membrane one. An earlier draft asserted the three
    rested on identical evidence; they do not - ADCK1 and ADCK2 carry
    ECO:0000269|PubMed:33988507, an experimental localisation from a kinome-wide screen whose
    library did not contain ADCK5, so the asymmetry is untested-versus-tested. A cross-gene
    claim of that kind has to be checkable from the repository, not only from a live query
    someone once ran - so the evidence tags are captured here rather than described in prose.
    """
    out = []
    for c in entry.get("comments", []):
        if c["commentType"] != "SUBCELLULAR LOCATION":
            continue
        for loc in c.get("subcellularLocations", []):
            v = loc.get("location", {})
            out.append(
                {
                    "location": v.get("value"),
                    "evidence": sorted(
                        {
                            f"{e.get('evidenceCode')}"
                            + (f"|{e.get('source')}:{e.get('id')}" if e.get("source") else "")
                            for e in v.get("evidences", [])
                        }
                    ),
                }
            )
    return out


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
        # GO:0004672 protein kinase / GO:0004674 protein Ser-Thr kinase /
        # GO:0016301 kinase activity / GO:0006468 protein phosphorylation
        KINASE_TERMS = {"GO:0004672", "GO:0004674", "GO:0016301", "GO:0006468"}
        kinase_terms = sorted(
            {
                f"{r['goId']} {r['goEvidence']} {r['qualifier']}"
                for r in rows
                if r["goId"] in KINASE_TERMS
            }
        )
        # WITH the reference, so a claim about *which paper* backs a paralog's kinase row is
        # checkable. Without it the review could state "COQ8B's positive GO:0004672 row is IDA
        # from PMID:38425362" - true, and the exact shape this PR retracted three times - with
        # nothing in the census to check it against.
        kinase_rows = sorted(
            {
                (r["goId"], r["goEvidence"], str(r.get("qualifier", "")), r["reference"])
                for r in rows
                if r["goId"] in KINASE_TERMS
            }
        )

        # Every GO:0005739 row with its evidence code and reference. Recorded because this
        # review asserts on three surfaces that ADCK1 and ADCK2 carry the same MitoCoP HTP
        # row as ADCK5 - a cross-gene claim about another entry's evidence, which is the
        # shape this PR has already had to retract twice. It must be checkable from the
        # repository rather than from a live query someone once ran.
        mito_rows = sorted(
            {
                (r["goEvidence"], r["reference"])
                for r in rows
                if r["goId"] == "GO:0005739"
            }
        )

        census[sym] = {
            "accession": acc,
            "entry_name": entry_name,
            "subcellular_locations": subcellular_evidence(ent),
            "mitochondrion_go_rows": [
                {"evidence": e, "reference": ref} for e, ref in mito_rows
            ],
            "reviewed": ent["entryType"].startswith("UniProtKB reviewed"),
            "ec_numbers": ecs,
            "has_ser_thr_kinase_keyword": "Serine/threonine-protein kinase" in kws,
            "n_annotations": len(rows),
            "n_iba": len(iba),
            "iba_nodes": iba_nodes,
            "negated_annotations": negated,
            "kinase_related_terms": kinase_terms,
            "kinase_rows": [
                {"term": g, "evidence": e, "qualifier": q, "reference": ref}
                for g, e, q, ref in kinase_rows
            ],
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

    # ---- the corrected cross-gene localisation claim, asserted ----
    # ADCK1 and ADCK2 hold an EXPERIMENTAL (ECO:0000269|PubMed:33988507) mitochondrial
    # location that ADCK5 does not; ADCK5's only location is a non-experimental membrane
    # inference. The asymmetry is untested-versus-tested, not identical evidence handled
    # differently: that screen's library did not contain ADCK5. This review previously
    # asserted the opposite, so the corrected form is pinned here rather than left to prose.
    # startswith, not ==: COQ8A/COQ8B use "Mitochondrion membrane". With an exact match a
    # refinement of ADCK1's line would raise a false alarm, and - worse - a refinement of
    # ADCK5's would make BOTH staleness checks below pass silently, which is the direction
    # that matters.
    def _mito_locs(sym: str) -> list[dict]:
        return [
            loc
            for loc in census[sym]["subcellular_locations"]
            if str(loc["location"]).startswith("Mitochondrion")
        ]

    def _mito_experimental(sym: str) -> bool:
        return any(
            any(e.startswith("ECO:0000269") for e in loc["evidence"]) for loc in _mito_locs(sym)
        )

    # Partition the family by what PMID:33988507 (the kinome-wide imaging screen) actually did
    # for each gene's UniProt localisation. This review previously said the screen "supplied"
    # the localisation for all four paralogs; for COQ8A and COQ8B it is one tag among several
    # and the latest of them, so it CORROBORATED rather than supplied. The distinction is
    # computed here so the prose can be held to it instead of restating it from memory.
    SCREEN = "33988507"
    provenance: dict[str, list[str]] = {"sole": [], "corroborating": [], "absent": []}
    for sym in GENES:
        tags = sorted({e for loc in _mito_locs(sym) for e in loc["evidence"]})
        screen_tags = [e for e in tags if SCREEN in e]
        if not screen_tags:
            provenance["absent"].append(sym)
        elif len(tags) == 1:
            provenance["sole"].append(sym)
        else:
            provenance["corroborating"].append(sym)

    # Both paralogs' SL-0173 rests on PubMed:33988507, an assay ADCK5 was never in.
    for sym in ("ADCK1", "ADCK2"):
        if not _mito_experimental(sym):
            problems.append(
                f"localisation claim: {sym} no longer carries an experimental (ECO:0000269) "
                f"Mitochondrion location; the review's account of the SL-0173/SL-0162 "
                f"asymmetry rests on it"
            )
    # One check, not two: the earlier pair had the second subsuming the first.
    if _mito_locs("ADCK5"):
        problems.append(
            "localisation claim: ADCK5's SUBCELLULAR LOCATION now includes a Mitochondrion "
            "term; the UniProt correction request in suggested_questions has been actioned "
            "upstream and must be revised"
        )
    # The MitoCoP claim, asserted rather than described.
    MITOCOP = "PMID:34800366"
    carries_mitocop = sorted(
        sym
        for sym in GENES
        if any(
            r["reference"] == MITOCOP and r["evidence"] == "HTP"
            for r in census[sym]["mitochondrion_go_rows"]
        )
    )
    for sym in ("ADCK5", "ADCK1", "ADCK2"):
        if sym not in carries_mitocop:
            problems.append(
                f"MitoCoP claim: {sym} no longer carries a GO:0005739 HTP row from {MITOCOP}. "
                f"The review states on three surfaces that ADCK5, ADCK1 and ADCK2 share it."
            )

    if provenance["sole"] != ["ADCK1", "ADCK2"] or provenance["absent"] != ["ADCK5"]:
        problems.append(
            f"localisation provenance changed: screen-as-sole-evidence={provenance['sole']}, "
            f"screen-corroborating={provenance['corroborating']}, "
            f"no-screen-evidence={provenance['absent']}. The review states the screen SUPPLIED "
            f"the localisation for ADCK1/ADCK2 and CORROBORATED it for COQ8A/COQ8B, and that "
            f"ADCK5 alone has none."
        )

    OUT.write_text(
        json.dumps(
            {
                "census": census,
                "mitochondrial_localisation_provenance": provenance,
                "problems": problems,
            },
            indent=2,
        )
        + "\n"
    )

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
    print(
        f"PMID:33988507 is the SOLE cited evidence for {provenance['sole']}, "
        f"one tag among several (corroborating) for {provenance['corroborating']}, "
        f"and absent for {provenance['absent']}."
    )
    print()
    print(f"GO:0005739 HTP row from {MITOCOP} carried by: {carries_mitocop}")
    print()
    print("UniProt SUBCELLULAR LOCATION and the evidence behind it:")
    for sym in GENES:
        for loc in census[sym]["subcellular_locations"]:
            print(f"  {sym:<8}{loc['location']:<16}{','.join(loc['evidence']) or '(none)'}")
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
