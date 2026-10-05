"""Is the dileucine-signal basic patch complete in the AP-4 epsilon-sigma4 hemicomplex?

Background (all from PMID:21097499, Mattera et al., J Biol Chem 2011):

  "This site consists of hydrophobic pockets on sigma2 that fit the Leu and (L/I)
  residues, and a basic patch straddling the boundary of alpha and sigma2 that might
  bind the Gln, phosphorylated Ser, or (D/E) residues of the signals"

so the acidic (D/E) position of a [DE]XXXL[LI] signal is read by TWO basic residues,
one on the large subunit and one on the sigma subunit. The paper names the large-subunit
residue in each binding complex -- gamma1 Arg15 (AP-1), alphaC Arg21 (AP-2), delta Arg26
(AP-3) -- and the sigma-subunit residue as Arg15 in sigma1A, sigma2 and sigma3A. It also
reports that the epsilon-sigma4 hemicomplex of AP-4 does NOT bind any of the three
signals tested.

`genes/human/AP1S1/AP1S1-bioinformatics/` already showed that sigma4 scores as well as
the verified binders at the five sigma-side pocket positions, so the sigma half of the
site cannot explain the AP-4 negative. This script asks the complementary question that
analysis left open: **is the large-subunit half of the basic patch present in epsilon?**

Two independent tests, and the script refuses to answer if the first fails:

  Test 1 (method control). Map each of the three verified large-subunit anchors onto the
  other two by pairwise alignment. The paper states these three positions are equivalent,
  so a correct alignment must recover gamma1 R15 <-> alphaC R21 <-> delta R26. If it does
  not, full-length pairwise alignment cannot place this region across the large adaptins
  at their level of divergence, and the script exits 2 without reporting Test 2.

  Test 2 (the question). Map the same three anchors onto epsilon (AP4E1) and report the
  epsilon residue at each mapped position, plus the local window.

Also re-derives the sigma side independently: maps sigma2 Arg15 onto sigma1A, sigma3A and
sigma4, so the two halves are scored by one method in one run.

Everything is fetched live from the UniProt REST API. Expected sequence lengths are
asserted, so a re-released canonical sequence aborts the run rather than silently
shifting every position. Nothing is hardcoded, and an inconclusive result is reported as
inconclusive.

Exit codes: 0 = both tests ran; 2 = a fetched sequence was not the expected length or the
method control failed (Test 2 then not reported).
"""

from __future__ import annotations

import json
import sys
import urllib.request
from dataclasses import dataclass

from Bio import Align
from Bio.Align import substitution_matrices

UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.fasta"

BASIC = set("RK")


@dataclass(frozen=True)
class Protein:
    acc: str
    label: str
    expected_len: int


# Large subunits. The three anchors are the basic residues named in PMID:21097499;
# epsilon is the subunit whose hemicomplex with sigma4 tested negative there.
GAMMA1 = Protein("O43747", "gamma1 (AP1G1)", 822)
ALPHA_C = Protein("O94973", "alphaC (AP2A2)", 939)
DELTA = Protein("O14617", "delta (AP3D1)", 1153)
EPSILON = Protein("Q9UPM8", "epsilon (AP4E1)", 1137)

LARGE_ANCHORS = {GAMMA1: 15, ALPHA_C: 21, DELTA: 26}

# Small subunits. sigma2 is the structurally defined anchor (PMID:21097499 cites the
# AP-2 core / CD4 Q-peptide structure for the patch); sigma4 is the subunit under review.
SIGMA2 = Protein("P53680", "sigma2 (AP2S1)", 142)
SIGMA1A = Protein("P61966", "sigma1A (AP1S1)", 158)
SIGMA3A = Protein("Q92572", "sigma3A (AP3S1)", 193)
SIGMA4 = Protein("Q9Y587", "sigma4 (AP4S1)", 144)

SIGMA_ANCHOR_POS = 15  # sigma2 Arg15


def fetch(protein: Protein) -> str:
    with urllib.request.urlopen(
        urllib.request.Request(
            UNIPROT.format(acc=protein.acc),
            headers={"User-Agent": "ai-gene-review AP4S1 analysis"},
        ),
        timeout=120,
    ) as handle:
        text = handle.read().decode()
    seq = "".join(line for line in text.splitlines() if not line.startswith(">"))
    if len(seq) != protein.expected_len:
        print(
            f"ABORT: {protein.acc} ({protein.label}) is {len(seq)} aa, expected "
            f"{protein.expected_len}. The canonical sequence changed; every position in "
            f"this analysis is anchored to the old numbering and must be re-checked.",
            file=sys.stderr,
        )
        sys.exit(2)
    return seq


