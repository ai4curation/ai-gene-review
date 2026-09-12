#!/usr/bin/env python3
"""Retraction / erratum / expression-of-concern check for every PMID this review relies on.

Per GENE_BRIEF:
  * A Publisher Correction is NOT discoverable by a publication-type search; it must be
    read from CommentsCorrections/RefType on each *cited* article's own PubMed record.
  * A correction can carry a NULL PubMed id (PMID:17994018's 2008 corrigendum), so the
    DOI must also be resolved at Crossref and its relation/update-to fields inspected.

Defect this script was written with, and the guard that now prevents it:
  `.//ArticleId` matches ArticleIds inside the *ReferenceList* as well as the article's
  own PubmedData, so three of fifteen PMIDs were Crossref-checked against a DOI belonging
  to a paper they merely cited -- and reported "crossref=none", a false clean. The DOI is
  now read only from PubmedData/ArticleIdList, and cross-checked against Crossref's title.
  Run with --self-test to exercise both directions of that guard.
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

BAD_REFTYPES = {
    "RetractionIn", "ErratumIn", "ExpressionOfConcernIn",
    "RepublishedIn", "CorrectedandRepublishedIn", "UpdateIn",
}
CROSSREF_RELATIONS = ("is-corrected-by", "has-correction", "update-to")
UA = {"User-Agent": "ai-gene-review ADGRA2 review (mailto:cjmungall@lbl.gov)"}


def efetch(pmids: list[str]) -> ET.Element:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "id": ",".join(pmids), "retmode": "xml"}
    )
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA)) as fh:
        assert fh.status == 200, f"HTTP {fh.status} from efetch"
        return ET.parse(fh).getroot()


def own_doi(article: ET.Element) -> str | None:
    """The article's OWN doi.

    Anchored to PubmedData/ArticleIdList (and the Article's own ELocationID) so a DOI
    belonging to an entry in ReferenceList can never be returned.
    """
    for aid in article.findall("./PubmedData/ArticleIdList/ArticleId"):
        if aid.get("IdType") == "doi" and aid.text:
            return aid.text.strip()
    for el in article.findall("./MedlineCitation/Article/ELocationID"):
        if el.get("EIdType") == "doi" and el.text:
            return el.text.strip()
    return None


def own_comments_corrections(article: ET.Element) -> list[ET.Element]:
    return article.findall("./MedlineCitation/CommentsCorrectionsList/CommentsCorrections")


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()


def crossref(doi: str) -> dict:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as fh:
            return json.load(fh)["message"]
    except urllib.error.HTTPError as exc:
        return {"_error": f"HTTP {exc.code}"}
    except Exception as exc:
        return {"_error": str(exc)}


def check(pmids: list[str], verbose: bool = True) -> list[dict]:
    root = efetch(pmids)
    arts = root.findall(".//PubmedArticle")
    got = {a.findtext(".//PMID") for a in arts}
    missing = set(pmids) - got
    assert not missing, f"PubMed returned no record for {sorted(missing)}"

    findings = []
    for art in arts:
        pmid = art.findtext(".//PMID")
        title = (art.findtext("./MedlineCitation/Article/ArticleTitle") or "").strip()
        doi = own_doi(art)
        flags = []
        for cc in own_comments_corrections(art):
            rt = cc.get("RefType")
            if rt in BAD_REFTYPES:
                flags.append(f"{rt}->PMID:{cc.findtext('PMID') or 'NULL'}")
        pubtypes = [p.text for p in art.findall(".//PublicationType")]
        if any("Retract" in (p or "") for p in pubtypes):
            flags.append("PUBTYPE:" + ",".join(pubtypes))

        cr_flags, doi_ok = {}, None
        if doi:
            m = crossref(doi)
            if "_error" in m:
                doi_ok = f"crossref-error:{m['_error']}"
            else:
                cr_title = (m.get("title") or [""])[0]
                ratio = difflib.SequenceMatcher(None, norm(title), norm(cr_title)).ratio()
                # The guard: a DOI scraped from the reference list resolves to a DIFFERENT paper.
                doi_ok = "title-match" if ratio > 0.6 else f"DOI-TITLE-MISMATCH({ratio:.2f}) -> {cr_title[:60]!r}"
                rel = m.get("relation") or {}
                cr_flags = {k: rel[k] for k in CROSSREF_RELATIONS if k in rel}
                if m.get("update-to"):
                    cr_flags["update-to"] = m["update-to"]
            time.sleep(0.3)

        rec = {"pmid": pmid, "title": title, "doi": doi, "doi_check": doi_ok,
               "pubmed_flags": flags, "crossref_flags": cr_flags}
        findings.append(rec)
        if verbose:
            print(f"PMID:{pmid} {title[:68]}")
            print(f"   doi={doi}  [{doi_ok}]")
            print(f"   pubmed={flags or 'clean'}  crossref={cr_flags or 'clean'}")
        assert doi_ok is None or not str(doi_ok).startswith("DOI-TITLE-MISMATCH"), (
            f"PMID:{pmid} DOI {doi} does not resolve to this article ({doi_ok}) -- "
            "the DOI was probably scraped from the reference list; fix own_doi()."
        )
        time.sleep(0.3)
    return findings


def self_test() -> None:
    """Break-test the guard in BOTH directions (GENE_BRIEF: a guard can be wrong about
    success as easily as about failure)."""
    xml = """<PubmedArticleSet><PubmedArticle>
      <MedlineCitation><PMID>28600358</PMID><Article>
        <ArticleTitle>Cell adhesion controlled by adhesion G protein-coupled receptor GPR124/ADGRA2</ArticleTitle>
      </Article>
      <CommentsCorrectionsList>
        <CommentsCorrections RefType="ErratumIn"><PMID>99999999</PMID></CommentsCorrections>
      </CommentsCorrectionsList></MedlineCitation>
      <PubmedData><ArticleIdList>
        <ArticleId IdType="doi">10.1074/jbc.M117.780304</ArticleId>
      </ArticleIdList></PubmedData>
      <ReferenceList><Reference><ArticleIdList>
        <ArticleId IdType="doi">10.3791/50316</ArticleId>
      </ArticleIdList></Reference></ReferenceList>
    </PubmedArticle></PubmedArticleSet>"""
    art = ET.fromstring(xml).find(".//PubmedArticle")

    # Direction 1 (the bug): the reference-list DOI must NOT be returned.
    got = own_doi(art)
    assert got == "10.1074/jbc.M117.780304", f"own_doi picked up a reference DOI: {got}"
    assert got != "10.3791/50316"

    # Direction 2 (happy path must still work): a record whose ONLY doi is an ELocationID.
    xml2 = xml.replace(
        '<PubmedData><ArticleIdList>\n        <ArticleId IdType="doi">10.1074/jbc.M117.780304</ArticleId>\n      </ArticleIdList></PubmedData>',
        "<PubmedData><ArticleIdList/></PubmedData>",
    ).replace(
        "</ArticleTitle>",
        '</ArticleTitle><ELocationID EIdType="doi">10.1074/jbc.M117.780304</ELocationID>',
    )
    art2 = ET.fromstring(xml2).find(".//PubmedArticle")
    assert own_doi(art2) == "10.1074/jbc.M117.780304", f"ELocationID fallback broken: {own_doi(art2)}"

    # Direction 3: an article with no DOI anywhere returns None rather than raising.
    xml3 = re.sub(r'<ArticleId IdType="doi">[^<]*</ArticleId>', "", xml)
    art3 = ET.fromstring(xml3).find(".//PubmedArticle")
    assert own_doi(art3) is None, f"expected None, got {own_doi(art3)}"

    # Direction 4: the erratum detector must FIRE on the planted ErratumIn ...
    ccs = own_comments_corrections(art)
    assert [c.get("RefType") for c in ccs] == ["ErratumIn"], ccs
    # ... and must NOT fire on a benign RefType (guard is not a blanket "any CC is bad").
    xml4 = xml.replace('RefType="ErratumIn"', 'RefType="CommentIn"')
    art4 = ET.fromstring(xml4).find(".//PubmedArticle")
    benign = [c for c in own_comments_corrections(art4) if c.get("RefType") in BAD_REFTYPES]
    assert benign == [], f"CommentIn wrongly flagged: {benign}"

    # Direction 5: CommentsCorrections nested in a Reference must not be read as the
    # article's own (the same scope bug as the DOI, in the other field).
    xml5 = xml.replace(
        "<ReferenceList><Reference>",
        '<ReferenceList><Reference><CommentsCorrectionsList>'
        '<CommentsCorrections RefType="RetractionIn"><PMID>11111111</PMID></CommentsCorrections>'
        "</CommentsCorrectionsList>",
    )
    art5 = ET.fromstring(xml5).find(".//PubmedArticle")
    rts = sorted(c.get("RefType") for c in own_comments_corrections(art5))
    assert rts == ["ErratumIn"], f"reference-scoped CommentsCorrections leaked in: {rts}"

    print("self-test OK: 5 directions exercised (reference-DOI leak, ELocationID fallback, "
          "no-DOI, erratum fires / benign does not, reference-scoped CC leak)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("pmids", nargs="*")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--json", help="write findings here")
    a = ap.parse_args()
    if a.self_test:
        self_test()
        sys.exit(0)
    assert a.pmids, "give me PMIDs (or --self-test)"
    out = check(a.pmids)
    hits = [f for f in out if f["pubmed_flags"] or f["crossref_flags"]]
    print(f"\nCHECKED {len(out)} PMIDs; {len(hits)} carry a correction/retraction signal")
    for h in hits:
        print("  !", h["pmid"], h["pubmed_flags"], h["crossref_flags"])
    if a.json:
        json.dump(out, open(a.json, "w"), indent=2)
