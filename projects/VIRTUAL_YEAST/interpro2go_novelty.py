#!/usr/bin/env python3
"""InterPro2GO prediction-novelty benchmark against curated GOA (yeast).

A genuine, reproducible source of GO predictions that are (or are not) in GOA:
for each reviewed gene we read its **real** InterPro domains from the cached UniProt
record, map them through the InterPro2GO table, and compare the predicted GO terms to
the terms already present in the gene's GOA file.

This produces the "true novelty" axis the retention pilot could not:
  - CNN  (Correct, Not Novel): predicted term already in GOA (exact id match)
  - NOVEL: predicted term absent from GOA (candidate COR / LSP / UNC / *_INCORRECT)
  - plus a count of uninformative "binding" defaults (a REP/frequency-bias signature)

Per-prediction COR/CNN/LSP/UNC/PLI/NPI/REP adjudication needs biological judgment and is
done by hand in <GENE>-interpro2go-predictions-review.yaml (see GCN5 worked example).
This script only counts what can be counted deterministically. Nothing is hardcoded.

Exact-id match is a *conservative* novelty proxy: it does not resolve ontology
subsumption, so a predicted ancestor/descendant of a GOA term is counted NOVEL here.

Run: python3 interpro2go_novelty.py [--genes-dir genes/yeast] [--i2g rules/arba/_interpro2go.txt]
"""
from __future__ import annotations

import argparse
import csv
import glob
import os
import re
import sys
from collections import Counter, defaultdict

# Uninformative / high-frequency "default" MF terms (REP / frequency-bias signature).
UNINFORMATIVE = {
    "GO:0005515": "protein binding",
    "GO:0005488": "binding",
    "GO:0003674": "molecular_function",
    "GO:0005575": "cellular_component",
    "GO:0008150": "biological_process",
    "GO:0005829": "cytosol",
    "GO:0005737": "cytoplasm",
}

IPR_RE = re.compile(r"^DR\s+InterPro;\s+(IPR\d+);")
I2G_RE = re.compile(r"^InterPro:(IPR\d+)\b.*?;\s*(GO:\d{7})\s*$")


def load_interpro2go(path: str) -> dict[str, set[str]]:
    mapping: dict[str, set[str]] = defaultdict(set)
    with open(path) as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            m = I2G_RE.match(line.strip())
            if m:
                mapping[m.group(1)].add(m.group(2))
    return mapping


def gene_interpro_ids(uniprot_txt: str) -> set[str]:
    ids: set[str] = set()
    with open(uniprot_txt) as fh:
        for line in fh:
            m = IPR_RE.match(line)
            if m:
                ids.add(m.group(1))
    return ids


def gene_goa_terms(goa_tsv: str) -> set[str]:
    terms: set[str] = set()
    with open(goa_tsv) as fh:
        reader = csv.reader(fh, delimiter="\t")
        header = next(reader, None)
        if not header:
            return terms
        try:
            idx = header.index("GO TERM")
        except ValueError:
            idx = 4
        for row in reader:
            if len(row) > idx and row[idx].startswith("GO:"):
                terms.add(row[idx])
    return terms


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--genes-dir", default="genes/yeast")
    ap.add_argument("--i2g", default="rules/arba/_interpro2go.txt")
    args = ap.parse_args()

    i2g = load_interpro2go(args.i2g)
    if not i2g:
        sys.exit(f"empty/unreadable InterPro2GO table: {args.i2g}")

    genes_with_pred = 0
    tot_pred = tot_cnn = tot_novel = tot_uninf = 0
    novel_term_freq: Counter = Counter()
    per_gene = []

    for gdir in sorted(glob.glob(os.path.join(args.genes_dir, "*"))):
        if not os.path.isdir(gdir):
            continue
        up = glob.glob(os.path.join(gdir, "*-uniprot.txt"))
        goa = glob.glob(os.path.join(gdir, "*-goa.tsv"))
        if not up or not goa:
            continue
        iprs = gene_interpro_ids(up[0])
        predicted = set()
        for ipr in iprs:
            predicted |= i2g.get(ipr, set())
        if not predicted:
            continue
        goa_terms = gene_goa_terms(goa[0])
        cnn = predicted & goa_terms
        novel = predicted - goa_terms
        uninf = predicted & set(UNINFORMATIVE)
        genes_with_pred += 1
        tot_pred += len(predicted)
        tot_cnn += len(cnn)
        tot_novel += len(novel)
        tot_uninf += len(uninf)
        for t in novel:
            novel_term_freq[t] += 1
        per_gene.append((os.path.basename(gdir), len(iprs), len(predicted),
                         len(cnn), len(novel), len(uninf)))

    if genes_with_pred == 0:
        print("No InterPro2GO-mappable predictions found (inconclusive).")
        return

    print(f"# InterPro2GO novelty benchmark  ({args.genes_dir})")
    print(f"# genes with >=1 domain-based prediction: {genes_with_pred}")
    print(f"# total unique predictions: {tot_pred}")
    pct = lambda x: f"{100*x/tot_pred:.1f}%"
    print(f"#   already in GOA (CNN, exact id): {tot_cnn} ({pct(tot_cnn)})")
    print(f"#   novel (absent from GOA):        {tot_novel} ({pct(tot_novel)})")
    print(f"#   uninformative 'binding' default:{tot_uninf} ({pct(tot_uninf)})\n")

    print("# Most frequent NOVEL predicted terms (candidates for hand review)")
    print("go_term\tn_genes")
    for t, n in novel_term_freq.most_common(15):
        flag = "  <-- uninformative" if t in UNINFORMATIVE else ""
        print(f"{t}\t{n}{flag}")

    print("\n# Per-gene (top 15 by prediction count)")
    print("gene\tn_interpro\tn_pred\tcnn\tnovel\tuninformative")
    for row in sorted(per_gene, key=lambda r: -r[2])[:15]:
        print("\t".join(map(str, row)))


if __name__ == "__main__":
    main()
