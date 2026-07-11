#!/usr/bin/env python3
"""Cluster the large ppu02010 ABC transporter batch into locus-neighborhood sub-batches."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


BATCH = Path("projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary.tsv")
OUT_TSV = Path("projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary_clusters.tsv")
OUT_MD = Path("projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary_clusters.md")


PATTERNS = [
    ("sulfur/sulfonate/taurine", re.compile(r"sulf|sulfonate|taurine|cystine|cys", re.I)),
    ("methionine/amino acid/polyamine", re.compile(r"methionine|amino acid|arginine|ornithine|branched-chain|peptide|putrescine|polyamine", re.I)),
    ("osmoprotectant/choline/betaine/carnitine", re.compile(r"choline|betaine|carnitine|osmoprotectant", re.I)),
    ("metal/cobalamin/siderophore", re.compile(r"zinc|znu|nickel|nik|molybdate|tungstate|iron|ferric|heme|siderophore|pyoverdine|cobalamin|vitamin b12", re.I)),
    ("lipid/lps/lipoprotein", re.compile(r"phospholipid|lipopolysaccharide|lps|lipoprotein|lipid|lol|mla", re.I)),
    ("phosphate/phosphonate/glycerol-phosphate", re.compile(r"phosphate|phosphonate|glycerol-phosphate", re.I)),
    ("sugar/polyol", re.compile(r"sugar|glucose|mannose|maltose|ribose|xylose|arabinose|polyol|glycerol|mannitol", re.I)),
    ("efflux/secretion/toxin", re.compile(r"efflux|secretion|toxin|export|resistance|pvdT", re.I)),
    ("general ABC", re.compile(r"ABC transporter|ATP-binding|permease|binding protein", re.I)),
]


def locus_number(row: dict) -> int:
    match = re.search(r"PP_(\d+)", row["ordered_locus"])
    return int(match.group(1)) if match else 10**9


def product_class(product: str) -> str:
    for label, pattern in PATTERNS:
        if pattern.search(product):
            return label
    return "other"


def cluster_rows(rows: list[dict]) -> list[list[dict]]:
    rows = sorted(rows, key=locus_number)
    clusters: list[list[dict]] = []
    current: list[dict] = []
    previous = None
    for row in rows:
        number = locus_number(row)
        if not current or (previous is not None and number - previous <= 3):
            current.append(row)
        else:
            clusters.append(current)
            current = [row]
        previous = number
    if current:
        clusters.append(current)
    return clusters


def summarize_cluster(index: int, cluster: list[dict]) -> dict:
    classes = Counter(product_class(row["protein_name"]) for row in cluster)
    primary = Counter(row["primary_bucket_id"] for row in cluster)
    review = Counter(row["review_status"] for row in cluster)
    asta = Counter(row["asta_research_status"] for row in cluster)
    loci = [row["ordered_locus"] for row in cluster]
    genes = [row["suggested_review_name"] for row in cluster]
    products = [row["protein_name"] for row in cluster]
    return {
        "cluster_id": f"ppu02010-C{index:02d}",
        "start_locus": loci[0],
        "end_locus": loci[-1],
        "size": str(len(cluster)),
        "dominant_class": classes.most_common(1)[0][0],
        "classes": "; ".join(f"{k}:{v}" for k, v in classes.most_common()),
        "primary_buckets": "; ".join(f"{k}:{v}" for k, v in primary.most_common()),
        "review_status": "; ".join(f"{k}:{v}" for k, v in review.most_common()),
        "asta_status": "; ".join(f"{k}:{v}" for k, v in asta.most_common()),
        "genes": ", ".join(genes),
        "products": " | ".join(products),
    }


def main() -> None:
    rows = list(csv.DictReader(BATCH.open(), delimiter="\t"))
    clusters = cluster_rows(rows)
    summaries = [summarize_cluster(index + 1, cluster) for index, cluster in enumerate(clusters)]

    fieldnames = list(summaries[0])
    with OUT_TSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(summaries)

    class_counts = Counter(summary["dominant_class"] for summary in summaries)
    review_totals = Counter(row["review_status"] for row in rows)
    asta_totals = Counter(row["asta_research_status"] for row in rows)
    by_class_genes = defaultdict(int)
    by_class_missing = defaultdict(int)
    for row in rows:
        label = product_class(row["protein_name"])
        by_class_genes[label] += 1
        if row["review_status"] != "PRESENT":
            by_class_missing[label] += 1

    lines = [
        "---",
        'title: "PSEPK ppu02010 ABC transporter cluster report"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK ppu02010 ABC Transporter Cluster Report",
        "",
        f"- Candidate genes: {len(rows)}",
        f"- Locus-neighborhood clusters: {len(clusters)}",
        f"- Review status: {dict(review_totals)}",
        f"- Asta status: {dict(asta_totals)}",
        "",
        "## Product-Class Summary",
        "",
        "| Product class | Genes | Missing reviews | Dominant-neighborhood clusters |",
        "|---|---:|---:|---:|",
    ]
    for label, count in sorted(by_class_genes.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| {label} | {count} | {by_class_missing[label]} | {class_counts[label]} |")
    lines.extend(
        [
            "",
            "## Candidate Sub-Batch Guidance",
            "",
            "- Do not treat `ppu02010` as a single satisfiable pathway. It is an umbrella map for many unrelated ABC import/export systems.",
            "- Reuse already curated sulfur-transporter members from `sulfur_metabolism_boundary` rather than reopening them unless a warning appears.",
            "- Good first sub-batches are coherent locus blocks with recognizable substrates: methionine/zinc at PP_0112-PP_0120, sulfur/cystine at PP_0225-PP_0240, choline/betaine/carnitine at PP_0294-PP_0304, phosphonate at PP_0824-PP_0827, and zinc/nickel/metal systems.",
            "- Large generic ABC clusters should be deferred until substrate-specific neighbors or module context are clearer.",
            "",
            "## Locus-Neighborhood Clusters",
            "",
            "| Cluster | Locus span | Size | Dominant class | Review status | Asta status | Genes |",
            "|---|---|---:|---|---|---|---|",
        ]
    )
    for summary in summaries:
        lines.append(
            f"| {summary['cluster_id']} | {summary['start_locus']}-{summary['end_locus']} | {summary['size']} | {summary['dominant_class']} | {summary['review_status']} | {summary['asta_status']} | {summary['genes']} |"
        )
    OUT_MD.write_text("\n".join(lines) + "\n")
    print(f"Wrote {OUT_TSV}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
