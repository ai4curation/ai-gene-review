# CPA1 (YOR303W, P07258) notes

Evidence journal built from UniProt and cached abstracts.

- Small (glutamine amidotransferase, CarA-family) subunit of arginine-specific CPSase A; "binds and cleaves glutamine to supply the large subunit with the substrate ammonia" [UniProt:P07258].
- Two-component enzyme: [PMID:206535 "The enzyme is an aggregate consisting of two protein components, coded for by the unlinked genes cpaI and cpaII."]; [PMID:206535 "The small component was required in addition to the large one for the physiologically functional glutamine-dependent activity."]; [PMID:206652 "a light subunit conferring upon the holoenzyme the ability to utilize glutamine"].
- Subunit roles: [PMID:8626695 "with a 45-kDa CPA1 subunit binding and cleaving glutamine, and a 124-kDa CPA2 subunit accepting the ammonia moiety cleaved from glutamine"].
- Catalytic residues: [PMID:9290206 "implicate residues Cys 264 and His 349 in the glutaminase catalytic activity, and His 307 in the binding of glutamine to the active site."]; the mutants cannot grow on minimal medium [PMID:9290206].
- Location: cytoplasm/soluble [PMID:205532 "arginine pathway-specific carbamoylphosphate synthetase, ornithine carbamoyltransferase, argininosuccinate synthetase, and argininosuccinate lyase"] (soluble fraction); UniProt: in S. cerevisiae the two CPSases "appear to contribute to the formation of a single cellular pool of carbamoyl phosphate", unlike S. pombe/Neurospora where the arginine CPSase is mitochondrial [UniProt:P07258].
- Regulation: repressed by arginine [UniProt:P07258].

## Curation decisions
- GO:0004088 rows: IBA/IDA/IMP/RCA use contributes_to (correct); EXP/IEA rows use enables (slightly loose for a subunit) - accepted, deferring to curators.
- Core MF: glutaminase activity (GO:0004359), contributes_to GO:0004088, in CPSase complex (GO:0005951), cytosol, arginine biosynthesis.
- de novo pyrimidine nucleobase (IEA InterPro) -> MARK_AS_OVER_ANNOTATED (paralog specialisation: URA2 is pyrimidine CPSase). Pyrimidine nucleotide biosynthesis IDA -> KEEP_AS_NON_CORE (shared CP pool).
- Stress granule HDA -> KEEP_AS_NON_CORE.
