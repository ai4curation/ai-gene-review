# pcaY (PP_2643, Q88JK6) notes

## 2026-11-03 re-review
- Deep research: `just deep-research PSEPK pcaY --provider perplexity` failed (provider 'perplexity' not available); `just mod-description-deep-research` skipped (no MOD provider configured for PSEPK). Existing falcon report used; every falcon quote was checked as a verbatim substring.
- UniProt quotes now cite the local flat file (file:PSEPK/pcaY/pcaY-uniprot.txt). ARBA-only, imported (ECO:0000313), DE-name and DR GO lines are not used as support.
- Completed truncated quotes; replaced a paper-title quote (PMID:33021055) with an abstract result [PMID:33021055 "The domain formed a four-helix bundle (4HB), and both ligand binding sites of the dimer were occupied with the high-affinity ligands protocatechuate and quinate"]; removed quotes attached to GO_REF entries.
- Key evidence [PMID:28620365 "Mutation of the pcaY_PP gene abolished chemotaxis to these compounds; phenotype that was restored following gene complementation."].
- GO:0007165 -> MODIFY GO:0007166; GO:0016020 -> MODIFY GO:0005886 (aligned with E. coli Tar). GO:0004888 (module MF), GO:0005886, GO:0006935 ACCEPT. Status COMPLETE.
