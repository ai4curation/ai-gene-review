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


def annotations(accession: str) -> list[dict]:
    rows: list[dict] = []
    page = 1
    total: int | None = None
    while True:
        qs = urllib.parse.urlencode({
            "geneProductId": f"UniProtKB:{accession}",
            "goId": RNA_SPLICING,
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
        rec = {
            "symbol": sym,
            "annotations_under_rna_splicing": len(rows),
            "evidence_codes": dict(codes),
            "terms_with_experimental_evidence": exp_terms,
            "all_terms": all_terms,
            "qualifies_as_splicing_factor": qualifies,
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
        time.sleep(0.2)

    here = Path(__file__).resolve().parent
    (here / "splicing_factor_eligibility.json").write_text(
        json.dumps(out, indent=2, sort_keys=True)
    )
    print(f"\nwrote {here / 'splicing_factor_eligibility.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
