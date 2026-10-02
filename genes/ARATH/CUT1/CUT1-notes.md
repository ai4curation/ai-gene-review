# CUT1 (CER6/KCS6; At1g68530; Q9XF43) review notes

## Identity and function
- CUT1 = CER6 = KCS6, a FAE1-type 3-ketoacyl-CoA synthase (condensing enzyme) of the ER VLCFA elongase [PMID:11041893 "segregation analysis showed that CER6 is identical to CUT1"].
- Required for wax production; suppression gives waxless stems with wax at 6-7% of WT and conditional male sterility [PMID:10330468 "the stem wax load was reduced to 6 to 7% of wild-type levels"].
- Chain length: C24 components accumulate in suppressed plants [PMID:10330468 "suggesting that CUT1 is required for elongation of C24 VLCFAs"]; in yeast KCS6 elongates C22 to C24-C28 [PMID:36798704 "KCS5 and KCS6, which share 88% identity, led to the elongation of C22 into C24 up to C28 compounds"].
- Major condensing enzyme for stem wax and pollen coat lipids [PMID:12177469 "these data implicate CER6 as the major condensing enzyme for stem wax and pollen coat lipid biosynthesis"].
- Expression: epidermis, tapetum; light required, ABA/osmotic stress enhance [PMID:12177469 "light is essential for CER6 transcription"].
- Localization: ER [PMID:36798704 "The 21 Arabidopsis KCSs localize in the endoplasmic reticulum of tobacco cells."].
- Falcon deep research (file:ARATH/CUT1/CUT1-deep-research-falcon.md) agrees; notes CER2/CER26 accessory proteins extend elongation beyond C28.

## GO term check
- GO:0009922 "fatty acid elongase activity" is now defined as the condensation step (very-long-chain acyl-CoA + malonyl-CoA -> 3-oxoacyl-CoA), i.e. exactly the KCS reaction (checked in local go.db).

## Decisions
- ACCEPT: MF (EXP/IBA/IEA), ER/ER membrane (all), VLCFA metabolic (IBA, IDA), wax biosynthesis (IMP), general IEA parents.
- KEEP_AS_NON_CORE: response to cold (x2 IEP), response to light (IEP), unidimensional cell growth (IMP; indirect via VLCFA/ethylene, PMID:17993622), cutin-based cuticle development.
- MARK_AS_OVER_ANNOTATED: cytoplasm (ISM), mitochondrion (HDA, PMID:28887381 high-throughput co-fractionation).
- No NEW terms. Core function uses GO:0042761 and GO:0009923 (validator warns they are not in GOA; kept as they are accurate).
- Note: UniProt says CER6 is down-regulated by low temperature (PMID:18465198), whereas PMID:41718707 reports cold induction of KCSs (unnamed in abstract); both kept as non-core IEP.
