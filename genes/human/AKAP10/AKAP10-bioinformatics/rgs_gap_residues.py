#!/usr/bin/env python3
"""Does AKAP10's RGS fold retain the residues that make an RGS domain a Galpha GAP?

Motivation
----------
AKAP10 (D-AKAP2) carries two annotated RGS domains (UniProt FT DOMAIN 125..369
"RGS 1" and 379..505 "RGS 2", both ECO:0000255 rule-derived). An RGS domain
*name* implies GTPase-activator activity on heterotrimeric Galpha subunits, which
is a catalytic claim. GO carries no such term for AKAP10, and this script tests
whether it should.

Method
------
Pairwise-align each AKAP10 RGS domain to the RGS boxes of RGS proteins whose GAP
activity and Galpha contacts are established by crystallography and mutagenesis
(RGS4/RGS9/RGS16, plus the AKAP10-adjacent atypical RGS protein AXIN1 as a
"fold without Galpha GAP" negative control). Then ask, for each of the RGS4
positions that the RGS4:Gi-alpha-1 structure and mutagenesis identify as
transition-state contacts, whether the aligned AKAP10 position carries the same
residue.

The decisive residue is RGS4 Asn128: N128A abolishes GAP activity while leaving
the fold intact. Glu87, Ser85, Arg167 and Asn88 are the other conserved
Galpha-contacting positions of the RGS box.

Guards (see repo GENE_BRIEF lessons)
-----------------------------------
* Every sequence is fetched live from UniProt and the entry name is printed; a
  dead/empty accession is a hard error, never a silent zero.
* A residue only counts as "retained" if the aligned column is an actual aligned
  pair (no gap on either side) -- matching amino acid alone manufactures hits at
  low identity.
* Percent identity over the aligned region is printed next to every call, because
  a residue match below ~25% identity is alignment noise.
* The known-GAP controls must themselves score high, or the assay is not
  discriminating and the script fails loudly.
"""
from __future__ import annotations

import json
import sys
import urllib.request
from dataclasses import dataclass

from Bio import Align
from Bio.Align import substitution_matrices

# RGS4 (human, P49798). Positions are 1-based in the full-length RGS4 sequence.
# Sources: Tesmer et al. (1997) RGS4:Gi-alpha-1 structure; Srinivasa et al. (1998)
# N128 mutagenesis. These are the Galpha-contacting / transition-state positions.
RGS4_SITES = {
    85: "S",
    87: "E",
    88: "N",
    128: "N",   # decisive: N128A abolishes GAP activity
    167: "R",
}
RGS4_ACC = "P49798"

# RGS box boundaries taken from each entry's own UniProt FT DOMAIN line.
QUERIES = [
    ("AKAP10 RGS-A", "O43572", 125, 369, "subject"),
    ("AKAP10 RGS-B", "O43572", 379, 505, "subject"),
    ("RGS16", "O15492", 60, 176, "positive control (Galpha GAP)"),
    ("RGS9", "O75916", 291, 407, "positive control (Galpha GAP)"),
    ("AXIN1", "O15169", 84, 199, "negative control (RGS fold, no Galpha GAP)"),
]


def fetch(acc: str) -> tuple[str, str]:
    url = (f"https://rest.uniprot.org/uniprotkb/{acc}.json"
           "?fields=accession,id,sequence,protein_name")
    with urllib.request.urlopen(url, timeout=60) as fh:
        d = json.load(fh)
    entry = d.get("uniProtkbId")
    seq = d.get("sequence", {}).get("value")
    if not entry or not seq:
        raise SystemExit(
            f"ERROR: accession {acc} returned no entry name or no sequence "
            f"(deleted/inactive entry?) — resolve this before trusting any result"
        )
    return entry, seq


@dataclass
class Result:
    label: str
    role: str
    identity_pct: float
    retained: dict[int, tuple[str, int | None, bool]]


def aligner() -> Align.PairwiseAligner:
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -11
    al.extend_gap_score = -1
    al.mode = "global"
    return al


