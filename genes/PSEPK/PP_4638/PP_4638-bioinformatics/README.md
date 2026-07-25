# PP_4638 MTHFR-family comparison

## Objective

Assess whether PP_4638 (Q88E30) can be treated as equivalent to the canonical
Pseudomonas putida MetF protein Q88D51, or only as an MTHFR-like candidate.

The workflow compares both P. putida proteins with experimentally characterized
E. coli MetF (P0AEZ1) and reverse-direction S6MTHFR (BAK65950.1). It also retrieves
current InterPro coordinates for the two P. putida proteins. Pairwise similarity
does not establish reaction direction, cofactor specificity, or in vivo function;
those remain evidence questions for the gene review.

## Run

```bash
just analyze
```

The command writes downloaded sequences and tabular results under `results/`.
Inputs and outputs are passed as arguments to the analysis script; the script
does not encode gene-specific paths or conclusions.
