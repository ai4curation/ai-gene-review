#!/usr/bin/env python3
"""Compare how GO annotation sources use "regulation of X" terms and extensions.

For each GAF (non-NOT, biological_process rows):

- share of BP rows that are regulation terms (a direct ``regulates`` edge, see
  ``regulation_triage.Ontology``);
- share of regulation rows whose target is gene expression / transcription
  (an is_a/part_of descendant of GO:0010467 gene expression);
- regulation rows made to a gene with DNA-binding TF activity (GO:0003700) in
  the same GAF, split by whether the regulated process is transcriptional;
- extension (GAF column 16) use on regulation rows, and how often an extension
  names a gene product (the "which gene does it regulate" information);
- for TF molecular-function rows, how often an extension names a target gene;
- evidence: share of regulation rows supported only by perturbation codes.

Usage::

    python projects/REGULATION_CONSISTENCY/regulation_by_species.py \
        --obo go.obo goa_human.gaf.gz pombase.gaf.gz sgd.gaf.gz ... \
        --out projects/REGULATION_CONSISTENCY/results/regulation_by_species.yaml
"""

from __future__ import annotations

import argparse
import gzip
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml
from regulation_triage import PERTURBATION, Ontology

GENE_EXPRESSION = "GO:0010467"
TF_ACTIVITY = "GO:0003700"
# Extension fillers that are not gene products.
NON_GENE_PREFIXES = {
    "GO", "CL", "UBERON", "CHEBI", "PO", "WBbt", "WBls", "FBbt", "FBdv", "EMAPA",
    "SO", "PR", "NCBITaxon", "EMAP", "MA", "ZFA", "BTO", "UBERON", "PATO", "TAIR",
}  # fmt: skip
EXT_TERM = re.compile(r"([A-Za-z_]+)\(([^()]+)\)")


def gene_filler(value: str) -> bool:
    """True when an extension filler is a gene product, not an ontology class.

    >>> gene_filler("PomBase:SPBC12D12.01"), gene_filler("GO:0005637")
    (True, False)
    """
    prefix = value.split(":", 1)[0]
    return prefix not in NON_GENE_PREFIXES or value.startswith("TAIR:locus")


def frac(n: int, d: int) -> float:
    return round(n / d, 3) if d else 0.0


def analyse(gaf: Path, onto: Ontology, expr: set[str], tf_terms: set[str]) -> dict:
    bp_rows = reg_rows = 0
    c: Counter = Counter()
    ext_rel: Counter = Counter()
    gene_rel: Counter = Counter()
    rows_by_gene: dict[str, list] = defaultdict(list)
    tf_genes: set[str] = set()
    tf_mf_rows = tf_mf_gene_ext = 0
    with gzip.open(gaf, "rt", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            f = line.rstrip("\n").split("\t")
            if len(f) < 15 or "NOT" in f[3].split("|"):
                continue
            term = onto.canon(f[4])
            gene = f[1]
            ext = f[15] if len(f) > 15 else ""
            has_gene_ext = any(gene_filler(v) for _, v in EXT_TERM.findall(ext))
            if term in tf_terms:
                tf_genes.add(gene)
                tf_mf_rows += 1
                tf_mf_gene_ext += has_gene_ext
            if onto.namespace.get(term) != "biological_process":
                continue
            bp_rows += 1
            if not onto.is_reg(term):
                continue
            reg_rows += 1
            transcriptional = any(t in expr for _, t in onto.reg_targets(term))
            rows_by_gene[gene].append((transcriptional, f[6], f[3], ext, has_gene_ext))
    for gene, rows in rows_by_gene.items():
        tf = gene in tf_genes
        for transcriptional, ev, qual, ext, has_gene_ext in rows:
            c["transcriptional"] += transcriptional
            c["perturbation_only"] += ev in PERTURBATION
            c["upstream_qualifier"] += qual.startswith("acts_upstream")
            if ext:
                c["with_extension"] += 1
                for rel, val in EXT_TERM.findall(ext):
                    ext_rel[rel] += 1
                    if gene_filler(val):
                        gene_rel[rel] += 1
            c["gene_extension"] += has_gene_ext
            if tf:
                c["tf_rows"] += 1
                c["tf_transcriptional"] += transcriptional
                c["tf_nontranscriptional_gene_ext"] += (
                    not transcriptional
                ) and has_gene_ext
                c["tf_transcriptional_gene_ext"] += transcriptional and has_gene_ext
    tf_tx = c["tf_transcriptional"]
    tf_nontx = c["tf_rows"] - tf_tx
    return {
        "bp_rows": bp_rows,
        "regulation_rows": reg_rows,
        "regulation_share_of_bp": frac(reg_rows, bp_rows),
        "genes_with_regulation_rows": len(rows_by_gene),
        "transcriptional_share": frac(c["transcriptional"], reg_rows),
        "perturbation_only_share": frac(c["perturbation_only"], reg_rows),
        "acts_upstream_qualifier_share": frac(c["upstream_qualifier"], reg_rows),
        "with_any_extension_share": frac(c["with_extension"], reg_rows),
        "with_gene_extension_share": frac(c["gene_extension"], reg_rows),
        "extension_relations": dict(ext_rel.most_common(8)),
        "gene_filler_relations": dict(gene_rel.most_common(6)),
        "tf_genes": len(tf_genes),
        "regulation_rows_on_tf_genes_share": frac(c["tf_rows"], reg_rows),
        "tf_regulation_rows_transcriptional": tf_tx,
        "tf_regulation_rows_nontranscriptional": tf_nontx,
        "tf_transcriptional_rows_with_gene_extension_share": frac(
            c["tf_transcriptional_gene_ext"], tf_tx
        ),
        "tf_nontranscriptional_rows_with_gene_extension_share": frac(
            c["tf_nontranscriptional_gene_ext"], tf_nontx
        ),
        "tf_activity_mf_rows": tf_mf_rows,
        "tf_activity_mf_rows_with_gene_extension_share": frac(
            tf_mf_gene_ext, tf_mf_rows
        ),
    }


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("gafs", nargs="+", type=Path)
    ap.add_argument("--obo", required=True, type=Path)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()
    onto = Ontology.from_obo(args.obo)
    expr = {t for t in onto.name if GENE_EXPRESSION in onto.ancestors(t)}
    tf_terms = {t for t in onto.name if TF_ACTIVITY in onto.ancestors(t)}
    out = {}
    for gaf in args.gafs:
        out[gaf.name.split(".")[0]] = analyse(gaf, onto, expr, tf_terms)
    text = yaml.safe_dump(out, sort_keys=False, width=100)
    print(text)
    if args.out:
        args.out.write_text(text)


if __name__ == "__main__":
    main()
