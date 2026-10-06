# TPS3 (YMR261C) notes

UniProt P38426; module `trehalose_metabolism` (TSL1/TPS3-type regulatory subunit annoton, GO:0030234).

## Evidence journal
- Fourth subunit, partially redundant with Tsl1 [PMID:9837904 "We conclude that Tps3 is a fourth subunit of the complex with functions partially redundant to those of Tsl1"].
- Activity effects [PMID:9837904 "Deletion of TPS3, in particular in a tsl1Delta background, reduced both TPS and TPP activities and trehalose content"].
- Not able to replace Tps1 [PMID:9837904 "Even when overproduced, none of the other subunits could take over this function of Tps1 despite the homology shared by all four proteins"].
- Two-hybrid with Tps1/Tps2 [PMID:9194697 "both TsI1 and Tps3 can interact with Tps1 and Tps2"].
- Homomer and Tsl1 heteromer detected by DHFR-PCA (PMID:31454312, PMID:18467557) per GOA IPI rows.
- 13500 molecules/cell vs 1960 for Tsl1 in log phase [UniProt:P38426, UniProt:P38427].

## Curation decisions
- GO:0003824 marked over-annotated; protein binding REMOVE; identical protein binding KEEP_AS_NON_CORE.
- Regulatory mechanism (phosphate / F6P sensitivity) is only directly shown for Tsl1; Tps3 enzyme regulator activity rests on IMP.
