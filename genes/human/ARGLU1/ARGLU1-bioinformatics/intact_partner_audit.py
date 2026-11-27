#!/usr/bin/env python3
"""Audit ARGLU1's IntAct interaction record and the four GOA IPI partners.

Three checks that earlier genes in this campaign showed are worth running even
when they come back negative:

1. **Is ``NbExp`` really N independent experiments?**  A single screen can be
   logged under several sub-method terms (``two hybrid array`` +
   ``two hybrid pooling`` + ``validated two hybrid``), so UniProt's ``NbExp``
   overcounts. Expand the records and count distinct *publications* and distinct
   *detection methods*, not ``NbExp``.
2. **Is each named partner the canonical protein?**  A partner listed by symbol
   can resolve to an unreviewed partial ORFeome clone rather than the canonical
   Swiss-Prot entry. Compare accession, reviewed status and length.
3. **Is the subject a hub, or are the partners hubs?**  Promiscuity on the
   partner side plus topological inaccessibility is the strong form of the
   screen-noise argument.

Run:  uv run python intact_partner_audit.py
"""

from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

INTACT = "https://www.ebi.ac.uk/intact/ws/interaction/findInteractions"
UNIPROT = "https://rest.uniprot.org/uniprotkb/search"

SUBJECT = "Q9NWB6"  # human ARGLU1

# The partners GOA cites in the WITH/FROM column of ARGLU1's GO:0005515 rows.
PARTNERS = {
    "P78362": "SRPK2",
    "P26368": "U2AF2",
    "Q9UHX1": "PUF60",
    "Q6NYC1": "JMJD6",
}


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=90) as fh:
                return json.load(fh)
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503) and attempt < 3:
                time.sleep(2 ** attempt)
                continue
            raise
    raise RuntimeError(f"unreachable: {url}")


def intact_all(accession: str, page_size: int = 200) -> list[dict]:
    """Fetch every IntAct binary interaction row for an accession.

    The loop terminates on the server's own reported total, and asserts the
    accumulated row count matches it, so a clamped page size cannot silently
    truncate the result.
    """
    rows: list[dict] = []
    page = 0
    total: int | None = None
    while True:
        qs = urllib.parse.urlencode({"page": page, "pageSize": page_size})
        d = _get(f"{INTACT}/{accession}?{qs}")
        content = d.get("content") or []
        if total is None:
            total = d.get("totalElements")
            if total is None:
                raise RuntimeError(
                    f"IntAct returned no totalElements for {accession}; "
                    "cannot bound the fetch, refusing to guess."
                )
        rows.extend(content)
        if not content or len(rows) >= total:
            break
        page += 1
        if page > 500:
            raise RuntimeError("pagination runaway")
        time.sleep(0.2)
    if len(rows) != total:
        raise RuntimeError(
            f"truncated IntAct fetch for {accession}: totalElements={total}, got {len(rows)}"
        )
    return rows


def base_acc(token: str) -> str:
    """'Q9NWB6-3 (uniprotkb)' -> 'Q9NWB6'  (isoform suffix stripped)."""
    tok = token.split(" ")[0]
    return tok.split("-")[0]


def partner_of(row: dict, subject: str) -> str | None:
    a, b = base_acc(row.get("uniqueIdA", "")), base_acc(row.get("uniqueIdB", ""))
    if a == subject and b != subject:
        return b
    if b == subject and a != subject:
        return a
    if a == subject and b == subject:
        return subject  # self-interaction
    return None


