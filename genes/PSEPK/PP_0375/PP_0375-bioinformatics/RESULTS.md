# PP_0375 PqqG/PqqM ortholog check

## Question

Is KT2440 PP_0375 (UniProt Q88QV9) a close sequence homolog of the
experimentally implicated Pseudomonas fluorescens B16 PqqG/PqqM protein
(GenPept AAX10035.1)?

## Method

The script downloads PP_0375 and two comparison proteins from UniProt and NCBI
and compares them with MMseqs2 `easy-search`:

```bash
./compare_pqqg_ortholog.sh results
```

## Result

Q88QV9 aligned to AAX10035.1 at 66.0% amino-acid identity across 606 residues,
covering 98.9% of Q88QV9 and 99.8% of AAX10035.1. The alignment had an E-value
of 5.125e-294 and a bit score of 817.

Q88QV9 aligned to the *Pseudomonas aeruginosa* PA1990/PqqH protein Q9I2B9 at
52.2% amino-acid identity across 597 residues, covering 97.1% of Q88QV9 and
98.2% of Q9I2B9. The alignment had an E-value of 2.409e-197 and a bit score of
569.

## Interpretation

The nearly full-length, high-identity match supports transfer of broad
PqqG/PqqM pathway association by sequence similarity. It does not establish
the native PP_0375 substrate or prove that this S9 peptidase directly processes
PqqA. Those mechanistic questions remain open.

The NCBI protein record names AAX10035.1 as the *Pseudomonas fluorescens* B16
`pqqG` gene product, a dipeptidyl aminopeptidase/acylaminoacyl-peptidase. The
B16 full text names `pqqM` among 11 ORFs and states that "the Tn3-gusA
insertions in each ORF abolished PQQ production" [PMID:18055583;
PMCID:PMC2245851]. This supplies gene-specific pathway genetics but does not
identify the PqqM substrate or biochemical reaction. The KT2440 operon study
independently names PP_0375 as putative `pqqG` based on conserved locus and
sequence [PMID:27287323].

The PA1990 study reports that disruption of this S9-family ortholog eliminated
PQQ excretion into the culture supernatant, whereas a separate `pqqF` mutant
could not produce PQQ [PMID:19902179]. Thus, close homologs support a conserved
PQQ-pathway association but do not establish whether PP_0375 acts in precursor
maturation, PQQ export, or both.
