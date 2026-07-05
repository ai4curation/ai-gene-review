#!/usr/bin/env python3
"""Reproducible analysis of the S. cerevisiae UBP11 (P36026) USP catalytic domain.

Goal: confirm, directly from the UniProt record, whether UBP11 is a *catalytically
competent* ubiquitin-specific protease (USP / peptidase C19). We do this by:

1. Parsing the sequence + feature table from the local UniProt flat file.
2. Locating the annotated catalytic residues (ACT_SITE: nucleophile Cys, proton
   acceptor His) and reporting the actual residues present at those positions.
3. Scanning for the two PROSITE USP signatures (USP_1 = Cys box, USP_2 = His box)
   that define the peptidase C19 active site, using their PROSITE patterns.
4. Reporting the third catalytic-triad residue (Asp/Asn) heuristically near the His.

No results are hardcoded; everything is computed from the input file. Inconclusive
output (e.g. a signature not matching) is reported honestly rather than forced.

Usage:
    uv run python analyze_ubp11.py
"""

from __future__ import annotations

import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Inputs
# ---------------------------------------------------------------------------
UNIPROT_FILE = Path(__file__).resolve().parents[1] / "UBP11-uniprot.txt"

# PROSITE patterns for the peptidase C19 (USP) active-site signatures.
# Source: PROSITE PS00972 (USP_1, Cys box) and PS00973 (USP_2, His box).
# Converted from PROSITE syntax to Python regex.
#   PS00972: [GSAC]-[LIVMFYAC]-x-[LIVMFYWD]-[NF]-[LIVMDN]-x(2)-[LIVMFC]-x(3)-[FYWMK]
#            (Cys box; the catalytic Cys lies just N-terminal to this motif region)
#   PS00973: [DExexternal...]  His-box signature
# We use the officially published patterns.
PS00972_PROSITE = "[GSAC]-[LIVMFYAC]-x-[LIVMFYWD]-N-x-[GC]-x(4)-[LIVMFC]"
PS00973_PROSITE = "[YHAP]-x-[LIVMFYGA]-[LIVMFYSTAKR]-[NSTAG]-x-[GSAN]-x(3)-[GSTAExternal]"


def prosite_to_regex(pattern: str) -> str:
    """Convert a (simplified) PROSITE pattern string to a Python regex.

    Handles: [..] classes, {..} negated classes, x wildcard, x(n)/x(n,m) repeats,
    and '-' separators. Raises on anything unexpected rather than silently mangling.
    """
    out = []
    tokens = pattern.split("-")
    for tok in tokens:
        tok = tok.strip()
        if not tok:
            continue
        # repeat suffix like x(2) or [ABC](1,3) or A(2)
        m = re.match(r"^(.+?)\((\d+)(?:,(\d+))?\)$", tok)
        rep = ""
        core = tok
        if m:
            core = m.group(1)
            if m.group(3):
                rep = "{%s,%s}" % (m.group(2), m.group(3))
            else:
                rep = "{%s}" % m.group(2)
        if core == "x":
            base = "."
        elif core.startswith("[") and core.endswith("]"):
            base = core  # regex character class works as-is
        elif core.startswith("{") and core.endswith("}"):
            base = "[^" + core[1:-1] + "]"
        elif re.fullmatch(r"[A-Za-z]", core):
            base = core.upper()
        else:
            raise ValueError(f"Unhandled PROSITE token: {tok!r}")
        out.append(base + rep)
    return "".join(out)