def uniprot_entries(accessions: list[str]) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for acc in accessions:
        qs = urllib.parse.urlencode({
            "query": f"accession:{acc}",
            "fields": "accession,id,protein_name,gene_names,length,reviewed,cc_subcellular_location",
            "format": "json", "size": 5,
        })
        res = _get(f"{UNIPROT}?{qs}").get("results", [])
        if len(res) != 1:
            raise RuntimeError(
                f"{acc}: expected 1 UniProt hit, got {len(res)} -- an ambiguous or dead "
                "accession must be reported, not silently resolved."
            )
        r = res[0]
        entry_type = r.get("entryType", "")
        locs = []
        for c in r.get("comments", []):
            if c.get("commentType") == "SUBCELLULAR LOCATION":
                for sl in c.get("subcellularLocations", []):
                    v = (sl.get("location") or {}).get("value")
                    if v:
                        locs.append(v)
        out[acc] = {
            "accession": r["primaryAccession"],
            "entry_name": r.get("uniProtkbId"),
            # "reviewed" is a substring of "unreviewed": anchor the test.
            "reviewed": entry_type.startswith("UniProtKB reviewed"),
            "entry_type": entry_type,
            "length": r.get("sequence", {}).get("length"),
            "genes": [g.get("geneName", {}).get("value") for g in r.get("genes", [])],
            "subcellular_locations": sorted(set(locs)),
        }
        time.sleep(0.1)
    return out


def main() -> int:
    rows = intact_all(SUBJECT)
    partners: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        p = partner_of(r, SUBJECT)
        if p:
            partners[p].append(r)

    report: dict = {
        "subject": SUBJECT,
        "intact_binary_rows": len(rows),
        "distinct_partners": len(partners),
        "focus_partners": {},
    }

    print(f"ARGLU1 ({SUBJECT}): {len(rows)} IntAct binary rows, "
          f"{len(partners)} distinct partner accessions")

    details = uniprot_entries(sorted(PARTNERS))
    for acc, symbol in PARTNERS.items():
        rs = partners.get(acc, [])
        pubs: Counter = Counter()
        pubmed: set[str] = set()
        methods: Counter = Counter()
        for r in rs:
            for pid in (r.get("publicationIdentifiers") or []):
                pubs[pid] += 1
                # IntAct lists several identifier FORMS for one study (pubmed id,
                # doi, MINT ac, IntAct ac). Counting raw identifiers would report
                # 10 "publications" for 3 studies -- count PubMed ids separately.
                if pid.endswith("(pubmed)"):
                    pubmed.add(pid.split(" ")[0])
            m = r.get("detectionMethod")
            if m:
                methods[m] += 1
        d = details[acc]
        # Partner promiscuity: how many partners does the partner itself have?
        p_rows = intact_all(acc)
        p_partners = {partner_of(x, acc) for x in p_rows}
        p_partners.discard(None)

        rec = {
            "symbol": symbol,
            "uniprot": d,
            "intact_rows_with_arglu1": len(rs),
            "all_publication_identifier_forms": sorted(pubs),
            "n_publication_identifier_forms": len(pubs),
            "distinct_pubmed_studies": sorted(pubmed),
            "n_distinct_pubmed_studies": len(pubmed),
            "detection_methods": dict(methods),
            "n_distinct_detection_methods": len(methods),
            "partner_total_intact_partners": len(p_partners),
        }
        report["focus_partners"][acc] = rec

        status = "Swiss-Prot" if d["reviewed"] else "TrEMBL"
        print(f"\n  {symbol} ({acc}, {d['entry_name']}, {status}, {d['length']} aa)")
        print(f"    locations: {d['subcellular_locations']}")
        print(f"    IntAct rows with ARGLU1: {len(rs)}")
        print(f"    distinct PubMed studies: {len(pubmed)} -> {sorted(pubmed)}")
        print(f"    (raw identifier forms, incl. doi/MINT/IntAct acs: {len(pubs)})")
        print(f"    distinct detection methods: {len(methods)} -> {dict(methods)}")
        print(f"    partner's own total IntAct partners: {len(p_partners)}")
        time.sleep(0.2)

    here = Path(__file__).resolve().parent
    (here / "intact_partners.json").write_text(json.dumps(report, indent=2, sort_keys=True))
    print(f"\nwrote {here / 'intact_partners.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
