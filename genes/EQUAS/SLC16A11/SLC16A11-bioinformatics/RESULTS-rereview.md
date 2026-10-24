# SLC16A11 (donkey): comparison of all donkey gene models with human MCT11 (re-review, 2026-10-21)

Script: `compare_gene_models_rereview.py` (PEP 723; Biopython PairwiseAligner, global with free end gaps, BLOSUM62, gap open -10, extend -0.5).
Command: `uv run --script compare_gene_models_rereview.py alignment_rereview`
Outputs: `alignment_rereview/results_rereview.json` (all numbers below), and the fetched FASTA files in `alignment_rereview/`.
The earlier analysis (`RESULTS.md`, `align_to_human.py`) is left unchanged; this re-review adds the other donkey entries for the same gene.

## Donkey UniProt entries for SLC16A11

UniProt holds five unreviewed donkey entries named SLC16A11, all cross-referenced to one Ensembl gene, ENSEASG00005017919.2 (chromosome 13), each from a different Ensembl transcript. They are alternative transcript models of one gene, not paralogs. All five carry PANTHER PTHR11360:SF80 (MONOCARBOXYLATE TRANSPORTER 11).

| Accession | Length | Starts with Met | Identity to human over aligned pairs (%) | TM1 / TM2 / TM3 identical fraction | Identical C-terminal suffix shared with A0A8C4PS96 |
|---|---|---|---|---|---|
| A0A8C4PS96 | 520 | yes | 90.6 | 0.95 / 0.95 / 0.90 | whole sequence (reference) |
| A0A9L0J0E5 | 472 | yes | 90.5 | 0.95 / 0.67 / 0.00 | 331 residues (142-472) |
| A0A9L0JV53 (benchmark) | 439 | no | 83.0 | 0.00 / 0.19 / 0.29 | 332 residues (108-439 = A0A8C4PS96 189-520) |
| A0A9L0JFG5 | 434 | yes | 77.6 | 0.19 / 0.14 / 0.14 | 332 residues (103-434) |
| A0A9L0JZU6 | 416 | no | 80.8 | 0.00 / 0.00 / 0.00 | 0 (different C-terminus) |

TM1-TM3 are the human Q8NCK7 positions 12-32, 54-74 and 82-102 (UniProt sequence-analysis helices).

## Results

- A0A8C4PS96 (520 aa) is the only donkey model that contains the whole human MCT11 sequence: all 447 human residues align, at 90.6% identity, and human Met1 corresponds to donkey residue 74. The 73 residues before it are an N-terminal extension.
- The benchmark entry A0A9L0JV53 (439 aa) does not start with methionine. Its residues 108-439 are identical to A0A8C4PS96 residues 189-520, which correspond to human residues 116-447. Residues 1-107 are a different sequence: the alignment forces some of them against human residues 65-115, but they do not match human TM1-TM3 (0%, 19% and 29% of positions identical).
- By inspection of the FASTA files (not computed by the script), A0A9L0JFG5 contains the same segment GDVPILGKQPEAGSQGCQIPRGGTDVETSLIG that sits just before the shared C-terminal region in A0A9L0JV53, so that segment comes from an alternative 5' exon used by more than one Ensembl transcript, not from a single misassembly.

## Interpretation

A0A9L0JV53 is an alternative transcript model of donkey SLC16A11 that lacks the first three of the twelve MFS transmembrane helices. Its C-terminal 332 residues are identical to the corresponding part of the full-length model A0A8C4PS96. A0A8C4PS96 is the most complete product of the gene and the best candidate for the canonical donkey MCT11; its 73-residue N-terminal extension resembles the extended N-termini that UniProt flags as erroneous initiation in human cDNAs (Q8NCK7 sequence caution). Whether the A0A9L0JV53 transcript is translated in donkey tissues is not known; if it is, the product would be a truncated MFS fold and is unlikely to transport on its own.
