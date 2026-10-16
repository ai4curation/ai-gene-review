#!/usr/bin/env python3
"""Before proposing a replacement term, check what comparable RhoGAPs actually carry.

Three of this review's `MODIFY` actions rest on a claim about GO convention rather
than about ARHGAP4:

* `GO:0007266 Rho protein signal transduction` describes the *transduction*, which
  is something a Rho GTPase does; a GAP terminates it.  If that is right, curated
  RhoGAPs should sit on `GO:0035023`/`GO:0035024` and not on `GO:0007266`.
* `GO:0007010 cytoskeleton organization` asserts that ARHGAP4 organises the
  cytoskeleton, where the cited observation is that it *inhibits* stress-fibre
  formation -- a regulation term.
* `GO:0007165 signal transduction`, mapped from the RhoGAP domain
  (`InterPro:IPR000198`), throws away the one thing the domain specifies.

Each of those is a falsifiable prediction about other genes, so it is checked
against them rather than asserted.  CLAUDE.md calls this the comparator check and
requires it before claiming a curation convention: a systematic pattern across
several well-curated family members is a convention; its absence means the
proposal is idiosyncratic and should be dropped.

The comparators are RhoGAPs with substantial experimental curation -- ARHGAP1/p50
(the structural archetype), ARHGAP35/p190A, ARHGAP17, ARHGAP21, ARHGAP24,
SRGAP2 (ARHGAP4's closest curated PANTHER relative), and DLC1/ARHGAP7.

Run:    uv run --with requests python comparator_terms.py
        uv run --with requests python comparator_terms.py --self-test
Writes: comparator_terms.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import requests

SEARCH = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

COMPARATORS = {
    "Q07960": "ARHGAP1/p50",
    "Q9NRY4": "ARHGAP35/p190A",
    "Q68EM7": "ARHGAP17",
    "Q5T5U3": "ARHGAP21",
    "Q8N264": "ARHGAP24/FilGAP",
    "O75044": "SRGAP2",
    "Q96QB1": "DLC1/ARHGAP7",
}
TARGET = {"P98171": "ARHGAP4"}

# term -> what carrying it would mean for the corresponding proposal
QUESTIONS = {
    "GO:0007266": "Rho protein signal transduction (the term ARHGAP4 currently has)",
    "GO:0035023": "regulation of Rho protein signal transduction (proposed)",
    "GO:0035024": "negative regulation of Rho protein signal transduction (proposed)",
    "GO:0007010": "cytoskeleton organization (the term ARHGAP4 currently has)",
    "GO:0051497": "negative regulation of stress fiber assembly (proposed)",
    "GO:0032956": "regulation of actin cytoskeleton organization (conservative alternative)",
    "GO:0007165": "signal transduction (the term ARHGAP4 currently has)",
    "GO:0005938": "cell cortex (proposed)",
    "GO:0005737": "cytoplasm (the term ARHGAP4 currently has)",
}


def annotations(acc: str) -> list[dict[str, str]]:
    """Every GOA row for one protein.  Asked once per protein rather than once per
    (protein, term) pair, so a term that is simply absent is distinguishable from a
    query that returned nothing."""
    r = requests.get(
        SEARCH,
        params={"geneProductId": f"UniProtKB:{acc}", "limit": 100},
        headers={"Accept": "application/json"},
        timeout=120,
    )
    r.raise_for_status()
    d = r.json()
    rows = d.get("results") or []
    hits = d.get("numberOfHits")
    if hits is not None and hits > len(rows):
        raise RuntimeError(
            f"{acc}: {hits} annotations but only {len(rows)} returned; "
            "an absence read off this page would be a page artefact"
        )
    return [
        {"go_id": x["goId"], "evidence": x.get("goEvidence"), "qualifier": x.get("qualifier")}
        for x in rows
    ]


def run() -> dict[str, object]:
    all_rows = {acc: annotations(acc) for acc in {**COMPARATORS, **TARGET}}

    table: dict[str, dict[str, object]] = {}
    for term in QUESTIONS:
        carriers = {}
        for acc, sym in COMPARATORS.items():
            hits = [r for r in all_rows[acc] if r["go_id"] == term]
            if hits:
                carriers[sym] = sorted({r["evidence"] for r in hits})
        target_hits = [r for r in all_rows["P98171"] if r["go_id"] == term]
        table[term] = {
            "question": QUESTIONS[term],
            "n_comparators_carrying": len(carriers),
            "n_comparators": len(COMPARATORS),
            "carriers": carriers,
            "on_target": sorted({r["evidence"] for r in target_hits}),
        }

    def verdict(current: str, proposed: str) -> dict[str, object]:
        cur, prop = table[current], table[proposed]
        return {
            "current_term": current,
            "proposed_term": proposed,
            "comparators_on_current": cur["n_comparators_carrying"],
            "comparators_on_proposed": prop["n_comparators_carrying"],
            # A proposal is supported when the family's curated practice favours
            # the proposed term over the current one.
            "convention_supports_proposal": prop["n_comparators_carrying"]
            > cur["n_comparators_carrying"],
        }

    return {
        "comparators": COMPARATORS,
        "per_term": table,
        "proposals": [
            verdict("GO:0007266", "GO:0035023"),
            verdict("GO:0007266", "GO:0035024"),
            verdict("GO:0007010", "GO:0051497"),
            verdict("GO:0007010", "GO:0032956"),
            verdict("GO:0007165", "GO:0035023"),
            verdict("GO:0005737", "GO:0005938"),
        ],
    }


def self_test() -> int:
    checks: list[tuple[str, str]] = []

    # 1. The query must return a substantial annotation set for a well-curated
    #    comparator -- otherwise every 'absent' below is a broken query.
    rows = annotations("Q07960")
    checks.append(
        (
            "positive control: ARHGAP1 returns many annotations",
            "PASS" if len(rows) >= 20 else f"FAIL {len(rows)}",
        )
    )
    # 2. A term ARHGAP1 certainly has must be found.
    checks.append(
        (
            "positive control: ARHGAP1 carries GO:0005096",
            "PASS" if any(r["go_id"] == "GO:0005096" for r in rows) else "FAIL",
        )
    )
    # 3. NEGATIVE CONTROL: a term it certainly lacks must read absent.
    checks.append(
        (
            "negative control: ARHGAP1 does not carry GO:0003735 (structural constituent of ribosome)",
            "PASS" if not any(r["go_id"] == "GO:0003735" for r in rows) else "FAIL",
        )
    )
    # 4. Pagination must abort rather than silently truncate, because a clipped
    #    page turns a present term into an absent one.
    try:
        annotations("P04637")  # TP53: far more than 100 annotations
        checks.append(("pagination aborts rather than truncating", "FAIL (no exception)"))
    except RuntimeError as e:
        checks.append(
            (
                "pagination aborts rather than truncating",
                "PASS" if "page artefact" in str(e) else f"FAIL wrong error: {e}",
            )
        )

    for name, verdict_ in checks:
        print(
            f"  [{verdict_.split()[0]}] {name}"
            + ("" if verdict_.startswith("PASS") else f" -- {verdict_}")
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
    dest = Path(__file__).with_name("comparator_terms.json")
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print(f"{'term':<12} {'n/7':>4}  carriers")
    for term, v in out["per_term"].items():
        car = ", ".join(f"{s}({'/'.join(e)})" for s, e in v["carriers"].items()) or "-"
        on_t = "/".join(v["on_target"]) or "-"
        print(f"{term:<12} {v['n_comparators_carrying']:>4}  {car}")
        print(f"{'':<12} {'':>4}  ARHGAP4: {on_t}   [{v['question']}]")
    print()
    for p in out["proposals"]:
        print(
            f"  {p['current_term']} ({p['comparators_on_current']}/7) -> "
            f"{p['proposed_term']} ({p['comparators_on_proposed']}/7): "
            f"convention supports proposal = {p['convention_supports_proposal']}"
        )
    print(f"\nwrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
