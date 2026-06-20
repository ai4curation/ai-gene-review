#!/usr/bin/env python3
"""Pull PANTHER PTN node-level (PAINT) annotations for the reviewed genes.

Where ``extract_iba_propagation.py`` reconstructs each *leaf* IBA's source node
from the gene's GOA ``with/from`` field, this script goes to the *node* itself:
for every ancestral PTN node an IBA propagated from, it pulls the complete set
of node-level annotations from PANTHER's ``IBD.gaf`` (the IBD/IRD/IKR layer).

This surfaces three things the leaf view cannot:

* the **canonical seed set** curated at the node (typically far richer than the
  handful of seeds echoed into any single leaf's ``with/from``);
* **loss annotations** (IRD/IKR ``NOT``) made at the node, i.e. functions a
  subfamily was curated to have *lost*;
* node annotations that **did not propagate** to our gene (``propagated``=False):
  either candidate missing annotations or functions lost on our lineage.

The node-level data comes from a cached ``IBD.gaf`` (downloaded on demand via
``ai_gene_review.etl.panther_paint``). Nothing is hardcoded.

Run from the repo root:

    python3 projects/PANTHER_IBA_REVIEW/extract_node_annotations.py
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

# Reuse the gene list + GOA/review helpers from the sibling extractor.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_iba_propagation import (  # noqa: E402
    GENES,
    IBA_REF,
    gene_accession,
    iba_actions,
    parse_withfrom,
)

# Reuse the PAINT ingest engine for the node-level GAF.
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from ai_gene_review.etl.panther_paint import (  # noqa: E402
    IBD_GAF_URL,
    download_cached,
    parse_ibd_gaf,
)

REPO = Path(__file__).resolve().parents[2]


def main() -> None:
    cache_dir = REPO / ".cache" / "panther"
    ibd_path = download_cached(IBD_GAF_URL, cache_dir)
    with ibd_path.open() as fh:
        ibd_index = parse_ibd_gaf(fh)

    rows = []
    for gene in GENES:
        gdir = REPO / "genes" / "SCHPO" / gene
        review = gdir / f"{gene}-ai-review.yaml"
        goa = gdir / f"{gene}-goa.tsv"
        if not goa.exists():
            print(f"WARN missing {goa}", file=sys.stderr)
            continue
        acc = gene_accession(review)
        actions = iba_actions(review)

        # Map node -> set of GO ids that actually propagated to this gene (as IBA),
        # so we can mark which node annotations reached the gene.
        propagated: dict[str, set[str]] = {}
        for line in goa.read_text().splitlines():
            f = line.split("\t")
            if len(f) < 11 or IBA_REF not in line:
                continue
            go_id, withfrom = f[4], f[10]
            nodes, _ = parse_withfrom(withfrom)
            for node in nodes:
                propagated.setdefault(node, set()).add(go_id)

        for node, gene_gos in sorted(propagated.items()):
            for rec in ibd_index.get(node, []):
                did_propagate = rec.go_id in gene_gos
                rows.append(
                    {
                        "gene": gene,
                        "acc": acc or "",
                        "node": node,
                        "go_id": rec.go_id,
                        "aspect": rec.aspect,
                        "evidence": rec.evidence,
                        "negated": "true" if rec.negated else "false",
                        "n_seeds": len(rec.seeds),
                        "propagated": "true" if did_propagate else "false",
                        "our_action": actions.get(rec.go_id, "-") if did_propagate else "-",
                        "node_date": rec.date,
                    }
                )

    out = REPO / "projects" / "PANTHER_IBA_REVIEW" / "node_annotations.tsv"
    cols = list(rows[0].keys())
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    # Console summary
    n = len(rows)
    losses = [r for r in rows if r["negated"] == "true"]
    not_prop = [r for r in rows if r["propagated"] == "false"]
    print(f"Node-level annotations pulled: {n}")
    print(f"  distinct nodes: {len({r['node'] for r in rows})}")
    print(f"  loss annotations (IRD/IKR, NOT): {len(losses)}")
    print(f"  node annotations NOT propagated to the gene: {len(not_prop)}")
    if losses:
        print("\nLoss (IRD/IKR) annotations on nodes our genes derive from:")
        for r in losses:
            print(f"  {r['gene']:7s} {r['node']} {r['go_id']} [{r['evidence']}]")
    print(f"\nWrote {out.relative_to(REPO)}")


if __name__ == "__main__":
    main()
