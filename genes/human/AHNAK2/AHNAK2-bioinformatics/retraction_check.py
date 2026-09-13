"""Retraction / erratum / expression-of-concern check for every cited PMID.

A publication-type search does NOT find Publisher Corrections. The status has to
be read from `CommentsCorrectionsList/RefType` on each *cited* article's own
record, so that is what this does, via EFetch XML.

Run: uv run python retraction_check.py
"""

from __future__ import annotations

import xml.etree.ElementTree as ET

from uniprot import _cached_get

PMIDS = [
    "17185750",  # AHNAK/dysferlin -- source of 5 AHNAK2 rows
    "24675079",  # PDB 4CN0
    "20833135",  # costamere
    "15007166",  # AHNAK2 discovery
    "21940993",  # AHNAK splicing
    "25560297",  # FGF1 export
    "31011849",  # CMT
    "35158796",  # AHNAK2 review
    "24633211",  # human PRX nucleus IDA (donor evidence)
    "10671475",  # mouse Prx nucleus EXP (donor evidence)
]
BAD = {"RetractionIn", "ErratumIn", "ExpressionOfConcernIn", "RepublishedIn",
       "CorrectedandRepublishedIn", "UpdateIn"}


def main() -> None:
    flagged = 0
    for pmid in PMIDS:
        xml = _cached_get(
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
            f"?db=pubmed&id={pmid}&retmode=xml",
            f"efetch_{pmid}", accept="application/xml",
        )
        root = ET.fromstring(xml)
        art = root.find(".//PubmedArticle")
        if art is None:
            raise SystemExit(f"PMID:{pmid} returned no PubmedArticle -- a silent "
                             "empty result must not read as 'clean'")
        ptypes = [e.text for e in art.iter("PublicationType")]
        refs = [(e.get("RefType"), (e.findtext("PMID") or "").strip())
                for e in art.iter("CommentsCorrections")]
        hits = [r for r in refs if r[0] in BAD]
        status = "CLEAN"
        if hits or any(p and ("Retract" in p or "Erratum" in p) for p in ptypes):
            status = "FLAGGED"
            flagged += 1
        print(f"PMID:{pmid}  {status}")
        if refs:
            print(f"    CommentsCorrections: {refs}")
        if status == "FLAGGED":
            print(f"    publication types: {ptypes}")
    print()
    print(f"{len(PMIDS)} PMIDs checked, {flagged} flagged.")


if __name__ == "__main__":
    main()
