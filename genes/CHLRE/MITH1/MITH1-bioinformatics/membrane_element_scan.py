#!/usr/bin/env python3
"""Does MITH1 carry a membrane-binding element distinguishable from its coiled-coil background?

The knowledge gap records that MITH1 co-pellets with membranes in a detergent-sensitive
way but has no transmembrane segment, which is the signature of peripheral association.
This script enumerates the three candidate peripheral mechanisms and scores each along
the sequence:

  1. amphipathic helix  -> hydrophobic moment (Eisenberg) per 18-residue window
  2. anionic-lipid-binding basic patch -> net charge per 18-residue window
  3. hydrophobic insertion loop -> mean Kyte-Doolittle hydropathy per 18-residue window

The point of the script is the CONTROL, not the ranking. ~50% of this protein is
annotated coiled-coil, and coiled coils have periodic hydrophobic faces, so they score
highly as "amphipathic helices" by construction. Every hit is therefore reported with
whether it falls inside an annotated COILED region, and each score distribution is
compared between coiled-coil and non-coiled-coil positions. A hit that is not separable
from the coiled-coil background is not evidence of a membrane-binding element.

Stdlib only, no network. Reads ../MITH1-uniprot.txt. Hardcodes no results.
"""
from __future__ import annotations
import math
import re
import sys
from pathlib import Path

KD = {"A":1.8,"R":-4.5,"N":-3.5,"D":-3.5,"C":2.5,"Q":-3.5,"E":-3.5,"G":-0.4,
      "H":-3.2,"I":4.5,"L":3.8,"K":-3.9,"M":1.9,"F":2.8,"P":-1.6,"S":-0.8,
      "T":-0.7,"W":-0.9,"Y":-1.3,"V":4.2}
# Eisenberg consensus hydrophobicity, used for the hydrophobic moment.
EIS = {"A":0.62,"R":-2.53,"N":-0.78,"D":-0.90,"C":0.29,"Q":-0.85,"E":-0.74,
       "G":0.48,"H":-0.40,"I":1.38,"L":1.06,"K":-1.50,"M":0.64,"F":1.19,
       "P":0.12,"S":-0.18,"T":-0.05,"W":0.81,"Y":0.26,"V":1.08}
POS, NEG = set("KR"), set("DE")
WIN = 18
DEG100 = math.radians(100.0)  # alpha-helical rise per residue


def read_record(path: Path):
    text = path.read_text()
    i = text.index("\nSQ ")
    seq = "".join(re.findall(r"^ {5}(.*)$", text[i:], re.M)).replace(" ", "")
    spans: dict[str, list[tuple[int, int]]] = {}
    for key, rng in re.findall(r"^FT   (\w+)\s+(\S+)$", text[:i], re.M):
        m = re.match(r"(\d+)\.\.(\d+)$", rng)
        if m:
            spans.setdefault(key, []).append((int(m.group(1)), int(m.group(2))))
    return seq, spans


def hydrophobic_moment(window: str) -> float:
    """Eisenberg muH per residue for an ideal alpha helix."""
    sx = sum(EIS.get(a, 0.0) * math.cos(k * DEG100) for k, a in enumerate(window))
    sy = sum(EIS.get(a, 0.0) * math.sin(k * DEG100) for k, a in enumerate(window))
    return math.hypot(sx, sy) / len(window)


def in_spans(pos: int, spans: list[tuple[int, int]]) -> bool:
    return any(s <= pos <= e for s, e in spans)


def summarize(name: str, scored: list[tuple[int, float]], coiled, top=5):
    """Print the top windows and the coiled vs non-coiled distributions."""
    ranked = sorted(scored, key=lambda kv: -kv[1])
    print(f"\n-- {name}: top {top} windows")
    for start, val in ranked[:top]:
        mid = start + WIN // 2
        tag = "INSIDE annotated coiled-coil" if in_spans(mid, coiled) else "outside coiled-coil"
        print(f"   {start}-{start+WIN-1}  {val:+.3f}  {tag}")
    cc = [v for s, v in scored if in_spans(s + WIN // 2, coiled)]
    nc = [v for s, v in scored if not in_spans(s + WIN // 2, coiled)]
    if cc and nc:
        mcc, mnc = sum(cc) / len(cc), sum(nc) / len(nc)
        best_cc, best_nc = max(cc), max(nc)
        print(f"   mean inside coiled-coil {mcc:+.3f} (n={len(cc)}), outside {mnc:+.3f} (n={len(nc)})")
        print(f"   best inside coiled-coil {best_cc:+.3f}, best outside {best_nc:+.3f}")
        verdict = ("no window outside the coiled-coil regions exceeds the best coiled-coil window"
                   if best_nc <= best_cc else
                   "at least one window outside the coiled-coil regions exceeds every coiled-coil window")
        print(f"   CONTROL: {verdict}")


def main() -> int:
    root = Path(__file__).resolve().parents[4]
    rec = root / "genes/CHLRE/MITH1/MITH1-uniprot.txt"
    if not rec.exists():
        print(f"ERROR: record not found at {rec}", file=sys.stderr)
        return 1
    seq, spans = read_record(rec)
    coiled = spans.get("COILED", [])
    disorder = spans.get("REGION", [])
    n = len(seq)
    print(f"record: {rec.relative_to(root)}")
    print(f"length: {n} residues")
    print(f"annotated COILED: {coiled}")
    print(f"annotated REGION (low-complexity/disordered): {disorder}")
    cc_cov = sum(e - s + 1 for s, e in coiled)
    print(f"coiled-coil coverage: {cc_cov} residues ({100*cc_cov/n:.1f}% of the protein)")
    print(f"no TRANSMEM feature in record: {'TRANSMEM' not in spans}")

    windows = [(i + 1, seq[i : i + WIN]) for i in range(n - WIN + 1)]
    summarize("amphipathic helix (Eisenberg hydrophobic moment)",
              [(s, hydrophobic_moment(w)) for s, w in windows], coiled)
    summarize("basic patch (net charge)",
              [(s, float(sum(1 for a in w if a in POS) - sum(1 for a in w if a in NEG)))
               for s, w in windows], coiled)
    summarize("hydrophobic loop (mean Kyte-Doolittle)",
              [(s, sum(KD.get(a, 0.0) for a in w) / WIN) for s, w in windows], coiled)

    print("\n-- interpretation limits")
    print("   These are sequence scores, not binding measurements. A high score is not")
    print("   evidence of lipid binding; a score indistinguishable from the coiled-coil")
    print("   background is evidence that the scan has found nothing specific. Neither")
    print("   outcome identifies a lipid, a leaflet, or a mechanism.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
