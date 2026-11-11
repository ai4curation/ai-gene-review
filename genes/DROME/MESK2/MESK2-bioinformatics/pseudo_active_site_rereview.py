"""MESK2 re-review: isoform comparison and NDRG pseudo-active-site check.

1. Compares the benchmark accession Q8T0V2 (isoforms A/E/F) with the UniProt
   gene-centric canonical Q7KVN0 (isoform I; sequence-identical to Q9GU50).
2. Aligns MESK2 with human NDRG2 (Q9UN36) and reports which MESK2 residues sit at
   the positions of the alpha/beta-hydrolase catalytic triad. Hwang et al. 2011
   (PMID:21247902) report that in hNDRG2 these positions are Gly132-Gly279-Ala251.
   The paper numbers a 357-aa isoform; in the 371-aa UniProt canonical Q9UN36-1
   the same residues are Gly146, Ala265 and Gly293 (offset +14; the script checks
   the triplet G/A/G at 146/265/293 before mapping).

Run: uv run python pseudo_active_site_rereview.py
"""

import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    text = urllib.request.urlopen(url).read().decode()
    return "".join(line.strip() for line in text.splitlines() if not line.startswith(">"))


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    return a


def map_positions(aln, positions):
    """Map 1-based positions in target (seq 0) to residues in query (seq 1)."""
    out = {}
    t_blocks, q_blocks = aln.aligned
    for p in positions:
        i = p - 1
        res = None
        for (ts, te), (qs, qe) in zip(t_blocks, q_blocks):
            if ts <= i < te:
                j = qs + (i - ts)
                res = (int(j) + 1, aln.sequences[1][j])
                break
        out[p] = res
    return out


def identity(aln) -> float:
    t, q = aln.sequences
    same = 0
    cols = 0
    for (ts, te), (qs, qe) in zip(*aln.aligned):
        for k in range(te - ts):
            cols += 1
            same += t[ts + k] == q[qs + k]
    return same / cols if cols else 0.0


def proteomes(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}?fields=accession,xref_proteomes&format=tsv"
    rows = urllib.request.urlopen(url).read().decode().rstrip("\n").splitlines()
    fields = rows[-1].split("\t")
    return fields[1].strip() if len(fields) > 1 else ""


def main() -> None:
    q8 = fetch("Q8T0V2")
    a4 = fetch("A4UZR7")
    print(f"Q8T0V2 == A4UZR7 (sequence identical): {q8 == a4}")
    for acc in ["Q8T0V2", "A4UZR7", "Q7KVN0", "Q9GU50"]:
        print(f"{acc} proteomes: {proteomes(acc) or 'none'}")
    canon = fetch("Q7KVN0")
    q9 = fetch("Q9GU50")
    print(f"Q8T0V2 length {len(q8)}; Q7KVN0 length {len(canon)}; Q9GU50 length {len(q9)}")
    print(f"Q7KVN0 == Q9GU50: {canon == q9}")
    core_start = q8.find(canon[:40])
    print(f"Q7KVN0 residues 1-40 found in Q8T0V2 at position {core_start + 1}")
    # longest shared block
    k = 0
    while core_start + k < len(q8) and k < len(canon) and q8[core_start + k] == canon[k]:
        k += 1
    print(f"Identical shared block: Q8T0V2 {core_start + 1}-{core_start + k} == Q7KVN0 1-{k}")
    print(f"Q8T0V2-specific N-terminus: 1-{core_start} ({core_start} aa)")
    print(f"Q8T0V2-specific C-terminus: {core_start + k + 1}-{len(q8)} ({len(q8) - core_start - k} aa)")
    print(f"Q7KVN0-specific C-terminus: {k + 1}-{len(canon)} ({len(canon) - k} aa)")

    ndrg2 = fetch("Q9UN36")
    triad = [146, 265, 293]
    print(f"hNDRG2 Q9UN36 length {len(ndrg2)}; residues at 146/265/293: "
          + ", ".join(f"{p}:{ndrg2[p-1]}" for p in triad))
    a = aligner()
    for name, seq in [("Q8T0V2", q8), ("Q7KVN0", canon)]:
        aln = a.align(ndrg2, seq)[0]
        print(f"{name} vs hNDRG2: identity over aligned columns {identity(aln):.2f}")
        for p, res in map_positions(aln, triad).items():
            print(f"  hNDRG2 {p}{ndrg2[p-1]} -> {name} {res}")
        # local context around mapped nucleophile-elbow position
        mp = map_positions(aln, [146])[146]
        if mp:
            j = mp[0]
            print(f"  {name} context around nucleophile-elbow position: {seq[j-6:j+5]}")
        print(f"  hNDRG2 context: {ndrg2[140:151]}")


if __name__ == "__main__":
    main()
