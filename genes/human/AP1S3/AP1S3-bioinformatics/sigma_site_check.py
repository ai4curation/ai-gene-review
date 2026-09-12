#!/usr/bin/env python3
"""Check the AP-1 sigma-subunit residue positions reported in two structural
papers against the live UniProt sequences of AP1S3 and its paralogues.

Two things are tested, both by direct sequence lookup (no hardcoded answers):

1. IDENTITY. PMID:36261523 (2.34 A cryo-EM, PDB 7R4H) and PMID:40752490
   (1.68 A X-ray, PDB 9DDT) both describe an "AP-1 sigma" / "AP1sigma3"
   chain by residue number. Do those numbers resolve, in Q96PC3 (AP1S3)
   numbering, to the residues the papers name?

2. DISCRIMINATION. If the same integer positions resolve to the same residues
   in AP1S1 / AP1S2 / AP2S1, the numbering alone would not identify which
   sigma paralogue was crystallised. Report, per site, the residue each
   paralogue carries at (a) the same integer position and (b) the position
   that actually aligns to the AP1S3 site in a global pairwise alignment.

Run:  uv run python sigma_site_check.py
"""
from __future__ import annotations

import io
import json
import sys
from dataclasses import dataclass

import requests
from Bio import Align
from Bio.Align import substitution_matrices

UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.fasta"

TARGET = "Q96PC3"  # AP1S3 / sigma-1C
PARALOGS = {
    "P61966": "AP1S1 (sigma-1A)",
    "P56377": "AP1S2 (sigma-1B)",
    "P53680": "AP2S1 (sigma-2)",
}
EXPECTED_LENGTH = {"Q96PC3": 154, "P61966": 158, "P56377": 157, "P53680": 142}

# (position, residue asserted by the paper, role, source)
SITES: list[tuple[int, str, str, str]] = [
    # PMID:36261523 - AP-1 sigma contacts to phospho-STING CTT
    (60, "K", "H-bonds the pS366 phospho-moiety of STING", "PMID:36261523"),
    (61, "R", "H-bonds the pS366 phospho-moiety of STING", "PMID:36261523"),
    (65, "L", "hydrophobic contact to STING L364/I365 (EXXXLI)", "PMID:36261523"),
    (67, "F", "hydrophobic contact to STING L364/I365 (EXXXLI)", "PMID:36261523"),
    (85, "H", "hydrophobic contact to STING L364/I365 (EXXXLI)", "PMID:36261523"),
    (88, "V", "hydrophobic contact to STING L364/I365; V88D abolishes binding", "PMID:36261523"),
    (98, "V", "hydrophobic contact to STING L364/I365 (EXXXLI)", "PMID:36261523"),
    (103, "I", "dileucine-recognition residue; I103S abolishes binding", "PMID:36261523"),
    # PMID:40752490 - AAGAB pseudoGTPase domain interface
    (10, "R", "salt bridge with AAGAB E155; H-bond with AAGAB Q128", "PMID:40752490"),
    (13, "K", "salt bridge with AAGAB E108 (beta1-beta2 loop)", "PMID:40752490"),
    (40, "L", "hydrophobic contact with AAGAB I132 (H1 helix)", "PMID:40752490"),
    (41, "S", "hydrophobic contact with AAGAB I132 (H1 helix)", "PMID:40752490"),
    (61, "R", "salt bridge with AAGAB D151; H-bond to AAGAB F153 carbonyl", "PMID:40752490"),
    (62, "Y", "lines the hydrophobic pocket that receives AAGAB F153", "PMID:40752490"),
    (63, "A", "mainchain N H-bond to AAGAB F153 carbonyl", "PMID:40752490"),
    (88, "V", "lines the hydrophobic pocket that receives AAGAB F153", "PMID:40752490"),
    (98, "V", "lines the pocket; shifts ~2.6 A to occlude the L0 site", "PMID:40752490"),
    (101, "L", "hydrophobic contact with AAGAB A168", "PMID:40752490"),
    (104, "L", "hydrophobic contact with AAGAB A168", "PMID:40752490"),
    (124, "Q", "start of the C-terminal helix unmodelled in 9DDT (Q124-R154)", "PMID:40752490"),
    (154, "R", "last residue of the C-terminal helix unmodelled in 9DDT", "PMID:40752490"),
    # PMID:24791904 - pustular psoriasis variants
    (4, "F", "hydrophobic core; p.Phe4Cys destabilises the protein", "PMID:24791904"),
    (33, "R", "sigma1C/mu1A interface; p.Arg33Trp weakens the interaction", "PMID:24791904"),
]


@dataclass
class Seq:
    acc: str
    header: str
    seq: str


def fetch(acc: str) -> Seq:
    r = requests.get(UNIPROT.format(acc=acc), timeout=60)
    r.raise_for_status()
    lines = r.text.strip().splitlines()
    header = lines[0]
    seq = "".join(lines[1:])
    return Seq(acc=acc, header=header, seq=seq)


