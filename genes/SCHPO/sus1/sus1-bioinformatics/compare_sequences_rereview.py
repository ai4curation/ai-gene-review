# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Pairwise comparison of S. pombe Sus1 (Q7LL15) with S. cerevisiae Sus1 (Q6WNK7)
and human ENY2 (Q9NPA8), and mapping of the budding-yeast residues mutated in
sus1-10 (E18A/S19A/G20A), sus1-11 (G37A/W38A) and sus1-12 (V73A/D75A)
(Klockner et al. 2009, PMID:19269973) onto the fission-yeast sequence.

Sequences are fetched live from UniProt; nothing is hardcoded except accessions
and the published mutant positions.
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = {"Q7LL15": "S. pombe sus1", "Q6WNK7": "S. cerevisiae SUS1", "Q9NPA8": "human ENY2"}
SC_MUTANTS = {"sus1-10": [18, 19, 20], "sus1-11": [37, 38], "sus1-12": [73, 75]}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    return a


def stats(aln) -> tuple[int, int, int]:
    s1, s2 = aln[0], aln[1]
    ident = sum(1 for x, y in zip(s1, s2) if x == y and x != "-")
    cols = sum(1 for x, y in zip(s1, s2) if x != "-" and y != "-")
    return ident, cols, len(s1)


def residue_map(aln) -> dict[int, int]:
    """Map 1-based positions in seqB (aln target index 1) to seqA (index 0)."""
    m: dict[int, int] = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for k in range(a1 - a0):
            m[b0 + k + 1] = a0 + k + 1
    return m


def main() -> None:
    seqs = {a: fetch(a) for a in ACCS}
    for a, s in seqs.items():
        print(f"{a}\t{ACCS[a]}\tlength={len(s)}")
    al = aligner()
    sp = seqs["Q7LL15"]
    for other in ("Q6WNK7", "Q9NPA8"):
        aln = al.align(sp, seqs[other])[0]
        ident, cols, length = stats(aln)
        print(f"\n== Q7LL15 vs {other} ({ACCS[other]})")
        print(f"identity={ident}/{cols} aligned columns ({100*ident/cols:.1f}%), alignment length {length}")
        print(aln)
    aln = al.align(sp, seqs["Q6WNK7"])[0]
    m = residue_map(aln)
    sc = seqs["Q6WNK7"]
    print("\n== Budding-yeast mutant residues mapped to S. pombe")
    for allele, pos in SC_MUTANTS.items():
        for p in pos:
            q = m.get(p)
            sp_res = f"{sp[q-1]}{q}" if q else "gap"
            print(f"{allele}\tSc {sc[p-1]}{p}\t-> Sp {sp_res}")


if __name__ == "__main__":
    main()
