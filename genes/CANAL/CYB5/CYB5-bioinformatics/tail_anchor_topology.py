#!/usr/bin/env python3
"""Topology analysis of Candida albicans Cyb5 from its local UniProt record.

Addresses the knowledge gap "the subcellular localization and membrane topology of
C. albicans Cyb5 have not been directly measured" by computing, rather than
asserting, the three sequence-level quantities that constrain the topology:

1. the position and hydrophobicity of the C-terminal hydrophobic segment;
2. whether its length and flanking polarity fit a tail anchor (inserts without
   crossing) rather than a conventional transmembrane helix;
3. where the heme-ligating histidines sit relative to that segment, which fixes
   which face of the membrane the functional domain occupies.

Stdlib only, no network. Reads genes/CANAL/CYB5/CYB5-uniprot.txt. Prints every
number it derives; nothing is hardcoded. This is a prediction from sequence and is
NOT a measurement of localisation.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

# Kyte & Doolittle (1982) hydropathy index.
KD = {
    "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5,
    "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8,
    "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2,
}
POSITIVE = set("KR")
NEGATIVE = set("DE")


def read_record(path: Path) -> tuple[str, dict[str, list[tuple[int, int]]]]:
    """Return (sequence, features) from a UniProt flat file."""
    text = path.read_text()
    idx = text.index("\nSQ ")
    seq = "".join(re.findall(r"^ {5}(.*)$", text[idx:], re.M)).replace(" ", "")
    feats: dict[str, list[tuple[int, int]]] = {}
    for key, rng in re.findall(r"^FT   (\w+)\s+(\S+)$", text[:idx], re.M):
        m = re.match(r"(\d+)\.\.(\d+)$", rng)
        if m:
            span = (int(m.group(1)), int(m.group(2)))
        elif rng.isdigit():
            span = (int(rng), int(rng))
        else:
            continue
        feats.setdefault(key, []).append(span)
    return seq, feats


def hydropathy_windows(seq: str, window: int) -> list[tuple[int, float]]:
    """Mean KD hydropathy per window, keyed by 1-based window start."""
    out = []
    for i in range(len(seq) - window + 1):
        vals = [KD[a] for a in seq[i : i + window] if a in KD]
        if len(vals) == window:
            out.append((i + 1, sum(vals) / window))
    return out


def net_charge(seq: str) -> int:
    return sum(1 for a in seq if a in POSITIVE) - sum(1 for a in seq if a in NEGATIVE)


def main() -> int:
    root = Path(__file__).resolve().parents[4]
    rec = root / "genes/CANAL/CYB5/CYB5-uniprot.txt"
    if not rec.exists():
        print(f"ERROR: record not found at {rec}", file=sys.stderr)
        return 1
    seq, feats = read_record(rec)
    n = len(seq)
    print(f"record: {rec.relative_to(root)}")
    print(f"length: {n} residues")
    print(f"curated features used: {dict(feats)}")

    win = 19
    prof = hydropathy_windows(seq, win)
    peak_start, peak_val = max(prof, key=lambda kv: kv[1])
    peak_end = peak_start + win - 1
    print(f"\n-- most hydrophobic {win}-residue window (Kyte-Doolittle mean)")
    print(f"   {peak_start}-{peak_end}  mean KD {peak_val:+.2f}  seq {seq[peak_start-1:peak_end]}")
    print(f"   whole-protein mean KD {sum(KD[a] for a in seq if a in KD)/n:+.2f}")

    # Distance from the hydrophobic segment to the C-terminus: the tail-anchor test.
    tail = seq[peak_end:]
    print(f"\n-- tail beyond the hydrophobic segment")
    print(f"   residues {peak_end+1}-{n} ({len(tail)} aa): {tail or '(none)'}")
    print(f"   net charge {net_charge(tail):+d}"
          f"  basic {sum(1 for a in tail if a in POSITIVE)}"
          f"  acidic {sum(1 for a in tail if a in NEGATIVE)}")
    print(f"   distance from segment end to C-terminus: {n - peak_end} residues")

    # Flanking charge: the positive-inside rule orients the segment.
    flank = 15
    before = seq[max(0, peak_start - 1 - flank) : peak_start - 1]
    print(f"\n-- flanking charge (positive-inside rule), {flank}-residue flanks")
    print(f"   N-flank {max(1, peak_start-flank)}-{peak_start-1}: {before}  net {net_charge(before):+d}")
    print(f"   C-flank (tail above): net {net_charge(tail):+d}")

    # Heme ligands relative to the segment.
    ligands = [s for s, e in feats.get("BINDING", []) if s == e]
    print(f"\n-- curated BINDING residues (heme ligands) relative to the segment")
    for p in ligands:
        side = "N-terminal to segment" if p < peak_start else "C-terminal to segment"
        print(f"   {seq[p-1]}{p}  {side}")
    dom = feats.get("DOMAIN", [])
    for s, e in dom:
        print(f"   DOMAIN {s}-{e} ends {peak_start - e} residues before the segment start")

    print("\n-- interpretation limits")
    print("   This is a sequence prediction. It does not measure localisation, and it")
    print("   cannot distinguish ER from other organellar membranes: the topology it")
    print("   constrains is the orientation of the functional domain relative to the")
    print("   bilayer, not which bilayer.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
