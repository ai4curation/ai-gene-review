"""Pairwise identity of ANKRD20A1 with its full-length (823 aa) human paralogs.

Near-identical copies would make antibody, GFP-fusion and short-read evidence hard to assign
to one locus. This script
fetches the reviewed human ANKRD20A-family entries from UniProt, aligns each to ANKRD20A1
(global, BLOSUM62) and reports identity over the aligned ANKRD20A1 length.
    uv run --with biopython python paralog_identity.py
"""
import urllib.request
from Bio import Align
from Bio.Align import substitution_matrices

TARGET = "Q5TYW2"
QUERY = ("https://rest.uniprot.org/uniprotkb/search?query=gene:ANKRD20A*+AND+organism_id:9606"
         "+AND+reviewed:true&fields=accession,gene_primary,sequence&format=tsv")


def main() -> None:
    with urllib.request.urlopen(QUERY) as r:
        rows = [ln.split("\t") for ln in r.read().decode().splitlines()[1:]]
    seqs = {acc: (gene, seq) for acc, gene, seq in rows}
    tgt = seqs[TARGET][1]
    al = Align.PairwiseAligner(mode="global", open_gap_score=-10, extend_gap_score=-0.5)
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    print(f"target {TARGET} {seqs[TARGET][0]} len={len(tgt)}")
    for acc, (gene, seq) in sorted(seqs.items()):
        if acc == TARGET:
            continue
        a = al.align(tgt, seq)[0]
        ident = sum(x == y for x, y in zip(a[0], a[1]) if x != "-")
        print(f"{acc}\t{gene}\tlen={len(seq)}\tidentical_positions={ident}\tidentity_over_target={ident/len(tgt):.3f}")


if __name__ == "__main__":
    main()
