"""Retraction / erratum / expression-of-concern check for every PMID this review
relies on.

Two routes, because each misses cases the other catches:
  1. the article's own PubMed record - `CommentsCorrectionsList` with RefType
     ``RetractionIn`` / ``ErratumIn`` / ``ExpressionOfConcernIn`` (a Publisher
     Correction is NOT discoverable by a publication-type search);
  2. the article's PublicationTypeList, which catches records typed as
     "Retracted Publication".

A correction can carry a NULL PubMed id and be visible only via Crossref, so a
clean result here is reported as "none found by these two routes", not as
"no correction exists".

Usage: uv run python retractions.py
"""

from __future__ import annotations

import json
import pathlib
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

OUT = pathlib.Path(__file__).parent / "retractions.json"

PMIDS = [
    "7634337",
    "7637788",
    "10613896",
    "11545741",
    "11711676",
    "14701878",
    "14724135",
    "15749819",
    "16765935",
    "18775314",
    "18809720",
    "18819912",
    "22484487",
    "23433073",
    "25416956",
    "27654348",
    "31533044",
    "34369554",
    "38606629",
    "39089666",
]
FLAG_REFTYPES = {
    "RetractionIn",
    "ErratumIn",
    "ExpressionOfConcernIn",
    "CorrectedandRepublishedIn",
    "RepublishedIn",
    "RetractionOf",
}
FLAG_PUBTYPES = {
    "Retracted Publication",
    "Retraction of Publication",
    "Expression of Concern",
    "Published Erratum",
}
# Known-positive control: PMID:32125225 was cited unflagged by a provider record
# earlier in this campaign and IS retracted. If the control comes back clean the
# parser is broken and every "clean" verdict below is meaningless.
CONTROL = "32125225"


def efetch(pmids: list[str]) -> ET.Element:
    params = urllib.parse.urlencode(
        {"db": "pubmed", "id": ",".join(pmids), "retmode": "xml"}
    )
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?{params}"
    with urllib.request.urlopen(url) as fh:
        assert fh.status == 200, f"HTTP {fh.status} for {url}"
        return ET.fromstring(fh.read())


def scan(root: ET.Element) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for art in root.iter("PubmedArticle"):
        pmid_el = art.find(".//MedlineCitation/PMID")
        assert pmid_el is not None
        pmid = pmid_el.text
        flags = []
        for cc in art.iter("CommentsCorrections"):
            rt = cc.get("RefType")
            if rt in FLAG_REFTYPES:
                ref = cc.find("PMID")
                flags.append({"refType": rt, "pmid": ref.text if ref is not None else None})
        pubtypes = [pt.text for pt in art.iter("PublicationType")]
        flagged_pubtypes = sorted(set(pubtypes) & FLAG_PUBTYPES)
        out[pmid] = {
            "comments_corrections_flags": flags,
            "flagged_publication_types": flagged_pubtypes,
            "all_reftypes_seen": sorted(
                {cc.get("RefType") for cc in art.iter("CommentsCorrections")}
                - {None}
            ),
        }
    return out


def main() -> None:
    root = efetch(PMIDS + [CONTROL])
    res = scan(root)
    missing = set(PMIDS + [CONTROL]) - set(res)
    assert not missing, f"no PubMed record parsed for {sorted(missing)}"

    ctrl = res[CONTROL]
    assert ctrl["comments_corrections_flags"] or ctrl["flagged_publication_types"], (
        f"CONTROL FAILED: {CONTROL} is retracted but this parser saw nothing "
        f"({ctrl}); every clean verdict below would be meaningless"
    )
    print(
        f"positive control OK: {CONTROL} flagged "
        f"{ctrl['comments_corrections_flags']} {ctrl['flagged_publication_types']}"
    )

    dirty = []
    for p in PMIDS:
        r = res[p]
        if r["comments_corrections_flags"] or r["flagged_publication_types"]:
            dirty.append(p)
            print(f"  *** PMID:{p} {r}")
        else:
            print(f"  PMID:{p} clean (reftypes present: {r['all_reftypes_seen'] or 'none'})")
    print(
        f"\n{len(dirty)}/{len(PMIDS)} relied-on references carry a retraction, erratum "
        "or expression-of-concern flag by these two routes"
    )
    if not dirty:
        print(
            "NOTE: a correction can carry a NULL PubMed id and be visible only via "
            "Crossref, so this is 'none found by these routes', not 'none exists'."
        )
    OUT.write_text(json.dumps({"control": {CONTROL: ctrl}, "results": {p: res[p] for p in PMIDS}}, indent=2, sort_keys=True) + "\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
