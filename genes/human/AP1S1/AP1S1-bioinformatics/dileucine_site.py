#!/usr/bin/env python3
"""Test whether human AP1S1 (sigma1A) retains the dileucine-signal binding site.

Background
----------
[DE]XXXL[LI] ("dileucine") sorting signals are not bound by any single AP subunit.
They bind the gamma-sigma1 (AP-1), alpha-sigma2 (AP-2) and delta-sigma3 (AP-3)
hemicomplexes, and NOT the homologous epsilon-sigma4 hemicomplex of AP-4
(PMID:14691137, PMID:17360967, PMID:21097499). The structural site was defined on
AP-2: hydrophobic pockets on sigma2 accept the Leu and (L/I) residues, and a basic
patch straddling the alpha/sigma2 boundary binds the acidic residue.

Mattera et al. 2011 (PMID:21097499) mutated the sigma2 pocket residues and their
homologues in sigma1A and sigma3A, and reported:

    "This is evidenced by the loss of signal binding by the sigma2 V88D or L103S
     substitutions and the homologous sigma1A V88D and I103S and sigma3A V94D and
     L109S substitutions."

and, for the basic patch, that sigma1A R15 is "a basic residue equivalent to sigma2
Arg 15".

This script tests the underlying structural claim independently: are the sigma2
dileucine-pocket positions actually conserved in sigma1A (and sigma1B/sigma1C, which
also bind these signals), and are they NOT conserved in sigma4, which does not?

sigma4 (AP4S1) is the built-in negative control: a paralog in the same PANTHER
family (PTHR11753) with a verified NEGATIVE binding phenotype. A residue-conservation
argument that cannot separate the binders from the non-binder is not evidence.

Everything is fetched live from UniProt. No results are hardcoded.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass

import requests
from Bio import Align
from Bio.Align import substitution_matrices

UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.json"

# Small subunits of the human AP complexes, plus two deep orthologues of sigma1A.
# expected_length is asserted so a silently-changed canonical sequence is caught
# rather than shifting every position in this analysis.
PROTEINS: dict[str, tuple[str, int | None]] = {
    "P61966": ("AP1S1 sigma1A (human, TARGET)", 158),
    "P56377": ("AP1S2 sigma1B (human)", 157),
    "Q96PC3": ("AP1S3 sigma1C (human)", 154),
    "P53680": ("AP2S1 sigma2 (human, structural ANCHOR)", 142),
    "Q92572": ("AP3S1 sigma3A (human)", 193),
    "Q9Y587": ("AP4S1 sigma4 (human, NEGATIVE CONTROL)", 144),
    "P61967": ("Ap1s1 sigma1A (mouse, PAINT IBD donor)", 158),
    "Q9P7N2": ("vas2 sigma1 (S. pombe, PAINT IBD donor)", 162),
    "P35181": ("APS1 sigma1 (S. cerevisiae, PAINT IBD donor)", 156),
}

# Positions named in the primary literature, in each protein's OWN numbering.
# sigma2 (P53680) is the anchor: its pocket was defined by the AP-2 core crystal
# structure with the CD4 dileucine Q-peptide, and each of these was mutated in
# PMID:21097499.
ANCHOR = "P53680"
ANCHOR_SITES: dict[int, str] = {
    15: "basic patch; binds the acidic (D/E) residue at signal position -4",
    63: "hydrophobic pocket; A63D abolishes signal binding",
    88: "hydrophobic pocket for the first Leu; V88D abolishes signal binding",
    100: "E100A largely abolishes signal binding",
    103: "hydrophobic pocket for the (L/I); L103S abolishes signal binding",
}

# Positions the paper states for sigma1A and sigma3A, used only as an independent
# cross-check on the alignment (the alignment must reproduce them).
LITERATURE_HOMOLOGUES: dict[str, dict[int, int]] = {
    # anchor sigma2 position -> stated homologous position
    "P61966": {15: 15, 63: 63, 88: 88, 103: 103},
    "Q92572": {88: 94, 103: 109},
}

MEDNIK_POSITION = 90  # sigma1A L90P, the causal MEDNIK missense variant (PMID:39269494)

# Whether each paralog's hemicomplex binds [DE]XXXL[LI] signals, from the cited
# experimental papers. None = not tested in these papers.
BINDS_DILEUCINE: dict[str, bool | None] = {
    "P61966": True,   # gamma1-sigma1A  (PMID:14691137, PMID:21097499)
    "P56377": True,   # gamma1-sigma1B  (PMID:21097499)
    "Q96PC3": True,   # gamma1-sigma1C  (PMID:21097499)
    "P53680": True,   # alphaC-sigma2   (PMID:21097499)
    "Q92572": True,   # delta-sigma3A   (PMID:14691137, PMID:21097499)
    "Q9Y587": False,  # epsilon-sigma4 does NOT bind (PMID:21097499)
    "P61967": None,
    "Q9P7N2": None,
    "P35181": None,
}


@dataclass
class Protein:
    accession: str
    label: str
    sequence: str
    sequence_version: int

    def at(self, pos: int) -> str:
        if not 1 <= pos <= len(self.sequence):
            raise IndexError(f"{self.accession}: position {pos} outside 1..{len(self.sequence)}")
        return self.sequence[pos - 1]


def fetch(acc: str, label: str, expected_length: int | None) -> Protein:
    r = requests.get(UNIPROT.format(acc=acc), timeout=60)
    r.raise_for_status()
    d = r.json()
    seq = d["sequence"]["value"]
    ver = d["entryAudit"]["sequenceVersion"]
    if expected_length is not None and len(seq) != expected_length:
        raise AssertionError(
            f"{acc} ({label}): expected {expected_length} aa, UniProt now returns {len(seq)} aa. "
            "Every position in this analysis is invalidated; re-read the record before trusting it."
        )
    return Protein(acc, label, seq, ver)


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    a.mode = "global"
    return a


def map_positions(anchor: Protein, other: Protein) -> tuple[dict[int, int | None], float]:
    """Map anchor 1-based positions onto `other` via a global pairwise alignment.

    Returns (mapping, percent identity). A mapping value of None means the anchor
    position aligns to a gap.
    """
    aln = aligner().align(anchor.sequence, other.sequence)[0]
    a_idx, b_idx = aln.indices  # 0-based, -1 for gap
    mapping: dict[int, int | None] = {}
    ident = cols = 0
    for ai, bi in zip(a_idx, b_idx):
        if ai >= 0 and bi >= 0:
            mapping[ai + 1] = bi + 1
            cols += 1
            if anchor.sequence[ai] == other.sequence[bi]:
                ident += 1
        elif ai >= 0:
            mapping[ai + 1] = None
    pid = 100.0 * ident / cols if cols else 0.0
    return mapping, pid


def main() -> int:
    print("=" * 78)
    print("AP1S1 (sigma1A) dileucine-signal binding site: residue conservation test")
    print("=" * 78)

    proteins = {
        acc: fetch(acc, label, ln) for acc, (label, ln) in PROTEINS.items()
    }
    print("\n## Sequences fetched live from UniProt\n")
    for acc, p in proteins.items():
        print(f"  {acc}  SV{p.sequence_version}  {len(p.sequence):3d} aa  {p.label}")

    anchor = proteins[ANCHOR]
    target = proteins["P61966"]

    print(f"\n## Anchor site on {ANCHOR} ({anchor.label})\n")
    for pos, role in sorted(ANCHOR_SITES.items()):
        print(f"  {anchor.at(pos)}{pos:<4} {role}")

    print("\n## Target residues named directly in the literature for sigma1A\n")
    named = {15: "R", 63: "A", 88: "V", 103: "I", MEDNIK_POSITION: "L"}
    literature_ok = True
    for pos, expected in sorted(named.items()):
        actual = target.at(pos)
        ok = actual == expected
        literature_ok &= ok
        tag = "OK " if ok else "MISMATCH"
        note = " (MEDNIK L90P variant position)" if pos == MEDNIK_POSITION else ""
        print(f"  {tag}  P61966 position {pos:<4} expected {expected}, found {actual}{note}")

    print("\n## Alignment-based mapping of the sigma2 pocket onto each paralog\n")
    header = f"  {'accession':10} {'binds':6} {'%id':>5}  " + "  ".join(
        f"{anchor.at(p)}{p}" for p in sorted(ANCHOR_SITES)
    ) + "   conserved"
    print(header)
    print("  " + "-" * (len(header) - 2))

    results: dict[str, dict] = {}
    for acc, p in proteins.items():
        if acc == ANCHOR:
            continue
        mapping, pid = map_positions(anchor, p)
        cells, n_same = [], 0
        per_site = {}
        for ap in sorted(ANCHOR_SITES):
            tp = mapping.get(ap)
            if tp is None:
                cells.append("  -")
                per_site[ap] = None
                continue
            res = p.at(tp)
            same = res == anchor.at(ap)
            n_same += same
            cells.append(f"{res}{tp}".rjust(5 if tp >= 100 else 4))
            per_site[ap] = {"position": tp, "residue": res, "identical_to_anchor": same}
        binds = BINDS_DILEUCINE[acc]
        blabel = {True: "yes", False: "NO", None: "n/d"}[binds]
        print(f"  {acc:10} {blabel:6} {pid:5.1f}  " + "  ".join(cells)
              + f"   {n_same}/{len(ANCHOR_SITES)}")
        results[acc] = {
            "label": p.label, "percent_identity_to_sigma2": round(pid, 1),
            "binds_dileucine": binds, "sites": per_site,
            "identical_at_anchor_sites": n_same,
        }

    print("\n## Cross-check: does the alignment reproduce the positions the paper states?\n")
    alignment_ok = True
    for acc, stated in LITERATURE_HOMOLOGUES.items():
        mapping, _ = map_positions(anchor, proteins[acc])
        for ap, expected_tp in stated.items():
            got = mapping.get(ap)
            ok = got == expected_tp
            alignment_ok &= ok
            print(f"  {'OK ' if ok else 'MISMATCH'}  sigma2 {ap} -> {acc} {got} "
                  f"(paper states {expected_tp})")

    print("\n## Verdict\n")
    tgt = results["P61966"]
    binders = [a for a, r in results.items() if r["binds_dileucine"] is True]
    nonbinder = [a for a, r in results.items() if r["binds_dileucine"] is False]
    print(f"  sigma1A identity to sigma2 anchor sites: "
          f"{tgt['identical_at_anchor_sites']}/{len(ANCHOR_SITES)}")
    if binders:
        lo = min(results[a]["identical_at_anchor_sites"] for a in binders)
        print(f"  verified binders (n={len(binders)}): >= {lo}/{len(ANCHOR_SITES)} identical")
    for a in nonbinder:
        print(f"  verified NON-binder {a} ({results[a]['label']}): "
              f"{results[a]['identical_at_anchor_sites']}/{len(ANCHOR_SITES)} identical")
    discriminates = bool(nonbinder) and all(
        results[a]["identical_at_anchor_sites"] < min(
            results[b]["identical_at_anchor_sites"] for b in binders)
        for a in nonbinder
    )
    print(f"\n  literature residues verified against P61966 : {literature_ok}")
    print(f"  alignment reproduces stated homologies      : {alignment_ok}")
    print(f"  site separates binders from the non-binder  : {discriminates}")
    if not discriminates:
        print("\n  NOTE: the pocket does NOT cleanly separate binders from sigma4 by identity")
        print("  alone. The conservation argument is therefore weaker than it looks, and the")
        print("  direct mutagenesis of sigma1A itself (PMID:21097499) carries the claim.")

    with open("results.json", "w") as fh:
        json.dump(
            {"anchor": ANCHOR, "anchor_sites": ANCHOR_SITES, "proteins": results,
             "literature_residues_verified": literature_ok,
             "alignment_reproduces_literature": alignment_ok,
             "site_discriminates_binders": discriminates},
            fh, indent=2, default=str,
        )
    print("\n  wrote results.json")
    return 0 if literature_ok and alignment_ok else 1


if __name__ == "__main__":
    sys.exit(main())
