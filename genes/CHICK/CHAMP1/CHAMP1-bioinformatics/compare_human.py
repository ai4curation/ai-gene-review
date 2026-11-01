"""Compare chicken CHAMP1 (A0A8V0YM97) with human CHAMP1 (Q96JM3).

Usage (from repo root):
  uv run python genes/CHICK/CHAMP1/CHAMP1-bioinformatics/compare_human.py \
      genes/human/CHAMP1/CHAMP1-uniprot.txt genes/CHICK/CHAMP1/CHAMP1-uniprot.txt

Reports global identity, per-window identity along the human sequence, and the
occurrences of WK, FPE and SPE motifs (Itoh et al. 2011 repeat motifs) in each.
"""
import re
import sys

from Bio import Align
from Bio.Align import substitution_matrices


def read_seq(path):
    txt = open(path).read()
    body = txt.split("\nSQ   ")[1].split("\n", 1)[1].split("//")[0]
    return "".join(c for c in body if c.isalpha())


def main(hpath, cpath):
    h, c = read_seq(hpath), read_seq(cpath)
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "global"
    aln = al.align(h, c)[0]
    pairs = [(i, j) for i, j in zip(*aln.indices) if i >= 0 and j >= 0]
    ident = sum(1 for i, j in pairs if h[i] == c[j])
    print(f"human_len={len(h)} chick_len={len(c)} identical={ident} "
          f"identity_over_human={ident/len(h):.3f}")
    m = dict(pairs)
    print("window\tidentity_over_human_window")
    for lo in range(0, len(h), 100):
        hi = min(lo + 100, len(h))
        n = sum(1 for i in range(lo, hi) if i in m and h[i] == c[m[i]])
        print(f"{lo+1}-{hi}\t{n/(hi-lo):.2f}")
    for name, s in (("human", h), ("chick", c)):
        wk = [(x.start() + 1, s[x.start() - 6:x.start() + 8]) for x in re.finditer("WK", s)]
        print(f"{name}\tWK_count={len(wk)}\tFPE_count={len(re.findall('FPE', s))}"
              f"\tSPE_count={len(re.findall('SPE', s))}")
        for pos, ctx in wk:
            print(f"  {name} WK at {pos}: {ctx}")
        cys_his = [x.start() + 1 for x in re.finditer(r"C..C.{12}H...H", s)]
        print(f"  {name} C2H2-like (C..C.{{12}}H...H) starts: {cys_his}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
