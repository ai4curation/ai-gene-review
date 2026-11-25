# dfg10 (SPAC7D4.09c; UniProt O14264) notes

## Naming trap
- UniProt still calls O14264 "Uncharacterized protein C7D4.09c" with no gene name; dfg10 is the PomBase symbol. `just fetch-gene SCHPO dfg10` failed; fetched with `-u O14264`.

## Evidence
- [UniProt:O14264 "SIMILARITY: Belongs to the steroid 5-alpha reductase family."]; [UniProt:O14264 "InterPro; IPR039698; Dfg10/SRD5A3."]; [UniProt:O14264 "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"] (GFP screen, PMID:16823372); 5 TM helices.
- No S. pombe experimental study. Orthologs: [PMID:38821050 "The SRD5A3 yeast orthologue Dfg10 also shows activity on polyprenal but not on polyprenol."]; [PMID:38821050 "We first measured polyisoprenoid levels from Dfg10-deficient yeast, and noted a 4-fold decrease in dolichol, accompanied by a 36-fold increase in polyprenol and a 45-fold increase in polyprenal"]; [PMID:20637498 "we detected a 70% decrease in dolichol in the dfg10–100 mutant compared to the wt yeast from the same background"].

## GO-CAM
- PomBase 671ae02600003548: dfg10 enables GO:0160198, occurs_in ER membrane, part_of GO:0043048 (ISO from SRD5A3). Agrees. Model lacks the DHRSX/TDA5-type flanking steps.

## Decisions
- lipid metabolic process -> MODIFY GO:0043048; CH-CH oxidoreductase -> MODIFY GO:0160198 (both as in S. cerevisiae DFG10 review).
- dolichol-linked oligosaccharide biosynthetic process IBA non-core.
