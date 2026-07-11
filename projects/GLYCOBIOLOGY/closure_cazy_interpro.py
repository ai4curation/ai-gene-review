#!/usr/bin/env python3
"""Closure-filter the cazy2go-vs-interpro2go marginal set (turn the upper bound into the truth).

compare_cazy_interpro.py computes the EXACT-MATCH marginal: cazy2go GO MF terms a family reaches
that interpro2go does not give verbatim. That is an upper bound, because a "marginal" specific term
may be an ancestor/descendant of a term interpro2go DOES supply. This script applies GO is_a closure
(oaklib, cached sqlite:obo:go) to partition each marginal (family, GO) pair:

  DESCENDANT_MASKED : interpro2go gives G itself or a DESCENDANT of G (same-or-more-specific)
                      -> NOT a contribution; drop (this shrinks the headline).
  ALTITUDE_GAIN     : interpro2go gives only a proper ANCESTOR of G (a generic parent)
                      -> cazy2go adds reaction-level specificity over a generic InterPro term.
  TRUE_GAP          : interpro2go gives nothing on G's is_a lineage for this family
                      -> genuinely new branch InterPro is silent on (strongest contribution).

"True marginal after closure" = ALTITUDE_GAIN + TRUE_GAP.

Usage:  uv run python projects/GLYCOBIOLOGY/closure_cazy_interpro.py
"""

from __future__ import annotations

import sys
from collections import Counter, defaultdict

sys.path.insert(0, "projects/GLYCOBIOLOGY")
from build_cazy2go import load_ec2go  # noqa: E402
from compare_cazy_interpro import (  # noqa: E402
    cazy_go_for_family,
    load_cazy_ec_interpro,
    load_interpro2go,
)

from oaklib import get_adapter  # noqa: E402
from oaklib.datamodels.vocabulary import IS_A  # noqa: E402


def main():
    print("Loading ec2go, interpro2go, UniProt, GO closure ...", file=sys.stderr)
    ec2go = load_ec2go()
    ipr2go = load_interpro2go()
    fam_ec, fam_ipr, fam_mem = load_cazy_ec_interpro()
    go = get_adapter("sqlite:obo:go")

    # cache proper-ancestor sets (is_a) on demand
    _anc: dict[str, set[str]] = {}

    def anc(curie: str) -> set[str]:
        if curie not in _anc:
            a = set(go.ancestors(curie, predicates=[IS_A]))
            a.discard(curie)
            _anc[curie] = a
        return _anc[curie]

    stats = Counter()
    fam_class: dict[str, Counter] = defaultdict(Counter)
    true_gap_rows, altitude_rows = [], []

    for fam in fam_ec:
        cazy_go = cazy_go_for_family(fam_ec[fam], ec2go)
        if not cazy_go:
            continue
        ipr_go = set()
        for ipr in fam_ipr[fam]:
            ipr_go |= ipr2go.get(ipr, set())
        for g, lbl in cazy_go.items():
            if g in ipr_go:
                stats["exact_masked"] += 1
                continue
            # descendant-masked: some interpro term i is a descendant of g  (g in ancestors(i))
            if any(g in anc(i) for i in ipr_go):
                stats["descendant_masked"] += 1
                fam_class[fam]["descendant_masked"] += 1
                continue
            # altitude-gain: some interpro term i is an ancestor of g
            g_anc = anc(g)
            if any(i in g_anc for i in ipr_go):
                stats["altitude_gain"] += 1
                fam_class[fam]["altitude_gain"] += 1
                altitude_rows.append((fam, len(fam_mem[fam]), g, lbl))
            else:
                stats["true_gap"] += 1
                fam_class[fam]["true_gap"] += 1
                true_gap_rows.append((fam, len(fam_mem[fam]), g, lbl))

    marginal = stats["descendant_masked"] + stats["altitude_gain"] + stats["true_gap"]
    print("\n========= closure-filtered cazy2go vs interpro2go =========")
    print(f"exact-match marginal pairs (upper bound)      : {marginal}")
    print(f"  DESCENDANT_MASKED (drop; InterPro >= specific): {stats['descendant_masked']} "
          f"({100*stats['descendant_masked']/marginal:.0f}%)")
    print(f"  ALTITUDE_GAIN (CAZy more specific than InterPro): {stats['altitude_gain']} "
          f"({100*stats['altitude_gain']/marginal:.0f}%)")
    print(f"  TRUE_GAP (InterPro silent on branch)          : {stats['true_gap']} "
          f"({100*stats['true_gap']/marginal:.0f}%)")
    print(f"TRUE marginal after closure (altitude+gap)    : {stats['altitude_gain']+stats['true_gap']}")

    fams_true_gap = sum(1 for f in fam_class if fam_class[f]["true_gap"])
    fams_any_gain = sum(1 for f in fam_class
                        if fam_class[f]["altitude_gain"] or fam_class[f]["true_gap"])
    fams_only_masked = sum(1 for f in fam_class
                           if not fam_class[f]["altitude_gain"] and not fam_class[f]["true_gap"])
    print(f"\nfamilies with >=1 TRUE_GAP term               : {fams_true_gap}")
    print(f"families with >=1 real gain (altitude or gap) : {fams_any_gain}")
    print(f"families whose entire marginal is descendant-masked (drop): {fams_only_masked}")

    print("\n-- TRUE_GAP examples (InterPro silent on this activity branch) --")
    seen = set()
    for fam, mem, g, lbl in sorted(true_gap_rows, key=lambda x: -x[1]):
        if fam in seen:
            continue
        seen.add(fam)
        print(f"  {fam:7} ({mem:3} members)  {g} {lbl[:52]}")
        if len(seen) >= 18:
            break


if __name__ == "__main__":
    main()
