# OPI3 (PEM2, YJR073C, P05375) notes

## Identity
- Phospholipid N-methyltransferase (PLMT), EC 2.1.1.71 (minor 2.1.1.17); PEMT family; ER multi-pass membrane protein [UniProt:P05375].

## Evidence
- PEM2 membranes convert PE to PC; prefer PMME/PDME [PMID:2445736 "the membrane fraction from the transformants carrying PEM2 catalyzed the synthesis of phosphatidylcholine (PC) from PE, indicating that it contains all of the three methylation activities"].
- pem2 disruption loses 2nd and 3rd methylations [PMID:2684666 "When the PEM2 locus was disrupted, the activities for the second and third methylations were totally lost, but that for the first methylation remained."]
- PLMT kinetics in cho2 disruptants [PMID:2198947 "phospholipid methyltransferase (PLMT) catalyzes the second two methylation reactions"].
- opi3-3 mutant: 2-3% PC without choline, accumulates PMME/PDME [PMID:6337128 "The Saccharomyces cerevisiae opi3-3 mutant was shown to be defective in the synthesis of phosphatidylcholine via methylation of phosphatidylethanolamine."]
- PE-methylation activity microsomal [PMID:3005242 "phosphatidylethanolamine methyltransferase activity was confined to microsomal fractions"].

## Curation decisions
- Core: GO:0000773 + PC biosynthesis at ER membrane. GO:0004608 (first methylation) non-core (minor, Cho2 is main enzyme).
- Mitochondrial / cell-periphery HDA/EXP kept non-core (likely contact-site association). Cytosol RCA removed.