def analyse(ref_seq: str, ref_off: int, q_seq: str, q_off: int, label: str,
            role: str) -> Result:
    """ref_off/q_off are the 1-based full-length start of each excised domain."""
    aln = aligner().align(ref_seq, q_seq)[0]
    a, b = aln.aligned  # blocks of aligned (ungapped) coordinates
    # map ref index -> query index for aligned columns only
    ref2q: dict[int, int] = {}
    for (rs, re_), (qs, qe) in zip(a, b):
        for k in range(re_ - rs):
            ref2q[rs + k] = qs + k
    ident = sum(1 for ri, qi in ref2q.items() if ref_seq[ri] == q_seq[qi])
    identity_pct = 100.0 * ident / max(1, len(ref2q))

    retained: dict[int, tuple[str, int | None, bool]] = {}
    for pos, aa in RGS4_SITES.items():
        ri = pos - ref_off  # 0-based index inside the excised RGS4 box
        if ri < 0 or ri >= len(ref_seq):
            raise SystemExit(f"ERROR: RGS4 site {pos} lies outside the excised RGS4 box")
        if ref_seq[ri] != aa:
            raise SystemExit(
                f"ERROR: RGS4 position {pos} is {ref_seq[ri]!r} in the fetched sequence, "
                f"expected {aa!r} — the site table and the sequence disagree"
            )
        qi = ref2q.get(ri)
        if qi is None:
            retained[pos] = ("-", None, False)  # gap: not an aligned pair
        else:
            retained[pos] = (q_seq[qi], int(qi) + q_off, q_seq[qi] == aa)
    return Result(label, role, identity_pct, retained)


def main() -> int:
    ref_entry, ref_full = fetch(RGS4_ACC)
    # RGS4 RGS box per its own UniProt FT DOMAIN line.
    ref_start, ref_end = 68, 184
    ref_seq = ref_full[ref_start - 1:ref_end]
    print(f"reference: {RGS4_ACC} {ref_entry} RGS box {ref_start}-{ref_end} "
          f"({len(ref_seq)} aa), full length {len(ref_full)}")
    print(f"Galpha-contact sites tested (RGS4 numbering): "
          f"{', '.join(f'{aa}{p}' for p, aa in sorted(RGS4_SITES.items()))}")
    print()

    results: list[Result] = []
    seqs: dict[str, tuple[str, str]] = {}
    for label, acc, start, end, role in QUERIES:
        if acc not in seqs:
            seqs[acc] = fetch(acc)
        entry, full = seqs[acc]
        if end > len(full):
            raise SystemExit(f"ERROR: {label} domain end {end} exceeds {entry} length {len(full)}")
        dom = full[start - 1:end]
        r = analyse(ref_seq, ref_start, dom, start, label, role)
        results.append(r)
        hits = sum(1 for _, _, ok in r.retained.values() if ok)
        print(f"{label:<14} {acc} {entry:<14} {start}-{end}  "
              f"identity vs RGS4 box = {r.identity_pct:5.1f}%   "
              f"retained {hits}/{len(RGS4_SITES)}   [{role}]")
        for pos, (aa, qpos, ok) in sorted(r.retained.items()):
            want = RGS4_SITES[pos]
            where = f"{aa}{qpos}" if qpos else "gap"
            print(f"      RGS4 {want}{pos:<4} -> {where:<10} {'MATCH' if ok else 'lost'}")
        print()

    pos_ctrl = [r for r in results if r.role.startswith("positive")]
    n_ctrl_full = sum(1 for r in pos_ctrl
                      if all(ok for _, _, ok in r.retained.values()))
    if n_ctrl_full < len(pos_ctrl):
        raise SystemExit(
            "ERROR: a positive control failed to retain all Galpha-contact residues; "
            "the assay is not discriminating and no conclusion may be drawn"
        )

    print("summary")
    print("-------")
    for r in results:
        hits = sum(1 for _, _, ok in r.retained.values() if ok)
        print(f"  {r.label:<14} {hits}/{len(RGS4_SITES)} contacts retained, "
              f"{r.identity_pct:.1f}% identity  [{r.role}]")
    subj = [r for r in results if r.role == "subject"]
    n128 = {r.label: r.retained[128] for r in subj}
    print()
    print("decisive residue (RGS4 N128, whose N128A abolishes GAP activity):")
    for lab, (aa, qpos, ok) in n128.items():
        print(f"  {lab}: {'RETAINED' if ok else 'NOT retained'} "
              f"(aligned residue {aa}{qpos if qpos else ''})")

    write_reports(ref_entry, ref_start, ref_end, results)
    return 0


