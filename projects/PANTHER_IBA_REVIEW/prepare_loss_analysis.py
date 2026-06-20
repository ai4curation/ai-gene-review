#!/usr/bin/env python3
"""Prepare a ready-to-run input bundle for reconstructing a PAINT function loss.

PANTHER's IKR/IRD loss annotations record only that a function was lost in a
clade; the key-residue rationale a curator saw in the alignment is never
published (see README). This script gathers what a bioinformatics agent needs to
**reconstruct** that rationale for one loss:

* ``seed_proteins`` - the experimentally characterized proteins establishing the
  function (with/from of the ancestral IBD record); the source of "key residues",
* ``loss_clade`` - members descending from the loss node (predicted to have lost
  it),
* ``retaining_clade`` - family members still annotated with the function.

The agent then fetches these sequences, aligns them (e.g. MAFFT), and compares
the columns at the characterized functional residues across the two clades.

Usage (run from the repo root):

    python3 projects/PANTHER_IBA_REVIEW/prepare_loss_analysis.py \
        --family PTHR10037 --loss-node PTN008692511 --go GO:0005891

Reads the loss event from family_function_losses.tsv when --go is omitted (the
first loss at that node for the family). Writes YAML to stdout, or to --output.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "src"))
from ai_gene_review.etl.panther_paint import (  # noqa: E402
    IBD_GAF_URL,
    LEAF_GAF_URL,
    assemble_loss_input,
    download_cached,
    family_member_ids,
    family_member_subfamilies,
    iter_leaf_rows,
    open_text,
    parse_ibd_gaf,
    parse_ptn_nodes,
)

PANTHER = REPO / "interpro" / "panther"


def _resolve_gain_record(ibd_index, ancestral_nodes, go_id):
    """Return the ancestral IBD record (seeds) for ``go_id``, if present."""
    for anc in ancestral_nodes:
        for rec in ibd_index.get(anc, []):
            if rec.go_id == go_id and not rec.negated:
                return rec
    return None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--family", required=True, help="PANTHER family id, e.g. PTHR10037")
    ap.add_argument("--loss-node", required=True, help="PTN node of the loss (IRD/IKR)")
    ap.add_argument("--go", help="GO id of the lost function (default: first at node)")
    ap.add_argument("--output", "-o", type=Path, help="Write YAML here (default: stdout)")
    args = ap.parse_args()

    entries = PANTHER / args.family / f"{args.family}-entries.csv"
    if not entries.exists():
        sys.exit(f"❌ {entries} not found (fetch the family first).")

    cache_dir = REPO / ".cache" / "panther"
    ibd_path = download_cached(IBD_GAF_URL, cache_dir)
    leaf_path = download_cached(LEAF_GAF_URL, cache_dir)
    with ibd_path.open() as fh:
        ibd_index = parse_ibd_gaf(fh)

    # Find the loss record on the requested node.
    loss_recs = [
        rec
        for rec in ibd_index.get(args.loss_node, [])
        if rec.negated or rec.evidence in ("IRD", "IKR")
    ]
    if args.go:
        loss_recs = [r for r in loss_recs if r.go_id == args.go]
    if not loss_recs:
        sys.exit(
            f"❌ No loss (NOT / IRD / IKR) for {args.go or '(any GO)'} "
            f"on {args.loss_node}."
        )
    loss = loss_recs[0]
    ancestral_nodes = parse_ptn_nodes("|".join(loss.seeds))
    gain = _resolve_gain_record(ibd_index, ancestral_nodes, loss.go_id)
    seed_proteins = gain.seeds if gain else []

    members = family_member_ids(entries)
    member_subfamily = family_member_subfamilies(entries)

    # One leaf-GAF pass restricted to this family: members under the loss node
    # (loss clade) and members still annotated with the GO (retaining clade).
    loss_members: set[str] = set()
    retaining_members: set[str] = set()
    with open_text(leaf_path) as fh:
        for acc, go, nodes in iter_leaf_rows(fh):
            if acc not in members:
                continue
            if args.loss_node in nodes:
                loss_members.add(acc)
            if go == loss.go_id:
                retaining_members.add(acc)

    bundle = assemble_loss_input(
        family=args.family,
        go_id=loss.go_id,
        aspect=loss.aspect,
        evidence=loss.evidence,
        ancestral_node=";".join(ancestral_nodes),
        loss_node=args.loss_node,
        seed_proteins=seed_proteins,
        loss_members=loss_members,
        retaining_members=retaining_members,
        member_subfamily=member_subfamily,
    )

    doc = {
        "task": (
            "Reconstruct the PAINT key-residue rationale for this function loss. "
            "Fetch sequences for seed_uniprot (function characterized here), "
            "loss_clade, and retaining_clade; build an MSA; identify the "
            "functional/catalytic residues from the seed proteins and compare "
            "those columns between the retaining and loss clades. Report whether "
            "the key residues are substituted/lost in the loss clade."
        ),
        "gain_confirmed": gain is not None,
        **bundle.to_dict(),
    }
    text = yaml.dump(doc, sort_keys=False, allow_unicode=True)
    if args.output:
        args.output.write_text(text)
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
