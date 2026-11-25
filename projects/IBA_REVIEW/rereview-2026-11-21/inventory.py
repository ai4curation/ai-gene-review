"""Inventory every IBA row a gene review marks REMOVE, placed on its PAINT tree.

For each such row this finds the PAINT node the pinned snapshot propagates the term
from, the family tree holding it, and what PAINT records for the term on the gene's
lineage, and writes ``inventory.tsv``. The ``status`` column is computed, not judged:

  LIVE_IBD            an IBD for the term sits on an ancestor and no loss blocks it
  PAINT_LOSS          PAINT has an IRD/IKR for the term between that IBD and the gene
  NOT_IN_SNAPSHOT     the pinned PAINT snapshot no longer propagates the term to the gene
  NEGATED             the reviewed row is itself a NOT annotation
  UNPLACED            the snapshot has the IBA but the gene is not a leaf of a tree we can read

    uv run python projects/IBA_REVIEW/rereview-2026-11-21/inventory.py
"""

from __future__ import annotations

import csv
import glob
import os
import sys
from pathlib import Path

from ai_gene_review.etl.panther_paint import (
    IBD_GAF_URL,
    LEAF_GAF_URL,
    TREEGRAFTER_URL,
    download_cached,
    invert_family_nodes,
    open_text,
    parse_ibd_gaf,
    parse_ptn_nodes,
    treegrafter_family_nodes,
)
from ai_gene_review.etl.panther_trees import ancestors_of, leaf_nodes_for, leaves_below, load_family
from ai_gene_review.validation.gene_paint_losses import is_loss, paint_cache_dir, panther_families
from ai_gene_review.yaml_utils import safe_load

HERE = Path(__file__).parent
FIELDS = [
    "gene_file", "accession", "symbol", "go_id", "go_label", "negated", "status", "family",
    "ibd_node", "ibd_date", "ibd_seeds", "target_is_seed", "clade_leaves", "clade_species",
    "tree_leaves", "losses_on_lineage", "other_reviewed_rows_same_term", "has_propagation_review",
    "cites_node_in_reason",
]


def main() -> None:
    cache = paint_cache_dir(Path(".cache/paint"))
    with open_text(download_cached(IBD_GAF_URL, cache)) as fh:
        ibd = parse_ibd_gaf(fh)
    with open_text(download_cached(TREEGRAFTER_URL, cache)) as fh:
        node_family = invert_family_nodes(treegrafter_family_nodes(fh))
    leaf_rows: dict[tuple[str, str, bool], list[str]] = {}
    with open_text(download_cached(LEAF_GAF_URL, cache)) as fh:
        for line in fh:
            c = line.split("\t")
            if line.startswith("!") or len(c) < 8:
                continue
            leaf_rows.setdefault((c[1], c[4], "NOT" in c[3]), []).extend(parse_ptn_nodes(c[7]))

    out = []
    for path in sorted(glob.glob("genes/*/*/*-ai-review.yaml")):
        text = Path(path).read_text()
        if "IBA" not in text or "REMOVE" not in text:
            continue
        doc = safe_load(text) or {}
        acc = str(doc.get("id", ""))
        up = path.replace("-ai-review.yaml", "-uniprot.txt")
        dr = panther_families(Path(up).read_text()) if os.path.exists(up) else []
        anns = doc.get("existing_annotations") or []
        for a in anns:
            rev = a.get("review") or {}
            if a.get("evidence_type") != "IBA" or rev.get("action") != "REMOVE":
                continue
            go, neg = a["term"]["id"], bool(a.get("negated"))
            snap_nodes = leaf_rows.get((acc, go, neg))
            fams = list(dict.fromkeys(dr + sorted(f for n in snap_nodes or [] for f in node_family.get(n, ()))))
            row = dict.fromkeys(FIELDS, "")
            row.update(
                gene_file=path, accession=acc, symbol=doc.get("gene_symbol"), go_id=go,
                go_label=a["term"].get("label"), negated=neg,
                other_reviewed_rows_same_term=";".join(
                    f"{b.get('evidence_type')}:{(b.get('review') or {}).get('action')}"
                    for b in anns if b is not a and (b.get("term") or {}).get("id") == go
                ),
                has_propagation_review=bool(rev.get("propagation_review")),
                cites_node_in_reason="PTN0" in (str(rev.get("reason")) + str(rev.get("summary"))),
            )
            status = "NOT_IN_SNAPSHOT" if snap_nodes is None else "UNPLACED"
            for fam in fams:
                tree = load_family(fam, Path(".cache/panther_trees"))
                leaves = leaf_nodes_for(tree, acc) if tree else []
                for leaf in leaves:
                    lineage = sorted(ancestors_of(tree, leaf), key=lambda n: len(leaves_below(tree, n)))
                    recs = [(n, r) for n in lineage for r in ibd.get(n, []) if r.go_id == go]
                    pos = [(n, r) for n, r in recs if not is_loss(r)]
                    loss = [(n, r) for n, r in recs if is_loss(r)]
                    row["family"], row["tree_leaves"] = fam, len(tree["leaves"])
                    row["losses_on_lineage"] = ";".join(f"{r.evidence}@{n}" for n, r in loss)
                    if not pos:
                        continue
                    n, r = pos[0]
                    lv = leaves_below(tree, n)
                    row.update(
                        ibd_node=n, ibd_date=r.date, ibd_seeds=len(r.seeds),
                        target_is_seed=any(s.endswith(":" + acc) for s in r.seeds),
                        clade_leaves=len(lv),
                        clade_species=len({tree["leaves"][x].get("organism") for x in lv}),
                    )
                    blocked = any(len(leaves_below(tree, ln)) <= len(lv) for ln, _ in loss)
                    if snap_nodes is not None:
                        status = "NEGATED" if neg else ("PAINT_LOSS" if blocked else "LIVE_IBD")
                    break
                if row["ibd_node"]:
                    break
            row["status"] = status
            out.append(row)
    with open(HERE / "inventory.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, FIELDS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    counts: dict[str, int] = {}
    for r in out:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print(len(out), "rows in", len({r["gene_file"] for r in out}), "gene reviews:", counts, file=sys.stderr)


if __name__ == "__main__":
    main()
