# RNR3 (P21672) notes

Module: `dntp_de_novo_synthesis`, role = alternative large (R1/alpha) subunit of class Ia RNR.

## Evidence journal
- Alternative, non-essential large subunit, ~80% identical to Rnr1; high-copy RNR3 suppresses rnr1 [PMID:2199320 "A high-copy-number clone of RNR3 is able to suppress the lethality of rnr1 mutations."]
- Very low intrinsic activity, activated with Rnr1 [PMID:11893751 "The in vitro activity of Rnr3 was less than 1% of the Rnr1 activity."; "a strong synergism between Rnr3 and Rnr1 was observed"]
- Cytoplasmic, detectable only after HU/MMS or in crt1 [PMID:12732713 "Interestingly, under each of these conditions, Rnr3 was predominantly present in the cytoplasm"]
- UniProt: allosteric specificity/activity sites on the large subunit (by similarity) [UniProt:P21672]

## Annotation decisions
- RNR activity (IDA contributes_to, IEA, RCA) ACCEPT; ATP binding KEEP_AS_NON_CORE (allosteric site).
- Mitochondrion HDA x2: KEEP_AS_NON_CORE; no evidence for intramitochondrial RNR in yeast.
- GO:0106387 'de novo' GMP biosynthesis (RCA from YeastPathways PWY-7222-1): REMOVE, pathway-to-GO mapping error (RNR makes dGDP).

## Module/YeastCyc observations
- YeastCyc lists RNR1-4 on every NDP reduction step including several purine superpathways; fine for the complex, but the GO-CAM conversion of PWY-7222-1 uses GO:0106387 (GMP) as the process.
