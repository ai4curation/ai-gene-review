# PP_2928 evidence notes

## 2026-08-11

PP_2928/Q88IS1 is immediately adjacent to nspC and its exact UniProt record
places it in the CASDH-related PTHR43796:SF2 family with IPR005097. These
checkable family, length, and synteny observations support transfer of the
experimentally established alternative polyamine pathway, without relying on
the unreproducible sequence-identity percentages in the OpenScientist report.

The paired CANSDH/CANSDC route was established genetically in Vibrio cholerae,
and CASDH chemistry was characterized structurally and biochemically in
Helicobacter pylori. [PMID:19196710 "deletion of either CANSDC or the putative
CANSDH led to loss of sym-norspermidine and spermidine"; PMID:36283333 "CASDH
condenses putrescine and aspartate β-semialdehyde into carboxyspermidine in
an NADPH-dependent manner"]

No direct KT2440 PP_2928 enzyme assay is available, so the assignment remains ISS.

## 2026-11-02 (module curation: bacterial_carboxyspermidine_biosynthesis)

- Added verbatim quotes to the two NEW rows and the core function: V. cholerae
  genetics showing the CANSDH uses putrescine to make carboxyspermidine
  [PMID:19196710 "it increasingly uses putrescine as a substrate and forms
  carboxyspermidine, which is then converted to spermidine by CANSDC"] and the
  comparative-genomics result that CASDH/CASDC orthologues cluster with
  putrescine-biosynthesis genes [PMID:22025614].
- The PTHR43796 family review (interpro/panther/PTHR43796/PTHR43796-review.yaml)
  now records SF2 as the CASDH/CANSDH subfamily, with V. cholerae Q9KRL3
  (VC_1624; genes/VIBCH/VC_1624) as the experimentally characterized reference.
- No GOA rows exist for Q88IS1; both annotations remain NEW ISS inferences.
