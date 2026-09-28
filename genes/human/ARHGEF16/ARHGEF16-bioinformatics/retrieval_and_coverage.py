#!/usr/bin/env python3
"""Three counts the ARHGEF16 review turns on, each re-derivable.

**1. Retrieval.**  The deep-research provider (affinage) reported clean trust
gates and a 100% faithfulness self-score, and every citation it returned is
genuinely about this protein.  The question a clean gate cannot answer is what it
did *not* return.  PubMed is queried for the union of the protein's names, and
the result is diffed against affinage's citation list and against the PMIDs GOA
itself cites.  The expected shape of the miss is specific: the literature calls
this protein **Ephexin4** and the database calls it **ARHGEF16**, so a
symbol-keyed retriever loses the mechanistic papers.

**2. GO coverage.**  For each primary paper, QuickGO is asked -- *by reference*,
species-blind -- whether it produced any GO annotation on ARHGEF16 or its mouse
ortholog.  A paper with no annotation is a curation gap, not evidence of absent
biology.  Truncated result sets are reported as unknown rather than as zero.

**3. Propagation.**  `GO:0005096 GTPase activator activity` is a GAP molecular
function annotated to a GEF.  QuickGO is asked which gene products carry it with
`UniProtKB:Q5VV41` in their `WITH/FROM`, i.e. how far the human row has already
travelled, and Reactome is asked which reaction sets place ARHGEF16 on a GTPase.

Run:    uv run --with requests python retrieval_and_coverage.py
        uv run --with requests python retrieval_and_coverage.py --self-test
Writes: retrieval_and_coverage.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import requests

ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
REACTOME_QUERY = "https://reactome.org/ContentService/data/query/{sid}"
REACTOME_REFS = "https://reactome.org/ContentService/data/participants/{sid}/referenceEntities"

TIMEOUT = 120

HUMAN = "Q5VV41"
MOUSE = "Q3U5C8"

PUBMED_QUERY = (
    'Ephexin4[Title/Abstract] OR ARHGEF16[Title/Abstract] OR "Ephexin-4"[Title/Abstract]'
)

# Reactome reactions that supply ARHGEF16's TAS `cytosol` rows, and the GTPase
# each asserts.  The membership itself is read from Reactome, not assumed.
REACTOME_REACTIONS = {
    "R-HSA-419166": "RhoA,B,C",
    "R-HSA-205039": "RAC and Cdc42",
}


def repo_root() -> Path:
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "genes").is_dir() and (parent / "publications").is_dir():
            return parent
    raise RuntimeError("could not locate the repository root above this script")


def affinage_citations() -> list[str]:
    """Read the provider's own citation list out of the deep-research file."""
    f = repo_root() / "genes/human/ARHGEF16/ARHGEF16-deep-research-affinage.md"
    text = f.read_text()
    body = text.split("## Citations", 1)
    if len(body) != 2:
        raise RuntimeError(f"{f} has no '## Citations' section")
    return sorted(set(re.findall(r"PMID:(\d+)", body[1])))


def goa_pmids() -> list[str]:
    f = repo_root() / "genes/human/ARHGEF16/ARHGEF16-goa.tsv"
    return sorted(set(re.findall(r"PMID:(\d+)", f.read_text())))


