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


## 2026-10-26 — independent member audit

Reassessed every existing annotation/proposal with unchanged term, evidence, reference, qualifier and donor fields. No new row was added. Family and role inference are separated from native target assays. The 2000 E. coli deletion study is available in a normal PMC URL cache; full S-313 PMID:10781557 exposes transporter redundancy and conditional SsuE dispensability. These are not KT2440 knockout results.

A fresh literature search found Garret William O'Connell's 2024 DTU thesis, chapter 1: native KT2440 ΔssuD and combined ΔssuBC growth tests, strain mapping, and Figure 4 were inspected. The chapter was a manuscript in preparation; a matching journal publication was not established. The experiments support target pathway placement but do not isolate individual B/C activities, or test individual A/E necessity. Composite growth fitness is not a direct import-rate measurement, and the source documents contamination concerns for some sulfur compounds. The full normal URL cache is in publications/. No direct target kinetic constants, expanded substrate spectrum or PFAS-degradation claim is inferred.

SsuA support excludes ARBA-only CC fields and uses independent NCBIfam/CDD plus SignalP export evidence. Actual Falcon/fallback and fitness acquisition outcomes are recorded in the shared foundation logs; no failed provider output was fabricated. Existing genuine SsuB/SsuD reports remain discovery context. GOA files are annotation state, never biological support.

Focused schema, term, title and source-quote validation: valid with zero errors. Two panel advisories concern available but uncited genuine provider reports (SsuB/SsuD); independent primary/classification support is used rather than copying provider prose to silence them. All five helper histories and renders pass. No panel accession occurs in the cached GO-CAM index.
