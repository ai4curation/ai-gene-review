# aro4 (putative DAHP synthase, UniProt Q09755, SPAC24H6.10c) - notes

## Identity / NAMING TRAP
- PomBase names SPAC24H6.10c **aro4** (PomBase API product "phospho-2-dehydro-3-deoxyheptonate aldolase Aro4"); UniProt Q09755 has no gene name, only ORFNames=SPAC24H6.10c, and RecName "Putative phospho-2-dehydro-3-deoxyheptonate aldolase" [UniProt:Q09755]. UniProt's "aro4" (Q9UT09) is PomBase aro3. Always key on the accession.
- PANTHER subfamily PTHR21225:SF12 (label "...TYROSINE-INHIBITED") vs SF19 for aro3, i.e. the two S. pombe paralogs sit in different PANTHER subfamilies; neither maps cleanly onto S. cerevisiae ARO3 (Phe-inhibited) or ARO4 (Tyr-inhibited).

## Function
- Class-I DAHP synthase (EC 2.5.1.54) by homology: "Reaction=D-erythrose 4-phosphate + phosphoenolpyruvate + H2O = 7-" [UniProt:Q09755]; step 1/7 of chorismate biosynthesis.
- No experimental data; UniProt itself flags the activity as putative.

## Localization
- Cytosol and nucleus HDA from the ORFeome screen [PMID:16823372].

## GO-CAM
- gomodel:67369e7600004623: SPAC24H6.10c enables GO:0003849, occurs_in cytosol, part_of GO:0009423 (IBA). Consistent.
