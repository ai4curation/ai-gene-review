# IMD4 (YML056C, UniProt P50094) notes

## Function
- IMPDH, EC 1.1.1.205: "Reaction=IMP + NAD(+) + H2O = XMP + NADH + H(+)" [UniProt:P50094 (HAMAP)].
- Family genetics: "The simultaneous deletion of all four IMD genes was lethal unless growth media were supplemented with guanine." and "Although neither IMD3 nor IMD4 could confer drug resistance to cells lacking IMD2, either alone was sufficient to confer guanine prototrophy." [PMID:12746440]
- MPA-trapped intermediate formed in vivo by Imd2, Imd3 and Imd4; "the family of polypeptides coassemble to form heteromeric IMPDH complexes, suggesting that they form mixed tetramers" [PMID:15292516].
- mRNA cross-linking hit (HDA) [PMID:23222640]; cytoplasm [PMID:14562095].

## Pathway
- YeastPathways IMP-DEHYDROG-RXN (IMD2/3/4) in DENOVOPURINE2/3, PRPP-PWY-1, PWY-6125, PWY-7221, PWY3O-285. Superpathway inflation: PRPP-PWY-1 -> "nucleotide biosynthetic process" (MODIFY to GO:0006177); PWY3O-285 -> "purine-containing compound salvage" (MARK_AS_OVER_ANNOTATED, IMPDH is not a salvage step).
- GO-CAM: YeastPathways models only (cytosol default).

## Decisions
- Core MF GO:0003938; BP GO:0006177; cytoplasm.
- REMOVE 5 protein binding rows (Imd3; reflect heterotetramers).
- MODIFY catalytic activity / oxidoreductase -> GO:0003938.
