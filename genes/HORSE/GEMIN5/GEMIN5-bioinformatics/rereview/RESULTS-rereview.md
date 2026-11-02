# GEMIN5 (horse) re-review: gene-model and residue analysis (2026-10-20)

Inputs: UniProt FASTA files for human Q8TEQ6 and the four horse GEMIN5 entries,
downloaded from rest.uniprot.org on 2026-10-20 and kept in this folder.
All four horse entries are products of the same Ensembl gene, ENSECAG00000020479.3.

Scripts (run with `uv run <script>`):

- `compare_isoforms_rereview.py`: global alignment (BLOSUM62, gap open -10, extend -0.5, free end gaps) of each horse entry to human. Raw output: `RESULTS-rereview-raw.txt`.
- `check_residues_rereview.py`: maps the human RNA-contact residues mutated in PMID:27881601 onto the horse models. Raw output: `RESULTS-residues-raw.txt`.

## Horse GEMIN5 gene models

| Accession | Length | Identity to human | Human segments absent (>=5 aa) |
|---|---|---|---|
| F6WDM0 | 1517 | 0.888 | none (9-aa insertion after human 618) |
| A0A9L0R5P7 (benchmark) | 1433 | 0.892 | 723-798 |
| A0A3Q2H9B3 | 1420 | 0.895 | 1421-1508 (C-terminus) |
| A0A9L0TIL3 | 1471 | 0.889 | 799-836 |

F6WDM0 is the full-length product of the gene. It is the entry that carries the VGNC gene name and the PAINT IBA annotations from node PTN005299808 in GOA. The benchmark accession A0A9L0R5P7 is an alternative-transcript product of the same gene (ENSECAT00000103662.1). It lacks a 76-residue internal block that corresponds to human 723-798.

## Where the missing block lies

In the human crystal structure, the folded tandem WD40 region spans residues 3-722 (PMID:27881601). The block missing from A0A9L0R5P7 begins at human 723. It therefore sits C-terminal to the structured RNA-recognition module, not inside it. In the human UniProt record this stretch is annotated as a disordered region (715-790, MobiDB-lite). It carries phosphorylation sites (T751, S757, S770, S778) and a SUMO2 acceptor lysine (K754) from large-scale proteomics. The C-terminal TPR-like and RBS regions (Pfam PF23774, PF23777) are retained in A0A9L0R5P7.

The earlier note (RESULTS.md) said the deletion spans the end of the WD40 RNA-recognition module. That holds only against the 1-739 construct boundary. Measured against the solved structure (3-722), the deletion lies entirely outside the WD40 fold.

## Conservation of RNA-contact residues

All 12 human residues mutated in PMID:27881601 (N13, W14, Y15, R33, R335, M357, R359, F381, Y383, M403, W422, Y474) are identical at the aligned positions in both A0A9L0R5P7 and F6WDM0.

## Interpretation and limits

The benchmark isoform keeps the complete snRNA/cap-recognition module, its experimentally mapped contact residues, and the C-terminal regions. It lacks a disordered, modification-rich linker. No experiment tests whether this horse transcript is expressed as protein or whether the linker affects function. The analysis says nothing about the SMN 3'-UTR binding interface, which has not been mapped to a domain.
