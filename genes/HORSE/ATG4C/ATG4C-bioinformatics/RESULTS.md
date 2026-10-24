# ATG4C (horse A0A3Q2H6C4): gene-model comparison with human ATG4C and donkey ATG4C

Script: `compare_sequences.py` (PEP 723; run with `uv run --script genes/HORSE/ATG4C/ATG4C-bioinformatics/compare_sequences.py`).
Output: `results.json`. Inputs are the repository UniProt flat files for horse A0A3Q2H6C4 (666 aa),
human Q96DT6 (Swiss-Prot, 458 aa; copy in `genes/EQUAS/ATG4C/ATG4C-bioinformatics/`) and donkey
A0A9L0IIU3 (458 aa). Alignments use Biopython PairwiseAligner with BLOSUM62, gap open -10, extend -0.5.

## Findings

- Horse residues 1-400 align ungapped to human ATG4C 1-400; per-50-residue identity is 90-100% in every window
  from 1 to 400 (100% in 1-50, 201-250 and 351-400).
- Identity collapses after residue ~403: 8.0% in window 401-450 and 25.0% in 451-458 (ungapped comparison).
- The horse model's residues 404-666 (263 residues) have no significant local similarity to the human C-terminal
  tail 404-458 (best local alignment score 27.5, BLOSUM62, i.e. background level).
- The horse C-terminal extension is low-complexity (Pro-rich SPPR repeats, Gly-rich end) and is flagged as disordered
  by MobiDB-lite in the UniProt record; the human tail ending ...KRFSTEEFVLL is absent.
- The catalytic triad maps: human C111 -> horse C111 (nucleophile), D345 -> D345, H347 -> H347.
- The donkey ATG4C model (A0A9L0IIU3) is full-length and colinear with human over all 458 residues (94.98% identity).
  Horse and donkey are congeneric, so the 666-residue horse product with a divergent C-terminus is most likely an
  Ensembl gene-model error in the last exon(s), not a real horse-specific protein.

## Interpretation

A0A3Q2H6C4 is an aberrant gene model of horse ATG4C: the peptidase C54 catalytic domain (UniProt Pfam domain 77-398)
and the Cys-Asp-His triad are intact, but the canonical C-terminal ~55 residues are missing and replaced by ~263
residues of unrelated, low-complexity sequence. Functional inferences for the gene can rest on the conserved catalytic
domain; nothing should be inferred from the aberrant C-terminal extension.
This analysis does not prove the exon structure; it only shows the sequence divergence.
