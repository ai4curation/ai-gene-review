# NCU06005 (Q7S2F2) re-review sequence analysis (2026-10-21)

Script: `compare_sequences_rereview.py` (PEP 723; run with `uv run --script compare_sequences_rereview.py`).
Raw output: `RESULTS-rereview-raw.txt`. All values below are copied from that output; data are live UniProt REST queries.

## 1. Glycerol kinase gene complement of the N. crassa OR74A proteome

Only two N. crassa (taxon 367110) UniProt entries belong to PANTHER PTHR10196 (FGGY sugar kinase):

- Q7S2F2 NCU06005, glycerol kinase, 584 aa, PTHR10196:SF69 (GLYCEROL KINASE)
- A7UWY8 NCU11353, xylulose kinase, 590 aa, PTHR10196:SF57 (XYLULOSE KINASE)

Q7S2F2 is the only N. crassa entry carrying EC 2.7.1.30. NCU06005 is therefore the sole glycerol kinase gene in the reference proteome.
Its UniProt record places it on Linkage Group VI, the chromosome to which the classical glycerokinase structural gene glp-4 was mapped (PMID:6284716 abstract lists glp-1, glp-2 and glp-4 lesions on chromosomes I, II and VI).
Together these make NCU06005 the only plausible molecular identity of glp-4, although no published complementation or sequencing of a glp-4 allele was found.

## 2. Relationship to characterized glycerol kinases

Global BLOSUM62 alignment (gap open -10, extend -0.5), identity over aligned columns:

| Accession | Protein | Length | PANTHER subfamily | Identity |
|---|---|---|---|---|
| P32190 | S. cerevisiae GUT1 | 709 aa | PTHR10196:SF69 | 46.2% |
| Q9M8L4 | A. thaliana GLPK | 522 aa | PTHR10196:SF69 | 50.8% |
| P0A6F3 | E. coli GlpK | 502 aa | PTHR10196:SF69 | 45.9% |
| P32189 | human GK | 559 aa | PTHR10196:SF56 | 51.3% |

NCU06005 shares PANTHER subfamily SF69 with yeast GUT1, Arabidopsis GLPK and E. coli GlpK (all experimentally characterized glycerol kinases); mammalian GK is in a separate subfamily (SF56). Pairwise identity is similar (46-51%) to all of them, so subfamily membership, not best hit, is used to choose the closest characterized relative (GUT1, the fungal SF69 member).

## 3. N-terminal segment

Residues 1-63 (before the Pfam FGGY_N domain at 64): `MKLLNLNDGVEAGVMCVEPTLTNDGMDARNLAKAHKGPIVTHLEHLPRGIHETPEERKNHWFV`.
K+R = 7, D+E = 9, net charge -2. This is not the positively charged, acid-poor composition typical of a presequence-type mitochondrial targeting signal. This is a crude composition test, not a targeting predictor; it does not exclude a minor or internally targeted mitochondrial pool.
