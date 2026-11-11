# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Compare horse IRF9 gene model A0A9L0SN53 with the other horse IRF9 models and
with characterised IRF9 orthologs (human Q00978, mouse Q61179).

Reports global identity and the position/length/composition of every gap block
relative to human IRF9, so that model-specific insertions can be located with
respect to the human DBD (residues 1-117, Veals 1992) and the IAD.
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

ACCS = ["A0A9L0SN53", "F6Z2B0", "A0A9L0TC51", "A0A9L0STH9", "A0A9L0SUN9",
        "A0A9L0I7X9", "Q00978", "Q61179"]


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.mode = "global"
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.end_gap_score = 0
    return a


def gap_blocks(aln, qname: str):
    """Yield (ref_pos_before, length, seq) for insertions in the query (row 0)
    relative to the reference (row 1), and deletions likewise."""
    q, r = aln[0], aln[1]
    rpos = 0
    out = []
    i = 0
    n = len(q)
    while i < n:
        if r[i] == "-" and q[i] != "-":
            j = i
            while j < n and r[j] == "-":
                j += 1
            out.append(("insertion", rpos, j - i, q[i:j].replace("-", "")))
            i = j
            continue
        if q[i] == "-" and r[i] != "-":
            j = i
            while j < n and q[j] == "-":
                j += 1
            out.append(("deletion", rpos, j - i, r[i:j].replace("-", "")))
            rpos += j - i
            i = j
            continue
        rpos += 1
        i += 1
    return out


def main() -> None:
    seqs = {a: fetch(a) for a in ACCS}
    al = aligner()
    target = "A0A9L0SN53"
    print(f"{target} length {len(seqs[target])}")
    for ref in ACCS[1:]:
        aln = al.align(seqs[target], seqs[ref])[0]
        q, r = aln[0], aln[1]
        ident = sum(1 for x, y in zip(q, r) if x == y and x != "-")
        aligned = sum(1 for x, y in zip(q, r) if x != "-" and y != "-")
        print(f"\n== {target} vs {ref} (len {len(seqs[ref])}): identical {ident}/"
              f"{aligned} aligned positions ({100*ident/aligned:.1f}%)")
        for kind, pos, length, s in gap_blocks(aln, target):
            if length >= 3:
                print(f"  {kind} of {length} aa after {ref} residue {pos}: {s}")


if __name__ == "__main__":
    main()
