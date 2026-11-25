# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83"]
# ///
"""Align donkey SEC23A canonical A0A9L0JMP6 to characterised SEC23 paralogs/orthologs.

Usage:
  uv run --script compare_orthologs.py > compare_orthologs_output.txt

Sequences are fetched live from UniProt REST. Each comparator is globally aligned to
the donkey protein (BLOSUM62, open -10, extend -0.5); identity, gaps and the donkey
residue at each characterised human SEC23A functional position are printed.
"""
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

DONKEY = "A0A9L0JMP6"
COMPARATORS = {
    "Q15436": "human SEC23A (PTHR11141:SF7)",
    "Q01405": "mouse Sec23a (PTHR11141:SF7)",
    "Q15437": "human SEC23B (PTHR11141:SF10)",
    "P15303": "yeast Sec23 (PTHR11141:SF0)",
}
# Yeast Sec23 (P15303) arginine finger inserted into the Sar1 active site (Bi et al. 2002)
YEAST_FUNCTIONAL = {722: "Sar1 GAP arginine finger"}
# Human SEC23A (Q15436) positions characterised in the literature
FUNCTIONAL = {
    61: "Zn ligand Cys",
    66: "Zn ligand Cys",
    85: "Zn ligand Cys",
    88: "Zn ligand Cys",
    382: "CLSD residue Phe (F382L)",
    628: "gelsolin PPP-binding Phe",
    672: "gelsolin PPP-binding Tyr",
    678: "gelsolin PPP-binding Tyr",
    681: "gelsolin PPP-binding Phe",
}


def fasta_seq(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    txt = urllib.request.urlopen(url).read().decode()
    return "".join(l.strip() for l in txt.splitlines() if not l.startswith(">"))


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    return a


def pos_map(aln) -> dict[int, int]:
    """Map 1-based comparator (target) positions to 1-based donkey (query) positions."""
    m: dict[int, int] = {}
    for (ts, te), (qs, qe) in zip(*aln.aligned):
        for i in range(te - ts):
            m[ts + i + 1] = qs + i + 1
    return m


def main() -> None:
    donkey = fasta_seq(DONKEY)
    print(f"{DONKEY} donkey SEC23A canonical: {len(donkey)} aa")
    al = aligner()
    for acc, label in COMPARATORS.items():
        seq = fasta_seq(acc)
        aln = al.align(seq, donkey)[0]
        pairs = sum(te - ts for ts, te in aln.aligned[0])
        ident = sum(
            1
            for (ts, te), (qs, qe) in zip(*aln.aligned)
            for i in range(te - ts)
            if seq[ts + i] == donkey[qs + i]
        )
        print(f"\n{acc} {label}: {len(seq)} aa; aligned pairs {pairs}; "
              f"identical {ident} ({100*ident/pairs:.2f}% of aligned); "
              f"identity over donkey length {100*ident/len(donkey):.2f}%")
        sites = {"Q15436": FUNCTIONAL, "P15303": YEAST_FUNCTIONAL}.get(acc, {})
        if sites:
            m = pos_map(aln)
            for p, desc in sites.items():
                d = m.get(p)
                dres = donkey[d - 1] if d else "-"
                print(f"  {acc} {seq[p-1]}{p} ({desc}) -> donkey {dres}{d}")


if __name__ == "__main__":
    main()
