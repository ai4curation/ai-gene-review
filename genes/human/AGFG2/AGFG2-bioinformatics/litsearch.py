#!/usr/bin/env python3
"""Recorded PubMed queries behind every search-derived negative in this review.

A search-derived negative is a statement about a *query*, never about the world.
This script therefore stores the exact query strings alongside their hit counts
and titles, so the negative can be re-run and its scope checked.

Each negative query is paired with a **positive control** using the same call
pattern, because a rejected query and a genuine zero look identical downstream.
"""

from __future__ import annotations

import json
import pathlib
import sys
import time
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import get_json  # noqa: E402

HERE = pathlib.Path(__file__).parent
E = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

# (label, query, kind)  kind: "negative-under-test" | "positive-control"
QUERIES = [
    # --- Has ArfGAP catalytic activity ever been measured on an AGFG protein? ---
    ("agfg_gap_activity",
     '(AGFG1[tiab] OR AGFG2[tiab] OR HRB[tiab] OR HRBL[tiab] OR drongo[tiab]) '
     'AND ("GAP activity"[tiab] OR "GTPase-activating"[tiab] OR "GTPase activating"[tiab] '
     'OR "GTP hydrolysis"[tiab] OR ArfGAP[tiab] OR "Arf-GAP"[tiab])',
     "negative-under-test"),
    ("arfgap_activity_control",
     '("GAP activity"[tiab] OR "GTPase-activating"[tiab]) AND (ARFGAP1[tiab] OR ASAP1[tiab])',
     "positive-control"),
    # --- Broadest possible AGFG2 sweep, synonym space included ---
    ("agfg2_all_synonyms",
     'AGFG2[tiab] OR HRBL[tiab] OR "HRB-like"[tiab] OR "Rev/Rex activation domain-binding '
     'protein related"[tiab] OR "RAB-R"[tiab]',
     "negative-under-test"),
    ("agfg1_all_synonyms_control",
     'AGFG1[tiab] OR HRB[tiab] OR hRIP[tiab] OR "Rev-binding protein"[tiab]',
     "positive-control"),
    # --- Any acrosome / spermatogenesis study of AGFG2 itself? ---
    ("agfg2_acrosome",
     '(AGFG2[tiab] OR HRBL[tiab]) AND (acrosome[tiab] OR acrosomal[tiab] OR spermatid[tiab] '
     'OR spermatogenesis[tiab] OR sperm[tiab] OR testis[tiab])',
     "negative-under-test"),
    ("agfg1_acrosome_control",
     '(AGFG1[tiab] OR Hrb[tiab]) AND (acrosome[tiab] OR acrosomal[tiab])',
     "positive-control"),
    # --- Any intermediate-filament study of AGFG2 itself? ---
    ("agfg2_intermediate_filament",
     '(AGFG2[tiab] OR HRBL[tiab]) AND (keratin[tiab] OR "intermediate filament"[tiab] '
     'OR vimentin[tiab] OR manchette[tiab])',
     "negative-under-test"),
    # --- Zinc binding measured on an AGFG protein? ---
    ("agfg_zinc",
     '(AGFG1[tiab] OR AGFG2[tiab] OR HRB[tiab] OR HRBL[tiab]) AND (zinc[tiab] OR "zinc finger"[tiab])',
     "negative-under-test"),
]

# Individual PMIDs whose titles are load-bearing somewhere in the review.
TITLES_NEEDED = [
    "27654348",  # FlyBase IDA reference for drongo GO:0005737 / GO:0005938
    "11711676",  # mouse Hrb: acrosome assembly IMP + cytoplasmic vesicle IDA
    "14724135",  # mouse Hrb: acrosome assembly + intermediate filament organization IMP
    "16765935",  # mouse Hrb: spermatid nucleus differentiation IMP
    "19946888",  # AGFG2 GO:0016020 HDA
]

# Every other PMID the review cites, so the retraction/erratum sweep covers the same
# set as the YAML's `references` block rather than a subset of it.
CITED_BY_REVIEW = {
    "9303539",   # Salcini 1997, EH-domain targets (AGFG2 cDNA / RAB-R)
    "10613896",  # Doria 1999, Eps15/Eps15R + Hrb/Hrbl in the Rev export pathway
    "21284487",  # Panaro 2011, AGFG gene organisation
    "23433073",  # Schlacht 2013, Arf GAP phylogeny + catalytic-residue conservation
    "25496667",  # Landi 2014, genome-wide shRNA screen, CD4 down-regulation
    "26701340",  # Landi 2016, HRB/HRBL as Nef and Vpu co-factors
    "34369554",  # Watanabe 2021, SMAP1/AGFG2 and vWF exocytosis
}


