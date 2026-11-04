# vanA (Q6FDI6, ACIAD0980, Acinetobacter baylyi ADP1) curation notes

## 2026-11-04 review

No provider deep-research file was generated (no provider API keys in this
session). Sources: UniProt Q6FDI6 (unreviewed genome entry) and the cached
abstracts of Segura et al. 1999 (PMID:10348863) and Morawski et al. 2000
(PMID:10671462). A second unreviewed entry, O24841, holds the vanA sequence
submitted with the 1999 study (EMBL AAC27107.1); it is recorded in
alternative_records. The two sequences differ at 12 of 358 positions
(vanA-bioinformatics/RESULTS.md, from compare_records.py). For VanB, UniProt
merged the 1999 (AAC27106.1) and genome (CAG67871.1) submissions into the
Swiss-Prot entry O24840, which is why vanB is reviewed on a reviewed record.

- Genetics: "Genetic evidence supporting this conclusion was obtained by
  characterization of mutant Acinetobacter strains blocked in catabolism of both
  ferulate and vanillate." [PMID:10348863]
- VanAB is "a two-component monooxygenase"; PCR mutagenesis of vanAB yielded
  strains unable to metabolize vanillate, and missense mutations cluster in
  catalytic regions [PMID:10671462].
- Sequence check: the Rieske motif is intact (Cys47, His49, Cys66, His69 in a
  CxH...CxxH arrangement, computed from the UniProt sequence), despite the
  record's generic ProRule CAUTION. The C-terminal VanA_C catalytic domain is
  present.
- PANTHER PTHR21266:SF60, a subfamily that also holds KshA, NdmA/B, DdmC, PrnD
  and TsaM; see the PTHR21266 family review.