def residue(seq: str, pos: int) -> str | None:
    """1-based residue lookup; None if the position is past the end."""
    if pos < 1 or pos > len(seq):
        return None
    return seq[pos - 1]


def align(a: str, b: str):
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    return aligner.align(a, b)[0]


def aligned_position_map(aln) -> dict[int, int]:
    """Map 1-based query positions to 1-based target positions for an alignment."""
    out: dict[int, int] = {}
    for (qs, qe), (ts, te) in zip(aln.aligned[0], aln.aligned[1]):
        for off in range(qe - qs):
            out[qs + off + 1] = ts + off + 1
    return out


def main() -> int:
    seqs = {TARGET: fetch(TARGET)}
    for acc in PARALOGS:
        seqs[acc] = fetch(acc)

    print("# Sequences fetched live from UniProt\n")
    lengths_ok = True
    for acc, s in seqs.items():
        expected = EXPECTED_LENGTH[acc]
        ok = len(s.seq) == expected
        lengths_ok &= ok
        name = "AP1S3 (sigma-1C, the target)" if acc == TARGET else PARALOGS[acc]
        print(f"  {acc}  {name}: {len(s.seq)} aa (expected {expected}) "
              f"{'OK' if ok else 'LENGTH MISMATCH'}")
    if not lengths_ok:
        print("\nRefusing to score sites: a fetched sequence is not the expected length.")
        return 2

    target = seqs[TARGET].seq
    maps = {acc: aligned_position_map(align(target, seqs[acc].seq)) for acc in PARALOGS}

    print("\n# Test 1 - do the published positions resolve in AP1S3 (Q96PC3) numbering?\n")
    hits = misses = 0
    rows = []
    for pos, expect, role, src in SITES:
        got = residue(target, pos)
        ok = got == expect
        hits += ok
        misses += (not ok)
        rows.append((pos, expect, got, ok, role, src))
        print(f"  {src}  {expect}{pos:<4} -> AP1S3 has {got}   {'MATCH' if ok else 'MISMATCH'}")
    print(f"\n  {hits}/{hits + misses} published positions match AP1S3's own sequence.")

    mismatched = [r for r in rows if not r[3]]
    if mismatched:
        print("\n  Mismatched sites, with what each paralogue carries at the same position:")
        for pos, expect, got, ok, role, src in mismatched:
            cells = ", ".join(
                f"{PARALOGS[a].split()[0]}={residue(seqs[a].seq, pos) or '-'}{pos}"
                for a in PARALOGS)
            print(f"    {src} says {expect}{pos}; AP1S3={got}{pos}; {cells}")

    print("\n# Test 2 - does the same numbering also fit the paralogues?\n")
    print("  site        | " + " | ".join(
        f"{PARALOGS[a].split()[0]}: same-pos / aligned-pos" for a in PARALOGS))
    same_pos_agree = {a: 0 for a in PARALOGS}
    aligned_agree = {a: 0 for a in PARALOGS}
    n_sites = 0
    for pos, expect, got, ok, role, src in rows:
        if not ok:
            continue
        n_sites += 1
        cells = []
        for acc in PARALOGS:
            pseq = seqs[acc].seq
            sp = residue(pseq, pos)
            ap_pos = maps[acc].get(pos)
            ap = residue(pseq, ap_pos) if ap_pos else None
            same_pos_agree[acc] += (sp == expect)
            aligned_agree[acc] += (ap == expect)
            cells.append(f"{sp or '-'}{pos} / {ap or '-'}{ap_pos if ap_pos else '-'}")
        print(f"  {expect}{pos:<4}       | " + " | ".join(f"{c:<24}" for c in cells))

    print(f"\n  Of {n_sites} AP1S3 sites:")
    for acc in PARALOGS:
        print(f"    {PARALOGS[acc]}: {same_pos_agree[acc]}/{n_sites} carry the same residue at the "
              f"same integer position; {aligned_agree[acc]}/{n_sites} at the ALIGNED position.")

    print("\n# Test 3 - pairwise identity to AP1S3\n")
    for acc in PARALOGS:
        aln = align(target, seqs[acc].seq)
        ident = sum(1 for a, b in zip(str(aln[0]), str(aln[1])) if a == b and a != "-")
        print(f"  AP1S3 vs {PARALOGS[acc]}: {ident} identities over "
              f"{len(str(aln[0]))} alignment columns "
              f"({100.0 * ident / min(len(target), len(seqs[acc].seq)):.1f}% of the shorter sequence)")

    json.dump(
        {
            "target": TARGET,
            "lengths": {a: len(s.seq) for a, s in seqs.items()},
            "sites_matching_target": hits,
            "sites_total": hits + misses,
            "same_position_agreement": same_pos_agree,
            "aligned_position_agreement": aligned_agree,
            "n_sites_scored": n_sites,
        },
        open("results.json", "w"),
        indent=2,
    )
    print("\nWrote results.json")
    return 0 if misses == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
