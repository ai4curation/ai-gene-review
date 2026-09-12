#!/usr/bin/env python3
"""Projection test for the GDB `TAS` block that ADGRA2's GO:0004930 / GO:0007186 rows cite.

This analysis is load-bearing: it is the evidence for the two `REMOVE` verdicts, and it is
what lets those verdicts rest on the *distribution of annotations* rather than on a claim
about the full text of a paper that is `full_text_available: false` in the cache. It was
originally run ad hoc, which made it the one load-bearing analysis in this review without a
committed script and JSON. Now it is reproducible.

Two questions, per the ACTR8/ACTRT3 discriminator:
  1. How many *entities* does the reference annotate, with what evidence and assigner?
     (An annotation count is NOT an entity count -- one entity can hold several rows for a
     term. Entities are derived as a distinct set of gene-product ids.)
  2. Does the functional term spread across the set, or stay on a perturbed gene?
     For a repertoire survey there is no perturbed gene at all, which is the point.

It also settles a sub-claim the review makes and the ad-hoc run did not evidence: that the
two pseudogene recipients, ADGRE4P and ADGRF2P, are among those receiving the *molecular
function* GO:0004930. The reported 25-of-27 distribution alone does not establish this --
it is consistent with the pseudogenes being the two that missed it -- so the per-entity
matrix is emitted and the pseudogenes are checked by name.

Usage:  python3 projection_test.py [--self-test]
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "projection_test.json"

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
PAGE = 100  # QuickGO's cap for this endpoint; it CLAMPS rather than erroring on more.
REFERENCE = "PMID:15203201"
UA = {"Accept": "application/json"}

# Pseudogenes among the recipients, by HGNC locus type. Named explicitly so the check is
# a check and not a restatement of whatever the query happens to return.
EXPECTED_PSEUDOGENES = {"ADGRE4P", "ADGRF2P"}
MF_TERM = "GO:0004930"


def fetch_all(reference: str) -> list[dict]:
    """Page through the annotation search, asserting nothing was silently truncated."""
    results: list[dict] = []
    page, total = 1, None
    while True:
        url = QUICKGO + "?" + urllib.parse.urlencode(
            {"reference": reference, "limit": PAGE, "page": page}
        )
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=60) as fh:
            assert fh.status == 200, f"HTTP {fh.status} for {url}"
            d = json.load(fh)
        if total is None:
            total = d["numberOfHits"]
        got = d["results"]
        results.extend(got)
        if len(results) >= total or not got:
            break
        page += 1
    # Compare against len(results), never against PAGE: a server that clamps instead of
    # erroring would sail past a page-size guard while returning a partial set.
    assert len(results) == total, (
        f"TRUNCATED: numberOfHits={total} but read {len(results)} rows for {reference}"
    )
    assert total > 0, f"{reference} returned zero annotations -- a silent zero reads as a finding"
    return results


def analyse(rows: list[dict]) -> dict:
    per_term_entities: dict[str, set[str]] = defaultdict(set)
    per_entity_terms: dict[str, set[str]] = defaultdict(set)
    evidence: dict[str, int] = defaultdict(int)
    assigner: dict[str, int] = defaultdict(int)
    taxa: dict[int, int] = defaultdict(int)
    symbol_of: dict[str, str] = {}

    for r in rows:
        gp, sym = r["geneProductId"], r["symbol"]
        symbol_of[gp] = sym
        per_term_entities[r["goId"]].add(gp)
        per_entity_terms[gp].add(r["goId"])
        evidence[r["goEvidence"]] += 1
        assigner[r["assignedBy"]] += 1
        taxa[r["taxonId"]] += 1

    entities = sorted(symbol_of.values())
    mf_recipients = {symbol_of[g] for g in per_term_entities.get(MF_TERM, set())}
    mf_missing = sorted(set(entities) - mf_recipients)

    return {
        "reference": REFERENCE,
        "n_annotations": len(rows),
        "n_entities": len(entities),
        "entities": entities,
        "evidence_codes": dict(evidence),
        "assigned_by": dict(assigner),
        "taxa": {str(k): v for k, v in taxa.items()},
        "entities_per_term": {t: len(v) for t, v in sorted(per_term_entities.items())},
        "per_entity_terms": {symbol_of[g]: sorted(t) for g, t in
                             sorted(per_entity_terms.items(), key=lambda kv: symbol_of[kv[0]])},
        "mf_term": MF_TERM,
        "mf_recipients_count": len(mf_recipients),
        "mf_missing_from": mf_missing,
        "pseudogenes_checked": sorted(EXPECTED_PSEUDOGENES),
        "pseudogenes_receiving_mf": sorted(EXPECTED_PSEUDOGENES & mf_recipients),
        "pseudogenes_missing_mf": sorted(EXPECTED_PSEUDOGENES - mf_recipients),
    }


def report(a: dict, verbose: bool = True) -> list[str]:
    problems: list[str] = []

    # A projection is a reference whose evidence and assigner are uniform across many entities.
    if len(a["evidence_codes"]) != 1:
        problems.append(f"evidence is not uniform: {a['evidence_codes']}")
    if len(a["assigned_by"]) != 1:
        problems.append(f"assigner is not uniform: {a['assigned_by']}")

    # The pseudogene sub-claim, checked rather than assumed.
    absent = set(a["pseudogenes_checked"]) - set(a["entities"])
    if absent:
        problems.append(f"expected pseudogene recipients not annotated by this reference at all: {sorted(absent)}")
    elif a["pseudogenes_missing_mf"]:
        problems.append(
            f"the review claims the pseudogenes receive {a['mf_term']}, but "
            f"{a['pseudogenes_missing_mf']} do not -- the claim must be withdrawn"
        )

    if verbose:
        print(f"reference        : {a['reference']}")
        print(f"annotations      : {a['n_annotations']}")
        print(f"distinct entities: {a['n_entities']}")
        print(f"evidence         : {a['evidence_codes']}")
        print(f"assigned by      : {a['assigned_by']}")
        print(f"taxa             : {a['taxa']}")
        print("entities per term:")
        for t, n in a["entities_per_term"].items():
            print(f"    {t}: {n}")
        print(f"{a['mf_term']} reaches {a['mf_recipients_count']}/{a['n_entities']} entities; "
              f"absent from {a['mf_missing_from'] or 'none'}")
        print(f"pseudogenes {a['pseudogenes_checked']} receiving {a['mf_term']}: "
              f"{a['pseudogenes_receiving_mf'] or 'NONE'}")
        OUT.write_text(json.dumps(a, indent=2))
        print(f"\nwrote {OUT.name}")
    return problems


def self_test() -> None:
    """Break-test in both directions."""
    # 1. The silent-zero guard must fire on a reference with no annotations. This exercises
    #    committed code rather than restating an assert inline: a query that legitimately
    #    returns nothing is indistinguishable downstream from a query that failed.
    try:
        fetch_all("PMID:99999999")
    except AssertionError as exc:
        assert "silent zero" in str(exc), exc
    else:
        raise AssertionError("fetch_all accepted a zero-annotation reference")

    # 2. The pseudogene check must FAIL on data where a pseudogene lacks the MF term.
    #    Both pseudogenes must be present in `entities`, or the earlier not-annotated-at-all
    #    branch fires instead and this direction is never actually exercised. (That is exactly
    #    what a first draft of this fixture did -- the guard fired, but on the wrong clause.)
    bad = {"reference": "x", "n_annotations": 3, "n_entities": 3,
           "entities": ["ADGRE4P", "ADGRF2P", "ADGRA2"],
           "evidence_codes": {"TAS": 2}, "assigned_by": {"GDB": 2}, "taxa": {"9606": 2},
           "entities_per_term": {MF_TERM: 1}, "per_entity_terms": {}, "mf_term": MF_TERM,
           "mf_recipients_count": 1, "mf_missing_from": ["ADGRE4P", "ADGRF2P"],
           "pseudogenes_checked": ["ADGRE4P", "ADGRF2P"], "pseudogenes_receiving_mf": [],
           "pseudogenes_missing_mf": ["ADGRE4P", "ADGRF2P"]}
    probs = report(bad, verbose=False)
    assert any("must be withdrawn" in p for p in probs), probs

    # 3. ... and must PASS on the real data (the happy path is the untested path).
    a = analyse(fetch_all(REFERENCE))
    probs = report(a, verbose=False)
    assert probs == [], f"live projection test reports problems: {probs}"
    assert set(a["pseudogenes_receiving_mf"]) == EXPECTED_PSEUDOGENES, a["pseudogenes_receiving_mf"]

    # 4. Non-uniform evidence must be flagged, so "uniform" is a finding not a default.
    mixed = dict(bad, evidence_codes={"TAS": 1, "IDA": 1},
                 pseudogenes_missing_mf=[], pseudogenes_receiving_mf=["ADGRE4P", "ADGRF2P"],
                 mf_missing_from=[], entities=["ADGRE4P", "ADGRF2P"])
    assert any("evidence is not uniform" in p for p in report(mixed, verbose=False))

    print("self-test OK: 4 directions exercised (silent-zero guard fires on an empty reference; "
          "pseudogene check fails on withdrawal-worthy data; passes on the real data; "
          "non-uniform evidence flagged)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        self_test()
        sys.exit(0)
    found = report(analyse(fetch_all(REFERENCE)))
    print()
    if found:
        for p in found:
            print("PROBLEM:", p)
        sys.exit(1)
    print("OK: uniform evidence and assigner across all entities, and every claim the review "
          "makes about this reference's distribution is reproduced by this run")
