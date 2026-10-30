"""Global pairwise identity of a query against characterized trans-sulfuration
family (PTHR11808 / Pfam PF01053) members, plus their PANTHER subfamily and EC.

Usage: python placement_identity.py QUERY_ACC REF_ACC [REF_ACC ...]

Sequences and annotations are fetched live from the UniProt REST API.
Alignment: Needleman-Wunsch (Biopython PairwiseAligner, global), BLOSUM62,
gap open -10, extend -0.5. Identity = identical columns / shorter sequence length.
Also reports the position of the PLP Schiff-base lysine in an S-x-T/S-K-[FY] motif.
"""
import re
import sys
import urllib.request

from Bio.Align import PairwiseAligner, substitution_matrices

UNIPROT = "https://rest.uniprot.org/uniprotkb"


def fetch(url: str) -> str:
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read().decode()


def seq(acc: str) -> str:
    return "".join(fetch(f"{UNIPROT}/{acc}.fasta").splitlines()[1:])


def meta(acc: str) -> list[str]:
    tsv = fetch(f"{UNIPROT}/{acc}?fields=gene_primary,protein_name,ec,xref_panther&format=tsv")
    return tsv.splitlines()[1].split("\t")


def main() -> None:
    query, refs = sys.argv[1], sys.argv[2:]
    al = PairwiseAligner(mode="global")
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score = -10, -0.5
    q = seq(query)
    qm = meta(query)
    m = re.search(r"S.[TS]K[FY]", q)
    print(f"query\t{query}\t{qm[0]}\tlen={len(q)}\tPANTHER={qm[3]}")
    print(f"PLP-lysine motif\t{m.group(0) if m else 'none'}\tK{m.start() + 4 if m else '-'}")
    print("ref\tgene\tEC\tPANTHER\tidentity_pct\tprotein_name")
    for acc in refs:
        s = seq(acc)
        a = al.align(q, s)[0]
        ident = sum(1 for x, y in zip(a[0], a[1]) if x == y and x != "-")
        g, name, ec, panther = meta(acc)
        print(f"{acc}\t{g}\t{ec}\t{panther}\t{100 * ident / min(len(q), len(s)):.1f}\t{name[:60]}")


if __name__ == "__main__":
    main()
