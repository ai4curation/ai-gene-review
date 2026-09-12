# ssuA curation notes

## Identity and paralog discrimination

- Q88R96 is PP_0237 in the contiguous KT2440 `ssuEADCB` locus
  (PP_0236-PP_0240). This synteny matches the SsuABC/SsuED organization
  established genetically in *Pseudomonas putida* S-313 [PMID:10781557,
  "an ATP-binding cassette-type transporter (ssuABC), a two-component reduced
  flavin mononucleotide-dependent monooxygenase (ssuED)"].
- UniProt places Q88R96 in the joint bacterial SsuA/TauA solute-binding family,
  so family membership alone cannot establish substrate specificity
  [file:PSEPK/ssuA/ssuA-uniprot.txt, "Belongs to the bacterial solute-binding
  protein SsuA/TauA family"]. KT2440 has a separate TauABC locus with TauA
  Q88RA0. PP_0237 synteny and the S-313 exclusion of taurine/cysteate from the
  tested Ssu phenotype support the alkanesulfonate assignment [PMID:10781557,
  "aliphatic sulfonates other than the natural sulfonates taurine and
  cysteate"].
- E. coli SsuA P75853 is the explicit ISS comparator. The target record's
  signal peptide and periplasmic assignment support the binding-protein role
  [file:PSEPK/ssuA/ssuA-uniprot.txt, "SUBCELLULAR LOCATION: Periplasm"].

## Research coverage

The completed OpenScientist process for `ssuA` did not materialize a report in
this worktree. No provider output was reconstructed or invented. Curation uses
the exact UniProt record, cached primary literature, synteny, the separate
KT2440 TauABC reviews, and verified E. coli exemplars.

## Residual uncertainty

Direct ligand-binding measurements for Q88R96 are unavailable. The substrate
range and discrimination against taurine should be tested with purified SsuA
and a clean KT2440 deletion/complementation series.
