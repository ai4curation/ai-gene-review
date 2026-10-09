# tea (E1JH25) curation notes

- Discovered in [PMID:27835648 "Here we discover a novel protein, Tea, that is specifically enriched at telomeres to prevent telomere fusion"]; [PMID:27835648 "Tea recruits Ver and Moi to telomeres, and point mutations disrupting MTV interaction in vitro result in telomere uncapping"]; MTV binds ssDNA.
- Only 7 GOA rows; complex membership missing from GOA -> added NEW part_of GO:0000783 for consistency with moi/ver. No NEW capping BP added, because the carried GO:0031848 is already a descendant of GO:0016233.
- Same location convention as other terminin subunits.
- Falcon deep research (late): tea RNAi/mutants give ~6.7 fusions per nucleus, rescued by a genomic transgene; recruitment hierarchy HOAP -> Tea -> Moi/Ver; MTV binds ssDNA (not dsDNA) and protects it from ExoI.
- Review-bot round: core BP set to the carried GO:0031848 rather than adding NEW GO:0016233, since GO:0016233 is an ancestor of the carried term (CLAUDE.md: reject ancestor NEW terms).
- Review-bot round 2: added NEW contributes_to GO:0043047 (IDA, PMID:27835648) so the core MF has a row.
