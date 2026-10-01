#!/usr/bin/env python3
"""Characterise ARHGAP21's IntAct evidence per partner: how many DISTINCT
experiments, by which methods, and over which construct.

Three questions the GOA `GO:0005515` rows cannot answer on their own:

1. **Is a replicate count real replication?**  UniProt's `NbExp` counts
   IntAct sub-methods, and one screen is routinely logged as several
   (`two hybrid array` + `two hybrid pooling` + `validated two hybrid`).
   Count distinct publications and distinct detection methods separately.

2. **Which fragment was assayed?**  ARHGAP21 is 1958 aa with a PDZ (50-159),
   a PH (931-1040) and a Rho-GAP (1147-1339).  `PMID:36115835` is a
   PDZ-domain/PDZ-binding-motif affinity survey whose full text never names
   ARHGAP21, so the claim "these rows measure the PDZ domain" has to be
   checked against the recorded participant ranges rather than assumed.

3. **Is the partner set a hub artefact?**  A partner with hundreds of IntAct
   partners against ARHGAP21's own count is a promiscuity signal.

Run:  uv run --with requests python intact_methods.py
Writes: intact_methods.json
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

import requests

WS = "https://www.ebi.ac.uk/intact/ws/interaction/findInteractions"
SUBJECT = "Q5T5U3"
PAGE_SIZE = 200

# Partners that appear as IPI rows in ARHGAP21's GOA file.
GOA_PARTNERS = {
    "O15169": "AXIN1",
    "P03126": "E6 (HPV16)",
    "P06463": "E6 (HPV18)",
    "P13569": "CFTR",
    "P25054": "APC",
    "P29692": "EEF1D",
    "P31947": "SFN",
    "P35222": "CTNNB1",
    "P60484": "PTEN",
    "P63104": "YWHAZ",
    "P84078": "Arf1 (mouse)",
    "Q15418": "RPS6KA1",
    "Q5SSQ6": "SAPCD1",
    "Q92614": "MYO18A",
}

# UniProt FT DOMAIN boundaries, used to say which module a construct covers.
DOMAINS = [("PDZ", 50, 159), ("PH", 931, 1040), ("RhoGAP", 1147, 1339)]


def fetch_all() -> list[dict[str, object]]:
    """Page through every interaction. Compare against totalElements, never a
    page-size constant: if the service clamps rather than erroring, a guard
    keyed on the constant passes while rows were silently dropped."""
    rows: list[dict[str, object]] = []
    page = 0
    total: int | None = None
    while True:
        resp = requests.get(
            WS + f"/{SUBJECT}",
            params={"page": page, "pageSize": PAGE_SIZE},
            headers={"Accept": "application/json"},
            timeout=180,
        )
        resp.raise_for_status()
        d = resp.json()
        if total is None:
            total = d.get("totalElements")
        content = d.get("content") or []
        if not content:
            break
        rows.extend(content)
        page += 1
        if total is not None and len(rows) >= total:
            break
    assert total is not None, "IntAct did not report totalElements"
    assert len(rows) == total, f"paged {len(rows)} rows but totalElements={total}"
    return rows


def acc_of(raw: object) -> str | None:
    """IntAct ids arrive as 'Q5T5U3-1 (uniprotkb)' -- accession FIRST, then the
    database in parentheses.  Assuming the commoner 'db:ACC' shape yields a
    parse that matches nothing, which surfaces as every partner being ABSENT:
    a silent zero that reads as a finding.  Hence the caller asserts that a
    non-trivial fraction of rows parsed."""
    if not isinstance(raw, str):
        return None
    token = raw.split("(", 1)[0].strip()
    if not token:
        return None
    return token.split("-", 1)[0]


def covered_domains(ranges: object) -> list[str]:
    """Map an IntAct participant feature range onto ARHGAP21's domains."""
    if not isinstance(ranges, list):
        return []
    hits: set[str] = set()
    for r in ranges:
        text = r if isinstance(r, str) else json.dumps(r)
        for token in str(text).replace("-", " ").replace("..", " ").split():
            if not token.isdigit():
                continue
            pos = int(token)
            for name, start, end in DOMAINS:
                if start <= pos <= end:
                    hits.add(name)
    return sorted(hits)


