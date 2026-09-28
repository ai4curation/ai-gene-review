#!/usr/bin/env python3
"""Test whether human ADM5 retains the features a functional adrenomedullin-family peptide needs.

Human ADM5 (C9JUS6) carries seven IBA annotations asserting hormone activity, adrenomedullin
receptor signalling, and cardiovascular/renal regulation, all propagated from the ancestral
AM5 node. UniProt calls the human protein a "Probable non-functional remnant of
adrenomedullin-5". This script checks that claim against the sequences themselves, using pig
ADM5 (A5LHG2) -- the reviewed, experimentally characterised mammalian ortholog with an
annotated mature peptide -- as the functional reference.

Two features are decisive for a CGRP/adrenomedullin-family peptide:

1. The intramolecular disulfide ring (C-x-x-x-x-C).
2. C-terminal alpha-amidation, which in the precursor is encoded as the amidated residue
   followed by a glycine donor and a dibasic cleavage site (X-G-K/R-K/R). Amidation is
   required for receptor activation across this peptide family, so losing the signal
   abolishes the hormone regardless of what else is retained.

Nothing here is hardcoded: sequences and features are fetched live from the UniProt REST API
and the alignment is computed. The script prints its findings and makes no claim beyond them.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.request
from dataclasses import dataclass, field

HUMAN = "C9JUS6"
PIG = "A5LHG2"
API = "https://rest.uniprot.org/uniprotkb"


@dataclass
class Entry:
    accession: str
    name: str
    organism: str
    sequence: str
    features: list[dict] = field(default_factory=list)

    def feature(self, ftype: str, note: str | None = None) -> dict | None:
        for f in self.features:
            if f["type"] != ftype:
                continue
            if note and note.lower() not in (f.get("description") or "").lower():
                continue
            return f
        return None


def fetch(accession: str) -> Entry:
    with urllib.request.urlopen(f"{API}/{accession}.json") as fh:
        data = json.load(fh)
    return Entry(
        accession=accession,
        name=data["proteinDescription"]["recommendedName"]["fullName"]["value"],
        organism=data["organism"]["scientificName"],
        sequence=data["sequence"]["value"],
        features=[
            {
                "type": f["type"],
                "start": f["location"]["start"]["value"],
                "end": f["location"]["end"]["value"],
                "description": f.get("description", ""),
            }
            for f in data.get("features", [])
        ],
    )


def align(a: str, b: str) -> tuple[str, str]:
    """Needleman-Wunsch with BLOSUM62-ish scoring, kept simple and dependency-free."""
    match, mismatch, gap = 2, -1, -6
    n, m = len(a), len(b)
    score = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        score[i][0] = i * gap
    for j in range(1, m + 1):
        score[0][j] = j * gap
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            score[i][j] = max(
                score[i - 1][j - 1] + (match if a[i - 1] == b[j - 1] else mismatch),
                score[i - 1][j] + gap,
                score[i][j - 1] + gap,
            )
    i, j, ra, rb = n, m, [], []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and score[i][j] == score[i - 1][j - 1] + (
            match if a[i - 1] == b[j - 1] else mismatch
        ):
            ra.append(a[i - 1]); rb.append(b[j - 1]); i -= 1; j -= 1
        elif i > 0 and score[i][j] == score[i - 1][j] + gap:
            ra.append(a[i - 1]); rb.append("-"); i -= 1
        else:
            ra.append("-"); rb.append(b[j - 1]); j -= 1
    return "".join(reversed(ra)), "".join(reversed(rb))


def project(aln_ref: str, aln_qry: str, ref_pos: int) -> tuple[int | None, str]:
    """Map a 1-based position in the reference onto the query via the alignment."""
    r = q = 0
    for cr, cq in zip(aln_ref, aln_qry):
        if cr != "-":
            r += 1
        if cq != "-":
            q += 1
        if r == ref_pos and cr != "-":
            return (q, cq) if cq != "-" else (None, "-")
    return None, "?"


AMIDATION = re.compile(r"G[KR][KR]")


def main() -> int:
    pig, human = fetch(PIG), fetch(HUMAN)
    for e in (pig, human):
        print(f"{e.accession}  {e.organism:22}  {len(e.sequence):3d} aa  {e.name}")
    print()

    pep = pig.feature("Peptide", "Adrenomedullin-5")
    amide = pig.feature("Modified residue", "amide")
    if not pep:
        print("FAIL: pig mature-peptide feature not found; UniProt schema may have changed")
        return 2
    print(f"Pig mature AM5 : residues {pep['start']}-{pep['end']}  "
          f"{pig.sequence[pep['start']-1:pep['end']]}")
    if amide:
        print(f"Pig amidation  : position {amide['start']} "
              f"({pig.sequence[amide['start']-1]}) -> {amide['description']}")
        tail = pig.sequence[amide["start"]:amide["start"] + 3]
        print(f"Pig signal     : ...{pig.sequence[amide['start']-1]}|{tail}  "
              f"(G+dibasic present: {bool(AMIDATION.match(tail))})")
    print()

    a_pig, a_hum = align(pig.sequence, human.sequence)
    ident = sum(1 for x, y in zip(a_pig, a_hum) if x == y and x != "-")
    cols = sum(1 for x, y in zip(a_pig, a_hum) if x != "-" and y != "-")
    print(f"Global alignment: {ident}/{cols} identical in aligned columns "
          f"({100*ident/cols:.1f}%)\n")

    # --- feature-by-feature ---
    print("Feature retention in human, projected through the alignment:")
    ss = pig.feature("Disulfide bond")
    verdict = {}
    if ss:
        hs, rs = project(a_pig, a_hum, ss["start"])
        he, re_ = project(a_pig, a_hum, ss["end"])
        ok = rs == "C" and re_ == "C"
        verdict["disulfide_ring"] = ok
        print(f"  disulfide ring  pig C{ss['start']}..C{ss['end']}  ->  "
              f"human {rs}{hs}..{re_}{he}   {'RETAINED' if ok else 'LOST'}")

    if amide:
        ha, ra = project(a_pig, a_hum, amide["start"])
        nxt = human.sequence[ha:ha + 3] if ha else ""
        ok = bool(AMIDATION.match(nxt))
        verdict["amidation_signal"] = ok
        print(f"  amidated resid  pig {pig.sequence[amide['start']-1]}{amide['start']}  ->  "
              f"human {ra}{ha}")
        print(f"  amidation motif pig '{pig.sequence[amide['start']:amide['start']+3]}'  ->  "
              f"human '{nxt}'   {'RETAINED' if ok else 'LOST (no G+dibasic donor)'}")

    # does the human protein carry an amidation signal ANYWHERE?
    hits = [(m.start() + 1, m.group()) for m in AMIDATION.finditer(human.sequence)]
    print(f"\n  any G+dibasic motif anywhere in human ADM5: "
          f"{hits if hits else 'none'}")
    pig_hits = [(m.start() + 1, m.group()) for m in AMIDATION.finditer(pig.sequence)]
    print(f"  any G+dibasic motif anywhere in pig ADM5  : {pig_hits if pig_hits else 'none'}")

    # where does homology stop?
    run = 0
    last_aligned = 0
    r = 0
    for cr, cq in zip(a_pig, a_hum):
        if cr != "-":
            r += 1
        if cr != "-" and cq != "-" and cr == cq:
            run += 1
            last_aligned = r
        elif cr == "-" or cq == "-":
            run = 0
    print(f"\n  last identity-anchored pig position: {last_aligned} of {len(pig.sequence)}")
    print(f"  pig length {len(pig.sequence)} vs human {len(human.sequence)}: "
          f"human C-terminal extension of {len(human.sequence)-len(pig.sequence)} residues")

    print("\n--- Summary ---")
    for k, v in verdict.items():
        print(f"  {k:18} {'retained' if v else 'LOST'}")
    if verdict.get("disulfide_ring") and not verdict.get("amidation_signal"):
        print("\n  The ring is intact but the C-terminal amidation signal is not. Alpha-amidation\n"
              "  is required for receptor activation throughout the CGRP/adrenomedullin family,\n"
              "  so an intact ring alone does not make a functional hormone. This is consistent\n"
              "  with UniProt's 'probable non-functional remnant' call, reached independently.")
    elif verdict.get("amidation_signal"):
        print("\n  The amidation signal is present; this analysis does NOT support a\n"
              "  loss-of-function call and the IBA annotations should stand.")
    else:
        print("\n  Inconclusive: see the feature table above.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
