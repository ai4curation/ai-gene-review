# R (P22946) Curation Notes — Escherichia phage P1

## Functional Summary
- **Gene symbol**: `R` (first gene of the late `R-S-U` tail-fiber operon, transcribed from `LP_S`).
- **Protein**: Tail-fiber operon protein R / baseplate wedge component (`gpR`; 144 aa, ~15.6 kDa) [PMID:2526777].
- **Biological role**:
  - Guidolin et al. 1989 [PMID:2526777] sequenced the `R-S-U` operon and showed that `R` is the promoter-proximal gene preceding the tail-fiber structural gene `S` and assembly chaperone gene `U`.
  - Genetic studies summarized by Łobocka et al. 2004 [PMID:15489417] showed that amber mutations in `R` cause the same morphogenetic defect as mutations in baseplate wedge gene `26` (`gp53` homolog), `16`, and `21`: mutant infections produce complete heads and aberrant polysheaths but no assembled tail structures, indicating that `gpR` is a structural component of the P1 baseplate required for tail morphogenesis.
  - Quantitative LC-MS/MS proteomics of CsCl-purified P1 virions (Gonzales et al. 2022, [PMID:35458408]) confirmed that `gpR` is an abundant virion structural protein (25.7% sequence coverage, 5 unique peptides) and identified `gpR` by HHpred homology modeling as a baseplate wedge component orthologous to bacteriophage T4 gp8 (which in T4 forms the baseplate wedge module that connects the long tail fibers to the baseplate).
- **Existing GOA annotations**: None (`existing_annotations: []`).
- **Core functions**: Baseplate wedge component (`GO:0098025` `virus tail, baseplate`) directly involved in viral tail assembly (`GO:0098003` `viral tail assembly`) [PMID:2526777, PMID:15489417, PMID:35458408].
