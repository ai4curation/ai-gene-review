#!/usr/bin/env python3
"""Pairwise alignment of DMS3-25 (A0SMN5) against the two chains of PDB 9OOX.

9OOX is the cryo-EM structure from PMID:41639445: Escherichia phage HK446 Rip1
(the 164-residue pore-forming antiphage defence protein, chain L..W) bound to
Enterobacteria phage T6 small terminase (the activating phage ring, chain A..K).

Question: is DMS3-25 a homologue of the DEFENCE protein (Rip1) or of the
ACTIVATING phage protein (small terminase)? The answer decides whether the
GO:0051607 annotation on DMS3-25 describes a process the protein executes
(involved_in) or one it merely triggers (acts_upstream_of_or_within_*).

Inputs: sequences.fasta (A0SMN5 verbatim from DMS3-25-uniprot.txt;
9OOX chains verbatim from https://www.rcsb.org/fasta/entry/9OOX).
Run: uv run python align_rip1.py
"""
from Bio import Align
from Bio.Align import substitution_matrices


def read_fasta(path):
    seqs, name = {}, None
    for line in open(path):
        line = line.rstrip()
        if line.startswith(">"):
            name = line[1:].split()[0]
            seqs[name] = ""
        else:
            seqs[name] += line
    return seqs


def main():
    seqs = read_fasta("sequences.fasta")
    query = seqs["A0SMN5"]

    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"

    for target in ("9OOX_2", "9OOX_1"):
        aln = aligner.align(query, seqs[target])[0]
        a, b = str(aln[0]), str(aln[1])
        ident = sum(1 for x, y in zip(a, b) if x == y and x != "-")
        aligned_cols = sum(1 for x, y in zip(a, b) if x != "-" and y != "-")
        print(f"=== A0SMN5 (175 aa) vs {target} ({len(seqs[target])} aa) ===")
        print(f"score={aln.score:.1f}  identities={ident}/{aligned_cols} "
              f"aligned columns = {100*ident/aligned_cols:.1f}% identity")
        print(aln)
        print()

    # The diagnostic motif: Rip1's C-terminal twin Cys-X-X-Cys pair.
    import re
    for name in ("A0SMN5", "9OOX_2", "9OOX_1"):
        hits = [m.group(0) for m in re.finditer(r"C..C", seqs[name])]
        print(f"{name}: CxxC motifs = {hits}")


if __name__ == "__main__":
    main()
