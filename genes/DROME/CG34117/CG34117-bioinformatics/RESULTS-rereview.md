# CG34117 (Q0KI97) re-review: comparison with human FMC1 and yeast Fmc1

Script: `compare_fmc1_rereview.py` (run with `uv run compare_fmc1_rereview.py`);
raw output: `compare_fmc1_rereview.out`. Sequences and PANTHER cross-references
are fetched live from UniProt REST.

## Family placement (from UniProt PANTHER cross-references)

| Accession | Protein | Length | PANTHER |
|---|---|---|---|
| Q0KI97 | CG34117 (D. melanogaster) | 101 | PTHR31716, PTHR31716:SF1 |
| Q96HJ9 | FMC1 / C7orf55 (human) | 113 | PTHR31716, PTHR31716:SF1 |
| P40491 | Fmc1 (S. cerevisiae) | 155 | PTHR28015, PTHR28015:SF1 |

CG34117 and human FMC1 are in the same PANTHER family and subfamily. Yeast Fmc1
is in a different PANTHER family (PTHR28015).

## Pairwise global alignments (BLOSUM62, gap -10/-0.5)

- Q0KI97 vs Q96HJ9: score 177.5, 40.6% identity over 101 aligned positions;
  collinear end-to-end alignment, with a conserved C-terminal block
  (fly HGRGERSVRDTADLVGFKLP / human HGKGERSVEESAGLVGLKLP).
- Q0KI97 vs P40491: score 30.5, gapped, with no extended conserved block.
- Q96HJ9 vs P40491: score 5.0, gapped, with no extended conserved block.

## Interpretation

CG34117 is a full-length (not fragmentary) member of the animal FMC1 subfamily,
aligning collinearly over its whole length with human FMC1. The fly and human
proteins show no convincing sequence similarity to yeast Fmc1, consistent with
their separate PANTHER families and with the statement in PMID:28719601 that the
human and yeast proteins share no BLASTP-detectable homology. The yeast and
animal proteins share only a Pfam Complex1_LYR_2 (LYRM-like) assignment.
Therefore functional transfer to CG34117 should rest on human FMC1, not yeast Fmc1.
The simple [LIVF]Y[RK] regex hits only fly position 73 (LYK). It finds no motif
in human or yeast, so it says nothing about a conserved LYR motif.
