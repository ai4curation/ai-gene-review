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
    # referenced by GOA
    "14961121",  # Tian 2004 Nature -- source of 7 AGGF1 rows
    "15905966",  # Timur 2005 review -- source of the GO:0001570 TAS row
    "16189514", "22365833", "25416956", "31515488", "32296183", "33961781",
    "39251607", "40205054",
    # relied on by this review
    "23197652",  # zebrafish aggf1 venous identity (donor of the GO:0001525 IBA)
    "24277077",  # zebrafish hemangioblast hierarchy
    "27513923",  # JNK-dependent autophagy
    "27522498",  # PI3K/AKT, VE-cadherin
    "33069768",  # FHA domain binds p53; COSMIC somatic mutations
    "34551592",  # integrin alpha5beta1 receptor; FQRDDAPAS motif
    "35202649",  # integrin alpha7 on VSMCs
    "35608889",  # AGGF1-coated paraspeckles; NEAT1 RNA-IP
    "36696895",  # TWEAK/Fn14 in muscle atrophy
    "37081014",  # ITGA7-LAP-TGF-beta1
    "39905000",  # HIF-1alpha; TNFSF12-FN14
    "40035560",  # general splicing factor; SRSF6 exon 3
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
