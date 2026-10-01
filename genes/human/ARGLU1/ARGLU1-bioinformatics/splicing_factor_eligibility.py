#!/usr/bin/env python3
"""Which of ARGLU1's four IPI partners qualify for GO:1990935 splicing factor binding?

`GO:1990935 splicing factor binding` is defined as "Binding to a protein involved
in the process of removing sections of the primary RNA transcript to form the
mature form of the RNA." Whether it applies to a given interaction row therefore
depends on the *partner*, and specifically on whether the partner is itself
involved in splicing -- which is a checkable fact about GOA, not a judgement about
the partner's reputation.

This script asks GOA directly, per partner, for annotations to `GO:0008380`
RNA splicing and its descendants, and reports the evidence codes.

Why it exists: an earlier draft of this review asserted that no
splicing-factor-binding molecular function term existed at all, and removed six
`GO:0005515` rows on that basis. The assertion was false. It came from searching
for "spliceosomal complex binding" -- and GO's search is token-based, so
*spliceosomal complex* can never retrieve *splicing factor*, however the query is
phrased. The term was found by walking the ontology instead. This script is the
follow-up that decides, per partner, whether the recovered term actually applies.

Run:  uv run python splicing_factor_eligibility.py
"""

from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"

# GO experimental evidence codes, including the high-throughput set.
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
                "HTP", "HDA", "HMP", "HGI", "HEP"}

RNA_SPLICING = "GO:0008380"

# A descendant query over is_a/part_of CANNOT reach regulation terms: GO relates
# a regulation term to its target by `regulates`, which is not in that closure. An
# earlier version of this script asked only about GO:0008380 and reported "zero
# annotations anywhere under RNA splicing" for JMJD6 -- true of the query, false as
# stated, and JMJD6 in fact holds GO:0048024 by IMP. These roots are queried too so
# the regulation branch is visible.
REGULATION_ROOTS = [
    "GO:0043484",  # regulation of RNA splicing
    "GO:0048024",  # regulation of mRNA splicing, via spliceosome
    "GO:0000381",  # regulation of alternative mRNA splicing, via spliceosome
]

PARTNERS = {
    "P26368": "U2AF2",
    "Q9UHX1": "PUF60",
    "Q6NYC1": "JMJD6",
    "P78362": "SRPK2",
}


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                return json.load(fh)
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503) and attempt < 3:
                time.sleep(2 ** attempt)
                continue
            raise
    raise RuntimeError(f"unreachable: {url}")


def annotations(accession: str, root: str = RNA_SPLICING) -> list[dict]:
    rows: list[dict] = []
    page = 1
    total: int | None = None
    while True:
        qs = urllib.parse.urlencode({
            "geneProductId": f"UniProtKB:{accession}",
            "goId": root,
            "goUsage": "descendants",
            "goUsageRelationships": "is_a,part_of",
            "limit": 100,
            "page": page,
        })
        d = _get(f"{QUICKGO}?{qs}")
        if total is None:
            total = d["numberOfHits"]
        rows.extend(d["results"])
        if not d["results"] or len(rows) >= total:
            break
        page += 1
        time.sleep(0.2)
    # Compare against the server's own total, never against the page size chosen.
    if len(rows) != total:
        raise RuntimeError(
            f"truncated fetch for {accession}: numberOfHits={total}, got {len(rows)}"
        )
    return rows


def main() -> int:
    out: dict = {"term": "GO:1990935", "criterion_term": RNA_SPLICING, "partners": {}}
    for acc, sym in PARTNERS.items():
        rows = annotations(acc)
        codes = Counter(r["goEvidence"] for r in rows)
        exp_terms = sorted({r["goId"] for r in rows if r["goEvidence"] in EXPERIMENTAL})
        all_terms = sorted({r["goId"] for r in rows})
        qualifies = bool(rows)
        # Widen: the regulation branch, which the descendant query above cannot see.
        reg: dict[str, dict] = {}
        for root in REGULATION_ROOTS:
            rrows = annotations(acc, root)
            if rrows:
                reg[root] = {
                    "annotations": len(rrows),
                    "evidence_codes": dict(Counter(r["goEvidence"] for r in rrows)),
                    "terms": sorted({r["goId"] for r in rrows}),
                    "has_experimental": any(r["goEvidence"] in EXPERIMENTAL
                                            for r in rrows),
                }
            time.sleep(0.1)

        rec = {
            "symbol": sym,
            "annotations_under_rna_splicing": len(rows),
            "evidence_codes": dict(codes),
            "terms_with_experimental_evidence": exp_terms,
            "all_terms": all_terms,
            "qualifies_as_splicing_factor": qualifies,
            "splicing_regulation_scope": reg,
            "regulates_splicing_only": (not qualifies) and bool(reg),
        }
        out["partners"][acc] = rec
        verdict = "splicing factor" if qualifies else "NOT a splicing factor"
        strength = ("experimental" if exp_terms
                    else ("inferred only" if rows else "none"))
        print(f"{sym} ({acc}): {len(rows)} annotation(s) under {RNA_SPLICING} "
              f"-> {verdict} [{strength}]")
        print(f"    evidence: {dict(codes) or '{}'}")
        if exp_terms:
            print(f"    experimental terms: {exp_terms}")
        if reg:
            for root, r in reg.items():
                print(f"    regulation branch {root}: {r['annotations']} "
                      f"{r['evidence_codes']} terms={r['terms']}")
        if rec["regulates_splicing_only"]:
            print("    -> REGULATES splicing but is not annotated TO splicing; "
                  "GO:1990935 is withheld on that distinction, which the term's "
                  "definition does not itself adjudicate")
        time.sleep(0.2)

    here = Path(__file__).resolve().parent
    (here / "splicing_factor_eligibility.json").write_text(
        json.dumps(out, indent=2, sort_keys=True)
    )
    print(f"\nwrote {here / 'splicing_factor_eligibility.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
