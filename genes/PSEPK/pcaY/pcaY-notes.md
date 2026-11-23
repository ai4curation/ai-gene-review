# pcaY (PP_2643, Q88JK6) notes

## 2026-11-03 re-review
- Deep research: `just deep-research PSEPK pcaY --provider perplexity` failed (provider 'perplexity' not available); `just mod-description-deep-research` skipped (no MOD provider configured for PSEPK). Existing falcon report used; every falcon quote was checked as a verbatim substring.
- UniProt quotes now cite the local flat file (file:PSEPK/pcaY/pcaY-uniprot.txt). ARBA-only, imported (ECO:0000313), DE-name and DR GO lines are not used as support.
- Completed truncated quotes; replaced a paper-title quote (PMID:33021055) with an abstract result [PMID:33021055 "The domain formed a four-helix bundle (4HB), and both ligand binding sites of the dimer were occupied with the high-affinity ligands protocatechuate and quinate"]; removed quotes attached to GO_REF entries.
- Key evidence [PMID:28620365 "Mutation of the pcaY_PP gene abolished chemotaxis to these compounds; phenotype that was restored following gene complementation."].
- GO:0007165 -> MODIFY GO:0007166; GO:0016020 -> MODIFY GO:0005886 (aligned with E. coli Tar). GO:0004888 (module MF), GO:0005886, GO:0006935 ACCEPT. Status COMPLETE.


## Taxon/module audit, 2026-11-06

PcaY_PP is PP_2643 in KT2440. Direct LBD binding plus mutant/complementation supports the receptor and chemotaxis calls. Quinate and shikimate are non-aromatic cyclic ligands, so the core wording now matches the broader description. No gene-participation claim in catabolism is inferred from sensing these metabolites.

Source anchor: [PMID:28620365 "Tightest binding compounds were quinate, shikimate, 3-dehydroshikimate and protocatechuate, which are at the interception of the biosynthetic shikimate and catabolic quinate pathways."]

All existing annotations were reassessed. Machine annotation fields, inherited NEW rows, UniProt/GOA files and provider reports were preserved. No new annotation rows were added; unchanged actions reflect retained biological judgments, not skipped review. Existing provider/manual research was consulted; this focused audit creates no provider-authored report. Current ontology definitions and primary literature take precedence over module completeness.
