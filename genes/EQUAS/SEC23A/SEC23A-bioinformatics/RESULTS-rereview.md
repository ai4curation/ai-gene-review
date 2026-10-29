# SEC23A (donkey): gene-model comparison for the 2026-10-21 re-review

Reproduce (from this folder):
`uv run --script compare_gene_models_rereview.py rereview-sequences > compare_gene_models_rereview_output.txt`

The script queries the UniProt gene-centric service for A0A9L0IQB9, downloads every donkey
SEC23A product in that gene-centric group, globally aligns each to human SEC23A Q15436
(Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5), lists the Ensembl
transcripts of the donkey gene and diffs the exon coordinates of the benchmark transcript
against those of the transcript that encodes the UniProt canonical. Raw output is in
`compare_gene_models_rereview_output.txt`; sequences are in `rereview-sequences/`.
The earlier `RESULTS.md` (pairwise donkey-human alignment) is unchanged and still valid.

## Findings

- UniProt gene-centric canonical for donkey SEC23A: A0A9L0JMP6 (765 aa). A0A9L0IQB9 is one
  of five other members of the same gene-centric group (A0A8C4LKL1 771 aa, A0A9L0ITE5 99 aa,
  A0A8C4LJA7 736 aa, A0A9L0IQB9 739 aa, A0A8C4LGG5 751 aa). All six are encoded by one Ensembl
  gene, ENSEASG00005007615 (chromosome 2).
- The canonical A0A9L0JMP6 aligns end-to-end with human SEC23A, 99.35% identity over 765 pairs,
  100% coverage, no gaps.
- The benchmark A0A9L0IQB9 (transcript ENSEAST00005045719, 19 exons) is 99.32% identical to
  human over 739 pairs and lacks the 26-residue segment equivalent to human 554-579
  (CQKFGEYHKDDPSSFRFSETFSLYPQ). Compared with the canonical transcript ENSEAST00005083518
  (20 exons), the benchmark transcript lacks one 78-nt exon (chr2:220699373-220699450),
  an in-frame exon skip that removes exactly 26 codons; the only other exon difference is the
  length of the last exon (UTR end).
- Every characterised functional residue of human SEC23A maps to an identical residue in
  A0A9L0IQB9: the zinc-finger ligands C61, C66, C85, C88; F382 (the residue mutated in
  cranio-lenticulo-sutural dysplasia); and the gelsolin-like PPP-motif-binding residues
  F628, Y672, Y678, F681 (donkey F602, Y646, Y652, F655).

## Interpretation

A0A9L0IQB9 is an alternative transcript product (in-frame exon-skipping model) of donkey
SEC23A, not the canonical product. The skipped segment sits in the linker between the helical
domain and the gelsolin-like repeat (human 632-718), so all annotated domains and functional
residues are retained. Whether this transcript is expressed in donkey tissues is not
established by any data here (no cDNA, no proteomics; human UniProt lists no isoform lacking
this segment). Function claims for A0A9L0IQB9 are therefore transfers from the canonical
SEC23A product, and the effect of the 26-residue deletion on coat assembly is unknown.
