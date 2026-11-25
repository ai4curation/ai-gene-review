"""Explain the NOT_IN_SNAPSHOT rows of inventory.tsv and write batches/withdrawn-upstream.yaml.

For a row whose IBA the pinned PAINT snapshot no longer propagates, this reports why,
from the tree alone: a PAINT loss on the lineage, no IBD for the term on any ancestor,
or the gene not being a leaf of its family tree. No judgement is made here.

    uv run python projects/IBA_REVIEW/rereview-2026-11-21/withdrawn.py
"""

from __future__ import annotations

import csv
from pathlib import Path

import yaml

from ai_gene_review.etl.panther_paint import IBD_GAF_URL, download_cached, open_text, parse_ibd_gaf
from ai_gene_review.etl.panther_trees import ancestors_of, leaf_nodes_for, leaves_below, load_family
from ai_gene_review.validation.gene_paint_losses import is_loss, paint_cache_dir, panther_families

HERE = Path(__file__).parent


def main() -> None:
    with open_text(download_cached(IBD_GAF_URL, paint_cache_dir(Path(".cache/paint")))) as fh:
        ibd = parse_ibd_gaf(fh)
    genes: dict[str, list[dict]] = {}
    for r in csv.DictReader(open(HERE / "inventory.tsv"), delimiter="\t"):
        if r["status"] != "NOT_IN_SNAPSHOT":
            continue
        up = Path(r["gene_file"].replace("-ai-review.yaml", "-uniprot.txt"))
        fams = panther_families(up.read_text()) if up.exists() else []
        facts, cause = [], "NO_FAMILY_ON_UNIPROT_RECORD"
        for fam in fams:
            tree = load_family(fam, Path(".cache/panther_trees"))
            leaves = leaf_nodes_for(tree, r["accession"]) if tree else []
            if not leaves:
                cause = "GENE_NOT_A_LEAF_OF_FAMILY_TREE"
                facts.append(f"{r['accession']} is not a leaf of the {fam} tree ({len(tree['leaves']) if tree else 0} leaves).")
                continue
            lineage = sorted(ancestors_of(tree, leaves[0]), key=lambda n: len(leaves_below(tree, n)))
            recs = [(n, x) for n in lineage for x in ibd.get(n, []) if x.go_id == r["go_id"]]
            loss = [(n, x) for n, x in recs if is_loss(x)]
            pos = [(n, x) for n, x in recs if not is_loss(x)]
            if loss:
                cause = "PAINT_LOSS_ON_LINEAGE"
                facts += [f"{x.evidence} loss for the term at {n} ({len(leaves_below(tree, n))} leaves, dated {x.date}) in {fam}." for n, x in loss]
                facts += [f"IBD for the term at {n} ({len(leaves_below(tree, n))} leaves)." for n, x in pos]
            else:
                cause = "NO_IBD_FOR_TERM_ON_LINEAGE"
                facts.append(f"No PAINT record for the term on any of the {len(lineage)} nodes above {r['accession']} in {fam}.")
            break
        genes.setdefault(r["gene_file"], []).append(
            {
                "go_id": r["go_id"],
                "go_label": r["go_label"],
                "family": ", ".join(fams),
                "snapshot_cause": cause,
                "tree_reading": " ".join(facts) or "The UniProt record names no PANTHER family.",
                "verdict": "REMOVE_UPHELD",
                "ground": "WITHDRAWN_UPSTREAM",
                "paint_fix": {"paint_action": "NONE"},
                "review_edited": False,
            }
        )
    doc = {
        "scope": "Rows whose IBA the pinned PAINT snapshot no longer propagates to the gene. "
        "PAINT has already made the change the REMOVE asked for, so the action stands and no fix is requested. "
        "snapshot_cause and tree_reading are computed by withdrawn.py.",
        "genes": [{"gene_file": g, "rows": rows} for g, rows in genes.items()],
    }
    out = HERE / "batches" / "withdrawn-upstream.yaml"
    out.write_text(yaml.safe_dump(doc, sort_keys=False, width=100, allow_unicode=True))
    counts: dict[str, int] = {}
    for rows in genes.values():
        for x in rows:
            counts[x["snapshot_cause"]] = counts.get(x["snapshot_cause"], 0) + 1
    print(counts)


if __name__ == "__main__":
    main()
