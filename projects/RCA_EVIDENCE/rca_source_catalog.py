"""Catalogue every reference behind an RCA annotation in GOA and classify the analysis type.

Answers "which computational analyses does GO code as RCA, and how many are omics?"
for the whole of GOA rather than for the gene corpus in this repository.

Pipeline (each step cached under data/ so reruns are offline and reproducible):
  1. download all RCA rows from QuickGO (ECO:0000245 *and descendants* -- BHF-UCL uses
     ECO:0007666, invisible to an exact query)          -> data/rca_goa_all.tsv
  2. fetch PubMed titles for every PMID reference (NCBI esummary)
                                                         -> data/rca_reference_titles.yaml
  3. fetch GO term labels for every term id (QuickGO ontology API)
                                                         -> data/rca_term_labels.yaml
  4. classify each reference:  analysis_class from a CURATED override table
     (rca_reference_classes.yaml) when present, otherwise from the title keyword rules
     below; the source of each call ("curated" / "title-rule" / "unclassified") is kept
     so a reader can see which calls were judged and which were pattern-matched.
                                                         -> data/rca_reference_catalog.yaml
  5. print summary tables (by class, by class x aspect, by class x group, top references)

Predicates:
  * rows are GOA annotation rows as QuickGO returns them (one per gene product x term x
    reference x with/from x qualifier).
  * "omics" = analysis_class in OMICS_CLASSES (high-throughput experimental data:
    proteomics, transcriptomics, interactomics, genetic-interaction or phenotype screens,
    other omics). Proteome-wide *computational* predictions (e.g. a zinc-binding scan of
    the predicted proteome) are a separate class, `proteome_scale_prediction`: they
    integrate sequence/structure data, not measurements.

Usage:
  python3 projects/RCA_EVIDENCE/rca_source_catalog.py            # use caches
  python3 projects/RCA_EVIDENCE/rca_source_catalog.py --refresh  # re-download everything
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
GOA_TSV = os.path.join(DATA, "rca_goa_all.tsv")
TITLES = os.path.join(DATA, "rca_reference_titles.yaml")
LABELS = os.path.join(DATA, "rca_term_labels.yaml")
CATALOG = os.path.join(DATA, "rca_reference_catalog.yaml")
OVERRIDES = os.path.join(HERE, "rca_reference_classes.yaml")

QUICKGO_DL = "https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch"
QUICKGO_TERMS = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/"
ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

OMICS_CLASSES = {
    "proteomics",
    "transcriptomics",
    "interactomics",
    "genetic_screen",
    "other_omics",
}

# Title keyword rules, applied in order; first match wins. Deliberately conservative:
# anything ambiguous should be settled in rca_reference_classes.yaml, not here.
TITLE_RULES: list[tuple[str, str]] = [
    ("interactomics", r"interactome|two-hybrid|yeast two hybrid|protein[- ]protein interaction|"
                      r"affinity purification|protein complexes|interaction map|interaction network"),
    ("proteomics", r"proteom|mass spectromet|\bLC-MS|\bMS/MS|glycoproteom|phosphoproteom|"
                   r"secretome|matrisome|\bSILAC\b|peptide identification|organelle composition"),
    ("transcriptomics", r"transcriptom|microarray|RNA-seq|RNA seq|expression profil|gene expression atlas|"
                        r"\bSAGE\b|expressed sequence tag|\bESTs?\b|serial analysis"),
    ("genetic_screen", r"genome-wide screen|genetic interaction|synthetic lethal|deletion (mutant )?(collection|library)|"
                       r"transposon (mutagenesis|sequencing)|\bTn-?seq\b|RNAi screen|phenotypic screen|"
                       r"functional profiling"),
    ("other_omics", r"metabolom|lipidom|ChIP-chip|ChIP-seq|localizome|GFP-tagged"),
    ("proteome_scale_prediction", r"\bin silico\b|prediction of|computational|bioinformatic|"
                                  r"proteome-wide|genome-wide (prediction|identification)"),
    ("family_or_genome_survey", r"family|superfamily|homologs|homologues|comparative genom|"
                                r"genome sequence|complete genome|repertoire|inventory"),
    ("pathway_or_metabolic_model", r"metabolic (network|reconstruction|model)|pathway database|Cyc\b"),
    ("single_gene_study", r"nucleotide sequence|operon|cloning|cloned|molecular characteri[sz]ation|"
                          r"characteri[sz]ation of|encoding|encodes|\bgene\b|\bgenes\b|mutant|"
                          r"identification of|isolation of"),
]


def fetch(url: str, accept: str | None = None, data: bytes | None = None, tries: int = 4) -> bytes:
    headers = {"Accept": accept} if accept else {}
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, data=data, headers=headers)
            with urllib.request.urlopen(req, timeout=300) as resp:
                return resp.read()
        except Exception:  # noqa: BLE001 - network retry
            if attempt == tries - 1:
                raise
            time.sleep(2 ** (attempt + 1))
    raise RuntimeError("unreachable")


def download_goa(refresh: bool) -> list[dict]:
    if refresh or not os.path.exists(GOA_TSV):
        q = urllib.parse.urlencode(
            {
                "evidenceCode": "ECO:0000245",
                "evidenceCodeUsage": "descendants",
                "downloadLimit": 50000,
                "selectedFields": "geneProductId,symbol,qualifier,goId,goAspect,evidenceCode,"
                "reference,withFrom,taxonId,assignedBy,date",
            }
        )
        raw = fetch(f"{QUICKGO_DL}?{q}", accept="text/tsv")
        os.makedirs(DATA, exist_ok=True)
        with open(GOA_TSV, "wb") as fh:
            fh.write(raw)
    with open(GOA_TSV, newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def fetch_titles(refs: list[str], refresh: bool) -> dict[str, dict]:
    cache: dict[str, dict] = {}
    if os.path.exists(TITLES) and not refresh:
        cache = yaml.safe_load(open(TITLES)) or {}
    pmids = [r.split(":", 1)[1] for r in refs if r.startswith("PMID:") and r not in cache]
    for i in range(0, len(pmids), 150):
        batch = pmids[i : i + 150]
        body = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(batch), "retmode": "json"})
        res = json.loads(fetch(ESUMMARY, data=body.encode()))["result"]
        for pmid in batch:
            rec = res.get(pmid) or {}
            cache[f"PMID:{pmid}"] = {
                "title": rec.get("title", ""),
                "year": (rec.get("pubdate") or "")[:4],
                "journal": rec.get("source", ""),
            }
        time.sleep(0.4)
    with open(TITLES, "w") as fh:
        fh.write("# Generated by rca_source_catalog.py (NCBI esummary) -- do not edit\n")
        yaml.safe_dump(dict(sorted(cache.items())), fh, sort_keys=False, width=120, allow_unicode=True)
    return cache


def fetch_labels(ids: list[str], refresh: bool) -> dict[str, str]:
    cache: dict[str, str] = {}
    if os.path.exists(LABELS) and not refresh:
        cache = yaml.safe_load(open(LABELS)) or {}
    todo = [i for i in ids if i not in cache]
    for i in range(0, len(todo), 100):
        batch = todo[i : i + 100]
        res = json.loads(fetch(QUICKGO_TERMS + ",".join(batch), accept="application/json"))
        for t in res.get("results", []):
            cache[t["id"]] = t.get("name", "")
    with open(LABELS, "w") as fh:
        fh.write("# Generated by rca_source_catalog.py (QuickGO ontology API) -- do not edit\n")
        yaml.safe_dump(dict(sorted(cache.items())), fh, sort_keys=False, width=120)
    return cache


def classify(ref: str, title: str, overrides: dict) -> tuple[str, str]:
    if ref in overrides:
        return overrides[ref]["class"], "curated"
    for cls, pat in TITLE_RULES:
        if title and re.search(pat, title, re.IGNORECASE):
            return cls, "title-rule"
    return "unclassified", "unclassified"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true")
    args = ap.parse_args()

    rows = download_goa(args.refresh)
    print(f"RCA rows downloaded: {len(rows)}")
    refs = sorted({r["REFERENCE"] for r in rows})
    titles = fetch_titles(refs, args.refresh)
    labels = fetch_labels(sorted({r["GO TERM"] for r in rows}), args.refresh)
    overrides = (yaml.safe_load(open(OVERRIDES)) or {}) if os.path.exists(OVERRIDES) else {}

    by_ref: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_ref[r["REFERENCE"]].append(r)

    catalog = []
    for ref, rs in sorted(by_ref.items(), key=lambda kv: -len(kv[1])):
        meta = titles.get(ref, {})
        cls, how = classify(ref, meta.get("title", ""), overrides)
        terms = Counter(f'{r["GO TERM"]} {labels.get(r["GO TERM"], "")}' for r in rs)
        catalog.append(
            {
                "reference": ref,
                "rows": len(rs),
                "genes": len({r["GENE PRODUCT ID"] for r in rs}),
                "title": meta.get("title") or overrides.get(ref, {}).get("title", ""),
                "year": meta.get("year", ""),
                "analysis_class": cls,
                "class_source": how,
                "class_note": overrides.get(ref, {}).get("note", ""),
                "assigned_by": dict(Counter(r["ASSIGNED BY"] for r in rs).most_common()),
                "taxa": dict(Counter(r["TAXON ID"] for r in rs).most_common(5)),
                "aspects": dict(Counter(r["GO ASPECT"] for r in rs).most_common()),
                "negated_rows": sum(1 for r in rs if r["QUALIFIER"].startswith("NOT")),
                "annotation_years": dict(sorted(Counter(r["DATE"][:4] for r in rs).items())),
                "top_terms": dict(terms.most_common(5)),
            }
        )
    with open(CATALOG, "w") as fh:
        fh.write("# Generated by rca_source_catalog.py -- do not edit; curate rca_reference_classes.yaml\n")
        yaml.safe_dump(catalog, fh, sort_keys=False, width=120, allow_unicode=True)

    total = len(rows)

    def show(title: str, counter: Counter, denom: int = total):
        print(f"\n## {title}")
        for k, v in counter.most_common():
            print(f"  {v:6d}  {100 * v / denom:5.1f}%  {k}")

    cls_rows = Counter()
    cls_refs = Counter()
    src_rows = Counter()
    for c in catalog:
        cls_rows[c["analysis_class"]] += c["rows"]
        cls_refs[c["analysis_class"]] += 1
        src_rows[c["class_source"]] += c["rows"]
    show("Rows by analysis_class", cls_rows)
    print("\n## References by analysis_class")
    for k, v in cls_refs.most_common():
        print(f"  {v:6d}  {k}")
    show("Rows by how the class was assigned", src_rows)

    omics_rows = sum(v for k, v in cls_rows.items() if k in OMICS_CLASSES)
    print(f"\nOMICS rows (classes {sorted(OMICS_CLASSES)}): {omics_rows} ({100 * omics_rows / total:.1f}%)")

    ref_class = {c["reference"]: c["analysis_class"] for c in catalog}
    asp = defaultdict(Counter)
    grp = defaultdict(Counter)
    neg = Counter()
    for r in rows:
        k = ref_class[r["REFERENCE"]]
        asp[k][r["GO ASPECT"]] += 1
        grp[k][r["ASSIGNED BY"]] += 1
        if r["QUALIFIER"].startswith("NOT"):
            neg[k] += 1
    print("\n## analysis_class x aspect (P/F/C) and NOT rows")
    for k in sorted(asp, key=lambda k: -sum(asp[k].values())):
        a = asp[k]
        print(f"  {k:28s} P={a['P']:5d} F={a['F']:5d} C={a['C']:5d}  NOT={neg[k]}")
    print("\n## analysis_class x assigned_by")
    for k in sorted(grp, key=lambda k: -sum(grp[k].values())):
        print(f"  {k:28s} " + ", ".join(f"{g}={n}" for g, n in grp[k].most_common()))

    # How omics data are used: group x aspect x polarity, plus annotation year range
    use = Counter()
    years: dict[tuple, set] = defaultdict(set)
    for r in rows:
        if ref_class[r["REFERENCE"]] in OMICS_CLASSES:
            key = (r["ASSIGNED BY"], r["GO ASPECT"], "NOT" if r["QUALIFIER"].startswith("NOT") else "positive")
            use[key] += 1
            years[key].add(r["DATE"][:4])
    print("\n## Omics rows by assigned_by x aspect x polarity (annotation years)")
    for (g, a, p), n in use.most_common():
        print(f"  {n:5d}  {g:10s} {a} {p:8s} {min(years[(g, a, p)])}-{max(years[(g, a, p)])}")

    # The omics aspect question: what does each omics reference assert?
    print("\n## Omics references (>=3 rows): rows, aspects, top terms")
    for c in catalog:
        if c["analysis_class"] in OMICS_CLASSES and c["rows"] >= 3:
            terms = "; ".join(f"{k} ({v})" for k, v in list(c["top_terms"].items())[:3])
            print(
                f'  {c["rows"]:5d} {c["reference"]:28s} [{c["analysis_class"]}/{c["class_source"]}] '
                f'{",".join(c["assigned_by"])} aspects={c["aspects"]} NOT={c["negated_rows"]} '
                f'annotated={",".join(c["annotation_years"])}\n'
                f'        {c["title"][:110]}\n        {terms}'
            )
    print("\n## Unclassified references (>=3 rows) -- curate in rca_reference_classes.yaml")
    for c in catalog:
        if c["analysis_class"] == "unclassified" and c["rows"] >= 3:
            print(f'  {c["rows"]:5d} {c["reference"]:28s} {",".join(c["assigned_by"])}  {c["title"][:110]}')
    return 0


if __name__ == "__main__":
    sys.exit(main())
