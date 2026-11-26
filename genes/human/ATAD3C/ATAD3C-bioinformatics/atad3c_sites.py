"""Align human ATAD3C (Q5T2N8) to ATAD3A isoform 2 (Q9NVI7-2), the numbering
used by Frazier et al. 2021 (PMID:32004445), and report the ATAD3C residues at
the AAA+ Walker A, Walker B and arginine-finger positions of ATAD3A, each with
a +/-6 residue window so gap-placement offsets are visible.

Positive control: the same positions are reported for ATAD3B (Q5T9A4), whose
AAA module is expected to be complete.

Sequences are fetched from UniProt at run time. ATAD3A motif positions are
located in the ATAD3A sequence itself (Walker A G..G.GK[ST], Walker B
hhhhDE, and Arg466, the arginine finger named in PMID:32004445).
"""
import re
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

REF = "Q9NVI7-2"
TARGETS = {"ATAD3C": "Q5T2N8", "ATAD3B (control)": "Q5T9A4"}
ARG_FINGER = 466


def seq(acc: str) -> str:
    with urllib.request.urlopen(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta") as r:
        return "".join(r.read().decode().splitlines()[1:])


def mapping(ref: str, tgt: str) -> dict[int, int]:
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score = -10, -0.5
    al.mode = "local"
    best = al.align(ref, tgt)[0]
    m = {}
    for (rs, re_), (ts, _) in zip(*best.aligned):
        for k in range(re_ - rs):
            m[rs + k + 1] = ts + k + 1
    return m


def window(s: str, p: int) -> str:
    return s[max(0, p - 7): p + 6]


def main() -> None:
    ref = seq(REF)
    wa = re.search(r"G..G.GK[ST]", ref)
    wb = re.search(r"[ILVMF]{4}DE", ref)
    sites = {
        "Walker A K": wa.start() + 7,
        "Walker B D": wb.start() + 5,
        "Walker B E": wb.start() + 6,
        "arginine finger": ARG_FINGER,
    }
    print(f"ATAD3A ({REF}) length {len(ref)}")
    for name, p in sites.items():
        print(f"  {name}: {ref[p-1]}{p}  window {window(ref, p)}")
    assert ref[ARG_FINGER - 1] == "R", "Arg466 not found in ATAD3A isoform 2"
    for label, acc in TARGETS.items():
        tgt = seq(acc)
        m = mapping(ref, tgt)
        ident = sum(1 for p, t in m.items() if ref[p - 1] == tgt[t - 1])
        span = (min(m), max(m))
        print(f"\n{label} ({acc}) length {len(tgt)}; aligned ATAD3A {span[0]}-{span[1]}, identity {ident}/{len(m)}")
        for name, p in sites.items():
            t = m.get(p)
            if t is None:
                print(f"  {name} ATAD3A {ref[p-1]}{p}: no aligned residue")
            else:
                print(f"  {name} ATAD3A {ref[p-1]}{p} -> {tgt[t-1]}{t}   ATAD3A {window(ref, p)} / {window(tgt, t)}")


if __name__ == "__main__":
    main()
