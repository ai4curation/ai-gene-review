# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Compare Drosophila CG18507 isoform products with vertebrate TMEM268 (PANTHER PTHR31193:SF1).

Fetches sequences live from UniProt REST, then:
1. reports pairwise relationships among the five CG18507 UniProt products (shared prefix / differing C-terminus);
2. local-aligns M9PBB3 to human TMEM268 (Q5VZI3) and mouse Tmem268 (Q8R239) with BLOSUM62,
   reporting identity/similarity over the aligned region and the aligned coordinate ranges.
Results are printed and written to results-tmem268.json.
"""
import json
import requests
from Bio import Align
from Bio.Align import substitution_matrices

FLY = ["M9PBB3", "M9PCX0", "M9PFU6", "Q7KTB0", "Q9VJW7"]
VERT = ["Q5VZI3", "Q8R239"]


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def shared_prefix(a: str, b: str) -> int:
    n = 0
    while n < min(len(a), len(b)) and a[n] == b[n]:
        n += 1
    return n


def local(a: str, b: str):
    al = Align.PairwiseAligner()
    al.mode = "local"
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -11
    al.extend_gap_score = -1
    aln = al.align(a, b)[0]
    ident = sim = cols = 0
    blosum = al.substitution_matrix
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for i, j in zip(range(s1, e1), range(s2, e2)):
            cols += 1
            ident += a[i] == b[j]
            sim += blosum[a[i]][b[j]] > 0
    span_a = (int(aln.aligned[0][0][0]) + 1, int(aln.aligned[0][-1][1]))
    span_b = (int(aln.aligned[1][0][0]) + 1, int(aln.aligned[1][-1][1]))
    return {
        "score": float(aln.score),
        "aligned_pairs": cols,
        "identity_pct": round(100 * ident / cols, 1),
        "similarity_pct": round(100 * sim / cols, 1),
        "query_span": span_a,
        "target_span": span_b,
        "target_length": len(b),
    }


def main() -> None:
    seqs = {a: fetch(a) for a in FLY + VERT}
    ref = seqs["M9PBB3"]
    out = {"isoforms": {}, "vs_vertebrate": {}}
    for a in FLY:
        out["isoforms"][a] = {
            "length": len(seqs[a]),
            "shared_prefix_with_M9PBB3": shared_prefix(ref, seqs[a]),
        }
    for v in VERT:
        out["vs_vertebrate"][v] = local(ref, seqs[v])
    print(json.dumps(out, indent=2))
    with open("results-tmem268.json", "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
