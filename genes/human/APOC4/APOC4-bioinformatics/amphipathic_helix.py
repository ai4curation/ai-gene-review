#!/usr/bin/env python3
"""Is the human apoC-IV mature chain amphipathic, like the other exchangeable apoCs?

The only molecular-function claim GOA makes for APOC4 (GO:0005319 lipid carrier
activity, TAS) traces to a 1995 paper that inferred it from "two potential
amphipathic alpha-helical domains" in the predicted sequence, and the only direct
biophysical demonstration in the family is on the rabbit orthologue. This script
tests the sequence-level half of that claim quantitatively and live: it fetches
each protein from UniProt, trims to the mature CHAIN, and scans the Eisenberg
hydrophobic moment over 18-residue windows at 100 degrees per residue.

It reports numbers, not a verdict: high mean hydrophobicity with a high
hydrophobic moment is the signature of a lipid-surface-seeking helix, and the
comparison set is what makes an APOC4 value interpretable.

Run: uv run python amphipathic_helix.py
"""
import json
import math
import sys

import numpy as np
import requests

# Eisenberg normalized consensus hydrophobicity scale (Eisenberg et al. 1984).
EISENBERG = {
    "A": 0.62, "R": -2.53, "N": -0.78, "D": -0.90, "C": 0.29,
    "Q": -0.85, "E": -0.74, "G": 0.48, "H": -0.40, "I": 1.38,
    "L": 1.06, "K": -1.50, "M": 0.64, "F": 1.19, "P": 0.12,
    "S": -0.18, "T": -0.05, "W": 0.81, "Y": 0.26, "V": 1.08,
}

WINDOW = 18
DELTA = math.radians(100.0)

PROTEINS = [
    ("P55056", "APOC4_HUMAN", "target"),
    ("P55057", "APOC4_RABIT", "orthologue with direct lipid-binding data"),
    ("Q61268", "APOC4_MOUSE", "orthologue, IBA donor"),
    ("P02654", "APOC1_HUMAN", "exchangeable apoC control"),
    ("P02655", "APOC2_HUMAN", "exchangeable apoC control"),
    ("P02656", "APOC3_HUMAN", "exchangeable apoC control"),
    ("P02647", "APOA1_HUMAN", "class-A amphipathic-helix positive control"),
    ("P61769", "B2MG_HUMAN", "secreted all-beta negative control"),
    ("P10599", "THIO_HUMAN", "cytosolic globular negative control"),
]

S = requests.Session()
S.headers.update({"Accept": "application/json", "User-Agent": "ai-gene-review/APOC4"})


def fetch(acc: str) -> dict:
    r = S.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60)
    r.raise_for_status()
    d = r.json()
    assert "sequence" in d, (
        f"{acc} is not an active UniProt entry "
        f"({d.get('entryType')}, {d.get('inactiveReason')}) - pick a live accession"
    )
    seq = d["sequence"]["value"]
    assert len(seq) == d["sequence"]["length"], f"{acc}: declared length != sequence"
    chain = None
    for f in d.get("features", []):
        if f["type"] == "Chain":
            loc = f["location"]
            s, e = loc["start"]["value"], loc["end"]["value"]
            if s is None or e is None:
                continue
            if chain is None or (e - s) > (chain[1] - chain[0]):
                chain = (s, e)
    if chain is None:
        chain = (1, len(seq))
    mature = seq[chain[0] - 1: chain[1]]
    assert len(mature) == chain[1] - chain[0] + 1
    return {
        "accession": acc,
        "id": d["uniProtkbId"],
        "full_length": len(seq),
        "chain": chain,
        "mature": mature,
    }


def moment_scan(seq: str) -> list[dict]:
    out = []
    for i in range(0, len(seq) - WINDOW + 1):
        w = seq[i: i + WINDOW]
        h = np.array([EISENBERG.get(a, 0.0) for a in w])
        ang = np.arange(WINDOW) * DELTA
        mu = math.hypot(float((h * np.cos(ang)).sum()), float((h * np.sin(ang)).sum())) / WINDOW
        out.append({"start": i + 1, "seq": w, "muH": mu, "H": float(h.mean())})
    return out


def main() -> int:
    rows = []
    for acc, expect_id, role in PROTEINS:
        rec = fetch(acc)
        assert rec["id"] == expect_id, f"{acc} resolved to {rec['id']}, expected {expect_id}"
        scan = moment_scan(rec["mature"])
        assert scan, f"{acc}: mature chain shorter than the {WINDOW}-residue window"
        best = max(scan, key=lambda w: w["muH"])
        # count non-overlapping high-moment segments (muH >= 0.35, Eisenberg's
        # surface-seeking cutoff), greedily from the strongest window
        taken: list[int] = []
        for w in sorted(scan, key=lambda w: -w["muH"]):
            if w["muH"] < 0.35:
                break
            if all(abs(w["start"] - t) >= WINDOW for t in taken):
                taken.append(w["start"])
        density = len(taken) / len(rec["mature"])
        chain_H = float(np.mean([EISENBERG.get(a, 0.0) for a in rec["mature"]]))
        rows.append({
            "segment_density_per_residue": round(density, 4),
            "mean_H_whole_chain": round(chain_H, 3),
            "accession": acc, "id": rec["id"], "role": role,
            "full_length": rec["full_length"],
            "chain": f"{rec['chain'][0]}-{rec['chain'][1]}",
            "mature_length": len(rec["mature"]),
            "max_muH": round(best["muH"], 3),
            "max_muH_start": best["start"],
            "max_muH_window": best["seq"],
            "mean_H_at_max": round(best["H"], 3),
            "n_segments_muH_ge_0.35": len(taken),
            "segment_starts": sorted(taken),
        })

    hdr = (f"{'protein':14} {'chain':>9} {'mat':>4} {'maxMuH':>7} {'<H>all':>7} "
           f"{'nSeg':>5} {'seg/res':>8}  role")
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        print(f"{r['id']:14} {r['chain']:>9} {r['mature_length']:>4} {r['max_muH']:>7} "
              f"{r['mean_H_whole_chain']:>7} {r['n_segments_muH_ge_0.35']:>5} "
              f"{r['segment_density_per_residue']:>8}  {r['role']}")

    tgt = next(r for r in rows if r["accession"] == "P55056")
    print(f"\nAPOC4_HUMAN strongest window (mature residue {tgt['max_muH_start']}): {tgt['max_muH_window']}")
    print(f"APOC4_HUMAN segments with muH >= 0.35 starting at mature residues: {tgt['segment_starts']}")

    with open("amphipathic_helix_result.json", "w") as fh:
        json.dump({"window": WINDOW, "angle_deg": 100.0,
                   "scale": "Eisenberg normalized consensus", "rows": rows}, fh, indent=2)
    print("\nwrote amphipathic_helix_result.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
