#!/usr/bin/env python3
"""Retraction / erratum / expression-of-concern check for every PMID this review cites.

Two independent routes, because each misses cases the other catches
(campaign brief):

  1. ``PublicationType`` on the article itself -- catches a *retracted* article.
  2. ``CommentsCorrectionsList`` on the article's own record -- catches Errata and
     Publisher Corrections, which a publication-type SEARCH cannot see.

A correction can also carry a NULL PubMed id (discoverable only via Crossref), so a
clean result here is a floor, not a proof.

Usage:
    uv run python genes/human/AFF3/AFF3-bioinformatics/corrections_check.py
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
REVIEW = HERE.parent / "AFF3-ai-review.yaml"
NOTES = HERE.parent / "AFF3-notes.md"
AFFINAGE = HERE.parent / "AFF3-deep-research-affinage.md"
EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
UA = {"User-Agent": "ai-gene-review/AFF3 (cjmungall@lbl.gov)"}

FLAG_TYPES = {
    "Retracted Publication", "Retraction of Publication",
    "Expression of Concern", "Published Erratum",
}
FLAG_REFTYPES = {
    "ErratumIn", "RetractionIn", "ExpressionOfConcernIn",
    "CorrectedandRepublishedIn", "RepublishedIn",
}


def collect_pmids() -> list[str]:
    pmids: set[str] = set()
    for path in (REVIEW, NOTES, AFFINAGE):
        if path.exists():
            pmids |= set(re.findall(r"PMID:(\d+)", path.read_text()))
    if not pmids:
        raise SystemExit(
            f"FATAL: found no PMIDs in {REVIEW}, {NOTES}, {AFFINAGE}. "
            "A silent zero here would read as 'nothing to check'."
        )
    return sorted(pmids, key=int)


def efetch(pmids: list[str]) -> ET.Element:
    data = urllib.parse.urlencode({
        "db": "pubmed", "retmode": "xml", "id": ",".join(pmids),
    }).encode()
    req = urllib.request.Request(EFETCH, data=data, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as fh:
        return ET.fromstring(fh.read())


def main() -> None:
    pmids = collect_pmids()
    print(f"checking {len(pmids)} PMIDs\n")
    root = efetch(pmids)
    seen = set()
    flagged = []
    for art in root.iter("PubmedArticle"):
        pmid = art.findtext(".//MedlineCitation/PMID")
        seen.add(pmid)
        ptypes = {e.text for e in art.iter("PublicationType")}
        bad_types = sorted(ptypes & FLAG_TYPES)
        corrections = []
        for cc in art.iter("CommentsCorrections"):
            rt = cc.get("RefType")
            if rt in FLAG_REFTYPES:
                corrections.append((rt, cc.findtext("PMID"), cc.findtext("RefSource")))
        if bad_types or corrections:
            flagged.append((pmid, bad_types, corrections))
            print(f"!! PMID:{pmid}")
            for t in bad_types:
                print(f"     publication type: {t}")
            for rt, cpmid, src in corrections:
                print(f"     {rt}: PMID={cpmid}  {src}")
    missing = set(pmids) - seen
    if missing:
        raise SystemExit(f"FATAL: PubMed returned no record for {sorted(missing)}")
    if not flagged:
        print("no retraction / erratum / expression-of-concern flags found")
    print(f"\n{len(flagged)} of {len(pmids)} PMIDs carry a correction-type flag")
    (HERE / "corrections.json").write_text(json.dumps(
        {"n_pmids": len(pmids), "pmids": pmids,
         "flagged": [{"pmid": p, "publication_types": t,
                      "corrections": [{"ref_type": a, "pmid": b, "source": c}
                                      for a, b, c in c_]}
                     for p, t, c_ in flagged]}, indent=2))
    print(f"wrote {HERE / 'corrections.json'}")


if __name__ == "__main__":
    main()
