"""Sequence-level checks for the human APPL2 (Q8NEU8) GO annotation review.

Two questions are answered here, both of which the review's reasoning depends on:

1. **How safe are the ISS/IEA orthology transfers from mouse Appl2 (Q8K3G9)?**
   Twenty-four ISS rows (GO_REF:0000024) and nineteen IEA rows (GO_REF:0000107)
   on human APPL2 are transfers from the single mouse donor Q8K3G9. The transfer
   is only as good as the orthology, so we measure human-mouse APPL2 identity and
   compare it with the human APPL2 / human APPL1 paralog identity.

2. **Are the residues the structural paper attributes to APPL2 actually there?**
   King et al. (PMID:23055524) name three human APPL2 PH-domain residues,
   Arg-287, Lys-289 and Trp-297, as the candidate non-canonical inositol-phosphate
   contact surface, and quote a putative nuclear localisation signal at
   151-PKKKENE-157 (the motif originally proposed by Miaczynska et al.).
   Both are checkable directly against Q8NEU8's own sequence, and their
   conservation in mouse Appl2 bears on whether the IDA phosphoinositide-binding
   and nucleus rows transfer.

Everything is fetched live from the UniProt REST API; nothing is hardcoded except
the accessions and the literature-derived positions being tested.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass

import requests
from Bio import Align

UNIPROT_FASTA = "https://rest.uniprot.org/uniprotkb/{acc}.fasta"

# The four family members that matter here. PANTHER PTHR46415 classifies human and
# mouse APPL2 into subfamily SF1 and the APPL1 proteins into SF3.
PROTEINS = {
    "Q8NEU8": "human APPL2",
    "Q8K3G9": "mouse Appl2",
    "Q9UKG1": "human APPL1",
    "Q8K3H0": "mouse Appl1",
}

# Expected chain lengths, asserted so a truncated or wrong record fails loudly
# rather than being scored as substitutions.
EXPECTED_LENGTHS = {
    "Q8NEU8": 664,
    "Q8K3G9": 662,
    "Q9UKG1": 709,
    "Q8K3H0": 707,
}

# UniProt FT DOMAIN spans for Q8NEU8 (1-based, inclusive).
APPL2_DOMAINS = {"BAR": (3, 268), "PH": (277, 375), "PID": (488, 637)}

# Literature-derived positions in human APPL2, all from PMID:23055524.
# (residue, description)
APPL2_SITES = {
    287: ("R", "PH-domain basic patch; candidate Ins(1,4,5)P3 contact"),
    289: ("K", "PH-domain basic patch; candidate Ins(1,4,5)P3 contact"),
    297: ("W", "PH-domain aromatic; candidate Ins(1,4,5)P3 contact"),
}
APPL2_NLS = (151, "PKKKENE", "putative nuclear localisation signal in BAR loop 2")


@dataclass
class Seq:
    accession: str
    label: str
    sequence: str

    def at(self, pos: int) -> str:
        """1-based residue lookup."""
        return self.sequence[pos - 1]


def fetch(accession: str, label: str) -> Seq:
    resp = requests.get(UNIPROT_FASTA.format(acc=accession), timeout=60)
    resp.raise_for_status()
    lines = resp.text.strip().splitlines()
    if not lines[0].startswith(">"):
        raise ValueError(f"{accession}: response is not FASTA: {lines[0][:80]!r}")
    seq = "".join(lines[1:])
    expected = EXPECTED_LENGTHS[accession]
    if len(seq) != expected:
        raise ValueError(
            f"{accession} ({label}): fetched {len(seq)} aa, expected {expected} aa. "
            "The record changed or the wrong entry was returned; do not score this run."
        )
    return Seq(accession, label, seq)


def aligner() -> Align.PairwiseAligner:
    al = Align.PairwiseAligner()
    al.mode = "global"
    al.substitution_matrix = Align.substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -11
    al.extend_gap_score = -1
    return al


def identity(a: Seq, b: Seq) -> tuple[float, int, int, dict[int, int]]:
    """Return (% identity over aligned columns, identities, aligned columns, a->b position map)."""
    aln = aligner().align(a.sequence, b.sequence)[0]
    ident = 0
    cols = 0
    pos_map: dict[int, int] = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for off in range(a1 - a0):
            ai, bi = a0 + off, b0 + off
            cols += 1
            pos_map[ai + 1] = bi + 1
            if a.sequence[ai] == b.sequence[bi]:
                ident += 1
    return 100.0 * ident / cols, ident, cols, pos_map


def main() -> int:
    seqs = {acc: fetch(acc, label) for acc, label in PROTEINS.items()}
    rows: list[tuple[str, ...]] = []

    print("== sequences ==")
    for acc, s in seqs.items():
        print(f"  {acc}  {s.label:14s}  {len(s.sequence)} aa")

    print("\n== pairwise global identity (BLOSUM62, gap -11/-1) ==")
    pairs = [
        ("Q8NEU8", "Q8K3G9", "human APPL2 vs mouse Appl2 (ortholog; ISS/IEA donor)"),
        ("Q9UKG1", "Q8K3H0", "human APPL1 vs mouse Appl1 (ortholog)"),
        ("Q8NEU8", "Q9UKG1", "human APPL2 vs human APPL1 (paralog)"),
        ("Q8K3G9", "Q8K3H0", "mouse Appl2 vs mouse Appl1 (paralog)"),
    ]
    maps: dict[tuple[str, str], dict[int, int]] = {}
    for x, y, note in pairs:
        pct, ident, cols, pos_map = identity(seqs[x], seqs[y])
        maps[(x, y)] = pos_map
        print(f"  {x} vs {y}: {pct:5.1f}%  ({ident}/{cols} aligned columns)  {note}")
        rows.append(("identity", f"{x}:{y}", f"{pct:.1f}", f"{ident}/{cols}", note))

    print("\n== Q8NEU8 UniProt domain spans ==")
    for name, (start, end) in APPL2_DOMAINS.items():
        frag = seqs["Q8NEU8"].sequence[start - 1 : end]
        print(f"  {name:4s} {start:3d}-{end:3d} ({end - start + 1} aa) starts {frag[:12]}...")
        rows.append(("domain", name, f"{start}-{end}", str(end - start + 1), frag[:12]))

    print("\n== literature-derived residues in human APPL2 (PMID:23055524) ==")
    o_map = maps[("Q8NEU8", "Q8K3G9")]
    p_map = maps[("Q8NEU8", "Q9UKG1")]
    for pos, (expected_res, role) in sorted(APPL2_SITES.items()):
        observed = seqs["Q8NEU8"].at(pos)
        ok = "MATCH" if observed == expected_res else "MISMATCH"
        mpos = o_map.get(pos)
        mres = seqs["Q8K3G9"].at(mpos) if mpos else None
        apos = p_map.get(pos)
        ares = seqs["Q9UKG1"].at(apos) if apos else None
        in_ph = APPL2_DOMAINS["PH"][0] <= pos <= APPL2_DOMAINS["PH"][1]
        print(
            f"  Q8NEU8 {pos}: paper says {expected_res}, sequence has {observed} [{ok}]"
            f"; in PH domain: {in_ph}"
            f"; mouse Appl2 {mpos}={mres}; human APPL1 {apos}={ares}  -- {role}"
        )
        rows.append(
            ("site", f"Q8NEU8:{pos}", f"{expected_res}->{observed}", ok,
             f"mouse={mpos}:{mres};APPL1={apos}:{ares};in_PH={in_ph}")
        )

    nls_start, nls_motif, nls_role = APPL2_NLS
    nls_end = nls_start + len(nls_motif) - 1
    observed_motif = seqs["Q8NEU8"].sequence[nls_start - 1 : nls_end]
    ok = "MATCH" if observed_motif == nls_motif else "MISMATCH"
    mouse_span = "".join(
        seqs["Q8K3G9"].at(o_map[p]) if p in o_map else "-" for p in range(nls_start, nls_end + 1)
    )
    appl1_span = "".join(
        seqs["Q9UKG1"].at(p_map[p]) if p in p_map else "-" for p in range(nls_start, nls_end + 1)
    )
    in_bar = APPL2_DOMAINS["BAR"][0] <= nls_start and nls_end <= APPL2_DOMAINS["BAR"][1]
    print(
        f"\n  Q8NEU8 {nls_start}-{nls_end}: paper says {nls_motif}, sequence has "
        f"{observed_motif} [{ok}]; within BAR domain: {in_bar}"
        f"; mouse Appl2 aligned span {mouse_span}; human APPL1 aligned span {appl1_span}"
        f"  -- {nls_role}"
    )
    rows.append(
        ("motif", f"Q8NEU8:{nls_start}-{nls_end}", f"{nls_motif}->{observed_motif}", ok,
         f"mouse={mouse_span};APPL1={appl1_span};in_BAR={in_bar}")
    )

    with open("appl_orthology.tsv", "w") as fh:
        fh.write("kind\tsubject\tvalue\tstatus\tnote\n")
        for r in rows:
            fh.write("\t".join(r) + "\n")
    print("\nwrote appl_orthology.tsv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
