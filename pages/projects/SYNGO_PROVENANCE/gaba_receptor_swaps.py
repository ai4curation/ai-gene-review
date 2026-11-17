"""Find SynGO annotations that put GABA-B receptor findings on GABA-A genes, or the reverse.

GABA-B receptor subunits are written GABA(B1) and GABA(B2) (genes GABBR1,
GABBR2); GABA-A beta subunits are beta1-3 (genes GABRB1-3). A name-matching
slip maps one onto the other. This script:

1. fetches every SynGO annotation from QuickGO and keeps those on a GABA
   receptor gene (symbols GABR*/GABBR*, any species);
2. fetches each cited paper's title and abstract from PubMed;
3. flags a paper when a GABA-A gene is annotated from it and its text names
   GABA-B receptors at least as often as GABA-A receptors, or when a GABA-B gene
   is annotated from a paper that names GABA-A receptors more often than GABA-B;
4. for each flagged (paper, gene product), lists SynGO's terms and counts the
   annotations derived from that seed: QuickGO rows with the same GO term whose
   WITH/FROM names the seed's accession (Ensembl projections, ISO, UniProt).

The flag is a lead for reading, not a verdict: a paper on both receptor types
can be annotated correctly to both. Output:
``data/gaba_receptor_swaps.yaml``.

    python projects/SYNGO_PROVENANCE/gaba_receptor_swaps.py
"""
from __future__ import annotations

import collections
import datetime
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "projects/SYNGO_PROVENANCE/data/gaba_receptor_swaps.yaml"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
GABA_B_TEXT = re.compile(r"GABA\s*\(?B|GABAB|GABA-B|baclofen|GABBR", re.I)
GABA_A_TEXT = re.compile(r"GABA\s*\(?A\)?\s*receptor|GABAA|GABA-A|GABA\(A|benzodiazepine|muscimol|bicuculline|gabazine",
                         re.I)


def quickgo(**params: str) -> list[dict]:
    """Return every QuickGO annotation matching ``params`` (paged)."""
    rows, page = [], 1
    while True:
        url = f"{QUICKGO}?{urllib.parse.urlencode(dict(params, limit=100, page=page))}"
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.load(resp)
        rows += data.get("results", [])
        if page >= data.get("pageInfo", {}).get("total", 1):
            return rows
        page += 1


def pubmed_text(pmids: list[str]) -> dict[str, tuple[str, str]]:
    """Map PMID to (title, abstract)."""
    out: dict[str, tuple[str, str]] = {}
    for i in range(0, len(pmids), 150):
        query = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(pmids[i:i + 150]), "retmode": "xml"})
        with urllib.request.urlopen(f"{EUTILS}?{query}", timeout=120) as resp:
            root = ET.fromstring(resp.read())
        for art in root.findall(".//PubmedArticle"):
            title_el = art.find(".//ArticleTitle")
            title = "".join(title_el.itertext()) if title_el is not None else ""
            abstract = " ".join("".join(e.itertext()) for e in art.findall(".//AbstractText"))
            out[art.findtext(".//PMID") or ""] = (title, abstract)
        time.sleep(0.5)
    return out


def is_gaba_b_gene(symbol: str) -> bool:
    return symbol.upper().startswith("GABBR")


def main() -> None:
    syngo = [r for r in quickgo(assignedBy="SynGO", includeFields="goName")
             if re.match(r"GABR|GABBR", (r.get("symbol") or "").upper())]
    by_ref: dict[str, list[dict]] = collections.defaultdict(list)
    for r in syngo:
        by_ref[r["reference"]].append(r)
    text = pubmed_text(sorted({ref.split(":", 1)[1] for ref in by_ref if ref.startswith("PMID:")}))
    papers = []
    for ref in sorted(by_ref):
        title, abstract = text.get(ref.split(":", 1)[1], ("", ""))
        n_b = len(GABA_B_TEXT.findall(f"{title} {abstract}"))
        n_a = len(GABA_A_TEXT.findall(f"{title} {abstract}"))
        symbols = sorted({r["symbol"] for r in by_ref[ref]})
        on_a = [s for s in symbols if not is_gaba_b_gene(s)]
        on_b = [s for s in symbols if is_gaba_b_gene(s)]
        flagged = bool((on_a and n_b and n_b >= n_a) or (on_b and n_a > n_b))
        paper = {"reference": ref, "title": title, "gaba_a_genes": on_a, "gaba_b_genes": on_b,
                 "gaba_b_mentions": n_b, "gaba_a_mentions": n_a, "flagged": flagged}
        if flagged:
            seeds = collections.defaultdict(set)
            suspect = on_a if n_b >= n_a else on_b
            for r in by_ref[ref]:
                if r["symbol"] in suspect:
                    seeds[(r["symbol"], r["taxonId"], r["geneProductId"])].add((r["goId"], r["goName"]))
            paper["suspect_annotations"] = []
            for (sym, tax, gp), terms in sorted(seeds.items()):
                acc = gp.split(":", 1)[1]
                rec = {"symbol": sym, "taxon": tax, "gene_product": gp, "terms": []}
                for go_id, go_name in sorted(terms):
                    derived = quickgo(withFrom=acc, goId=go_id, goUsage="exact")
                    other_syngo = sorted({x["reference"] for x in quickgo(geneProductId=gp, goId=go_id, goUsage="exact",
                                                                          assignedBy="SynGO")} - {ref})
                    rec["terms"].append({
                        "go_id": go_id, "go_name": go_name, "derived_rows": len(derived),
                        "derived_taxa": len({x["taxonId"] for x in derived}),
                        "derived_human": sorted({x["symbol"] for x in derived if x["taxonId"] == 9606}),
                        "same_term_from_other_syngo_papers": other_syngo})
                paper["suspect_annotations"].append(rec)
        papers.append(paper)
    doc = {"retrieved": datetime.date.today().isoformat(), "syngo_rows_on_gaba_receptor_genes": len(syngo),
           "papers": len(papers), "flagged": sum(p["flagged"] for p in papers),
           "flagged_papers": [p for p in papers if p["flagged"]],
           "unflagged_papers": [{k: p[k] for k in ("reference", "gaba_a_genes", "gaba_b_genes", "gaba_b_mentions",
                                                    "gaba_a_mentions")} for p in papers if not p["flagged"]]}
    with OUT.open("w") as fh:
        yaml.safe_dump(doc, fh, sort_keys=False, width=120, allow_unicode=True)
    for p in doc["flagged_papers"]:
        print(p["reference"], p["title"][:90])
        for s in p["suspect_annotations"]:
            for t in s["terms"]:
                print(f"  {s['symbol']} ({s['taxon']}) {t['go_id']} {t['go_name']}: {t['derived_rows']} derived rows,"
                      f" other SynGO papers: {t['same_term_from_other_syngo_papers']}")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
