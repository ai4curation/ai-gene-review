# UBC9 (P50623) subfamily placement and active-site check

Script: `subfamily_and_active_site.py` (run with `uv run --script subfamily_and_active_site.py`;
raw output in `results-run.txt`). Data were pulled live from the PANTHER geneinfo
service and UniProt REST on 2026-10-21.

## PANTHER subfamily placement

| accession | protein | PANTHER subfamily | identity to P50623 | residue at yeast C93 |
|---|---|---|---|---|
| P50623 | S. cerevisiae UBC9 | PTHR24067:SF248 | 157/157 (100.0%) | C93 |
| P40984 | S. pombe hus5 | PTHR24067:SF248 | 95/157 (60.5%) | C93 |
| Q1K772 | N. crassa NCU04302 | PTHR24067:SF248 | 91/156 (58.3%) | C92 |
| P63279 | H. sapiens UBE2I | PTHR24067:SF280 | 88/157 (56.1%) | C93 |

S. cerevisiae Ubc9 P50623 is placed in PANTHER subfamily PTHR24067:SF248, together with S. pombe hus5 P40984 and Neurospora NCU04302 Q1K772; human UBE2I P63279 is in PTHR24067:SF280.

The yeast catalytic cysteine Cys93 (UniProt ACT_SITE, glycyl thioester intermediate) aligns to a cysteine in all three other proteins.

## Interpretation

- SF248 (fungal Ubc9 proteins) and SF280 (vertebrate UBE2I) are sister subfamilies.
  Both descend from the PAINT Ubc9 node PTN000629675, and SGD:S000002222 (this gene)
  is one of that node's experimental seeds (see `interpro/panther/PTHR24067/PTHR24067-paint.tsv`).
- Global identity to the fission-yeast and Neurospora proteins (58-61%) is only a little
  higher than to human UBE2I (56%). The subfamily split does not reflect a large difference
  in sequence and does not show any change of function. The node-level terms (SUMO
  conjugating enzyme activity, protein sumoylation, nucleus) apply to both branches.
- The catalytic cysteine is retained in every protein checked, so nothing here points to a
  pseudoenzyme. Retaining the residue does not by itself prove activity: the S. pombe
  Hus5.62 mutant still forms a thioester but is defective in conjugation.
