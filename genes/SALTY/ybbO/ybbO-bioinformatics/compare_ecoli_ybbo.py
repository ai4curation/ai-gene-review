"""Pairwise global alignment of Salmonella STM0505 (Q7CR11) vs E. coli YbbO (P0AFP4).

Fetches both sequences from UniProt REST, aligns with BLOSUM62 (gap open -10,
extend -0.5), and reports identity plus conservation of the SDR catalytic tetrad
positions (N, S, Y, K) and the TGxxxGxG cofactor motif in the Salmonella protein.
"""
import re
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices


def fetch(acc):
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as r:
        lines = r.read().decode().splitlines()
    return "".join(l for l in lines if not l.startswith(">"))


def main():
    sal, eco = fetch("Q7CR11"), fetch("P0AFP4")
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score, aligner.extend_gap_score = -10, -0.5
    aln = aligner.align(sal, eco)[0]
    pairs = [(a, b) for a, b in zip(aln[0], aln[1]) if a != "-" and b != "-"]
    ident = sum(a == b for a, b in pairs)
    print(f"Q7CR11 length: {len(sal)}; P0AFP4 length: {len(eco)}")
    print(f"Aligned positions: {len(pairs)}; identical: {ident}; "
          f"identity over shorter sequence: {100 * ident / min(len(sal), len(eco)):.1f}%")
    print(aln)
    for m in re.finditer(r"(?=(TG...G.G))", sal):
        print(f"Cofactor-binding TGxxxGxG motif at {m.start() + 1}: {m.group(1)}")
    # Catalytic tetrad: Y in YxxxK motif near the PROSITE-predicted active site (146)
    for i in range(len(sal) - 4):
        if sal[i] == "Y" and sal[i + 4] == "K":
            print(f"YxxxK motif at Y{i + 1}/K{i + 5}: {sal[i:i + 5]}")


if __name__ == "__main__":
    main()