def main() -> int:
    rows = fetch_all()

    per_partner: dict[str, dict[str, object]] = defaultdict(
        lambda: {
            "publications": set(),
            "methods": set(),
            "interaction_types": set(),
            "subject_ranges": set(),
            "domains": set(),
            "n_rows": 0,
        }
    )

    matched_rows = 0
    for r in rows:
        a, b = acc_of(r.get("idA")), acc_of(r.get("idB"))
        if a is None or b is None:
            continue
        if a == SUBJECT and b == SUBJECT:
            continue
        if a == SUBJECT:
            partner, subj_ranges = b, r.get("featureRangesA")
        elif b == SUBJECT:
            partner, subj_ranges = a, r.get("featureRangesB")
        else:
            continue
        matched_rows += 1

        rec = per_partner[partner]
        rec["n_rows"] = int(rec["n_rows"]) + 1
        pmid = r.get("publicationPubmedIdentifier")
        if pmid:
            rec["publications"].add(str(pmid))
        if r.get("detectionMethod"):
            rec["methods"].add(str(r["detectionMethod"]))
        if r.get("type"):
            rec["interaction_types"].add(str(r["type"]))
        for d in covered_domains(subj_ranges):
            rec["domains"].add(d)
        if isinstance(subj_ranges, list):
            for rng in subj_ranges:
                rec["subject_ranges"].add(str(rng))

    out_partners: dict[str, object] = {}
    for acc, rec in per_partner.items():
        out_partners[acc] = {
            "label": GOA_PARTNERS.get(acc),
            "in_goa": acc in GOA_PARTNERS,
            "n_intact_rows": rec["n_rows"],
            "n_distinct_publications": len(rec["publications"]),
            "publications": sorted(rec["publications"]),
            "n_distinct_methods": len(rec["methods"]),
            "methods": sorted(rec["methods"]),
            "interaction_types": sorted(rec["interaction_types"]),
            "subject_domains_in_construct": sorted(rec["domains"]),
            "subject_ranges": sorted(rec["subject_ranges"])[:8],
        }

    # A parser that matches nothing reports every partner ABSENT, which reads
    # as a finding instead of the tooling failure it is.  Relate what was found
    # to what was fetched and fail loudly when the two cannot both be true.
    assert matched_rows > 0, (
        f"parsed 0 of {len(rows)} IntAct rows as involving {SUBJECT}: "
        "the id format almost certainly changed (expected 'ACC (db)')"
    )
    assert out_partners, "no partners recovered despite matched rows"

    # Assert presence for every GOA partner: a loop that only validates what it
    # finds passes silently when a partner is absent, and "absent from IntAct"
    # is a different fact from "present with weak evidence".
    absent = sorted(a for a in GOA_PARTNERS if a not in out_partners)
    assert len(absent) < len(GOA_PARTNERS), (
        "every GOA partner is absent from IntAct -- that is a parse failure, "
        "not a result"
    )

    out = {
        "subject": SUBJECT,
        "total_intact_rows": len(rows),
        "n_distinct_partners": len(out_partners),
        "goa_partners_absent_from_intact": absent,
        "partners": out_partners,
        "goa_partner_summary": {
            acc: {
                "label": GOA_PARTNERS[acc],
                "n_distinct_publications": out_partners.get(acc, {}).get(
                    "n_distinct_publications"
                ),
                "methods": out_partners.get(acc, {}).get("methods"),
                "domains": out_partners.get(acc, {}).get(
                    "subject_domains_in_construct"
                ),
            }
            for acc in sorted(GOA_PARTNERS)
        },
    }

    dest = Path(__file__).with_name("intact_methods.json")
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print(f"IntAct rows for {SUBJECT}: {len(rows)}; distinct partners: {len(out_partners)}")
    print(f"GOA partners absent from IntAct: {absent or 'none'}")
    print()
    print(f"{'acc':<9} {'label':<14} {'rows':>4} {'pubs':>4}  domains / methods")
    for acc in sorted(GOA_PARTNERS):
        p = out_partners.get(acc)
        if p is None:
            print(f"{acc:<9} {GOA_PARTNERS[acc]:<14} {'-':>4} {'-':>4}  ABSENT")
            continue
        print(
            f"{acc:<9} {GOA_PARTNERS[acc]:<14} {p['n_intact_rows']:>4} "
            f"{p['n_distinct_publications']:>4}  "
            f"{','.join(p['subject_domains_in_construct']) or '-'} / "
            f"{'; '.join(p['methods'])[:70]}"
        )
    print(f"\nwrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