def pubmed_ids(query: str) -> list[str]:
    r = requests.get(
        ESEARCH,
        params={"db": "pubmed", "retmode": "json", "retmax": 200, "term": query},
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    res = r.json()["esearchresult"]
    if int(res["count"]) > len(res["idlist"]):
        raise RuntimeError("PubMed result truncated; raise retmax")
    return sorted(res["idlist"])


def pubmed_summaries(pmids: list[str]) -> dict[str, dict[str, str]]:
    if not pmids:
        return {}
    r = requests.get(
        ESUMMARY,
        params={"db": "pubmed", "retmode": "json", "id": ",".join(pmids)},
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    d = r.json()["result"]
    return {
        k: {
            "title": d[k].get("title", ""),
            "journal": d[k].get("source", ""),
            "year": (d[k].get("pubdate") or "")[:4],
        }
        for k in d.get("uids", [])
    }


def go_rows_for_reference(pmid: str) -> dict[str, object]:
    """Species-blind: ask whether this paper produced ANY annotation on either
    ortholog.  Reported as unknown, never as zero, if the page was truncated."""
    r = requests.get(
        QUICKGO,
        params={
            "geneProductId": f"UniProtKB:{HUMAN},UniProtKB:{MOUSE}",
            "reference": f"PMID:{pmid}",
            "limit": 200,
        },
        headers={"Accept": "application/json"},
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    d = r.json()
    rows = d.get("results") or []
    n = d.get("numberOfHits")
    if n is not None and n > len(rows):
        return {"n": n, "truncated": True, "terms": None}
    return {
        "n": len(rows),
        "truncated": False,
        "terms": sorted({f"{x['goId']}/{x['goEvidence']}" for x in rows}),
    }


def rows_propagated_from_human(go_id: str) -> dict[str, object]:
    """Every annotation, in any species, whose WITH/FROM names human ARHGEF16.

    Paged rather than capped: the IBA node for `GO:0005085` carries Q5VV41 as a
    donor and is inherited by orthologs across the whole tree, so a single page
    silently loses most of the answer -- and a truncated count read as a total is
    exactly the kind of number that ends up quoted in a review.
    """
    rows: list[dict] = []
    page, total = 1, None
    while True:
        r = requests.get(
            QUICKGO,
            params={
                "goId": go_id,
                "withFrom": f"UniProtKB:{HUMAN}",
                "limit": 200,
                "page": page,
            },
            headers={"Accept": "application/json"},
            timeout=TIMEOUT,
        )
        r.raise_for_status()
        d = r.json()
        total = d.get("numberOfHits") if total is None else total
        batch = d.get("results") or []
        rows.extend(batch)
        if not batch or len(rows) >= (total or 0):
            break
        page += 1
        if page > 50:
            raise RuntimeError(f"propagation query for {go_id} did not terminate")
    if total is not None and len(rows) != total:
        raise RuntimeError(f"propagation query for {go_id}: got {len(rows)} of {total}")
    by_taxon: dict[str, int] = {}
    for x in rows:
        by_taxon[str(x.get("taxonId"))] = by_taxon.get(str(x.get("taxonId")), 0) + 1
    return {
        "n": len(rows),
        "n_taxa": len(by_taxon),
        "evidence_codes": sorted({x.get("goEvidence") for x in rows}),
        "human_and_mouse_rows": sorted(
            {
                (x.get("geneProductId"), x.get("goEvidence"), x.get("reference"))
                for x in rows
                if x.get("taxonId") in (9606, 10090)
            }
        ),
    }


def reactome_membership() -> dict[str, dict[str, object]]:
    out: dict[str, dict[str, object]] = {}
    for sid, asserted in REACTOME_REACTIONS.items():
        meta = requests.get(REACTOME_QUERY.format(sid=sid), timeout=TIMEOUT).json()
        refs = requests.get(
            REACTOME_REFS.format(sid=sid),
            headers={"Accept": "application/json"},
            timeout=TIMEOUT,
        ).json()
        accs = sorted({x["identifier"] for x in refs if x.get("identifier")})
        names = sorted(
            {
                x.get("displayName", "").split()[-1]
                for x in refs
                if x.get("identifier") and x["identifier"].startswith(("O", "P", "Q", "A"))
            }
        )
        out[sid] = {
            "display_name": meta.get("displayName"),
            "asserted_gtpase": asserted,
            "n_protein_participants": len([a for a in accs if a[0] in "OPQA"]),
            "contains_ARHGEF16": HUMAN in accs,
            "participant_symbols": names,
        }
    return out


def run() -> dict[str, object]:
    affinage = affinage_citations()
    goa = goa_pmids()
    pubmed = pubmed_ids(PUBMED_QUERY)
    missed = sorted(set(pubmed) - set(affinage))
    summaries = pubmed_summaries(pubmed)

    if not affinage:
        raise RuntimeError("no affinage citations parsed; the file format changed")
    if not set(affinage) <= set(pubmed):
        raise RuntimeError(
            "affinage cited a PMID the name query does not return: "
            f"{sorted(set(affinage) - set(pubmed))}"
        )

    # Of the papers affinage missed, how many name the protein "Ephexin" in the
    # title while the database name is ARHGEF16?  This is the mechanism of the
    # miss, stated as a count rather than an impression.
    missed_ephexin_titled = sorted(
        p for p in missed if "ephexin" in summaries.get(p, {}).get("title", "").lower()
    )

    coverage = {p: go_rows_for_reference(p) for p in pubmed}
    no_annotation = sorted(p for p, c in coverage.items() if not c["truncated"] and c["n"] == 0)
    unknown = sorted(p for p, c in coverage.items() if c["truncated"])

    return {
        "retrieval": {
            "pubmed_query": PUBMED_QUERY,
            "n_pubmed": len(pubmed),
            "n_affinage_citations": len(affinage),
            "affinage_citations": affinage,
            "n_missed_by_affinage": len(missed),
            "missed_with_ephexin_in_title": {
                p: summaries.get(p, {}) for p in missed_ephexin_titled
            },
            "goa_cited_pmids": goa,
            "goa_pmids_missed_by_affinage": sorted(set(goa) & set(missed)),
        },
        "go_coverage": {
            "per_reference": coverage,
            "n_papers_with_no_GO_annotation": len(no_annotation),
            "papers_with_no_GO_annotation": {p: summaries.get(p, {}) for p in no_annotation},
            "unknown_because_truncated": unknown,
        },
        "propagation": {
            "GO:0005096_rows_sourced_from_human_ARHGEF16": rows_propagated_from_human(
                "GO:0005096"
            ),
            "GO:0005085_rows_sourced_from_human_ARHGEF16": rows_propagated_from_human(
                "GO:0005085"
            ),
        },
        "reactome": reactome_membership(),
    }


def self_test() -> int:
    checks: list[tuple[str, str]] = []

    # 1. The citation parser must find the provider's list.
    a = affinage_citations()
    checks.append(("affinage citations parsed", "PASS" if len(a) >= 5 else f"FAIL {a}"))

    # 2. NEGATIVE CONTROL: a file with no Citations section must raise, not return [].
    import tempfile
    import unittest.mock as mock

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "genes/human/ARHGEF16").mkdir(parents=True)
        (root / "publications").mkdir()
        (root / "genes/human/ARHGEF16/ARHGEF16-deep-research-affinage.md").write_text("# nothing\n")
        with mock.patch(f"{__name__}.repo_root", return_value=root):
            try:
                affinage_citations()
                checks.append(("missing Citations section raises", "FAIL (no exception)"))
            except RuntimeError:
                checks.append(("missing Citations section raises", "PASS"))

    # 3. The PubMed query must return the paper GOA leans on hardest.
    ids = pubmed_ids(PUBMED_QUERY)
    checks.append(
        (
            "PubMed query returns PMID:20679435",
            "PASS" if "20679435" in ids else f"FAIL {len(ids)} ids",
        )
    )

    # 4. Truncation must be detected, not silently accepted.
    try:
        pubmed_ids("cancer[Title]")
        checks.append(("truncated PubMed result raises", "FAIL (no exception)"))
    except RuntimeError:
        checks.append(("truncated PubMed result raises", "PASS"))

    # 5. Coverage probe: a paper GOA definitely cites must come back non-zero,
    #    and a paper it definitely does not must come back zero.  Both directions,
    #    because a probe that always says zero would look like a finding.
    pos = go_rows_for_reference("20679435")
    neg = go_rows_for_reference("33597305")
    checks.append(
        (
            "coverage probe distinguishes cited from uncited papers",
            "PASS" if pos["n"] > 0 and neg["n"] == 0 else f"FAIL {pos['n']} / {neg['n']}",
        )
    )

    # 6. Reactome membership must find ARHGEF16 in the RhoA,B,C GEF set, and the
    #    set must be broad enough that the claim is about set-level lumping.
    rc = reactome_membership()
    r = rc["R-HSA-419166"]
    checks.append(
        (
            "Reactome R-HSA-419166 contains ARHGEF16 among many GEFs",
            "PASS"
            if r["contains_ARHGEF16"] and r["n_protein_participants"] > 20
            else f"FAIL {r['contains_ARHGEF16']} / {r['n_protein_participants']}",
        )
    )

    # 7. An affinage citation outside the PubMed set must abort the run.
    real = affinage_citations
    try:
        globals()["affinage_citations"] = lambda: ["99999999"]
        run()
        checks.append(("out-of-set citation aborts run", "FAIL (no exception)"))
    except RuntimeError as e:
        checks.append(
            (
                "out-of-set citation aborts run",
                "PASS" if "does not return" in str(e) else f"FAIL {e}",
            )
        )
    finally:
        globals()["affinage_citations"] = real

    for name, verdict in checks:
        mark = verdict.split()[0]
        print(f"  [{mark}] {name}" + ("" if mark == "PASS" else f" -- {verdict}"))
    bad = [c for c in checks if not c[1].startswith("PASS")]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} self-tests passed")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    out = run()
    dest = Path(__file__).with_name("retrieval_and_coverage.json")
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    r = out["retrieval"]
    print(f"PubMed returns {r['n_pubmed']} records for the protein's names")
    print(f"affinage returned {r['n_affinage_citations']}, missing {r['n_missed_by_affinage']}")
    print(f"GOA cites {len(r['goa_cited_pmids'])} PMIDs; affinage missed "
          f"{len(r['goa_pmids_missed_by_affinage'])} of them: {r['goa_pmids_missed_by_affinage']}")
    print("\nmissed papers whose title says 'Ephexin' rather than ARHGEF16:")
    for p, s in r["missed_with_ephexin_in_title"].items():
        print(f"  {p}  {s.get('year')}  {s.get('journal')}  {s.get('title')}")

    c = out["go_coverage"]
    print(f"\n{c['n_papers_with_no_GO_annotation']} of {r['n_pubmed']} papers produced no GO "
          f"annotation on ARHGEF16 or mouse Arhgef16")
    if c["unknown_because_truncated"]:
        print(f"  (unknown, truncated: {c['unknown_because_truncated']})")

    p = out["propagation"]
    print("\nrows carrying UniProtKB:Q5VV41 in WITH/FROM:")
    for go, d in p.items():
        print(f"  {go}: {d['n']} rows across {d['n_taxa']} taxa, evidence {d['evidence_codes']}")
        for row in d["human_and_mouse_rows"]:
            print(f"     {row}")

    print("\nReactome reactions behind the TAS cytosol rows:")
    for sid, d in out["reactome"].items():
        print(
            f"  {sid} {d['display_name']}: asserts {d['asserted_gtpase']}, "
            f"{d['n_protein_participants']} protein participants, "
            f"contains ARHGEF16 = {d['contains_ARHGEF16']}"
        )
    print(f"\nwrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
