# tar (P07017, MCP-II, aspartate/maltose chemoreceptor) — review notes

## 2026-11-03 session

### Deep research
- `just deep-research ECOLI tar --provider perplexity` failed: "Provider 'perplexity' not available. Available: falcon, openscientist, claude_code" (no agentapi / API keys). Not retried.
- `just mod-description-deep-research ECOLI tar`: skipped, "no MOD provider configured for organism 'ECOLI'".
- Tried Europe PMC / NCBI PMC full text for PMC2593199 (PMID:18931127), PMC3111312 (PMID:21606342), PMC52936 (PMID:1660136): Europe PMC returned HTTP 500; NCBI efetch says the publisher does not allow full-text download. All GOA papers except PMID:19547746 are abstract-only in the cache.

### Evidence summary (provenance)
- Receptor activity: [file:ECOLI/tar/tar-uniprot.txt "Receptor for the attractant L-aspartate and related amino and dicarboxylic acids."]; transmembrane signaling [PMID:1660136 "The ability of an 18-18' cross-linked dimer to transmit an aspartate-induced transmembrane signal is also supportive of such an extended helix."]
- Genetics: [PMID:333433 "responses to a complementary set of stimuli are defective in tar mutants"]; [PMID:333434 "CheM(-) mutants show chemotaxis toward some attractants (Tar(-) phenotype)"]
- Membrane: [PMID:334749 "The motA, motB, cheM, and cheD gene products were found to be confined exclusively to the inner cytoplasmic membrane fraction"]
- Ternary complex: [PMID:1326408 "Receptor directly bound CheW, but receptor-CheA binding was dependent upon the presence of CheW."]; core unit [PMID:21606342 "Purified complexes contained two receptor trimers of dimers and two CheW for each CheA dimer"]
- Polar arrays: [PMID:19547746 "Consistent with previous studies [4],[17],[40],[41], the largest clusters are found predominantly at cell poles."]
- Adaptational assistance: [PMID:15916610 "Using membrane vesicles containing both high-abundance receptor Tar and low-abundance receptor Trg, we observed effective assistance in vitro for all three adaptational modifications: methylation, demethylation and deamidation."]

### Decisions
- Module MF GO:0004888 transmembrane signaling receptor activity: SUPPORTED (IBA, IEA, IMP rows accepted; core function).
- 6 bare GO:0005515 rows: 5 REMOVE (CheW partners; Y2H/pull-down screens), 1 MODIFY (PMID:21606342, CheA) to GO:0043424 protein histidine kinase binding.
- GO:0007165 signal transduction (IEA) -> MODIFY to GO:0007166 cell surface receptor signaling pathway (definition: initiated by an extracellular ligand binding a cell-surface receptor). Note: the KT2440 MCP reviews (mcpS, pcaY) used KEEP_AS_NON_CORE for this row at the time of writing; correct-but-general rule favours MODIFY.
- GO:0016020 membrane -> MODIFY to GO:0005886 plasma membrane.
- GO:0035556 intracellular signal transduction (IMP, PMID:15916610) -> MARK_AS_OVER_ANNOTATED (paper measures adaptational modification assistance, not intracellular signal relay).
- GO:0042802 identical protein binding -> MODIFY to GO:0042803; homodimerization, homooligomerization and histidine kinase binding kept as non-core.
- PMID:18931127 is Tsr-focused and abstract-only; its Tar rows were accepted/kept deferring to the curator, as all the claims are well established for Tar.
- Phosphorelay (GO:0000160) not added: Tar controls CheA but is not itself a phosphorelay participant; no row exists and none proposed.
- No NEW rows. Considered GO:0070335 aspartate binding (ligand-binding domain structures exist, PMID:15299315, 9315712) but not cached; raised as a suggested question instead.


## 2026-11-06 taxonomic module audit

Refined the intracellular-signaling row to the chemotaxis phosphorelay using the independent receptor-controlled CheA assay (PMID1326408), instead of rejecting the claim because its original adaptation paper is abstract-only. Retained the ligand-specific E. coli receptor core and all other actions.

Reviewed all existing rows, references and core functions. Current PAINT-loss checks found no IRD or IKR on this target lineage. A normal Falcon research attempt failed with HTTP 403 authentication; no provider report was fabricated or overwritten. Existing source payloads, raw files and inherited NEW rows are preserved; no new annotation rows were added. Comparative scope was checked against the full text of PMID33684668: the E. coli ligand-response direction and optional adaptation/termination components are not universal.
