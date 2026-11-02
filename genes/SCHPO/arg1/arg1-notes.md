# arg1 (SPCC777.09c, UniProt O74548) notes

## Naming trap
- S. pombe arg1 = acetylornithine aminotransferase (ortholog of S. cerevisiae ARG8). S. cerevisiae ARG1 (argininosuccinate synthase) = S. pombe arg12.

## Identity / activity
- [UniProt:O74548 "RecName: Full=Probable acetylornithine aminotransferase, mitochondrial;"], class-III PLP aminotransferase, PTHR11986:SF79; activity by similarity [UniProt:O74548 "Reaction=N(2)-acetyl-L-ornithine + 2-oxoglutarate = N-acetyl-L-"].
- Matrix location by similarity (transit peptide predicted) [UniProt:O74548 "SUBCELLULAR LOCATION: Mitochondrion matrix {ECO:0000250}."].

## Genetics
- Mercier & Labbe 2010: [PMID:20435771 "which encodes an acetylornithine aminotransferase essential to mitochondrial ornithine production"]; [PMID:20435771 "The arginine auxotrophy of the arg1Δ and arg1Δ car1Δ car3Δ strains was validated by their inability to grow on arginine-free minimal medium"]. arg1 car1 car3 lose all ornithine; matters for ferrichrome under iron starvation.
- Ma et al. 2007 marker screen: [PMID:17622533 "New alleles of arg1 (+), lys3 (+) and met6 (+) were"].
- Deletion screen PMID:32896087 (EXP).

## Decisions
- urea cycle EXP (PMID:20435771) MARK_AS_OVER_ANNOTATED: aminotransferase is upstream of ornithine, not a urea-cycle reaction.
- Did not add GO:0006592 (ornithine biosynthesis) as NEW; ARG8 carries it as TAS but PomBase did not annotate it.
- Core: GO:0003992, GO:0006526, mitochondrial matrix (= ARG8 core minus the ornithine BP).


## 2026-10-26 systematic fungal annotation audit

Reviewed all 13 existing rows and the core functions with the review and annotation-reviewer workflows. Preserved every machine-sourced term, evidence code, qualifier, source identifier, WITH/FROM entry and row order. No new annotations were added in this audit.

The acetylornithine aminotransferase lies upstream of ornithine entry into the urea-cycle topology. Its process annotation is refined to arginine biosynthesis rather than retained as urea-cycle participation. PMID:20435771 native genetics and amino-acid requirements support the biosynthetic role; necessity is considered together with the inherited enzyme chemistry.

Live GO:0000050 describes ornithine-to-arginine synthesis followed by arginine cleavage to urea and regenerated ornithine; it does not require ureotelic nitrogen excretion. PMID:20435771 directly measures S. pombe Car1/Car3 arginase-dependent urea production, and PMID:18849471 explicitly places OTC in the urea-cycle segment. Existing OTC/ASS/ASL rows are retained as non-core participation in this reaction topology, without asserting net full-cycle flux or universal simultaneous operation. The upstream acetylornithine-producing Arg1 is treated separately.

Normal publication caching completed. Normal Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota failures prevented a generated report. Manual review used the actual cached primary sources and curated UniProt, and no provider-named research file was fabricated. Per-gene attempts and validation logs are in `.cache/module-audit-logs/arginine-SCHPO-arg1-*`. Abstract-only or bibliographic-only sources are distinguished from full text in reference reviews; unavailable source details are not treated as experimental refutations.

Actions: ACCEPT 10, MODIFY 3. Record sections were backfilled; focused schema/reference validation passed on the initial complete panel. Final targeted checks and HTML rendering are recorded in the audit logs.

Final quote QA replaced a UniProt protein-name quotation with curated aminotransferase-family membership; the primary PMID:20435771 support remains.
