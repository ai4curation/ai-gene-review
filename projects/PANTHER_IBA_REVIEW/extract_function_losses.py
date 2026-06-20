#!/usr/bin/env python3
"""Flag PANTHER families where a *subfamily lost a function* (PAINT IRD/IKR).

PAINT curators record function *loss* at internal nodes with IRD (Inferred from
Reviewed Descendant) / IKR (Inferred from Key Residues) evidence and a ``NOT``
qualifier: the ancestral node had the function (IBD), a descendant clade lost it.
These are the strongest within-family neo-/sub-functionalization signals, and a
direct curation guard: **do not propagate the ancestral function to the members
under the loss node**.

For every cached family (``interpro/panther/<FAM>/<FAM>-entries.csv``) this report
pairs each loss with the ancestral gain node, checks the loss is within the
family's PTN node set, and attributes it to the family **subfamilies** whose
members descend from the loss node (resolved from the leaf IBA GAF + the member
tables). Output:

    projects/PANTHER_IBA_REVIEW/family_function_losses.tsv

Nothing is hardcoded; all data derives from the cached PAINT GAFs and the
``interpro/panther/`` member tables. Run from the repo root:

    python3 projects/PANTHER_IBA_REVIEW/extract_function_losses.py
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "src"))
from ai_gene_review.etl.panther_paint import (  # noqa: E402
    IBD_GAF_URL,
    LEAF_GAF_URL,
    _COL_OBJECT_ID,
    _COL_WITH_FROM,
    _open_text,
    download_cached,
    family_member_subfamilies,
    iter_losses,
    load_all_family_members,
    parse_ibd_gaf,
    parse_ptn_nodes,
)

PANTHER = REPO / "interpro" / "panther"


def main() -> None:
    cache_dir = REPO / ".cache" / "panther"
    ibd_path = download_cached(IBD_GAF_URL, cache_dir)
    leaf_path = download_cached(LEAF_GAF_URL, cache_dir)

    with ibd_path.open() as fh:
        ibd_index = parse_ibd_gaf(fh)

    # Pair every loss with its ancestral (gain) node(s).
    losses = list(iter_losses(ibd_index))
    loss_nodes = {rec.node for rec, _ in losses}

    # Family membership + per-member subfamily.
    member_to_families, family_dirs = load_all_family_members(PANTHER)
    family_members: dict[str, set[str]] = {f: set() for f in family_dirs}
    for member, fams in member_to_families.items():
        for f in fams:
            family_members[f].add(member)
    member_subfamily: dict[str, str] = {}
    for family, fdir in family_dirs.items():
        for acc, sf in family_member_subfamilies(
            fdir / f"{family}-entries.csv"
        ).items():
            if sf:
                member_subfamily[acc] = sf

    # Single leaf-GAF pass: family node sets + which members descend from a loss node.
    family_nodes: dict[str, set[str]] = {}
    loss_node_members: dict[str, set[str]] = {}
    with _open_text(leaf_path) as fh:
        for line in fh:
            if not line or line.startswith("!"):
                continue
            cols = line.split("\t")
            if len(cols) <= _COL_WITH_FROM:
                continue
            acc = cols[_COL_OBJECT_ID]
            fams = member_to_families.get(acc)
            if not fams:
                continue
            nodes = parse_ptn_nodes(cols[_COL_WITH_FROM])
            for n in nodes:
                for f in fams:
                    family_nodes.setdefault(f, set()).add(n)
                if n in loss_nodes:
                    loss_node_members.setdefault(n, set()).add(acc)

    rows = []
    for rec, ancestors in losses:
        anc_set = set(ancestors)
        # Which cached families is this loss relevant to? (gain or loss node in F)
        candidate_families = set()
        for f, nodes in family_nodes.items():
            if rec.node in nodes or anc_set & nodes:
                candidate_families.add(f)
        descendants = loss_node_members.get(rec.node, set())
        # Confirm the ancestral node actually carries this GO as a gain (IBD).
        gain_confirmed = any(
            r.go_id == rec.go_id and not r.negated
            for anc in ancestors
            for r in ibd_index.get(anc, [])
        )
        for family in sorted(candidate_families):
            affected = descendants & family_members.get(family, set())
            subfamilies = sorted({member_subfamily[m] for m in affected if m in member_subfamily})
            rows.append(
                {
                    "family": family,
                    "go_id": rec.go_id,
                    "aspect": rec.aspect,
                    "evidence": rec.evidence,
                    "ancestral_node": ";".join(ancestors),
                    "loss_node": rec.node,
                    "gain_confirmed": "true" if gain_confirmed else "false",
                    "n_members_affected": len(affected),
                    "n_subfamilies": len(subfamilies),
                    "subfamilies": ";".join(subfamilies),
                    "loss_date": rec.date,
                }
            )

    rows.sort(key=lambda r: (r["family"], r["go_id"]))
    out = REPO / "projects" / "PANTHER_IBA_REVIEW" / "family_function_losses.tsv"
    cols = list(rows[0].keys())
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    families_with_losses = {r["family"] for r in rows}
    attributed = [r for r in rows if r["n_subfamilies"]]
    print(f"Loss (IRD/IKR) annotations globally: {len(losses)}")
    print(f"Within-family loss findings: {len(rows)}")
    print(f"  cached families with >=1 within-family loss: {len(families_with_losses)}")
    print(f"  findings attributed to >=1 subfamily: {len(attributed)}")
    print(f"\nWrote {out.relative_to(REPO)}")


if __name__ == "__main__":
    main()
