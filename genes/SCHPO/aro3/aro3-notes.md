# aro3 (DAHP synthase, UniProt Q9UT09, SPAP8A3.07c) - notes

## Identity / NAMING TRAP
- PomBase names SPAP8A3.07c **aro3** (product "phospho-2-dehydro-3-deoxyheptonate aldolase Aro3", PomBase API), but UniProt Q9UT09 carries Name=aro4 [UniProt:Q9UT09 "GN   Name=aro4; ORFNames=SPAP8A3.07c;"]. GOA (QuickGO) rows for Q9UT09 also use symbol "aro4". The other paralog, SPAC24H6.10c (Q09755), has no UniProt gene name and is PomBase **aro4**.
- The S. pombe names do not map one-to-one to S. cerevisiae ARO3 (Phe-inhibited) / ARO4 (Tyr-inhibited). UniProt calls Q9UT09 "Phospho-2-dehydro-3-deoxyheptonate aldolase, tyrosine-inhibited" and PANTHER places it in PTHR21225:SF19 ("...TYROSINE-INHIBITED"), but no S. pombe feedback-inhibition data were found.

## Function
- Class-I DAHP synthase, EC 2.5.1.54: "Reaction=D-erythrose 4-phosphate + phosphoenolpyruvate + H2O = 7-" [UniProt:Q9UT09]; step 1/7 of chorismate biosynthesis [UniProt:Q9UT09].
- No S. pombe enzymology; function by homology to S. cerevisiae ARO3/ARO4 and PAINT node PTN000476971.

## Localization
- Cytoplasm and nucleus in the ORFeome screen [PMID:16823372] (HDA cytosol + nucleus).

## GO-CAM
- gomodel:67369e7600004623 (PomBase aromatic amino acid biosynthesis): SPAP8A3.07c enables GO:0003849, occurs_in cytosol, part_of GO:0009423. Consistent.
