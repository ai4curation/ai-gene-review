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


## 2026-10-26 systematic fungal annotation audit

Reviewed all 31 existing rows and the core functions with the review and annotation-reviewer workflows. Preserved every machine-sourced term, evidence code, qualifier, source identifier, WITH/FROM entry and row order. No new annotations were added in this audit.

The small CPSase subunit hydrolyzes glutamine and contributes to whole-complex carbamoyl-phosphate synthesis; it is not assigned autonomous whole-complex catalysis in the core. PMID:8626695, 206535 and 9290206 distinguish subunit reactions and catalytic residues. Secondary pyrimidine participation is retained consistently with shared carbamoyl-phosphate pools in budding yeast. PMID:26777405 was force-fetched to full main text and read; supplementary CPA1 identification remained inaccessible after direct download attempts. Stress-granule localization is therefore UNDECIDED, not dismissed as contamination. The HDA cytoplasm claim is refined using independent localization evidence.

Normal publication caching completed. Normal Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota failures prevented a generated report. Manual review used the actual cached primary sources and curated UniProt, and no provider-named research file was fabricated. Per-gene attempts and validation logs are in `.cache/module-audit-logs/arginine-yeast-CPA1-*`. Abstract-only or bibliographic-only sources are distinguished from full text in reference reviews; unavailable source details are not treated as experimental refutations.

Actions: ACCEPT 20, KEEP_AS_NON_CORE 2, MODIFY 8, UNDECIDED 1. Record sections were backfilled; focused schema/reference validation passed on the initial complete panel. Final targeted checks and HTML rendering are recorded in the audit logs.
