#!/usr/bin/env python3
"""Two questions about human AP3S1 (sigma3A) and the AP-3 dileucine cargo-signal site.

Background
----------
Acidic dileucine sorting signals (the (D/E)XXXL(L/I) motif) are not bound by any single
AP subunit. They bind the gamma1-sigma1A (AP-1), alphaC-sigma2 (AP-2) and delta-sigma3
(AP-3) hemicomplexes, but not the homologous epsilon-sigma4 hemicomplex of AP-4
(PMID:14691137, PMID:17360967, PMID:21097499). The site was defined structurally on AP-2:
hydrophobic pockets on sigma2 accept the Leu and (L/I) residues, and basic residues
straddling the alpha/sigma2 boundary bind the acidic residue at signal position -4.

Mattera et al. 2011 (PMID:21097499) transferred that site onto AP-1 and AP-3 by
mutagenesis and reported, for sigma3A specifically:

    "This is evidenced by the loss of signal binding by the sigma2 V88D or L103S
     substitutions and the homologous sigma1A V88D and I103S and sigma3A V94D and
     L109S substitutions."

    "In contrast, substitution of the corresponding residues in sigma3A (Arg 15 and
     Leu 107) decreased the interaction of (D/E) XXX L(L/I) signals with delta-sigma3A"

Questions
---------
1. Do the sigma3A residues the paper names (R15, V94, D98, L107, L109) actually occur at
   those positions in the current UniProt sequence of Q92572, and does an independent
   alignment reproduce the sigma2 88 -> sigma3A 94 and sigma2 103 -> sigma3A 109
   correspondences the paper asserts?

2. Can sigma3A (AP3S1) be told apart from sigma3B (AP3S2) at this site? GOA gives the two
   paralogs near-identical annotation sets, and PMID:14691137 found that both delta-sigma3A
   and delta-sigma3B bind the LIMP-II dileucine signal. If the pocket is identical between
   them, that interchangeability is a property of the proteins rather than a gap in
   curation.

sigma4 (AP4S1, Q9Y587) is the built-in negative control: same PANTHER family (PTHR11753),
verified NEGATIVE binding phenotype. A residue-conservation argument that cannot separate
the binders from the non-binder is not evidence, and including sigma4 is what makes that
testable rather than assumed.

Everything is fetched live from UniProt. No result is hardcoded.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass

import requests
from Bio import Align
from Bio.Align import substitution_matrices

UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.json"

# expected_length is asserted so a silently re-released canonical sequence aborts the run
# instead of shifting every position in this analysis.
PROTEINS: dict[str, tuple[str, int]] = {
    "Q92572": ("AP3S1 sigma3A (human, TARGET)", 193),
    "P59780": ("AP3S2 sigma3B (human, paralog under test)", 193),
    "P53680": ("AP2S1 sigma2 (human, structural ANCHOR)", 142),
    "P61966": ("AP1S1 sigma1A (human)", 158),
    "P56377": ("AP1S2 sigma1B (human)", 157),
    "Q96PC3": ("AP1S3 sigma1C (human)", 154),
    "Q9Y587": ("AP4S1 sigma4 (human, NEGATIVE CONTROL)", 144),
    "Q9DCR2": ("Ap3s1 sigma3A (mouse, 1:1 ortholog and Ensembl-Compara donor)", 193),
    "P47064": ("APS3 sigma3 (S. cerevisiae, PAINT IBD donor)", 194),
    "Q59QC5": ("APS3 sigma3 (C. albicans, PAINT IBD donor)", 175),
}

TARGET = "Q92572"
PARALOG = "P59780"
ANCHOR = "P53680"

# Anchor positions on sigma2, in sigma2's own numbering. Each was mutated in
# PMID:21097499; the pocket itself comes from the AP-2 core structure with the CD4
# dileucine Q-peptide.
ANCHOR_SITES: dict[int, str] = {
    15: "basic patch; binds the acidic (D/E) residue at signal position -4",
    63: "hydrophobic pocket; A63D abolishes signal binding",
    88: "hydrophobic pocket for the first Leu; V88D abolishes signal binding",
    100: "E100A largely abolishes signal binding",
    103: "hydrophobic pocket for the (L/I); L103S abolishes signal binding",
}

# Residues the primary literature names for sigma3A itself, in Q92572 numbering.
LITERATURE_SIGMA3A: dict[int, tuple[str, str]] = {
    15: ("R", "sigma3A Arg 15; R15E reduces signal binding (PMID:21097499)"),
    94: ("V", "sigma3A V94D abolishes signal binding (PMID:21097499)"),
    98: ("D", "sigma3A D98A, signal-dependent effect on tyrosinase (PMID:21097499)"),
    107: ("L", "sigma3A L107, substitution decreases binding (PMID:21097499)"),
    109: ("L", "sigma3A L109S abolishes signal binding (PMID:21097499)"),
}

# Correspondences the paper states, used purely as an independent check on the alignment.
LITERATURE_HOMOLOGUES: dict[str, dict[int, int]] = {
    # anchor sigma2 position -> stated homologous position in that protein
    "Q92572": {88: 94, 103: 109},
    "P61966": {88: 88, 103: 103},
}

# Whether each paralog's hemicomplex binds (D/E)XXXL(L/I) signals, from the cited papers.
# None = not tested in those papers.
BINDS_DILEUCINE: dict[str, bool | None] = {
    "Q92572": True,   # delta-sigma3A  (PMID:14691137, PMID:21097499, PMID:16162817)
    "P59780": True,   # delta-sigma3B  (PMID:14691137, LIMP-II tail)
    "P53680": True,   # alphaC-sigma2  (PMID:21097499)
    "P61966": True,   # gamma1-sigma1A (PMID:14691137, PMID:21097499)
    "P56377": True,   # gamma1-sigma1B (PMID:21097499)
    "Q96PC3": True,   # gamma1-sigma1C (PMID:21097499)
    "Q9Y587": False,  # epsilon-sigma4 does NOT bind (PMID:14691137, PMID:21097499)
    "Q9DCR2": None,
    "P47064": None,
    "Q59QC5": None,
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


def fetch(acc: str, label: str, expected_length: int) -> Protein:
    r = requests.get(UNIPROT.format(acc=acc), timeout=60)
    r.raise_for_status()
    d = r.json()
    seq = d["sequence"]["value"]
    ver = d["entryAudit"]["sequenceVersion"]
    if len(seq) != expected_length:
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
    """Map anchor 1-based positions onto `other` by global pairwise alignment.

    Returns (mapping, percent identity over aligned columns). A value of None means the
    anchor position aligns to a gap.
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
    print("AP3S1 (sigma3A): the AP-3 dileucine cargo-signal pocket, and sigma3A vs sigma3B")
    print("=" * 78)

    proteins = {acc: fetch(acc, label, ln) for acc, (label, ln) in PROTEINS.items()}
    print("\n## Sequences fetched live from UniProt\n")
    for acc, p in proteins.items():
        print(f"  {acc}  SV{p.sequence_version}  {len(p.sequence):3d} aa  {p.label}")

    anchor = proteins[ANCHOR]
    target = proteins[TARGET]
    paralog = proteins[PARALOG]

    print(f"\n## Anchor site on {ANCHOR} ({anchor.label})\n")
    for pos, role in sorted(ANCHOR_SITES.items()):
        print(f"  {anchor.at(pos)}{pos:<4} {role}")

    print("\n## Q1a. Residues the literature names for sigma3A, checked on the live sequence\n")
    literature_ok = True
    for pos, (expected, role) in sorted(LITERATURE_SIGMA3A.items()):
        actual = target.at(pos)
        ok = actual == expected
        literature_ok &= ok
        print(f"  {'OK ' if ok else 'MISMATCH'}  {TARGET} position {pos:<4} "
              f"expected {expected}, found {actual}   [{role}]")

    print("\n## Q1b. Does an independent alignment reproduce the stated correspondences?\n")
    alignment_ok = True
    for acc, stated in LITERATURE_HOMOLOGUES.items():
        mapping, _ = map_positions(anchor, proteins[acc])
        for ap, expected_tp in stated.items():
            got = mapping.get(ap)
            ok = got == expected_tp
            alignment_ok &= ok
            print(f"  {'OK ' if ok else 'MISMATCH'}  sigma2 {ap} -> {acc} {got} "
                  f"(paper states {expected_tp})")

    print("\n## Q2a. The sigma2 pocket mapped onto every paralog\n")
    header = (f"  {'accession':10} {'binds':6} {'%id':>5}  "
              + "  ".join(f"{anchor.at(p)}{p}" for p in sorted(ANCHOR_SITES))
              + "   identical")
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
            "label": p.label,
            "percent_identity_to_sigma2": round(pid, 1),
            "binds_dileucine": binds,
            "sites": per_site,
            "identical_at_anchor_sites": n_same,
        }

    print("\n## Q2b. sigma3A (AP3S1) against sigma3B (AP3S2), directly\n")
    s3_map, s3_pid = map_positions(target, paralog)
    print(f"  global identity sigma3A vs sigma3B : {s3_pid:.1f}%  "
          f"({len(target.sequence)} aa vs {len(paralog.sequence)} aa)")
    pocket_rows = []
    pocket_identical = True
    for pos, (expected, _role) in sorted(LITERATURE_SIGMA3A.items()):
        tp = s3_map.get(pos)
        pres = paralog.at(tp) if tp is not None else None
        same = pres == target.at(pos)
        pocket_identical &= bool(same)
        pocket_rows.append({
            "sigma3A_position": pos, "sigma3A_residue": target.at(pos),
            "sigma3B_position": tp, "sigma3B_residue": pres, "identical": bool(same),
        })
        print(f"    sigma3A {target.at(pos)}{pos:<4} -> sigma3B "
              f"{pres if pres else '-'}{tp if tp else ''}   "
              f"{'identical' if same else 'DIFFERENT'}")
    print(f"\n  all five literature-named sigma3A positions identical in sigma3B: {pocket_identical}")

    print("\n## Q3. sigma3A against its mouse 1:1 ortholog (the Ensembl-Compara / ISS donor)\n")
    mouse = proteins["Q9DCR2"]
    m_map, m_pid = map_positions(target, mouse)
    print(f"  global identity human AP3S1 vs mouse Ap3s1 : {m_pid:.1f}%  "
          f"({len(target.sequence)} aa vs {len(mouse.sequence)} aa)")
    ortholog_rows = []
    for pos, (_expected, _role) in sorted(LITERATURE_SIGMA3A.items()):
        tp = m_map.get(pos)
        mres = mouse.at(tp) if tp is not None else None
        ortholog_rows.append({
            "human_position": pos, "human_residue": target.at(pos),
            "mouse_position": tp, "mouse_residue": mres,
            "identical": bool(mres == target.at(pos)),
        })
    print("  pocket positions identical in the mouse ortholog: "
          f"{sum(r['identical'] for r in ortholog_rows)}/{len(ortholog_rows)}")

    print("\n## Verdict\n")
    tgt = results[TARGET]
    binders = [a for a, r in results.items() if r["binds_dileucine"] is True]
    nonbinders = [a for a, r in results.items() if r["binds_dileucine"] is False]
    print(f"  sigma3A identity to the sigma2 anchor sites : "
          f"{tgt['identical_at_anchor_sites']}/{len(ANCHOR_SITES)}")
    if binders:
        lo = min(results[a]["identical_at_anchor_sites"] for a in binders)
        print(f"  verified binders (n={len(binders)})                   : "
              f">= {lo}/{len(ANCHOR_SITES)} identical")
    for a in nonbinders:
        print(f"  verified NON-binder {a} ({results[a]['label']}): "
              f"{results[a]['identical_at_anchor_sites']}/{len(ANCHOR_SITES)} identical")
    discriminates = bool(nonbinders) and bool(binders) and all(
        results[a]["identical_at_anchor_sites"]
        < min(results[b]["identical_at_anchor_sites"] for b in binders)
        for a in nonbinders
    )
    print(f"\n  literature residues verified against {TARGET}  : {literature_ok}")
    print(f"  alignment reproduces stated homologies       : {alignment_ok}")
    print(f"  site separates binders from the non-binder   : {discriminates}")
    if not discriminates:
        print("\n  NOTE: identity at this pocket does NOT separate the verified binders from")
        print("  sigma4, the verified non-binder. Conservation alone is therefore not evidence")
        print("  that sigma3A binds these signals; the direct sigma3A mutagenesis in")
        print("  PMID:21097499 is what carries that claim.")
    if pocket_identical:
        print("\n  NOTE: sigma3A and sigma3B are identical at every literature-named pocket")
        print("  position, so no sequence feature of this site distinguishes them. Their")
        print("  shared annotation in GOA reflects that, rather than a curation shortcut.")

    payload = {
        "anchor": ANCHOR,
        "anchor_sites": ANCHOR_SITES,
        "target": TARGET,
        "proteins": results,
        "sigma3A_vs_sigma3B": {
            "global_percent_identity": round(s3_pid, 1),
            "pocket_positions": pocket_rows,
            "pocket_identical": pocket_identical,
        },
        "human_vs_mouse_ortholog": {
            "global_percent_identity": round(m_pid, 1),
            "pocket_positions": ortholog_rows,
        },
        "literature_residues_verified": literature_ok,
        "alignment_reproduces_literature": alignment_ok,
        "site_discriminates_binders": discriminates,
    }
    with open("results.json", "w") as fh:
        json.dump(payload, fh, indent=2, default=str)
    print("\n  wrote results.json")
    return 0 if literature_ok and alignment_ok else 1


if __name__ == "__main__":
    sys.exit(main())
