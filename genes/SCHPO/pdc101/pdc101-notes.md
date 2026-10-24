# pdc101 (SPAC1F8.07c, UniProt Q92345, PDC2_SCHPO) notes

## Naming trap
- Fission-yeast pdc1 is an mRNA decapping scaffold (SPAC4F10.01), hence the pdc101/102/201/202 names [PMID:25102102 "Since the gene name pdc1 has been already used for mRNA decapping scaffold protein (SPAC4F10.01) [24], we propose to name the paralogs as pdc101(SPAC1F8.07c), pdc102(SPAC186.09), pdc201(SPAC3G9.11c), and pdc202(SPAC13A11.06)"].
- UniProt entry names do not follow the gene numbers: pdc101 = PDC2_SCHPO, pdc102 = PDC3_SCHPO, pdc201 = PDC4_SCHPO, pdc202 = PDC1_SCHPO.

## Evidence
- Main growth-phase isozyme [PMID:25102102 "Therefore, Pdc101 is most likely the primary pyruvate decarboxylase that supports exponential growth."]; not Phx1-dependent.
- Probably essential [PMID:25102102 "We were not able to obtain a Δpdc101 mutant, consistent with the prediction that this gene is essential"].
- Abundant protein [PMID:25102102 "Pdc101 is expressed at ~500,000 copies per cell during growth"].
- Phylogeny: separate clade from ScPdc1/5/6 [PMID:25102102 "Pdc101 and Pdc102 clustered closely in a separate clade, along with PDCs of N. crassa and A. fumigatus and four PDC proteins from plant kingdom"]. PANTHER PTHR43452:SF1.
- No purified-enzyme data; activity rests on conserved active site and IBA.

## GO-CAM
- gomodel:678073a900000393: pdc101 enables GO:0004737, part_of GO:0019660 pyruvate fermentation (generic; curator comment says fermentation terms to be refined, go-ontology issue 29511). Acetaldehyde in the model feeds both adh1 (ethanol) and atd1 (acetate, GO:0019654).

## Review decisions
- Generic root/parent MFs MODIFY -> GO:0004737; all else ACCEPT. Core BP = GO:0019660 to follow PomBase (differs from ScPDC1 core, which uses GO:0019655).
