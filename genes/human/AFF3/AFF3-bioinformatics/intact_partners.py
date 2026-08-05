#!/usr/bin/env python3
"""Derive AFF3's IntAct partner set, and count publications and methods PER PARTNER.

Written because the hand-counted version of this table was WRONG: "5 records across 4
publications and 4 methods with MI 0.73" for CDK9 is actually 6 records across
5 publications and 3 methods, with MI scores of
0.35 and 0.73 (the lower one is an isoform-2 pairing).
Per the campaign rule, anything computable is computed and then compared against what was
written -- and note that this docstring itself said "5 records" for a whole round after the
prose had been fixed, which is why low-salience surfaces need the same sweep as prose.

Asserts, so a predicate that never fires cannot leave a plausible-looking count:
  - the subject is NOT in its own partner set (a common symptom of a broken id test);
  - `numberOfHits`-equivalent: every record IntAct reports is retrieved;
  - at least one partner is found (a silent zero is not a pass).

Note IntAct ids carry a " (uniprotkb)" suffix, so the subject test is on the accession
extracted from the id, not an `endswith`.

Usage:
    uv run python genes/human/AFF3/AFF3-bioinformatics/intact_partners.py
"""

from __future__ import annotations

import json
import re
import urllib.request
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUBJECT = "P51826"
URL = ("https://www.ebi.ac.uk/intact/ws/interaction/findInteractions/"
       f"{SUBJECT}?page=0&pageSize=200")
UA = {"User-Agent": "ai-gene-review/AFF3 (cjmungall@lbl.gov)"}


def acc(intact_id: str | None) -> str:
    """P50750-2 (uniprotkb) -> P50750. Strips the suffix and the isoform tag."""
    if not intact_id:
        return ""
    base = re.sub(r"\s*\(.*\)$", "", intact_id).strip()
    return base.split("-")[0]


def main() -> None:
    req = urllib.request.Request(URL, headers=UA)
    with urllib.request.urlopen(req, timeout=90) as fh:
        data = json.load(fh)
    records = data.get("content") or []
    total = data.get("totalElements")
    if total is not None and total != len(records):
        raise SystemExit(
            f"FATAL: IntAct reports {total} elements but {len(records)} retrieved -- "
            f"paginate rather than reading one page as the whole."
        )

    per_partner: dict[str, dict] = defaultdict(
        lambda: {"records": 0, "pmids": set(), "methods": set(), "scores": set(),
                 "names": set(), "isoforms": set()}
    )
    for r in records:
        a, b = acc(r.get("idA")), acc(r.get("idB"))
        if a == SUBJECT:
            pacc, pname, praw = b, r.get("moleculeB"), r.get("idB")
        elif b == SUBJECT:
            pacc, pname, praw = a, r.get("moleculeA"), r.get("idA")
        else:
            raise SystemExit(
                f"FATAL: neither side of a record is the subject: {r.get('idA')} / "
                f"{r.get('idB')} -- the accession test did not fire."
            )
        e = per_partner[pacc]
        e["records"] += 1
        e["pmids"].add(r.get("publicationPubmedIdentifier"))
        e["methods"].add(r.get("detectionMethod"))
        e["scores"].add(r.get("intactMiscore"))
        e["names"].add(pname)
        e["isoforms"].add(praw)

    if SUBJECT in per_partner:
        raise SystemExit("FATAL: the subject is in its own partner set")
    if not per_partner:
        raise SystemExit("FATAL: zero partners found -- a silent zero is not a pass")

    print(f"AFF3 ({SUBJECT}) IntAct: {len(records)} records, "
          f"{len(per_partner)} distinct partners\n")
    print(f"{'partner':<12} {'name':<10} {'recs':>4} {'pubs':>4} {'methods':>7}  "
          f"MI scores / method names / PMIDs")
    rows = sorted(per_partner.items(), key=lambda kv: (-kv[1]["records"], kv[0]))
    for pacc, e in rows:
        name = sorted(n for n in e["names"] if n)[0] if any(e["names"]) else "?"
        print(f"{pacc:<12} {name:<10} {e['records']:>4} {len(e['pmids']):>4} "
              f"{len(e['methods']):>7}  MI={sorted(e['scores'])} "
              f"methods={sorted(m for m in e['methods'] if m)} "
              f"PMIDs={sorted(p for p in e['pmids'] if p)}")

    out = {
        "subject": SUBJECT,
        "n_records": len(records),
        "n_partners": len(per_partner),
        "partners": {
            p: {
                "records": e["records"],
                "n_publications": len(e["pmids"]),
                "n_methods": len(e["methods"]),
                "pmids": sorted(x for x in e["pmids"] if x),
                "methods": sorted(x for x in e["methods"] if x),
                "mi_scores": sorted(x for x in e["scores"] if x is not None),
                "names": sorted(x for x in e["names"] if x),
                "intact_ids": sorted(x for x in e["isoforms"] if x),
            }
            for p, e in rows
        },
    }
    dest = HERE / "intact_partners.json"
    dest.write_text(json.dumps(out, indent=2))
    print(f"\nwrote {dest}")


if __name__ == "__main__":
    main()
