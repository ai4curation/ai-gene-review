#!/usr/bin/env python3
"""Is this gene model's N-terminal extension a mitochondrial presequence?

The knowledge gap records that the model carries 14 residues ahead of the
E. coli-aligned core "with two arginines and no acidic residue", and the existing
RESULTS.md in this folder notes that no targeting-sequence predictor was ever run.
This script does not run one either -- TargetP and MitoFates are not installed and
there is no network -- but it computes the features such predictors rest on, and,
more importantly, it asks whether those features are distinguishable from chance in
a segment this short.

That control is the point. "No acidic residue in 14 residues" sounds like evidence
until the expectation is computed from the protein's own composition, at which point
it may be exactly what chance gives. The script computes:

  1. composition of the N-terminal extension vs the rest of the protein;
  2. the binomial probability of seeing zero acidic residues in a window that long,
     under the protein's own acidic frequency;
  3. the same for the observed basic count;
  4. amphipathicity (hydrophobic moment), which real cleavable presequences show;
  5. the position of arginines relative to the putative cleavage point, since the
     processing peptidase prefers an arginine at -2 or -3.

Stdlib only, no network. Hardcodes no results.
"""
from __future__ import annotations
import math
import re
import sys
from pathlib import Path

EIS = {"A":0.62,"R":-2.53,"N":-0.78,"D":-0.90,"C":0.29,"Q":-0.85,"E":-0.74,
       "G":0.48,"H":-0.40,"I":1.38,"L":1.06,"K":-1.50,"M":0.64,"F":1.19,
       "P":0.12,"S":-0.18,"T":-0.05,"W":0.81,"Y":0.26,"V":1.08}
POS, NEG = set("KR"), set("DE")
DEG100 = math.radians(100.0)
# Length of the N-terminal extension ahead of the E. coli-aligned core, as the
# knowledge gap states it. Declared here so the assumption is explicit and editable.
EXTENSION_LEN = 14


def read_seq(path: Path) -> str:
    text = path.read_text()
    i = text.index("\nSQ ")
    return "".join(re.findall(r"^ {5}(.*)$", text[i:], re.M)).replace(" ", "")


def binom_tail_zero(n: int, p: float) -> float:
    """P(zero successes in n trials)."""
    return (1.0 - p) ** n


def binom_at_least(n: int, k: int, p: float) -> float:
    """P(at least k successes in n trials)."""
    total = 0.0
    for i in range(k, n + 1):
        total += math.comb(n, i) * p**i * (1 - p) ** (n - i)
    return total


def moment(window: str) -> float:
    sx = sum(EIS.get(a, 0.0) * math.cos(j * DEG100) for j, a in enumerate(window))
    sy = sum(EIS.get(a, 0.0) * math.sin(j * DEG100) for j, a in enumerate(window))
    return math.hypot(sx, sy) / len(window)


def main() -> int:
    root = Path(__file__).resolve().parents[4]
    rec = root / "genes/9FUNG/SUCLG2__A0A9P6TY68/SUCLG2__A0A9P6TY68-uniprot.txt"
    if not rec.exists():
        print(f"ERROR: record not found at {rec}", file=sys.stderr)
        return 1
    seq = read_seq(rec)
    n = len(seq)
    ext, rest = seq[:EXTENSION_LEN], seq[EXTENSION_LEN:]
    print(f"record: {rec.relative_to(root)}")
    print(f"length: {n} residues")
    print(f"assumed N-terminal extension: 1-{EXTENSION_LEN} = {ext}")

    p_neg = sum(1 for a in seq if a in NEG) / n
    p_pos = sum(1 for a in seq if a in POS) / n
    print(f"\n-- background composition (whole protein)")
    print(f"   acidic D+E: {sum(1 for a in seq if a in NEG)}/{n} = {p_neg:.3f}")
    print(f"   basic  K+R: {sum(1 for a in seq if a in POS)}/{n} = {p_pos:.3f}")

    obs_neg = sum(1 for a in ext if a in NEG)
    obs_pos = sum(1 for a in ext if a in POS)
    print(f"\n-- the extension against that background")
    print(f"   observed acidic in extension: {obs_neg}")
    print(f"   P(zero acidic in {EXTENSION_LEN} residues) = {binom_tail_zero(EXTENSION_LEN, p_neg):.3f}")
    print(f"   observed basic in extension: {obs_pos}  ({' '.join(f'{a}{i+1}' for i, a in enumerate(ext) if a in POS)})")
    print(f"   P(>= {obs_pos} basic in {EXTENSION_LEN} residues) = {binom_at_least(EXTENSION_LEN, obs_pos, p_pos):.3f}")

    print(f"\n-- amphipathicity (cleavable presequences form amphipathic helices)")
    print(f"   hydrophobic moment of the extension: {moment(ext):+.3f}")
    win = 14
    allw = [moment(seq[i : i + win]) for i in range(n - win + 1)]
    better = sum(1 for v in allw if v >= moment(ext))
    print(f"   rank among all {win}-residue windows in this protein: {better}/{len(allw)}"
          f"  (percentile {100*(1-better/len(allw)):.1f})")

    print(f"\n-- arginine position relative to the putative cleavage point")
    print(f"   cleavage assumed between {EXTENSION_LEN} and {EXTENSION_LEN+1}")
    for i, a in enumerate(ext, start=1):
        if a == "R":
            print(f"   R{i} is at position -{EXTENSION_LEN - i + 1} relative to the cut")
    print("   (mitochondrial processing peptidase prefers Arg at -2 or -3)")

    print(f"\n-- interpretation limits")
    print("   No targeting-sequence predictor was run; these are the underlying")
    print("   features, not a prediction. The sequence is from a preliminary WGS")
    print("   entry, so the start codon itself is unverified: if the model's start is")
    print("   wrong, the extension analysed here is not the real N-terminus.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