def aligner() -> Align.PairwiseAligner:
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -11
    al.extend_gap_score = -1
    al.mode = "global"
    return al


def map_position(al: Align.PairwiseAligner, src: str, dst: str, src_pos: int):
    """Map 1-based src_pos onto dst through the best global alignment.

    Returns (dst_pos, dst_residue) or (None, None) if src_pos aligns to a gap.
    """
    alignment = al.align(src, dst)[0]
    src_blocks, dst_blocks = alignment.aligned
    for (s0, s1), (d0, d1) in zip(src_blocks, dst_blocks):
        if s0 <= src_pos - 1 < s1:
            dst_idx = int(d0) + (src_pos - 1 - int(s0))
            return dst_idx + 1, dst[dst_idx]
    return None, None


def identity(al: Align.PairwiseAligner, a: str, b: str) -> float:
    alignment = al.align(a, b)[0]
    matches = sum(
        1
        for (s0, s1), (d0, d1) in zip(*alignment.aligned)
        for i in range(s1 - s0)
        if a[s0 + i] == b[d0 + i]
    )
    return 100.0 * matches / min(len(a), len(b))


def window(seq: str, pos: int, flank: int = 6) -> str:
    lo, hi = max(0, pos - 1 - flank), min(len(seq), pos + flank)
    left, centre, right = seq[lo : pos - 1], seq[pos - 1], seq[pos:hi]
    return f"{left}[{centre}]{right}"


