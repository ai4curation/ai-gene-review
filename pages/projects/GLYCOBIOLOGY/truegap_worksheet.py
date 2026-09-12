#!/usr/bin/env python3
"""Build an evidence worksheet for hand-review of the cazy2go TRUE_GAP safe rows.

For each mono-specific family whose single specific GO MF term is classified TRUE_GAP vs interpro2go
(InterPro silent on that activity branch), emit the evidence a reviewer needs to adjudicate whether
the mapping is a genuine, actionable interpro2go gap:

  family | GO id | GO label | EC(s) | n_members | n_interpro_sigs |
  interpro2go_MF_terms_for_family (what InterPro DOES give on the MF branch, if anything)

Writes a TSV to stdout (sorted by member count, descending).
"""
from __future__ import annotations

import sys

sys.path.insert(0, "projects/GLYCOBIOLOGY")
from build_cazy2go import GENERIC_PARENTS, load_ec2go  # noqa: E402
from compare_cazy_interpro import (  # noqa: E402
    cazy_go_for_family,
    load_cazy_ec_interpro,
    load_interpro2go,
)
from oaklib import get_adapter  # noqa: E402
from oaklib.datamodels.vocabulary import IS_A  # noqa: E402


def main():
    ec2go = load_ec2go()
    ipr2go = load_interpro2go()
    fam_ec, fam_ipr, fam_mem = load_cazy_ec_interpro()
    go = get_adapter("sqlite:obo:go")
    mf_root = "GO:0003674"
    _anc: dict[str, set[str]] = {}

    def anc(c):
        if c not in _anc:
            a = set(go.ancestors(c, predicates=[IS_A]))
            a.discard(c)
            _anc[c] = a
        return _anc[c]

    def is_mf(g):
        return g == mf_root or mf_root in anc(g)

    rows = []
    for fam in fam_ec:
        cg = cazy_go_for_family(fam_ec[fam], ec2go)
        if len(cg) != 1:
            continue
        go_id, _ = next(iter(cg.items()))
        if go_id in GENERIC_PARENTS:
            continue
        ipr_go = set()
        for ipr in fam_ipr[fam]:
            ipr_go |= ipr2go.get(ipr, set())
        if go_id in ipr_go or any(go_id in anc(i) for i in ipr_go):
            continue  # masked
        if any(i in anc(go_id) for i in ipr_go):
            continue  # altitude_gain, not true_gap
        # TRUE_GAP. What MF does InterPro give for this family (if any)?
        ipr_mf = sorted({i for i in ipr_go if is_mf(i)})
        ipr_mf_labels = "; ".join(f"{i} {go.label(i)}" for i in ipr_mf) or "(none)"
        ecs = sorted({e for e in fam_ec[fam] if any(g == go_id for g, _ in ec2go.get(e, []))})
        rows.append((
            len(fam_mem[fam]), fam, go_id, go.label(go_id),
            ",".join(ecs), len(fam_ipr[fam]), ipr_mf_labels,
        ))

    rows.sort(key=lambda r: -r[0])
    print("n_members\tfamily\tGO_id\tGO_label\tEC\tn_ipr_sigs\tinterpro2go_MF_terms_for_family")
    for r in rows:
        print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}\t{r[5]}\t{r[6]}")
    print(f"\n# {len(rows)} TRUE_GAP mono-specific families", file=sys.stderr)


if __name__ == "__main__":
    main()
