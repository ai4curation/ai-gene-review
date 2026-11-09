# ruvA curation notes

- Q88NJ1 is the RuvA junction-recognition subunit in the contiguous KT2440 `ruvCAB` locus. Its UniProt record assigns specific Holliday-junction binding and opening to RuvA and the ATP-dependent pump to RuvB [UniProtKB:Q88NJ1, "RuvA specifically binds to HJ cruciform DNA, conferring on it an open structure"; "The RuvB hexamer acts as an ATP-dependent pump"].
- GO:0009378 is retained as a contribution rather than an independently enabled activity. RuvA loads the RuvB helicase and the two proteins jointly promote branch migration, but RuvB supplies the motor [PMID:9501105, "branch migration is catalysed by the RuvB protein, a hexameric DNA helicase that is loaded onto the junction by RuvA"; PMID:9973614, "RuvA and RuvB promote branch migration of Holliday junctions"].
- Generic DNA-helicase activity is marked over-annotated because it is meaningful only at RuvAB-complex level; ATP binding is removed because RuvA is not the ATPase motor. Neither decision removes RuvA from the RuvAB helicase complex.

## 2026-11-09 re-review (Claude, AI-assisted; module audit)

- Earlier bullets above are superseded where they conflict. GO:0009378 four-way junction helicase activity is now ACCEPT (not over-annotated), consistent with the E. coli RuvA IDA and the PAINT IBD on RuvA (PTN008659601, PTHR33796); the core keeps it as `contributes_to`. Generic DNA helicase activity and DNA binding are TOO_GENERAL.
- DNA repair and DNA recombination are MODIFY to recombinational repair (GO:0000725), the term used on the E. coli orthologs; ARBA DNA damage response is TOO_GENERAL.
- ATP binding stays REMOVE and is now recorded as an InterPro2GO source defect.
- Q88NJ1 has no PANTHER assignment; E. coli RuvA is in PTHR33796:SF1. The module grounds the RuvA step to InterPro IPR000085 instead (see module notes).
