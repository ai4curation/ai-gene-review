"""Compare the four UniProt hbt (FBgn0264308) isoform products and probe the
AIG1/ADTRP Thr/His relationship mentioned by PMID:27018888.

Fetches sequences live from UniProt REST; prints results (no hardcoding).
Usage: uv run python compare_isoforms.py
"""

import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {
    "Q9VK03": "isoform D (benchmark)",
    "A0A6H2EJZ8": "isoform E (UniProt gene-centric canonical)",
    "M9PFU0": "isoform A",
    "Q9VK01": "isoform C",
}
CONTROLS = {
    "O44252": "Rost (Drosophila rolling stone, PTHR12242:SF46)",
    "Q9NVV5": "human AIG1 (FAHFA hydrolase, Thr43/His134)",
}


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as r:
        lines = r.read().decode().splitlines()
    return "".join(x for x in lines if not x.startswith(">"))


def aligner(mode: str) -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.mode = mode
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    return a


def identity(aln) -> tuple[int, int]:
    s1, s2 = aln[0], aln[1]
    pairs = [(x, y) for x, y in zip(s1, s2) if x != "-" and y != "-"]
    return sum(x == y for x, y in pairs), len(pairs)


def main() -> None:
    seqs = {a: fetch(a) for a in list(ACCS) + list(CONTROLS)}
    for a, d in {**ACCS, **CONTROLS}.items():
        print(f"{a}\t{len(seqs[a])} aa\t{d}")
    d = seqs["Q9VK03"]
    print("\n## Isoform D vs other isoforms (local alignment)")
    for a in ["A0A6H2EJZ8", "M9PFU0", "Q9VK01"]:
        aln = aligner("local").align(d, seqs[a])[0]
        idn, n = identity(aln)
        q0, q1 = aln.aligned[0][0][0], aln.aligned[0][-1][1]
        t0, t1 = aln.aligned[1][0][0], aln.aligned[1][-1][1]
        print(f"{a}: D {q0+1}-{q1} aligns to {t0+1}-{t1}; identity {idn}/{n}"
              f" = {100*idn/n:.1f}%")
        # report exact shared substrings longer than 50 aa
        tail = d[-60:]
        print(f"   D C-terminal 60 aa present verbatim in {a}: {tail in seqs[a]}")
        print(f"   D residues 30-451 present verbatim in {a}: {d[29:] in seqs[a]}")
    print("\n## Isoform D vs controls (local alignment; remote homology is NOT"
          " reliably detected by pairwise SW, see PMID:27018888 which used HHpred)")
    for a in CONTROLS:
        aln = aligner("local").align(d, seqs[a])[0]
        idn, n = identity(aln)
        q0, q1 = aln.aligned[0][0][0], aln.aligned[0][-1][1]
        t0, t1 = aln.aligned[1][0][0], aln.aligned[1][-1][1]
        print(f"{a}: D {q0+1}-{q1} vs {t0+1}-{t1}; identity {idn}/{n} = "
              f"{100*idn/n:.1f}%; score {aln.score}")
        if a == "Q9NVV5":
            # map AIG1 T43 and H134 onto D through this alignment
            for pos in (43, 134):
                hit = None
                for (qa, qb), (ta, tb) in zip(*aln.aligned):
                    if ta <= pos - 1 < tb:
                        hit = qa + (pos - 1 - ta)
                print(f"   AIG1 {seqs[a][pos-1]}{pos} -> D "
                      + (f"{d[hit]}{hit+1}" if hit is not None else "unaligned"))
        print(aln)


if __name__ == "__main__":
    main()
