"""Inventory CACAO-assigned GO annotations against existing gene reviews.

Reads a QuickGO download of all annotations with assignedBy=CACAO, finds the
gene reviews in genes/ whose accession carries CACAO rows, and records the
review action given to each CACAO row (matched on term, evidence code and
reference). Writes projects/CACAO/cacao-inventory.yaml.

Usage:
    uv run python projects/CACAO/scripts/cacao_inventory.py [QUICKGO_TSV]

Fetch a fresh snapshot with:
    curl -H "Accept: text/tsv" \
      "https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch?assignedBy=CACAO"
"""

import collections
import csv
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_TSV = ROOT / "projects/CACAO/data/cacao-quickgo-2026-10-28.tsv"
OUT = ROOT / "projects/CACAO/cacao-inventory.yaml"
ID_RE = re.compile(r"^id:\s*['\"]?([A-Z0-9-]+)", re.M)


def load_cacao(path):
    by_acc = collections.defaultdict(list)
    with open(path) as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            by_acc[row["GENE PRODUCT ID"]].append(row)
    return by_acc


def index_reviews(accessions):
    found = {}
    for f in sorted(ROOT.glob("genes/*/*/*-ai-review.yaml")):
        with open(f) as fh:
            m = ID_RE.search(fh.read(2000))
        if m and m.group(1) in accessions:
            found.setdefault(m.group(1), []).append(f)
    return found


def row_actions(review_file, rows):
    doc = yaml.safe_load(review_file.read_text()) or {}
    anns = doc.get("existing_annotations") or []
    idx = collections.defaultdict(list)
    for a in anns:
        key = ((a.get("term") or {}).get("id"), a.get("evidence_type"), a.get("original_reference_id"))
        idx[key].append((a.get("review") or {}).get("action"))
    out = []
    for r in rows:
        key = (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"])
        acts = idx.get(key)
        out.append({
            "term": r["GO TERM"],
            "evidence": r["GO EVIDENCE CODE"],
            "reference": r["REFERENCE"],
            "qualifier": r["QUALIFIER"],
            "action": (acts[0] or "PENDING") if acts else "NOT_IN_REVIEW",
        })
    return doc.get("status"), out


def main():
    tsv = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_TSV
    by_acc = load_cacao(tsv)
    reviews = index_reviews(set(by_acc))
    total_rows = sum(len(v) for v in by_acc.values())
    taxa = collections.Counter(r["TAXON ID"] for v in by_acc.values() for r in v)
    action_counts = collections.Counter()
    genes = []
    for acc, files in sorted(reviews.items()):
        rows = by_acc[acc]
        f = files[0]
        status, acted = row_actions(f, rows)
        action_counts.update(a["action"] for a in acted)
        genes.append({
            "accession": acc,
            "symbol": rows[0]["SYMBOL"],
            "taxon": f"NCBITaxon:{rows[0]['TAXON ID']}",
            "review": str(f.relative_to(ROOT)),
            "review_status": status,
            "cacao_rows": acted,
        })
    unreviewed = collections.Counter()
    for acc, rows in by_acc.items():
        if acc not in reviews:
            unreviewed[rows[0]["TAXON ID"]] += 1
    summary = {
        "source": str(tsv.relative_to(ROOT)) if tsv.is_relative_to(ROOT) else str(tsv),
        "cacao_annotations": total_rows,
        "cacao_gene_products": len(by_acc),
        "gene_products_with_review": len(reviews),
        "cacao_rows_in_reviewed_genes": sum(len(g["cacao_rows"]) for g in genes),
        "actions": dict(action_counts.most_common()),
        "top_taxa_by_rows": {f"NCBITaxon:{t}": n for t, n in taxa.most_common(15)},
        "unreviewed_gene_products_by_taxon": {f"NCBITaxon:{t}": n for t, n in unreviewed.most_common(15)},
    }
    OUT.write_text(yaml.safe_dump({"summary": summary, "genes": genes}, sort_keys=False, width=100))
    print(yaml.safe_dump(summary, sort_keys=False))


if __name__ == "__main__":
    main()