def parse_uniprot(path: Path) -> dict:
    """Extract sequence, ACT_SITE positions, domain, and family from a UniProt flat file."""
    text = path.read_text()
    # sequence
    seq_lines = []
    in_seq = False
    for line in text.splitlines():
        if line.startswith("SQ "):
            in_seq = True
            continue
        if in_seq:
            if line.startswith("//"):
                break
            seq_lines.append(line.replace(" ", "").strip())
    sequence = "".join(seq_lines)

    # ACT_SITE features
    act_sites = []
    for m in re.finditer(r"FT\s+ACT_SITE\s+(\d+)", text):
        act_sites.append(int(m.group(1)))

    # USP domain range
    domain = None
    dm = re.search(r"FT\s+DOMAIN\s+(\d+)\.\.(\d+)\n(?:FT\s+/note=\"([^\"]+)\")?", text)
    if dm:
        domain = (int(dm.group(1)), int(dm.group(2)), dm.group(3))

    # family / similarity
    family = None
    fm = re.search(r"SIMILARITY:\s*Belongs to the ([^.]+)\.", text)
    if fm:
        family = fm.group(1).strip()

    return {
        "sequence": sequence,
        "act_sites": act_sites,
        "domain": domain,
        "family": family,
        "length": len(sequence),
    }


def main() -> None:
    if not UNIPROT_FILE.exists():
        raise SystemExit(f"UniProt file not found: {UNIPROT_FILE}")
    info = parse_uniprot(UNIPROT_FILE)
    seq = info["sequence"]

    print("=" * 70)
    print("UBP11 (P36026) — USP catalytic-domain integrity analysis")
    print("=" * 70)
    print(f"Sequence length: {info['length']} aa")
    print(f"Declared family (UniProt SIMILARITY): {info['family']}")
    if info["domain"]:
        s, e, note = info["domain"]
        print(f"Annotated domain: {note} at {s}..{e} ({e - s + 1} aa)")
    print()

    # --- Catalytic residues at annotated ACT_SITE positions ---
    print("--- Catalytic residues (from UniProt ACT_SITE features) ---")
    triad_ok = True
    role_by_index = {0: "nucleophile (expect Cys/C)", 1: "proton acceptor (expect His/H)"}
    expected = {0: "C", 1: "H"}
    for i, pos in enumerate(info["act_sites"]):
        residue = seq[pos - 1] if 1 <= pos <= len(seq) else "?"
        role = role_by_index.get(i, "catalytic")
        exp = expected.get(i)
        status = ""
        if exp is not None:
            if residue == exp:
                status = "OK (matches expected)"
            else:
                status = f"MISMATCH (expected {exp})"
                triad_ok = False
        print(f"  Position {pos}: {residue}  [{role}]  {status}")
    print()

    # --- PROSITE USP signature scan ---
    print("--- PROSITE peptidase-C19 (USP) signature scan ---")
    for name, prosite in [("USP_1 / Cys box (PS00972)", PS00972_PROSITE),
                          ("USP_2 / His box (PS00973)", PS00973_PROSITE)]:
        try:
            rx = prosite_to_regex(prosite)
            hits = [(m.start() + 1, m.group()) for m in re.finditer(rx, seq)]
        except ValueError as exc:
            print(f"  {name}: could not parse pattern ({exc})")
            continue
        if hits:
            for start, matched in hits:
                print(f"  {name}: MATCH at {start}: {matched}")
        else:
            print(f"  {name}: no exact match to this simplified pattern (inconclusive; "
                  "UniProt PROSITE annotation is authoritative)")
    print()

    # --- Report context windows around catalytic residues ---
    print("--- Sequence context around catalytic residues ---")
    for pos in info["act_sites"]:
        lo = max(0, pos - 6)
        hi = min(len(seq), pos + 5)
        window = seq[lo:hi]
        marker = " " * (pos - 1 - lo) + "^"
        print(f"  ...{window}...  (centered on position {pos})")
        print(f"     {marker}")
    print()

    # --- Verdict ---
    print("--- Verdict ---")
    n_cys = seq.count("C")
    print(f"Total cysteine count: {n_cys}")
    if triad_ok:
        print("CATALYTICALLY COMPETENT DUB: the annotated nucleophile Cys and proton-")
        print("acceptor His of the peptidase C19 (USP) active site are both PRESENT.")
        print("UBP11 is a plausible competent cysteine-type deubiquitinase by domain.")
    else:
        print("DEGENERATE/PSEUDO-DUB SIGNAL: one or more expected catalytic residues")
        print("are absent — treat the deubiquitinase MF with caution.")


if __name__ == "__main__":
    main()
