"""Cross-check this analysis against the independent AP3M1 one already on main.

genes/human/AP3M1/AP3M1-bioinformatics/ ran the same question for the AP-3 mu
subunit and committed a machine-readable results.json.  It derived its mu2 pocket
from the same structure (PDB 1BXX) at the same 4.5 A cutoff, but with a different
script, a different sequence panel (AP3M2, AP1M2 and mouse AP3M1 instead of AP5M1,
mouse Ap5m1 and Arabidopsis AP5M) and therefore a different alignment.

So the two runs are an independent replicate wherever they overlap.  This script
reports both the agreements and the disagreements rather than only the agreements;
a silent cross-check is worth nothing.

Exits non-zero if the shared, alignment-free part disagrees - the contact set
derived from the structure - since that would mean one of the two derivations is
wrong.  Alignment-dependent differences are reported, not failed: the two runs
aligned different sequence sets, so they are allowed to differ, and where they do
it marks a column whose assignment is not robust.
"""

from __future__ import annotations

import csv
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
AP3M1_JSON = HERE.parent.parent / "AP3M1" / "AP3M1-bioinformatics" / "results.json"
MAPPING = HERE / "mu_cargo_pocket_mapping.tsv"
POCKET = HERE / "mu2_cargo_pocket.tsv"

# Columns of mu_cargo_pocket_mapping.tsv <-> keys of results.json ap2m1_pocket_projected_onto
SHARED = {
    "AP1M1_Q9BXS5": "AP1M1_HUMAN",
    "AP3M1_Q9Y2T2": "AP3M1_HUMAN",
    "AP4M1_O00189": "AP4M1_HUMAN",
}


def main() -> int:
    if not AP3M1_JSON.exists():
        print(f"AP3M1 results not present at {AP3M1_JSON}; nothing to cross-check")
        return 0
    other = json.loads(AP3M1_JSON.read_text())
    mine_pocket = {int(r["mu2_position"]): r for r in csv.DictReader(POCKET.open(), delimiter="\t")}
    mine_map = {int(r["mu2_position"]): r for r in csv.DictReader(MAPPING.open(), delimiter="\t")}

    ok = True

    print(f"cutoff: mine 4.5 A (mu2_cargo_pocket.py), theirs {other['cutoff_angstrom']} A")
    if other["cutoff_angstrom"] != 4.5:
        ok = False
        print("  DISAGREE: different cutoffs, the contact sets are not comparable")

    theirs_1bxx = {r["resnum"]: r for r in other["contacts"]["1BXX"]["mu_residues"]}
    print(f"\n1BXX contact set (structure-derived, alignment-free): "
          f"mine {len(mine_pocket)} residues, theirs {len(theirs_1bxx)}")
    if set(mine_pocket) != set(theirs_1bxx):
        ok = False
        print(f"  DISAGREE: mine-only {sorted(set(mine_pocket) - set(theirs_1bxx))}, "
              f"theirs-only {sorted(set(theirs_1bxx) - set(mine_pocket))}")
    else:
        for pos in sorted(mine_pocket):
            m, t = mine_pocket[pos], theirs_1bxx[pos]
            same_aa = m["mu2_residue"] == t["aa"]
            same_d = abs(float(m["min_distance_A"]) - float(t["min_distance"])) < 0.02
            if not (same_aa and same_d):
                ok = False
                print(f"  DISAGREE at {pos}: mine {m['mu2_residue']} {m['min_distance_A']} A, "
                      f"theirs {t['aa']} {t['min_distance']} A")
        print("  AGREE: identical positions, residues and minimum distances")

    print("\nprojected pocket positions (alignment-dependent; different sequence panels):")
    for my_col, their_key in SHARED.items():
        theirs = other["ap2m1_pocket_projected_onto"][their_key]
        agree = diff = 0
        notes = []
        for pos in sorted(mine_map):
            m = mine_map[pos][my_col]
            t = theirs.get(str(pos)) or "gap"
            if m == t:
                agree += 1
            else:
                diff += 1
                notes.append(f"mu2 {pos}: mine {m}, theirs {t}")
        print(f"  {my_col:<14} vs {their_key:<12} {agree}/{agree+diff} identical assignments")
        for n in notes:
            print(f"      {n}")

    print("\nCROSS-CHECK " + ("PASSED" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
