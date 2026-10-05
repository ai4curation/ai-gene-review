#!/usr/bin/env python3
"""Check every PMID this review relies on for retraction / erratum / expression of concern.

Why this is not a publication-type search: a Publisher Correction is **not
discoverable** by querying for correction-type publications.  It has to be read
from `CommentsCorrectionsList/RefType` on each *cited* article's own record.
The ARHGAP21 review hit exactly this -- `PMID:36115835` carries an
`ErratumIn` that no pubtype query would have surfaced.

Run:  uv run --with requests python check_corrections.py
Writes: corrections.json
"""

from __future__ import annotations

import json
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import requests

EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# RefTypes that mean "something is wrong with, or appended to, this paper".
CONCERNING = {
    "RetractionIn",
    "ErratumIn",
    "ExpressionOfConcernIn",
    "CorrectedandRepublishedIn",
    "RepublishedIn",
}

# Every PMID cited anywhere in the ARHGAP21 review or notes.
PMIDS = [
    "12056806",
    "15161933",
    "15778465",
    "15793564",
    "16184169",
    "16527809",
    "17347647",
    "17510365",
    "18662671",
    "19268501",
    "19692570",
    "20195357",
    "20525016",
    "21173159",
    "22318733",
    "22922005",
    "23200924",
    "23235160",
    "25744409",
    "26496610",
    "28514442",
    "28749339",
    "29212046",
    "33961781",
    "36012204",
    "36115835",
    "36931259",
    "37712268",
    "38556137",
    "41957357",
]


def fetch_records(pmids: list[str]) -> ET.Element:
    resp = requests.post(
        EFETCH,
        data={"db": "pubmed", "id": ",".join(pmids), "retmode": "xml"},
        timeout=120,
    )
    resp.raise_for_status()
    return ET.fromstring(resp.content)


def main() -> int:
    root = fetch_records(PMIDS)
    articles = root.findall(".//PubmedArticle")

    seen: dict[str, dict[str, object]] = {}
    for art in articles:
        pmid_el = art.find(".//MedlineCitation/PMID")
        if pmid_el is None or pmid_el.text is None:
            continue
        pmid = pmid_el.text
        title_el = art.find(".//ArticleTitle")
        ptypes = [
            (p.text or "") for p in art.findall(".//PublicationTypeList/PublicationType")
        ]
        refs = []
        for cc in art.findall(".//CommentsCorrectionsList/CommentsCorrections"):
            ref_type = cc.get("RefType", "")
            ref_pmid_el = cc.find("PMID")
            refs.append(
                {
                    "ref_type": ref_type,
                    "ref_pmid": ref_pmid_el.text if ref_pmid_el is not None else None,
                }
            )
        concerning = [r for r in refs if r["ref_type"] in CONCERNING]
        retracted_pubtype = any(
            "Retracted Publication" in p or "Retraction of Publication" in p
            for p in ptypes
        )
        seen[pmid] = {
            "title": "".join(title_el.itertext()) if title_el is not None else None,
            "publication_types": ptypes,
            "comments_corrections": refs,
            "concerning": concerning,
            "retracted_by_pubtype": retracted_pubtype,
        }

    # A PMID that PubMed did not return is NOT "clean" -- it is unchecked.
    # Failing to distinguish the two is how an absence becomes a finding.
    unreturned = sorted(set(PMIDS) - set(seen))
    assert len(seen) + len(unreturned) == len(set(PMIDS)), "record accounting mismatch"

    flagged = {
        p: v
        for p, v in seen.items()
        if v["concerning"] or v["retracted_by_pubtype"]
    }

    out = {
        "n_requested": len(PMIDS),
        "n_returned": len(seen),
        "unreturned_pmids": unreturned,
        "n_flagged": len(flagged),
        "flagged": flagged,
        "clean_pmids": sorted(set(seen) - set(flagged)),
    }

    dest = Path(__file__).with_name("corrections.json")
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print(f"requested {len(PMIDS)}, returned {len(seen)}, unreturned {unreturned}")
    if not flagged:
        print("NO retraction / erratum / expression-of-concern found on any cited PMID.")
    for p, v in sorted(flagged.items()):
        print(f"\nPMID:{p}  retracted_by_pubtype={v['retracted_by_pubtype']}")
        print(f"  {v['title']}")
        for r in v["concerning"]:
            print(f"  -> {r['ref_type']}: PMID:{r['ref_pmid']}")
    print(f"\nwrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
