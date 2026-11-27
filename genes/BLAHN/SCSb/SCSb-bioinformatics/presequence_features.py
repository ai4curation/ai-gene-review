#!/usr/bin/env python3
"""Is the curated presequence of Blastocystis SCS beta distinguishable from chance?

The knowledge gap cites, as established, "a predicted N-terminal presequence with
arginine two residues before the predicted cleavage site". A companion analysis on the
Mortierellomycota SUCLG2-type beta subunit
(genes/9FUNG/SUCLG2__A0A9P6TY68/SUCLG2__A0A9P6TY68-bioinformatics/) showed that
observations of exactly this shape can be chance-level once the expectation is computed
from the protein's own composition, so the claim is worth testing here rather than
inherited.

This case differs from that one in a way that matters: the cleavage point here is
CURATED in the record (TRANSIT 1..18, CHAIN 19..318), not assumed from an alignment.
The arginine-at-minus-two observation is therefore not conditional on a guessed cut,
which was the caveat that weakened the equivalent claim for the beta subunit.

Computes, for the curated transit peptide:
  1. composition against the protein's own background, with binomial expectations;
  2. amphipathicity (hydrophobic moment), which cleavable presequences display;
  3. the identity and position of every basic residue relative to the curated cut.

Stdlib only, no network. Hardcodes no results; the transit-peptide boundary is read
from the record's own feature table rather than being typed in.
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


def read_record(path: Path):
    text = path.read_text()
    i = text.index("\nSQ ")
    seq = "".join(re.findall(r"^ {5}(.*)$", text[i:], re.M)).replace(" ", "")
    spans: dict[str, tuple[int, int]] = {}
    for m in re.finditer(r"^FT   (\w+)\s+(\d+)\.\.(\d+)$", text[:i], re.M):
        spans.setdefault(m.group(1), (int(m.group(2)), int(m.group(3))))
    return seq, spans


def binom_at_least(n: int, k: int, p: float) -> float:
    return sum(math.comb(n, i) * p**i * (1 - p) ** (n - i) for i in range(k, n + 1))


def moment(w: str) -> float:
    sx = sum(EIS.get(a, 0.0) * math.cos(j * DEG100) for j, a in enumerate(w))
    sy = sum(EIS.get(a, 0.0) * math.sin(j * DEG100) for j, a in enumerate(w))
    return math.hypot(sx, sy) / len(w)


def main() -> int:
    root = Path(__file__).resolve().parents[4]
    rec = root / "genes/BLAHN/SCSb/SCSb-uniprot.txt"
    if not rec.exists():
        print(f"ERROR: record not found at {rec}", file=sys.stderr)
        return 1
    seq, spans = read_record(rec)
    n = len(seq)
    if "TRANSIT" not in spans:
        print("ERROR: no curated TRANSIT feature in record; this script requires one",
              file=sys.stderr)
        return 1
    t_start, t_end = spans["TRANSIT"]
    pre = seq[t_start - 1 : t_end]
    print(f"record: {rec.relative_to(root)}")
    print(f"length: {n} residues")
    print(f"curated features: {spans}")
    print(f"curated transit peptide {t_start}-{t_end} ({len(pre)} aa): {pre}")
    print(f"cut is curated, not assumed: cleavage between {t_end} and {t_end+1}")

    p_neg = sum(1 for a in seq if a in NEG) / n
    p_pos = sum(1 for a in seq if a in POS) / n
    obs_neg = sum(1 for a in pre if a in NEG)
    obs_pos = sum(1 for a in pre if a in POS)
    L = len(pre)
    print(f"\n-- composition against the protein's own background")
    print(f"   background acidic {p_neg:.3f}, basic {p_pos:.3f}")
    print(f"   observed in presequence: acidic {obs_neg}, basic {obs_pos}")
    print(f"   P(zero acidic in {L}) = {(1-p_neg)**L:.4f}")
    print(f"   P(>= {obs_pos} basic in {L}) = {binom_at_least(L, obs_pos, p_pos):.4f}")

    print(f"\n-- amphipathicity")
    mu = moment(pre)
    allw = [moment(seq[i : i + L]) for i in range(n - L + 1)]
    better = sum(1 for v in allw if v >= mu)
    print(f"   presequence hydrophobic moment {mu:+.3f}")
    print(f"   rank among all {L}-residue windows: {better}/{len(allw)}"
          f"  (percentile {100*(1-better/len(allw)):.1f})")

    print(f"\n-- basic residues relative to the curated cut")
    for i, a in enumerate(pre, start=1):
        if a in POS:
            print(f"   {a}{i} at position -{t_end - i + 1}")
    print("   (mitochondrial processing peptidase prefers Arg at -2 or -3)")

    print(f"\n-- interpretation limits")
    print("   No targeting-sequence predictor was run; these are the features such")
    print("   predictors rest on. A presequence that looks unremarkable by composition")
    print("   may still be a real one, since the record's TRANSIT assignment is itself")
    print("   curated evidence; what these numbers test is whether the composition")
    print("   observations quoted in the knowledge gap add anything to it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
