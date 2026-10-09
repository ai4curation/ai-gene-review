# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
"""Report GTEx v8 median expression (TPM) for a target locus and its parent.

Resolves the versioned GENCODE v26 id via the GTEx reference endpoint, then
queries median gene expression across tissues. Prints the top tissues and the
maximum median TPM, or states that GTEx returned no expression rows.

Usage:
    uv run gtex_expression.py ENSG_TARGET [ENSG_PARENT ...]
"""
import sys

import requests

API = "https://gtexportal.org/api/v2"


def versioned(gene):
    r = requests.get(f"{API}/reference/gene",
                     params={"geneId": gene, "gencodeVersion": "v26",
                             "genomeBuild": "GRCh38/hg38"}, timeout=60)
    r.raise_for_status()
    d = r.json()["data"]
    return (d[0]["gencodeId"], d[0]["geneSymbol"], d[0]["geneType"]) if d else (None, None, None)


def median_expr(gid):
    r = requests.get(f"{API}/expression/medianGeneExpression",
                     params={"gencodeId": gid, "datasetId": "gtex_v8"}, timeout=60)
    r.raise_for_status()
    return r.json().get("data", [])


for gene in sys.argv[1:]:
    gid, sym, gtype = versioned(gene)
    if not gid:
        print(f"{gene}: not found in GTEx GENCODE v26 reference")
        continue
    rows = sorted(median_expr(gid), key=lambda x: -x["median"])
    print(f"{gene} -> {gid} {sym} ({gtype}); tissues with data: {len(rows)}")
    if not rows:
        print("  GTEx returned no median-expression rows for this gene")
        continue
    print(f"  max median TPM {rows[0]['median']:.3f} ({rows[0]['tissueSiteDetailId']})")
    for x in rows[:5]:
        print(f"    {x['tissueSiteDetailId']:45s} {x['median']:.3f}")
