#!/usr/bin/env python3
"""How much of the ARHGEF19 literature has reached GO, in any species?

Run from this directory:  uv run python go_coverage_by_reference.py

ARHGEF19 (WGEF / Ephexin-2) is sparsely characterised, so the interesting
question is not "which annotations are over-called" but "which experiments never
became annotations at all". This script asks QuickGO, for every primary paper
about the gene, how many GO annotations in ANY species cite that paper -- and
how many of those are about ARHGEF19 itself rather than a co-studied partner.

The paper list is assembled from two INDEPENDENT sources so that the answer does
not depend on either one being complete:

  * the citations of the Affinage deep-research record for this gene, and
  * a live PubMed E-utilities search over the gene's synonyms.

Both are searched at run time; nothing is hardcoded except the query strings and
the hand-classified paper type (primary experimental work on the gene vs review,
commentary, genomics survey or passing mention), which is the one judgement a
machine cannot make for us and is therefore stated explicitly below.

Exit codes: 0 = ran and reported; 2 = a service did not answer.
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
AFFINAGE = (
    Path(__file__).resolve().parent.parent / "ARHGEF19-deep-research-affinage.md"
)

GENE = "ARHGEF19"
GENE_SYNONYMS = {"ARHGEF19", "WGEF", "EPHEXIN-2", "EPHEXIN2", "RHOGEF19", "GEF19"}

# Live PubMed queries. "GEF19" is included deliberately: one paper about this
# gene is titled "Grhl3 and GEF19 in the front rho", which no ARHGEF19 or WGEF
# query returns.
PUBMED_QUERIES = [
    "ARHGEF19",
    "WGEF",
    '"RhoGEF19"',
    '"GEF19"',
    "ephexin2 OR ephexin-2",
]

# Paper classification. PRIMARY = reports its own experiments on this gene's
# product. The rest are excluded from the coverage denominator and listed
# separately so the exclusion is auditable rather than silent.
PRIMARY = {
    "15485661": "first characterisation; RhoA/Cdc42/Rac1 pulldowns, actin phenotype",
    "18256687": "Wnt-PCP; human+Xenopus RhoA activation, Dvl/Daam1 binding, autoinhibition",
    "18537266": "Tyr-phosphorylation relief of N-terminal autoinhibition in Wgef and Ngef",
    "19503838": "DNA methylation of exon 1; negative regulator of adipogenesis (3T3-L1)",
    "20643356": "GRHL3 target; keratinocyte polarity, actin and wound repair",
    "20810787": "negative result: WGEF shRNA does not block Dvl/Wnt-3a RhoA activation in N1E-115",
    "21804089": "Daam1/WGEF/Rho branch required for pronephric tubulogenesis",
    "24405610": "direct miR-503 target in hepatocellular carcinoma",
    "29164615": "binds BRAF via DH+PH; activates MAPK, RhoA-independent (NSCLC)",
    "31469868": "required for primary ciliogenesis in MDCKII/IMCD3",
    "32993957": "binds HRAS via DH+PH; activates MAPK/ERK (SCLC)",
    "34813497": "promotes breast cancer growth via MAPK",
    "38714795": "Dvl2-PDZ engages an internal PDZ-binding motif; releases autoinhibition",
    "39409035": "ANKK1 binds WGEF and regulates the WGEF-RhoA interaction (SH-SY5Y)",
}
NOT_PRIMARY = {
    "21686262": "commentary on PMID:20643356",
    "30682817": "review of the Ephexin family",
    "33597305": "Ephexin-family structural study; ARHGEF19 mentioned, not assayed",
    "24431302": "Wnt-signalling review (the source of the existing NAS annotation)",
    "32296183": "proteome-scale binary interactome screen, not an ARHGEF19 study",
}


@dataclass
class Row:
    pmid: str
    total: int
    on_gene: int
    on_gene_terms: set[str]


def get(url: str, attempts: int = 5) -> dict:
    for i in range(attempts):
        try:
            req = urllib.request.Request(
                url, headers={"Accept": "application/json", "User-Agent": "aigr-arhgef19"}
            )
            with urllib.request.urlopen(req, timeout=90) as fh:
                return json.load(fh)
        except urllib.error.HTTPError as exc:
            if exc.code not in (429, 500, 502, 503) or i == attempts - 1:
                print(f"SERVICE FAILURE: {url} -> HTTP {exc.code}", file=sys.stderr)
                sys.exit(2)
            time.sleep(3 * (i + 1))
    sys.exit(2)


def pubmed_union() -> set[str]:
    found: set[str] = set()
    for q in PUBMED_QUERIES:
        url = (
            f"{EUTILS}/esearch.fcgi?db=pubmed&retmode=json&retmax=200&term="
            + urllib.parse.quote(q)
        )
        d = get(url)
        found |= set(d["esearchresult"].get("idlist", []))
        time.sleep(0.4)
    return found


def quickgo_by_reference(pmid: str) -> Row:
    d = get(f"{QUICKGO}?reference=PMID:{pmid}&limit=200")
    total = int(d.get("numberOfHits", 0))
    on_gene = 0
    terms: set[str] = set()
    for r in d.get("results", []):
        sym = (r.get("symbol") or "").upper()
        if sym in GENE_SYNONYMS:
            on_gene += 1
            terms.add(f"{r.get('goId')} ({r.get('goEvidence')})")
    return Row(pmid, total, on_gene, terms)


def main() -> int:
    print(f"# GO coverage of the {GENE} literature (QuickGO, all species)")
    print()

    pm = pubmed_union()
    print(f"PubMed union over {len(PUBMED_QUERIES)} live queries: {len(pm)} PMIDs")
    classified = set(PRIMARY) | set(NOT_PRIMARY)
    missing = sorted(p for p in classified if p not in pm)
    print(f"Classified papers not returned by any live PubMed query: "
          f"{missing if missing else 'none'}")
    print("  (a classified paper the queries miss is a retrieval blind spot, not "
          "an error -- it is still scored below)")
    print()

    rows = []
    for pmid in sorted(PRIMARY):
        rows.append(quickgo_by_reference(pmid))
        time.sleep(0.2)

    print("## Primary experimental papers on ARHGEF19")
    print()
    print("| PMID | what it reports | GO annotations citing it (any gene, any species) "
          "| ...that are ON ARHGEF19 | terms |")
    print("|---|---|---|---|---|")
    for r in rows:
        terms = ", ".join(sorted(r.on_gene_terms)) or "-"
        print(f"| PMID:{r.pmid} | {PRIMARY[r.pmid]} | {r.total} | {r.on_gene} | {terms} |")
    print()

    zero_any = [r for r in rows if r.total == 0]
    zero_gene = [r for r in rows if r.on_gene == 0]
    informative = [
        r for r in rows
        if any(not t.startswith("GO:0005515") for t in r.on_gene_terms)
    ]
    print(f"- {len(zero_any)}/{len(rows)} primary papers have produced **no GO "
          f"annotation of any gene in any species**: "
          + ", ".join(f"PMID:{r.pmid}" for r in zero_any))
    print(f"- {len(zero_gene)}/{len(rows)} have produced **no GO annotation of "
          f"ARHGEF19 in any species**")
    print(f"- {len(informative)}/{len(rows)} have produced an ARHGEF19 annotation "
          "to anything other than GO:0005515 protein binding: "
          + (", ".join(f"PMID:{r.pmid}" for r in informative) or "none"))
    print()

    print("## What the Affinage record cited, and what it did not")
    print()
    if not AFFINAGE.exists():
        print(f"(no Affinage record at {AFFINAGE}; skipping)")
    else:
        cited = set(re.findall(r"PMID:(\d+)", AFFINAGE.read_text(encoding="utf-8")))
        print(f"Affinage cites {len(cited)} PMIDs. Its trust gates say nothing about "
              "recall, so the useful number is what it left out.")
        print()
        missed_primary = sorted(set(PRIMARY) - cited)
        missed_other = sorted(set(NOT_PRIMARY) - cited)
        extra = sorted(cited - classified)
        print(f"- primary papers NOT cited by Affinage ({len(missed_primary)} of "
              f"{len(PRIMARY)}): "
              + (", ".join(f"PMID:{p}" for p in missed_primary) or "none"))
        for p in missed_primary:
            print(f"    - PMID:{p}: {PRIMARY[p]}")
        print(f"- non-primary papers NOT cited ({len(missed_other)}): "
              + (", ".join(f"PMID:{p}" for p in missed_other) or "none"))
        print(f"- cited but not in this review's classification ({len(extra)}): "
              + (", ".join(f"PMID:{p}" for p in extra) or "none"))
        print()

    print("## Excluded from the denominator (not primary work on this gene)")
    print()
    print("| PMID | why excluded | GO annotations citing it |")
    print("|---|---|---|")
    for pmid in sorted(NOT_PRIMARY):
        r = quickgo_by_reference(pmid)
        time.sleep(0.2)
        print(f"| PMID:{pmid} | {NOT_PRIMARY[pmid]} | {r.total} |")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
