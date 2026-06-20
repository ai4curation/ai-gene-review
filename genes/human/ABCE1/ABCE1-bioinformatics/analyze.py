#!/usr/bin/env python3
"""Sequence-level analysis of human ABCE1 (UniProt P61221).

Purpose: provide reproducible, programmatic support for three curation
decisions in ABCE1-ai-review.yaml that otherwise rest on assertion or on
the UniProt feature table alone:

  1. ABCE1 has no transmembrane region (supports REMOVE of GO:0016020
     "membrane" and the broader "ABC transporter domains are non-functional"
     interpretation -> ABCE1 is a soluble cytosolic ATPase, not a transporter).
  2. ABCE1 has two nucleotide-binding-domain (NBD) Walker A / Walker B motifs
     (supports ATP binding / ATP hydrolysis activity).
  3. ABCE1 has an N-terminal cysteine-rich region consistent with two
     ferredoxin-type [4Fe-4S] clusters (supports MODIFY of GO:0005506
     "iron ion binding" -> GO:0051539 "4 iron, 4 sulfur cluster binding").

The script is pure standard library and parses the curated UniProt record
(../ABCE1-uniprot.txt) at run time. Nothing is hardcoded: the sequence,
the TRANSMEM feature count, and all motif positions are derived from the
input file. Methods are heuristics and are clearly bounded in RESULTS.md;
the authoritative line of evidence remains the curated UniProt feature table.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# Kyte & Doolittle (1982) hydropathy values.
KD = {
    "I": 4.5, "V": 4.2, "L": 3.8, "F": 2.8, "C": 2.5, "M": 1.9, "A": 1.8,
    "G": -0.4, "T": -0.7, "S": -0.8, "W": -0.9, "Y": -1.3, "P": -1.6,
    "H": -3.2, "E": -3.5, "Q": -3.5, "D": -3.5, "N": -3.5, "K": -3.9, "R": -4.5,
}

# Window and threshold conventions for putative TM-helix detection.
TM_WINDOW = 19
TM_THRESHOLD = 1.6  # mean KD score above which a window is flagged as TM-like

UNIPROT = Path(__file__).resolve().parent.parent / "ABCE1-uniprot.txt"


def parse_uniprot(path: Path) -> tuple[str, int, int]:
    """Return (sequence, declared_length, transmem_feature_count)."""
    text = path.read_text()
    # Sequence: lines between the "SQ" line and the terminating "//".
    seq_lines: list[str] = []
    in_seq = False
    declared_len = -1
    for line in text.splitlines():
        if line.startswith("SQ"):
            in_seq = True
            m = re.search(r"SEQUENCE\s+(\d+)\s+AA", line)
            if m:
                declared_len = int(m.group(1))
            continue
        if in_seq:
            if line.startswith("//"):
                break
            seq_lines.append(line.strip())
    sequence = re.sub(r"[^A-Z]", "", "".join(seq_lines).upper())
    # Count curated TRANSMEM feature keys in the feature table.
    transmem = len(re.findall(r"^FT\s+TRANSMEM\b", text, flags=re.MULTILINE))
    return sequence, declared_len, transmem


def hydropathy_scan(seq: str, window: int, threshold: float) -> dict:
    if len(seq) < window:
        return {"max_mean": None, "max_center": None, "tm_like_windows": 0}
    scores = [KD.get(aa, 0.0) for aa in seq]
    best_mean = float("-inf")
    best_center = -1
    tm_like = 0
    half = window // 2
    for start in range(0, len(seq) - window + 1):
        mean = sum(scores[start:start + window]) / window
        if mean >= threshold:
            tm_like += 1
        if mean > best_mean:
            best_mean = mean
            best_center = start + half + 1  # 1-based residue index
    return {
        "max_mean": round(best_mean, 3),
        "max_center": best_center,
        "tm_like_windows": tm_like,
    }


def find_walker_a(seq: str) -> list[dict]:
    """P-loop / Walker A consensus [AG]-x(4)-G-K-[ST]."""
    hits = []
    for m in re.finditer(r"[AG].{4}GK[ST]", seq):
        hits.append({"start": m.start() + 1, "end": m.end(), "motif": m.group()})
    return hits


def find_walker_b(seq: str) -> list[dict]:
    """Walker B-like consensus: 3-4 hydrophobic residues followed by DE."""
    hits = []
    for m in re.finditer(r"[ILVFM]{3,4}DE", seq):
        hits.append({"start": m.start() + 1, "end": m.end(), "motif": m.group()})
    return hits


def nterminal_cysteines(seq: str, region_end: int = 80) -> dict:
    region = seq[:region_end]
    positions = [i + 1 for i, aa in enumerate(region) if aa == "C"]
    cxxc = [m.start() + 1 for m in re.finditer(r"(?=C..C)", region)]
    return {
        "region": f"1-{region_end}",
        "cysteine_count": len(positions),
        "cysteine_positions": positions,
        "cxxc_motif_starts": cxxc,
    }


def main() -> int:
    if not UNIPROT.exists():
        print(f"ERROR: UniProt record not found at {UNIPROT}", file=sys.stderr)
        return 1
    seq, declared_len, transmem = parse_uniprot(UNIPROT)
    result = {
        "uniprot_id": "P61221",
        "gene_symbol": "ABCE1",
        "source_file": str(UNIPROT.name),
        "sequence_length": len(seq),
        "declared_length": declared_len,
        "length_matches_header": len(seq) == declared_len,
        "uniprot_transmem_features": transmem,
        "hydropathy": hydropathy_scan(seq, TM_WINDOW, TM_THRESHOLD),
        "tm_window": TM_WINDOW,
        "tm_threshold": TM_THRESHOLD,
        "walker_a_motifs": find_walker_a(seq),
        "walker_b_motifs": find_walker_b(seq),
        "n_terminal_fe_s": nterminal_cysteines(seq),
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
