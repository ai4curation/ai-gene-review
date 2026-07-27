"""Expand AGFG1's IntAct interaction records and count DISTINCT EXPERIMENTS, not
`NbExp`.

`NbExp` has been shown three different ways to be a bad evidence-strength proxy:
it can count sub-methods of a single screen, replicates within one study, or even
domains of one protein. So this script prints, per partner, the detection
methods, publications and MI scores, and reports the number of distinct
publications alongside the number of records.

It also runs the promiscuity check: a partner with hundreds of IntAct partners
against a subject with a few dozen is a hub, and a singleton hit on a hub from
one screen is weak.

Usage: uv run python intact.py
"""

from __future__ import annotations

import json
import pathlib
import urllib.parse
import urllib.request
from collections import defaultdict

SUBJECT = "P52594"
OUT = pathlib.Path(__file__).parent / "intact.json"
# Partners whose GOA GO:0005515 rows are being adjudicated.
FOCUS = {"P51809": "VAMP7", "P56282": "POLE2", "Q9P242": "NYAP2", "Q9H4D5": "NXF3"}


def psicquic(acc: str) -> list[list[str]]:
    """MITAB27 rows from IntAct's PSICQUIC endpoint."""
    url = (
        "https://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/"
        f"current/search/interactor/{urllib.parse.quote(acc)}?format=tab27"
    )
    req = urllib.request.Request(url, headers={"Accept": "text/plain"})
    with urllib.request.urlopen(req) as fh:
        assert fh.status == 200, f"HTTP {fh.status} for {url}"
        text = fh.read().decode("utf-8", "replace")
    rows = [ln.split("\t") for ln in text.splitlines() if ln.strip()]
    return rows


def uniprot_ids(field: str) -> set[str]:
    """Extract bare UniProt accessions. IntAct ids carry a '(uniprotkb)' style
    decoration, so an unanchored endswith() test silently never fires."""
    out = set()
    for tok in field.split("|"):
        tok = tok.strip()
        if tok.startswith("uniprotkb:"):
            acc = tok.split(":", 1)[1].split("-")[0]
            out.add(acc)
    return out


def main() -> None:
    rows = psicquic(SUBJECT)
    print(f"IntAct returned {len(rows)} MITAB rows for {SUBJECT}")
    assert rows, "no rows - a rejected query and an empty result look identical"

    per_partner = defaultdict(list)
    for r in rows:
        ids = uniprot_ids(r[0]) | uniprot_ids(r[1])
        partners = ids - {SUBJECT}
        # Self-inclusion is the classic symptom of a predicate that never fired.
        assert SUBJECT in ids, f"subject absent from its own interaction row: {r[:2]}"
        for p in partners or {"(self/no-partner)"}:
            per_partner[p].append(
                {
                    "method": r[6],
                    "publication": r[8],
                    "type": r[11],
                    "score": r[14],
                }
            )

    print(f"{len(per_partner)} distinct partners\n")
    focus_out = {}
    for acc, sym in FOCUS.items():
        recs = per_partner.get(acc, [])
        pubs = sorted({x["publication"] for x in recs})
        methods = sorted({x["method"] for x in recs})
        focus_out[acc] = {
            "symbol": sym,
            "n_records": len(recs),
            "n_distinct_publications": len(pubs),
            "publications": pubs,
            "methods": methods,
            "scores": sorted({x["score"] for x in recs}),
        }
        print(f"{sym} ({acc}): {len(recs)} records, {len(pubs)} distinct publication(s)")
        for p in pubs:
            print(f"    pub: {p}")
        for m in methods:
            print(f"    method: {m}")
        print(f"    scores: {focus_out[acc]['scores']}")

    # Promiscuity: how many partners does each focus protein itself have?
    print("\npromiscuity (distinct IntAct partners of each protein):")
    prom = {SUBJECT: len(per_partner)}
    for acc, sym in FOCUS.items():
        r2 = psicquic(acc)
        parts = set()
        for r in r2:
            parts |= uniprot_ids(r[0]) | uniprot_ids(r[1])
        parts.discard(acc)
        prom[acc] = len(parts)
        print(f"  {sym} ({acc}): {len(parts)}")
    print(f"  AGFG1 ({SUBJECT}): {len(per_partner)}")

    OUT.write_text(
        json.dumps(
            {
                "subject_partner_count": len(per_partner),
                "focus": focus_out,
                "promiscuity": prom,
                "all_partners": sorted(per_partner),
            },
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
