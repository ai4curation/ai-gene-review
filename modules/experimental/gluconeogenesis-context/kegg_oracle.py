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
#
# This table MUST cover every atom in the module it is used with. An atom the table
# does not name cannot be resolved, and silently treating it as absent manufactures a
# fake pathway gap -- see `holds_for` below and projects/PATHWAY_SATISFIABILITY/REVIEW.md.
STEP_KO = {
    "metA": "K00651",  # homoserine O-succinyltransferase
    "metX": "K00641",  # homoserine O-acetyltransferase
    "metB": "K01739",  # cystathionine gamma-synthase
    "metC": "K01760",  # cystathionine beta-lyase
    "metY": "K01740",  # O-acylhomoserine sulfhydrylase (direct, O-acetyl)
    "metZ": "K10764",  # O-succinylhomoserine sulfhydrylase (direct, O-succinyl)
    # Homoserine-independent route: sulfide transferred straight onto L-aspartate
    # semialdehyde (EC 2.8.1.16). Two obligate subunits. PMID:25938369.
    "MJ0100": "K23975",  # L-aspartate semialdehyde sulfurtransferase
    "MJ0099": "K23976",  # ...its iron-sulfur / ferredoxin partner subunit
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
    "syn": "Synechocystis sp. PCC 6803",
    "mja": "Methanocaldococcus jannaschii",
    "rpr": "Rickettsia prowazekii",
}


class UnmappedStepError(KeyError):
    """A module atom has no KEGG Orthology id in :data:`STEP_KO`.

    Deciding such an atom is impossible, and answering ``False`` would be
    indistinguishable from a genuine genome gap -- which is exactly how the
    aspartate-semialdehyde route once produced two phantom "metabolic dark matter"
    hits. Better to fail than to invent a gap.
    """


def holds_for(present_genes: dict[str, bool], step_ko: dict[str, str] | None = None):
    """Build a per-genome atom predicate that refuses to guess.

    ``present_genes`` maps gene symbol -> encoded?, as returned per organism by
    :func:`load_cache`. Any atom whose symbol is not in the step->KO table raises
    :class:`UnmappedStepError` rather than silently counting as absent.

    >>> holds = holds_for({"metA": True, "metX": False}, {"metA": "K00651", "metX": "K00641"})
    >>> class A: gene_symbol = "metA"
    >>> holds(A())
    True
    >>> class B: gene_symbol = "metX"
    >>> holds(B())
    False
    >>> class C: gene_symbol = "metQQQ"
    >>> holds(C())
    Traceback (most recent call last):
        ...
    kegg_oracle.UnmappedStepError: "no KEGG Orthology id for step 'metQQQ'; add it to STEP_KO"
    """
    table = STEP_KO if step_ko is None else step_ko

    def holds(atom) -> bool:
        symbol = getattr(atom, "gene_symbol", None)
        if not symbol:
            return False
        if symbol not in table:
            raise UnmappedStepError(
                f"no KEGG Orthology id for step {symbol!r}; add it to STEP_KO"
            )
        return present_genes.get(symbol, False)

    return holds


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