def main() -> int:
    al = aligner()
    results: dict = {"tests": {}}

    print(__doc__.split("Exit codes")[0].strip()[:0] or "", end="")
    print("=" * 78)
    print("AP4S1 / AP-4: is the large-subunit half of the dileucine basic patch present?")
    print("=" * 78)

    large = {p: fetch(p) for p in (GAMMA1, ALPHA_C, DELTA, EPSILON)}
    small = {p: fetch(p) for p in (SIGMA2, SIGMA1A, SIGMA3A, SIGMA4)}
    print("\nSequences fetched live and length-asserted:")
    for p, s in list(large.items()) + list(small.items()):
        print(f"  {p.acc}  {p.label:<18} {len(s):>5} aa")
    results["sequence_lengths"] = {
        p.acc: len(s) for p, s in list(large.items()) + list(small.items())
    }

    # --- sanity: each anchor really is the residue the paper names -------------------
    print("\nAnchor residues stated by PMID:21097499, checked against the live sequence:")
    anchor_ok = True
    for p, pos in LARGE_ANCHORS.items():
        res = large[p][pos - 1]
        ok = res == "R"
        anchor_ok &= ok
        print(f"  {p.label:<18} position {pos:>3}: {res}  {'OK' if ok else 'MISMATCH'}")
    res = small[SIGMA2][SIGMA_ANCHOR_POS - 1]
    anchor_ok &= res == "R"
    print(
        f"  {SIGMA2.label:<18} position {SIGMA_ANCHOR_POS:>3}: {res}  "
        f"{'OK' if res == 'R' else 'MISMATCH'}"
    )
    results["anchors_verbatim"] = anchor_ok
    if not anchor_ok:
        print("\nABORT: a published anchor position does not hold in the live sequence.")
        return 2

    # --- Test 1: method control ------------------------------------------------------
    print("\n" + "-" * 78)
    print("TEST 1 (method control): do the three verified anchors map onto each other?")
    print("-" * 78)
    control = []
    anchors = list(LARGE_ANCHORS.items())
    for src, src_pos in anchors:
        for dst, dst_pos in anchors:
            if src is dst:
                continue
            got_pos, got_res = map_position(al, large[src], large[dst], src_pos)
            ok = got_pos == dst_pos
            control.append(
                {
                    "from": src.label,
                    "from_pos": src_pos,
                    "to": dst.label,
                    "expected_pos": dst_pos,
                    "got_pos": got_pos,
                    "got_residue": got_res,
                    "agrees": ok,
                }
            )
            print(
                f"  {src.label:<18} R{src_pos:<4} -> {dst.label:<18} "
                f"expected {dst_pos:<4} got {str(got_pos):<6} ({got_res}) "
                f"{'AGREES' if ok else 'DISAGREES'}"
            )
    results["tests"]["control"] = control
    n_ok = sum(1 for c in control if c["agrees"])
    print(f"\n  control pairs agreeing: {n_ok}/{len(control)}")

    print("\n  pairwise identity between the large subunits (BLOSUM62 global):")
    pid = {}
    names = [GAMMA1, ALPHA_C, DELTA, EPSILON]
    for i, a in enumerate(names):
        for b in names[i + 1 :]:
            v = identity(al, large[a], large[b])
            pid[f"{a.acc}/{b.acc}"] = round(v, 1)
            print(f"    {a.label:<18} vs {b.label:<18} {v:5.1f}%")
    results["large_subunit_identity_pct"] = pid

    if n_ok != len(control):
        print(
            "\nINCONCLUSIVE: full-length pairwise alignment does not reproduce the "
            "equivalences that PMID:21097499 states between the three verified "
            "large-subunit anchors. The mapping method is therefore not trustworthy at "
            "this level of divergence, and Test 2 is NOT reported. A structure-based "
            "superposition on the AP-4 core (PMID:41565640) would be required instead."
        )
        results["verdict"] = "INCONCLUSIVE_CONTROL_FAILED"
        _write(results)
        return 2

    # --- Test 2: the question --------------------------------------------------------
    print("\n" + "-" * 78)
    print("TEST 2: what residue does epsilon (AP4E1) carry at the mapped patch position?")
    print("-" * 78)
    eps_rows = []
    for src, src_pos in anchors:
        got_pos, got_res = map_position(al, large[src], large[EPSILON], src_pos)
        basic = got_res in BASIC if got_res else None
        eps_rows.append(
            {
                "anchor": src.label,
                "anchor_pos": src_pos,
                "epsilon_pos": got_pos,
                "epsilon_residue": got_res,
                "is_basic": basic,
                "epsilon_window": window(large[EPSILON], got_pos) if got_pos else None,
            }
        )
        print(
            f"  from {src.label:<18} R{src_pos:<4} -> epsilon position "
            f"{str(got_pos):<6} residue {str(got_res):<4} "
            f"{'BASIC' if basic else 'not basic' if got_res else 'aligns to a gap'}"
        )
        if got_pos:
            print(f"      epsilon context: {window(large[EPSILON], got_pos)}")
    results["tests"]["epsilon"] = eps_rows

    print("\n  for comparison, the same window in each verified large subunit:")
    for p, pos in anchors:
        print(f"    {p.label:<18} {window(large[p], pos)}")

    # --- sigma side, same method -----------------------------------------------------
    print("\n" + "-" * 78)
    print("SIGMA SIDE (same method): sigma2 Arg15 mapped onto the sigma paralogs")
    print("-" * 78)
    sigma_rows = []
    for dst in (SIGMA1A, SIGMA3A, SIGMA4):
        got_pos, got_res = map_position(al, small[SIGMA2], small[dst], SIGMA_ANCHOR_POS)
        basic = got_res in BASIC if got_res else None
        sigma_rows.append(
            {
                "sigma": dst.label,
                "accession": dst.acc,
                "position": got_pos,
                "residue": got_res,
                "is_basic": basic,
            }
        )
        print(
            f"  sigma2 R15 -> {dst.label:<18} position {str(got_pos):<5} residue "
            f"{str(got_res):<4} {'BASIC' if basic else 'not basic'}"
        )
    results["tests"]["sigma"] = sigma_rows

    # --- verdict ---------------------------------------------------------------------
    print("\n" + "=" * 78)
    eps_basic = [r for r in eps_rows if r["is_basic"]]
    sigma4_row = next(r for r in sigma_rows if r["accession"] == SIGMA4.acc)
    if eps_basic:
        verdict = "EPSILON_RETAINS_BASIC"
        print(
            f"VERDICT: epsilon carries a basic residue at {len(eps_basic)}/{len(eps_rows)} "
            "of the mapped anchor positions, so a missing large-subunit basic residue "
            "does NOT explain why the epsilon-sigma4 hemicomplex fails to bind "
            "(D/E)XXXL(L/I) signals."
        )
    else:
        verdict = "EPSILON_LACKS_BASIC"
        print(
            "VERDICT: epsilon carries no basic residue at any of the three mapped anchor "
            "positions, whereas sigma4 does retain the sigma-side Arg. The basic patch "
            "that reads the acidic (D/E) position of a dileucine signal is therefore "
            "HALF-COMPLETE in AP-4: present on sigma4, absent on epsilon. This is a "
            "hypothesis consistent with the measured non-binding of epsilon-sigma4 "
            "(PMID:21097499); it is not a test of it."
        )
    print(
        f"         sigma4 at the sigma-side anchor: position "
        f"{sigma4_row['position']} = {sigma4_row['residue']} "
        f"({'basic' if sigma4_row['is_basic'] else 'not basic'})"
    )
    print("=" * 78)
    results["verdict"] = verdict
    _write(results)
    return 0


def _write(results: dict) -> None:
    with open("results.json", "w") as handle:
        json.dump(results, handle, indent=2)
    print("\nwrote results.json")


if __name__ == "__main__":
    sys.exit(main())
