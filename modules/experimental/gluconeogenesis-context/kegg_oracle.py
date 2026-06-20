#!/usr/bin/env python
"""KEGG genome-presence oracle: is a pathway step's ortholog encoded in a genome?

This is the prokaryote-side analogue of the expression oracles. Where GapMind maps
each pathway step to candidate sequences (HMMs/characterized proteins), here each
step's gene symbol is mapped to a KEGG Orthology (KO) id, and presence in a genome
is decided by the KEGG ``link`` endpoint: ``/link/<org>/ko:<KO>`` returns the
organism's gene(s) assigned to that KO (empty if the genome encodes none).

The step->KO table is the oracle's "step definitions" (kept here, not in the
pathway template), mirroring GapMind's split between a pathway definition and its
candidate definitions. Results are cached to a TSV for reproducibility.
"""

from __future__ import annotations

import time
from pathlib import Path

import requests

HERE = Path(__file__).parent
CACHE = HERE / "cache" / "kegg_presence.tsv"
KEGG = "https://rest.kegg.jp"

# Step (gene symbol) -> KEGG Orthology id. The methionine-biosynthesis template.
STEP_KO = {
    "metA": "K00651",  # homoserine O-succinyltransferase
    "metX": "K00641",  # homoserine O-acetyltransferase
    "metB": "K01739",  # cystathionine gamma-synthase
    "metC": "K01760",  # cystathionine beta-lyase
    "metY": "K01740",  # O-acylhomoserine sulfhydrylase (direct)
    "metE": "K00549",  # cobalamin-independent methionine synthase
    "metH": "K00548",  # cobalamin-dependent methionine synthase
}

# KEGG organism code -> human-readable label.
ORGANISMS = {
    "eco": "Escherichia coli K-12 MG1655",
    "bsu": "Bacillus subtilis 168",
    "hin": "Haemophilus influenzae Rd",
    "cgl": "Corynebacterium glutamicum",
    "buc": "Buchnera aphidicola (APS, Acyrthosiphon pisum endosymbiont)",
}


def present(org: str, ko: str) -> bool:
    """True iff genome ``org`` encodes at least one gene assigned to ``ko``."""
    r = requests.get(f"{KEGG}/link/{org}/ko:{ko}", timeout=30)
    r.raise_for_status()
    return bool(r.text.strip())


def build_cache(organisms=None, step_ko=None) -> None:
    organisms = organisms or ORGANISMS
    step_ko = step_ko or STEP_KO
    symbols = list(step_ko)
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    rows: dict[str, dict[str, int]] = {}
    for org in organisms:
        rows[org] = {}
        for sym in symbols:
            rows[org][sym] = int(present(org, step_ko[sym]))
            time.sleep(0.1)
    with CACHE.open("w") as fh:
        fh.write("organism\t" + "\t".join(symbols) + "\n")
        for org in organisms:
            fh.write(org + "\t" + "\t".join(str(rows[org][s]) for s in symbols) + "\n")


def load_cache() -> dict[str, dict[str, bool]]:
    if not CACHE.exists():
        build_cache()
    lines = CACHE.read_text().splitlines()
    symbols = lines[0].split("\t")[1:]
    out: dict[str, dict[str, bool]] = {}
    for line in lines[1:]:
        c = line.split("\t")
        out[c[0]] = {s: v == "1" for s, v in zip(symbols, c[1:])}
    return out


if __name__ == "__main__":
    build_cache()
    matrix = load_cache()
    syms = list(STEP_KO)
    print("organism  " + " ".join(f"{s:>5}" for s in syms))
    for org, row in matrix.items():
        print(f"{org:8s}  " + " ".join(f"{('Y' if row[s] else '.'):>5}" for s in syms))
