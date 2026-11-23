"""Align a query UniProt sequence to a reference UniProt sequence and report
the query residues that align to named reference positions, plus percent
identity over named reference regions.

Usage:
  python residue_conservation.py QUERY_UNIPROT.txt REFERENCE_UNIPROT.txt \
      --site R42 --site D399 ... --region GIY-YIG:16-94 ...

Each --site is <expected reference residue><reference position>; the script
first checks that the reference really carries that residue (guarding against
wrong numbering), then reports the aligned query residue. Results are computed
at run time; nothing is hard-coded.
"""
import argparse
import re
import sys

from Bio import Align
from Bio.Align import substitution_matrices


def read_uniprot_seq(path):
    seq, on = [], False
    acc = None
    for line in open(path):
        if line.startswith("AC   ") and acc is None:
            acc = line[5:].split(";")[0].strip()
        if line.startswith("SQ   "):
            on = True
            continue
        if on:
            if line.startswith("//"):
                break
            seq.append(re.sub(r"[^A-Z]", "", line))
    return acc, "".join(seq)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("reference")
    ap.add_argument("--site", action="append", default=[])
    ap.add_argument("--region", action="append", default=[])
    a = ap.parse_args()
    qacc, q = read_uniprot_seq(a.query)
    racc, r = read_uniprot_seq(a.reference)
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "global"
    aln = al.align(r, q)[0]
    # map reference index -> query index
    rmap = {}
    for (rs, re_), (qs, qe) in zip(*aln.aligned):
        for i in range(re_ - rs):
            rmap[rs + i] = qs + i
    ident = sum(1 for i, j in rmap.items() if r[i] == q[j])
    print(f"query {qacc} length {len(q)}; reference {racc} length {len(r)}")
    print(f"aligned reference positions: {len(rmap)}; identical: {ident} "
          f"({100 * ident / len(r):.1f}% of reference length)")
    print("\nSITES (reference residue -> aligned query residue)")
    for s in a.site:
        exp, pos = s[0], int(s[1:])
        ref_res = r[pos - 1]
        flag = "" if ref_res == exp else f"  !! reference has {ref_res}, not {exp}"
        j = rmap.get(pos - 1)
        qres = f"{q[j]}{j + 1}" if j is not None else "gap"
        status = "conserved" if j is not None and q[j] == ref_res else "NOT conserved"
        print(f"  {racc} {ref_res}{pos} -> {qacc} {qres}  [{status}]{flag}")
    print("\nREGIONS (percent identity over reference region)")
    for reg in a.region:
        name, rng = reg.rsplit(":", 1)
        s, e = (int(x) for x in rng.split("-"))
        idx = range(s - 1, e)
        alnd = [i for i in idx if i in rmap]
        same = sum(1 for i in alnd if r[i] == q[rmap[i]])
        print(f"  {name} {racc} {s}-{e}: aligned {len(alnd)}/{len(idx)}, "
              f"identical {same} ({100 * same / len(idx):.1f}%)")


if __name__ == "__main__":
    sys.exit(main())