def esearch(term: str) -> dict:
    url = f"{E}/esearch.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "term": term, "retmode": "json", "retmax": 60}
    )
    d = get_json(url)["esearchresult"]
    return {"count": int(d["count"]), "pmids": d.get("idlist", [])}


def esummary(pmids: list[str]) -> dict:
    if not pmids:
        return {}
    url = f"{E}/esummary.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "id": ",".join(pmids), "retmode": "json"}
    )
    d = get_json(url)["result"]
    return {
        p: {
            "title": d[p].get("title"),
            "journal": d[p].get("fulljournalname"),
            "year": (d[p].get("pubdate") or "")[:4],
            "pubtypes": d[p].get("pubtype"),
        }
        for p in d.get("uids", [])
    }


def comments_corrections(pmid: str) -> list[dict]:
    """Retraction / erratum / expression-of-concern check.

    Read from the *cited* article's own record, because a Publisher Correction is
    not discoverable through a publication-type search.
    """
    import urllib.request
    from xml.etree import ElementTree as ET

    url = f"{E}/efetch.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "id": pmid, "retmode": "xml"}
    )

    with urllib.request.urlopen(url, timeout=90) as r:
        if r.status != 200:
            raise RuntimeError(f"HTTP {r.status} for efetch {pmid}")
        xml = r.read()
    root = ET.fromstring(xml)
    out = []
    for cc in root.iter("CommentsCorrections"):
        ref = cc.findtext("PMID")
        out.append({"refType": cc.get("RefType"), "pmid": ref,
                    "source": cc.findtext("RefSource")})
    return out


def main() -> None:
    out: dict = {"queries": {}, "titles": {}, "comments_corrections": {}}
    for label, term, kind in QUERIES:
        r = esearch(term)
        out["queries"][label] = {"query": term, "kind": kind, **r}
        time.sleep(0.4)

    # A negative is only interpretable if its control is non-zero.
    for label, v in out["queries"].items():
        if v["kind"] == "positive-control" and v["count"] == 0:
            raise AssertionError(f"positive control {label} returned 0 — endpoint broken")

    all_pmids = sorted({p for v in out["queries"].values() for p in v["pmids"]}
                       | set(TITLES_NEEDED))
    for i in range(0, len(all_pmids), 40):
        out["titles"].update(esummary(all_pmids[i:i + 40]))
        time.sleep(0.4)

    # Every PMID the review relies on, so the retraction/erratum count in RESULTS.md
    # is over the same set the review cites.  Keep this list in step with the YAML.
    cited = sorted(set(TITLES_NEEDED) | CITED_BY_REVIEW)
    out["n_cited_checked"] = len(cited)
    for p in cited:
        out["comments_corrections"][p] = comments_corrections(p)
        time.sleep(0.4)

    (HERE / "litsearch.json").write_text(json.dumps(out, indent=2, sort_keys=True))

    for label, v in out["queries"].items():
        print(f"\n[{v['kind']}] {label}: {v['count']} hits")
        print(f"  query: {v['query']}")
        for p in v["pmids"][:25]:
            t = out["titles"].get(p, {})
            print(f"    {p} ({t.get('year')}) {t.get('title')}")

    print("\n=== titles needed ===")
    for p in TITLES_NEEDED:
        t = out["titles"].get(p, {})
        print(f"  PMID:{p} ({t.get('year')}) {t.get('journal')} — {t.get('title')}")

    print("\n=== retraction / erratum check (CommentsCorrections on each cited record) ===")
    for p, cc in out["comments_corrections"].items():
        flags = [c for c in cc if c["refType"] in {
            "RetractionIn", "ErratumIn", "ExpressionOfConcernIn", "CorrectedandRepublishedIn",
            "RetractedandRepublishedIn",
        }]
        print(f"  PMID:{p}: {len(cc)} CommentsCorrections; problem flags: {flags or 'none'}")


if __name__ == "__main__":
    main()