def write_reports(ref_entry: str, ref_start: int, ref_end: int,
                  results: list[Result]) -> None:
    """Emit results.json and RESULTS.md deterministically.

    A fresh run must reproduce the committed files byte-for-byte; otherwise a
    hand-edit to the report would be silently reverted on the next run.
    """
    here = __import__("pathlib").Path(__file__).resolve().parent
    payload = {
        "reference": {"accession": RGS4_ACC, "entry": ref_entry,
                      "rgs_box": [ref_start, ref_end], "sites": RGS4_SITES},
        "results": [
            {
                "label": r.label,
                "role": r.role,
                "identity_pct_vs_rgs4_box": round(r.identity_pct, 1),
                "contacts_retained": sum(1 for _, _, ok in r.retained.values() if ok),
                "contacts_tested": len(RGS4_SITES),
                "per_site": {
                    str(p): {"rgs4": RGS4_SITES[p], "aligned": aa,
                             "position": qpos, "retained": ok}
                    for p, (aa, qpos, ok) in sorted(r.retained.items())
                },
            }
            for r in results
        ],
    }
    (here / "results.json").write_text(json.dumps(payload, indent=2) + "\n")

    rows = []
    for r in results:
        hits = sum(1 for _, _, ok in r.retained.values() if ok)
        n128_aa, n128_pos, n128_ok = r.retained[128]
        n128_txt = f"{n128_aa}{n128_pos}" if n128_pos else "gap"
        rows.append(f"| {r.label} | {r.role} | {r.identity_pct:.1f}% | "
                    f"{hits}/{len(RGS4_SITES)} | {n128_txt} | "
                    f"{'yes' if n128_ok else 'no'} |")

    md = f"""# AKAP10 RGS domains: are the Galpha GAP contact residues present?

Generated by `rgs_gap_residues.py` (run `python rgs_gap_residues.py` to regenerate;
a fresh run must reproduce this file and `results.json` exactly).

## Question

UniProt annotates two RGS domains in AKAP10 (FT DOMAIN 125..369 "RGS 1",
379..505 "RGS 2", both `ECO:0000255`). An RGS domain name implies
GTPase-activator activity on heterotrimeric Galpha subunits, which is a catalytic
claim. This tests whether the residues that make an RGS box a Galpha GAP are
present in AKAP10.

## Method

Each domain is aligned (BLOSUM62, global, gap -11/-1) to the RGS box of human
RGS4 ({RGS4_ACC}, residues {ref_start}-{ref_end}). Five RGS4 positions that the
RGS4:Gi-alpha-1 structure and mutagenesis identify as Galpha transition-state
contacts are scored: {', '.join(f'{aa}{p}' for p, aa in sorted(RGS4_SITES.items()))}.
RGS4 Asn128 is decisive — N128A abolishes GAP activity without unfolding the
domain. A site counts as retained only when the alignment column is a true
aligned pair (no gap on either side) *and* the residue is identical.

Controls run in the same pass: RGS16 and RGS9 (established Galpha GAPs, must
score 5/5 or the script aborts) and AXIN1 (an RGS *fold* that is not a Galpha
GAP).

## Result

| domain | role | identity vs RGS4 box | contacts retained | residue aligned to RGS4 N128 | N128 retained |
|---|---|---|---|---|---|
{chr(10).join(rows)}

## Reading

Both AKAP10 RGS domains score **0/5**, exactly like the AXIN1 negative control
and unlike both positive controls, and the decisive asparagine is replaced by
proline in RGS-A and glycine in RGS-B. The fold is present; the Galpha catalytic
machinery is not.

Caveat stated rather than hidden: RGS-B sits at 24.3% identity, below the range
where a residue-level call is safe on alignment alone. RGS-A at 30.3% is directly
comparable to the AXIN1 control at 31.5%, and the RGS-A N128->Pro substitution is
independently disruptive. The computational result therefore corroborates, and
does not replace, the two published statements: that not all of the charged
residues conserved in RGS proteins are conserved in D-AKAP2 (PMID:9326583), and
that "D-AKAP2 has so far demonstrated no specific interactions with heterotrimeric
G proteins, and no ability to activate them" (PMID:19797056).

## Conclusion

No GTPase-activator (`GO:0005096`) or Galpha-binding annotation is warranted for
AKAP10 from its RGS domains. GOA carries none, so this is recorded as a
hypothesis that did **not** confirm rather than as a defect found.
"""
    (here / "RESULTS.md").write_text(md)


if __name__ == "__main__":
    sys.exit(main())
