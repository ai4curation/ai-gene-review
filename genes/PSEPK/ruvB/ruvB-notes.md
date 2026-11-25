# ruvB curation notes

- Q88NJ0 is the ATP-dependent branch-migration motor in the KT2440 `ruvCAB` locus. The target record assigns the ATP-driven pump and DNA-translocation activity to RuvB [UniProtKB:Q88NJ0, "The RuvB hexamer acts as an ATP-dependent pump"].
- RuvB's head domain contacts DNA, but RuvA recognizes and opens the four-way junction [UniProtKB:Q88NJ0, "The head domain binds DNA"; PMID:9501105, "loaded onto the junction by RuvA"]. GO:0000400 is therefore modified from independently `enables` to a contribution within RuvAB, symmetric with RuvA's contribution to GO:0009378.
- The RuvBL268S study confirms that ATPase, DNA binding, DNA unwinding, and RuvA-dependent branch migration are separable from full in-vivo function [PMID:9973614, "the purified protein is fully active in vitro with regard to its ATPase, DNA binding and DNA unwinding activities"]. KT2440 function remains homology-grade.

## 2026-11-09 re-review (Claude, AI-assisted; module audit)

- Earlier bullets above are superseded where they conflict. GO:0000400 four-way junction DNA binding is now KEEP_AS_NON_CORE (true but peripheral; RuvA supplies junction specificity), and the core no longer lists it as a contribution. DNA binding is TOO_GENERAL. ATP binding is non-core.
- DNA repair and DNA recombination are MODIFY to recombinational repair (GO:0000725). A NEW ISS row adds Holliday junction helicase complex (GO:0009379), the complex the core function names.
