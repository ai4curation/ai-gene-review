# mcpS (PP_4658, Q88E10) notes

## 2026-11-03 re-review
- Deep research: `just deep-research PSEPK mcpS --provider perplexity` failed (provider 'perplexity' not available); `just mod-description-deep-research` skipped (no MOD provider configured for PSEPK). Existing falcon report used; every falcon quote was checked as a verbatim substring.
- UniProt quotes now cite the local flat file (file:PSEPK/mcpS/mcpS-uniprot.txt). ARBA-only, imported (ECO:0000313), DE-name and DR GO lines are not used as support.
- Replaced truncated quote fragments ("Malate, succinate,", "McpS as the specific chemoreceptor for 6") with complete sentences [PMID:20498372 "We report the identification of McpS as the specific chemoreceptor for 6 tricarboxylic acid (TCA) cycle intermediates and butyrate in Pseudomonas putida."] [PMID:20498372 "The analysis of the bacterial mutant deficient in mcpS and complementation assays demonstrate that McpS is the only chemoreceptor of TCA cycle intermediates in the strain under study."].
- GO:0007165 signal transduction: KEEP_AS_NON_CORE -> MODIFY to GO:0007166 cell surface receptor signaling pathway; GO:0016020 membrane: MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0005886 (both aligned with E. coli Tar). GO:0004888 (module MF), GO:0005886, GO:0006935 ACCEPT.
- Description rewritten as a standalone summary (topology, HBM LBD, ligands, CheR2 methylation). Status COMPLETE.


## Taxon/module audit, 2026-11-06

The old exclusivity claim is outdated. McpS ligand specificity is retained; the primary McpQ study resolves the apparent conflict. PMID:23112148 directly supports malate/succinate versus acetate binding in different modules. No standalone ligand-binding GO rows are added because receptor signaling already captures this integrated function.

Source anchor: [PMID:26463109 "We show here that the McpS paralogue McpQ recognizes specifically citrate and citrate/metal2+ complexes."]

All existing annotations were reassessed. Machine annotation fields, inherited NEW rows, UniProt/GOA files and provider reports were preserved. No new annotation rows were added; unchanged actions reflect retained biological judgments, not skipped review. Existing provider/manual research was consulted; this focused audit creates no provider-authored report. Current ontology definitions and primary literature take precedence over module completeness.
