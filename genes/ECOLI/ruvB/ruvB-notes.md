# ruvB (E. coli K-12, P0A812) curation notes

Reviewed by Claude (AI-assisted) as the E. coli exemplar and PAINT seed (PTN000349951) for the RuvB step of `modules/bacterial_ruvabc_holliday_junction_processing.yaml`.

- Provider deep research was not run (no provider API keys in this session); the review rests on UniProt and cached publications.
- RuvB is the hexameric AAA+ motor [PMID:9047358, "The results suggest a model for branch migration in which DNA is pumped out of the small end of each ring as ATP is hydrolyzed"].
- GO:0000400 is kept as non-core: RuvB binds junction DNA, but RuvA provides specificity [UniProtKB:P0A812, "RuvA gives specificity by binding to cruciform junctions, while the RuvB ATPase provides the motor force for branch migration"].
- GO:0003678 (IDA, PMID:8433990) is TOO_GENERAL against the accepted GO:0009378.
- RuvB-Cas1 (YgbT) co-purification [PMID:21219465] is real but is bare protein binding and was removed per policy.
