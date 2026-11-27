#!/usr/bin/env python3
"""Quantify ARGLU1's compositional bias and map it onto the annotated features.

ARGLU1's name asserts a *composition* (arginine- and glutamate-rich), not an
activity. This script measures that composition from the committed UniProt flat
file so the review can state what is actually there rather than inferring a
function from the gene symbol:

* residue composition of the two experimentally delimited regions
  (1-74, "necessary and sufficient for RNA binding"; 75-273, "necessary and
  sufficient for transcriptional regulation");
* the Arg-Ser dipeptide (RS-repeat) content of the N-terminus, which is the
  structural claim behind treating ARGLU1 as an SRPK2 substrate;
* where UniProt's annotated phosphosites fall relative to those regions;
* the complete InterPro/Pfam/PANTHER signature set, i.e. what fold evidence
  exists at all.

Input is ``../ARGLU1-uniprot.txt`` (committed alongside this script). A missing
input is a hard error naming the fix, never a silently skipped section.

Run:  uv run python composition_and_features.py
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
UNIPROT_TXT = HERE.parent / "ARGLU1-uniprot.txt"

# Regions UniProt delimits with experimental evidence (ECO:0000269|PubMed:30698747).
REGIONS = {
    "N-terminal RNA-binding region (1-74)": (1, 74),
    "C-terminal transcription-regulatory region (75-273)": (75, 273),
    "full length": None,
}


def parse_uniprot(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(
            f"missing input {path}\n"
            f"Regenerate it with:  just fetch-gene human ARGLU1"
        )
    text = path.read_text()

    # Sequence: everything between the SQ line and the terminating '//'.
    m = re.search(r"^SQ   SEQUENCE.*?$(.*?)^//", text, re.S | re.M)
    if not m:
        raise SystemExit(f"{path}: no SQ block found; the flat file is malformed.")
    seq = re.sub(r"[^A-Z]", "", m.group(1))

    m_len = re.search(r"^ID   \S+\s+Reviewed;\s+(\d+) AA\.", text, re.M)
    if not m_len:
        raise SystemExit(f"{path}: cannot read the declared length from the ID line.")
    declared = int(m_len.group(1))
    if len(seq) != declared:
        raise SystemExit(
            f"{path}: parsed {len(seq)} residues but the ID line declares {declared}. "
            "Refusing to compute composition on a mis-parsed sequence."
        )

    # MOD_RES phosphosites.
    phos = []
    for mm in re.finditer(r"^FT   MOD_RES\s+(\d+)\n(?:FT\s+/note=\"([^\"]+)\")", text, re.M):
        phos.append((int(mm.group(1)), mm.group(2)))

    # InterPro / Pfam / PANTHER cross-references.
    sigs = []
    for db in ("InterPro", "Pfam", "PANTHER", "PROSITE", "SMART", "SUPFAM", "Gene3D"):
        for mm in re.finditer(rf"^DR   {db}; (.+?)\.$", text, re.M):
            sigs.append(f"{db}: {mm.group(1)}")

    return {"sequence": seq, "phosphosites": phos, "signatures": sigs}


def composition(seq: str) -> dict:
    n = len(seq)
    c = Counter(seq)
    return {aa: round(100 * cnt / n, 1) for aa, cnt in c.most_common()}


def rs_dipeptides(seq: str) -> dict:
    """Count RS/SR dipeptides -- the hallmark of an SR-protein RS domain."""
    rs = len(re.findall(r"(?=RS)", seq))
    sr = len(re.findall(r"(?=SR)", seq))
    # longest run of alternating R/S
    best = 0
    run = 0
    for i in range(len(seq) - 1):
        if {seq[i], seq[i + 1]} == {"R", "S"}:
            run += 1
            best = max(best, run)
        else:
            run = 0
    return {"RS_dipeptides": rs, "SR_dipeptides": sr,
            "longest_alternating_RS_run_dipeptides": best}


def main() -> int:
    data = parse_uniprot(UNIPROT_TXT)
    seq = data["sequence"]
    out: dict = {"length": len(seq), "regions": {}, "signatures": data["signatures"]}

    print(f"ARGLU1 Q9NWB6, {len(seq)} aa (parsed from {UNIPROT_TXT.name})\n")

    for label, span in REGIONS.items():
        sub = seq if span is None else seq[span[0] - 1: span[1]]
        comp = composition(sub)
        rs = rs_dipeptides(sub)
        top = list(comp.items())[:6]
        rec = {
            "span": span,
            "length": len(sub),
            "pct_R": comp.get("R", 0.0),
            "pct_E": comp.get("E", 0.0),
            "pct_S": comp.get("S", 0.0),
            "pct_K": comp.get("K", 0.0),
            "pct_R_plus_K": round(comp.get("R", 0) + comp.get("K", 0), 1),
            "pct_E_plus_D": round(comp.get("E", 0) + comp.get("D", 0), 1),
            "top6_residues_pct": top,
            **rs,
        }
        out["regions"][label] = rec
        print(f"{label}  [{len(sub)} aa]")
        print(f"   R={rec['pct_R']}%  K={rec['pct_K']}%  (R+K={rec['pct_R_plus_K']}%)   "
              f"E={rec['pct_E']}%  D={comp.get('D',0)}%  (E+D={rec['pct_E_plus_D']}%)   "
              f"S={rec['pct_S']}%")
        print(f"   top residues: {top}")
        print(f"   RS dipeptides={rs['RS_dipeptides']}  SR={rs['SR_dipeptides']}  "
              f"longest alternating RS run={rs['longest_alternating_RS_run_dipeptides']} dipeptides")
        print()

    print("UniProt MOD_RES phosphosites and which region they fall in:")
    region_hits = Counter()
    for pos, note in data["phosphosites"]:
        where = "N-term 1-74" if pos <= 74 else "C-term 75-273"
        region_hits[where] += 1
        print(f"   {note} {pos}  -> {where}")
    out["phosphosites"] = [{"position": p, "note": n,
                            "region": "1-74" if p <= 74 else "75-273"}
                           for p, n in data["phosphosites"]]
    out["phosphosites_by_region"] = dict(region_hits)
    print(f"   -> {dict(region_hits)}")

    print("\nAll sequence-signature cross-references in the UniProt entry:")
    for s in data["signatures"]:
        print("   ", s)
    if not data["signatures"]:
        raise SystemExit("no signature cross-references parsed; check the DR parser.")

    (HERE / "composition.json").write_text(json.dumps(out, indent=2, sort_keys=True))
    print(f"\nwrote {HERE / 'composition.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
