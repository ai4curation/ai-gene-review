# UppS curation notes

- OpenScientist was allowed to run for the full configured 7200 seconds on
  2026-09-01 and returned no report. No provider-named deep-research file was
  synthesized manually.
- The reaction assignment is retained from the exact target UniProt/HAMAP
  record: Q88MH6 condenses eight IPP units with FPP to produce C55-PP
  [file:PSEPK/uppS/uppS-uniprot.txt "Catalyzes the sequential condensation of isopentenyl diphosphate (IPP) with (2E,6E)-farnesyl diphosphate (E,E-FPP)"].
- UppS supplies a shared envelope-glycan carrier precursor; peptidoglycan
  biosynthesis is downstream use rather than the sole core process
  [file:PSEPK/uppS/uppS-uniprot.txt "UPP is the precursor of glycosyl carrier lipid in the biosynthesis of bacterial cell wall polysaccharide components such as peptidoglycan and lipopolysaccharide."].
- PANTHER places Q88MH6 and E. coli UppS in PTHR10291:SF0. The module asserts
  that established identifier with the exact official label
  "DEHYDRODOLICHYL DIPHOSPHATE SYNTHASE 2" and uses `preferred_term` to state
  the bacterial UppS role clearly.

## 2026-11-02 completion pass

- Parent MF rows (GO:0004659, GO:0016765, GO:0045547) changed to TOO_GENERAL:
  GO:0008834 is accepted and entails them; matches the E. coli ispU review.
- Cytosol (TreeGrafter IEA) changed from UNDECIDED to ACCEPT: the E. coli ortholog is
  cytosolic by IDA and purified from the soluble fraction
  [PMID:9882662 "was purified from the soluble fraction of Escherichia coli"], and
  Q88MH6 has no membrane features. Status set to COMPLETE.
