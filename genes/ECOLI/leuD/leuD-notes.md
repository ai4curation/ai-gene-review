# E. coli leuD (P30126) curation notes

Provider deep research was not run for this gene. These notes record the
literature read for the review (cached abstracts under `publications/`).

- Isomerase subunit structure: see genes/ECOLI/leuC/leuC-notes.md; LeuD has
  no cofactor of its own (the [4Fe-4S] cluster is bound by LeuC cysteines in
  UniProt P0A6A6).
- Two-subunit enzyme in the Salmonella ortholog [PMID:7026530 "It is a complex enzyme composed of two subunits which are coded for by two genes of the leucine operon, leuC and leuD."].
- All three GO:0003861 rows (IBA, IEA) accepted with WRONG_QUALIFIER
  (enables -> contributes_to) source defects, matching SALTY and PSEPK leuD.
- The IMP complex row (EcoliWiki, PMID:4587614) cites an abstract-only paper
  whose gene-enzyme assignments were not visible; accepted with deference.
