# STR2 (YJR130C) notes

## Identity
- Cystathionine gamma-synthase (Str2p, "sulfur transfer protein 2"), PLP-dependent, trans-sulfuration enzyme family, MET7 subfamily [UniProt:P47164].
- UniProt describes the reaction with O-succinyl-L-homoserine (EC 2.5.1.48, RHEA:20397) by analogy; in S. cerevisiae the homoserine ester made by Met2p is O-acetyl-L-homoserine, and YeastPathways writes the reaction as L-cysteine + O-acetyl-L-homoserine -> L-cystathionine + acetate (no EC). GO:0003962 is defined on the O-succinyl substrate; GO has no O-acetylhomoserine-specific CGS term (QuickGO search, 2026-10). The substrate specificity of Str2p has not been measured biochemically.

## Evidence
- Genetic: disruption of YJR130c (STR2) or YGL184c (STR3) gives strains that cannot convert cysteine into homocysteine [PMID:10821189 "Two genes that presumably encode cystathionine gamma-synthase and cystathionine beta-lyase were identified by genetic disruption (ORFs YJR130c and YGL184c), yielding yeast strains that cannot convert cysteine into homocysteine."].
- Disruption phenotype: growth defect on cysteine or glutathione as sole sulfur source [UniProt:P47164 "DISRUPTION PHENOTYPE: Leads to a clear growth defect on medium"].
- Localization: cytoplasm and nucleus in the global GFP screen [UniProt:P47164 "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:14562095}. Nucleus"].

## Pathway context
- STR2/STR3 form the forward (cysteine -> homocysteine) transsulfuration route; CYS4/CYS3 form the reverse route. The main de novo homocysteine route in yeast is direct sulfhydrylation by Met17p, so STR2 matters mainly when sulfur is supplied as cysteine/GSH.
- GO:0019346 transsulfuration is obsolete; QuickGO 'consider' replacements are GO:0071269 L-homocysteine biosynthetic process and GO:0019344 L-cysteine biosynthetic process. For STR2 the direction is homocysteine synthesis (GO:0071269).
