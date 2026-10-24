# RRT2 / DPH7 / ERE1 (YBR246W, P38332) notes

Module `diphthamide_biosynthesis`, step 3 (EC 3.1.1.97 diphthine methylesterase).

- ybr246w accumulates diphthine [PMID:22188241 "the deletion of YBR246W leads to the accumulation of diphthine"].
- Methylesterase [PMID:24739148 "Dph7 is a methylesterase that hydrolyzes methylated diphthine to produce diphthine"]; not the synthetase [PMID:24739148 "Dph7 is not the diphthamide synthetase, as it lacks the ATP-binding domain required."; PMID:23169644 "it lacks an ATP-dependent catalytic domain"].
- Moonlighting as Ere1 in retromer recycling of Can1 [PMID:21880895 "Ere1 is required for Can1 recycling via the retromer-mediated pathway"]; mostly cytoplasmic, transiently endosomal [PMID:21880895 "In wild-type cells, Ere1-GFP was mostly cytoplasmic"].
- Reactome R-SCE-5367021 describes cytosolic RRT2 demethylating Me-diphthine EFT1.

Observations: YeastCyc DIPHTINE--AMMONIA-LIGASE-RXN (EC 6.3.1.14) is assigned to RRT2 citing PMID:22188241; this is wrong (DPH6 is the ligase). The derived RCA GO:0017178 is REMOVED. Endosome / endocytic recycling kept as non-core.
